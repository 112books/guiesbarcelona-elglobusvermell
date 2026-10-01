#!/usr/bin/env python3
"""Resum de tasques i temps per al control horari i la rentabilitat.

Llegeix els registres diaris de `.taques/<projecte>/*.md` (format del skill
time-tracker) i genera un document amb totes les tasques fetes, la durada de
cadascuna i els totals. Serveix per estudiar la rentabilitat del projecte al
final, sense esborrar mai cap registre.

Ús:
    python3 scripts/resum-tasques.py                      # projecte per defecte: elglobusvermell.org
    python3 scripts/resum-tasques.py --project altre
    python3 scripts/resum-tasques.py --out docs/resum.md
    python3 scripts/resum-tasques.py --csv docs/resum.csv

Els fitxers `.taques/` són dades locals (gitignored); aquest script no les mou.
"""
import argparse
import csv
import os
import re
import sys
from datetime import datetime

TASK_RE = re.compile(r"^###\s+(.+?)\s*$")
DUR_RE = re.compile(r"\*\*Durada:\*\*\s*(.+)")
HORA_RE = re.compile(r"\*\*Hora inici:\*\*\s*(.+)")
ESTAT_RE = re.compile(r"\*\*Estat:\*\*\s*(.+)")
DESC_RE = re.compile(r"\*\*Descripció:\*\*\s*(.+)")


def parse_durada(text):
    """Retorna minuts a partir de '1h 30min', '45 min', '5 min'..."""
    if not text:
        return 0
    text = text.strip().replace("~", "").replace("≈", "")
    h = re.search(r"(\d+)\s*h", text)
    m = re.search(r"(\d+)\s*min", text)
    total = 0
    if h:
        total += int(h.group(1)) * 60
    if m:
        total += int(m.group(1))
    if not h and not m:
        plain = re.search(r"(\d+)", text)
        if plain:
            total = int(plain.group(1))
    return total


def parse_day(path):
    tasks = []
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = TASK_RE.match(line)
            if m:
                if cur:
                    tasks.append(cur)
                cur = {"titol": m.group(1), "durada_text": "", "minuts": 0,
                       "hora": "", "estat": "", "descripcio": ""}
                continue
            if cur is None:
                continue
            d = DUR_RE.search(line)
            if d:
                cur["durada_text"] = d.group(1).strip()
                cur["minuts"] = parse_durada(d.group(1))
            h = HORA_RE.search(line)
            if h:
                cur["hora"] = h.group(1).strip()
            e = ESTAT_RE.search(line)
            if e:
                cur["estat"] = e.group(1).strip()
            de = DESC_RE.search(line)
            if de:
                cur["descripcio"] = de.group(1).strip()
    if cur:
        tasks.append(cur)
    return tasks


def fmt_minuts(m):
    if m >= 60:
        return f"{m // 60}h {m % 60:02d}min"
    return f"{m} min"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(here)
    default_project = "elglobusvermell.org"
    taques_root = os.path.join(repo, ".taques")
    if os.path.isdir(taques_root) and not os.path.isdir(os.path.join(taques_root, default_project)):
        subdirs = sorted(d for d in os.listdir(taques_root)
                         if os.path.isdir(os.path.join(taques_root, d)))
        if subdirs:
            default_project = subdirs[0]

    ap = argparse.ArgumentParser(description="Resum de tasques i temps del control horari")
    ap.add_argument("--project", default=default_project)
    ap.add_argument("--out", default=None, help="Fitxer markdown de sortida")
    ap.add_argument("--csv", default=None, help="Fitxer CSV de sortida (opcional)")
    args = ap.parse_args()

    project_dir = os.path.join(taques_root, args.project)
    if not os.path.isdir(project_dir):
        sys.exit(f"No trobo el directori {project_dir}")

    dies = []
    for name in sorted(os.listdir(project_dir)):
        if not name.endswith(".md") or name.startswith("."):
            continue
        if name in ("config.md", "resum-tasques.md"):
            continue
        data = name[:-3]
        tasks = parse_day(os.path.join(project_dir, name))
        if tasks:
            dies.append((data, tasks))

    files = [(d, t, min(x["minuts"] for x in t) if t else 0) for d, t in dies]
    total_min = sum(x["minuts"] for _, tasks in dies for x in tasks)
    n_tasques = sum(len(tasks) for _, tasks in dies)

    linies = []
    linies.append("# Resum de tasques i temps — control horari")
    linies.append("")
    linies.append(f"Projecte: **{args.project}**  ")
    linies.append(f"Generat: {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    linies.append(f"Font: `.taques/{args.project}/*.md` (registres diaris, append-only)")
    linies.append("")
    linies.append("## Totals")
    linies.append("")
    linies.append("| Mètrica | Valor |")
    linies.append("|---------|-------|")
    linies.append(f"| Dies amb registre | {len(dies)} |")
    linies.append(f"| Tasques | {n_tasques} |")
    linies.append(f"| Temps total | {fmt_minuts(total_min)} ({total_min / 60:.2f} h) |")
    if len(dies):
        linies.append(f"| Mitjana per dia treballat | {fmt_minuts(round(total_min / len(dies)))} |")
    linies.append("")
    linies.append("## Tasques per dia")
    for data, tasks in dies:
        day_min = sum(t["minuts"] for t in tasks)
        linies.append("")
        linies.append(f"### {data} — {fmt_minuts(day_min)}")
        linies.append("")
        linies.append("| Tasca | Durada | Estat |")
        linies.append("|-------|--------|-------|")
        for t in tasks:
            titol = t["titol"].replace("|", "\\|")
            linies.append(f"| {titol} | {fmt_minuts(t['minuts'])} | {t['estat'] or '-'} |")

    report = "\n".join(linies) + "\n"
    out = args.out or os.path.join(project_dir, "resum-tasques.md")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Escrit: {out}")
    print(f"Tasques: {n_tasques} · Temps total: {fmt_minuts(total_min)} ({total_min / 60:.2f} h)")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["data", "hora_inici", "tasca", "minuts", "durada", "estat"])
            for data, tasks in dies:
                for t in tasks:
                    w.writerow([data, t["hora"], t["titol"], t["minuts"],
                                fmt_minuts(t["minuts"]), t["estat"]])
        print(f"CSV: {args.csv}")


if __name__ == "__main__":
    main()
