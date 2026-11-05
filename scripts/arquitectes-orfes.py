#!/usr/bin/env python3
"""Classifica els noms d'arquitecte que surten als elements però no tenen fitxa.

Només llegeix: no modifica cap fitxa. Genera .ai/pla-arquitectes-orfes-<data>.json
amb dos grups:

  resolts  -> el nom es pot substituir sense decisions (variant, typo, "A + B").
  pendents -> cal decidir (fitxa nova, un altre nom, o no és arquitecte).

Ús:  python3 scripts/arquitectes-orfes.py [--data YYYY-MM-DD]
"""
import argparse
import datetime
import difflib
import glob
import json
import os
import re
import unicodedata

import yaml

ARREL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CONTINGUT = os.path.join(ARREL, 'content', 'ca')


def fmt(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().strip())


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', fmt(s))


def frontmatter(path):
    m = re.match(r'^---\n(.*?)\n---', open(path, encoding='utf-8').read(), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def carrega_titols():
    titols = {}
    for p in glob.glob(os.path.join(CONTINGUT, 'arquitectes', '*', '_index.md')):
        t = (frontmatter(p).get('title') or '').strip()
        if t:
            titols[t] = os.path.basename(os.path.dirname(p))
    return titols


def neteja(s):
    s = re.sub(r'\.\s*(1[89]\d\d|20\d\d)\s*$', '', s.strip())
    s = re.sub(r'\s*\((?:1[89]\d\d|20\d\d)\)\s*', '', s)
    return s.strip(' .,')


def resol_una(s, tnorm):
    s = neteja(s)
    n = norm(s)
    if not n:
        return None, None
    if n in tnorm:
        return tnorm[n], 'exacte'
    aprop = difflib.get_close_matches(n, list(tnorm), n=1, cutoff=0.88)
    if aprop:
        return tnorm[aprop[0]], 'variant'
    cand = [t for n2, t in tnorm.items() if (n in n2 or n2 in n) and abs(len(n2) - len(n)) <= 14]
    if len(set(cand)) == 1:
        return cand[0], 'parcial'
    return None, None


def resol(valor, tnorm):
    parts = [x for x in re.split(r'\s*\+\s*', valor) if x.strip()]
    fora = []
    for p in parts:
        m, k = resol_una(p, tnorm)
        if m:
            fora.append([m, k])
            continue
        for mm in re.finditer(r' i ', p):
            a, b = p[:mm.start()], p[mm.start() + 3:]
            ma, _ = resol_una(a, tnorm)
            mb, _ = resol_una(b, tnorm)
            if ma and mb:
                fora += [[ma, 'separat'], [mb, 'separat']]
                break
        else:
            fora.append([p, None])
    return fora


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', default=datetime.date.today().isoformat())
    args = ap.parse_args()

    titols = carrega_titols()
    tnorm = {norm(t): t for t in titols}

    orfes = {}
    for p in sorted(glob.glob(os.path.join(CONTINGUT, 'elements', '*.md'))):
        nom_fitxa = os.path.basename(p)[:-3]
        d = frontmatter(p)
        vals = []
        a = d.get('arquitectes') or []
        if isinstance(a, str):
            a = [a]
        vals += [('arquitectes', v) for v in a if isinstance(v, str) and v.strip()]
        for it in (d.get('intervencions') or []):
            if isinstance(it, dict):
                au = it.get('autors') or []
                if isinstance(au, str):
                    au = [au]
                vals += [('intervencions', v) for v in au if isinstance(v, str) and v.strip()]
        for camp, v in vals:
            if v.strip() not in titols:
                orfes.setdefault(v.strip(), set()).add(nom_fitxa)

    resolts, pendents = [], []
    for nom, fitxes in sorted(orfes.items()):
        parts = resol(nom, tnorm)
        item = {'nom': nom, 'fragments': parts, 'fitxes': sorted(fitxes)}
        (pendents if any(k is None for _, k in parts) else resolts).append(item)

    sortida = {
        'meta': {
            'data': args.data,
            'origen': 'content/ca/elements + content/ca/arquitectes',
            'fitxes_arquitecte': len(titols),
            'noms_orfs': len(orfes),
            'fitxes_afectades': len(set().union(*[s for s in orfes.values()])) if orfes else 0,
            'resolts': len(resolts),
            'pendents': len(pendents),
        },
        'resolts': resolts,
        'pendents': pendents,
    }
    desti = os.path.join(ARREL, '.ai', 'pla-arquitectes-orfes-%s.json' % args.data)
    with open(desti, 'w', encoding='utf-8') as f:
        json.dump(sortida, f, ensure_ascii=False, indent=1)
    m = sortida['meta']
    print('%d noms orfs a %d fitxes | resolts: %d | pendents: %d' % (
        m['noms_orfs'], m['fitxes_afectades'], m['resolts'], m['pendents']))
    print('Escrit: ' + os.path.relpath(desti, ARREL))


if __name__ == '__main__':
    main()
