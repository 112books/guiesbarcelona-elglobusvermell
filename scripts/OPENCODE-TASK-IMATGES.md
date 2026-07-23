# Tasca per OpenCode: descarregar imatges dels edificis (elements)

## Context

Aquest projecte Hugo (`guiesbarcelona.elglobusvermell.org`) té 656 fitxes d'edificis
a `content/ca/elements/*.md`. Cada fitxa mostra una foto destacada si té el camp
`foto:` al front matter (path tipus `/img/elements/<slug>.jpg`); si no el té,
la plantilla mostra un placeholder "Imatge pendent"
(`themes/guiesbcn-elglobusvermell/layouts/elements/single.html:18-26`).

**A dia 2026-07-23, només 9 de 656 elements tenen `foto:` definit.** Calen les
altres ~647.

Les fotos existeixen al WordPress de producció
(`https://guiesbarcelona.elglobusvermell.org`), incrustades al cos de cada
article. Hi ha un script existent que ja sap trobar la pàgina WP de cada
element i identificar quina imatge és la foto de l'edifici (no una icona de
categoria): `scripts/sync_elements_wp.py`.

## Script ja preparat

`scripts/download-images-elements.py` — **ja escrit i provat** (5 elements de
prova, 1 descarregat correctament: `acabados-tintes-y-estampados`).

Fa, per a cada element sense `foto:`:
1. Troba la URL WP corresponent (`find_wp_url`, per slug + categoria de la
   publicació).
2. Raspa la pàgina i n'extreu la primera imatge que no sigui icona/portada
   (`scrape_wp_page`, ja filtra logos, portades, icones de categoria).
3. Prova d'aconseguir la versió d'alta resolució (elimina el sufix
   `-300x300` etc. del nom de fitxer WP i comprova que existeixi).
4. Descarrega la imatge a `static/img/elements/<slug>.jpg`.
5. Afegeix `foto: /img/elements/<slug>.jpg` al front matter del `.md`.

És **idempotent**: si un element ja té `foto:`, se salta. Si el fitxer local
ja existeix, no el torna a descarregar. Es pot aturar i reprendre sense
problema.

## Com executar-ho

Ja hi ha un entorn virtual preparat amb les dependències instal·lades:

```bash
cd "/Volumes/1TbExt/Obsidian/hugo-websites/elglobusvermell.org/guiesbarcelona.elglobusvermell.org"

# Prova amb pocs elements primer (ja fet, però per referència):
.venv-scripts/bin/python3 scripts/download-images-elements.py --limit 10

# Execució completa (els ~647 pendents, triga per l'espera educada
# de 0.8s entre peticions a WP — compte, pot trigar 15-25 minuts):
.venv-scripts/bin/python3 scripts/download-images-elements.py
```

Genera `scripts/download_images_report.md` amb el resultat: quants
descarregats, quants sense imatge trobada a WP, quants no trobats, i errors.

## Coses a vigilar

- **No cal tocar `sync_elements_wp.py`** — només se n'importen dues funcions
  (`find_wp_url`, `scrape_wp_page`). No dupliquis aquesta lògica.
- Alguns elements (uns 42 de 656) tenen un slug a Hugo que **no coincideix
  exactament** amb el slug de WordPress (compte de duplicats "-2", canvis de
  nom, etc.). Aquests sortiran a la secció "Not found on WP" del report —
  **no cal perseguir-los ara**, és una llista per revisar manualment després.
- Alguns edificis simplement no tenen cap foto de l'edifici a WP (només
  icona de categoria) — sortiran com "No image found". Tampoc cal insistir-hi.
- Si el WP en viu queda inaccessible o comença a donar 429/503 (massa
  peticions), atura't i informa — no cal reintentar en bucle.
- Un cop acabat: fer `git status` per veure quants `.md` s'han modificat i
  quantes imatges noves hi ha a `static/img/elements/`, i deixar-ho preparat
  per a revisió/commit per en Joan (no fer commit ni push automàticament).

## Resultat esperat

Que el màxim nombre d'elements possible passi de "Imatge pendent" a mostrar
la foto real de l'edifici, sense haver tocat manualment cap `.md` un per un.
