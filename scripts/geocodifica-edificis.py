#!/usr/bin/env python3
"""
Geocodifica (afegeix lat/long) als edificis d'una publicació que encara no en
tenen, via Nominatim (OSM), acotat a la ciutat de Barcelona per evitar falsos
positius amb carrers homònims d'altres poblacions.

Ús:
    python3 scripts/geocodifica-edificis.py --slug marina --dir content/ca/elements
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

NOMINATIM = "https://nominatim.openstreetmap.org/search"
VIEWBOX = "2.05,41.47,2.25,41.30"  # Barcelona ciutat, aprox.
USER_AGENT = "elglobusvermell-migration/1.0 (linuxbcn@gmail.com)"


def geocode(adreca: str):
    params = {
        "q": f"{adreca}, Barcelona",
        "format": "json",
        "limit": 1,
        "viewbox": VIEWBOX,
        "bounded": 1,
    }
    url = NOMINATIM + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if not data:
        return None
    return data[0]["lat"], data[0]["lon"]


def first_addr_variant(adreca: str) -> str:
    """Si l'adreça és composta ('A + B' o 'A / B'), prova amb la primera part."""
    return re.split(r"\s*[+/]\s*", adreca)[0].strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="slug de publicació (ex: marina)")
    ap.add_argument("--dir", default="content/ca/elements")
    args = ap.parse_args()

    out_dir = Path(args.dir)
    candidats = []
    for f in sorted(out_dir.glob("*.md")):
        if f.name == "_index.md":
            continue
        text = f.read_text(encoding="utf-8")
        if not text.startswith("+++"):
            continue  # format YAML (fitxes curades a mà), no tocar
        if "\nlat" in text:
            continue  # ja geocodificat
        m_pub = re.search(r'publicacions = \[(.*?)\]', text)
        if not m_pub or f'"{args.slug}"' not in m_pub.group(1):
            continue
        m_adr = re.search(r'^adreca = "(.+?)"', text, re.MULTILINE)
        if not m_adr:
            continue
        candidats.append((f, text, m_adr.group(1)))

    print(f"{len(candidats)} edificis de '{args.slug}' sense coordenades")

    ok = fail = 0
    for f, text, adreca in candidats:
        query_adr = first_addr_variant(adreca)
        try:
            result = geocode(query_adr)
        except Exception as e:
            print(f"  ERR {f.name}: {e}")
            result = None

        if result:
            lat, lon = result
            new_text = re.sub(
                r'(^adreca = ".+?"\n)',
                rf'\1lat = "{lat}"\nlong = "{lon}"\n',
                text, count=1, flags=re.MULTILINE,
            )
            f.write_text(new_text, encoding="utf-8")
            print(f"  OK  {f.name}: {lat}, {lon}")
            ok += 1
        else:
            print(f"  NO  {f.name}: sense resultat per '{query_adr}'")
            fail += 1

        time.sleep(1)  # política d'ús de Nominatim: max 1 req/seg

    print(f"\n{ok} geocodificats, {fail} pendents de revisió manual")


if __name__ == "__main__":
    main()
