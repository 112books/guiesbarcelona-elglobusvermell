import difflib

import pytest
import yaml

import renom


def fm(text):
    return yaml.safe_load(text.split("---\n")[1])


def es_subsequencia(original, nou):
    """Cap línia original no s'ha esborrat ni reordenat."""
    it = iter(nou.splitlines())
    return all(any(l == n for n in it) for l in original.splitlines())


INLINE = '---\naliases: ["/elements/a/"]\ntitle: X\n---\ncos\n'
BLOC = '---\naliases:\n  - /elements/a/\n  - /wp/b/\narquitectes:\n- Nom\ntitle: X\n---\ncos\n'
SENSE = '---\narquitectes:\n- Nom\ntitle: X\n---\ncos\n'


def test_alias_inline():
    r = renom.afegeix_alias(INLINE, "/elements/b/")
    assert 'aliases: ["/elements/a/", "/elements/b/"]\n' in r
    assert fm(r)["aliases"] == ["/elements/a/", "/elements/b/"]
    assert es_subsequencia(INLINE.replace('["/elements/a/"]', '["/elements/a/", "/elements/b/"]'), r)


def test_alias_inline_buit():
    r = renom.afegeix_alias('---\naliases: []\ntitle: X\n---\n', "/elements/b/")
    assert fm(r)["aliases"] == ["/elements/b/"]


def test_alias_bloc_nomes_afegeix_una_linia():
    r = renom.afegeix_alias(BLOC, "/elements/b/")
    assert fm(r)["aliases"] == ["/elements/a/", "/wp/b/", "/elements/b/"]
    diff = [l for l in difflib.unified_diff(BLOC.splitlines(), r.splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    assert diff == ["+  - /elements/b/"]


def test_alias_bloc_indentacio_zero_i_cometes():
    t = '---\naliases:\n- "/a/"\ntitle: X\n---\n'
    r = renom.afegeix_alias(t, "/b/")
    assert '- "/a/"\n- "/b/"\n' in r


def test_alias_sense_aliases_sota_el_primer_guio():
    r = renom.afegeix_alias(SENSE, "/elements/b/")
    assert r.startswith('---\naliases: ["/elements/b/"]\narquitectes:')
    assert fm(r)["aliases"] == ["/elements/b/"]
    assert es_subsequencia(SENSE, r)


@pytest.mark.parametrize("t", [INLINE, BLOC, SENSE])
def test_alias_idempotent_i_sense_esborrar(t):
    una = renom.afegeix_alias(t, "/elements/z/")
    dues = renom.afegeix_alias(una, "/elements/z/")
    assert una == dues
    assert es_subsequencia(t.replace('["/elements/a/"]', '["/elements/a/", "/elements/z/"]'), una) or es_subsequencia(t, una)


def test_alias_ja_existent_no_canvia():
    assert renom.afegeix_alias(INLINE, "/elements/a/") == INLINE
    assert renom.afegeix_alias(BLOC, "/wp/b/") == BLOC


def test_alias_autoreferencia_no_s_afegeix():
    assert renom.afegeix_alias(INLINE, "/elements/n/", canonica="/elements/n/") == INLINE


def test_alias_amb_caracters_especials_es_conserva_valid():
    r = renom.afegeix_alias(BLOC, "/arquitectes/a&eb/")
    assert fm(r)["aliases"][-1] == "/arquitectes/a&eb/"
    r = renom.afegeix_alias(INLINE, "/arquitectes/lópez-i-íñigo/")
    assert fm(r)["aliases"][-1] == "/arquitectes/lópez-i-íñigo/"


def test_llegeix_aliases():
    assert renom.llegeix_aliases(INLINE) == ["/elements/a/"]
    assert renom.llegeix_aliases(BLOC) == ["/elements/a/", "/wp/b/"]
    assert renom.llegeix_aliases(SENSE) == []
    assert renom.llegeix_aliases("---\naliases: ['/a/', \"/b/\", /c/]\n---\n") == ["/a/", "/b/", "/c/"]


def test_treu_alias_nomes_l_exacta():
    r = renom.treu_alias(BLOC, "/elements/a/")
    assert fm(r)["aliases"] == ["/wp/b/"]
    r = renom.treu_alias('---\naliases: ["/a/", "/b/", "/c/"]\n---\n', "/b/")
    assert fm(r)["aliases"] == ["/a/", "/c/"]
    assert renom.treu_alias(BLOC, "/inexistent/") == BLOC


# ---------------- aplica_renom_fitxa (Tasca 7) ----------------

from conftest import canvia_titol, commit_sveltia, git  # noqa: E402


def sveltia_canvia(repo, stem, nou_titol, tipus="Edifici"):
    base = git(repo, "rev-parse", "HEAD")
    canvia_titol(repo, f"content/ca/elements/{stem}.md", nou_titol)
    commit_sveltia(repo, tipus, stem)
    return renom.detecta_renoms(repo, base, "HEAD")[0]


def estat(repo):
    return git(repo, "status", "--porcelain").splitlines()


def test_renom_fitxa_simple(repo_prova):
    ev = sveltia_canvia(repo_prova, "torre-llevant", "Torre del Llevant")
    r = renom.aplica_renom_fitxa(repo_prova, ev)
    assert r.estat == "aplicat"
    assert (r.url_antiga, r.url_nova) == ("/elements/torre-llevant/", "/elements/torre-del-llevant/")
    assert not (repo_prova / "content/ca/elements/torre-llevant.md").exists()
    t = (repo_prova / "content/ca/elements/torre-del-llevant.md").read_text(encoding="utf-8")
    # aliases en bloc: antigues intactes + la nova a l'últim lloc
    assert fm(t)["aliases"] == ["/barris/torre-llevant/", "/torre-llevant-antic/", "/elements/torre-llevant/"]
    assert fm(t)["title"] == "Torre del Llevant"
    # git status: només el canvi esperat (renom + modificació de l'alias)
    assert len(estat(repo_prova)) == 1 and estat(repo_prova)[0].startswith("R")


def test_renom_fitxa_aliases_inline_existent(repo_prova):
    ev = sveltia_canvia(repo_prova, "casa-bloc", "Casa Bloc de Sant Andreu")
    r = renom.aplica_renom_fitxa(repo_prova, ev)
    t = (repo_prova / "content/ca/elements/casa-bloc-de-sant-andreu.md").read_text(encoding="utf-8")
    assert fm(t)["aliases"] == ["/avantguarda-1928-1938/casa-bloc/", "/elements/casa-bloc/"]
    assert r.estat == "aplicat"


def test_renom_fitxa_sense_aliases(repo_prova):
    ev = sveltia_canvia(repo_prova, "mixta", "Mixta Nova")
    renom.aplica_renom_fitxa(repo_prova, ev)
    t = (repo_prova / "content/ca/elements/mixta-nova.md").read_text(encoding="utf-8")
    assert t.startswith('---\naliases: ["/elements/mixta/"]\n')


def test_renom_fitxa_excepcio_preexistent(repo_prova):
    ev = sveltia_canvia(repo_prova, "biblioteca-vall-d-hebron", "Biblioteca Vall d'Hebron Nova")
    r = renom.aplica_renom_fitxa(repo_prova, ev)
    assert r.estat == "aplicat"
    t = (repo_prova / "content/ca/elements/biblioteca-vall-dhebron-nova.md").read_text(encoding="utf-8")
    assert "/elements/biblioteca-vall-d-hebron/" in fm(t)["aliases"]
    assert "/biblioteques/vall-d-hebron/" in fm(t)["aliases"]


def test_renom_fitxa_actualitza_enllac_intern(repo_prova):
    ev = sveltia_canvia(repo_prova, "casa-bloc", "Casa Bloc Nova")
    r = renom.aplica_renom_fitxa(repo_prova, ev)
    mapa = (repo_prova / "content/ca/mapa/_index.md").read_text(encoding="utf-8")
    assert "(/elements/casa-bloc-nova/)" in mapa
    # l'`aliases` del mapa (adreces antigues) no es toca
    assert 'aliases: ["/elements/", "/mapa-grisos/"]' in mapa
    assert "content/ca/mapa/_index.md" in r.pla.enllaços


def test_renom_fitxa_sense_canvi_d_adreca(repo_prova):
    ev = sveltia_canvia(repo_prova, "casa-bloc", "CASA BLOC")
    r = renom.aplica_renom_fitxa(repo_prova, ev)
    assert r.estat == "sense-canvi"
    assert (repo_prova / "content/ca/elements/casa-bloc.md").exists()


def test_renom_fitxa_colisio_agafa_l_adreca(repo_prova):
    """Dues fitxes poden dur el mateix títol (Xavi, 19/11): la segona agafa el carrer."""
    ev = sveltia_canvia(repo_prova, "casa-bloc", "Mixta")
    r = renom.aplica_renom_fitxa(repo_prova, ev)
    assert r.estat == "aplicat", r.motiu
    nou = "content/ca/elements/mixta-passeig-de-torras-i-bages.md"
    assert (repo_prova / nou).exists()
    assert not (repo_prova / "content/ca/elements/casa-bloc.md").exists()
    # la fitxa «mixta» que ja hi havia no s'ha tocat
    assert (repo_prova / "content/ca/elements/mixta.md").exists()
    assert renom.llegeix_titol((repo_prova / nou).read_text(encoding="utf-8")) == "Mixta"


def test_renom_fitxa_no_esborra_cap_linia_original(repo_prova):
    original = (repo_prova / "content/ca/elements/torre-llevant.md").read_text(encoding="utf-8")
    ev = sveltia_canvia(repo_prova, "torre-llevant", "Torre del Llevant")
    renom.aplica_renom_fitxa(repo_prova, ev)
    nou = (repo_prova / "content/ca/elements/torre-del-llevant.md").read_text(encoding="utf-8")
    sense_titol = [l for l in original.splitlines() if not l.startswith("title:")]
    assert es_subsequencia("\n".join(sense_titol), nou)
