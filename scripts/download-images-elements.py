#!/usr/bin/env python3
"""
download-images-elements.py
For every Hugo element (content/ca/elements/*.md) without a `foto:` field,
find the element's page on the live WordPress site, pick the building photo
(skipping category icons / book covers), download it into
static/img/elements/<slug>.<ext>, and set `foto: /img/elements/<slug>.<ext>`
in the element's front matter.

Reuses find_wp_url() and scrape_wp_page() from sync_elements_wp.py so the
WP→Hugo matching logic (publicacio -> category -> slug URL) stays in one place.

Safe to run multiple times (idempotent):
  - Skips elements that already have `foto:` set.
  - Skips downloading if the target image file already exists on disk.

Usage:
  pip install requests python-frontmatter beautifulsoup4
  python3 scripts/download-images-elements.py [--limit N] [--dry-run] [--local]
  python3 scripts/download-images-elements.py --local --batch-size 15 --batch-pause 120
"""

import argparse
import logging
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
from sync_elements_wp import find_wp_url, scrape_wp_page, get_url, REQUEST_DELAY, set_local_mode  # noqa: E402

try:
    import frontmatter
except ImportError:
    sys.exit("Missing 'python-frontmatter'. Run: pip install python-frontmatter")

ELEMENTS_DIR = Path(__file__).parent.parent / "content" / "ca" / "elements"
IMG_DIR = Path(__file__).parent.parent / "static" / "img" / "elements"
REPORT_FILE = Path(__file__).parent / "download_images_report.md"

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)


def guess_ext(url: str) -> str:
    path = urlparse(url).path
    ext = Path(path).suffix.lower()
    if ext in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        return ".jpg" if ext == ".jpeg" else ext
    return ".jpg"


def download_image(url: str, dest: Path) -> bool:
    r = get_url(url)
    if r is None or r.status_code != 200 or not r.content:
        return False
    dest.write_bytes(r.content)
    return True


THUMB_SUFFIX = re.compile(r"-\d+x\d+(\.\w+)$")


def prefer_fullsize(url: str) -> str:
    """WP thumbnails look like name-300x300.jpg; the original name.jpg is usually
    higher resolution. Try it; fall back to the thumbnail if it 404s."""
    m = THUMB_SUFFIX.search(url)
    if not m:
        return url
    fullsize = THUMB_SUFFIX.sub(m.group(1), url)
    r = get_url(fullsize)
    if r is not None and r.status_code == 200 and r.content:
        return fullsize
    return url


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="Process at most N elements (for testing)")
    ap.add_argument("--dry-run", action="store_true", help="Don't write files, just report what would happen")
    ap.add_argument("--local", action="store_true", help="Run via 127.0.0.1 to bypass WP Cerber (run on server)")
    ap.add_argument("--batch-size", type=int, default=15, help="Images per batch before pausing (default: 15)")
    ap.add_argument("--batch-pause", type=int, default=120, help="Pause between batches in seconds (default: 120)")
    args = ap.parse_args()

    if args.local:
        set_local_mode(True)
        log.info("LOCAL MODE: requests via 127.0.0.1 with Host header (bypass WP Cerber)")

    IMG_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(ELEMENTS_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != "_index.md"]

    pending = []
    for md_path in md_files:
        post = frontmatter.load(str(md_path))
        if not post.metadata.get("foto"):
            pending.append(md_path)

    log.info(f"{len(md_files)} total elements, {len(pending)} missing `foto:`")

    if args.limit:
        pending = pending[: args.limit]
        log.info(f"Limiting to first {len(pending)} for this run")

    stats = {"downloaded": 0, "no_image_found": 0, "not_found_on_wp": 0, "errors": 0}
    report = {"downloaded": [], "no_image": [], "not_found": [], "errors": []}
    batch_downloaded = 0

    for idx, md_path in enumerate(pending, 1):
        slug = md_path.stem
        post = frontmatter.load(str(md_path))
        meta = post.metadata
        publicacions = meta.get("publicacions", [])

        found = find_wp_url(slug, publicacions)
        if not found:
            log.warning(f"NOT FOUND on WP: {slug}")
            stats["not_found_on_wp"] += 1
            report["not_found"].append(f"- `{slug}` (publicacions: {publicacions})")
            continue

        wp_url, _category = found
        scraped = scrape_wp_page(wp_url)
        time.sleep(REQUEST_DELAY)

        if scraped is None:
            stats["errors"] += 1
            report["errors"].append(f"- `{slug}`: scrape failed ({wp_url})")
            continue

        foto_url = scraped["_raw_fields"].get("_possible_foto")
        if not foto_url:
            stats["no_image_found"] += 1
            report["no_image"].append(f"- `{slug}`: no building photo found on {wp_url}")
            continue

        foto_url = prefer_fullsize(foto_url)
        time.sleep(REQUEST_DELAY)
        ext = guess_ext(foto_url)
        dest = IMG_DIR / f"{slug}{ext}"
        rel_path = f"/img/elements/{slug}{ext}"

        if args.dry_run:
            log.info(f"[DRY RUN] Would download {foto_url} -> {dest}, set foto: {rel_path}")
            stats["downloaded"] += 1
            report["downloaded"].append(f"- `{slug}`: {foto_url} -> {rel_path} (dry-run)")
            continue

        if not dest.exists():
            ok = download_image(foto_url, dest)
            if not ok:
                stats["errors"] += 1
                report["errors"].append(f"- `{slug}`: download failed ({foto_url})")
                continue

        meta["foto"] = rel_path
        post.metadata = meta
        md_path.write_text(frontmatter.dumps(post), encoding="utf-8")

        stats["downloaded"] += 1
        batch_downloaded += 1
        report["downloaded"].append(f"- `{slug}`: {foto_url} -> {rel_path}")
        log.info(f"OK {slug}: {rel_path}")

        if batch_downloaded >= args.batch_size and idx < len(pending):
            log.info(f"Batch complete ({batch_downloaded} images). Pausing {args.batch_pause}s to avoid overloading WP Cerber...")
            time.sleep(args.batch_pause)
            batch_downloaded = 0

    lines = [
        "# Image Download Report", "",
        f"| Metric | Value |", f"|---|---|",
        f"| Pending processed | {len(pending)} |",
        f"| Downloaded / foto set | {stats['downloaded']} |",
        f"| No building photo found | {stats['no_image_found']} |",
        f"| Not found on WP | {stats['not_found_on_wp']} |",
        f"| Errors | {stats['errors']} |",
        "",
    ]
    for section, title in [("downloaded", "Downloaded"), ("no_image", "No image found"),
                            ("not_found", "Not found on WP"), ("errors", "Errors")]:
        if report[section]:
            lines += [f"## {title}", ""] + report[section] + [""]

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:12]))
    print(f"\nFull report: {REPORT_FILE}")


if __name__ == "__main__":
    main()
