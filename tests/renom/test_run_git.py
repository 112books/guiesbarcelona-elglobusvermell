import json
import subprocess

import pytest

import renom
from conftest import canvia_titol, commit, commit_sveltia, escriu, git


def clona(remot, destí):
    subprocess.run(["git", "clone", "-q", str(remot), str(destí)], check=True)
    return destí


def log_auto(remot):
    return [l for l in git(remot, "log", "--format=%an|%s").splitlines() if "auto:" in l]


def xavi_canvia(repo, camí, nou, tipus, slug):
    canvia_titol(repo, camí, nou)
    sha = commit_sveltia(repo, tipus, slug)
    git(repo, "push", "-q", "origin", "main")
    return sha


def test_renom_d_arquitecte_arriba_al_remot(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    xavi_canvia(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez", "Arquitecte", "pere-lópez")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, base, "HEAD", avisos_json=tmp_path / "avisos.json") == 0
    # el remot té exactament un commit del robot
    auto = log_auto(remot_bare)
    assert auto == ["github-actions[bot]|auto: renom arquitecte «Pere López» → «Pere López Núñez» (3 fitxes)"]
    # arbre coherent: cap `arquitectes:` amb el nom antic
    final = clona(remot_bare, tmp_path / "final")
    assert git(final, "grep", "-l", "-E", "^\\s*-\\s+['\"]?Pere López['\"]?\\s*$", "--", "content", "data", check=False) == ""
    assert (final / "content/ca/arquitectes/pere-lópez-núñez/_index.md").exists()
    assert "commit `" in (final / ".ai/REGISTRE-CANVIS-FITXES.md").read_text(encoding="utf-8")
    avisos = json.loads((tmp_path / "avisos.json").read_text(encoding="utf-8"))
    assert len(avisos) == 1 and "Pere López Núñez" in avisos[0]["assumpte"]


def test_segona_execucio_es_no_op(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    xavi_canvia(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova", "Edifici", "casa-bloc")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, base, "HEAD") == 0
    cap1 = git(remot_bare, "rev-parse", "main")
    # nova execució (p. ex. un workflow_dispatch) sobre el mateix rang, ara des de l'estat final
    robot2 = clona(remot_bare, tmp_path / "robot2")
    assert renom.executa_flux(robot2, base, "HEAD") == 0
    assert git(remot_bare, "rev-parse", "main") == cap1
    assert len(log_auto(remot_bare)) == 1


def test_base_no_disponible_usa_head_20_i_la_idempotencia(tmp_path, repo_prova, remot_bare):
    xavi_canvia(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova", "Edifici", "casa-bloc")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, "0" * 40, "HEAD") == 0
    assert len(log_auto(remot_bare)) == 1
    robot2 = clona(remot_bare, tmp_path / "robot2")
    assert renom.executa_flux(robot2, "", "HEAD") == 0
    assert len(log_auto(remot_bare)) == 1


def test_un_commit_per_esdeveniment_dos_renoms_al_mateix_push(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    canvia_titol(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova")
    commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    canvia_titol(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez")
    commit_sveltia(repo_prova, "Arquitecte", "pere-lópez")
    git(repo_prova, "push", "-q", "origin", "main")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, base, "HEAD") == 0
    assert len(log_auto(remot_bare)) == 2
    final = clona(remot_bare, tmp_path / "final")
    assert (final / "content/ca/elements/casa-bloc-nova.md").exists()
    assert (final / "content/ca/arquitectes/pere-lópez-núñez").exists()
    # i el nom d'arquitecte s'ha propagat també a la fitxa que s'acabava de moure
    t = (final / "content/ca/elements/casa-bloc-nova.md").read_text(encoding="utf-8")
    assert "- Pere López Núñez\n" in t


def test_a_b_c_a_la_mateixa_passada(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    canvia_titol(repo_prova, "content/ca/elements/mixta.md", "Mixta B")
    commit_sveltia(repo_prova, "Edifici", "mixta")
    canvia_titol(repo_prova, "content/ca/elements/mixta.md", "Mixta C")
    commit_sveltia(repo_prova, "Edifici", "mixta")
    git(repo_prova, "push", "-q", "origin", "main")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, base, "HEAD") == 0
    final = clona(remot_bare, tmp_path / "final")
    assert not (final / "content/ca/elements/mixta.md").exists()
    t = (final / "content/ca/elements/mixta-c.md").read_text(encoding="utf-8")
    assert t.startswith('---\naliases: ["/elements/mixta/", "/elements/mixta-b/"]\n')
    assert len(log_auto(remot_bare)) == 2


def test_concurrencia_xavi_puja_just_abans_del_push_del_robot(tmp_path, repo_prova, remot_bare, monkeypatch):
    base = git(repo_prova, "rev-parse", "HEAD")
    xavi_canvia(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez", "Arquitecte", "pere-lópez")
    robot = clona(remot_bare, tmp_path / "robot")
    original = renom._passada
    cridades = []

    def passada_i_xavi_puja(*a, **k):
        res = original(*a, **k)
        cridades.append(1)
        if len(cridades) == 1:
            # just abans del push del robot, en Xavi canvia un altre títol i el puja
            xavi_canvia(repo_prova, "content/ca/elements/mixta.md", "Mixta Nova", "Edifici", "mixta")
        return res

    monkeypatch.setattr(renom, "_passada", passada_i_xavi_puja)
    assert renom.executa_flux(robot, base, "HEAD") == 0
    assert len(cridades) == 2                       # el primer push s'ha rebutjat i s'ha recalculat
    auto = log_auto(remot_bare)
    assert len(auto) == 2                            # un commit del robot per esdeveniment, sense duplicats
    final = clona(remot_bare, tmp_path / "final")
    assert (final / "content/ca/elements/mixta-nova.md").exists()        # el canvi d'en Xavi, renombrat a la 2a passada
    assert (final / "content/ca/arquitectes/pere-lópez-núñez").exists()
    log = git(remot_bare, "log", "--format=%an|%s")
    assert "xaviglobus|Update Edifici “mixta”" in log                      # el seu commit es conserva
    assert git(remot_bare, "rev-list", "--merges", "--count", "main") == "0"  # historial lineal


def test_commit_de_joan_no_dispara_el_renom(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    canvia_titol(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova")
    commit(repo_prova, "content(descripcions): retoca títols")
    git(repo_prova, "push", "-q", "origin", "main")
    robot = clona(remot_bare, tmp_path / "robot")
    cap = git(remot_bare, "rev-parse", "main")
    assert renom.executa_flux(robot, base, "HEAD") == 0
    assert git(remot_bare, "rev-parse", "main") == cap


def test_conflicte_surt_amb_error_sense_tocar_el_contingut(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    xavi_canvia(repo_prova, "content/ca/elements/mixta.md", "Mixta Nova", "Edifici", "mixta")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, base, "HEAD") == 0       # el robot mou mixta -> mixta-nova
    # una pestanya antiga recrea mixta.md (Xavi puja)
    xavi_clon = clona(remot_bare, tmp_path / "xavi2")
    git(xavi_clon, "config", "user.name", "x")
    escriu(xavi_clon, "content/ca/elements/mixta.md", "---\ntitle: Mixta\n---\n")
    commit_sveltia(xavi_clon, "Edifici", "mixta")
    git(xavi_clon, "push", "-q", "origin", "main")
    robot2 = clona(remot_bare, tmp_path / "robot2")
    contingut_abans = git(robot2, "rev-parse", "HEAD:content")
    codi = renom.executa_flux(robot2, git(robot2, "rev-parse", "HEAD~1"), "HEAD", avisos_json=tmp_path / "av.json")
    assert codi == 1
    assert git(robot2, "rev-parse", "HEAD:content") == contingut_abans        # cap canvi de contingut
    assert (robot2 / "content/ca/elements/mixta.md").exists() and (robot2 / "content/ca/elements/mixta-nova.md").exists()
    avisos = json.loads((tmp_path / "av.json").read_text(encoding="utf-8"))
    assert len(avisos) == 1 and "Atenció" in avisos[0]["assumpte"]
    assert "conflicte detectat" in (robot2 / ".ai/REGISTRE-CANVIS-FITXES.md").read_text(encoding="utf-8")


def test_cli_run_no_push_i_envia_avisos_no_enviar(tmp_path, repo_prova):
    import sys
    base = git(repo_prova, "rev-parse", "HEAD")
    canvia_titol(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova")
    commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    av = tmp_path / "avisos.json"
    r = subprocess.run([sys.executable, str(renom.__file__), "run", "--repo", str(repo_prova), "--base", base,
                        "--no-push", "--avisos-json", str(av)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert (repo_prova / "content/ca/elements/casa-bloc-nova.md").exists()
    r = subprocess.run([sys.executable, str(renom.__file__), "envia-avisos", str(av), "--no-enviar",
                        "--sortida", str(tmp_path / "cossos")], capture_output=True, text=True)
    assert r.returncode == 0
    assert "https://112books.github.io/guiesbarcelona-elglobusvermell/elements/casa-bloc-nova/" in (
        tmp_path / "cossos/avis-1.txt").read_text(encoding="utf-8")


def test_una_colisio_es_refusa_i_no_bloqueja_la_resta(tmp_path, repo_prova, remot_bare):
    base = git(repo_prova, "rev-parse", "HEAD")
    canvia_titol(repo_prova, "content/ca/arquitectes/rebecca-horn/_index.md", "Pere López")   # col·lisió
    commit_sveltia(repo_prova, "Arquitecte", "rebecca-horn")
    canvia_titol(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova")             # correcte
    commit_sveltia(repo_prova, "Edifici", "casa-bloc")
    git(repo_prova, "push", "-q", "origin", "main")
    robot = clona(remot_bare, tmp_path / "robot")
    assert renom.executa_flux(robot, base, "HEAD", avisos_json=tmp_path / "av.json") == 0
    auto = log_auto(remot_bare)
    assert len(auto) == 2 and any("renom refusat" in l for l in auto)
    final = clona(remot_bare, tmp_path / "final")
    assert renom.llegeix_titol((final / "content/ca/arquitectes/rebecca-horn/_index.md").read_text(encoding="utf-8")) == "Rebecca Horn"
    assert (final / "content/ca/elements/casa-bloc-nova.md").exists()
    avisos = json.loads((tmp_path / "av.json").read_text(encoding="utf-8"))
    assert [a["assumpte"].startswith("No s'ha pogut") for a in avisos] == [True, False]
