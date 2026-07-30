#!/usr/bin/env python3
"""
genera-galeria-dades.py
Regenera static/admin/galeria/dades.json a partir del front matter real de
content/ca/elements/*.md. Executar cada cop que canviïn fotos o títols i es
vulgui refrescar la galeria estàtica de l'administrador.

Ús: python3 scripts/genera-galeria-dades.py
"""
import frontmatter
import glob
import json
from pathlib import Path

ELEMENTS_DIR = Path(__file__).parent.parent / "content" / "ca" / "elements"
OUT_FILE = Path(__file__).parent.parent / "static" / "admin" / "galeria" / "dades.json"


def main():
    files = sorted(f for f in glob.glob(str(ELEMENTS_DIR / "*.md")) if not f.endswith("_index.md"))
    items = []
    for f in files:
        p = frontmatter.load(f)
        slug = Path(f).stem
        items.append({
            "slug": slug,
            "title": p.metadata.get("title", slug),
            "foto": p.metadata.get("foto") or None,
            "pubs": p.metadata.get("publicacions", []) or [],
        })

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(items, ensure_ascii=False), encoding="utf-8")
    with_photo = sum(1 for i in items if i["foto"])
    print(f"Escrit {OUT_FILE}: {len(items)} elements, {with_photo} amb foto")


if __name__ == "__main__":
    main()
