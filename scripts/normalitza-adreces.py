#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detecta adreces dins del camp descripcio de les fitxes d'element.
NO modifica res: genera un informe de propostes per revisar abans d'aplicar."""
import os, re, glob, datetime
try:
    import yaml
except ImportError:
    raise SystemExit("Cal PyYAML")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CDIR = os.path.join(ROOT, "content/ca/elements")
INFORME = os.path.join(ROOT, ".ai", "informe-adreces-descripcio-2026-10-13.md")

VIA = r"(?:C\.|C/|Carrer|Ctra\.|Carretera|Pl\.|Plaça|Av\.|Avinguda|Pg\.|Passeig|Ronda|Camí|Travessera|Via|Gran Via|Moll|Rambla|Parc|Jardins|Passatge|Baixada|Torrent|Riera|Autovia|Carretera)"
NAME_NUM = r"[A-ZÀ-Ü][\w'’\. ]{2,40},\s*\d"

def front(p):
    s = open(p, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", s, re.S)
    return yaml.safe_load(m.group(1)) if m else {}

def neteja(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()

files = sorted(glob.glob(os.path.join(CDIR, "*.md")))
candidats = []
for p in files:
    d = front(p)
    desc = neteja(d.get("descripcio"))
    if not desc:
        continue
    cat = None
    if re.match(r"^Adreça:\s*\S", desc):
        cat = "Etiqueta Adreça:"
    elif re.match(r"^(?:" + VIA + r")\b", desc):
        cat = "Prefix de via"
    elif re.match(r"^" + NAME_NUM, desc):
        cat = "Nom, número"
    if not cat:
        continue
    slug = os.path.basename(p)[:-3]
    adreca = neteja(d.get("adreca"))
    cos = re.sub(r"^Adreça:\s*", "", desc)
    coincideix = bool(adreca) and cos.lower().startswith(adreca.lower())
    candidats.append({"slug": slug, "adreca": adreca, "inici": cos[:170],
                      "cat": cat, "coincideix": coincideix})

avui = datetime.date.today().isoformat()
L = []
L.append("# Informe — adreces dins del camp descripcio (" + avui + ")")
L.append("")
L.append("**B3** del correu de Xavi (9/10). Detecció automàtica, **sense modificar cap fitxa**. Cal revisar cas a cas abans d'aplicar. Generat per scripts/normalitza-adreces.py.")
L.append("")
L.append("**Candidats trobats:** " + str(len(candidats)) + " (dels quals " + str(sum(1 for c in candidats if c["coincideix"])) + " ja tenen l'adreca al camp i la dupliquen al text).")
L.append("")
L.append("| # | Fitxa | Detecció | adreca actual | Inici de descripcio |")
L.append("|---|-------|----------|---------------|---------------------|")
for i, c in enumerate(candidats, 1):
    L.append("| " + str(i) + " | " + c["slug"] + " | " + c["cat"] + " | " + (c["adreca"] or "—") + " | " + c["inici"].replace("|", "/") + " |")
L.append("")
L.append("## Proposta d'actuació")
L.append("- **Ja tenen adreca** i el text la duplica: treure de descripcio el prefix que repeteix l'adreca (la informacio no es perd: es queda al camp adreca).")
L.append("- **Sense adreca**: moure el segment inicial a adreca; cal marcar manualment on acaba (no hi ha separador fiable).")
L.append("- Revisar tambe les 7 fitxes amb adreca dins d'intervencions[].descripcio.")
L.append("- Cap canvi s'aplica automaticament; aquest informe es per decidir.")

open(INFORME, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("CANDIDATS:", len(candidats))
print("PER CATEGORIA:", {k: sum(1 for c in candidats if c["cat"] == k) for k in set(c["cat"] for c in candidats)})
print("COINCIDENTS:", sum(1 for c in candidats if c["coincideix"]))
for c in candidats:
    print(" -", c["slug"], "|", c["cat"], "| adreca:", (c["adreca"] or "—"), "| duplica:", c["coincideix"])
