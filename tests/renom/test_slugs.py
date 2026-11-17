import glob
import os
import subprocess
import sys
from pathlib import Path

import pytest

import renom

ARREL = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).parent / "fixtures"


@pytest.mark.parametrize("titol,esperat", [
    ("Casa Bloc", "casa-bloc"),
    ("Ca l’Alier", "ca-lalier"),
    ("Col·legi de Metges", "collegi-de-metges"),
    ("Edifici d’habitatges «110 Rooms»", "edifici-dhabitatges-110-rooms"),
    ("Biblioteca Vall d'Hebron", "biblioteca-vall-dhebron"),
    ("Edifici d’habitatges dotacionals «Greenh@use»", "edifici-dhabitatges-dotacionals-greenh-use"),
    ("  Plaça Mons – obra  ", "placa-mons-obra"),
])
def test_slug_fitxa(titol, esperat):
    assert renom.slug_fitxa(titol) == esperat


def test_slug_fitxa_cli():
    r = subprocess.run([sys.executable, str(ARREL / "scripts/renom.py"), "slug-fitxa", "Casa Bloc"],
                       capture_output=True, text=True)
    assert r.stdout.strip() == "casa-bloc"


def test_llegeix_titol_formes():
    assert renom.llegeix_titol("---\ntitle: Casa Bloc\n---\n") == "Casa Bloc"
    assert renom.llegeix_titol('---\ntitle: "Jardins d\'Ada Byron"\n---\n') == "Jardins d'Ada Byron"
    assert renom.llegeix_titol("---\ntitle: 'It''s'\n---\n") == "It's"
    assert renom.llegeix_titol("---\na: 1\ntitle: «L’estel ferit»\n---\nx") == "«L’estel ferit»"
    assert renom.llegeix_titol("---\ntitle: Primera part\n  segona part\nfoto: x\n---\n") == "Primera part segona part"
    assert renom.llegeix_titol("---\na: 1\n---\n") is None
    assert renom.llegeix_titol("sense frontmatter") is None


def _excepcions():
    linies = (FIXTURES / "excepcions_fitxes.txt").read_text(encoding="utf-8").splitlines()
    return dict(l.split("\t", 1) for l in linies if l)


@pytest.mark.real
def test_slug_fitxa_contra_fitxes_reals():
    """Només lectura. Les discrepàncies han de ser exactament les excepcions preexistents."""
    excepcions = _excepcions()
    discrepancies = {}
    for f in glob.glob(str(ARREL / "content/ca/elements/*.md")):
        nom = os.path.basename(f)
        if nom == "_index.md":
            continue
        titol = renom.llegeix_titol(Path(f).read_text(encoding="utf-8"))
        assert titol, nom
        if renom.slug_fitxa(titol) != nom[:-3]:
            discrepancies[nom] = titol
    noves = set(discrepancies) - set(excepcions)
    perdudes = set(excepcions) - set(discrepancies)
    print(f"{len(discrepancies)} discrepàncies, {len(noves)} fitxes noves fora de la llista")
    assert not noves, noves
    assert not perdudes, perdudes
    # El pla en deia 27: la 27a era un artefacte (títol d'escalar pla en 2 línies
    # llegit truncat). Amb la lectura correcta en són 26.
    assert len(discrepancies) == 26


# ---- urlize d'arquitectes contra la taula generada amb Hugo 0.159 ----

def _taula_hugo():
    import json
    return json.loads((FIXTURES / "urlize_hugo.json").read_text(encoding="utf-8"))


def test_urlize_arquitecte_coincideix_amb_hugo():
    taula = _taula_hugo()
    assert len(taula) >= 280
    errors = {t: (renom.urlize_arquitecte(t), c) for t, c in taula.items()
              if renom.urlize_arquitecte(t) != c}
    assert not errors, errors


@pytest.mark.parametrize("nom,esperat", [
    ("Arriola & Fiol Arquitectes", "arriola--fiol-arquitectes"),
    ("Roldán+Berengué Arquitectes", "roldán+berengué-arquitectes"),
    ("Prince, Smith & Son", "prince-smith--son"),
    ("Josep Lluís Sert i López", "josep-lluís-sert-i-lópez"),
])
def test_urlize_arquitecte_exemples(nom, esperat):
    assert renom.urlize_arquitecte(nom) == esperat


@pytest.mark.real
def test_urlize_contra_carpetes_reals():
    """Només lectura. Les úniques carpetes reals que no són urlize(títol) són preexistents."""
    desajustos = {}
    for f in glob.glob(str(ARREL / "content/ca/arquitectes/*/_index.md")):
        titol = renom.llegeix_titol(Path(f).read_text(encoding="utf-8"))
        carpeta = Path(f).parent.name
        if renom.urlize_arquitecte(titol) != carpeta:
            desajustos[carpeta] = titol
    print(f"{len(desajustos)} carpetes preexistents ≠ urlize(títol): {sorted(desajustos)}")
    assert set(desajustos) == {"a&eb", "josep-m.-pericas", "pere-lópez-i-íñigo"}
    # i no hi ha cap títol real sense carpeta de Hugo a la taula
    taula = _taula_hugo()
    assert all(t in taula for t in desajustos.values())
