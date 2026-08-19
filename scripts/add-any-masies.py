#!/usr/bin/env python3
"""
Canvi 2a: Afegir camp `any` (en format "s. XIV") a les masies que no el tinguin.
Extreu el(s) numeral(s) romà(ns) del camp `descripcio` del frontmatter YAML.
"""
import re
import os
import sys
import yaml

BASE = os.path.join(os.path.dirname(__file__), '..', 'content', 'ca', 'elements')
BASE = os.path.abspath(BASE)

# Patrons de cerca de segles en català dins el text de descripcio
# Exemple: "segle XV", "segles XIV-XV", "s. XVII", "segles XIV i XV", "s. XIV-XV"
# Numerals romans vàlids per a segles (I fins a XXI)
ROMANS = r'(?:X{0,2}(?:IX|IV|V?I{0,3}))'  # I..XII etc — grup simple
# Patró complet:
SGLE_RE = re.compile(
    r'\b(?:segles?|s\.)\s+'           # "segle", "segles", "s."
    r'(' + ROMANS + r'(?:[-–]\s*' + ROMANS + r')?)',  # XIV o XIV-XV
    re.IGNORECASE
)
# Alternativa: numeral romà sol precedit d'espai (menys prioritari)
SGLE_SOL_RE = re.compile(
    r'\bsegle\s+(' + ROMANS + r')',
    re.IGNORECASE
)

def normalitza_numeral(s):
    """Retorna el numeral en majúscules, netejant espais."""
    return re.sub(r'\s+', '', s).upper()

def extreu_segle(text):
    """Retorna string 's. XIV' o 's. XIV-XV' si en troba, o None."""
    m = SGLE_RE.search(text)
    if m:
        raw = m.group(1).strip()
        # Neteja el guió amb possibles espais
        raw = re.sub(r'\s*[-–]\s*', '-', raw)
        return 's. ' + normalitza_numeral(raw)
    return None

def insereix_any_al_frontmatter(fm_text, valor):
    """Insereix 'any: valor' just abans de 'draft:' o al final del frontmatter."""
    linia = f"any: '{valor}'\n"
    # Preferentment inserir abans de 'draft:'
    if re.search(r'^draft:', fm_text, re.MULTILINE):
        return re.sub(r'^(draft:)', linia + r'\1', fm_text, count=1, flags=re.MULTILINE)
    # Si no, afegir al final (abans del \n final)
    return fm_text.rstrip('\n') + '\n' + linia + '\n'

modified = []
no_data = []
ja_te_any = []

for fname in sorted(os.listdir(BASE)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(BASE, fname)
    content = open(fpath, encoding='utf-8').read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue
    fm = parts[1]

    # Filtrar: ha de tenir masies a publicacions
    if 'masies' not in fm:
        continue

    # Ja té camp any?
    if re.search(r'^any:', fm, re.MULTILINE):
        ja_te_any.append(fname)
        continue

    # Buscar al camp descripcio (dins el frontmatter YAML)
    descripcio_m = re.search(r'^descripcio:\s*(.+?)(?=\n\w|\Z)', fm, re.MULTILINE | re.DOTALL)
    descripcio = ''
    if descripcio_m:
        descripcio = descripcio_m.group(1).strip()

    # Si no hi ha descripcio al frontmatter, mirar el cos del document
    if not descripcio:
        descripcio = parts[2]

    segle = extreu_segle(descripcio)
    if not segle:
        no_data.append(fname)
        continue

    # Inserir camp any
    new_fm = insereix_any_al_frontmatter(fm, segle)
    new_content = '---' + new_fm + '---' + parts[2]
    open(fpath, 'w', encoding='utf-8').write(new_content)
    modified.append((fname, segle))

print(f"=== Masies amb any afegit ({len(modified)}) ===")
for fname, s in modified:
    print(f"  {fname}  =>  {s}")

print(f"\n=== Masies que ja tenien camp any ({len(ja_te_any)}) ===")
for f in ja_te_any:
    print(f"  {f}")

print(f"\n=== Masies SENSE data trobada ({len(no_data)}) — cal revisar manualment ===")
for f in no_data:
    print(f"  {f}")

print(f"\nResum: {len(modified)} afegides | {len(ja_te_any)} ja tenien any | {len(no_data)} sense dades")
