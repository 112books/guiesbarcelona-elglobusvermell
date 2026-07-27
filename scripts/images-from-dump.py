#!/usr/bin/env python3
"""
images-from-dump.py
Populate `foto:` on Hugo elements using the WordPress SQL dump instead of
live crawling. WP Cerber (the WP security plugin) blocks bot-like traffic to
*rendered pages* regardless of source IP or User-Agent (confirmed: even
127.0.0.1 loopback gets 403 after a burst of requests). Direct static asset
requests to /wp-content/uploads/... are served by nginx and never touch
WordPress/Cerber (confirmed 200 externally), so this script:

  1. Reads building image URLs straight out of `wp_posts.post_content` in a
     SQL dump (zero HTTP requests, zero risk of getting flagged).
  2. Matches each Hugo element to its WP post: exact slug match first, then
     a fuzzy title-normalization fallback for the ~40 elements whose Hugo
     slug doesn't match the WP post_name.
  3. Downloads ONLY the final image file directly (static path, bypasses
     Cerber) — never fetches an HTML page.

Usage:
  .venv-scripts/bin/python3 scripts/images-from-dump.py --dump sql-dumps/wp_posts-20260727.sql [--limit N] [--dry-run]
"""

import argparse
import re
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))

try:
    import frontmatter
except ImportError:
    sys.exit("Missing 'python-frontmatter'. Run: pip install python-frontmatter")

try:
    import requests
except ImportError:
    sys.exit("Missing 'requests'. Run: pip install requests")

ELEMENTS_DIR = Path(__file__).parent.parent / "content" / "ca" / "elements"
IMG_DIR = Path(__file__).parent.parent / "static" / "img" / "elements"
REPORT_FILE = Path(__file__).parent / "images_from_dump_report.md"

BOOK_COVER_KEYWORDS = [
    "203x300", "portada", "coberta", "cover", "book", "logoweb", "logo",
    "icon", "arrow", "avatar", "gatpac", "poblenou-", "jardins-203",
    "biblioteques-", "mercats-", "masies-", "barceloneta-", "marina-",
    "cob_cat", "-cob-", "_cob_",
]

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})


# ── SQL dump parsing (extended-INSERT aware, handles backslash-escaped quotes) ──

def extract_rows(sql_text: str, table: str):
    inserts = re.findall(rf"INSERT INTO `{table}` VALUES (.*?);\n", sql_text, re.DOTALL)
    rows = []
    for ins in inserts:
        i, n = 0, len(ins)
        while i < n:
            if ins[i] == '(':
                depth, j, in_str = 1, i + 1, False
                while j < n and depth > 0:
                    c = ins[j]
                    if in_str:
                        if c == '\\':
                            j += 2
                            continue
                        elif c == "'":
                            in_str = False
                    else:
                        if c == "'":
                            in_str = True
                        elif c == '(':
                            depth += 1
                        elif c == ')':
                            depth -= 1
                    j += 1
                rows.append(ins[i + 1:j - 1])
                i = j
            else:
                i += 1
    return rows


def split_fields(row: str):
    fields, cur, in_str = [], [], False
    i, n = 0, len(row)
    while i < n:
        c = row[i]
        if in_str:
            if c == '\\':
                cur.append(row[i:i + 2])
                i += 2
                continue
            elif c == "'":
                in_str = False
                cur.append(c)
            else:
                cur.append(c)
        else:
            if c == "'":
                in_str = True
                cur.append(c)
            elif c == ',':
                fields.append(''.join(cur))
                cur = []
            else:
                cur.append(c)
        i += 1
    fields.append(''.join(cur))
    return [f.strip() for f in fields]


def unquote(s: str) -> str:
    s = s.strip()
    if s.startswith("'") and s.endswith("'"):
        s = s[1:-1].replace("\\'", "'").replace('\\"', '"').replace("\\\\", "\\")
    return s


def normalize_title(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t


def load_wp_posts(dump_path: Path):
    """Returns dict: slug -> {id, title, content}, plus title-normalized index."""
    content = dump_path.read_text(encoding="utf-8", errors="ignore")
    rows = extract_rows(content, "wp_posts")
    by_slug = {}
    by_norm_title = {}
    for r in rows:
        f = split_fields(r)
        if len(f) < 23:
            continue
        status, ptype = unquote(f[7]), unquote(f[20])
        if status != "publish" or ptype != "post":
            continue
        pid = int(unquote(f[0]))
        title = unquote(f[5])
        slug = unquote(f[11])
        post_content = unquote(f[4])
        entry = {"id": pid, "title": title, "slug": slug, "content": post_content}
        by_slug[slug] = entry
        by_norm_title.setdefault(normalize_title(title), entry)
    return by_slug, by_norm_title


def find_building_image(post_content: str) -> str:
    for m in re.finditer(r'<img[^>]+src="([^"]+)"', post_content):
        src = m.group(1)
        if "/wp-content/uploads/" not in src:
            continue
        if any(kw in src.lower() for kw in BOOK_COVER_KEYWORDS):
            continue
        return src
    return ""


THUMB_SUFFIX = re.compile(r"-\d+x\d+(\.\w+)$")


def prefer_fullsize(url: str) -> str:
    m = THUMB_SUFFIX.search(url)
    if not m:
        return url
    fullsize = THUMB_SUFFIX.sub(m.group(1), url)
    try:
        r = session.head(fullsize, timeout=15, allow_redirects=True)
        if r.status_code == 200:
            return fullsize
    except requests.RequestException:
        pass
    return url


def guess_ext(url: str) -> str:
    ext = Path(urlparse(url).path).suffix.lower()
    return ".jpg" if ext in ("", ".jpeg") else ext


def download_image(url: str, dest: Path) -> bool:
    try:
        r = session.get(url, timeout=20)
    except requests.RequestException:
        return False
    if r.status_code != 200 or not r.content:
        return False
    dest.write_bytes(r.content)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True, help="Path to a SQL dump containing wp_posts")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dump_path = Path(args.dump)
    if not dump_path.exists():
        sys.exit(f"Dump not found: {dump_path}")

    print(f"Parsing {dump_path} ...")
    by_slug, by_norm_title = load_wp_posts(dump_path)
    print(f"{len(by_slug)} published WP posts loaded")

    IMG_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(p for p in ELEMENTS_DIR.glob("*.md") if p.name != "_index.md")
    pending = []
    for md_path in md_files:
        post = frontmatter.load(str(md_path))
        if not post.metadata.get("foto"):
            pending.append(md_path)

    print(f"{len(md_files)} total elements, {len(pending)} missing `foto:`")
    if args.limit:
        pending = pending[: args.limit]
        print(f"Limiting to first {len(pending)}")

    stats = {"downloaded": 0, "no_image": 0, "not_matched": 0, "errors": 0}
    report = {"downloaded": [], "no_image": [], "not_matched": [], "errors": []}

    for md_path in pending:
        slug = md_path.stem
        post = frontmatter.load(str(md_path))
        meta = post.metadata

        entry = by_slug.get(slug)
        if entry is None:
            norm = normalize_title(str(meta.get("title", slug)))
            entry = by_norm_title.get(norm)

        if entry is None:
            stats["not_matched"] += 1
            report["not_matched"].append(f"- `{slug}` (title: {meta.get('title', '')!r})")
            continue

        img_url = find_building_image(entry["content"])
        if not img_url:
            stats["no_image"] += 1
            report["no_image"].append(f"- `{slug}` (WP id {entry['id']}, {entry['slug']})")
            continue

        img_url = prefer_fullsize(img_url)
        ext = guess_ext(img_url)
        dest = IMG_DIR / f"{slug}{ext}"
        rel_path = f"/img/elements/{slug}{ext}"

        if args.dry_run:
            print(f"[DRY RUN] {slug}: {img_url} -> {rel_path}")
            stats["downloaded"] += 1
            report["downloaded"].append(f"- `{slug}`: {img_url} -> {rel_path} (dry-run)")
            continue

        if not dest.exists():
            if not download_image(img_url, dest):
                stats["errors"] += 1
                report["errors"].append(f"- `{slug}`: download failed ({img_url})")
                continue

        meta["foto"] = rel_path
        post.metadata = meta
        md_path.write_text(frontmatter.dumps(post), encoding="utf-8")
        stats["downloaded"] += 1
        report["downloaded"].append(f"- `{slug}`: {img_url} -> {rel_path}")
        print(f"OK {slug}: {rel_path}")
        time.sleep(0.3)

    lines = [
        "# Images-from-dump report", "",
        "| Metric | Value |", "|---|---|",
        f"| Pending processed | {len(pending)} |",
        f"| Downloaded / foto set | {stats['downloaded']} |",
        f"| No building photo in dump | {stats['no_image']} |",
        f"| Not matched WP post | {stats['not_matched']} |",
        f"| Errors | {stats['errors']} |",
        "",
    ]
    for key, title in [("downloaded", "Downloaded"), ("no_image", "No image in dump"),
                       ("not_matched", "Not matched to a WP post"), ("errors", "Errors")]:
        if report[key]:
            lines += [f"## {title}", ""] + report[key] + [""]

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:10]))
    print(f"\nFull report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
