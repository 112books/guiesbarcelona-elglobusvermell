# CMS Sveltia — diagnosi «no es veuen els Edificis i elements» (2026-09-30)

**Estat:** Resolt (no era cap avaria; era lentitud de càrrega).

## Símptoma

Joan: «no es veuen els Edificis i elements 660 per poder-los editar».

## Conclusió

El CMS **funciona**. Amb un token real i un navegador net, la col·lecció es carrega i mostra correctament:

- Col·leccions: **Edificis i elements (660)**, Pàgines (3), Plànols-guia (13), Arquitectes (197).
- Dins de «Edificis i elements»: llistat de **660 entrades**.

El que passava és que el **primer carregament és lent** (segons l'entorn, de l'ordre d'un minut) i, si sembla penjat, es té la sensació que no hi ha res. Els carregaments següents es fan des de la memòria cau del navegador (IndexedDB) i són ràpids.

## Verificacions fetes

1. `content/ca/elements`: 661 fitxers (660 entrades + `_index.md`), tots amb YAML frontal vàlid.
2. `static/admin/cms/config.yml`: vàlid; cap error a la pantalla de login de Sveltia.
3. API GitHub: arbre del repo (1.644 blobs) i GraphQL dels 661 blobs de les fitxes → OK.
4. Reproducció amb Chrome headless + token real: la llista de col·leccions i les 660 entrades es renderitzen (trigant).

## Causa

El primer carregament descarrega totes les entrades, els assets i la metainformació de commits. Amb ~660 fitxes d'elements + ~197 d'arquitectes, la primera càrrega pot trigar. No és un error de configuració ni de dades.

## Recomanacions

- Esperar el primer carregament; no recarregar mentre carrega.
- Si es vol alleugerir: `thumbnail: false` a la col·lecció elements (evita carregar miniatures) i/o simplificar `view_groups`.
- El CDN de Sveltia (`https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js`) està **sense fixar**: s'actualitza sol. Convé fixar la versió per evitar canvis inesperats.

## Notes

- L'editor master és a `/admin/cms/`; l'admin, a `/admin/cms-admin/`.
- Autenticació Fase 0: **PAT clàssic** de GitHub amb `public_repo` (el fine-grained no funciona per a convidats d'aquest repo).
- Versió de Sveltia servida en el moment de la diagnosi: **0.224.0**.

## Observació de Joan (2026-09-30, tarda)

A l'editor veu: «La creació d'entrades noves en aquesta col·lecció està desactivada per l'administrador» i, a sota, **«No s'ha trobat cap entrada.»**

Lectura:
- El primer missatge és correcte: `/admin/cms/` és l'editor d'edició (create: false). Per crear entrades noves cal `/admin/cms-admin/`.
- «No s'ha trobat cap entrada» pot ser (a) que el llistat encara s'està carregant (primer carregament lent) o (b) que hi ha un filtre o agrupació de la vista seleccionat que no té coincidències (botons «Filtra» i «Agrupa»).
- Què comprovar: esperar que acabi el carregament i, si continua, obrir «Filtra» i «Agrupa» i triar l'opció sense filtre; si tampoc, esborrar les dades del lloc al navegador (IndexedDB/sessionStorage) i tornar a entrar.

## Mesures aplicades (2026-09-30, vespre)

Perquè el CMS no depengui d'un estat de memòria cau vell (el cas reportat a Safari):

1. **Botó «Neteja la memòria cau»** a `static/admin/cms/index.html`: esborra IndexedDB i CacheStorage i recarrega. **No toca el token** (localStorage), així que no cal tornar-lo a introduir.
2. **Reinici automàtic de memòria cau** en canviar la constant `CMS_CACHE_VERSION` de la mateixa pàgina: la primera visita després d'un canvi neteja i recarrega un cop; la resta de visites no fan res.
3. **Càrrega de Sveltia dinàmica**: el script del CDN s'injecta després de la comprovació de memòria cau, perquè no quedi mai servit des d'un estat vell. S'hi afegeix `data-cfasync="false"` (evita el Rocket Loader de Cloudflare, si algun dia hi és).
4. **`thumbnail: false`** a la col·lecció d'elements de `config.yml`: el llistat de les 660 fitxes ja no baixa les miniatures al primer carregament.
