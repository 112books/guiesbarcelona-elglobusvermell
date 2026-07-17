#!/usr/bin/env python3
"""Remove downloaded placeholder/category-cover files (not real building photos)."""
import os

STATIC_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements"

# Known placeholder file sizes (category cover images, not building photos)
PLACEHOLDER_SIZES = {
    39289,   # cropped-AU-guies_logoweb-gris-1.jpg (site logo)
    617980,  # gatpac.jpg (avantguarda category cover)
    276543,  # poblenou.jpg (poblenou-industrial category cover)
    571022,  # jardins.jpg (eixample-jardins category cover)
}

# These were already there before the script ran (real building photos)
KEEP = {
    'biblioteca-el-clot-josep-benet.jpg',
    'casa-bloc.jpg',
    'farinera-sant-jaume-la-farinera-del-clot.jpg',
    'fundacio-joan-miro.jpg',
    'jardins-ada-byron.jpg',
    'jardins-dada-byron.jpg',
    'la-ciutat-groga.jpg',
    'les-escales-park.jpg',
    'mercat-dels-encants-fira-de-bellcaire.jpg',
    'pavello-de-la-republica-de-1937-replica.jpg',
}

removed = []
kept = []
for fname in os.listdir(STATIC_DIR):
    fpath = os.path.join(STATIC_DIR, fname)
    if fname in KEEP:
        kept.append(fname)
        continue
    size = os.path.getsize(fpath)
    if size in PLACEHOLDER_SIZES:
        os.remove(fpath)
        removed.append(f"{fname} ({size} bytes)")
    else:
        kept.append(f"{fname} ({size} bytes)")

print(f"Removed {len(removed)} placeholder files:")
for f in sorted(removed):
    print(f"  {f}")
print(f"\nKept {len(kept)} files:")
for f in sorted(kept):
    print(f"  {f}")
