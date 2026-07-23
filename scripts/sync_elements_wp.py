#!/usr/bin/env python3
"""
sync_elements_wp.py
Scrapes all fields from WordPress production site and updates Hugo element .md files.
Safe to run multiple times (idempotent).

WP HTML structure (discovered by inspection):
  - Metadata rendered as <li>Label: value</li> or <p>Label: value</p>
  - Fields: Adreça, Projecte (architect + year), Reformes, Categoria, Nivell de protecció,
    Premi, Superfície, and description paragraphs
  - NO map coordinates in WP (coordinates are only in Hugo)
  - Images: /wp-content/uploads/... (often book covers, not building photos)
"""

import os
import re
import sys
import time
import logging
from pathlib import Path
from typing import Optional
from datetime import datetime

try:
    import requests
except ImportError:
    sys.exit("Missing 'requests'. Run: pip install requests")

try:
    import frontmatter
except ImportError:
    sys.exit("Missing 'python-frontmatter'. Run: pip install python-frontmatter")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Missing 'beautifulsoup4'. Run: pip install beautifulsoup4")

# ── Configuration ─────────────────────────────────────────────────────────────

ELEMENTS_DIR = Path(__file__).parent.parent / "content" / "ca" / "elements"
REPORT_FILE  = Path(__file__).parent / "sync_report.md"
BASE_URL     = "https://guiesbarcelona.elglobusvermell.org"
REQUEST_DELAY = 0.8  # seconds between requests (be polite)
LOCAL_MODE = False   # set to True to bypass WP Cerber via 127.0.0.1

# publicacio slug → ordered list of WP category slugs to try
PUBLICACIO_TO_CATEGORIES = {
    "gatcpac":        ["avantguarda-1928-1938"],
    "50-75":          ["moderna-1950-1975"],
    "poblenou":       ["poblenou-industrial"],
    "interiors-illa": ["eixample-jardins-interiors"],
    "biblioteques":   ["biblioteques"],
    "mercats":        ["mercats"],
    "masies":         ["masies"],
    "barceloneta":    ["barceloneta"],
    "marina":         ["marina-prat-vermell"],
    "76-08":          ["1975-2008"],
    "09-25":          ["2010-2025"],
}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
log = logging.getLogger(__name__)

# ── HTTP helpers ───────────────────────────────────────────────────────────────

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 HugoSync/1.0"
})


def set_local_mode(enabled: bool = True):
    """Switch to localhost mode to bypass WP Cerber when running on the server.
    Must be called BEFORE any HTTP requests."""
    global BASE_URL, LOCAL_MODE
    LOCAL_MODE = enabled
    if enabled:
        BASE_URL = "https://127.0.0.1"
        session.headers.update({"Host": "guiesbarcelona.elglobusvermell.org"})
        session.verify = False
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    else:
        BASE_URL = "https://guiesbarcelona.elglobusvermell.org"
        session.headers.pop("Host", None)
        session.verify = True


def get_url(url: str, timeout: int = 15) -> Optional[requests.Response]:
    try:
        r = session.get(url, timeout=timeout, allow_redirects=True)
        return r
    except requests.RequestException as e:
        log.debug(f"Request error for {url}: {e}")
        return None


# ── WP page scraper ────────────────────────────────────────────────────────────

def scrape_wp_page(url: str) -> Optional[dict]:
    """
    Scrape all relevant fields from a WP element page.

    WP structure:
    - Metadata in <ul><li> or <p> tags: "Label: value"
    - Description in <p> tags (not starting with a label)
    - No coordinates (maps not in WP)
    - Images in /wp-content/uploads/ (often book covers - flag, don't auto-set)
    """
    r = get_url(url)
    if r is None or r.status_code != 200:
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    data = {"_url": url, "_raw_fields": {}, "_warnings": []}
    raw = data["_raw_fields"]

    # ── Title ──────────────────────────────────────────────────────────────────
    h1 = (
        soup.find("h1", class_=re.compile(r"entry-title|post-title", re.I))
        or soup.find("h1")
    )
    if h1:
        raw["title"] = h1.get_text(strip=True)

    # ── Find the main content area ─────────────────────────────────────────────
    content_el = (
        soup.find("div", class_=re.compile(r"entry-content|post-content", re.I))
        or soup.find("article")
        or soup.find("main")
    )

    if not content_el:
        data["_warnings"].append("No content element found")
        return data

    # ── Parse labeled fields from li and p tags ────────────────────────────────
    # Pattern: "Label: value" or "Label: value" in any li/p
    label_pattern = re.compile(
        r'^(Adreça|Projecte|Arquitectes?|Reformes?|Categoria|Nivell de protecció|'
        r'Protecció|Premi|Premis|Superfície|Obertura|Equipament|'
        r'Nomenclàtor|Dedicatòria|Web|Edifici original|Intervenció|Intervencions?)'
        r'\s*[:\-]\s*(.+)$',
        re.IGNORECASE | re.DOTALL
    )

    description_paras = []
    labeled_texts = set()

    for tag in content_el.find_all(["li", "p"]):
        text = tag.get_text(separator=" ", strip=True)
        text = re.sub(r'\s+', ' ', text).strip()
        if not text:
            continue

        m = label_pattern.match(text)
        if m:
            label = m.group(1).strip().lower()
            value = m.group(2).strip()
            raw[label] = value
            labeled_texts.add(text[:50])
        else:
            # It's a description paragraph if it's not navigation/link-only
            # Skip very short texts and texts that look like category links
            skip_patterns = [
                r'^Més informació',
                r'^Arquitectura (d|a)',
                r'^El patrimoni',
                r'^Presentació',
                r'^En paper',
                r'^Crèdits',
            ]
            if (len(text) > 30 and
                    not any(re.match(p, text, re.I) for p in skip_patterns) and
                    text not in labeled_texts):
                description_paras.append(text)

    if description_paras:
        # Take the longest paragraph as the description (most informative)
        # Filter out very short ones
        long_paras = [p for p in description_paras if len(p) > 50]
        if long_paras:
            raw["_description_paras"] = long_paras

    # ── Extract images (flag only, don't auto-set) ─────────────────────────────
    building_imgs = []
    book_cover_keywords = ["203x300", "portada", "coberta", "cover", "book",
                           "logoweb", "logo", "icon", "arrow", "avatar",
                           "gatpac", "poblenou", "jardins-203", "biblioteques",
                           "mercats", "masies", "barceloneta", "marina",
                           "Portada"]
    for img in soup.find_all("img"):
        src = img.get("src", "")
        alt = img.get("alt", "").lower()
        if not src:
            continue
        if any(kw.lower() in src.lower() or kw.lower() in alt for kw in book_cover_keywords):
            continue
        if "/wp-content/uploads/" in src:
            building_imgs.append(src)

    if building_imgs:
        raw["_possible_foto"] = building_imgs[0]

    return data


# ── Field parsing helpers ──────────────────────────────────────────────────────

def parse_projecte(projecte_text: str) -> dict:
    """
    Parse 'Architect Name. Year' or 'Arch1 i Arch2. Year' from Projecte field.
    Returns dict with 'arquitectes' list and 'any' integer (if parseable).
    """
    result = {}
    if not projecte_text:
        return result

    # Extract year: last 4-digit number
    year_match = re.search(r'\b(1[0-9]{3}|20[0-9]{2})\b', projecte_text)
    if year_match:
        result["any"] = int(year_match.group(1))

    # Extract architect names: everything before the year
    # Remove trailing year portion
    name_part = re.sub(r'[\.,]\s*\d{4}.*$', '', projecte_text).strip()
    name_part = re.sub(r'\.$', '', name_part).strip()

    if name_part:
        # Split by " i ", ",", ";"
        names = re.split(r'\s+i\s+|,\s*|;\s*', name_part)
        names = [n.strip() for n in names if n.strip() and len(n.strip()) > 1]
        if names:
            result["arquitectes"] = names

    return result


def parse_any(any_text: str) -> tuple:
    """
    Returns (int_year or None, text_year or None).
    If parseable as integer → (int, None)
    If text (e.g. 'Principis S. XIX') → (None, text)
    """
    if not any_text:
        return (None, None)
    m = re.search(r'\b(1[0-9]{3}|20[0-9]{2})\b', str(any_text))
    if m:
        return (int(m.group(1)), None)
    return (None, str(any_text).strip())


LABEL_MAP = {
    "adreça":              "adreca",
    "adresa":              "adreca",
    "projecte":            "_projecte",  # needs special parsing
    "arquitecte":          "arquitectes",
    "arquitectes":         "arquitectes",
    "reformes":            "_reformes",
    "reforma":             "_reformes",
    "categoria":           "tipologia",
    "nivell de protecció": "proteccio",
    "protecció":           "proteccio",
    "premi":               "premis",
    "premis":              "premis",
    "superfície":          "superficie",
    "obertura":            "obertura",
    "equipament":          "equipament",
    "nomenclàtor":         "descripcio_nomenclator",
    "dedicatòria":         "descripcio_nomenclator",
    "web":                 "web",
    "edifici original":    "edifici_original",
}


def extract_hugo_fields(raw: dict) -> dict:
    """Convert raw WP label→value pairs to Hugo field names."""
    hugo = {}

    for raw_label, value in raw.items():
        if raw_label.startswith("_"):
            continue
        mapped = LABEL_MAP.get(raw_label.lower().strip())
        if not mapped:
            continue

        if mapped == "_projecte":
            parsed = parse_projecte(value)
            if "arquitectes" in parsed:
                hugo.setdefault("arquitectes", parsed["arquitectes"])
            if "any" in parsed:
                hugo.setdefault("any", parsed["any"])

        elif mapped == "_reformes":
            # Store raw reform text for reference
            hugo.setdefault("_reformes_text", value)

        elif mapped == "arquitectes":
            # Split by " i ", ","
            names = re.split(r'\s+i\s+|,\s*|;\s*', value)
            names = [n.strip() for n in names if n.strip()]
            hugo["arquitectes"] = names

        elif mapped == "premis":
            items = [x.strip() for x in re.split(r'[;,]', value) if x.strip()]
            hugo["premis"] = items

        elif mapped == "superficie":
            # Extract numeric part
            m = re.search(r'(\d[\d.,]*)', value)
            if m:
                try:
                    hugo["superficie"] = int(float(m.group(1).replace(",", ".")))
                except ValueError:
                    hugo["superficie"] = value
            else:
                hugo["superficie"] = value

        else:
            hugo[mapped] = value

    # Description paragraphs
    paras = raw.get("_description_paras", [])
    if paras:
        hugo["_descripcio_candidates"] = paras

    # Possible foto
    if "_possible_foto" in raw:
        hugo["_possible_foto"] = raw["_possible_foto"]

    # Title
    if "title" in raw:
        hugo["_wp_title"] = raw["title"]

    return hugo


# ── WP URL resolution ──────────────────────────────────────────────────────────

def find_wp_url(slug: str, publicacions: list) -> Optional[tuple]:
    """
    Try to find the WP URL for an element.
    Returns (url, category) or None.
    """
    categories_to_try = []
    for pub in publicacions:
        for cat in PUBLICACIO_TO_CATEGORIES.get(pub, []):
            if cat not in categories_to_try:
                categories_to_try.append(cat)

    for category in categories_to_try:
        url = f"{BASE_URL}/{category}/{slug}/"
        r = get_url(url)
        time.sleep(REQUEST_DELAY)
        if r and r.status_code == 200:
            return (url, category)

    return None


# ── Hugo .md update logic ──────────────────────────────────────────────────────

def update_md_file(md_path: Path, hugo_fields: dict, wp_url: str) -> dict:
    """
    Safely update a Hugo element .md file with scraped data.
    NEVER overwrites existing non-empty data.
    Returns update result dict.
    """
    post = frontmatter.load(str(md_path))
    meta = post.metadata

    result = {
        "file": md_path.name,
        "url": wp_url,
        "updated": [],
        "skipped": [],
        "flags": [],
    }

    # ── Title: flag if different ───────────────────────────────────────────────
    wp_title = hugo_fields.get("_wp_title", "")
    hugo_title = str(meta.get("title", ""))
    if wp_title and hugo_title:
        if wp_title.lower().strip() != hugo_title.lower().strip():
            result["flags"].append(
                f"⚠️ Title mismatch: Hugo=`{hugo_title}` WP=`{wp_title}`"
            )

    # ── adreca ────────────────────────────────────────────────────────────────
    wp_adreca = hugo_fields.get("adreca", "")
    hugo_adreca = str(meta.get("adreca", "")).strip()
    if wp_adreca and not hugo_adreca:
        meta["adreca"] = wp_adreca
        result["updated"].append(f"adreca={wp_adreca!r}")
    elif wp_adreca and hugo_adreca and wp_adreca.lower() != hugo_adreca.lower():
        result["flags"].append(
            f"⚠️ Adreca mismatch: Hugo=`{hugo_adreca}` WP=`{wp_adreca}`"
        )

    # ── any ───────────────────────────────────────────────────────────────────
    wp_any = hugo_fields.get("any")
    hugo_any = meta.get("any")
    if wp_any and hugo_any is None:
        meta["any"] = wp_any
        result["updated"].append(f"any={wp_any}")

    # ── arquitectes ───────────────────────────────────────────────────────────
    wp_arq = hugo_fields.get("arquitectes", [])
    hugo_arq = meta.get("arquitectes", [])
    if wp_arq and not hugo_arq:
        meta["arquitectes"] = wp_arq
        result["updated"].append(f"arquitectes={wp_arq}")

    # ── descripcio ────────────────────────────────────────────────────────────
    hugo_desc = str(meta.get("descripcio", "")).strip()
    desc_candidates = hugo_fields.get("_descripcio_candidates", [])

    if desc_candidates and not hugo_desc:
        # Use the longest candidate
        best = max(desc_candidates, key=len)
        meta["descripcio"] = best
        result["updated"].append(f"descripcio ({len(best)} chars)")
    elif desc_candidates and hugo_desc:
        result["skipped"].append("descripcio (already has content)")

    # ── tipologia ─────────────────────────────────────────────────────────────
    wp_tip = hugo_fields.get("tipologia", "")
    if wp_tip and not meta.get("tipologia"):
        meta["tipologia"] = wp_tip
        result["updated"].append(f"tipologia={wp_tip!r}")

    # ── proteccio ─────────────────────────────────────────────────────────────
    wp_prot = hugo_fields.get("proteccio", "")
    if wp_prot and not meta.get("proteccio"):
        # Normalise: just the letter(s)
        prot_clean = re.sub(r'\s+', ' ', wp_prot).strip()
        meta["proteccio"] = prot_clean
        result["updated"].append(f"proteccio={prot_clean!r}")

    # ── superficie ────────────────────────────────────────────────────────────
    wp_sup = hugo_fields.get("superficie")
    if wp_sup and not meta.get("superficie"):
        meta["superficie"] = wp_sup
        result["updated"].append(f"superficie={wp_sup}")

    # ── obertura ─────────────────────────────────────────────────────────────
    wp_ob = hugo_fields.get("obertura", "")
    if wp_ob and not meta.get("obertura"):
        meta["obertura"] = wp_ob
        result["updated"].append(f"obertura={wp_ob!r}")

    # ── equipament ───────────────────────────────────────────────────────────
    wp_eq = hugo_fields.get("equipament", "")
    if wp_eq and not meta.get("equipament"):
        meta["equipament"] = wp_eq
        result["updated"].append(f"equipament={wp_eq!r}")

    # ── descripcio_nomenclator ────────────────────────────────────────────────
    wp_nom = hugo_fields.get("descripcio_nomenclator", "")
    hugo_nom = str(meta.get("descripcio_nomenclator", "")).strip()
    if wp_nom and not hugo_nom:
        meta["descripcio_nomenclator"] = wp_nom
        result["updated"].append(f"descripcio_nomenclator ({len(wp_nom)} chars)")
    elif wp_nom and hugo_nom:
        result["skipped"].append("descripcio_nomenclator (already has content)")

    # ── premis ────────────────────────────────────────────────────────────────
    wp_premis = hugo_fields.get("premis", [])
    if wp_premis and not meta.get("premis"):
        meta["premis"] = wp_premis
        result["updated"].append(f"premis={wp_premis}")

    # ── web ───────────────────────────────────────────────────────────────────
    wp_web = hugo_fields.get("web", "")
    if wp_web and not meta.get("web"):
        meta["web"] = wp_web
        result["updated"].append(f"web={wp_web!r}")

    # ── edifici_original ─────────────────────────────────────────────────────
    wp_eo = hugo_fields.get("edifici_original", "")
    if wp_eo and not meta.get("edifici_original"):
        meta["edifici_original"] = wp_eo
        result["updated"].append(f"edifici_original={wp_eo!r}")

    # ── foto: flag only ───────────────────────────────────────────────────────
    wp_foto = hugo_fields.get("_possible_foto", "")
    if wp_foto and not meta.get("foto"):
        result["flags"].append(f"📷 Possible foto from WP (review manually): {wp_foto}")

    # ── reformes text: flag ───────────────────────────────────────────────────
    ref_text = hugo_fields.get("_reformes_text", "")
    if ref_text and not (meta.get("anys_reforma") or meta.get("usos_reforma")):
        result["flags"].append(f"🔧 Reformes info from WP (review manually): {ref_text}")

    # ── Write back if changed ─────────────────────────────────────────────────
    if result["updated"]:
        post.metadata = meta
        new_content = frontmatter.dumps(post)
        md_path.write_text(new_content, encoding="utf-8")

    return result


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    md_files = sorted(ELEMENTS_DIR.glob("*.md"))
    md_files = [f for f in md_files if f.name != "_index.md"]

    log.info(f"Found {len(md_files)} element files in {ELEMENTS_DIR}")

    stats = {
        "total": len(md_files),
        "found_on_wp": 0,
        "not_found": 0,
        "files_updated": 0,
        "descriptions_filled": 0,
        "fields_added": 0,
        "scrape_errors": 0,
    }

    report_sections = {
        "updated": [],
        "flags": [],
        "not_found": [],
        "skipped": [],
        "errors": [],
    }

    for md_path in md_files:
        slug = md_path.stem
        try:
            post = frontmatter.load(str(md_path))
        except Exception as e:
            log.error(f"Cannot parse {md_path.name}: {e}")
            report_sections["errors"].append(f"- `{slug}`: parse error: {e}")
            continue

        meta = post.metadata
        publicacions = meta.get("publicacions", [])

        log.info(f"Processing: {slug}")

        # Resolve WP URL
        found = find_wp_url(slug, publicacions)

        if not found:
            log.warning(f"  NOT FOUND on WP: {slug}")
            stats["not_found"] += 1
            report_sections["not_found"].append(
                f"- `{slug}` (publicacions: {publicacions})"
            )
            continue

        wp_url, wp_category = found
        stats["found_on_wp"] += 1
        log.info(f"  Found: {wp_url}")

        # Scrape
        scraped = scrape_wp_page(wp_url)
        time.sleep(REQUEST_DELAY)

        if scraped is None:
            log.warning(f"  Scrape failed: {wp_url}")
            stats["scrape_errors"] += 1
            report_sections["errors"].append(f"- `{slug}`: scrape failed ({wp_url})")
            continue

        # Extract Hugo fields
        hugo_fields = extract_hugo_fields(scraped["_raw_fields"])
        for w in scraped.get("_warnings", []):
            log.debug(f"  WP warning: {w}")

        # Update file
        result = update_md_file(md_path, hugo_fields, wp_url)

        if result["updated"]:
            stats["files_updated"] += 1
            stats["fields_added"] += len(result["updated"])
            if any("descripcio" in u for u in result["updated"]):
                stats["descriptions_filled"] += 1

            lines = [f"### `{slug}`", f"- URL: {wp_url}"]
            for u in result["updated"]:
                lines.append(f"  - ✅ {u}")
            for s in result["skipped"]:
                lines.append(f"  - ⏭️ skipped: {s}")
            report_sections["updated"].append("\n".join(lines))
            log.info(f"  Updated: {result['updated']}")

        elif result["skipped"]:
            report_sections["skipped"].append(
                f"- `{slug}`: {'; '.join(result['skipped'])}"
            )

        for flag in result["flags"]:
            report_sections["flags"].append(f"- `{slug}`: {flag}")

        if result["flags"]:
            log.info(f"  Flags: {result['flags']}")

    # ── Build report ──────────────────────────────────────────────────────────
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# Sync Report: Hugo Elements ↔ WordPress",
        f"\nGenerated: {now}",
        f"Base URL: {BASE_URL}",
        "\n---\n",
        "## Summary\n",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total elements | {stats['total']} |",
        f"| Found on WP | {stats['found_on_wp']} |",
        f"| Not found on WP | {stats['not_found']} |",
        f"| Scrape errors | {stats['scrape_errors']} |",
        f"| Files updated | {stats['files_updated']} |",
        f"| Descriptions filled | {stats['descriptions_filled']} |",
        f"| Total fields added | {stats['fields_added']} |",
        "\n---\n",
    ]

    if report_sections["updated"]:
        lines += ["## Updated Elements\n"]
        lines += report_sections["updated"]
        lines += ["\n---\n"]

    if report_sections["flags"]:
        lines += ["## Flags for Human Review\n"]
        lines += report_sections["flags"]
        lines += ["\n---\n"]

    if report_sections["skipped"]:
        lines += ["## Skipped (already has data)\n"]
        lines += report_sections["skipped"]
        lines += ["\n---\n"]

    if report_sections["not_found"]:
        lines += ["## Elements NOT Found on WP\n"]
        lines += ["These slugs need manual URL mapping:\n"]
        lines += report_sections["not_found"]
        lines += ["\n"]

    if report_sections["errors"]:
        lines += ["## Errors\n"]
        lines += report_sections["errors"]
        lines += ["\n"]

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"SYNC COMPLETE")
    print(f"{'='*60}")
    print(f"  Total elements:        {stats['total']}")
    print(f"  Found on WP:           {stats['found_on_wp']}")
    print(f"  Not found on WP:       {stats['not_found']}")
    print(f"  Scrape errors:         {stats['scrape_errors']}")
    print(f"  Files updated:         {stats['files_updated']}")
    print(f"  Descriptions filled:   {stats['descriptions_filled']}")
    print(f"  Total fields added:    {stats['fields_added']}")
    print(f"  Report: {REPORT_FILE}")
    print(f"{'='*60}\n")

    if report_sections["not_found"]:
        print("NOT FOUND ON WP:")
        for s in report_sections["not_found"]:
            print(f"  {s}")


if __name__ == "__main__":
    main()
