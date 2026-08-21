#!/usr/bin/env python3
"""Afegeix el camp `zona` als mercats (agrupació històrica del plànol en paper).

Estructura del plànol Mercats de Barcelona (content/ca/publicacions/mercats/_index.md):
- Ciutat Vella / Eixample / Antics municipis (amb sub-municipis) / Nous barris /
  Mercats no alimentaris.

Criteri per als sub-municipis d'Antics municipis: municipi històric al moment de
l'agregació (1897/1904/1921). Els mercats sense sub-municipi al plànol (Les Corts)
queden amb la zona mare.
"""

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "content/ca/elements"

# slug -> zona (full)
ZONES = {
    # Ciutat Vella
    "mercat-de-la-boqueira": None,  # placeholder per error tipogràfic, mai usat
}

MAPA = {
    # ── Ciutat Vella ──
    "mercat-de-la-boqueria": "Ciutat Vella",
    "mercat-de-santa-caterina-i-habitatges-per-ancians": "Ciutat Vella",
    "mercat-de-la-barceloneta": "Ciutat Vella",
    "el-born-muhba-mercat-del-born": "Ciutat Vella",
    # ── Eixample ──
    "mercat-de-sant-antoni": "Eixample",
    "mercat-de-la-concepcio": "Eixample",
    "mercat-de-la-sagrada-familia": "Eixample",
    "mercat-del-ninot": "Eixample",
    "illa-dequipaments-fort-pienc": "Eixample",
    # ── Antics municipis: sense sub-zona al plànol ──
    "mercat-de-les-corts": "Antics municipis",
    # ── Antics municipis: Sants (municipi Santa Maria de Sants) ──
    "mercat-de-sants": "Sants",
    "mercat-dhostafrancs": "Sants",
    "mercat-de-la-marina": "Sants",
    "placa-i-mercat-de-la-marina": "Sants",
    # ── Antics municipis: Sarrià (annexionat 1921) ──
    "mercat-de-sarria": "Sarrià",
    # ── Antics municipis: Sant Gervasi (municipi Sant Gervasi de Cassoles) ──
    "mercat-de-sant-gervasi": "Sant Gervasi",
    "mercat-de-galvany": "Sant Gervasi",
    # DUBTÓS: les Tres Torres podria ser Sarrià; validar amb Xavi
    "mercat-de-les-tres-torres": "Sant Gervasi",
    # ── Antics municipis: Gràcia ──
    "mercat-de-la-llibertat": "Gràcia",
    "mercat-de-lesseps": "Gràcia",
    "mercat-de-lestrella": "Gràcia",
    "mercat-delabaceria": "Gràcia",
    # ── Antics municipis: Horta (annexionat 1904) ──
    "mercat-dhorta": "Horta",
    "mercat-del-carmel": "Horta",
    "mercat-del-guinardo": "Horta",
    "mercat-de-la-vall-dhebron-teixonera": "Horta",
    # ── Antics municipis: Sant Andreu ──
    "mercat-de-sant-andreu": "Sant Andreu",
    "mercat-del-bon-pastor": "Sant Andreu",
    # ── Antics municipis: Sant Martí de Provençals ──
    "mercat-de-sant-marti": "Sant Martí de Provençals",
    "mercat-de-felip-ii": "Sant Martí de Provençals",
    "mercat-de-provencals": "Sant Martí de Provençals",
    "mercat-del-clot": "Sant Martí de Provençals",
    "mercat-del-poblenou": "Sant Martí de Provençals",
    "mercat-del-besos": "Sant Martí de Provençals",
    # ── Nous barris (ona de construcció 1950-1970) ──
    "mercat-de-canyelles": "Nous barris",
    "mercat-de-ciutat-meridiana": "Nous barris",
    "mercat-de-la-guineueta": "Nous barris",
    "mercat-de-la-merce": "Nous barris",
    "mercat-de-la-montserrat": "Nous barris",
    "mercat-de-la-trinitat": "Nous barris",
    "mercat-de-nuria": "Nous barris",
    # ── Mercats no alimentaris ──
    "mercat-dels-encants-fira-de-bellcaire": "Mercats no alimentaris",
}


def afegeix_zona(path: Path, zona: str) -> bool:
    text = path.read_text(encoding="utf-8")
    m = re.search(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not m:
        print(f"  !! sense frontmatter: {path.name}")
        return False
    fm = m.group(1)
    if re.search(r"^zona:", fm, re.MULTILINE):
        return False  # ja el té
    if re.search(r"^districte:.*$", fm, re.MULTILINE):
        def repl(mo):
            return mo.group(1) + f'\nzona: "{zona}"'
        fm_nou = re.sub(
            r"^(districte:.*)$",
            repl,
            fm,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        fm_nou = fm + f'\nzona: "{zona}"'
    text_nou = text[: m.start(1)] + fm_nou + text[m.end(1) :]
    path.write_text(text_nou, encoding="utf-8")
    return True


def main() -> int:
    n_ok, n_falten = 0, []
    for slug, zona in MAPA.items():
        fitxa = BASE / f"{slug}.md"
        if not fitxa.exists():
            n_falten.append(slug)
            continue
        if afegeix_zona(fitxa, zona):
            n_ok += 1

    # Verificació: cap fitxa de la publicació 'mercats' sense zona
    pub_mercats = set(MAPA)
    for fitxa in sorted(BASE.glob("*.md")):
        if fitxa.stem in pub_mercats:
            continue
        text = fitxa.read_text(encoding="utf-8")
        m = re.search(r"^publicacions:\n((?:- .*\n)+)", text, re.MULTILINE)
        if m and re.search(r"^- mercats$", m.group(1), re.MULTILINE):
            n_falten.append(fitxa.stem)

    print(f"zones afegides: {n_ok}")
    if n_falten:
        print(f"ATENCIÓ ({len(n_falten)}): fitxes de mercats sense mapa:")
        for s in n_falten:
            print(f"  - {s}")
        return 1
    print("cap fitxa de mercats pendents de zona")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
