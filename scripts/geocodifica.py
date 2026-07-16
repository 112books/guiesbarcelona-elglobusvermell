#!/usr/bin/env python3
"""
Geocodificació automàtica d'edificis sense coordenades via Nominatim (OSM).
Afegeix lat/long als fitxers .md que no en tenen.

Ús:
  python3 scripts/geocodifica.py [--dry-run] [--force]

Opcions:
  --dry-run   Mostra el resultat sense modificar fitxers
  --force     Tornar a geocodificar fins i tot els que ja tenen coordenades

Límit: Nominatim permet 1 petició/segon (respectat automàticament).
"""

import sys
import time
import re
import urllib.request
import urllib.parse
import json
from pathlib import Path

import yaml  # pip install pyyaml

DRY_RUN = '--dry-run' in sys.argv
FORCE   = '--force'   in sys.argv

NOMINATIM_URL  = 'https://nominatim.openstreetmap.org/search'
USER_AGENT     = 'guiesbarcelona-geocoder/1.0 (linuxbcn@gmail.com)'
DELAY_SECONDS  = 1.1  # Nominatim: max 1 req/s

ELEMENTS_DIR = Path(__file__).parent.parent / 'content' / 'ca' / 'elements'


def llegeix_frontmatter(text: str) -> tuple[dict, str]:
    """Separa frontmatter YAML i cos del fitxer."""
    if not text.startswith('---'):
        return {}, text
    end = text.find('\n---', 3)
    if end == -1:
        return {}, text
    fm_str = text[3:end].strip()
    body   = text[end + 4:].lstrip('\n')
    data   = yaml.safe_load(fm_str) or {}
    return data, body


def escriu_frontmatter(data: dict, body: str) -> str:
    """Reconstrueix el fitxer amb frontmatter YAML."""
    fm = yaml.dump(data, allow_unicode=True, default_flow_style=False,
                   sort_keys=False).strip()
    result = f'---\n{fm}\n---\n'
    if body:
        result += body
    return result


def geocodifica(adreca: str, ciutat: str = 'Barcelona') -> tuple[float, float] | None:
    """Consulta Nominatim per a una adreça a Barcelona. Retorna (lat, long) o None."""
    query = f'{adreca}, {ciutat}'
    params = urllib.parse.urlencode({
        'q':              query,
        'format':         'json',
        'limit':          1,
        'countrycodes':   'es',
        'addressdetails': 0,
    })
    url = f'{NOMINATIM_URL}?{params}'
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            results = json.loads(resp.read())
            if results:
                return float(results[0]['lat']), float(results[0]['lon'])
    except Exception as e:
        print(f'    Error Nominatim: {e}')
    return None


def main():
    fitxers = sorted(ELEMENTS_DIR.glob('*.md'))
    geocodificats  = 0
    sense_adreca   = 0
    ja_te_coords   = 0
    errors         = 0

    mode = 'DRY RUN — ' if DRY_RUN else ''
    print(f'\n{mode}Geocodificació via Nominatim/OSM')
    print(f'Directori: {ELEMENTS_DIR}\n')

    for fitxer in fitxers:
        text = fitxer.read_text(encoding='utf-8')
        data, body = llegeix_frontmatter(text)

        if not data:
            continue

        te_coords = data.get('lat') and data.get('long')

        if te_coords and not FORCE:
            ja_te_coords += 1
            continue

        adreca = data.get('adreca', '').strip()
        if not adreca:
            print(f'  — {fitxer.name}: sense adreça, saltat')
            sense_adreca += 1
            continue

        print(f'  ? {fitxer.name}: "{adreca}"', end=' ', flush=True)

        time.sleep(DELAY_SECONDS)
        coords = geocodifica(adreca)

        if not coords:
            print('→ no trobat')
            errors += 1
            continue

        lat, long = coords
        print(f'→ {lat:.6f}, {long:.6f}')

        if not DRY_RUN:
            data['lat']  = round(lat,  7)
            data['long'] = round(long, 7)
            fitxer.write_text(escriu_frontmatter(data, body), encoding='utf-8')
            geocodificats += 1
        else:
            geocodificats += 1

    print(f'\nResultat:')
    print(f'  ✓ Geocodificats: {geocodificats}')
    print(f'  · Ja tenien coords: {ja_te_coords}')
    print(f'  · Sense adreça: {sense_adreca}')
    print(f'  ✗ No trobats: {errors}')

    if DRY_RUN:
        print('\nExecuta sense --dry-run per aplicar els canvis.')


if __name__ == '__main__':
    main()
