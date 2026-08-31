#!/usr/bin/env python3
"""Paquet mercats aprovat per Joan (31 ago 2026): zones definitives + camp ordre.

Font: llista d'Xavi del mail del 31 ago al vespre (ordre del PDF),
docs/2026-08-31-mail-xavi-3-mercats-zones.md — 11 fitxes passen a "Nous barris".
- ordre = posició al PDF dins de cada zona
- La Marina duplicada (2 fitxes): totes dues ordre 9, pendent fusionar
- Encants-Fira de Bellcaire ordre 4: reserva 2-3 pels Encants/Dominical de
  Sant Antoni quan es creïn
- Mercat de Sant Gervasi ordre 3: no és a la llista d'Xavi (dubte pendent),
  es manté al final de la seva sub-zona
"""

import pathlib
import re
import sys

BASE = pathlib.Path('content/ca/elements')

ZONA_ORDRE = {
    # Ciutat Vella
    'mercat-de-la-boqueria': ('Ciutat Vella', 1),
    'mercat-de-santa-caterina-i-habitatges-per-ancians': ('Ciutat Vella', 2),
    'el-born-muhba-mercat-del-born': ('Ciutat Vella', 3),
    'mercat-de-la-barceloneta': ('Ciutat Vella', 4),
    # Eixample
    'mercat-de-sant-antoni': ('Eixample', 1),
    'mercat-del-ninot': ('Eixample', 2),
    'mercat-de-la-concepcio': ('Eixample', 3),
    'mercat-de-la-sagrada-familia': ('Eixample', 4),
    'illa-dequipaments-fort-pienc': ('Eixample', 5),
    # Antics municipis — Sants
    'mercat-dhostafrancs': ('Sants', 1),
    'mercat-de-sants': ('Sants', 2),
    # Antics municipis — Sarrià
    'mercat-de-sarria': ('Sarrià', 1),
    # Antics municipis — Sant Gervasi
    'mercat-de-galvany': ('Sant Gervasi', 1),
    'mercat-de-les-tres-torres': ('Sant Gervasi', 2),
    'mercat-de-sant-gervasi': ('Sant Gervasi', 3),
    # Antics municipis — Gràcia
    'mercat-de-la-llibertat': ('Gràcia', 1),
    'mercat-delabaceria': ('Gràcia', 2),
    # Antics municipis — Sant Martí de Provençals
    'mercat-del-clot': ('Sant Martí de Provençals', 1),
    'mercat-del-poblenou': ('Sant Martí de Provençals', 2),
    # Antics municipis — Horta
    'mercat-dhorta': ('Horta', 1),
    # Antics municipis — Sant Andreu
    'mercat-de-sant-andreu': ('Sant Andreu', 1),
    # Nous barris (ordre del PDF; La Marina duplicada)
    'mercat-del-guinardo': ('Nous barris', 1),
    'mercat-de-felip-ii': ('Nous barris', 2),
    'mercat-del-bon-pastor': ('Nous barris', 3),
    'mercat-de-provencals': ('Nous barris', 4),
    'mercat-de-sant-marti': ('Nous barris', 5),
    'mercat-del-besos': ('Nous barris', 6),
    'mercat-de-lestrella': ('Nous barris', 7),
    'mercat-de-lesseps': ('Nous barris', 8),
    'mercat-de-la-marina': ('Nous barris', 9),
    'placa-i-mercat-de-la-marina': ('Nous barris', 9),
    'mercat-de-les-corts': ('Nous barris', 10),
    'mercat-de-la-vall-dhebron-teixonera': ('Nous barris', 11),
    'mercat-del-carmel': ('Nous barris', 12),
    'mercat-de-nuria': ('Nous barris', 13),
    'mercat-de-ciutat-meridiana': ('Nous barris', 14),
    'mercat-de-canyelles': ('Nous barris', 15),
    'mercat-de-la-guineueta': ('Nous barris', 16),
    'mercat-de-la-merce': ('Nous barris', 17),
    'mercat-de-la-montserrat': ('Nous barris', 18),
    'mercat-de-la-trinitat': ('Nous barris', 19),
    # Mercats no alimentaris (2 i 3 reservats pels de Sant Antoni)
    'mercat-dels-encants-fira-de-bellcaire': ('Mercats no alimentaris', 4),
}


def main():
    errors = []
    canvis_zona = 0
    for slug, (zona, ordre) in ZONA_ORDRE.items():
        path = BASE / (slug + '.md')
        if not path.exists():
            errors.append('NO TROBADA: ' + slug)
            continue
        text = path.read_text(encoding='utf-8')
        m = re.match(r'\A---\n(.*?)\n---(\n?)', text, re.S)
        if not m:
            errors.append('SENSE FRONTMATTER: ' + slug)
            continue
        fm = m.group(1)
        if '- mercats' not in fm:
            errors.append('SENSE PUBLICACIO mercats: ' + slug)
            continue
        out = []
        zona_previa = None
        inserit = False
        for line in fm.split('\n'):
            if re.match(r'^ordre:', line):
                continue
            if re.match(r'^zona:', line):
                zona_previa = line
                out.append('zona: "%s"' % zona)
                out.append('ordre: %d' % ordre)
                inserit = True
                continue
            out.append(line)
        if not inserit:
            errors.append('SENSE CAMP zona: ' + slug)
            continue
        path.write_text(
            '---\n' + '\n'.join(out) + '\n---' + m.group(2) + text[m.end():],
            encoding='utf-8')
        marcador = '' if zona_previa == 'zona: "%s"' % zona else '  << ZONA CANVIADA'
        if marcador:
            canvis_zona += 1
        print('%-55s zona %-28s -> %-20s ordre %2d%s' % (
            slug, zona_previa, zona, ordre, marcador))
    print('\n%d fitxes, %d canvis de zona' % (len(ZONA_ORDRE), canvis_zona))
    if errors:
        print('\nERRORS:')
        for e in errors:
            print('  ' + e)
        sys.exit(1)


if __name__ == '__main__':
    main()
