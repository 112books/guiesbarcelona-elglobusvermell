#!/usr/bin/env python3
"""Genera data/imatges_dims.json amb les dimensions (amplada, alçada) de totes
les imatges de static/img — les fa servir single.html per als atributs
width/height dels <img> de les fitxes (evitar canvis de disseny en carregar, CLS).

Re-executable: es pot tornar a correr sempre que s'afegeixin o substitueixin imatges.
Requereix ImageMagick (magick).
"""
import json
import os
import subprocess
import sys

BASES = ["static/img/elements", "static/img/publicacions"]
SORTIDA = "data/imatges_dims.json"

def main():
    dims = {}
    for base in BASES:
        fitxes = sorted(f for f in os.listdir(base) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))
        for nom in fitxes:
            cami = os.path.join(base, nom)
            try:
                out = subprocess.check_output(
                    ["magick", "identify", "-format", "%w %h", cami + "[0]"]
                ).decode().strip()
            except subprocess.CalledProcessError:
                print(f"AVÍS: no he pogut llegir {cami}", file=sys.stderr)
                continue
            parts = out.split()
            dims[nom] = [int(parts[0]), int(parts[1])]
    with open(SORTIDA, "w", encoding="utf-8") as fp:
        json.dump(dims, fp, separators=(",", ":"), sort_keys=True)
    print(f"{SORTIDA}: {len(dims)} imatges")

if __name__ == "__main__":
    main()
