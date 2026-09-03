#!/usr/bin/env python3
"""Genera data/imatges_dims.json amb les dimensions (amplada, alçada) de totes
les imatges de static/img — les fa servir single.html per als atributs
width/height dels <img> de les fitxes (evitar canvis de disseny en carregar, CLS).

Re-executable: es pot tornar a correr sempre que s'afegeixin o substitueixin imatges.
Usa Pillow (pip install Pillow) amb fallback a ImageMagick si Pillow no és disponible.
"""
import json
import os
import subprocess
import sys

BASES = ["static/img/elements", "static/img/publicacions"]
SORTIDA = "data/imatges_dims.json"

def get_dims(cami):
    try:
        from PIL import Image
        with Image.open(cami) as img:
            return img.size  # (width, height)
    except ImportError:
        pass
    # Fallback: ImageMagick
    try:
        out = subprocess.check_output(
            ["magick", "identify", "-format", "%w %h", cami + "[0]"]
        ).decode().strip()
        parts = out.split()
        return int(parts[0]), int(parts[1])
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def main():
    dims = {}
    for base in BASES:
        if not os.path.isdir(base):
            continue
        fitxes = sorted(f for f in os.listdir(base) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))
        for nom in fitxes:
            cami = os.path.join(base, nom)
            result = get_dims(cami)
            if result is None:
                print(f"AVIS: no he pogut llegir {cami}", file=sys.stderr)
                continue
            dims[nom] = [result[0], result[1]]
    with open(SORTIDA, "w", encoding="utf-8") as fp:
        json.dump(dims, fp, separators=(",", ":"), sort_keys=True)
    print(f"{SORTIDA}: {len(dims)} imatges")

if __name__ == "__main__":
    main()
