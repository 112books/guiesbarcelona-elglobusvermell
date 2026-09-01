#!/usr/bin/env python3
"""Afegeix aliases (redireccions 301-equivalents) del WordPress antic a les fitxes Hugo.

Font: post-sitemap.xml del WordPress de producció (671 URLs).
Els slugs del WP coincideixen majoritàriament amb els fitxers Hugo; les
excepcions (renoms, fusionats, pàgines /text/ de les publicacions) es mapen
explícitament, verificades contra els títols del WP i el contingut Hugo.
Hugo genera una pàgina de redirecció (meta-refresh + canonical, sense
indexar) per cada alias.

Idempotent: fusiona amb una clau aliases existent i no duplica valors.
"""
import os
import re
import urllib.request
from collections import defaultdict

SITEMAP = "https://guiesbarcelona.elglobusvermell.org/post-sitemap.xml"
ELEMENTS = "content/ca/elements"
PUBLI = "content/ca/publicacions"

EXCEPCIONS = {
    "boqueria": "mercat-de-la-boqueria",
    "santa-caterina": "mercat-de-santa-caterina-i-habitatges-per-ancians",
    "born": "el-born-muhba-mercat-del-born",
    "can-folch": "xemeneia-de-can-folch",
    "letona": "fabrica-letona",
    "union-metalurgica": "la-union-metalurgica",
    "xemeneia-2": "xemeneia",
    "xemeneia-3": "xemeneia",
    "xemeneia-4": "xemeneia",
    "filatura-el-canem-2": "filatura-el-canem",
    "sant-miquel-del-port": "esglesia-de-sant-miquel-del-port",
    "casa-f-esponac": "casa-f-espona",
    "edifici-dhabitatges-carrer-balmes-2": "edifici-dhabitatges-carrer-balmes",
    "pavello-de-la-republica-de-1937": "pavello-de-la-republica-biblioteca-crai-ub",
    "edifici-dhabitatges-2": "edifici-dhabitatges-avinguda-pedralbes",
    "edifici-dhabitatges-carrer-pallar": "edifici-dhabitatges-carrer-pallars",
    "edifici-dhabitatges-monitor-2": "edifici-dhabitatges-monitor",
    "jardins-de-safo-2": "jardins-de-safo",
    "jardins-de-sebastia-gasch-2": "jardins-de-sebastia-gasch",
    "jardi-de-cristina-fernandez": "jardi-de-cristina-fernandez-pereira",
    "jardins-de-candida-perez": "biblioteca-sant-antoni-joan-oliver-casal-davis-i-jardins-de-candida-perez",
    "jardi-de-roger-de-flor": "jardins-dagusti-centelles",
    "interior-dilla-antics-cinema-niza": "jardins-de-les-treballadores-de-la-numax",
    "biblioteca-esquerra-de-leixample-agusti-centelles": "edifici-collage-centre-cultural-teresa-pamies",
    "biblioteca-vallcarca-i-els-penitents-m-antonieta-cot": "biblioteca-vallcarca-i-els-penitents-maria-antonieta-cot",
    "biblioteca-vila-de-gracia": "biblioteca-vila-de-gracia-rosa-maria-arquimbau",
    "biblioteca-canyelles": "biblioteca-canyelles-maria-angels-rivas",
    "biblioteca-les-roquetes": "biblioteca-les-roquetes-rafa-juncadella",
    "biblioteca-nou-barris": "biblioteca-nou-barris-aurora-diaz-plaja",
    "biblioteca-vilapicina-i-la-torre-llobeta": "biblioteca-vilapicina-i-la-torre-llobeta-carmen-laforet",
    "biblioteca-zona-nord": "biblioteca-zona-nord-maria-sanchez",
    "biblioteca-bon-pastor": "biblioteca-bon-pastor-josefina-castellvi",
    "biblioteca-trinitat-vella-j-barbero": "biblioteca-trinitat-vella-jose-barbero",
    "biblioteca-camp-de-larpa-caterina-albert": "illa-dequipaments-alchemika",
    "biblioteca-sant-marti-de-provencals": "biblioteca-gabriel-garcia-marquez",
    "masia-torre-de-sant-joan": "torre-de-sant-joan",
    "masia-masoveria-de-can-safont": "masia-i-masoveria-de-can-safont",
    "masia-torre-velez": "torre-velez",
    "masia-can-mestres-2": "masia-can-mestres",
    "masia-torre-rodona": "torre-rodona",
    "masia-torre-de-santa-caterina": "torre-de-santa-caterina",
    "edifici-dhabitatges-3": "edifici-dhabitatges",
    "edifici-dhabitatges-socials-2": "edifici-dhabitatges-socials",
    "edifici-doficines-2": "edifici-doficines",
    "mercat-de-la-barceloneta-2": "mercat-de-la-barceloneta",
    "biblioteca-fort-pienc": "illa-dequipaments-fort-pienc",
}

PUBLI_TEXT = {
    "mercats": "mercats",
    "poblenou": "poblenou",
    "barceloneta": "barceloneta",
    "gatcpac": "gatcpac",
    "interiors-illa": "interiors-illa",
    "arquitectura-moderna-a-barcelona-1950-1975": "50-75",
    "biblioteques": "biblioteques",
    "la-marina-del-port-i-del-prat-vermell-passat-i-present": "marina",
    "masies": "masies",
    "arquitectura-a-barcelona-1975-2008-de-lesperanca-a-la-crisi": "76-08",
    "arquitectura-a-barcelona-2010-2025-la-revolucio-tranquilla": "09-25",
}


def main():
    xml = urllib.request.urlopen(SITEMAP, timeout=60).read().decode("utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", xml)
    print(f"URLs al sitemap WP: {len(locs)}")

    per_fitxa = defaultdict(list)
    misses = []
    for url in locs:
        path = re.sub(r"^https?://guiesbarcelona\.elglobusvermell\.org", "", url.strip())
        m = re.match(r"^/([a-z0-9-]+)/([a-z0-9-]+)/?$", path)
        if not m:
            misses.append((path, "URL fora del patró categoria/slug"))
            continue
        cat, slug_wp = m.group(1), m.group(2)

        if cat == "text" and slug_wp in PUBLI_TEXT:
            fitxa = os.path.join(PUBLI, PUBLI_TEXT[slug_wp], "_index.md")
        elif cat == "text":
            misses.append((path, "pàgina /text/ sense mapa"))
            continue
        else:
            slug_hugo = EXCEPCIONS.get(slug_wp, slug_wp)
            fitxa = os.path.join(ELEMENTS, slug_hugo + ".md")

        if not os.path.isfile(fitxa):
            misses.append((path, f"cap fitxa Hugo ({fitxa})"))
            continue
        per_fitxa[fitxa].append(f"/{cat}/{slug_wp}/")

    print(f"Fitxes Hugo a tocar: {len(per_fitxa)}")
    print(f"URLs mapejades: {sum(len(v) for v in per_fitxa.values())}")
    print(f"URLs sense mapa: {len(misses)}")

    for fitxa, aliases in sorted(per_fitxa.items()):
        text = open(fitxa, encoding="utf-8").read()
        lines = text.split("\n")
        if not lines or lines[0].strip() != "---":
            misses.append((fitxa, "no comença amb front matter ---"))
            continue

        idx = None
        for i, ln in enumerate(lines[:40]):
            if ln.startswith("aliases:"):
                idx = i
                break
        existents = re.findall(r'"(/[^"]+)"', lines[idx]) if idx is not None else []
        fusions = existents + [a for a in aliases if a not in existents]
        nova_linia = "aliases: [" + ", ".join(f'"{a}"' for a in fusions) + "]"

        if idx is None:
            lines.insert(1, nova_linia)
        elif nova_linia != lines[idx]:
            lines[idx] = nova_linia
        else:
            continue
        open(fitxa, "w", encoding="utf-8").write("\n".join(lines))

    print("\n--- URLs sense mapa (a revisar) ---")
    for path, motiu in misses:
        print(f"  {path}  →  {motiu}")


if __name__ == "__main__":
    main()
