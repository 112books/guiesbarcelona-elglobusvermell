#!/usr/bin/env python3
"""Comprova que el CSS publicat contingui els selectors crítics.

Evita publicar un web sense estils clau (com va passar el 2026-09-30 amb el
formulari de contacte i el bloc de xifres). S'executa després del build.

Ús: python3 scripts/comprova-css.py
"""
import re
import pathlib
import sys

PUBLIC = pathlib.Path("public")

CRITICS = {
    ".contacte-form": "formulari de contacte",
    ".form-input": "camps del formulari",
    ".stats-grid": "El projecte en xifres",
    ".credits-stats": "bloc de xifres",
    ".en-paper": "pàgina En paper",
    ".en-plan": "llista de plànols (En paper)",
    ".tts-btn": "botó Escoltar",
    ".cerca-resultat": "resultats de la cerca del mapa",
    ".site-header-inner": "capçalera alineada amb el cos",
    ".portada-nav": "navegació per blocs de la portada",
    ".splash-mobil": "splash del mòbil",
    ".tema-info": "informació dels temes transversals",
    ".fitxa-imatge": "fitxes d'element",
    ".publicacio": "pàgina de publicació",
    ".filtre-btn": "filtres del mapa",
    ".mapa-el": "mapa",
    ".pa-stats": "xifres de la portada",
    ".footer-main": "peu de pàgina",
}


def main():
    index = PUBLIC / "index.html"
    if not index.exists():
        print("ERROR: no existeix public/index.html; cal fer el build abans.")
        return 2
    html = index.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"/css/(main\.min\.[a-f0-9]+\.css)", html)
    if not m:
        print("ERROR: no s'ha trobat l'enllaç al CSS principal a public/index.html.")
        return 2
    css_path = PUBLIC / "css" / m.group(1)
    if not css_path.exists():
        print("ERROR: no existeix " + str(css_path) + ".")
        return 2
    css = css_path.read_text(encoding="utf-8", errors="replace")
    missing = [k for k in CRITICS if k not in css]
    print("CSS comprovat: " + str(css_path) + " (" + str(len(css)) + " bytes)")
    if missing:
        print("FALTEN selectors crítics:")
        for k in missing:
            print("  - " + k + "  (" + CRITICS[k] + ")")
        return 1
    print("OK: tots els " + str(len(CRITICS)) + " selectors crítics hi són.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
