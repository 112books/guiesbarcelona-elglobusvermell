import difflib

import pytest
import yaml

import renom
from conftest import FITXES


def fm(text):
    return yaml.safe_load(text.split("---\n")[1])


def linies_canviades(a, b):
    return [l for l in difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and l[:3] not in ("+++", "---")]


# ---- substitueix_arquitecte_a_fitxa ----

def test_indentacio_zero_sense_cometes():
    t = FITXES["casa-bloc"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Josep Lluís Sert", "Josep Lluís Sert i López")
    assert n == 1
    assert fm(r)["arquitectes"] == ["Josep Lluís Sert i López", "Pere López"]
    assert linies_canviades(t, r) == ["-- Josep Lluís Sert", "+- Josep Lluís Sert i López"]


def test_indentacio_dos_cometes_dobles():
    t = FITXES["torre-llevant"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Josep Lluís Sert", "Josep Sert")
    assert n == 1
    assert '  - "Josep Sert"\n' in r
    assert fm(r)["arquitectes"] == ["Arriola & Fiol Arquitectes", "Josep Sert"]


def test_intervencions_autors_cometes_simples():
    t = FITXES["lestel-ferit"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Rebecca Horn", "Rebecca Horn Estudi")
    assert n == 2  # arquitectes: + intervencions[].autors
    assert "    - 'Rebecca Horn Estudi'\n" in r
    d = fm(r)
    assert d["arquitectes"][0] == "Rebecca Horn Estudi"
    assert d["intervencions"][0]["autors"] == ["Rebecca Horn Estudi", "Pere López"]
    # la descripció (prosa lliure) no es toca
    assert "Autoria: Rebecca Horn. 1992" in r


def test_nom_nou_amb_ampersand_es_valid_sense_cometes():
    t = FITXES["casa-bloc"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Pere López", "Arriola & Fiol Arquitectes")
    assert n == 1
    assert "- Arriola & Fiol Arquitectes\n" in r
    assert fm(r)["arquitectes"][1] == "Arriola & Fiol Arquitectes"


@pytest.mark.parametrize("nou", ["Estudi: Nom", "Estudi #1", "&Estudi", "- Estudi", "yes", "123", "Estudi:"])
def test_nom_nou_que_necessita_cometes(nou):
    t = FITXES["casa-bloc"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Pere López", nou)
    assert n == 1
    assert fm(r)["arquitectes"][1] == nou
    assert f"- '{nou}'\n" in r


def test_nom_nou_amb_cometa_simple_en_estil_simple():
    t = FITXES["lestel-ferit"]
    r, _ = renom.substitueix_arquitecte_a_fitxa(t, "Pere López", "Pere l'Estudi")
    assert "    - 'Pere l''Estudi'\n" in r
    assert fm(r)["intervencions"][0]["autors"][1] == "Pere l'Estudi"


def test_subcadena_no_es_toca():
    t = FITXES["mixta"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Pere López", "Pere Nou")
    assert n == 1
    assert fm(r)["arquitectes"] == ["Pere López Íñigo", "Pere Nou", "Arriola & Fiol Arquitectes"]


def test_nom_dues_vegades():
    t = '---\narquitectes:\n- A\n- B\nintervencions:\n- any: 1\n  autors:\n  - A\ntitle: T\n---\n'
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "A", "C")
    assert n == 2
    d = fm(r)
    assert d["arquitectes"] == ["C", "B"] and d["intervencions"][0]["autors"] == ["C"]


def test_nom_absent_no_es_error():
    t = FITXES["casa-bloc"]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Ningú", "Algú")
    assert (r, n) == (t, 0)


def test_titol_i_descripcio_no_es_toquen():
    t = '---\ntitle: Pere López\ndescripcio: Obra de Pere López\narquitectes:\n- Pere López\n---\n'
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Pere López", "Pere Nou")
    assert n == 1
    assert "title: Pere López\n" in r and "Obra de Pere López" in r


@pytest.mark.parametrize("stem", list(FITXES))
def test_yaml_equivalent_abans_i_despres(stem):
    t = FITXES[stem]
    r, n = renom.substitueix_arquitecte_a_fitxa(t, "Pere López", "Pere López Nou")
    a, b = fm(t), fm(r)
    assert a.keys() == b.keys()
    canviats = {k for k in a if a[k] != b[k]}
    assert canviats <= {"arquitectes", "intervencions"}
    if n == 0:
        assert r == t
    # només han canviat línies d'ítem
    for l in linies_canviades(t, r):
        assert l[1:].lstrip().startswith("- ")


def test_fitxa_sense_arquitectes_buida():
    t = "---\narquitectes: []\ntitle: T\n---\n"
    assert renom.substitueix_arquitecte_a_fitxa(t, "A", "B") == (t, 0)


# ---- terme bio ----

def test_terme_bio_amb_cometes_dobles():
    t = '- terme: "Arriola & Fiol Arquitectes"\n  tipus: estudi\n- terme: Altre\n'
    r, n = renom.substitueix_terme_bio(t, "Arriola & Fiol Arquitectes", "A&F: Estudi")
    assert n == 1
    assert '- terme: "A&F: Estudi"\n' in r and "  tipus: estudi\n" in r
    assert yaml.safe_load(r)[0]["terme"] == "A&F: Estudi"


def test_terme_bio_sense_cometes_i_exacte():
    t = "- terme: Pere López\n- terme: Pere López Íñigo\n"
    r, n = renom.substitueix_terme_bio(t, "Pere López", "Pere Nou")
    assert n == 1 and r == "- terme: Pere Nou\n- terme: Pere López Íñigo\n"


def test_noms_sense_carpeta(repo_prova):
    assert renom.noms_sense_carpeta(repo_prova) == ["Sense Carpeta Uno"]
