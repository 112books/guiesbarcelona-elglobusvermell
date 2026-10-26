#!/usr/bin/env python3
"""
Corregeix els valors orfes del camp `arquitectes` a les fitxes d'elements.

Un valor és orfe quan el text emmagatzemat no coincideix amb el title de cap
fitxa a content/ca/arquitectes/. Passa perquè en Xavi ha renombrat arquitectes
(afegint cognoms complets) però les fitxes dels edificis guarden els noms antics.

Estratègia de match automàtic (en ordre de prioritat):
  1. Coincidència exacta (no hauria d'arribar aquí, però per seguretat)
  2. L'orfe és un prefix del títol existent (ex. "Sixte Illescas" → "Sixte Illescas i Mirosa")
  3. El títol existent comença per l'orfe (equivalent a 2, per normalització)
  4. L'orfe és contingut dins del títol existent (cas "BAAS Arquitectura (Jordi Badia)"
     conté "BAAS Arquitectura")

Ús:
  python3 scripts/corregeix-arquitectes-orfes.py          # dry-run (mostra canvis)
  python3 scripts/corregeix-arquitectes-orfes.py --apply  # aplica els canvis
"""

import os, re, sys

DRY_RUN = "--apply" not in sys.argv

# Correccions manuals per a renombrats que no es poden inferir automàticament
# (canvi de nom complet o diferència d'accent puntual)
CORRECCIONS_MANUALS = {
    "Toyo Ito Associates":  "Toyō Itō",
    "Xavier Subias i Fages": "Xavier Subías i Fages",
    "Carles Martínez Sánchez": "Carles Martínez i Sánchez",
}

def llegir_titols_arquitectes(arq_dir):
    titols = {}  # title -> slug
    for d in os.listdir(arq_dir):
        if d == '_index.md':
            continue
        idx = os.path.join(arq_dir, d, '_index.md')
        if not os.path.isfile(idx):
            continue
        with open(idx, encoding='utf-8') as f:
            for line in f:
                m = re.match(r'^title:\s*(.+)\s*$', line)
                if m:
                    val = m.group(1).strip().strip('"').strip("'")
                    titols[val] = d
                    break
    return titols

def trobar_match(orfe, titols):
    """Retorna el títol canònic si en trobem un, altrament None."""
    o_lower = orfe.lower().strip()
    for titol in titols:
        t_lower = titol.lower().strip()
        if o_lower == t_lower:
            return titol
        if t_lower.startswith(o_lower + ' ') or t_lower.startswith(o_lower + ','):
            return titol
        if o_lower.startswith(t_lower + ' ') or o_lower.startswith(t_lower + ','):
            return titol
    # Últim recurs: l'orfe conté el títol (ex. "BAAS Arquitectura (Jordi Badia)")
    for titol in titols:
        t_lower = titol.lower().strip()
        if len(t_lower) > 5 and o_lower.startswith(t_lower):
            return titol
    return None

def processar_element(fitxa_path, titols, dry_run):
    with open(fitxa_path, encoding='utf-8') as f:
        contingut = f.read()

    m = re.search(r'^(arquitectes:\s*\n)((?:[ \t]*-[ \t]*.+\n)+)', contingut, re.MULTILINE)
    if not m:
        return None, []

    bloc_original = m.group(0)
    linies_arq = re.findall(r'([ \t]*-[ \t]*)(.+)', m.group(2))

    canvis = []
    noves_linies = []
    for prefix, nom in linies_arq:
        nom_net = nom.strip().strip('"').strip("'")
        if nom_net in titols:
            noves_linies.append(f"{prefix}{nom_net}")
        elif nom_net in CORRECCIONS_MANUALS:
            match = CORRECCIONS_MANUALS[nom_net]
            canvis.append((nom_net, match))
            noves_linies.append(f"{prefix}{match}")
        else:
            match = trobar_match(nom_net, titols)
            if match:
                canvis.append((nom_net, match))
                noves_linies.append(f"{prefix}{match}")
            else:
                noves_linies.append(f"{prefix}{nom_net}")  # deixem sense canvi

    if not canvis:
        return None, []

    nou_bloc = m.group(1) + '\n'.join(noves_linies) + '\n'
    nou_contingut = contingut[:m.start()] + nou_bloc + contingut[m.end():]

    if not dry_run:
        with open(fitxa_path, 'w', encoding='utf-8') as f:
            f.write(nou_contingut)

    return fitxa_path, canvis

def main():
    arq_dir = 'content/ca/arquitectes'
    elem_dir = 'content/ca/elements'

    titols = llegir_titols_arquitectes(arq_dir)

    tots_orfes = set()
    resultats = []  # (fitxa, [(vell, nou), ...])
    sense_match = set()

    for nom in sorted(os.listdir(elem_dir)):
        if os.path.isfile(os.path.join(elem_dir, nom)):
            fitxa = os.path.join(elem_dir, nom)
        else:
            fitxa = os.path.join(elem_dir, nom, 'index.md')
            if not os.path.isfile(fitxa):
                continue

        fitxa_path, canvis = processar_element(fitxa, titols, DRY_RUN)
        if canvis:
            resultats.append((fitxa_path, canvis))
            for vell, nou in canvis:
                tots_orfes.add(vell)

    # Detectar orfes totals sense match
    for nom in sorted(os.listdir(elem_dir)):
        if os.path.isfile(os.path.join(elem_dir, nom)):
            fitxa = os.path.join(elem_dir, nom)
        else:
            fitxa = os.path.join(elem_dir, nom, 'index.md')
            if not os.path.isfile(fitxa):
                continue
        with open(fitxa, encoding='utf-8') as f:
            contingut = f.read()
        m = re.search(r'^arquitectes:\s*\n((?:[ \t]*-[ \t]*.+\n)+)', contingut, re.MULTILINE)
        if m:
            for arq in re.findall(r'-\s*(.+)', m.group(1)):
                arq = arq.strip().strip('"').strip("'")
                if arq and arq not in titols and arq not in CORRECCIONS_MANUALS and trobar_match(arq, titols) is None:
                    sense_match.add(arq)

    mode = "DRY-RUN (no s'han escrit canvis)" if DRY_RUN else "APLICAT"
    print(f"\n=== {mode} ===\n")
    print(f"Fitxes corregides: {len(resultats)}")
    print(f"Noms corregits automàticament: {len(tots_orfes)}")
    print(f"Noms sense match (pendents revisió manual): {len(sense_match)}\n")

    if resultats:
        print("--- CANVIS AUTOMÀTICS ---")
        for fitxa, canvis in resultats:
            slug = os.path.basename(os.path.dirname(fitxa)) if fitxa.endswith('index.md') else os.path.basename(fitxa).replace('.md','')
            for vell, nou in canvis:
                print(f"  {slug}: '{vell}' → '{nou}'")

    if sense_match:
        print("\n--- PENDENTS DE REVISIÓ MANUAL (no s'han tocat) ---")
        for s in sorted(sense_match):
            print(f"  - {s}")

if __name__ == '__main__':
    main()
