#!/usr/bin/env python3
"""Proposta de neteja de la informació encallada a «projecte» (B2/B4, correu de Xavi 9/10).

NOMÉS LLEGEIX: no modifica cap fitxa. Genera un informe Markdown amb, per a cada
fitxa afectada, el valor actual i la proposta, classificada en:

  AUTO   — patró inequívoc; es podria aplicar per script després de l'aprovació.
  REVISA — proposta automàtica que cal mirar a ull (noms, anys aproximats).
  MANUAL — cal decidir-ho a mà (text truncat, diverses fases, dades que falten).

Regla del projecte: MAI no s'esborra res. Les propostes només mouen text d'un camp
a un altre dins la mateixa fitxa; el text original es conserva sempre.

Ús:  python3 scripts/proposa-neteja-projecte.py > .ai/informe-neteja-projecte-AAAA-MM-DD.md
"""
import glob
import os
import re
import sys
from collections import Counter

import yaml

ELEMENTS = "content/ca/elements"
PERIODE = re.compile(r"^(inici|finals?|principis?|segona|primera|segle|segles|s\.|anys)\b", re.I)
ANY = re.compile(r"\d{4}")
ETIQUETES = ("Projecte original", "Rehabilitació", "Reforma", "Remodelació", "Ampliació")


def llegeix(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def separa_autor_any(valor):
    """«Autor. 1910, aprox.» -> ('Autor', '1910, aprox.'); None si no és clar."""
    v = str(valor).strip()
    m = re.match(r"^(?P<autor>.+?)[.,]\s+(?P<any>(?:\d{4}|inici|finals?|principis?|segona|c\.).*)$", v, re.I)
    if not m:
        return None
    autor, any_ = m.group("autor").strip(), m.group("any").strip()
    if ANY.match(autor) or PERIODE.match(autor):
        return None
    return autor, any_


def separa_nom_autor_any(valor):
    """Edifici original «Nom. Autor. 1880» -> (nom, autor, any)."""
    parts = [p.strip() for p in re.split(r"\.\s+", str(valor).strip().rstrip(".")) if p.strip()]
    if len(parts) >= 3 and ANY.search(parts[-1]):
        return ". ".join(parts[:-2]), parts[-2], parts[-1]
    if len(parts) == 2 and ANY.search(parts[-1]):
        return parts[0], "", parts[1]
    return None


def cel(v):
    s = str(v).replace("|", "/").replace("\n", " ")
    return s if len(s) <= 140 else s[:137] + "…"


def main():
    files = []  # (patró, fitxa, actual, proposta, classe)
    for path in sorted(glob.glob(os.path.join(ELEMENTS, "*.md"))):
        slug = os.path.basename(path)[:-3]
        if slug == "_index":
            continue
        d = llegeix(path)
        ivs = d.get("intervencions") or []
        pt = d.get("projecte_text")

        # 1. Autor i any barrejats dins intervencions[].any
        for n, iv in enumerate(ivs):
            a = str(iv.get("any") or "")
            if not a or re.fullmatch(r"[\d\s\-–/,+]+", a):
                continue
            if PERIODE.match(a) or re.fullmatch(r"\d{4},? aprox\.?", a):
                continue  # període o any aproximat: és un any vàlid en text
            if " + " in a or ":" in a or "(?)" in a:
                files.append(("1", slug, f"any: «{a}»", "Diverses fases o autoria dubtosa: separar a mà", "MANUAL"))
                continue
            sep = separa_autor_any(a)
            if sep and not (iv.get("autors") or "").strip():
                classe = "AUTO" if ANY.match(sep[1]) else "REVISA"
                files.append(("1", slug, f"any: «{a}»", f"autors: «{sep[0]}» · any: «{sep[1]}»", classe))
            elif not ANY.search(a) and not (iv.get("autors") or "").strip():
                files.append(("1", slug, f"any: «{a}»", f"autors: «{a}» · any: (buit)", "REVISA"))
            else:
                files.append(("1", slug, f"any: «{a}»", "Cal mirar-ho", "MANUAL"))

        # 2. projecte_text repetit (la plantilla el pinta a part, amb la intervenció)
        if pt:
            igual = any(str(iv.get("any") or "").strip() == str(pt).strip() for iv in ivs)
            if igual:
                files.append(("2", slug, f"projecte_text: «{pt}»", "Ja és a la intervenció: no mostrar-lo dos cops (plantilla; el camp es conserva)", "AUTO"))
            else:
                files.append(("2", slug, f"projecte_text: «{pt}»", "No coincideix amb cap intervenció: revisar", "MANUAL"))

        # 3. edifici_original -> intervenció «Projecte original»
        eo = d.get("edifici_original")
        if eo:
            sep = separa_nom_autor_any(eo)
            if sep and not re.search(r"\bs\.$|\bs\.\s*$", str(eo).strip()):
                nom, autor, any_ = sep
                proposta = f"nova intervenció «Projecte original»: autors «{autor}» · any «{any_}» · descripció «{nom}»"
                classe = "REVISA" if (not autor or re.search(r"(\b\w+\b) \1$", autor)) else "AUTO"
                files.append(("3", slug, f"edifici_original: «{eo}»", proposta, classe))
            else:
                files.append(("3", slug, f"edifici_original: «{eo}»", "Text truncat o sense any: completar amb el WordPress en producció", "MANUAL"))

        # 4-6. Etiquetes del WordPress dins de descripcions
        textos = [("descripcio", d.get("descripcio") or "")]
        textos += [(f"intervencions[{n}].descripcio", iv.get("descripcio") or "") for n, iv in enumerate(ivs)]
        for camp, t in textos:
            t = str(t)
            m = re.match(r"^\s*Categoria:\s*(.+?)(?:\s{2,}|\s(?=[A-ZÀ-Ú][a-zà-ú]+\s[a-zà-ú])|$)", t)
            if m:
                tip = m.group(1).strip()
                classe = "AUTO" if not d.get("tipologia") else "REVISA"
                files.append(("4", slug, f"{camp}: «{cel(t[:80])}»", f"tipologia: «{tip}» (si està buida) i treure l'etiqueta del text", classe))
            m = re.match(r"^\s*(Premi [^.]+?\d{4}|Premi Ciutat de Barcelona(?: \d{4})?)", t)
            if m:
                files.append(("5", slug, f"{camp}: «{cel(t[:80])}»", f"premis: «{m.group(1).strip()}»", "REVISA"))
            for et in ETIQUETES:
                m = re.search(et + r":\s*([^.]+?)\.\s*(\d{4}(?:[-–]\d{4})?|[Ss]egle [IVXL]+)", t)
                if m:
                    autor, any_ = m.group(1).strip(), m.group(2)
                    if len(autor) < 4:
                        files.append(("6", slug, f"{camp}: «{cel(t[:90])}»", f"«{et}» sense autor clar: passar-ho a intervenció a mà", "MANUAL"))
                        break
                    ja_hi_es = any(any_ in str(iv.get("any") or "") and autor.lower()[:12] in str(iv.get("autors") or "").lower()
                                   for iv in ivs)
                    if ja_hi_es:
                        files.append(("6", slug, f"{camp}: «{cel(t[:90])}»",
                                      f"Ja és a les intervencions ({et}: {autor}, {any_}): treure-ho només del text", "AUTO"))
                    else:
                        files.append(("6", slug, f"{camp}: «{cel(t[:90])}»",
                                      f"nova intervenció «{et}»: autors «{autor}» · any «{any_}»", "REVISA"))
                    break
                if re.search(et + r":", t):
                    files.append(("6", slug, f"{camp}: «{cel(t[:90])}»", f"«{et}» dins el text: passar-ho a intervenció a mà", "MANUAL"))
                    break

    noms = {
        "1": "Autor i any barrejats al camp «any» de la intervenció",
        "2": "«projecte_text» repetit",
        "3": "«Edifici original» que hauria de ser una intervenció «Projecte original»",
        "4": "Etiqueta «Categoria:» del WordPress dins la descripció",
        "5": "Premis dins la descripció",
        "6": "«Projecte original», «Reforma», «Rehabilitació»… dins la descripció",
    }
    out = sys.stdout
    total = Counter(c for *_, c in files)
    fitxes = len({f[1] for f in files})
    out.write("# Proposta de neteja — informació encallada a «projecte»\n\n")
    out.write("Generat per `scripts/proposa-neteja-projecte.py` (només lectura: **no s'ha aplicat res**).\n\n")
    out.write("Origen: correu de Xavi del 9/10 (B2/B4): «moltes informacions han quedat encallades dins l'etiqueta projecte… Ho fem nosaltres manualment fitxa per fitxa?».\n\n")
    out.write("**Regla:** no s'esborra res. Cada proposta mou text d'un camp a un altre dins la mateixa fitxa, i la plantilla deixa de mostrar-lo repetit.\n\n")
    out.write("## Resum\n\n| Patró | Casos | AUTO | REVISA | MANUAL |\n|---|---|---|---|---|\n")
    for k, nom in noms.items():
        sub = [f for f in files if f[0] == k]
        cc = Counter(f[4] for f in sub)
        out.write(f"| {k}. {nom} | {len(sub)} | {cc['AUTO']} | {cc['REVISA']} | {cc['MANUAL']} |\n")
    out.write(f"| **Total** ({fitxes} fitxes) | **{len(files)}** | **{total['AUTO']}** | **{total['REVISA']}** | **{total['MANUAL']}** |\n\n")
    out.write("- **AUTO:** patró inequívoc; es pot aplicar per script un cop aprovat.\n")
    out.write("- **REVISA:** el script fa la proposta, però cal una ullada (noms, anys aproximats, tipologia ja plena).\n")
    out.write("- **MANUAL:** text truncat a la migració, diverses fases o dades que falten; es completa amb el WordPress en producció.\n\n")
    for k, nom in noms.items():
        sub = [f for f in files if f[0] == k]
        if not sub:
            continue
        out.write(f"## {k}. {nom} ({len(sub)})\n\n| Fitxa | Ara | Proposta | Tipus |\n|---|---|---|---|\n")
        for _, slug, actual, prop, classe in sub:
            out.write(f"| `{slug}` | {cel(actual)} | {cel(prop)} | {classe} |\n")
        out.write("\n")


if __name__ == "__main__":
    main()
