#!/usr/bin/env python3
"""Importa fotos del plànol Biblioteques des de Fotos-web-app."""
import os, shutil, re

SRC_DIR   = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements/Fotos-web-app/biblioteques/biblioteques fotos"
DST_DIR   = "/Users/joan/Documents/Obsidian/elglobusvermell.org/static/img/elements"
CONTENT_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/content/ca/elements"

MAPPING = {
    4:  "biblioteca-sant-pau-santa-creu",
    5:  "edifici-collage-centre-cultural-teresa-pamies",
    7:  "biblioteca-joan-miro",
    8:  "biblioteca-sagrada-familia-josep-maria-ainaud-de-lasarte",
    9:  "biblioteca-sant-antoni-joan-oliver-casal-davis-i-jardins-de-candida-perez",
    14: "biblioteca-vapor-vell",
    15: "biblioteca-montserrat-abello",
    16: "biblioteca-les-corts-miquel-llongueras",
    17: "biblioteca-clara",
    21: "biblioteca-sarria-j-v-foix",
    24: "biblioteca-vila-de-gracia-rosa-maria-arquimbau",
    28: "biblioteca-montbau-albert-perez-baro",
    31: "biblioteca-nou-barris-aurora-diaz-plaja",
    33: "biblioteca-vilapicina-i-la-torre-llobeta-carmen-laforet",
    34: "biblioteca-zona-nord-maria-sanchez",
    36: "biblioteca-ignasi-iglesias-can-fabra",
    37: "biblioteca-la-sagrera-marina-clotet",
    38: "biblioteca-trinitat-vella-jose-barbero",
    39: "illa-dequipaments-alchemika",
    41: "biblioteca-gabriel-garcia-marquez",
    42: "biblioteca-poblenou-manuel-arranz",
    49: "pavello-de-la-republica-biblioteca-crai-ub",
    50: "biblioteca-crai-de-la-ciutadella-diposit-de-les-aigues-universitat-pompeu-fabra",
}

MISSING_SLUGS = [
    (6, "Biblioteca Fort Pienc - Ana María Moix — sense slug al contingut"),
]

def parse_num(f):
    m = re.match(r'^(\d+)[_\s]', f)
    return int(m.group(1)) if m else None

def update_foto(slug, val):
    path = os.path.join(CONTENT_DIR, f"{slug}.md")
    if not os.path.exists(path): print(f"  [AVÍS] no trobat: {slug}.md"); return
    c = open(path, encoding="utf-8").read()
    if re.search(r'^foto:', c, re.MULTILINE): print(f"  [INFO] ja té foto: {slug}.md"); return
    parts = c.split("---", 2)
    if len(parts) >= 3:
        parts[1] = parts[1].rstrip("\n") + f"\nfoto: {val}\n"
        open(path, "w", encoding="utf-8").write("---".join(parts))
        print(f"  [OK] foto → {slug}.md")
    else: print(f"  [AVÍS] frontmatter inesperat: {slug}.md")

src_files = sorted(os.listdir(SRC_DIR))
num_to_src = {}
for f in src_files:
    if not f.lower().endswith(".jpg"): continue
    n = parse_num(f)
    if n is not None and n not in num_to_src: num_to_src[n] = f

print("=== Importació fotos Biblioteques ===\n")
copied = skipped = 0; no_photo = []

for num, slug in sorted(MAPPING.items()):
    dst = os.path.join(DST_DIR, f"{slug}.jpg")
    if os.path.exists(dst): print(f"[SALTA] {slug}.jpg ja existeix"); skipped += 1; continue
    if num not in num_to_src: print(f"[MANCA] #{num:02d} → {slug}"); no_photo.append((num, slug)); continue
    shutil.copy2(os.path.join(SRC_DIR, num_to_src[num]), dst)
    print(f"[COPIA] '{num_to_src[num]}' → '{slug}.jpg'")
    update_foto(slug, f"{slug}.jpg"); copied += 1

print(f"\n=== Resum ===\nCopiades: {copied} | Ja existien: {skipped} | Sense foto: {len(no_photo)}")
if no_photo:
    for n, s in no_photo: print(f"    #{n:02d} {s}")
print("\nSense slug (cal crear):")
for n, d in MISSING_SLUGS: print(f"    #{n:02d} {d}")
