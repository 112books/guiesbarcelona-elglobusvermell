#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detecta adreces dins del camp descripcio i prepara el canvi (B3).
NO modifica cap fitxa: genera un informe i un patch .diff per revisar."""
import os, re, glob, datetime, difflib
try:
    import yaml
except ImportError:
    raise SystemExit("Cal PyYAML")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CDIR = os.path.join(ROOT, "content/ca/elements")
INFORME = os.path.join(ROOT, ".ai", "informe-adreces-descripcio-2026-10-13.md")
PATCH = os.path.join(ROOT, ".ai", "patch-adreces-descripcio.diff")

VIA = r"(?:C\.|C/|Carrer|Ctra\.|Carretera|Pl\.|Plaça|Av\.|Avinguda|Pg\.|Passeig|Ronda|Camí|Travessera|Via|Gran Via|Moll|Rambla|Parc|Jardins|Passatge|Baixada|Torrent|Riera|Autovia)"
NAME_NUM = r"[A-ZÀ-Ü][\w'’\. ]{2,40},\s*\d"

def front(p):
    s = open(p, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", s, re.S)
    return yaml.safe_load(m.group(1)) if m else {}

def neteja(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()

def norm(s):
    return s.replace("’", "'").replace("‘", "'").lower()

def yaml_scalar(v):
    return "'" + v.replace("'", "''") + "'"

def fes_patch(path, nou):
    s = open(path, encoding="utf-8").read()
    lines = s.split("\n")
    idx = None
    for i, l in enumerate(lines):
        if l.startswith("descripcio:"):
            idx = i
            break
    if idx is None:
        return None, "sense linia descripcio"
    end = idx + 1
    while end < len(lines) and lines[end].startswith(" ") and lines[end].strip():
        end += 1
    new = lines[:idx] + ["descripcio: " + yaml_scalar(nou)] + lines[end:]
    text_nou = "\n".join(new)
    m2 = re.match(r"^---\n(.*?)\n---", text_nou, re.S)
    if not m2:
        return None, "frontmatter no trobat"
    try:
        d2 = yaml.safe_load(m2.group(1))
    except Exception as e:
        return None, "YAML invalid: " + str(e)
    if neteja(d2.get("descripcio")) != neteja(nou):
        return None, "descripcio no coincideix"
    rel = os.path.relpath(path, ROOT)
    diff = list(difflib.unified_diff(lines, new, fromfile="a/" + rel, tofile="b/" + rel, lineterm=""))
    return diff, "ok"

files = sorted(glob.glob(os.path.join(CDIR, "*.md")))
candidats, nets, manuals = [], [], []
for p in files:
    d = front(p)
    desc = neteja(d.get("descripcio"))
    if not desc:
        continue
    if re.match(r"^Adreça:\s*\S", desc):
        cat = "Etiqueta Adreça:"
    elif re.match(r"^" + VIA + r"\b", desc):
        cat = "Prefix de via"
    elif re.match(r"^" + NAME_NUM, desc):
        cat = "Nom, número"
    else:
        continue
    slug = os.path.basename(p)[:-3]
    adreca = neteja(d.get("adreca"))
    cos = re.sub(r"^Adreça:\s*", "", desc)
    nou, motiu = "", ""
    if adreca and norm(cos).startswith(norm(adreca)):
        rem = cos[len(adreca):].strip()
        if rem and rem[0] not in "/|-,(:;.)":
            nou, motiu = rem, "net: treure el prefix duplicat"
        elif not rem:
            motiu = "manual: la descripcio nomes conte l'adreca"
        else:
            motiu = "manual: despres de l'adreca hi ha mes adreces o simbols"
    elif not adreca:
        motiu = "manual: la fitxa no te adreca; cal marcar on acaba"
    else:
        motiu = "manual: el text no comenca exactament per l'adreca guardada"
    c = {"path": p, "slug": slug, "adreca": adreca, "inici": cos[:170], "cat": cat, "nou": nou, "motiu": motiu}
    candidats.append(c)
    (nets if nou else manuals).append(c)

diffs, no_patch = [], []
for c in nets:
    df, mot = fes_patch(c["path"], c["nou"])
    if df:
        diffs.append("\n".join(df))
        c["patchable"] = True
    else:
        no_patch.append((c["slug"], mot))
        c["patchable"] = False

if diffs:
    open(PATCH, "w", encoding="utf-8").write("\n".join(diffs) + "\n")

avui = datetime.date.today().isoformat()
L = []
L.append("# Informe — adreces dins del camp descripcio (" + avui + ")")
L.append("")
L.append("**B3** del correu de Xavi (9/10). Deteccio automatica, **sense modificar cap fitxa**. Generat per scripts/normalitza-adreces.py.")
L.append("")
L.append("**Candidats:** " + str(len(candidats)) + " · **nets:** " + str(len(nets)) + " (patchables: " + str(sum(1 for c in nets if c["patchable"])) + ") · **manuals:** " + str(len(manuals)))
L.append("")
L.append("Patch generat a .ai/patch-adreces-descripcio.diff (no aplicat).")
L.append("")
L.append("## Canvis nets (treure el prefix duplicat)")
L.append("")
L.append("| # | Fitxa | adreca | Inici actual | Proposat: nou inici |")
L.append("|---|-------|--------|--------------|---------------------|")
for i, c in enumerate(nets, 1):
    L.append("| " + str(i) + " | " + c["slug"] + " | " + c["adreca"] + " | " + c["inici"].replace("|", "/") + " | " + c["nou"][:170].replace("|", "/") + " |")
L.append("")
L.append("## Revisio manual")
L.append("")
L.append("| # | Fitxa | Deteccio | adreca | Inici | Motiu |")
L.append("|---|-------|----------|--------|-------|-------|")
for i, c in enumerate(manuals, 1):
    L.append("| " + str(i) + " | " + c["slug"] + " | " + c["cat"] + " | " + (c["adreca"] or "—") + " | " + c["inici"].replace("|", "/") + " | " + c["motiu"] + " |")
open(INFORME, "w", encoding="utf-8").write("\n".join(L) + "\n")

print("CANDIDATS:", len(candidats), "| NETS:", len(nets), "| PATCHABLES:", sum(1 for c in nets if c["patchable"]), "| MANUALS:", len(manuals))
print("SENSE PATCH:", no_patch)
print("PATCH:", PATCH, os.path.getsize(PATCH) if os.path.exists(PATCH) else 0, "bytes")
