#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificació diària dels números de la portada — Guies de Barcelona.

Les xifres que veu tothom a la portada:
  - «edificis documentats»   → fitxes d'element amb coordenades (camp `lat`)
  - «guies de camp»          → entrades de data/publicacions.yaml
  - «arquitectes i estudis»  → termes de la taxonomia (noms de les fitxes)
  - «anys d'arquitectura»    → 1928 (valor editorial) – any en curs

La portada les calcula sola al build (index.html), així que mai queden
antigues; el risc és que canviin sense que ningú se n'adoni (una fitxa
editada que perd la coordenada, un YAML que es trenca, una entrada
esborrada...). Aquest script les compara cada dia:

  1. PUBLICAT  — el que surt a la portada en línia
  2. REPO      — el que ha de sortir, calculat sobre el contingut actual
  3. AHIR      — l'històric (.ai/numeros-web-history.json)

Escriu .ai/VERIFICACIO-NUMEROS.md i l'històric. No toca res del web.
Sortida: codi 0 sempre; si hi ha alerta, la marxa a GITHUB_OUTPUT
("alert", "resum") i el workflow la fa visible.
"""

import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE_URL = os.environ.get(
    "LIVE_URL",
    "https://112books.github.io/guiesbarcelona-elglobusvermell/")
REPORT = os.path.join(ROOT, ".ai", "VERIFICACIO-NUMEROS.md")
HISTORIC = os.path.join(ROOT, ".ai", "numeros-web-history.json")
ANY_MIN = 1928            # valor editorial del projecte (index.html)
DIES_HISTORIC = 120       # entrades que es guarden a l'històric
DIES_INFORME = 14         # dies que es mostren a l'informe

try:
    import yaml
except ImportError:
    yaml = None


def llegeix(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def frontmatter(path):
    """Front matter YAML d'una fitxa → dict (amb fallback mínim sense PyYAML)."""
    txt = llegeix(path)
    m = re.match(r"^---\s*\n(.*?)\n---", txt, re.S)
    if not m:
        return {}
    fm = m.group(1)
    if yaml is not None:
        try:
            d = yaml.safe_load(fm) or {}
            return d if isinstance(d, dict) else {}
        except Exception:
            pass
    d = {}
    d["draft"] = bool(re.search(r"^draft:\s*true\s*$", fm, re.M))
    mlat = re.search(r"^lat:\s*(\S+)\s*$", fm, re.M)
    d["lat"] = mlat.group(1) if mlat else None
    bloc = re.search(r"^arquitectes:\s*\n((?:\s*-\s.*\n?)+)", fm, re.M)
    d["arquitectes"] = ([l.strip().lstrip("- ").strip()
                         for l in bloc.group(1).splitlines()] if bloc else [])
    return d


def comptes_repo():
    """El que HAN de dir les xifres, segons el contingut del repo."""
    elements = [f for f in glob.glob(os.path.join(
        ROOT, "content", "ca", "elements", "*.md"))
        if not os.path.basename(f).startswith("_")]

    total = amb_lat = amb_pub = esborranys = 0
    noms_arquitectes = set()
    sense_lat = []
    for f in elements:
        fm = frontmatter(f)
        if fm.get("draft") is True:
            esborranys += 1
            continue
        total += 1
        lat = fm.get("lat")
        if lat not in (None, "", False):
            amb_lat += 1
        else:
            sense_lat.append(os.path.basename(f))
        if fm.get("publicacions"):
            amb_pub += 1
        for nom in (fm.get("arquitectes") or []):
            if isinstance(nom, str) and nom.strip():
                noms_arquitectes.add(nom.strip())

    # Guies: entrades de data/publicacions.yaml
    ruta_pub = os.path.join(ROOT, "data", "publicacions.yaml")
    guies = None
    if os.path.exists(ruta_pub):
        txt = llegeix(ruta_pub)
        if yaml is not None:
            try:
                dades = yaml.safe_load(txt)
                guies = len(dades) if isinstance(dades, list) else None
            except Exception:
                guies = None
        if guies is None:  # fallback
            guies = len(re.findall(r"^- slug:", txt, re.M))

    # Pàgines de publicació creades al web (referència)
    pagines_pub = len(glob.glob(os.path.join(
        ROOT, "content", "ca", "publicacions", "*", "_index.md")))

    return {
        "edificis": amb_lat,           # el que mostra la portada
        "guies": guies,
        "arquitectes": len(noms_arquitectes),
        "anys": f"{ANY_MIN}–{dt.datetime.now().year}",
        # referències addicionals (no són xifra de portada)
        "fitxes_totals": total,
        "sense_coordenades": sense_lat,
        "amb_publicacions": amb_pub,
        "esborranys": esborranys,
        "noms_arquitectes_distints": len(noms_arquitectes),
        "pagines_publicacio": pagines_pub,
    }


def numeros_publicats(url):
    """Les 4 xifres tal com surten a la portada en línia."""
    req = urllib.request.Request(
        url, headers={"User-Agent": "verificacio-numeros-guiesbcn/1.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode(
        "utf-8", "replace")
    nums = re.findall(r"pa-stat-num[^>]*>\s*([^<]+?)\s*<", html)
    if len(nums) < 4:
        return None, f"no s'han trobat les 4 xifres (trobades: {len(nums)})"
    if not all(re.fullmatch(r"\d+", n) for n in nums[:3]):
        return None, f"valors inesperats: {nums[:4]}"
    if not re.fullmatch(r"\d{4}[–-]\d{4}", nums[3]):
        return None, f"rang d'anys inesperat: {nums[3]}"
    return {"edificis": int(nums[0]), "guies": int(nums[1]),
            "arquitectes": int(nums[2]),
            "anys": nums[3].replace("-", "–")}, None


def carrega_historic():
    if os.path.exists(HISTORIC):
        try:
            with open(HISTORIC, encoding="utf-8") as f:
                dades = json.load(f)
            if isinstance(dades, list):
                return dades
        except Exception:
            pass
    return []


def compara(pub, repo, ahir):
    """Llista d'alertes (blocs) i notes (informatives)."""
    alertes, notes = [], []
    if pub is None:
        alertes.append("No s'ha pogut llegir la portada en línia.")
        return alertes, notes
    if pub["edificis"] != repo["edificis"]:
        alertes.append(
            f"Edificis: publicat {pub['edificis']} però el repo en té "
            f"{repo['edificis']} amb coordenades (deploy pendent o pèrdua "
            f"de coordenades en alguna fitxa).")
    if pub["guies"] != repo["guies"]:
        alertes.append(
            f"Guies: publicat {pub['guies']} però data/publicacions.yaml en "
            f"té {repo['guies']}.")
    if pub["anys"] != repo["anys"]:
        alertes.append(
            f"Anys: publicat {pub['anys']} però hauria de ser {repo['anys']}.")
    if pub["arquitectes"] != repo["arquitectes"]:
        alertes.append(
            f"Arquitectes: publicat {pub['arquitectes']} però els noms de les "
            f"fitxes en donen {repo['arquitectes']} — revisar la taxonomia.")
    if ahir:
        for clau, nom in (("edificis", "Edificis"), ("guies", "Guies"),
                          ("arquitectes", "Arquitectes"), ("anys", "Anys")):
            pub_ahir = ahir.get("publicat", {}).get(clau)
            repo_ahir = ahir.get("repo", {}).get(clau)
            if pub_ahir is not None and pub_ahir != pub[clau]:
                notes.append(f"{nom}: la xifra publicada ha canviat "
                             f"({pub_ahir} → {pub[clau]}) — confirmar que el "
                             f"canvi és intencionat.")
            if repo_ahir is not None and repo_ahir != repo[clau]:
                notes.append(f"{nom}: el contingut del repo ha canviat "
                             f"({repo_ahir} → {repo[clau]}) des d'ahir.")
    return alertes, notes


def escriu_informe(ara, pub, repo, alertes, notes, historic):
    ok = not alertes
    linies = []
    linies.append("# Verificació diària dels números del web\n")
    linies.append(f"**Execució:** {ara:%d/%m/%Y %H:%M} UTC · "
                  f"**Font pública:** {LIVE_URL}\n")
    if ok:
        linies.append("## Resultat: ✅ tot coincideix\n")
    else:
        linies.append("## Resultat: ⚠️ ALERTA\n")
        for a in alertes:
            linies.append(f"- **{a}**")
        linies.append("")
    linies.append("| Xifra de portada | Publicat | Segons el repo | Estat |")
    linies.append("|---|---|---|---|")
    for clau, nom in (("edificis", "Edificis documentats"),
                      ("guies", "Guies de camp"),
                      ("arquitectes", "Arquitectes i estudis"),
                      ("anys", "Anys d'arquitectura")):
        p = "—" if pub is None else pub[clau]
        estat = "✓" if (pub and pub[clau] == repo[clau]) else "⚠️"
        linies.append(f"| {nom} | {p} | {repo[clau]} | {estat} |")
    linies.append("")
    linies.append("## Què vol dir cada xifra\n")
    linies.append("- **Edificis documentats**: fitxes d'element *amb "
                  "coordenades* (així les conta la portada). Les fitxes sense "
                  "coordenades no compten, encara que existeixin.")
    linies.append("- **Guies de camp**: guies del projecte (entrades de "
                  "`data/publicacions.yaml`). No totes tenen pàgina pròpia "
                  "al web: New Babylon i La Barcelona de Tàpies són només "
                  "«en paper».")
    linies.append("- **Arquitectes i estudis**: termes de la taxonomia Hugo "
                  "— els noms que surten al camp `arquitectes` de les fitxes "
                  "(i les fitxes curades de `/arquitectes/`).")
    linies.append(f"- **Anys d'arquitectura**: {ANY_MIN} és un valor "
                  "editorial fix (hi ha masies anteriors — debat intern de "
                  "l'equip); el segon any és l'any en curs.\n")
    linies.append("## Referències del contingut\n")
    linies.append(f"- Fitxes d'element: **{repo['fitxes_totals']}** "
                  f"(amb publicacions: {repo['amb_publicacions']}; "
                  f"esborranys: {repo['esborranys']})")
    sl = repo["sense_coordenades"]
    detall = ", ".join(sl) if sl else "cap"
    linies.append(f"- Amb coordenades: **{repo['edificis']}** — sense: "
                  f"{len(sl)} ({detall})")
    linies.append(f"- Noms d'arquitecte a les fitxes: "
                  f"**{repo['noms_arquitectes_distints']}** · pàgines de "
                  f"publicació creades: {repo['pagines_publicacio']}\n")
    if notes:
        linies.append("## Canvis respecte l'última verificació\n")
        for n in notes:
            linies.append(f"- {n}")
        linies.append("")
    if historic:
        linies.append(f"## Històric (últims {DIES_INFORME} dies)\n")
        linies.append("| Data | Edificis | Guies | Arquitectes | Anys |")
        linies.append("|---|---|---|---|---|")
        for e in historic[-DIES_INFORME:]:
            p = e.get("publicat") or {}
            linies.append(f"| {e['data']} | {p.get('edificis', '—')} | "
                          f"{p.get('guies', '—')} | "
                          f"{p.get('arquitectes', '—')} | "
                          f"{p.get('anys', '—')} |")
        linies.append("")
    linies.append("---\n")
    linies.append("*Generat per `scripts/verifica-numeros-web.py` "
                  "(execució diària automàtica). Cap xifra de la portada no "
                  "és hardcoded: totes es calculen al build; això verifica "
                  "que el que es publica coincideix amb el contingut.*")
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(linies) + "\n")


def main():
    ara = dt.datetime.now(dt.timezone.utc)
    historic = carrega_historic()
    ahir = historic[-1] if historic else None

    repo = comptes_repo()
    pub, error = None, None
    try:
        pub, error = numeros_publicats(LIVE_URL)
    except Exception as e:
        error = str(e)

    alertes, notes = compara(pub, repo, ahir)
    if error:
        alertes.append(f"Error llegint el web: {error}")

    entrada = {"data": f"{ara:%Y-%m-%d}", "publicat": pub, "repo": {
        k: repo[k] for k in ("edificis", "guies", "arquitectes", "anys")}}
    if ahir and ahir["data"] == entrada["data"] and historic:
        historic[-1] = entrada
    else:
        historic.append(entrada)
    historic = historic[-DIES_HISTORIC:]
    with open(HISTORIC, "w", encoding="utf-8") as f:
        json.dump(historic, f, ensure_ascii=False, indent=1)

    escriu_informe(ara, pub, repo, alertes, notes, historic)

    print(f"Publicat : {pub if pub else '— (error)'}")
    print(f"Repo     : edificis={repo['edificis']} guies={repo['guies']} "
          f"arquitectes={repo['arquitectes']} anys={repo['anys']}")
    print(f"Fitxes   : {repo['fitxes_totals']} totals, "
          f"{len(repo['sense_coordenades'])} sense coordenades, "
          f"{repo['esborranys']} esborranys")
    if notes:
        print("Notes    :")
        for n in notes:
            print(f"  - {n}")
    if alertes:
        print("ALERTA   :")
        for a in alertes:
            print(f"  ! {a}")
    else:
        print("Resultat : tot coincideix")

    gout = os.environ.get("GITHUB_OUTPUT")
    if gout:
        with open(gout, "a", encoding="utf-8") as f:
            f.write(f"alert={'true' if alertes else 'false'}\n")
            resum = " | ".join(alertes) if alertes else "Números correctes"
            f.write(f"resum={resum}\n")


if __name__ == "__main__":
    main()
