#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detecta adreces dins del camp descripcio i prepara el canvi (B3).
NO modifica cap fitxa: genera un informe amb el valor proposat per a cada cas."""
import os, re, glob, datetime
try:
    import yaml
except ImportError:
    raise SystemExit("Cal PyYAML")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CDIR = os.path.join(ROOT, "content/ca/elements")
INFORME = os.path.join(ROOT, ".ai", "informe-adreces-descripcio-2026-10-13.md")

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
    c = {"slug": slug, "adreca": adreca, "inici": cos[:170], "cat": cat, "nou": nou, "motiu": motiu}
    candidats.append(c)
    (nets if nou else manuals).append(c)

avui = datetime.date.today().isoformat()
L = []
L.append("# Informe — adreces dins del camp descripcio (" + avui + ")")
L.append("")
L.append("**B3** del correu de Xavi (9/10). Deteccio automatica, **sense modificar cap fitxa**. Generat per scripts/normalitza-adreces.py. Cal vist-i-plau abans d'aplicar.")
L.append("")
L.append("**Candidats:** " + str(len(candidats)) + " · **canvi net (llest per aplicar):** " + str(len(nets)) + " · **revisio manual:** " + str(len(manuals)))
L.append("")
L.append("## Canvis nets (treure el prefix duplicat)")
L.append("")
L.append("Per a cada cas, la descripcio comenca per l'adreca que ja es al camp; es proposa treure'n el prefix. La informacio no es perd: es queda al camp adreca.")
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
L.append("")
L.append("## Notes")
L.append("- Cap canvi s'aplica automaticament; aquest informe i el patch son per revisar.")
L.append("- Pendent tambe revisar les 7 fitxes amb adreca dins d'intervencions[].descripcio.")

open(INFORME, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("CANDIDATS:", len(candidats), "| NETS:", len(nets), "| MANUALS:", len(manuals))
for c in nets:
    print("  NET:", c["slug"], "|", c["adreca"], "->", c["nou"][:90])
