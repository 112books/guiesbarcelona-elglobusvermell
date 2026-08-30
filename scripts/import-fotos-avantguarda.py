#!/usr/bin/env python3
"""Importa fotos del plànol Avantguarda (gatcpac) des de Fotos-web-app."""
import os, shutil, re

SRC_DIR   = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements/Fotos-web-app/avantguarda/avantguarda fotos"
DST_DIR   = "/Users/joan/Documents/Obsidian/elglobusvermell.org/static/img/elements"
CONTENT_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/content/ca/elements"

MAPPING = {
    1:  "fabrica-myrurgia",
    3:  "edifici-dhabitatges-carrer-rossello",
    4:  "casa-josefa-lopez",
    5:  "casa-viladot",
    6:  "casa-rodriguez-arias",
    8:  "edifici-dhabitatges-carrer-rector-ubach",
    10: "casa-ginesta",
    13: "grup-escolar-blanquerna",
    14: "edifici-astoria",
    17: "casa-j-espona",
    19: "joieria-roca",
    20: "casa-bloc",
    21: "dispensari-central-antituberculos",
    23: "casa-jaume-sans",
    27: "bloc-diagonal",
    28: "casa-cardenal",
    31: "edifici-dhabitatges-carrer-lincoln",
    37: "edifici-dhabitatges-carrer-viladomat",
    40: "pavello-de-la-republica-biblioteca-crai-ub",
}

MISSING_SLUGS = [
    (35, "Edifici d'habitatges Rosselló 133 — sense slug propi (el slug existent és Rosselló 36)"),
    (39, "Casa Roca Barallat — sense slug al contingut"),
    (43, "Fundació Joan Miró — slug existeix (50-75) però ja té foto"),
]

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
    if not f.lower().endswith(".jpg"): continue
    n = parse_num(f)
    if n is not None and n not in num_to_src: num_to_src[n] = f

print("=== Importació fotos Avantguarda (gatcpac) ===\n")
copied = skipped = 0; no_photo = []

for num, slug in sorted(MAPPING.items()):
    dst = os.path.join(DST_DIR, f"{slug}.jpg")
    if os.path.exists(dst): print(f"[SALTA] {slug}.jpg ja existeix"); skipped += 1; continue
    if num not in num_to_src: print(f"[MANCA] #{num:02d} → {slug}"); no_photo.append((num, slug)); continue
    shutil.copy2(os.path.join(SRC_DIR, num_to_src[num]), dst)
    print(f"[COPIA] '{num_to_src[num]}' → '{slug}.jpg'")
    update_foto(slug, f"img/elements/{slug}.jpg"); copied += 1

print(f"\n=== Resum ===\nCopiades: {copied} | Ja existien: {skipped} | Sense foto: {len(no_photo)}")
if no_photo:
    for n, s in no_photo: print(f"    #{n:02d} {s}")
print("\nSense slug (cal crear o verificar):")
for n, d in MISSING_SLUGS: print(f"    #{n:02d} {d}")
