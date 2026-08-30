#!/usr/bin/env python3
"""
Importa les fotos del plànol 1975-2008 (76-08) des de la carpeta Fotos-web-app.
- Copia i renombra cada foto al directori static/img/elements/
- Actualitza el camp `foto` al frontmatter YAML de cada fitxa .md
- Salta les que ja existeixen
"""

import os
import shutil
import re

SRC_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements/Fotos-web-app/1975-2008/1975-2008 fotos"
DST_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/static/img/elements"
CONTENT_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/content/ca/elements"

# Número del PDF → slug de la fitxa
# Quan hi ha diverses fotos del mateix número (a, b, c...) s'escull la primera disponible
MAPPING = {
    2:  "velodrom-municipal-dhorta",
    4:  "reforma-i-millora-de-les-places-de-gracia",
    5:  "jardins-de-la-villa-cecilia",
    6:  "parc-del-clot",
    7:  "via-julia",
    8:  "seu-central-de-la-diputacio-de-barcelona",
    10: "moll-de-la-fusta",
    11: "parc-de-la-creueta-del-coll",
    12: "escola-josep-maria-jujol",
    13: "cosmocaixa-barcelona",
    14: "48-habitatges-i-centre-civic",
    18: "installacions-dentrenament-de-tir-amb-arc",
    19: "escola-municipal-de-vela",
    20: "piscina-de-salts-de-montjuic",
    22: "conjunt-dhabitatges-tirant-lo-blanc",
    24: "edifici-porta-vila-olimpica",
    25: "residencia-geriatrica-dhorta",
    26: "tres-illes-dhabitatges-a-leixample-de-cerda",
    27: "centre-de-cultura-contemporania-de-barcelona-cccb",
    28: "illa-diagonal",
    29: "parc-del-nus-de-la-trinitat",
    30: "palau-nou-de-la-rambla",
    31: "aparthotel-citadines",
    32: "museu-dart-contemporani-de-barcelona-macba",
    33: "edifici-dhabitatges",
    35: "jardi-botanic-de-barcelona",
    36: "lauditori",
    38: "parc-diagonal-mar",
    40: "caixaforum",
    42: "parc-central-de-nou-barris",
    43: "ordenacio-de-la-ronda-del-mig-rambla-brasil",
    44: "esplanada-forum-pergola-fotovoltaica",
    45: "centre-de-convencions-internacional-de-catalunya-ccib",
    47: "habitatges-diagonal-mar-illa-de-la-llum",
    50: "edifici-dhabitatges-i-escola-mallorca",
    51: "parc-de-recerca-biomedica-de-barcelona-prbb",
    54: "habitatges-per-a-joves",
    56: "habitatges-de-proteccio-oficial-per-a-joves",
    57: "habitatges-vertix",
    58: "habitatges-socials-al-22",
    59: "edifici-mediapro",
    60: "edifici-dhabitatges-per-a-gent-gran",
    61: "habitatges-socials-per-a-joves-can-caralleu",
    62: "museu-can-framis-i-jardins-de-miquel-marti-i-pol",
    63: "habitatges-mas-de-roda",
    64: "edifici-media-tic",
    65: "seu-de-la-cmt",
    66: "plug-in-building",
    67: "filmoteca-de-catalunya",
}


def parse_num(filename):
    """Extreu el número del nom de fitxer tipus '02 b.jpg' o '40.jpg'."""
    m = re.match(r'^(\d+)', filename)
    return int(m.group(1)) if m else None


def update_foto_field(slug, foto_value):
    """Afegeix o actualitza el camp `foto` al frontmatter YAML d'una fitxa .md."""
    md_path = os.path.join(CONTENT_DIR, f"{slug}.md")
    if not os.path.exists(md_path):
        print(f"  [AVÍS] Fitxa no trobada: {md_path}")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Comprova si ja té camp foto
    if re.search(r'^foto:', content, re.MULTILINE):
        print(f"  [INFO] {slug}.md ja té camp foto, no es modifica")
        return

    # Insereix foto: just abans del tancament ---
    new_content = re.sub(
        r'^(---)(\s*\n)',
        r'\1\2',
        content
    )
    # Insereix la línia foto: just abans del --- de tancament
    new_content = re.sub(
        r'^---\s*$',
        f"foto: {foto_value}\n---",
        content,
        count=1,  # Només el primer ---
        flags=re.MULTILINE
    )
    # Fem-ho bé: inserim avant el segon ---
    parts = content.split("---", 2)
    if len(parts) >= 3:
        parts[1] = parts[1].rstrip("\n") + f"\nfoto: {foto_value}\n"
        new_content = "---".join(parts)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  [OK] foto afegida a {slug}.md")
    else:
        print(f"  [AVÍS] Format frontmatter inesperat a {slug}.md")


# Construeix un dict num → fitxer font (la primera foto disponible per número)
src_files = sorted(os.listdir(SRC_DIR))
num_to_src = {}
for fname in src_files:
    if not fname.lower().endswith(".jpg"):
        continue
    num = parse_num(fname)
    if num is not None and num not in num_to_src:
        num_to_src[num] = fname

print("=== Importació fotos 76-08 ===\n")

copied = 0
skipped_existing = 0
no_photo = []

for num, slug in sorted(MAPPING.items()):
    dst_path = os.path.join(DST_DIR, f"{slug}.jpg")

    if os.path.exists(dst_path):
        print(f"[SALTA] {slug}.jpg ja existeix")
        skipped_existing += 1
        continue

    if num not in num_to_src:
        print(f"[MANCA] #{num:02d} → {slug} (no hi ha foto a la carpeta)")
        no_photo.append((num, slug))
        continue

    src_fname = num_to_src[num]
    src_path = os.path.join(SRC_DIR, src_fname)
    shutil.copy2(src_path, dst_path)
    print(f"[COPIA] '{src_fname}' → '{slug}.jpg'")
    update_foto_field(slug, f"img/elements/{slug}.jpg")
    copied += 1

print(f"\n=== Resum ===")
print(f"Copiades:          {copied}")
print(f"Ja existien:       {skipped_existing}")
print(f"Sense foto (PDF):  {len(no_photo)}")
if no_photo:
    print("  Fitxes sense foto disponible:")
    for num, slug in no_photo:
        print(f"    #{num:02d} {slug}")
