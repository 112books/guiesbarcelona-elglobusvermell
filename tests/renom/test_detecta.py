import renom
from conftest import canvia_titol, commit, commit_sveltia, git, escriu

CAMI_BLOC = "content/ca/elements/casa-bloc.md"
CAMI_SERT = "content/ca/arquitectes/josep-lluís-sert/_index.md"


def base(repo):
    return git(repo, "rev-parse", "HEAD")


def test_sveltia_canvia_titol_fitxa(repo_prova):
    b = base(repo_prova)
    canvia_titol(repo_prova, CAMI_BLOC, "Casa Bloc Nova")
    sha = commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    ev = renom.detecta_renoms(repo_prova, b, "HEAD")
    assert len(ev) == 1
    e = ev[0]
    assert (e.tipus, e.commit, e.titol_antic, e.titol_nou) == ("fitxa", sha, "Casa Bloc", "Casa Bloc Nova")
    assert e.path_antic == CAMI_BLOC
    assert e.path_nou == "content/ca/elements/casa-bloc-nova.md"
    assert e.autor.startswith("xaviglobus")


def test_sveltia_canvia_titol_arquitecte(repo_prova):
    b = base(repo_prova)
    canvia_titol(repo_prova, CAMI_SERT, "Josep Lluís Sert i López")
    commit_sveltia(repo_prova, "Arquitecte", "josep-lluís-sert")
    ev = renom.detecta_renoms(repo_prova, b, "HEAD")
    assert [(e.tipus, e.titol_antic, e.titol_nou) for e in ev] == [
        ("arquitecte", "Josep Lluís Sert", "Josep Lluís Sert i López")]
    assert ev[0].path_nou == "content/ca/arquitectes/josep-lluís-sert-i-lópez/_index.md"


def test_commit_huma_no_dispara(repo_prova):
    b = base(repo_prova)
    canvia_titol(repo_prova, CAMI_BLOC, "Casa Bloc Nova")
    commit(repo_prova, "content(descripcions): retoca títols", autor=("Joan Mz Linux", "joan@example.org"))
    assert renom.detecta_renoms(repo_prova, b, "HEAD") == []


def test_opt_out_sense_renom(repo_prova):
    b = base(repo_prova)
    canvia_titol(repo_prova, CAMI_BLOC, "Casa Bloc Nova")
    commit_sveltia(repo_prova, "Edifici", "casa-bloc", extra="\n\nNomés correcció tipogràfica [sense-renom]")
    assert renom.detecta_renoms(repo_prova, b, "HEAD") == []


def test_commit_de_bot_no_dispara(repo_prova):
    b = base(repo_prova)
    canvia_titol(repo_prova, CAMI_BLOC, "Casa Bloc Nova")
    commit(repo_prova, "Update Edifici “casa-bloc”",
           autor=("github-actions[bot]", "41898282+github-actions[bot]@users.noreply.github.com"))
    assert renom.detecta_renoms(repo_prova, b, "HEAD") == []


def test_sveltia_sense_tocar_title(repo_prova):
    b = base(repo_prova)
    p = repo_prova / CAMI_BLOC
    p.write_text(p.read_text(encoding="utf-8").replace("Casa Bloc\n", "Casa Bloc\ntemes: [a]\n"), encoding="utf-8")
    p.write_text(p.read_text(encoding="utf-8").replace("Passeig de Torras", "Passeig de Torres"), encoding="utf-8")
    commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    assert renom.detecta_renoms(repo_prova, b, "HEAD") == []


def test_dos_commits_a_b_c_en_ordre(repo_prova):
    b = base(repo_prova)
    canvia_titol(repo_prova, CAMI_BLOC, "Casa B")
    s1 = commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    canvia_titol(repo_prova, CAMI_BLOC, "Casa C")
    s2 = commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    ev = renom.detecta_renoms(repo_prova, b, "HEAD")
    assert [(e.commit, e.titol_antic, e.titol_nou) for e in ev] == [(s1, "Casa Bloc", "Casa B"), (s2, "Casa B", "Casa C")]


def test_excepcio_preexistent_usa_el_nom_real_de_fitxer(repo_prova):
    b = base(repo_prova)
    cami = "content/ca/elements/biblioteca-vall-d-hebron.md"
    canvia_titol(repo_prova, cami, "Biblioteca Vall d'Hebron Nova")
    commit_sveltia(repo_prova, "Edifici", "biblioteca-vall-d-hebron")
    ev = renom.detecta_renoms(repo_prova, b, "HEAD")
    assert len(ev) == 1 and ev[0].path_antic == cami
    assert ev[0].path_nou == "content/ca/elements/biblioteca-vall-dhebron-nova.md"


def test_fitxer_nou_o_esborrat_no_es_renom(repo_prova):
    b = base(repo_prova)
    escriu(repo_prova, "content/ca/elements/nova.md", "---\ntitle: Nova\n---\n")
    commit_sveltia(repo_prova, "Edifici", "nova")
    (repo_prova / "content/ca/elements/mixta.md").unlink()
    commit_sveltia(repo_prova, "Edifici", "mixta")
    assert renom.detecta_renoms(repo_prova, b, "HEAD") == []


def test_es_commit_sveltia_unitari():
    assert renom.es_commit_sveltia("Update Edifici “casa-bloc”", "xaviglobus <x@y>")
    assert renom.es_commit_sveltia("Update Arquitecte “a-b”", "xaviglobus <x@y>")
    assert not renom.es_commit_sveltia("Create Edifici “casa-bloc”", "xaviglobus <x@y>")
    assert not renom.es_commit_sveltia("Update Plànol-guia “gatcpac”", "xaviglobus <x@y>")
    assert not renom.es_commit_sveltia("content: Update Edifici “x”", "Joan <j@y>")


def test_base_desconeguda_usa_head_menys_20(repo_prova):
    for i in range(22):
        escriu(repo_prova, f"extra/{i}.txt", str(i))
        commit(repo_prova, f"extra {i}")
    canvia_titol(repo_prova, CAMI_BLOC, "Casa Bloc Nova")
    commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    assert len(renom.detecta_renoms(repo_prova, "0" * 40, "HEAD")) == 1
    assert len(renom.detecta_renoms(repo_prova, "", "HEAD")) == 1
