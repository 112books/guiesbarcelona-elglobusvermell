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

No toca `static/admin/galeria/dades.json` (decisió Q8, opció B): és un fitxer de l'admin
que ja no coincideix amb el contingut i regenerar-lo el reformataria sencer; per
això, després d'un renom l'admin mostra el slug antic fins que es regeneri a mà.

Només biblioteca estàndard de Python (a l'Action no hi ha pip). Totes les edicions
de YAML són línia a línia sobre el text original: mai no es reformata un fitxer
i mai no s'esborra res (l'única excepció: la redirecció autoreferent, vegeu
`treu_alias`). Disseny: docs/superpowers/specs/2026-11-17-renombrar-sense-trencar-enllacos-design.md
"""
import re
import subprocess
import sys
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
# `aliases`: només s'hi afegeix (l'única excepció és `treu_alias`, Tasca 15)
# ---------------------------------------------------------------------------

_RE_ITEM_INLINE = re.compile(r"""\s*("(?:[^"\\]|\\.)*"|'(?:[^']|'')*'|[^,\]\s][^,\]]*?)\s*(?:,|$)""")


def _salt(linia):
    """Salt de línia de `linia` ('\\r\\n', '\\n' o '')."""
    return linia[len(linia.rstrip("\r\n")):]


def _troba_aliases(linies, i0, i1):
    """(i_clau, i_fi, forma): forma = 'inline' | 'bloc'; (None, None, None) si no n'hi ha.

    Per a 'bloc', linies[i_clau+1:i_fi] són els ítems (poden ser 0).
    """
    for i in range(i0, i1):
        m = re.match(r"^aliases:(.*)$", linies[i].rstrip("\r\n"))
        if not m:
            continue
        resta = m.group(1).strip()
        if resta.startswith("["):
            return i, i + 1, "inline"
        j = i + 1
        while j < i1 and re.match(r"^\s*-(\s|$)", linies[j]):
            j += 1
        return i, j, "bloc"
    return None, None, None


def _items_inline(linia):
    """Tokens crus (amb cometes) d'una línia `aliases: [..]`."""
    interior = linia[linia.index("[") + 1:linia.rindex("]")]
    return [m.group(1) for m in _RE_ITEM_INLINE.finditer(interior) if m.group(1)]


def llegeix_aliases(text):
    """Llista d'aliases (valors sense cometes) d'un fitxer de contingut."""
    i0, i1, linies = talla_frontmatter(text)
    k, fi, forma = _troba_aliases(linies, i0, i1)
    if forma == "inline":
        return [_desquota(t) for t in _items_inline(linies[k])]
    if forma == "bloc":
        return [_desquota(re.match(r"^\s*-\s*(.*?)\s*$", l.rstrip("\r\n")).group(1)) for l in linies[k + 1:fi]]
    return []


def _cita(valor, estil='"'):
    """Valor amb les cometes de l'`estil` (escapant-ne el que cal)."""
    if estil == "'":
        return "'" + valor.replace("'", "''") + "'"
    return '"' + valor.replace("\\", "\\\\").replace('"', '\\"') + '"'


def afegeix_alias(text, nova, canonica=None):
    """Afegeix `nova` a `aliases` sense tocar res més. Idempotent.

    * si `nova` ja hi és (qualsevol forma) o és la URL canònica pròpia: no fa res;
    * inline: `, "nova"` abans del `]`; en bloc: línia nova després de l'últim ítem;
    * sense `aliases`: línia `aliases: ["nova"]` sota el primer `---`.
    """
    if nova == canonica or nova in llegeix_aliases(text):
        return text
    i0, i1, linies = talla_frontmatter(text)
    if i1 == 0:
        raise ValueError("el fitxer no té frontmatter")
    k, fi, forma = _troba_aliases(linies, i0, i1)
    nl = _salt(linies[0]) or "\n"
    if forma == "inline":
        linia = linies[k].rstrip("\r\n")
        pos = linia.rindex("]")
        interior = linia[linia.index("[") + 1:pos].strip()
        estil = "'" if interior.startswith("'") else '"'
        sep = ", " if interior else ""
        linies[k] = linia[:pos].rstrip() + sep + _cita(nova, estil) + linia[pos:] + _salt(linies[k])
    elif forma == "bloc":
        if fi > k + 1:
            ultim = linies[fi - 1].rstrip("\r\n")
            m = re.match(r"^(\s*)-\s+(.*?)\s*$", ultim)
            sagnat, valor = (m.group(1), m.group(2)) if m else ("  ", "")
            if valor[:1] == '"':
                nou = _cita(nova, '"')
            elif valor[:1] == "'":
                nou = _cita(nova, "'")
            else:
                nou = nova if not re.search(r"[\s#'\"{}\[\],*!|>%@`]|: |:$", nova) else _cita(nova)
        else:
            sagnat, nou = "  ", nova
        # si l'últim ítem no acaba en salt de línia (final de fitxer improbable), afegeix-lo
        if not linies[fi - 1].endswith(("\n", "\r")):
            linies[fi - 1] += nl
        linies.insert(fi, f"{sagnat}- {nou}{nl}")
    else:
        linies.insert(i0, f"aliases: [{_cita(nova)}]{nl}")
    return "".join(linies)


def treu_alias(text, alias):
    """Treu de `aliases` EXACTAMENT `alias` (única excepció a «mai no s'esborra res»:
    la redirecció autoreferent, Tasca 15a). Edició d'una sola línia; res més no es toca."""
    i0, i1, linies = talla_frontmatter(text)
    k, fi, forma = _troba_aliases(linies, i0, i1)
    if forma == "inline":
        tokens = _items_inline(linies[k])
        restants = [t for t in tokens if _desquota(t) != alias]
        if len(restants) == len(tokens):
            return text
        linia = linies[k].rstrip("\r\n")
        linies[k] = linia[:linia.index("[") + 1] + ", ".join(restants) + linia[linia.rindex("]"):] + _salt(linies[k])
    elif forma == "bloc":
        for j in range(k + 1, fi):
            if _desquota(re.match(r"^\s*-\s*(.*?)\s*$", linies[j].rstrip("\r\n")).group(1)) == alias:
                del linies[j]
                break
        else:
            return text
    return "".join(linies)


# ---------------------------------------------------------------------------
# Substitució del nom d'arquitecte a les fitxes (camps estructurats, línia a línia)
# ---------------------------------------------------------------------------

_RE_ITEM_LLISTA = re.compile(r"^(\s*-\s+)(.*?)(\s*)$")
_VALORS_ESPECIALS = {"null", "true", "false", "yes", "no", "on", "off", "~", "y", "n"}


def _pla_es_segur(v):
    """Cert si `v` es pot escriure com a escalar pla YAML sense canviar de significat."""
    if not v or v != v.strip() or "\t" in v or "\n" in v:
        return False
    if v[0] in "-?:,[]{}#&*!|>'\"%@`":
        return False
    if ": " in v or " #" in v or v.endswith(":"):
        return False
    if v.lower() in _VALORS_ESPECIALS or re.fullmatch(r"[-+]?[\d.][\d._,eE+-]*", v):
        return False
    return True


def formata_valor(nou, cru_original):
    """Escriu `nou` mantenint l'estil de cometes de `cru_original`.

    Pla -> pla (o cometes simples si cal); 'simple' -> 'simple'; "doble" -> "doble".
    """
    if cru_original[:1] == "'":
        return _cita(nou, "'")
    if cru_original[:1] == '"':
        return _cita(nou, '"')
    return nou if _pla_es_segur(nou) else _cita(nou, "'")


def _indexs_items_persona(linies, i0, i1, autors=True):
    """Índexs de línia dels ítems de `arquitectes:` i (si `autors`) de `intervencions[].autors`."""
    indexs = []
    i = i0
    while i < i1:
        clau = _clau_primer_nivell(linies[i])
        if clau == "arquitectes":
            j = i + 1
            while j < i1 and _RE_ITEM_LLISTA.match(linies[j].rstrip("\r\n")):
                indexs.append(j)
                j += 1
            i = j
            continue
        if clau == "intervencions" and autors:
            j = i + 1
            while j < i1 and (not linies[j].strip() or linies[j][:1] in (" ", "-", "\t")):
                m = re.match(r"^(\s*)(-\s+)?autors:\s*$", linies[j].rstrip("\r\n"))
                if m:
                    sagnat_clau = len(m.group(1)) + (len(m.group(2)) if m.group(2) else 0)
                    k = j + 1
                    while k < i1:
                        mi = _RE_ITEM_LLISTA.match(linies[k].rstrip("\r\n"))
                        if not mi or len(mi.group(1)) - len(mi.group(1).lstrip()) < sagnat_clau:
                            break
                        indexs.append(k)
                        k += 1
                    j = k
                    continue
                j += 1
            i = j
            continue
        i += 1
    return indexs


def _items_arquitectes(text, autors=True):
    """[(índex_línia, valor_cru, nom)] dels ítems de persona d'una fitxa."""
    i0, i1, linies = talla_frontmatter(text)
    sortida = []
    for j in _indexs_items_persona(linies, i0, i1, autors):
        cru = _RE_ITEM_LLISTA.match(linies[j].rstrip("\r\n")).group(2)
        sortida.append((j, cru, _desquota(cru)))
    return sortida


def substitueix_arquitecte_a_fitxa(text, nom_antic, nom_nou):
    """Canvia `nom_antic` per `nom_nou` NOMÉS als ítems de `arquitectes:` i
    `intervencions[].autors` (coincidència exacta del valor). Retorna (text, n_canvis)."""
    i0, i1, linies = talla_frontmatter(text)
    n = 0
    for j in _indexs_items_persona(linies, i0, i1):
        linia = linies[j]
        m = _RE_ITEM_LLISTA.match(linia.rstrip("\r\n"))
        if _desquota(m.group(2)) != nom_antic:
            continue
        linies[j] = m.group(1) + formata_valor(nom_nou, m.group(2)) + m.group(3) + _salt(linia)
        n += 1
    return "".join(linies), n


def substitueix_terme_bio(text_yaml, nom_antic, nom_nou):
    """A `data/arquitectes-bio-extra.yaml`, canvia només la línia `terme:` exacta."""
    linies = text_yaml.splitlines(keepends=True)
    n = 0
    for j, linia in enumerate(linies):
        m = re.match(r"^(\s*(?:-\s+)?terme:\s*)(.*?)(\s*)$", linia.rstrip("\r\n"))
        if m and _desquota(m.group(2)) == nom_antic:
            linies[j] = m.group(1) + formata_valor(nom_nou, m.group(2)) + m.group(3) + _salt(linia)
            n += 1
    return "".join(linies), n


def noms_sense_carpeta(repo, exclou_carpeta=None):
    """Noms citats a `arquitectes:` de les fitxes (els únics que són termes de la taxonomia;
    `intervencions[].autors` és text de crèdit lliure) sense `_index.md` propi.

    Fora d'abast del renom, però compten per al control de col·lisió.
    """
    amb_carpeta = {t for c, t in titols_arquitectes(repo).items() if c != exclou_carpeta}
    citats = set()
    for f in sorted((Path(repo) / CARPETA_ELEMENTS).glob("*.md")):
        if f.name == "_index.md":
            continue
        for _, _, nom in _items_arquitectes(f.read_text(encoding="utf-8"), autors=False):
            citats.add(nom)
    return sorted(citats - amb_carpeta)


# ---------------------------------------------------------------------------
# Aplicació dels renoms: primer es planifica tot en memòria (cap escriptura),
# després s'escriu. Qualsevol col·lisió/error abans d'escriure = refús i cap canvi.
# ---------------------------------------------------------------------------

URL_BASE = "https://112books.github.io/guiesbarcelona-elglobusvermell"
CARPETA_BIO = "data/arquitectes-bio-extra.yaml"


class Refus(Exception):
    """El renom no es pot aplicar (col·lisió, adreça invàlida, …). `args[0]` = motiu en català."""


@dataclass
class Pla:
    moviments: list = field(default_factory=list)      # [(origen, destí)] relatius a l'arrel
    escriptures: dict = field(default_factory=dict)    # {camí final: text nou}
    actualitzats: list = field(default_factory=list)   # camins de fitxes d'element tocades
    enllaços: list = field(default_factory=list)       # camins d'altres fitxers amb l'enllaç corregit
    avisos: list = field(default_factory=list)
    alies_eliminats: list = field(default_factory=list)
    alies_afegits: list = field(default_factory=list)
    n_prosa: int = 0
    noms_actualitzats: dict = field(default_factory=dict)   # {camí: títol} de les fitxes tocades


@dataclass
class ResultatAplicacio:
    esdeveniment: object
    estat: str                 # "aplicat" | "refusat" | "sense-canvi" | "omes"
    motiu: str = ""
    url_antiga: str = ""       # ruta (p. ex. /elements/a/)
    url_nova: str = ""
    path_final: str = ""
    pla: object = None
    avisos: list = field(default_factory=list)

    @property
    def fitxes_actualitzades(self):
        return list(self.pla.actualitzats) if self.pla else []

    @property
    def alies_eliminats(self):
        return list(self.pla.alies_eliminats) if self.pla else []


def _llegeix(repo, camí):
    return (Path(repo) / camí).read_text(encoding="utf-8")


def _tots_els_md(repo):
    """Camins relatius de tots els .md de content/."""
    arrel = Path(repo)
    return sorted(str(p.relative_to(arrel)) for p in (arrel / "content").rglob("*.md"))


def indexa_aliases(repo):
    """{alias: [camí, …]} de tot el contingut."""
    index = {}
    for camí in _tots_els_md(repo):
        for a in llegeix_aliases(_llegeix(repo, camí)):
            index.setdefault(a, []).append(camí)
    return index


def url_canonica(camí):
    """Adreça canònica d'una fitxa o d'un arquitecte, o None per a altres fitxers."""
    m = RE_ELEMENT.match(camí)
    if m and m.group(1) != "_index":
        return f"/elements/{m.group(1)}/"
    m = RE_ARQUITECTE.match(camí)
    if m:
        return f"/arquitectes/{m.group(1)}/"
    return None


def _resol(repo, camí, mapa):
    """Camí actual d'un fitxer que pot haver estat mogut per un esdeveniment anterior."""
    return mapa.get(camí, camí) if mapa is not None else camí


def _gestiona_alias_propi(text, camí_propi, url_antiga, url_nova, index, pla):
    """Afegeix l'alias antiga i resol la col·lisió de la nova amb aliases (Tasca 15a).

    * la nova és alias d'ALTRA entrada -> Refus;
    * la nova és alias de la MATEIXA entrada -> se'n treu només aquesta (única excepció
      a «mai no s'esborra res»; queda al registre i al correu).
    """
    propietaris = [c for c in index.get(url_nova, []) if c != camí_propi]
    if propietaris:
        raise Refus(f"l'adreça nova {url_nova} ja és una redirecció de {propietaris[0]}")
    for u in url_antiga if isinstance(url_antiga, list) else [url_antiga]:
        if u != url_nova and u not in llegeix_aliases(text):
            pla.alies_afegits.append(u)
        text = afegeix_alias(text, u, canonica=url_nova)
    if url_nova in llegeix_aliases(text):
        text = treu_alias(text, url_nova)
        pla.alies_eliminats.append(url_nova)
    return text


def _substitueix_enllaços(text, antic, nou):
    """Canvia `antic` per `nou` línia a línia, excepte dins de `aliases` (són adreces antigues)."""
    i0, i1, linies = talla_frontmatter(text)
    k, fi, forma = _troba_aliases(linies, i0, i1)
    n = 0
    for j, l in enumerate(linies):
        if k is not None and k <= j < fi:
            continue
        if antic in l:
            linies[j] = l.replace(antic, nou)
            n += l.count(antic)
    return "".join(linies), n


def planifica_renom_fitxa(repo, ev, mapa=None):
    pla = Pla()
    antic = _resol(repo, ev.path_antic, mapa)
    if not (Path(repo) / antic).exists():
        raise FileNotFoundError(antic)
    stem_antic = Path(antic).stem
    stem_nou = slug_fitxa(ev.titol_nou)
    if not stem_nou:
        raise Refus(f"el títol «{ev.titol_nou}» no dóna cap adreça vàlida")
    path_nou = f"{CARPETA_ELEMENTS}/{stem_nou}.md"
    if path_nou == antic:
        return pla, antic, antic, True
    if (Path(repo) / path_nou).exists():
        raise Refus(f"ja existeix una fitxa amb l'adreça /elements/{stem_nou}/ ({path_nou})")
    index = indexa_aliases(repo)
    url_antiga, url_nova = f"/elements/{stem_antic}/", f"/elements/{stem_nou}/"
    text = _gestiona_alias_propi(_llegeix(repo, antic), antic, url_antiga, url_nova, index, pla)
    pla.moviments.append((antic, path_nou))
    pla.escriptures[path_nou] = text
    # Enllaços interns a l'adreça antiga (fora de les fitxes d'element: allà només hi ha aliases)
    for camí in _tots_els_md(repo):
        if RE_ELEMENT.match(camí):
            continue
        t = _llegeix(repo, camí)
        if url_antiga in t:
            nou_t, n = _substitueix_enllaços(t, url_antiga, url_nova)
            if n:
                pla.escriptures[camí] = nou_t
                pla.enllaços.append(camí)
    return pla, antic, path_nou, False


def escriu_pla(repo, pla):
    """Aplica un pla a l'arbre de treball (i a l'índex de git)."""
    arrel = Path(repo)
    for origen, desti in pla.moviments:
        (arrel / desti).parent.mkdir(parents=True, exist_ok=True)
        git(repo, "mv", origen, desti)
    for camí, text in pla.escriptures.items():
        (arrel / camí).write_text(text, encoding="utf-8", newline="")
        git(repo, "add", "--", camí)


def desfes_arbre(repo):
    """Retorna l'arbre de treball a HEAD (només local; mai toca el remot)."""
    git(repo, "reset", "--hard", "HEAD", check=False)
    git(repo, "clean", "-fdq", "--", "content", "data", check=False)


def aplica_renom_fitxa(repo, ev, mapa=None):
    """Renom d'una fitxa: `git mv` + alias antiga + enllaços interns. Retorna ResultatAplicacio."""
    try:
        pla, antic, nou, igual = planifica_renom_fitxa(repo, ev, mapa)
    except Refus as r:
        return ResultatAplicacio(ev, "refusat", str(r))
    except FileNotFoundError as e:
        return ResultatAplicacio(ev, "omes", f"la fitxa {e} ja no existeix")
    except Exception as e:  # error inesperat en planificar: res no s'ha escrit
        return ResultatAplicacio(ev, "refusat", f"error inesperat: {e}")
    url_antiga, url_nova = f"/elements/{Path(antic).stem}/", f"/elements/{Path(nou).stem}/"
    if igual:
        return ResultatAplicacio(ev, "sense-canvi", "el títol nou dóna la mateixa adreça", url_antiga, url_antiga, antic, pla)
    try:
        escriu_pla(repo, pla)
    except Exception as e:  # error inesperat a mig d'escriure: tornem l'arbre a l'estat de HEAD
        desfes_arbre(repo)
        return ResultatAplicacio(ev, "refusat", f"error inesperat: {e}")
    if mapa is not None:
        mapa[ev.path_antic] = nou
    return ResultatAplicacio(ev, "aplicat", "", url_antiga, url_nova, nou, pla)


def planifica_renom_arquitecte(repo, ev, mapa=None):
    pla = Pla()
    arrel = Path(repo)
    antic = _resol(repo, ev.path_antic, mapa)
    if not (arrel / antic).exists():
        raise FileNotFoundError(antic)
    carpeta_antiga = Path(antic).parent.name
    nom_antic, nom_nou = ev.titol_antic, ev.titol_nou
    slug_nou = urlize_arquitecte(nom_nou)
    if not slug_nou or "/" in nom_nou or "\\" in nom_nou:
        raise Refus(f"el nom «{nom_nou}» no dóna una adreça vàlida (sense «/» ni barres)")
    # --- col·lisions ---
    titols = titols_arquitectes(repo)
    for carpeta, t in titols.items():
        if carpeta != carpeta_antiga and t == nom_nou:
            raise Refus(f"ja existeix un arquitecte amb el nom «{nom_nou}» (/arquitectes/{carpeta}/)")
    if slug_nou != carpeta_antiga and (arrel / CARPETA_ARQUITECTES / slug_nou).exists():
        raise Refus(f"ja existeix l'arquitecte amb l'adreça /arquitectes/{slug_nou}/")
    sense = noms_sense_carpeta(repo, exclou_carpeta=carpeta_antiga)
    if nom_nou in sense:
        raise Refus(f"«{nom_nou}» ja surt a fitxes com a arquitecte (sense fitxa pròpia): es fusionarien")
    altres = {t for c, t in titols.items() if c != carpeta_antiga} | {n for n in sense if n != nom_antic}
    for t in sorted(altres):
        if urlize_arquitecte(t) == slug_nou:
            raise Refus(f"l'adreça /arquitectes/{slug_nou}/ coincideix amb la del terme «{t}»")
    index = indexa_aliases(repo)
    # --- propagació a fitxes d'element ---
    for camí in _tots_els_md(repo):
        if not RE_ELEMENT.match(camí) or camí.endswith("/_index.md"):
            continue
        t = _llegeix(repo, camí)
        if nom_antic not in t:
            continue
        nou_t, n = substitueix_arquitecte_a_fitxa(t, nom_antic, nom_nou)
        if n:
            pla.escriptures[camí] = nou_t
            pla.actualitzats.append(camí)
            pla.noms_actualitzats[camí] = llegeix_titol(nou_t) or Path(camí).stem
        if nom_antic in nou_t:
            pla.n_prosa += 1   # el nom queda en prosa lliure (descripcio): no es toca
    # --- bio extra ---
    if (arrel / CARPETA_BIO).exists():
        t = _llegeix(repo, CARPETA_BIO)
        nou_t, n = substitueix_terme_bio(t, nom_antic, nom_nou)
        if n:
            pla.escriptures[CARPETA_BIO] = nou_t
    # --- carpeta i alias ---
    url_nova = f"/arquitectes/{slug_nou}/"
    urls_antigues = [f"/arquitectes/{carpeta_antiga}/"]
    u2 = f"/arquitectes/{urlize_arquitecte(nom_antic)}/"
    if u2 not in urls_antigues:
        urls_antigues.append(u2)
    camí_nou = f"{CARPETA_ARQUITECTES}/{slug_nou}/_index.md"
    text = _gestiona_alias_propi(_llegeix(repo, antic), antic, urls_antigues, url_nova, index, pla)
    if slug_nou != carpeta_antiga:
        pla.moviments.append((f"{CARPETA_ARQUITECTES}/{carpeta_antiga}", f"{CARPETA_ARQUITECTES}/{slug_nou}"))
    pla.escriptures[camí_nou if slug_nou != carpeta_antiga else antic] = text
    return pla, antic, (camí_nou if slug_nou != carpeta_antiga else antic), carpeta_antiga, slug_nou


def aplica_renom_arquitecte(repo, ev, mapa=None):
    try:
        pla, antic, nou, carpeta_antiga, slug_nou = planifica_renom_arquitecte(repo, ev, mapa)
    except Refus as r:
        return ResultatAplicacio(ev, "refusat", str(r))
    except FileNotFoundError as e:
        return ResultatAplicacio(ev, "omes", f"l'arquitecte {e} ja no existeix")
    except Exception as e:
        return ResultatAplicacio(ev, "refusat", f"error inesperat: {e}")
    try:
        escriu_pla(repo, pla)
    except Exception as e:
        desfes_arbre(repo)
        return ResultatAplicacio(ev, "refusat", f"error inesperat: {e}")
    if mapa is not None:
        mapa[ev.path_antic] = nou
    return ResultatAplicacio(ev, "aplicat", "", f"/arquitectes/{carpeta_antiga}/", f"/arquitectes/{slug_nou}/", nou, pla)


# ---------------------------------------------------------------------------
# Refús: es reverteix el títol (només la línia `title:`)
# ---------------------------------------------------------------------------

def refusa(repo, ev, motiu, mapa=None):
    """Restaura el títol antic a la línia `title:` de l'arxiu de l'esdeveniment.

    No toca res més del commit de l'editor. Retorna ResultatAplicacio('refusat')
    amb `path_final` = arxiu on s'ha revertit el títol (o '' si ja no existeix).
    """
    camí = _resol(repo, ev.path_antic, mapa)
    p = Path(repo) / camí
    antic_text = git_show(repo, f"{ev.commit}^", ev.path_antic)
    if not p.exists() or antic_text is None:
        return ResultatAplicacio(ev, "refusat", motiu)
    a0, a1, al = talla_frontmatter(antic_text)
    r_antic = _rang_titol(al, a0, a1)
    c0, c1, cl = talla_frontmatter(p.read_text(encoding="utf-8"))
    r_nou = _rang_titol(cl, c0, c1)
    if r_antic and r_nou:
        cl[r_nou[0]:r_nou[1]] = al[r_antic[0]:r_antic[1]]
        p.write_text("".join(cl), encoding="utf-8", newline="")
        git(repo, "add", "--", camí)
    return ResultatAplicacio(ev, "refusat", motiu, path_final=camí)


def aplica_esdeveniment(repo, ev, mapa=None):
    """Aplica un esdeveniment; si es refusa, reverteix el títol (Tasca 9)."""
    aplica = aplica_renom_fitxa if ev.tipus == "fitxa" else aplica_renom_arquitecte
    r = aplica(repo, ev, mapa)
    if r.estat == "refusat":
        r.path_final = refusa(repo, ev, r.motiu, mapa).path_final
    return r


# ---------------------------------------------------------------------------
# Casos límit (Tasca 15b): una pestanya antiga de l'editor que recrea l'arxiu vell
# ---------------------------------------------------------------------------

def detecta_conflictes(repo):
    """Llista de descripcions (català) de conflictes a l'arbre que impedeixen publicar.

    * l'adreça d'una fitxa/arquitecte és alhora una redirecció (`aliases`) d'una altra
      entrada: típic d'una pestanya antiga de Sveltia que recrea l'arxiu abans de moure'l;
    * dos arquitectes amb el mateix nom (pàgina partida).
    No esborra ni mou res.
    """
    conflictes = []
    canon = {}
    for camí in _tots_els_md(repo):
        u = url_canonica(camí)
        if u:
            canon[u] = camí
    for alias, propietaris in sorted(indexa_aliases(repo).items()):
        c = canon.get(alias)
        if c and c not in propietaris:
            conflictes.append(f"L'adreça {alias} és alhora una pàgina ({c}) i una redirecció de {propietaris[0]}.")
    vistos = {}
    for carpeta, t in sorted(titols_arquitectes(repo).items()):
        if t in vistos:
            conflictes.append(f"Hi ha dos arquitectes amb el mateix nom «{t}» ({vistos[t]} i {carpeta}).")
        vistos[t] = carpeta
    return conflictes


# ---------------------------------------------------------------------------
# Registre (.ai/REGISTRE-CANVIS-FITXES.md): s'hi afegeix al final, mai no es toca el text previ
# ---------------------------------------------------------------------------

REGISTRE = ".ai/REGISTRE-CANVIS-FITXES.md"
APROVACIO = "automàtic — regla aprovada per Joan 17/11/2026"


def _md(text):
    """Escapa els caràcters de Markdown (i la barra de les taules) d'un nom."""
    return re.sub(r"([\\`*_\[\]|<>])", r"\\\1", text)


def _url(ruta):
    from urllib.parse import quote
    return f"{URL_BASE}{quote(ruta, safe='/~@')}"


def _nom_autor(autor):
    """`xaviglobus <x@y>` -> `xaviglobus`."""
    return re.sub(r"\s*<.*>\s*$", "", autor or "").strip() or "desconegut"


def _ara(ara=None):
    from datetime import datetime, timezone
    if ara is not None:
        return ara
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("Europe/Madrid"))
    except Exception:
        return datetime.now(timezone.utc)


def entrada_registre(r):
    """Dades del registre a partir d'un ResultatAplicacio."""
    ev = r.esdeveniment
    pla = r.pla
    return {
        "tipus": ev.tipus, "autor": _nom_autor(ev.autor), "clau": ev.sha7,
        "titol_antic": ev.titol_antic, "titol_nou": ev.titol_nou,
        "url_antiga": r.url_antiga, "url_nova": r.url_nova,
        "estat": r.estat, "motiu": r.motiu,
        "fitxes": [(c, (pla.noms_actualitzats.get(c) if pla else None) or Path(c).stem) for c in (pla.actualitzats if pla else [])],
        "enllaços": list(pla.enllaços) if pla else [],
        "alies_eliminats": list(pla.alies_eliminats) if pla else [],
        "n_prosa": pla.n_prosa if pla else 0,
    }


def ja_registrat(repo, entrada):
    """Idempotència: el commit de l'editor (SHA) amb aquests noms ja és al registre?"""
    p = Path(repo) / REGISTRE
    if not p.exists():
        return False
    text = p.read_text(encoding="utf-8")
    for bloc in text.split("\n### ")[1:]:
        capçalera = bloc.splitlines()[0]
        if f"`{entrada['clau']}`" not in bloc:
            continue
        if entrada["tipus"] == "conflicte":
            return "conflicte" in capçalera
        if f"«{_md(entrada['titol_antic'])}» → «{_md(entrada['titol_nou'])}»" in capçalera:
            return True
    return False


def compon_bloc_registre(e, ara=None):
    ara = _ara(ara)
    data = ara.strftime("%Y-%m-%d %H:%M")
    if e["tipus"] == "conflicte":
        linies = [
            f"### {data} — conflicte detectat: cal revisar abans de publicar", "",
            f"- **Clau del conflicte:** `{e['clau']}`",
            "- **Tipus:** conflicte (pestanya antiga de l'editor o noms duplicats)",
            "- **Detall:**",
        ] + [f"  - {_md(d)}" for d in e["detall"]] + [
            "- **Resultat:** build aturat abans de Hugo; no s'ha esborrat ni mogut res (es manté l'últim desplegament bo)",
            f"- **Aprovació:** {APROVACIO}",
        ]
        return "\n".join(linies) + "\n"
    nom_tipus = "fitxa" if e["tipus"] == "fitxa" else "arquitecte"
    acció = "refús de renom" if e["estat"] == "refusat" else "renom"
    l = [f"### {data} — {acció} de {nom_tipus} «{_md(e['titol_antic'])}» → «{_md(e['titol_nou'])}»", "",
         f"- **Autor del desament:** {_md(e['autor'])} (commit `{e['clau']}`)",
         f"- **Tipus:** {nom_tipus}"]
    if e["url_antiga"] or e["url_nova"]:
        l.append(f"- **Adreça antiga → nova:** `{e['url_antiga']}` → `{e['url_nova']}`")
    if e["tipus"] == "arquitecte" and e["estat"] == "aplicat":
        enllaços = ", ".join(f"[{_md(n)}]({_url('/elements/' + Path(c).stem + '/')})" for c, n in e["fitxes"])
        l.append(f"- **Fitxes actualitzades:** {len(e['fitxes'])}" + (f" ({enllaços})" if enllaços else ""))
        if e["n_prosa"]:
            l.append(f"- **Text lliure (descripcions) on encara surt el nom antic:** {e['n_prosa']} fitxes (no es toca)")
    if e["enllaços"]:
        l.append("- **Enllaços interns corregits a:** " + ", ".join(f"`{c}`" for c in e["enllaços"]))
    if e["alies_eliminats"]:
        l.append("- **Redireccions retirades:** " + ", ".join(f"`{a}`" for a in e["alies_eliminats"]) +
                 " (ara és l'adreça de la pàgina; única excepció a «no s'esborra res»)")
    if e["estat"] == "aplicat":
        l.append("- **Resultat:** aplicat")
    elif e["estat"] == "refusat":
        l.append(f"- **Resultat:** refusat ({_md(e['motiu'])}); s'ha revertit el títol a «{_md(e['titol_antic'])}»")
    else:
        l.append(f"- **Resultat:** sense canvi d'adreça ({_md(e['motiu'])})")
    l.append(f"- **Aprovació:** {APROVACIO}")
    l.append("- **Commit del robot:** el commit `auto:` que porta aquesta mateixa entrada")
    return "\n".join(l) + "\n"


def afegeix_registre(repo, entrada, ara=None):
    """Afegeix el bloc al final del registre. Retorna False (sense escriure) si ja hi era."""
    if ja_registrat(repo, entrada):
        return False
    p = Path(repo) / REGISTRE
    p.parent.mkdir(parents=True, exist_ok=True)
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    sep = "" if not text else ("\n" if text.endswith("\n") else "\n\n")
    with open(p, "a", encoding="utf-8", newline="") as f:
        f.write(sep + ("\n" if text else "") + compon_bloc_registre(entrada, ara))
    return True


# ---------------------------------------------------------------------------
# Correu d'avís (SMTP). Mai no fa fallar el deploy; mai no imprimeix la contrasenya.
# ---------------------------------------------------------------------------

REMITENT = "webmaster@linuxbcn.com"
FRASE_RECARREGA = "Recarrega l'editor abans de continuar editant."


def _llista_enllaços(r):
    return [(n, _url("/elements/" + Path(c).stem + "/")) for c, n in entrada_registre(r)["fitxes"]]


def compon_avis(r):
    """(assumpte, cos) en català planer, amb enllaços sencers. `r` és un ResultatAplicacio,
    o un dict {'tipus': 'conflicte', 'detall': [...]}."""
    peu = "\nUna salutació,\nLinuxBCN\n"
    if isinstance(r, dict) and r.get("tipus") == "conflicte":
        cos = ["Hola,", "",
               "No s'ha publicat res de nou al web perquè hem detectat un conflicte que cal revisar:", ""]
        cos += [f"  - {d}" for d in r["detall"]]
        cos += ["",
                "Això passa, per exemple, si una pestanya de l'editor que feia estona que era oberta torna a "
                "desar una fitxa amb el nom vell. El web continua mostrant l'última versió bona.",
                "No s'ha esborrat ni mogut res. Ho revisarà en Joan a mà; no cal que facis res.",
                "", FRASE_RECARREGA]
        return "Atenció: cal revisar el web abans de publicar més canvis", "\n".join(cos) + "\n" + peu
    ev = r.esdeveniment
    tipus = "la fitxa" if ev.tipus == "fitxa" else "l'arquitecte"
    nom_tipus = "fitxa" if ev.tipus == "fitxa" else "arquitecte"
    A, B = ev.titol_antic, ev.titol_nou
    if r.estat == "refusat":
        cos = ["Hola,", "",
               f"No s'ha pogut canviar el nom {tipus} «{A}» per «{B}».", "",
               f"Motiu: {r.motiu}.", "",
               f"Hem deixat el nom tal com era abans («{A}») perquè el web no es trenqui. "
               "Què pots fer: tria un altre nom per a aquesta entrada, o desfés el canvi i continua com abans.",
               "", FRASE_RECARREGA]
        return f"No s'ha pogut canviar el nom: «{A}» → «{B}»", "\n".join(cos) + "\n" + peu
    if r.estat == "sense-canvi":
        cos = ["Hola,", "", f"Has canviat el nom {tipus} «{A}» per «{B}». L'adreça de la pàgina no canvia "
               f"(continua sent {_url(r.url_antiga)}), així que no ha calgut fer res més.", "", FRASE_RECARREGA]
        return f"Canvi de nom aplicat: {nom_tipus} «{A}» → «{B}»", "\n".join(cos) + "\n" + peu
    cos = ["Hola,", "",
           f"S'ha canviat el nom {tipus} «{A}» per «{B}» i el web s'ha deixat coherent automàticament.", "",
           "L'adreça nova és:", _url(r.url_nova), "",
           "L'adreça antiga continua funcionant: qui hi entri serà dut automàticament a la nova:", _url(r.url_antiga)]
    llista = _llista_enllaços(r)
    if ev.tipus == "arquitecte":
        cos += ["", f"S'ha actualitzat el nom a {len(llista)} fitxes:"] if llista else ["", "Cap fitxa citava aquest nom."]
        cos += [f"  - {n}: {u}" for n, u in llista]
    if r.alies_eliminats:
        cos += ["", "Detall tècnic: " + ", ".join(
            f"s'ha tret la redirecció {a} perquè ara és l'adreça de la pàgina" for a in r.alies_eliminats) + "."]
    cos += ["", FRASE_RECARREGA]
    return f"Canvi de nom aplicat: {nom_tipus} «{A}» → «{B}»", "\n".join(cos) + "\n" + peu


def _neteja(text, secrets):
    for s in secrets:
        if s:
            text = text.replace(s, "***")
    return text


def envia_avis(assumpte, cos, env=None, smtp_classe=None, smtp_ssl_classe=None):
    """Envia un correu. Retorna SEMPRE 0: un error d'SMTP va a stderr i no fa fallar el deploy.

    Variables d'entorn (GitHub Secrets): SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD i
    AVIS_DESTINATARIS (adreces separades per comes). Si en falta alguna, s'omet l'enviament.
    """
    import os
    import sys
    from email.message import EmailMessage
    env = os.environ if env is None else env
    host, port = env.get("SMTP_HOST"), env.get("SMTP_PORT")
    usuari, clau = env.get("SMTP_USER"), env.get("SMTP_PASSWORD")
    dest = [d.strip() for d in (env.get("AVIS_DESTINATARIS") or "").split(",") if d.strip()]
    falten = [n for n, v in (("SMTP_HOST", host), ("SMTP_PORT", port), ("SMTP_USER", usuari),
                             ("SMTP_PASSWORD", clau), ("AVIS_DESTINATARIS", dest)) if not v]
    if falten:
        print(f"avís per correu omès: falten els secrets {', '.join(falten)}", file=sys.stderr)
        return 0
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = REMITENT, ", ".join(dest), assumpte
    msg.set_content(cos)
    try:
        import smtplib
        port = int(port)
        if port == 465:
            s = (smtp_ssl_classe or smtplib.SMTP_SSL)(host, port, timeout=30)
        else:
            s = (smtp_classe or smtplib.SMTP)(host, port, timeout=30)
        try:
            if port == 587:
                s.starttls()
            s.login(usuari, clau)
            s.send_message(msg, from_addr=REMITENT, to_addrs=dest)
        finally:
            try:
                s.quit()
            except Exception:
                pass
    except Exception as e:   # smtplib.SMTPException, OSError, ValueError…
        print(f"avís per correu no enviat ({type(e).__name__}): {_neteja(str(e), [clau, usuari])}", file=sys.stderr)
    return 0


# ---------------------------------------------------------------------------
# Flux complet: detecta -> aplica -> registre -> un commit per esdeveniment -> push
# ---------------------------------------------------------------------------

ROBOT_NOM = "github-actions[bot]"
ROBOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


def _commit_robot(repo, missatge):
    git(repo, "-c", f"user.name={ROBOT_NOM}", "-c", f"user.email={ROBOT_EMAIL}", "commit", "-q", "-m", missatge)


def _missatge_commit(r):
    ev = r.esdeveniment
    A, B = ev.titol_antic, ev.titol_nou
    if r.estat == "refusat":
        return f"auto: renom refusat de {ev.tipus} «{A}» → «{B}» (títol revertit)"
    if r.estat == "sense-canvi":
        return f"auto: renom de {ev.tipus} «{A}» → «{B}» (sense canvi d'adreça)"
    if ev.tipus == "arquitecte":
        n = len(r.fitxes_actualitzades)
        return f"auto: renom arquitecte «{A}» → «{B}» ({n} {'fitxa' if n == 1 else 'fitxes'})"
    return f"auto: renom fitxa «{A}» → «{B}»"


def _passada(repo, base, cap, ara=None):
    """Una passada: retorna (n_commits, avisos, codi). No fa push."""
    conflictes = detecta_conflictes(repo)
    if conflictes:
        import hashlib
        clau = hashlib.sha1("\n".join(conflictes).encode("utf-8")).hexdigest()[:7]
        e = {"tipus": "conflicte", "clau": clau, "detall": conflictes}
        n = 0
        if afegeix_registre(repo, e, ara=ara):
            git(repo, "add", "--", REGISTRE)
            _commit_robot(repo, "auto: registra un conflicte que impedeix publicar")
            n = 1
        print("CONFLICTE: no es publica res.\n  " + "\n  ".join(conflictes), file=sys.stderr)
        return n, [dict(zip(("assumpte", "cos"), compon_avis({"tipus": "conflicte", "detall": conflictes})))], 1
    mapa, bloquejats, avisos, n = {}, set(), [], 0
    for ev in detecta_renoms(repo, base, cap):
        entrada_previa = {"tipus": ev.tipus, "clau": ev.sha7, "titol_antic": ev.titol_antic, "titol_nou": ev.titol_nou}
        if ja_registrat(repo, entrada_previa):
            continue                                       # idempotència: ja processat
        if ev.path_antic in bloquejats:
            print(f"omès (l'esdeveniment anterior d'aquest arxiu s'ha refusat): {ev.path_antic}", file=sys.stderr)
            continue
        r = aplica_esdeveniment(repo, ev, mapa)
        if r.estat == "omes":
            print(f"omès: {r.motiu}", file=sys.stderr)
            continue
        if r.estat == "refusat":
            bloquejats.add(ev.path_antic)
        afegeix_registre(repo, entrada_registre(r), ara=ara)
        git(repo, "add", "-A", "--", "content", "data", REGISTRE)
        _commit_robot(repo, _missatge_commit(r))
        n += 1
        a, c = compon_avis(r)
        avisos.append({"assumpte": a, "cos": c})
    return n, avisos, 0


def executa_flux(repo, base, cap="HEAD", push=True, remot="origin", branca="main", max_intents=3,
                 avisos_json=None, ara=None):
    """Executa el flux complet. Retorna el codi de sortida (0 = ok, 1 = conflicte o push impossible).

    Si el push és rebutjat (algú ha pujat mentre), NO es fa rebase d'un commit derivat:
    `reset --hard` a l'última versió del remot (només s'hi perden els commits del robot, encara
    no pujats) i es torna a calcular tot sobre el cap nou. Màxim `max_intents`. Mai `--force`.
    """
    import json
    repo = Path(repo)
    base_sha = resol_base(repo, base)
    cap_actual = cap
    codi, avisos = 1, []
    for intent in range(1, max_intents + 1):
        n, avisos, codi = _passada(repo, base_sha, cap_actual, ara=ara)
        if n == 0 or not push:
            break
        r = subprocess.run(["git", "-C", str(repo), "push", remot, f"HEAD:{branca}"], capture_output=True, text=True)
        if r.returncode == 0:
            break
        print(f"push rebutjat (intent {intent}/{max_intents}); es recalcula sobre el remot:\n{r.stderr.strip()}", file=sys.stderr)
        f = subprocess.run(["git", "-C", str(repo), "fetch", remot, branca], capture_output=True, text=True)
        if f.returncode != 0:
            print(f"no s'ha pogut obtenir el remot: {f.stderr.strip()}", file=sys.stderr)
            codi, avisos = 1, []
            break
        git(repo, "reset", "--hard", "FETCH_HEAD")
        cap_actual = "HEAD"
        codi, avisos = 1, []
    else:
        print(f"no s'ha pogut pujar després de {max_intents} intents", file=sys.stderr)
        codi = 1
    if avisos_json:
        Path(avisos_json).write_text(json.dumps(avisos, ensure_ascii=False, indent=1), encoding="utf-8")
    return codi


def envia_avisos_fitxer(fitxer, no_enviar=False, sortida=None):
    """Envia (o, amb `no_enviar`, desa a `sortida`) els avisos que ha deixat `run`. Sempre 0."""
    import json
    p = Path(fitxer)
    if not p.exists():
        return 0
    for i, a in enumerate(json.loads(p.read_text(encoding="utf-8")), 1):
        if no_enviar:
            if sortida:
                Path(sortida).mkdir(parents=True, exist_ok=True)
                (Path(sortida) / f"avis-{i}.txt").write_text(f"Assumpte: {a['assumpte']}\n\n{a['cos']}", encoding="utf-8")
        else:
            envia_avis(a["assumpte"], a["cos"])
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Renom automàtic de fitxes i arquitectes")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("slug-fitxa", help="slug que Sveltia dóna a un títol de fitxa")
    p.add_argument("titol")
    p = sub.add_parser("urlize-arquitecte", help="carpeta que Hugo dona a un nom d'arquitecte")
    p.add_argument("nom")
    p = sub.add_parser("run", help="detecta i aplica els renoms de base..cap (un commit per esdeveniment)")
    p.add_argument("--repo", default=".")
    p.add_argument("--base", default="", help="SHA anterior (github.event.before); buit/zeros -> HEAD~20")
    p.add_argument("--cap", default="HEAD")
    p.add_argument("--remot", default="origin")
    p.add_argument("--branca", default="main")
    p.add_argument("--no-push", action="store_true", help="no puja res (proves locals)")
    p.add_argument("--no-enviar", action="store_true", help="compatibilitat: `run` mai no envia correus")
    p.add_argument("--avisos-json", help="desa aquí els avisos pendents (els envia `envia-avisos`)")
    p = sub.add_parser("envia-avisos", help="envia els avisos que ha deixat `run` (mai falla)")
    p.add_argument("fitxer")
    p.add_argument("--no-enviar", action="store_true", help="en lloc d'enviar, escriu els cossos a --sortida")
    p.add_argument("--sortida", help="carpeta (temporal) on escriure els cossos amb --no-enviar")
    args = ap.parse_args(argv)
    if args.cmd == "slug-fitxa":
        print(slug_fitxa(args.titol))
        return 0
    if args.cmd == "urlize-arquitecte":
        print(urlize_arquitecte(args.nom))
        return 0
    if args.cmd == "run":
        return executa_flux(args.repo, args.base, args.cap, push=not args.no_push, remot=args.remot,
                            branca=args.branca, avisos_json=args.avisos_json)
    if args.cmd == "envia-avisos":
        return envia_avisos_fitxer(args.fitxer, args.no_enviar, args.sortida)
    return 2


if __name__ == "__main__":
    sys.exit(main())
