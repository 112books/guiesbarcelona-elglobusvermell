import pytest
import yaml

import renom
from conftest import canvia_titol, commit, commit_sveltia, escriu, git


def esdeveniment(repo, camí, nou, tipus):
    base = git(repo, "rev-parse", "HEAD")
    canvia_titol(repo, camí, nou)
    commit_sveltia(repo, tipus, camí.split("/")[-1])
    return renom.detecta_renoms(repo, base, "HEAD")[0]


def titol_de(repo, camí):
    return renom.llegeix_titol((repo / camí).read_text(encoding="utf-8"))


def test_colisio_d_arquitecte_reverteix_el_titol_i_no_toca_fitxes(repo_prova):
    camí = "content/ca/arquitectes/rebecca-horn/_index.md"
    ev = esdeveniment(repo_prova, camí, "Pere López", "Arquitecte")
    r = renom.aplica_esdeveniment(repo_prova, ev)
    assert r.estat == "refusat" and "ja existeix" in r.motiu
    assert titol_de(repo_prova, camí) == "Rebecca Horn"          # revertit
    # l'únic canvi a l'arbre és la línia title (tornada al valor de HEAD~1)
    assert git(repo_prova, "diff", "HEAD~1", "--stat", "--", "content/ca/elements", "data") == ""
    assert git(repo_prova, "diff", "HEAD~1", "--", ".") == ""
    assert (repo_prova / "content/ca/arquitectes/rebecca-horn").exists()


def test_colisio_de_fitxa_agafa_l_adreca_i_no_reverteix_el_titol(repo_prova):
    """El títol repetit ja no es refusa: la fitxa nova agafa el carrer (Xavi, 19/11)."""
    camí = "content/ca/elements/casa-bloc.md"
    ev = esdeveniment(repo_prova, camí, "Mixta", "Edifici")
    r = renom.aplica_esdeveniment(repo_prova, ev)
    assert r.estat == "aplicat", r.motiu
    nou = "content/ca/elements/mixta-passeig-de-torras-i-bages.md"
    assert (repo_prova / nou).exists() and (repo_prova / "content/ca/elements/mixta.md").exists()
    assert titol_de(repo_prova, nou) == "Mixta"
    assert (r.url_antiga, r.url_nova) == ("/elements/casa-bloc/", "/elements/mixta-passeig-de-torras-i-bages/")


def test_renom_amb_colisio_conserva_la_resta_del_commit(repo_prova):
    camí = "content/ca/elements/casa-bloc.md"
    base = git(repo_prova, "rev-parse", "HEAD")
    # el commit de Sveltia també canvia una altra cosa: l'adreça
    p = repo_prova / camí
    p.write_text(p.read_text(encoding="utf-8").replace("title: Casa Bloc", "title: Mixta")
                 .replace("Passeig de Torras", "Passeig Nou"), encoding="utf-8")
    commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    ev = renom.detecta_renoms(repo_prova, base, "HEAD")[0]
    renom.aplica_esdeveniment(repo_prova, ev)
    # l'adreça ja era la nova quan s'ha fet el renom: el sufix surt d'«Passeig Nou»
    t = (repo_prova / "content/ca/elements/mixta-passeig-nou-i-bages.md").read_text(encoding="utf-8")
    assert "title: Mixta\n" in t and "Passeig Nou" in t      # la resta del commit queda intacta


def test_error_a_mig_de_l_escriptura_deixa_l_arbre_com_abans(repo_prova, monkeypatch):
    ev = esdeveniment(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez", "Arquitecte")
    original = renom.git
    cridades = {"add": 0}

    def git_que_falla(repo, *args, **kw):
        if args and args[0] == "add":
            cridades["add"] += 1
            if cridades["add"] == 2:
                raise renom.ErrorGit("fallada simulada")
        return original(repo, *args, **kw)

    monkeypatch.setattr(renom, "git", git_que_falla)
    r = renom.aplica_esdeveniment(repo_prova, ev)
    monkeypatch.setattr(renom, "git", original)
    assert r.estat == "refusat" and "error inesperat" in r.motiu
    assert cridades["add"] >= 2
    # L'arbre torna a l'estat d'abans de l'aplicació (HEAD) i, després del revert del títol
    # (únic canvi), és idèntic al de l'estat previ al desament de l'editor.
    assert git(repo_prova, "diff", "HEAD~1", "--", ".") == ""
    assert git(repo_prova, "status", "--porcelain").count("\n") == 0
    assert git(repo_prova, "status", "--porcelain").strip().startswith("M")   # només la línia title
    assert (repo_prova / "content/ca/arquitectes/pere-lópez/_index.md").exists()
    assert not (repo_prova / "content/ca/arquitectes/pere-lópez-núñez").exists()


# ---------------- Tasca 15a: A -> B -> A i alias que coincideix amb l'adreça nova ----------------

def fm(text):
    return yaml.safe_load(text.split("---\n")[1])


def test_anada_i_tornada_treu_nomes_l_alias_autoreferent(repo_prova):
    p0 = "content/ca/elements/torre-llevant.md"
    ev1 = esdeveniment(repo_prova, p0, "Torre del Llevant", "Edifici")
    mapa = {}
    r1 = renom.aplica_esdeveniment(repo_prova, ev1, mapa)
    assert r1.estat == "aplicat"
    git(repo_prova, "-c", "user.name=bot", "-c", "user.email=b@x", "commit", "-q", "-m", "auto")
    # Xavi torna al nom original (la fitxa ja és a torre-del-llevant.md)
    p1 = "content/ca/elements/torre-del-llevant.md"
    base = git(repo_prova, "rev-parse", "HEAD")
    canvia_titol(repo_prova, p1, "Torre Llevant")
    commit_sveltia(repo_prova, "Edifici", "torre-del-llevant")
    ev2 = renom.detecta_renoms(repo_prova, base, "HEAD")[0]
    r2 = renom.aplica_esdeveniment(repo_prova, ev2)
    assert r2.estat == "aplicat", r2.motiu
    t = (repo_prova / p0).read_text(encoding="utf-8")
    # s'ha tret NOMÉS /elements/torre-llevant/ (l'adreça actual); les del WordPress i la del pas 1 es conserven
    assert fm(t)["aliases"] == ["/barris/torre-llevant/", "/torre-llevant-antic/", "/elements/torre-del-llevant/"]
    assert r2.alies_eliminats == ["/elements/torre-llevant/"]


def test_slug_nou_igual_a_alias_wordpress_de_la_mateixa_fitxa(repo_prova):
    p0 = "content/ca/elements/torre-llevant.md"
    ev = esdeveniment(repo_prova, p0, "Torre Llevant Antic", "Edifici")   # slug = torre-llevant-antic
    # alias existent de la mateixa fitxa: /torre-llevant-antic/ no és /elements/..., així que
    # provem amb una alias exactament igual a la nova adreça
    t = (repo_prova / p0).read_text(encoding="utf-8")
    (repo_prova / p0).write_text(renom.afegeix_alias(t, "/elements/torre-llevant-antic/"), encoding="utf-8")
    git(repo_prova, "commit", "-qam", "afegeix alias WP simulat")
    r = renom.aplica_esdeveniment(repo_prova, ev)
    assert r.estat == "aplicat", r.motiu
    nou = (repo_prova / "content/ca/elements/torre-llevant-antic.md").read_text(encoding="utf-8")
    assert "/elements/torre-llevant-antic/" not in fm(nou)["aliases"]
    assert "/elements/torre-llevant/" in fm(nou)["aliases"]
    assert "/barris/torre-llevant/" in fm(nou)["aliases"]
    assert r.alies_eliminats == ["/elements/torre-llevant-antic/"]


def test_slug_nou_igual_a_alias_d_una_altra_fitxa_es_refusa(repo_prova):
    p = "content/ca/elements/mixta.md"
    t = (repo_prova / p).read_text(encoding="utf-8")
    (repo_prova / p).write_text(renom.afegeix_alias(t, "/elements/casa-bloc-nova/"), encoding="utf-8")
    git(repo_prova, "commit", "-qam", "alias d'una altra fitxa")
    ev = esdeveniment(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova", "Edifici")
    r = renom.aplica_esdeveniment(repo_prova, ev)
    assert r.estat == "refusat" and "redirecció" in r.motiu
    assert titol_de(repo_prova, "content/ca/elements/casa-bloc.md") == "Casa Bloc"


# ---------------- Tasca 15b: pestanya antiga que recrea l'arxiu vell ----------------

def test_sense_conflictes_a_l_estat_inicial(repo_prova):
    assert renom.detecta_conflictes(repo_prova) == []


def test_recreacio_de_l_arxiu_vell_es_detecta(repo_prova):
    ev = esdeveniment(repo_prova, "content/ca/elements/mixta.md", "Mixta Nova", "Edifici")
    renom.aplica_esdeveniment(repo_prova, ev)
    git(repo_prova, "-c", "user.name=bot", "-c", "user.email=b@x", "commit", "-q", "-m", "auto")
    # una pestanya antiga desa l'arxiu vell
    escriu(repo_prova, "content/ca/elements/mixta.md", "---\ntitle: Mixta\n---\n")
    commit_sveltia(repo_prova, "Edifici", "mixta")
    c = renom.detecta_conflictes(repo_prova)
    assert len(c) == 1 and "/elements/mixta/" in c[0] and "mixta-nova.md" in c[0]
    # no s'ha esborrat ni mogut res
    assert (repo_prova / "content/ca/elements/mixta.md").exists()
    assert (repo_prova / "content/ca/elements/mixta-nova.md").exists()


def test_dos_arquitectes_amb_el_mateix_nom_es_detecta(repo_prova):
    escriu(repo_prova, "content/ca/arquitectes/pere-lopez-bis/_index.md", "---\ntitle: Pere López\n---\n")
    c = renom.detecta_conflictes(repo_prova)
    assert len(c) == 1 and "dos arquitectes amb el mateix nom" in c[0]
