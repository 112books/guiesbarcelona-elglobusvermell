#!/usr/bin/env python3
"""Estampa al tauler de revisió la data i hora de la seva darrera actualització.

El tauler (/admin/revisio/) ensenya a la capçalera «Darrera actualització: …».
Escriure-ho a mà s'oblida, i llavors no se sap quins canvis reflecteix el tauler.
Aquí es treu del commit que va tocar `static/admin/revisio/tasques.json` i es
desa a `actualitzat` en hora de Madrid, amb el format `AAAA-MM-DDTHH:MM` que la
pàgina converteix a «17/11/2026 a les 18:20».

S'executa al desplegament, abans de Hugo. Si no pot esbrinar la data (fora d'un
repositori git, git que falla, etc.) deixa el valor que ja hi ha i surt amb codi
0: un desplegament no s'ha d'aturar per això.

    python3 scripts/estampa_tauler.py             # escriu al fitxer
    python3 scripts/estampa_tauler.py --dry-run   # només diu què hi posaria
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ARREL = Path(__file__).resolve().parents[1]
TAULER = "static/admin/revisio/tasques.json"
ZONA = ZoneInfo("Europe/Madrid")

# Només la línia del camp dalt de tot (indentada amb dos espais), no pas les
# aparicions del mot dins dels textos de les fitxes.
PATRO = re.compile(r'^(  "actualitzat": ")[^"]*(")', re.MULTILINE)


def cami_relatiu(fitxer, repo):
    """El camí del tauler relatiu a l'arrel del repositori, o None si no ho és."""
    try:
        return Path(fitxer).resolve().relative_to(Path(repo).resolve()).as_posix()
    except (ValueError, OSError):
        return None


def data_iso_local(text):
    """'2026-11-17T15:54:00+01:00', '…Z' o '2026-11-17T15:54' → '2026-11-17T15:54' a Madrid."""
    try:
        data = datetime.fromisoformat(str(text).strip().replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None
    if data.tzinfo is None:
        data = data.replace(tzinfo=ZONA)
    return data.astimezone(ZONA).strftime("%Y-%m-%dT%H:%M")


def data_del_commit(fitxer, repo):
    """Data i hora (a Madrid) de l'últim commit que va tocar el tauler, o None."""
    relatiu = cami_relatiu(fitxer, repo)
    if not relatiu:
        return None
    try:
        r = subprocess.run(
            ["git", "-C", str(repo), "log", "-1", "--format=%cI", "--", relatiu],
            capture_output=True, text=True, check=False,
        )
    except OSError:
        return None
    if r.returncode != 0 or not r.stdout.strip():
        return None
    return data_iso_local(r.stdout.strip())


def estampa(fitxer, valor):
    """Posa `valor` a «actualitzat» conservant la resta del fitxer tal com era."""
    p = Path(fitxer)
    text = p.read_text(encoding="utf-8")
    nou, canvis = PATRO.subn(lambda m: m.group(1) + valor + m.group(2), text, count=1)
    if canvis != 1:
        return False
    json.loads(nou)  # el tauler ha de continuar sent JSON vàlid
    if nou != text:
        p.write_text(nou, encoding="utf-8")
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description="Estampa la data del darrer canvi del tauler.")
    ap.add_argument("--repo", default=str(ARREL), help="arrel del repositori git")
    ap.add_argument("--fitxer", default=str(ARREL / TAULER), help="camí de tasques.json")
    ap.add_argument("--dry-run", action="store_true", help="no escriu res")
    args = ap.parse_args(argv)

    try:
        valor = data_del_commit(args.fitxer, args.repo)
        if valor is None:
            print("Tauler: no s'ha pogut esbrinar la data del darrer canvi; es deixa com és.")
            return 0
        if args.dry_run:
            print(f"Tauler: es posaria «{valor}».")
            return 0
        if not estampa(args.fitxer, valor):
            print("Tauler: no s'hi ha trobat el camp «actualitzat»; es deixa com és.")
            return 0
        print(f"Tauler: darrera actualització «{valor}».")
    except Exception as exc:  # noqa: BLE001 — mai no ha d'aturar un desplegament
        print(f"Tauler: no s'ha pogut estampar la data ({exc}); es deixa com és.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
