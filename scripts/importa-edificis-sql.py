#!/usr/bin/env python3
"""
Importa edificis del dump SQL de l'app original al format Hugo.

Genera un fitxer .md per cada edifici que pertany a una publicació
definida a data/publicacions.yaml.

Ús:
    python3 scripts/importa-edificis-sql.py

Sortida: content/ca/elements/<slug>.md
"""

import re
import unicodedata
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
REPO = Path(__file__).parent.parent
SQL_PATH = REPO.parent / "guia-globus-vermell/Backup PROD 260616/globus_vermell_260616.sql"
OUTPUT_DIR = REPO / "content/ca/elements"

# ── Mapeig id_publication_app → slug Hugo ──────────────────────────────────
PUB_ID_TO_SLUG = {
    31: "gatcpac",
    36: "interiors-illa",
    33: "poblenou",
    37: "mercats",
    34: "biblioteques",
    35: "76-08",
    32: "09-25",
}
# Publicacions sense id_app (50-75, barceloneta, marina, tapies, masies,
# new-babylon) no tenen edificis al dump — s'importaran manualment.


# ── Parser de blocs COPY ───────────────────────────────────────────────────

def parse_copy_block(sql_text: str, table: str, columns: list[str]) -> list[dict]:
    """Extreu les files d'un bloc COPY com a llista de dicts."""
    pattern = rf"COPY public\.{re.escape(table)} \([^)]+\) FROM stdin;\n(.*?)\n\\\."
    match = re.search(pattern, sql_text, re.DOTALL)
    if not match:
        return []
    rows = []
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        values = line.split("\t")
        row = {}
        for i, col in enumerate(columns):
            val = values[i] if i < len(values) else r"\N"
            row[col] = None if val == r"\N" else val
        rows.append(row)
    return rows


# ── Generació de slugs ─────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


# ── Escape de valors TOML ──────────────────────────────────────────────────

def toml_str(val) -> str:
    if val is None:
        return '""'
    return '"' + str(val).replace("\\", "\\\\").replace('"', '\\"') + '"'


def toml_list(items: list) -> str:
    escaped = [toml_str(i) for i in items]
    return "[" + ", ".join(escaped) + "]"


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    if not SQL_PATH.exists():
        print(f"ERROR: No trobo el dump SQL a {SQL_PATH}", file=sys.stderr)
        sys.exit(1)

    sql = SQL_PATH.read_text(encoding="utf-8", errors="replace")

    # Carregar totes les taules
    buildings = parse_copy_block(sql, "buildings", [
        "id_building", "name", "location", "construction_year", "description",
        "surface_area", "id_typology", "id_protection", "validated", "lat", "long",
        "description_es", "description_en", "description_fr", "description_ar",
    ])

    typologies_raw = parse_copy_block(sql, "typologies", ["id_typology", "name", "image"])
    typology_map = {r["id_typology"]: r["name"] for r in typologies_raw}

    protections_raw = parse_copy_block(sql, "protections", ["id_protection", "level", "description"])
    protection_map = {r["id_protection"]: r["level"] for r in protections_raw}

    architects_raw = parse_copy_block(sql, "architects", [
        "id_architect", "name", "description", "birth_year", "death_year",
        "nationality", "description_es", "description_en", "description_fr", "description_ar",
        "nationality_es", "nationality_en", "nationality_fr", "nationality_ar",
    ])
    architect_map = {r["id_architect"]: r["name"] for r in architects_raw}

    bld_architects_raw = parse_copy_block(sql, "building_architects", ["id_building", "id_architect"])
    bld_architects: dict[str, list] = {}
    for r in bld_architects_raw:
        bld_architects.setdefault(r["id_building"], []).append(
            architect_map.get(r["id_architect"], r["id_architect"])
        )

    bld_pubs_raw = parse_copy_block(sql, "building_publications", ["id_building", "id_publication"])
    bld_pubs: dict[str, list] = {}
    for r in bld_pubs_raw:
        slug = PUB_ID_TO_SLUG.get(int(r["id_publication"]))
        if slug:
            bld_pubs.setdefault(r["id_building"], []).append(slug)

    reforms_raw = parse_copy_block(sql, "reforms", [
        "id_reform", "year", "use", "id_building",
        "use_es", "use_en", "use_fr", "use_ar",
    ])
    bld_reforms: dict[str, list] = {}
    for r in reforms_raw:
        bld_reforms.setdefault(r["id_building"], []).append({
            "any": r["year"],
            "us": r["use"],
        })

    prizes_raw = parse_copy_block(sql, "prizes", ["id_prize", "name", "type", "year", "description"])
    prize_map = {r["id_prize"]: r["name"] for r in prizes_raw}

    bld_prizes_raw = parse_copy_block(sql, "building_prizes", ["id_building", "id_prize"])
    bld_prizes: dict[str, list] = {}
    for r in bld_prizes_raw:
        name = prize_map.get(r["id_prize"], r["id_prize"])
        bld_prizes.setdefault(r["id_building"], []).append(name)

    # Generar fitxes
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    created = skipped_no_pub = skipped_exists = 0

    for b in buildings:
        bid = b["id_building"]
        pubs = bld_pubs.get(bid, [])

        if not pubs:
            skipped_no_pub += 1
            continue

        slug = slugify(b["name"] or f"edifici-{bid}")
        out_path = OUTPUT_DIR / f"{slug}.md"

        # No sobreescriure fitxes existents (edicions manuals preservades)
        if out_path.exists():
            skipped_exists += 1
            continue

        # Lat/long
        lat = b["lat"]
        lng = b["long"]
        if lat and "No tenim" in lat:
            lat = None
        if lng and "No tenim" in lng:
            lng = None

        # Tipologia i protecció
        tipologia = typology_map.get(b["id_typology"]) if b["id_typology"] else None
        proteccio = protection_map.get(b["id_protection"]) if b["id_protection"] else None

        # Arquitectes
        arquitectes = bld_architects.get(bid, [])

        # Reformes
        reformes = bld_reforms.get(bid, [])

        # Premis
        premis = bld_prizes.get(bid, [])

        # Draft si no validat
        validated = b.get("validated", "f")
        draft = "false" if validated == "t" else "true"

        # Construir frontmatter TOML
        lines = ["+++"]
        lines.append(f'title = {toml_str(b["name"])}')
        lines.append(f"draft = {draft}")
        lines.append("")
        lines.append(f'adreca = {toml_str(b["location"])}')
        lines.append(f'any = {toml_str(b["construction_year"])}')

        if lat:
            lines.append(f'lat = "{lat}"')
        if lng:
            lines.append(f'long = "{lng}"')

        lines.append("")
        lines.append(f"publicacions = {toml_list(pubs)}")

        if b["surface_area"]:
            lines.append(f'superficie = {b["surface_area"]}')
        if tipologia:
            lines.append(f'tipologia = {toml_str(tipologia)}')
        if proteccio:
            lines.append(f'proteccio = {toml_str(proteccio)}')
        if arquitectes:
            lines.append(f"arquitectes = {toml_list(arquitectes)}")
        if reformes:
            anys_reforma = [r["any"] for r in reformes if r["any"]]
            usos_reforma = [r["us"] for r in reformes if r["us"]]
            if anys_reforma:
                lines.append(f"anys_reforma = {toml_list(anys_reforma)}")
            if usos_reforma:
                lines.append(f"usos_reforma = {toml_list(usos_reforma)}")
        if premis:
            lines.append(f"premis = {toml_list(premis)}")

        lines.append("")
        lines.append(f'descripcio = {toml_str(b["description"])}')
        lines.append("+++")

        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        created += 1
        print(f"  ✓ {slug}.md  [{', '.join(pubs)}]")

    print(f"\nResultat:")
    print(f"  {created} fitxes creades")
    print(f"  {skipped_exists} ja existien (preservades)")
    print(f"  {skipped_no_pub} edificis sense publicació coneguda (omesos)")


if __name__ == "__main__":
    main()
