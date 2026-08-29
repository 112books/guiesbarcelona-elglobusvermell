#!/usr/bin/env python3
"""Importa fotos del plànol Masies des de Fotos-web-app."""
import os, shutil, re

SRC_DIR   = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements/Fotos-web-app/masies/masies fotos"
DST_DIR   = "/Users/joan/Documents/Obsidian/elglobusvermell.org/static/img/elements"
CONTENT_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/content/ca/elements"

MAPPING = {
    3:  "masia-can-bruixa",
    4:  "masia-torre-del-rellotge",
    6:  "masia-la-petita-maria",
    7:  "masia-can-roses",
    9:  "torre-rodona",
    10: "masia-can-canet-de-la-riera",
    12: "masia-can-raspall",
    13: "masia-can-raventos",
    18: "masia-villa-florida",
    19: "masia-can-castello",
    24: "masia-can-tusquets",
    25: "masia-can-xipreret",
    31: "masia-can-garcini",
    32: "masia-mas-guinardo",
    37: "masia-can-gras",
    38: "biblioteca-horta-can-mariner",
    39: "masia-ca-nandalet",
    40: "masia-mas-enric",
    41: "masia-can-travi-nou",
    42: "masia-can-travi-vell",
    43: "masia-can-cortada",
    49: "masia-can-carreras",
    50: "masia-ca-nensenya",
    51: "masia-ca-nartes",
    52: "masia-can-baste",
    53: "masia-torre-llobeta",
    54: "masia-can-verdaguer",
    55: "masia-can-valent",
    59: "masia-can-joanet-del-borni",
    60: "masia-ca-la-xica",
    61: "masia-ca-la-figuera",
    63: "masia-torre-del-fang",
    64: "masia-can-miralletes",
    65: "masia-can-planes",
    66: "masia-rectoria-de-sant-marti",
    67: "masia-ca-larno",
    68: "masia-can-cadena",
}

def parse_num(f):
    m = re.match(r'^(\d+)[_]', f)
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
    if not f.lower().endswith((".jpg", ".jpeg")): continue
    n = parse_num(f)
    if n is not None and n not in num_to_src: num_to_src[n] = f

print("=== Importació fotos Masies ===\n")
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
