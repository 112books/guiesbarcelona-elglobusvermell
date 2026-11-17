#!/usr/bin/env python3
"""
renom.py — renombra fitxes i arquitectes sense trencar enllaços.

Quan en Xavi canvia el `title` d'una fitxa o d'un arquitecte des de Sveltia CMS,
aquest script (que corre dins del job de build, abans de Hugo):

  * fitxa: mou l'arxiu al slug nou (`git mv`), afegeix l'adreça antiga a `aliases`;
  * arquitecte: propaga el nom nou a totes les fitxes (`arquitectes:` i
    `intervencions[].autors`) i a `data/arquitectes-bio-extra.yaml`, mou la carpeta
    i afegeix l'adreça antiga a `aliases`;
  * ho deixa al registre (.ai/REGISTRE-CANVIS-FITXES.md) i prepara un avís per correu.

Només biblioteca estàndard de Python (a l'Action no hi ha pip). Totes les edicions
de YAML són línia a línia sobre el text original: mai no es reformata un fitxer
i mai no s'esborra res (l'única excepció: la redirecció autoreferent, vegeu
`treu_alias`). Disseny: docs/superpowers/specs/2026-11-17-renombrar-sense-trencar-enllacos-design.md
"""
import re
import subprocess
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

CARPETA_ELEMENTS = "content/ca/elements"
CARPETA_ARQUITECTES = "content/ca/arquitectes"

RE_ELEMENT = re.compile(r"^content/ca/elements/([^/]+)\.md$")
RE_ARQUITECTE = re.compile(r"^content/ca/arquitectes/([^/]+)/_index\.md$")


# ---------------------------------------------------------------------------
# Frontmatter (sense yaml): treballem amb llistes de línies
# ---------------------------------------------------------------------------

def talla_frontmatter(text):
    """Retorna (i0, i1, linies): el frontmatter són linies[i0:i1] (sense els `---`).

    `linies` conserva els salts de línia. Si no hi ha frontmatter, retorna (0, 0, linies).
    """
    linies = text.splitlines(keepends=True)
    if not linies or linies[0].rstrip("\r\n").rstrip() != "---":
        return 0, 0, linies
    for i in range(1, len(linies)):
        if linies[i].rstrip("\r\n").rstrip() == "---":
            return 1, i, linies
    return 0, 0, linies


def _clau_primer_nivell(linia):
    m = re.match(r"^([A-Za-z_][\w-]*):(?:\s|$)", linia)
    return m.group(1) if m else None


def _desquota(valor):
    """Valor escalar YAML d'una sola línia (pla, 'simple' o "doble") -> str."""
    v = valor.strip()
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1].replace("''", "'")
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        def esc(m):
            if m.group(1):
                return chr(int(m.group(2), 16))
            return {"n": "\n", "t": "\t"}.get(m.group(3), m.group(3))
        return re.sub(r"\\(?:(u)([0-9a-fA-F]{4})|(.))", esc, v[1:-1])
    return v


def _rang_titol(linies, i0, i1):
    """(inici, fi) de les línies del `title:` (incloent continuació d'un escalar pla)."""
    for i in range(i0, i1):
        if linies[i].startswith("title:"):
            j = i + 1
            valor = linies[i][len("title:"):].strip()
            if valor and valor[0] not in "'\"|>":
                while j < i1 and linies[j][:1] in (" ", "\t") and linies[j].strip():
                    j += 1
            return i, j
    return None


def llegeix_titol(text):
    """Títol d'una fitxa llegit amb regex (sense yaml); None si no n'hi ha."""
    i0, i1, linies = talla_frontmatter(text)
    r = _rang_titol(linies, i0, i1)
    if r is None:
        return None
    a, b = r
    primer = linies[a][len("title:"):].strip()
    if b - a > 1:  # escalar pla en diverses línies: es plega amb un espai
        parts = [primer] + [l.strip() for l in linies[a + 1:b]]
        return " ".join(p for p in parts if p)
    return _desquota(primer)


# ---------------------------------------------------------------------------
# Regla de slug de les fitxes (Sveltia `slug: "{{slug}}"`)
# ---------------------------------------------------------------------------

_RE_APOSTROFS = re.compile("['’‘`\"«»·]")


def slug_fitxa(titol):
    """Slug d'arxiu que Sveltia dóna a una fitxa (regla inferida; vegeu pla §4.1)."""
    t = unicodedata.normalize("NFD", titol)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = t.lower()
    t = _RE_APOSTROFS.sub("", t)
    t = re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")


# ---------------------------------------------------------------------------
# Carpeta d'un terme d'arquitecte: la que dona Hugo (taxonomia `arquitectes`)
# ---------------------------------------------------------------------------

# Caràcters de puntuació que Hugo conserva a la ruta del terme (comprovat amb
# Hugo 0.159 sobre tests/renom/fixtures/urlize_hugo.json, sondes incloses).
_CONSERVATS = "_.~#@+-"


def urlize_arquitecte(nom):
    """Carpeta (`/arquitectes/<carpeta>/`) que Hugo dona al terme `nom`.

    Atenció: NO és el mateix que la funció de plantilla `urlize` (aquesta
    %-codifica els accents i dóna `arriola-fiol`), sinó la ruta real del terme.
    Regles, cadascuna amb l'exemple que la motiva:
      * minúscules                      «Josep Lluís Sert» -> josep-lluís-sert
      * cada espai (també nbsp) -> «-»   «Arriola & Fiol»   -> arriola--fiol (l'«&» cau)
      * es conserven lletres (amb accent), xifres i marques; _ . ~ # @ + -
                                          «Roldán+Berengué» -> roldán+berengué
      * la resta cau (& , ( ) ' ’ « » · : ! ? " – % = etc.)
                                          «Ca l’Alier» -> ca-lalier
    """
    sortida = []
    for c in nom:
        cat = unicodedata.category(c)
        if c.isspace():
            sortida.append("-")
        elif c in _CONSERVATS or cat[0] in "LM" or cat == "Nd":
            sortida.append(c)
    return "".join(sortida).lower()


# ---------------------------------------------------------------------------
# Git
# ---------------------------------------------------------------------------

class ErrorGit(RuntimeError):
    pass


def git(repo, *args, check=True, entrada=None):
    """Executa git dins de `repo`; retorna stdout (str). Mai no usa `shell=True`."""
    r = subprocess.run(["git", "-C", str(repo), "-c", "core.quotepath=false", *args],
                       capture_output=True, text=True, encoding="utf-8", input=entrada)
    if check and r.returncode != 0:
        raise ErrorGit(f"git {' '.join(args)} ha fallat: {r.stderr.strip()}")
    return r.stdout


def git_show(repo, rev, camí):
    """Contingut de `camí` a `rev`, o None si no hi existeix."""
    r = subprocess.run(["git", "-C", str(repo), "show", f"{rev}:{camí}"],
                       capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def resol_base(repo, base):
    """Resol el commit base. Si és buit, tot zeros o no existeix, usa HEAD~20."""
    if base and not re.fullmatch(r"0+", base):
        r = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}"],
                           capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout.strip()
    commits = git(repo, "rev-list", "HEAD", "--max-count=21").split()
    return commits[-1] if commits else "HEAD"


# ---------------------------------------------------------------------------
# Detecció de canvis de títol (només commits fets des de Sveltia)
# ---------------------------------------------------------------------------

# Missatge que genera Sveltia en desar una entrada existent. Els `Create …` no
# disparen renom (una entrada nova no té nom antic).
RE_MISSATGE_SVELTIA = re.compile(r"^Update (Edifici|Arquitecte) “(.+)”$")
MARCA_OPT_OUT = "[sense-renom]"


def es_commit_sveltia(missatge, autor):
    """Cert si el commit el fa l'editor (Sveltia) i no s'ha exclòs amb `[sense-renom]`."""
    if MARCA_OPT_OUT in (missatge or ""):
        return False
    if "[bot]" in (autor or ""):
        return False
    primera = (missatge or "").strip().splitlines()[0] if (missatge or "").strip() else ""
    return bool(RE_MISSATGE_SVELTIA.match(primera.strip()))


@dataclass
class Esdeveniment:
    tipus: str            # "fitxa" | "arquitecte"
    commit: str           # SHA complet del commit de Sveltia
    autor: str
    path_antic: str       # nom REAL de l'arxiu (no el que donaria la regla)
    path_nou: str         # el que toca segons el títol nou
    titol_antic: str
    titol_nou: str

    @property
    def sha7(self):
        return self.commit[:7]


def _path_nou(tipus, path_antic, titol_nou):
    if tipus == "fitxa":
        return f"{CARPETA_ELEMENTS}/{slug_fitxa(titol_nou)}.md"
    return f"{CARPETA_ARQUITECTES}/{urlize_arquitecte(titol_nou)}/_index.md"


def detecta_renoms(repo, base, cap="HEAD"):
    """Esdeveniments de renom a `base..cap`, en ordre cronològic.

    Només per commits de Sveltia i només si el fitxer existia abans i després amb
    un `title` diferent (un fitxer nou o esborrat no és un renom).
    """
    base = resol_base(repo, base)
    sep = "\x1e"
    sortida = git(repo, "log", "--reverse", "--no-merges", f"--format=%H\x1f%an <%ae>\x1f%B{sep}", f"{base}..{cap}")
    esdeveniments = []
    for bloc in sortida.split(sep):
        bloc = bloc.strip("\n")
        if not bloc.strip():
            continue
        sha, autor, missatge = bloc.split("\x1f", 2)
        sha = sha.strip()
        if not es_commit_sveltia(missatge, autor):
            continue
        fitxers = git(repo, "diff", "--name-only", "--diff-filter=M", f"{sha}^", sha, check=False).splitlines()
        for camí in fitxers:
            if RE_ELEMENT.match(camí) and not camí.endswith("/_index.md"):
                tipus = "fitxa"
            elif RE_ARQUITECTE.match(camí):
                tipus = "arquitecte"
            else:
                continue
            abans = git_show(repo, f"{sha}^", camí)
            despres = git_show(repo, sha, camí)
            if abans is None or despres is None:
                continue
            t_antic, t_nou = llegeix_titol(abans), llegeix_titol(despres)
            if not t_antic or not t_nou or t_antic == t_nou:
                continue
            esdeveniments.append(Esdeveniment(tipus, sha, autor, camí, _path_nou(tipus, camí, t_nou), t_antic, t_nou))
    return esdeveniments


def titols_arquitectes(repo):
    """{carpeta: títol} dels `_index.md` d'arquitecte a l'arbre de treball."""
    sortida = {}
    base = Path(repo) / CARPETA_ARQUITECTES
    for f in sorted(base.glob("*/_index.md")):
        t = llegeix_titol(f.read_text(encoding="utf-8"))
        if t:
            sortida[f.parent.name] = t
    return sortida


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    import argparse
    import sys
    ap = argparse.ArgumentParser(description="Renom automàtic de fitxes i arquitectes")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("slug-fitxa", help="slug que Sveltia dóna a un títol de fitxa")
    p.add_argument("titol")
    p = sub.add_parser("urlize-arquitecte", help="carpeta que Hugo dona a un nom d'arquitecte")
    p.add_argument("nom")
    args = ap.parse_args(argv)
    if args.cmd == "slug-fitxa":
        print(slug_fitxa(args.titol))
        return 0
    if args.cmd == "urlize-arquitecte":
        print(urlize_arquitecte(args.nom))
        return 0
    return 2


if __name__ == "__main__":
    import sys
    sys.exit(main())
