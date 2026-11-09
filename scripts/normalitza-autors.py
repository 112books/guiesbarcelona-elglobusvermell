#!/usr/bin/env python3
"""Normalitza els autors de les intervencions: de text lliure a llistes.

A l'editor, el camp d'autors d'una intervenció és un camp de relació múltiple
i espera una llista. 309 fitxes antigues el tenen com un text («A + B + C») i
per això no es podien editar. Aquest script les converteix, sense perdre cap
paraula i mantenint l'ordre:

  autors: A + B + C     ->     autors:
                                 - 'A'
                                 - 'B'
                                 - 'C'

Se separa per « + », « – », coma i barra (els mateixos separadors que fa
servir la plantilla). MAI per « i », que forma part dels cognoms catalans.

Ús:
  python3 scripts/normalitza-autors.py --dry        # informe, no toca res
  python3 scripts/normalitza-autors.py              # aplica
"""
import argparse
import glob
import json
import os
import re
import sys

import yaml

ARREL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ELEMENTS = os.path.join(ARREL, 'content', 'ca', 'elements')

# Els «+» sense espais formen part del nom («Peris+Toral», «Roldán+Berengué»),
# així que només se separen amb espais al voltant, com fa la plantilla.
SEPARADORS = re.compile(r'\s\+\s|\s+–\s+|,\s*|\s+/\s+')


def separa(valor):
    noms = []
    for tros in SEPARADORS.split(valor):
        tros = ' '.join(tros.split())
        if tros and tros not in noms:
            noms.append(tros)
    return noms


def cita(s):
    return "'" + s.replace("'", "''") + "'"


def processa_fitxer(cami, aplica):
    """Retorna (canviat, detalls) sense escriure res si aplica és False."""
    text = open(cami, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        return False, []
    fm = m.group(1)
    linies = fm.split('\n')
    sortida = []
    canvis = []
    i = 0
    while i < len(linies):
        linia = linies[i]
        mm = re.match(r'^(\s*)autors:\s*(.*)$', linia)
        if not mm:
            sortida.append(linia)
            i += 1
            continue
        indent = mm.group(1)
        valor = mm.group(2).strip()
        if valor in ('', "''", '""'):
            # Pot ser un camp buit o una llista que comença a la línia següent.
            seguent = linies[i + 1] if i + 1 < len(linies) else ''
            if seguent.strip().startswith('- '):
                sortida.append(linia)
                i += 1
                continue
            # Buit de debò: també ha de ser una llista (buida) perquè l'editor
            # no el tracti com un text.
            canvis.append({'abans': '', 'despres': []})
            sortida.append(indent + 'autors: []')
            i += 1
            continue
        if valor.startswith('[') or valor.startswith(('>', '|')):
            sortida.append(linia)
            i += 1
            continue
        # Escalar partit en diverses línies: s'ajunten amb un espai.
        j = i + 1
        while j < len(linies):
            seg = linies[j]
            if not seg.strip():
                break
            if len(seg) - len(seg.lstrip()) <= len(indent):
                break
            valor += ' ' + seg.strip()
            j += 1
        valor = valor.strip().strip("'\"")
        noms = separa(valor)
        if len(noms) <= 1:
            # Ja és un sol nom: també passa a llista, perquè l'editor el pugui
            # tractar com a relació múltiple.
            if len(noms) == 1:
                canvis.append({'abans': valor, 'despres': noms})
                sortida.append(indent + 'autors:')
                for n in noms:
                    sortida.append(indent + '  - ' + cita(n))
            else:
                sortida.append(linia)
            i = j
            continue
        canvis.append({'abans': valor, 'despres': noms})
        sortida.append(indent + 'autors:')
        for n in noms:
            sortida.append(indent + '  - ' + cita(n))
        i = j
    if not canvis:
        return None, []
    nou = text.replace(fm, '\n'.join(sortida), 1)
    if aplica:
        open(cami, 'w', encoding='utf-8').write(nou)
    return nou, canvis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry', action='store_true', help='només informe')
    ap.add_argument('--json', default='', help='desar l informe en JSON')
    args = ap.parse_args()

    fitxers = 0
    valors = 0
    informe = {}
    errors = 0
    generat = {}
    for cami in sorted(glob.glob(os.path.join(ELEMENTS, '*.md'))):
        clau = os.path.basename(cami)[:-3]
        nou, canvis = processa_fitxer(cami, not args.dry)
        if nou is None:
            continue
        fitxers += 1
        valors += len(canvis)
        informe[clau] = canvis
        generat[clau] = nou

    # Comprovació: el text resultant (o el del disc, si s'ha aplicat) ha de
    # parsejar i els autors han de ser llistes amb el mateix contingut.
    for clau, text in generat.items():
        try:
            m = re.match(r'^---\n(.*?)\n---', text, re.S)
            d = yaml.safe_load(m.group(1))
            for it in (d.get('intervencions') or []):
                if not isinstance(it, dict) or 'autors' not in it:
                    continue
                if not isinstance(it['autors'], list):
                    errors += 1
                    print('  NO ÉS LLISTA:', clau, repr(it['autors'])[:60])
        except Exception as e:
            errors += 1
            print('  ERROR YAML:', clau, e)

    accio = 'CANVIARIA' if args.dry else 'CANVIAT'
    print('%s: %d fitxes, %d valors d autors · errors: %d' % (accio, fitxers, valors, errors))
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(informe, f, ensure_ascii=False, indent=1)
        print('Informe: ' + args.json)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
