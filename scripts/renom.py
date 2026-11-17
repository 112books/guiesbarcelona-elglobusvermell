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


def _indexs_items_persona(linies, i0, i1):
    """Índexs de línia dels ítems de `arquitectes:` i de `intervencions[].autors`."""
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
        if clau == "intervencions":
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


def _items_arquitectes(text):
    """[(índex_línia, valor_cru, nom)] dels ítems de persona d'una fitxa."""
    i0, i1, linies = talla_frontmatter(text)
    sortida = []
    for j in _indexs_items_persona(linies, i0, i1):
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
    """Noms d'arquitecte citats a fitxes (`arquitectes:` / `autors:`) sense `_index.md` propi.

    Fora d'abast del renom, però compten per al control de col·lisió.
    """
    amb_carpeta = {t for c, t in titols_arquitectes(repo).items() if c != exclou_carpeta}
    citats = set()
    for f in sorted((Path(repo) / CARPETA_ELEMENTS).glob("*.md")):
        if f.name == "_index.md":
            continue
        for _, _, nom in _items_arquitectes(f.read_text(encoding="utf-8")):
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
