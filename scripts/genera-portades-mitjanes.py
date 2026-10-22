#!/usr/bin/env python3
"""Genera les portades de mida mitjana (<slug>-560.jpg) per a carrusel i llistats.

Les portades petites (<slug>.jpg, 212x300) es veuen borroses a «En paper»
(264 px, i el doble en pantalles retina). Aquest script en fa una versió de
560 px d'amplada a partir de la versió gran en català (<slug>-cat.jpg).
Les plantilles fan servir <slug>-560.jpg si existeix i, si no, <slug>.jpg.

Només regenera si la mitjana no existeix o és més antiga que l'original.

Us:
  python3 scripts/genera-portades-mitjanes.py
  python3 scripts/genera-portades-mitjanes.py --dry-run
  python3 scripts/genera-portades-mitjanes.py --totes      # al CI
"""
import argparse
import os
import re

from PIL import Image

CARPETA = "static/img/publicacions"
AMPLADA = 560


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--totes", action="store_true", help="regenera-les totes (CI: al checkout les dates no són fiables)")
    args = ap.parse_args()
    fets = 0
    for nom in sorted(os.listdir(CARPETA)):
        m = re.fullmatch(r"(.+)-cat\.jpg", nom)
        if not m:
            continue
        origen = os.path.join(CARPETA, nom)
        desti = os.path.join(CARPETA, f"{m.group(1)}-{AMPLADA}.jpg")
        if not args.totes and os.path.exists(desti) and os.path.getmtime(desti) >= os.path.getmtime(origen):
            continue
        if args.dry_run:
            print(f"generaria: {desti}")
            continue
        with Image.open(origen) as img:
            img = img.convert("RGB")
            alcada = round(img.height * AMPLADA / img.width)
            img.resize((AMPLADA, alcada), Image.LANCZOS).save(desti, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"generada: {desti}  ({os.path.getsize(desti) // 1024} KB)")
        fets += 1
    print(f"{fets} portades mitjanes generades")


if __name__ == "__main__":
    main()
