#!/usr/bin/env python3
"""
Corregeix els valors de districte: barri → districte oficial de Barcelona.
Afegit després del geocodificació Nominatim que retornava noms de barri.
"""
import re
import os
import sys

BASE = os.path.join(os.path.dirname(__file__), '..', 'content', 'ca', 'elements')
BASE = os.path.abspath(BASE)

# Mapping barri → districte oficial (10 districtes de Barcelona)
MAPPING = {
    # Ciutat Vella
    'el Gòtic': 'Ciutat Vella',
    'el Raval': 'Ciutat Vella',
    'la Barceloneta': 'Ciutat Vella',
    # Eixample
    'el Fort Pienc': 'Eixample',
    'la Sagrada Família': 'Eixample',
    'Sant Antoni': 'Eixample',
    "l'Antiga Esquerra de l'Eixample": 'Eixample',
    "la Dreta de l'Eixample": 'Eixample',
    "el Camp de l'Arpa del Clot": 'Eixample',
    # Sants-Montjuïc
    'Hostafrancs': 'Sants-Montjuïc',
    'la Bordeta': 'Sants-Montjuïc',
    'la Font de la Guatlla': 'Sants-Montjuïc',
    'el Poble-sec': 'Sants-Montjuïc',
    'Pedralbes': 'Sants-Montjuïc',
    'la Marina de Port': 'Sants-Montjuïc',
    'la Montserratina': 'Sants-Montjuïc',
    'Montjuïc': 'Sants-Montjuïc',
    # Les Corts
    'la Maternitat i Sant Ramon': 'Les Corts',
    'les Corts': 'Les Corts',
    # Sarrià-Sant Gervasi
    'Sant Gervasi - la Bonanova': 'Sarrià-Sant Gervasi',
    'Sant Gervasi - Galvany': 'Sarrià-Sant Gervasi',
    'les Tres Torres': 'Sarrià-Sant Gervasi',
    'Vallvidrera, el Tibidabo i les Planes': 'Sarrià-Sant Gervasi',
    'Canitelles': 'Sarrià-Sant Gervasi',
    'Sarrià': 'Sarrià-Sant Gervasi',
    # Gràcia
    'el Coll': 'Gràcia',
    'la Salut': 'Gràcia',
    'la Vila de Gràcia': 'Gràcia',
    'Vallcarca i els Penitents': 'Gràcia',
    'el Baix Guinardó': 'Gràcia',
    "la Font d'en Fargues": 'Gràcia',
    # Horta-Guinardó
    'el Carmel': 'Horta-Guinardó',
    'el Guinardó': 'Horta-Guinardó',
    'Can Baró': 'Horta-Guinardó',
    'Sant Genís dels Agudells': 'Horta-Guinardó',
    'Montbau': 'Horta-Guinardó',
    'la Teixonera': 'Horta-Guinardó',
    # Nou Barris
    'Canyelles': 'Nou Barris',
    'Ciutat Meridiana': 'Nou Barris',
    'la Trinitat Nova': 'Nou Barris',
    'les Roquetes': 'Nou Barris',
    'Vallbona': 'Nou Barris',
    'el Turó de la Peira': 'Nou Barris',
    'la Prosperitat': 'Nou Barris',
    # Sant Andreu
    'el Bon Pastor': 'Sant Andreu',
    'la Trinitat Vella': 'Sant Andreu',
    'Torre Baró': 'Sant Andreu',
    'el Congrés i els Indians': 'Sant Andreu',
    'Porta': 'Sant Andreu',
    'Baró de Viver': 'Sant Andreu',
    # Sant Martí
    'el Poblenou': 'Sant Martí',
    'el Clot': 'Sant Martí',
    'la Verneda i la Pau': 'Sant Martí',
    'el Besòs i el Maresme': 'Sant Martí',
    'Provençals del Poblenou': 'Sant Martí',
    'el Parc i la Llacuna del Poblenou': 'Sant Martí',
    'la Vila Olímpica del Poblenou': 'Sant Martí',
    'la Sagrera': 'Sant Martí',
    # Barris addicionals (segona passada)
    'Sant Pere, Santa Caterina i la Ribera': 'Ciutat Vella',
    'la Marina del Prat Vermell': 'Sants-Montjuïc',
    'la Guineueta': 'Nou Barris',
    'Vilapicina i la Torre Llobeta': 'Nou Barris',
    "la Vall d'Hebron": 'Horta-Guinardó',
}

# districtes oficials (per no tocar-los si ja són correctes)
DISTRICTES_OFICIALS = {
    'Ciutat Vella', 'Eixample', 'Sants-Montjuïc', 'Les Corts',
    'Sarrià-Sant Gervasi', 'Gràcia', 'Horta-Guinardó',
    'Nou Barris', 'Sant Andreu', 'Sant Martí',
}

modified = []
already_ok = []
unknown = []

for fname in sorted(os.listdir(BASE)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(BASE, fname)
    content = open(fpath, encoding='utf-8').read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue
    fm = parts[1]

    m = re.search(r'^districte:\s*"([^"]+)"', fm, re.MULTILINE)
    if not m:
        continue

    actual = m.group(1).strip()

    # Ja és districte oficial?
    if actual in DISTRICTES_OFICIALS:
        already_ok.append((fname, actual))
        continue

    # És al mapping?
    if actual in MAPPING:
        nou = MAPPING[actual]
        new_fm = fm.replace(f'districte: "{actual}"', f'districte: "{nou}"')
        new_content = '---' + new_fm + '---' + parts[2]
        open(fpath, 'w', encoding='utf-8').write(new_content)
        modified.append((fname, actual, nou))
        print(f"  {fname}: \"{actual}\" → \"{nou}\"")
    else:
        unknown.append((fname, actual))
        print(f"  ??? {fname}: \"{actual}\" — NO MAPEJAT")

print(f"\n=== Resum ===")
print(f"  Corregides: {len(modified)}")
print(f"  Ja eren correctes: {len(already_ok)}")
print(f"  Sense mapeig: {len(unknown)}")
if unknown:
    print("\nSense mapejar:")
    for f, v in unknown:
        print(f"  {f}: \"{v}\"")
