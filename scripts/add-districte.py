#!/usr/bin/env python3
"""
Canvi 2b/3/4: Afegir camp `districte` a masies, biblioteques i mercats
via reverse geocoding Nominatim.

Ús:
  python3 add-districte.py masies
  python3 add-districte.py biblioteques
  python3 add-districte.py mercats
  python3 add-districte.py masies biblioteques mercats
"""
import re
import os
import sys
import time
import json
import urllib.request

BASE = os.path.join(os.path.dirname(__file__), '..', 'content', 'ca', 'elements')
BASE = os.path.abspath(BASE)

# Els 10 districtes oficials de Barcelona en ordre oficial
DISTRICTES_OFICIALS = [
    'Ciutat Vella',
    'Eixample',
    'Sants-Montjuïc',
    'Les Corts',
    'Sarrià-Sant Gervasi',
    'Gràcia',
    'Horta-Guinardó',
    'Nou Barris',
    'Sant Andreu',
    'Sant Martí',
]

# Variants -> nom oficial (normalització)
VARIANTS = {
    'ciutat vella': 'Ciutat Vella',
    'eixample': 'Eixample',
    "l'eixample": 'Eixample',
    'sants-montjuic': 'Sants-Montjuïc',
    'sants - montjuic': 'Sants-Montjuïc',
    'sants-montjuïc': 'Sants-Montjuïc',
    'les corts': 'Les Corts',
    'sarrià-sant gervasi': 'Sarrià-Sant Gervasi',
    'sarria-sant gervasi': 'Sarrià-Sant Gervasi',
    'sarrià - sant gervasi': 'Sarrià-Sant Gervasi',
    'gracia': 'Gràcia',
    'gràcia': 'Gràcia',
    'horta-guinardo': 'Horta-Guinardó',
    'horta-guinardó': 'Horta-Guinardó',
    'horta - guinardó': 'Horta-Guinardó',
    'nou barris': 'Nou Barris',
    'sant andreu': 'Sant Andreu',
    'sant martí': 'Sant Martí',
    'sant marti': 'Sant Martí',
}

def normalitza_districte(raw):
    """Retorna el nom oficial del districte o el valor raw amb avís."""
    key = raw.strip().lower()
    if key in VARIANTS:
        return VARIANTS[key], True
    # Cerca parcial
    for variant, oficial in VARIANTS.items():
        if variant in key or key in variant:
            return oficial, True
    return raw.strip(), False

def geocodifica(lat, lon):
    """Crida Nominatim i retorna el districte o None."""
    url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}'
    req = urllib.request.Request(url, headers={'User-Agent': 'guiesbarcelona-geocoder/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"    ERROR HTTP: {e}")
        return None

    addr = data.get('address', {})
    # Ordre de camps a provar
    for camp in ('city_district', 'quarter', 'suburb'):
        val = addr.get(camp)
        if val:
            return val
    return None

def insereix_districte_al_frontmatter(fm_text, valor):
    """Insereix 'districte: valor' just abans de 'draft:' o al final."""
    linia = f'districte: "{valor}"\n'
    if re.search(r'^draft:', fm_text, re.MULTILINE):
        return re.sub(r'^(draft:)', linia + r'\1', fm_text, count=1, flags=re.MULTILINE)
    return fm_text.rstrip('\n') + '\n' + linia + '\n'

def processa_publicacio(pub_slug):
    fitxes = []
    for fname in sorted(os.listdir(BASE)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(BASE, fname)
        content = open(fpath, encoding='utf-8').read()
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        fm = parts[1]
        if pub_slug not in fm:
            continue
        fitxes.append((fname, fpath, content, parts, fm))

    print(f"\n=== Processant {pub_slug}: {len(fitxes)} fitxes ===")

    modified = []
    ja_te = []
    sense_coords = []
    sense_districte = []
    no_oficial = []

    for i, (fname, fpath, content, parts, fm) in enumerate(fitxes, 1):
        # Ja té districte?
        if re.search(r'^districte:', fm, re.MULTILINE):
            ja_te.append(fname)
            print(f"  [{i}/{len(fitxes)}] {fname}  => ja té districte, saltat")
            continue

        # Té lat i long?
        lat_m = re.search(r'^lat:\s*([^\n]+)', fm, re.MULTILINE)
        lon_m = re.search(r'^long:\s*([^\n]+)', fm, re.MULTILINE)
        if not lat_m or not lon_m:
            sense_coords.append(fname)
            print(f"  [{i}/{len(fitxes)}] {fname}  => SENSE coordenades")
            continue

        lat = lat_m.group(1).strip()
        lon = lon_m.group(1).strip()
        print(f"  [{i}/{len(fitxes)}] {fname}  lat={lat} lon={lon} ... ", end='', flush=True)

        raw = geocodifica(lat, lon)
        time.sleep(1.1)  # respectar rate limit Nominatim

        if not raw:
            sense_districte.append(fname)
            print("SENSE districte a Nominatim")
            continue

        districte, es_oficial = normalitza_districte(raw)
        if not es_oficial:
            no_oficial.append((fname, raw, districte))
            print(f"AVIS: '{raw}' no es un districte oficial -> usat tal qual")

        print(f"=> {districte}")

        new_fm = insereix_districte_al_frontmatter(fm, districte)
        new_content = '---' + new_fm + '---' + parts[2]
        open(fpath, 'w', encoding='utf-8').write(new_content)
        modified.append((fname, districte))

    print(f"\n--- Resum {pub_slug} ---")
    print(f"  Modificades: {len(modified)}")
    print(f"  Ja tenien districte: {len(ja_te)}")
    print(f"  Sense coordenades: {len(sense_coords)}")
    if sense_coords:
        for f in sense_coords: print(f"    - {f}")
    print(f"  Sense districte Nominatim: {len(sense_districte)}")
    if sense_districte:
        for f in sense_districte: print(f"    - {f}")
    print(f"  Districte no oficial (revisar): {len(no_oficial)}")
    if no_oficial:
        for f, raw, used in no_oficial: print(f"    - {f}: '{raw}' -> '{used}'")

    return {
        'modified': modified,
        'ja_te': ja_te,
        'sense_coords': sense_coords,
        'sense_districte': sense_districte,
        'no_oficial': no_oficial,
    }

if __name__ == '__main__':
    pubs = sys.argv[1:] if len(sys.argv) > 1 else ['masies']
    if not pubs:
        print("Ús: python3 add-districte.py masies [biblioteques] [mercats]")
        sys.exit(1)

    for pub in pubs:
        processa_publicacio(pub)
