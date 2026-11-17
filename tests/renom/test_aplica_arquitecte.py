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


def test_noms_sense_carpeta_nomes_compta_arquitectes_no_autors(repo_prova):
    assert renom.noms_sense_carpeta(repo_prova) == ["Sense Carpeta Uno"]


# ---------------- aplica_renom_arquitecte (Tasca 8) ----------------

from conftest import canvia_titol, commit_sveltia, git  # noqa: E402


def sveltia_canvia_arq(repo, carpeta, nou):
    base = git(repo, "rev-parse", "HEAD")
    canvia_titol(repo, f"content/ca/arquitectes/{carpeta}/_index.md", nou)
    commit_sveltia(repo, "Arquitecte", carpeta)
    return renom.detecta_renoms(repo, base, "HEAD")[0]


def llegeix(repo, camí):
    return (repo / camí).read_text(encoding="utf-8")


def test_renom_arquitecte_propaga_i_mou_carpeta(repo_prova):
    ev = sveltia_canvia_arq(repo_prova, "pere-lópez", "Pere López Núñez")
    r = renom.aplica_renom_arquitecte(repo_prova, ev)
    assert r.estat == "aplicat", r.motiu
    assert (r.url_antiga, r.url_nova) == ("/arquitectes/pere-lópez/", "/arquitectes/pere-lópez-núñez/")
    # fitxes: indentació 0 (casa-bloc), intervencions[].autors (lestel-ferit), i la mixta
    assert fm(llegeix(repo_prova, "content/ca/elements/casa-bloc.md"))["arquitectes"] == ["Josep Lluís Sert", "Pere López Núñez"]
    d = fm(llegeix(repo_prova, "content/ca/elements/lestel-ferit.md"))
    assert d["intervencions"][0]["autors"] == ["Rebecca Horn", "Pere López Núñez"]
    assert fm(llegeix(repo_prova, "content/ca/elements/mixta.md"))["arquitectes"] == [
        "Pere López Íñigo", "Pere López Núñez", "Arriola & Fiol Arquitectes"]
    # subcadena: «Pere López Íñigo» no es toca enlloc
    assert fm(llegeix(repo_prova, "content/ca/elements/biblioteca-vall-d-hebron.md"))["arquitectes"] == ["Pere López Íñigo"]
    assert sorted(r.pla.actualitzats) == ["content/ca/elements/casa-bloc.md", "content/ca/elements/lestel-ferit.md",
                                          "content/ca/elements/mixta.md"]
    # carpeta moguda, alias afegida, títol nou
    assert not (repo_prova / "content/ca/arquitectes/pere-lópez").exists()
    idx = llegeix(repo_prova, "content/ca/arquitectes/pere-lópez-núñez/_index.md")
    assert fm(idx)["title"] == "Pere López Núñez"
    assert fm(idx)["aliases"] == ["/arquitectes/pere-lópez/"]
    # la prosa de la descripció no es toca (queda comptada)
    assert "Pere López Íñigo hi va col·laborar" in llegeix(repo_prova, "content/ca/elements/casa-bloc.md")


def test_renom_arquitecte_amb_ampersand_i_terme_bio(repo_prova):
    ev = sveltia_canvia_arq(repo_prova, "arriola--fiol-arquitectes", "Arriola & Fiol & Co")
    r = renom.aplica_renom_arquitecte(repo_prova, ev)
    assert r.estat == "aplicat", r.motiu
    assert r.url_nova == "/arquitectes/arriola--fiol--co/"   # carpeta que dona Hugo (taula validada a test_slugs)
    assert (repo_prova / "content/ca/arquitectes/arriola--fiol--co/_index.md").exists()
    assert yaml.safe_load(llegeix(repo_prova, "data/arquitectes-bio-extra.yaml"))[0]["terme"] == "Arriola & Fiol & Co"
    t = llegeix(repo_prova, "content/ca/elements/torre-llevant.md")
    assert fm(t)["arquitectes"][0] == "Arriola & Fiol & Co" and '  - "Arriola & Fiol & Co"\n' in t
    # l'alias que ja tenia es conserva; s'afegeix la carpeta antiga
    idx = fm(llegeix(repo_prova, "content/ca/arquitectes/arriola--fiol--co/_index.md"))
    assert idx["aliases"] == ["/arquitectes/arriola-fiol-arquitectes/", "/arquitectes/arriola--fiol-arquitectes/"]


def test_renom_arquitecte_carpeta_preexistent_discordant_dona_dues_alias(repo_prova):
    # carpeta `pere-lópez-i-íñigo` però urlize(títol) = `pere-lópez-íñigo`
    ev = sveltia_canvia_arq(repo_prova, "pere-lópez-i-íñigo", "Pere López Íñigo Estudi")
    r = renom.aplica_renom_arquitecte(repo_prova, ev)
    assert r.estat == "aplicat", r.motiu
    idx = fm(llegeix(repo_prova, "content/ca/arquitectes/pere-lópez-íñigo-estudi/_index.md"))
    assert idx["aliases"] == ["/vell/pere-lopez-inigo/", "/arquitectes/pere-lópez-i-íñigo/", "/arquitectes/pere-lópez-íñigo/"]


def _refus(repo, carpeta, nou, contingut):
    ev = sveltia_canvia_arq(repo, carpeta, nou)
    abans = git(repo, "rev-parse", "HEAD^{tree}")
    r = renom.aplica_renom_arquitecte(repo, ev)
    assert r.estat == "refusat" and contingut in r.motiu, (r.estat, r.motiu)
    assert git(repo, "status", "--porcelain") == ""       # cap fitxa modificada
    assert git(repo, "rev-parse", "HEAD^{tree}") == abans


def test_colisio_amb_arquitecte_existent_per_nom(repo_prova):
    _refus(repo_prova, "rebecca-horn", "Pere López", "ja existeix un arquitecte")


def test_colisio_amb_carpeta_existent(repo_prova):
    _refus(repo_prova, "rebecca-horn", "pere lópez", "ja existeix l'arquitecte amb l'adreça")


def test_colisio_amb_nom_sense_carpeta(repo_prova):
    _refus(repo_prova, "rebecca-horn", "Sense Carpeta Uno", "sense fitxa pròpia")


def test_colisio_amb_adreca_d_un_altre_terme_sense_carpeta(repo_prova):
    # «sense carpeta uno» (minúscules) dóna la mateixa adreça que el terme «Sense Carpeta Uno»
    _refus(repo_prova, "rebecca-horn", "sense carpeta uno", "coincideix amb la del terme")


def test_nom_amb_barra_es_refusa(repo_prova):
    _refus(repo_prova, "rebecca-horn", "Horn/Associats", "no dóna una adreça vàlida")


def test_colisio_amb_alias_d_una_altra_entrada(repo_prova):
    # l'adreça nova és una redirecció de pere-lópez-i-íñigo
    _refus(repo_prova, "rebecca-horn", "Arriola Fiol Arquitectes", "redirecció")


def test_renom_arquitecte_dues_vegades_el_nom_en_una_fitxa(repo_prova):
    ev = sveltia_canvia_arq(repo_prova, "rebecca-horn", "Rebecca Horn Estudi")
    r = renom.aplica_renom_arquitecte(repo_prova, ev)
    d = fm(llegeix(repo_prova, "content/ca/elements/lestel-ferit.md"))
    assert d["arquitectes"][0] == "Rebecca Horn Estudi"
    assert d["intervencions"][0]["autors"][0] == "Rebecca Horn Estudi"
    assert r.estat == "aplicat"
