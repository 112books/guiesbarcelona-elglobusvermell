#!/usr/bin/env python3
"""
Importa les fotos del plànol 2010-2025 (09-25) des de la carpeta Fotos-web-app.
- Copia i renombra cada foto al directori static/img/elements/
- Actualitza el camp `foto` al frontmatter YAML de cada fitxa .md
- Salta les que ja existeixen
- Quan hi ha foto _portada disponible, la prefereix
"""

import os
import shutil
import re

SRC_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements/Fotos-web-app/2010-2025/2010-2025 fotos"
DST_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/static/img/elements"
CONTENT_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/content/ca/elements"

# Número del PDF → slug de la fitxa
MAPPING = {
    1:  "passeig-de-sant-joan",
    5:  "edifici-collage-centre-cultural-teresa-pamies",
    6:  "el-born-muhba-mercat-del-born",
    7:  "entorns-del-mercat-del-born",
    8:  "villa-urania",
    9:  "rehabilitacio-de-les-bateries-antiaeries",
    10: "biblioteca-sant-gervasi-joan-maragall",
    11: "skate-park-mar-bella",
    13: "illa-dequipaments-alchemika",
    14: "escola-dels-encants",
    16: "cooperativa-pau-i-justicia-sala-beckett",
    17: "cristalleries-planell",
    18: "edifici-dhabitatges-110-rooms",
    19: "rambla-de-sants-jardins-elevats-de-sants",
    22: "jardins-del-doctor-pla-i-armengol",
    23: "estudis-industrials",
    24: "la-borda-cohabitatges-cooperatius",
    25: "jardins-antonia-vilas",
    26: "casal-de-barri-de-trinitat-nova",
    27: "edifici-dhabitatges-aprop-ciutat-vella",
    28: "centre-de-vida-comunitaria-de-trinitat-vella",
    29: "poliesportiu-turo-de-la-peira",
    31: "la-comunal-espai-cooperatiu",
    32: "carrer-cristobal-de-moura",
    34: "edifici-dhabitatges-per-a-4-amics",
    35: "centre-kalida",
    36: "oliva-artes-muhba",
    37: "edifici-dhabitatges-ali-bei",
    38: "poliesportiu-municipal-camp-del-ferro",
    39: "la-balma-cohabitatges-cooperatius",
    41: "escola-la-mar-bella",
    43: "edifici-residencial",
    44: "edifici-dhabitatges-set-vides",
    45: "biblioteca-gabriel-garcia-marquez",
    47: "placa-soller-i-ateneu-la-bobila",
    48: "edifici-doficines",
    51: "jardins-de-ca-laranyo",
    52: "edifici-doficines-entegra",
    53: "eixos-verds-de-leixample-superilla",
    54: "torre-de-bombers",
    59: "switch-nova-seu-de-simon",
    60: "conjunt-dhabitatges-illa-glories",
    62: "edifici-dhabitatges-dotacionals-greenhuse",
    63: "lci-barcelona-22-campus",
    65: "parc-de-les-glories",
}

# Ítems del PDF sense fitxa al contingut (cal crear-los manualment)
MISSING_SLUGS = [
    (64, "Edifici d'oficines Llull 122 — sense fitxa a content/ca/elements/"),
]


def parse_num(filename):
    m = re.match(r'^(\d+)[_\s]', filename)
    return int(m.group(1)) if m else None


def update_foto_field(slug, foto_value):
    md_path = os.path.join(CONTENT_DIR, f"{slug}.md")
    if not os.path.exists(md_path):
        print(f"  [AVÍS] Fitxa no trobada: {slug}.md")
        return
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    if re.search(r'^foto:', content, re.MULTILINE):
        print(f"  [INFO] {slug}.md ja té camp foto, no es modifica")
        return
    parts = content.split("---", 2)
    if len(parts) >= 3:
        parts[1] = parts[1].rstrip("\n") + f"\nfoto: {foto_value}\n"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("---".join(parts))
        print(f"  [OK] foto afegida a {slug}.md")
    else:
        print(f"  [AVÍS] Format frontmatter inesperat a {slug}.md")


# Construeix dict num → fitxer preferit (portada > primera disponible)
src_files = sorted(os.listdir(SRC_DIR))
num_to_src = {}
for fname in src_files:
    if not fname.lower().endswith(".jpg"):
        continue
    num = parse_num(fname)
    if num is None:
        continue
    if num not in num_to_src:
        num_to_src[num] = fname
    elif "_portada" in fname and "_portada" not in num_to_src[num]:
        num_to_src[num] = fname  # preferim la portada

print("=== Importació fotos 2010-2025 (09-25) ===\n")

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
    update_foto_field(slug, f"{slug}.jpg")
    copied += 1

print(f"\n=== Resum ===")
print(f"Copiades:          {copied}")
print(f"Ja existien:       {skipped_existing}")
print(f"Sense foto:        {len(no_photo)}")
if no_photo:
    for num, slug in no_photo:
        print(f"    #{num:02d} {slug}")
print(f"\nFitxes sense slug (cal crear):")
for num, desc in MISSING_SLUGS:
    print(f"    #{num:02d} {desc}")
