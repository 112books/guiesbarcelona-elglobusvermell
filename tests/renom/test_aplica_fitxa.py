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
