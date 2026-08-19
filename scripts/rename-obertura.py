#!/usr/bin/env python3
"""Canvi 1: renombra obertura: -> any: al frontmatter de fitxes interiors-illa."""
import re
import os
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', 'content', 'ca', 'elements')
BASE = os.path.abspath(BASE)

modified = []
skipped = []

for fname in sorted(os.listdir(BASE)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(BASE, fname)
    content = open(fpath, encoding='utf-8').read()

    # Comprovem que té interiors-illa i obertura:
    parts = content.split('---', 2)
    if len(parts) < 3:
        continue
    fm = parts[1]
    if 'interiors-illa' not in fm:
        continue
    if not re.search(r'^obertura:', fm, re.MULTILINE):
        continue

    # Substituïm obertura: -> any: NOMÉS al frontmatter
    new_fm = re.sub(r'^obertura:', 'any:', fm, flags=re.MULTILINE)
    new_content = '---' + new_fm + '---' + parts[2]
    open(fpath, 'w', encoding='utf-8').write(new_content)
    modified.append(fname)

print(f"Fitxes modificades ({len(modified)}):")
for f in modified:
    print(f"  {f}")
print(f"\nTotal: {len(modified)} fitxes")
