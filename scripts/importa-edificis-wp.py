#!/usr/bin/env python3
"""
Importa fitxes d'edifici/element des del WordPress en viu (API REST) al format Hugo.

Font: https://guiesbarcelona.elglobusvermell.org/wp-json/wp/v2/
El contingut no té camps estructurats — cal parsejar etiquetes lliures dins
el text ("Adreça:", "Projecte:", "Reforma:", "Nivell de protecció:"...).

Ús (test, sense escriure a content/):
    python3 scripts/importa-edificis-wp.py --slug marina --out /tmp/wp-import-test

Ús real:
    python3 scripts/importa-edificis-wp.py --slug marina --out content/ca/elements
"""

import argparse
import html
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

API = "https://guiesbarcelona.elglobusvermell.org/wp-json/wp/v2"

# ── Categoria WP → slug publicació Hugo ─────────────────────────────────────
CATEGORY_MAP = {
    "avantguarda-1928-1938": ("gatcpac", 2),
    "eixample-jardins-interiors": ("interiors-illa", 3),
    "poblenou-industrial": ("poblenou", 4),
    "moderna-1950-1975": ("50-75", 5),
    "mercats": ("mercats", 6),
    "biblioteques": ("biblioteques", 7),
    "barceloneta": ("barceloneta", 12),
    "marina-prat-vermell": ("marina", 21),
    "masies": ("masies", 22),
    "2010-2025": ("09-25", 23),
    "1975-2008": ("76-08", 24),
}

CAT_ID_TO_PUB = {cid: pub_slug for pub_slug, cid in CATEGORY_MAP.values()}

TAG_MAP = {
    17: "art-public",
    19: "dones-arquitectes",
    18: "espai-public",
    20: "nomenclator-femeni",
}

def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_posts(category_id: int) -> list[dict]:
    posts = []
    page = 1
    while True:
        url = f"{API}/posts?categories={category_id}&per_page=100&page={page}&_fields=id,slug,title,content,link,tags,categories"
        try:
            batch = fetch_json(url)
        except urllib.error.HTTPError as e:
            if e.code == 400:  # pàgina fora de rang
                break
            raise
        if not batch:
            break
        posts.extend(batch)
        page += 1
    return posts


# ── Neteja i parsing de contingut ───────────────────────────────────────────

def strip_tags(raw_html: str) -> str:
    text = re.sub(r"<[^>]+>", "\n", raw_html)
    return html.unescape(text)


def clean_title(raw_title: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", raw_title)).strip()


LABEL_PATTERNS = {
    "adreca": r"Adre[çc]a:\s*(.+)",
    "proteccio": r"Nivell de protecci[oó]:\s*(.+)",
    "tipologia": r"Tipologia:\s*(.+)",
    "superficie": r"Superf[ií]cie:\s*(.+)",
    "any_obertura": r"Obertura:\s*(.+)",
    "edifici_original": r"Edifici original:\s*(.+)",
}

# Ordre convencional de les intervencions (veure comentari a
# themes/.../elements/single.html: "remunta, remodelació, ampliació, reforma")
INTERVENCIO_LABELS = ["Projecte", "Remunta", "Remodelació", "Ampliació", "Reforma"]
INTERVENCIO_RE = re.compile(
    r"^(" + "|".join(INTERVENCIO_LABELS) + r"):\s*(.+)$"
)

YEAR_RE = re.compile(r"(\d{4})\s*$")
WEB_RE = re.compile(r"(https?://\S+|www\.\S+)")


def split_autor_any(value: str):
    """'Josep Maria Soteras i Mauri. 1959' -> (autor, any). Si no hi ha
    patró clar 'Nom. Any', retorna (None, None) i el valor es guarda sencer."""
    m = re.match(r"^(.*?)\.\s*(\d{4})$", value.strip())
    if m and m.group(1).strip():
        return m.group(1).strip(), m.group(2)
    if re.match(r"^\d{4}$", value.strip()):
        return None, value.strip()
    return None, None


def parse_post(post: dict, fallback_pub_slug: str) -> dict:
    text = strip_tags(post["content"]["rendered"])
    lines = [l.strip() for l in text.split("\n")]
    lines = [l for l in lines if l and l != "|"]

    fields = {"adreca": None, "proteccio": None, "tipologia": None,
              "superficie": None, "any_obertura": None, "edifici_original": None}
    intervencions_raw = []  # [(tipus, valor)] en l'ordre trobat al text
    desc_lines = []
    web = None

    for line in lines:
        if line.startswith("Més informació a"):
            break  # tot el que ve després és cita de publicacions, no descripció
        w = WEB_RE.search(line)
        if w and len(line) < 80:
            web = w.group(1).rstrip(".,")
            continue
        m_iv = INTERVENCIO_RE.match(line)
        if m_iv:
            intervencions_raw.append((m_iv.group(1), m_iv.group(2).strip()))
            continue
        matched = False
        for key, pattern in LABEL_PATTERNS.items():
            m = re.match(pattern, line)
            if m:
                fields[key] = m.group(1).strip()
                matched = True
                break
        if not matched:
            desc_lines.append(line)

    intervencions = []
    for tipus, valor in intervencions_raw:
        autor, any_ = split_autor_any(valor)
        intervencions.append({"tipus": tipus, "autors": autor, "any": any_ or (valor if not autor else None)})

    # El primer "Projecte" alimenta els camps de nivell superior (any/arquitectes)
    projecte_valor = next((v for t, v in intervencions_raw if t == "Projecte"), None)
    any_field = None
    arquitectes = []
    projecte_text = None
    if projecte_valor:
        autor, any_ = split_autor_any(projecte_valor)
        any_field = any_
        if autor:
            arquitectes.append(autor)
        if not autor and not any_:
            projecte_text = projecte_valor

    temes = [TAG_MAP[t] for t in post.get("tags", []) if t in TAG_MAP]

    publicacions = sorted({CAT_ID_TO_PUB[c] for c in post.get("categories", []) if c in CAT_ID_TO_PUB})
    if not publicacions:
        publicacions = [fallback_pub_slug]

    return {
        "title": clean_title(post["title"]["rendered"]),
        "slug": post["slug"],
        "wp_link": post["link"],
        "adreca": fields["adreca"],
        "projecte_text": projecte_text,
        "any": any_field,
        "arquitectes": arquitectes,
        "intervencions": intervencions,
        "proteccio": fields["proteccio"],
        "tipologia": fields["tipologia"],
        "superficie": fields["superficie"],
        "obertura": fields["any_obertura"],
        "edifici_original": fields["edifici_original"],
        "web": web,
        "descripcio": " ".join(desc_lines).strip(),
        "temes_transversals": temes,
        "publicacions": publicacions,
    }


# ── Generació TOML ──────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def toml_str(val) -> str:
    if val is None:
        return '""'
    return '"' + str(val).replace("\\", "\\\\").replace('"', '\\"') + '"'


def toml_list(items) -> str:
    return "[" + ", ".join(toml_str(i) for i in items) + "]"


def to_frontmatter(b: dict) -> str:
    lines = ["+++"]
    lines.append(f'title = {toml_str(b["title"])}')
    lines.append("draft = false")
    lines.append("")
    if b["adreca"]:
        lines.append(f'adreca = {toml_str(b["adreca"])}')
    if b["any"]:
        lines.append(f'any = {toml_str(b["any"])}')
    if b["projecte_text"]:
        lines.append(f'projecte_text = {toml_str(b["projecte_text"])}')
    lines.append("")
    lines.append(f"publicacions = {toml_list(b['publicacions'])}")
    if b["temes_transversals"]:
        lines.append(f"temes_transversals = {toml_list(b['temes_transversals'])}")
    if b["tipologia"]:
        lines.append(f'tipologia = {toml_str(b["tipologia"])}')
    if b["proteccio"]:
        lines.append(f'proteccio = {toml_str(b["proteccio"])}')
    if b["superficie"]:
        lines.append(f'superficie = {toml_str(b["superficie"])}')
    if b["obertura"]:
        lines.append(f'obertura = {toml_str(b["obertura"])}')
    if b["edifici_original"]:
        lines.append(f'edifici_original = {toml_str(b["edifici_original"])}')
    if b["arquitectes"]:
        lines.append(f"arquitectes = {toml_list(b['arquitectes'])}")
    if b["web"]:
        lines.append(f'web = {toml_str(b["web"])}')
    if b["intervencions"]:
        lines.append("")
        for iv in b["intervencions"]:
            lines.append("[[intervencions]]")
            lines.append(f'  tipus = {toml_str(iv["tipus"])}')
            if iv.get("autors"):
                lines.append(f'  autors = {toml_str(iv["autors"])}')
            if iv.get("any"):
                lines.append(f'  any = {toml_str(iv["any"])}')
    lines.append("")
    lines.append(f'descripcio = {toml_str(b["descripcio"])}')
    lines.append(f"# font: {b['wp_link']}")
    lines.append("+++")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True,
                     help="slug(s) de publicació separats per coma (ex: marina,mercats) o 'all'")
    ap.add_argument("--out", required=True, help="directori de sortida")
    args = ap.parse_args()

    if args.slug == "all":
        requested = [pub_slug for pub_slug, _ in CATEGORY_MAP.values()]
    else:
        requested = [s.strip() for s in args.slug.split(",")]

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    seen_post_ids = set()
    created = skipped_intro = skipped_dup = 0

    for pub_slug in requested:
        cat_slug, cat_id = None, None
        for wp_cat, (ps, cid) in CATEGORY_MAP.items():
            if ps == pub_slug:
                cat_slug, cat_id = wp_cat, cid
                break
        if not cat_id:
            print(f"ERROR: no conec la publicació '{pub_slug}'", file=sys.stderr)
            continue

        print(f"Descarregant categoria '{cat_slug}' (id {cat_id})...")
        posts = fetch_posts(cat_id)
        print(f"  {len(posts)} posts trobats")

        for post in posts:
            if post["id"] in seen_post_ids:
                skipped_dup += 1
                continue
            # El post de presentació del grup viu a /text/<slug>/ (categoria
            # "text", id 1) encara que també aparegui a la categoria del grup.
            # Detectar-lo pel path és molt més fiable que comparar títols.
            if "/text/" in post.get("link", ""):
                skipped_intro += 1
                continue
            seen_post_ids.add(post["id"])
            b = parse_post(post, pub_slug)
            slug = slugify(b["title"])
            out_path = out_dir / f"{slug}.md"
            out_path.write_text(to_frontmatter(b), encoding="utf-8")
            created += 1

    print(f"\nResultat:")
    print(f"  {created} fitxes generades a {out_dir}")
    print(f"  {skipped_intro} post(s) de presentació de grup omesos")
    print(f"  {skipped_dup} post(s) duplicats entre categories (ja fusionats)")


if __name__ == "__main__":
    main()
