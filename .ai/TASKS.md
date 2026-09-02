# TASKS.md — Llista de tasques

Llegenda: ✅ Fet | 🔄 En curs | ⏳ Pendent | 🔴 Bloquejat (espera info externa)

**⏱️ CONTROL DE TEMPS — OBLIGATORI (estipulat al projecte, recordat per Joan l'1 set):** previ a fer res a cada sessió, arrencar el skill `time-tracker` i registrar mentre es fa la feina; al tancament, escriure el log del dia a `../docs/.taques/guia-globus-vermell/YYYY-MM-DD.md` + línia a `../docs/.taques-central/` + commit i push des de `../docs`. Resum global i mètode: `../docs/.taques/guia-globus-vermell/projecte-resum.md` (regla completa al `CLAUDE.md` de l'arrel). **Cap sessió no es dóna per tancada sense el registre pujat.**

**Priorització de Joan:** **1) Rendiment, 2) Seguretat** ✅ completats l'1 set. **Pla nou (decidit l'1 set vespre):** demà 2 set → **deixar perfecte SEO + motors d'IA** («que ens trobin fàcil i eficientment»); després → **accessibilitat restant, seguretat restant i autoria del codi**. Cap mail diari a Xavi (vacances fins ~16 set): **esborrany de control cada dia + un únic resum setmanal a final de setmana** amb les tasques de cada dia. El pas al servidor de producció serà **la darrera cosa** (cal decidir servidor + migració completa); **GitHub Pages fins a nova ordre**.

**Detall del pla de la setmana:**
- **SEO + IA (demà 2 set)**: rellegir a fons `.ai/informe-seo-geo-aeo-2026-09-01.pdf` i aplicar tot el que no depengui del tall del domini; el que sí en depengui, deixar-lo preparat per activar just al tall (GSC, Bing/IndexNow — pas 5 de l'informe). FAQ/schema FAQPage, SSR de llistes, `og:image` 1200×630 i consistència de xifres toquen consens d'equip → només llistar-les, no avançar sol
- **Accessibilitat restant** (informe 30/8): teclat dels marcadors Leaflet (§2.2, capa JS amb `tabindex` + `keydown`), `aria-required` + errors accessibles als formularis (§2.3), «(PDF)» als enllaços de descàrrega de plànols (§3.3), tests automàtics axe/pa11y al CI (§3.4)
- **Seguretat restant**: OAuth proxy (Fase 1, espera Dinahosting), `analytics.json` (restringir post-migració), `envia.php` (auditar o substituir el dia del tall); revisar si hi ha res més aplicable ara
- **Autoria del codi (a aclarir amb Joan)**: (1) identitat git — 179 commits fets des d'aquesta màquina amb la config genèrica «El teu nom <el-teu-email@example.com>»: cal decidir quina identitat han de dur els commits i configurar-la (opcionalment `.mailmap` per unificar la vista dels existents, sense reescriure la història); (2) llicència del codi: el contingut és CC BY-SA 4.0 però el codi del tema i els scripts no en tenen cap; (3) crèdits d'autoria al web i al repo
- **Mail setmanal a Xavi**: esborrany diari a `docs/` (el de l'1 set ja escrit: `docs/esborrany-mail-control-xavi-1set.md` — queda com a dia 1 del resum) i **un sol mail-resum a final de setmana** amb les tasques de cada dia; enviat, es converteix en registre i s'arxiva al repo de docs com els altres

---

## Web guies (guiesbarcelona.elglobusvermell.org)

### Infraestructura
- ✅ Repositori GitHub + deploy automàtic a GitHub Pages
- ✅ Dominis: funcionant a https://112books.github.io/guiesbarcelona-elglobusvermell/
- ⏳ Configurar domini propi guiesbarcelona.elglobusvermell.org — **decisió de Joan (1 set): el pas a producció serà la DARRERA cosa a fer** (cal decidir encara el servidor i fer tota la migració). **El web queda a GitHub Pages fins a nova ordre.** Troballa 31 ao nit: el domini de producció (apex i www → `195.201.2.76`, Hetzner) encara serveix el WordPress antic; el Hugo viu a `112books.github.io` (quan el mail a Xavi diu "en línia" = github.io). Pas a pas del tall: `.ai/informe-seo-geo-aeo-2026-09-01.pdf`
- ✅ **Verificació diària dels números del web** (1 set, a petició de Joan): `scripts/verifica-numeros-web.py` + workflow `verifica-numeros.yml` (cada dia 06:30 UTC). Compara les xifres publicades a la portada (659 edificis / 13 guies / 274 arquitectes / 1928–2026) amb el càlcul sobre el contingut del repo i amb el dia anterior; escriu `.ai/VERIFICACIO-NUMEROS.md` (amb el significat de cada xifra i històric de 14 dies) + `.ai/numeros-web-history.json`, i marca una alerta visible al run si alguna cosa no quadra. Primera verificació (1 set): tot coincideix

### Contingut
- ✅ Importació de 66 edificis des del dump SQL (7 publicacions)
- ✅ Pàgina Presentació
- ✅ Pàgina En paper (13 publicacions)
- ✅ Pàgina Crèdits (amb LinuxBCN)
- ✅ **Contingut migrat fins a les fonts disponibles** (verificat 1 set): dump del 16/02/2026 + CSV d'ítems publicats + correccions d'Xavi → 660 fitxes (659 amb coordenades), 13 publicacions, 274 arquitectes, 837 imatges optimitzades (144 MB, 0 enllaços externs). Les entrades antigues «564 pendents» i «imatges espera Jorge» eren del PLAN inicial, anteriors a la importació — tancades
- 🔴 **Confirmació definitiva de la migració contra el WordPress en producció (la font «bona», recordatori de Joan 1 set)**: el dump és una instantània del 16/02 i el comptatge preliminar no quadra amb les 660 fitxes — cal verificar contra el WP en viu (accés Jorge o exportació fresca) que no hi ha canvis posteriors ni contingut absent, just abans del tall. Confirmació de dues línies demanada a Xavi al mail de control. **Regla ferma: MAI esborrar res de fitxes** — cap discrepància es resol esborrant; sempre corregint o afegint contra el WP
- ✅ Geocodificació dels edificis: completa — 659 de 660 fitxes amb coordenades; l'única sense és `flors-de-la-rambla` (31 ao, a propòsit: al llistat, sense punt al mapa, dades pendents d'Xavi ~16 set)
- ✅ Detecció i llistat de punts desubicats (`.ai/PUNTS-DESUBICATS.md`) — confirmats per Xavi (18 ago): les 5 fitxes ja tenien la coordenada correcta a la base de dades actual, no calia tocar res. Canvi de nom "Casa xalet passatge Roserar" → "Casa Mercè Escolano" aplicat al frontmatter (2026-08-19).

### Mapa
- ✅ Mapa Leaflet + OpenStreetMap
- ✅ Marcadors amb color per publicació
- ✅ Filtres per publicació (llista plana, activables independentment)
- ✅ Nou comportament del filtre: tots els punts atenuats al iniciar, ressaltar al marcar una publicació
- ✅ Punts en múltiples publicacions: dibuixats amb dos o més cercles de colors
- ✅ Filtre URL (?pub=gatcpac) per arribar al mapa pre-filtrat des de les fitxes — enllaç "Tots els elements" a la fitxa ara inclou `?pub=SLUG` (2026-08-19)

### Fitxes d'edifici
- ✅ Template single.html amb dades, navegació
- ✅ Enllaços a publicació i arquitecte des de la fitxa (corregit bug d'URL amb subpath)
- ✅ Fitxes sense foto: no es mostra placeholder
- ✅ **Color de la publicació com a identitat visual de la fitxa** — banda horitzontal 30px (`fitxa-pub-banda`) amb `var(--pub-color)`, idèntica al disseny de les publicacions (2026-08-19). Revertida banda vertical afegida sense aprovació.
- ✅ Mapa individual a la fitxa (JS carregant, revisat bug de quotes al FITXA_PUNT — 2026-08-19: verificat que `jsonify | safeJS` produeix JSON vàlid a totes les 656 fitxes amb lat/long, cap bug trobat)
- 🔴 Imatge de l'edifici a la fitxa (espera servidor)
- ⏳ Imatge del plànol-guia a la fitxa

### Arquitectes
- ✅ Taxonomia d'arquitectes activa a Hugo (`config/_default/hugo.toml`)
- ✅ Layouts per a pàgina de llistat i pàgina d'arquitecte individual (amb mapa i llistat d'edificis)
- ✅ Enllaços a arquitectes des de la fitxa d'edifici
- ⏳ Separar noms d'arquitectes combinats (73 casos, `.ai/ARQUITECTES-A-SEPARAR.md`) — format de resposta enviat a Xavi (18 ago): `Nom combinat → Nom 1, Nom 2`, una línia per cas. Pendent que Xavi ompli la llista.
- ✅ Normalitzar variants duplicades d'arquitectes: totes les fitxes ja fan servir el nom canònic (verificat 2026-08-19, cap variant del YAML trobada al contingut). Tasca tancada.

### Disseny
- ✅ Logo guiesbarcelona al header
- ✅ Sistema de colors per publicació
- ⏳ Decisió paleta definitiva (espera Xavi)
- 🔴 Logo elglobusvermell.org principal (espera servidor Jorge)
- ✅ Disseny mòbil (revisat responsiu 2026-08-19: breakpoints 48rem/36rem/480px ja cobreixen fitxa, mapa, llistat i navegació. Cap bug crític trobat)
- ✅ Revisar secció "En paper": miniatures per idioma + botons de PDF — afegits estils CSS per `.publicacio-idioma-link` i `.publicacio-idioma-placeholder` (2026-08-19). Pendents: PDFs francès (8), PDFs castellà/anglès (barceloneta, marina), portada gatcpac-fra.jpg
- ✅ Pàgina de cada guia: secció de descàrregues PDF per idioma preparada (es mostra quan hi ha PDFs a `static/pdf/`)

### CMS Editorial (Sveltia CMS) — vegeu `.ai/CMS-PLAN.md`

#### Fase 0 — sense servidor (implementable ara)
- ✅ Script migració TOML→YAML (`scripts/toml-to-yaml.py`)
- ✅ Migrats 70 fitxers d'elements a YAML + build Hugo verificat
- ✅ Crear `static/admin/index.html` + `config.yml` (master: tot)
- ✅ Crear `static/admin-editor/` (editors: només fitxes d'edificis)
- ✅ Verificar CMS a GitHub Pages amb PAT de prova — **FET 1 set (Joan)**: login amb PAT fine-grained ✓, desat d'una edició ✓ (commits a main com "Joan Mz Linux"), deploy ✓. **Trobat:** cada desat del Sveltia **reescriu el format del front matter** de la fitxa (reordena camps, llistes amb sagnat, afegeix els camps opcionals buits com `foto: ''`) — els valors no canvien i és harmless, però els diffs semblen grans; convé avisar l'equip a la guia. Fitxa de prova restaurada byte a byte (`1a7e157`). **El mail d'instruccions es va enviar l'1 set — amb una errata al PAS 4**: explicava el token *fine-grained*, que els convidats no poden crear (limitació de GitHub: només repos propis o d'organitzacions membre; aquest repo és d'un compte personal, i el test va funcionar perquè es va fer des del compte propietari). Corregit amb **token clàssic** el mateix dia — vegeu el mail rectificatiu
- ⏳ Invitar comptes GitHub al repo (rol Write) — **cap compte donat per fet**: cada membre confirma el seu nom d'usuari i el verifiquem a GitHub abans de convidar (del mail del 31 ago consta el de la Laia, `laiabrelglobusvermell-design`; verificar amb ella igualment)
- ✅ Mails d'accés a l'editor — **instruccions ENVIADES l'1 set a les 16:41** (Laia, Joan Vítoria, Mar + Xavi) **amb una errata al PAS 4**: el token *fine-grained* que explicava no el poden crear els convidats (limitació GitHub: només repos propis o d'organitzacions membre; el nostre repo és d'un compte personal — el test de la Fase 0 va funcionar perquè es va fer des del compte propietari, 112books). El mail enviat queda com a registre a `docs/esborrany-mail-instruccions-editor-cms-1set.md`. **Rectificatiu ENVIAT el mateix dia a la tarda** (resposta al mateix fil); registre i còpia al repo de docs a `docs/esborrany-mail-correccio-token-cms-1set.md` — PAS 4 reescrit amb **token clàssic** (`github.com/settings/tokens/new`, permís `public_repo` — el repo és públic i és el permís mínim possible: només toca repos públics —, caducitat 1 any via Custom, prefix `ghp_`), garantit per a col·laboradors i més senzill (no cal triar repositori). També corregeix l'etiqueta del botó de login (en català a la UI) i la frase de seguretat (el clàssic no és "només aquest projecte": és "només repos públics on el teu compte pot entrar"). Guia `/admin/guia/` i pistes de `cms/` + `cms-admin/` corregides (`a333625`, verificat en línia). **Pendent: esperem els noms d'usuari (PAS 2) per verificar-los a GitHub i convidar (rol Write)**
- ⏳ Guia de l'editor: afegir captures reals dels passos (el mail de l'1 set promet "captures" que la guia no té: l'única imatge és el logo)
- ✅ Sincronitzar `cms-admin/config.yml` amb `cms/config.yml` (1 set): bloc de fotografia idèntic (`foto_autoria` + `foto_peu` + `fotos_addicionals` com a objectes url/autoria/peu — la plantilla accepta tant strings com objectes, i cap fitxa fa servir encara `fotos_addicionals`, zero risc), i afegit el camp **"Web oficial" (`link_web`)** de la col·lecció Arquitectes, que també hi faltava (trobat amb el diff). Aprofitat per: treure la frase falsa de l'hint "el web mostra un espai reservat («Imatge pendent»)" (la plantilla no mostra cap placeholder — corregida també a la guia, que a més guanya les files d'Autoria i Peu de foto a la taula de camps) i actualitzar els comentaris d'autenticació dels dos configs al **token clàssic**. Diferències intencionals que queden: `create: true` i `app_title` "(Administrador)"
- ✅ Guies del CMS revisades (1 set): `guia/` mostrava el domini de producció (encara el WP antic) com a adreça de l'editor → ara l'adreça real github.io + el domini futur; nota provisional a `instal-la-al-mobil`. Hub i guies `/admin/` públics i **sense login** (per disseny, confirmat per Joan); a producció, el robots.txt ja fa `Disallow: /admin/`

#### Fase 1 — OAuth proxy (quan Dinahosting estigui llest)
- 🔴 Crear GitHub OAuth App per a dev (callback → GitHub Pages)
- 🔴 Crear GitHub OAuth App per a prod (callback → Dinahosting)
- 🔴 Crear `oauth/index.php` amb validació CSRF (state param)
- 🔴 Configurar secrets a Dinahosting fora del webroot
- 🔴 Actualitzar `config.yml` amb `base_url` del proxy
- 🔴 Provar flux OAuth complet (dev + prod)

#### Fase 2 — Editorial workflow (quan Sveltia CMS v1.0 — tardor 2026)
- ⏳ Activar `publish_mode: editorial_workflow`
- ⏳ Configurar branca `drafts` per a editors
- ⏳ Revisar rols si Sveltia v1.0 ja els implementa

---

## App mòbil Flutter

- ⏳ Eliminar Firebase del codi Flutter
- 🔴 Nova Google Maps API Key — caduca el setembre 2026. **Verificat 31 ago: el web NO la fa servir** (Leaflet + OpenStreetMap; l'única referència és un text d'ajuda de l'admin per buscar coordenades). La clau era per a l'app Flutter antiga. Proposta al mail de resposta: avaluar mapes lliures (flutter_map/OSM) a l'app nova → cap clau ni caducitat; decisió de Globus per a l'app antiga (Xavi/Jorge)
- ⏳ Compilar app buida iOS + Android
- ⏳ Decidir arquitectura BD (PostgreSQL / SQLite / altra)
- ⏳ Decidir futur backoffice Node.js
- ⏳ Migrar compte admin Xavi
- ⏳ Llistat d'edificis amb filtres per publicació
- ⏳ Fitxa d'edifici amb mapa
- ⏳ Mapa general amb punts
- ⏳ Clarificar "filtrar per publicacions" al mapa (preguntar Xavi)

### GoatCounter Dashboard — vegeu `.ai/GOATCOUNTER-HUGO-PLAN.md`

- ⏳ Adaptar `goatcounter-dashboard/admin/index.html` → layout Hugo `layouts/stats/list.html`
  (substituir CFG hardcoded per valors del frontmatter del `.md` de configuració)
- ⏳ Adaptar `scripts/fetch_goatcounter_analytics.py` → `scripts/fetch-goatcounter.py`
  (llegir config des del frontmatter, output a `static/data/analytics.json`)
- ⏳ Crear `.github/workflows/goatcounter.yml` (fetch horari + commit automàtic)
- ⏳ Crear `content/ca/estadistiques/_index.md` (fitxer de config del projecte)
- ⏳ Afegir tracking script a `head.html` (condicionat: no en local)
- ⏳ Afegir `GC_API_TOKEN` com a GitHub Secret al repo guiesbarcelona
- ⏳ Decidir path: `/ca/estadistiques/` vs `/admin/stats/`
- ⏳ Documentar procés per reutilitzar en altres projectes Hugo (15 min/projecte)

---

## Accessibilitat i millores d'experiència

- ✅ **Text a veu (TTS) per a fitxes d'edifici** — Web Speech API amb pausa/continua (2026-08-19). Boto: Escoltar → Pausa → Continua → Aturar. Pendents: millores de veu, velocitat ajustable, selecció de veu
  - Avaluar solucions de programari lliure (Web Speech API nativa del navegador, o eSpeak/Piper si es vol veu pròpia al servidor)
  - Decidir veu: Web Speech API és gratuïta i funciona sense servidor (veus del sistema, pot sonar robòtic); Piper TTS és lliure i permet veu neutra de qualitat
  - Icona de reproducció discreta a la fitxa (play/pause)
  - Valorar quins camps llegir: títol, adreça, any, arquitecte/s, descripció
  - Estimar temps i cost: Web Speech API = 1-2 dies (zero cost); Piper al servidor = 3-5 dies (cost infraestructura)
- ✅ **Crèdits → Tecnologia**: entrada TTS afegida (Web Speech API, confirmada per Xavi 28 ago) — ja ho havia fet el commit `4fdd097` (29 ago); l'entrada quedava desactualitzada
- ✅ **Accessibilitat → Mesures aplicades**: "Lectura en veu alta" i "Peu de foto com a alt text" ja hi són (`4fdd097`); verificat a la pàgina actual
- ✅ **Accessibilitat → Tecnologia**: Web Speech API ja llistada a la secció "Tecnologia utilitzada"
- ✅ **Fotografies crèdit**: **CC-BY-SA 4.0, "El Globus Vermell"** — confirmat per Xavi (mail 2026-08-28). Implementat al peu de foto de `elements/single.html` (commit `4fdd097`, 29 ago).

---

## SEO, RGPD i seguretat (30 ago 2026)

### Implementat ✅
- ✅ **Informes d'auditoria** — generats i guardats a `.ai/` (30/08/2026):
  - `.ai/informe-accessibilitat-2026-08-30.md` — WCAG 2.1 AA, ~75-80% conformitat
  - `.ai/informe-seguretat-2026-08-30.md` — nivell MODERAT-BAIX
  - `.ai/informe-rendiment-2026-08-30.md` — bloquejat per imatges (880 MB sense WebP)
  - `.ai/informe-seo-rgpd-2026-08-30.md` — RGPD conforme, SEO moderat
- ✅ **Open Graph + Twitter Cards** — `head.html`: metadades socials per a fitxes i pàgines; imatge de l'edifici com a `og:image`; condicionals: inactiu a staging
- ✅ **Schema.org JSON-LD** — `partials/schema.html` nou: `WebSite` (inici) + `LandmarksOrHistoricalBuildings` (fitxes, amb adreça, coordenades GPS, arquitectes, any)
- ✅ **Meta description automàtica** — si no hi ha `description` al front matter, s'usa `.Params.descripcio` truncat a 155 caràcters
- ✅ **Política de privacitat** — `content/ca/legal/privacitat.md`: RGPD, GoatCounter, drets ARCO
- ✅ **Política de galetes** — `content/ca/legal/cookies.md`: sense cookies, GoatCounter sense cookies, OpenStreetMap/CartoDB
- ✅ **Avís legal** — `content/ca/legal/avis-legal.md`: propietat intel·lectual, CC BY-SA 4.0, responsabilitat
- ✅ **Fotos-web-app a .gitignore** — 880 MB d'imatges locals excloses de git
- ✅ **Auditoria SEO/GEO/AEO completa (1 set 2026)** — `.ai/informe-seo-geo-aeo-2026-09-01.pdf` (15 pàgines; SEO 6/10, GEO 5/10, AEO 5/10 — el desbloquejador únic és el tall del domini, amb pas a pas a l'informe). Crawling del staging + build de producció verificat en local + WordPress mare (671 URLs). PDF regenerat el mateix dia amb els recomptes exactes (660 fitxes, 274 arquitectes, 79 de 274 pàgines d'arquitecte sense contingut propi — l'original deia 661/277/277)
- ✅ **Paquet de millores SEO/GEO/AEO (1 set)** — aprovat per Joan («sense tocar el disseny, arreglar al màxim»; només metadades, detall a `.ai/REGISTRE-CANVIS-FITXES.md`):
  - JSON-LD corregit amb `safeJS` (tota la dada estructurada era invàlida) + schema Person/Organization nou per als 274 arquitectes amb `sameAs` (COAC/Viquipèdia/web oficial)
  - Redireccions de les **671 URLs del WordPress antic** via `aliases` a 660 fitxes (44 renoms verificats un per un + 11 pàgines `/text/` → publicacions); `scripts/aliases-wordpress.py` idempotent; plantilla `alias.html` catalana amb noindex
  - `robots.txt` de producció amb `Sitemap:` + `Disallow: /admin/`; `llms.txt` nou per a motors d'IA; `404.html` propi amb el layout del tema
  - Meta descriptions a les 13 publicacions + hubs (arquitectes, accessibilitat, presentació, publicacions amb títol nou); `og:image` per defecte (logo) + portades a les publicacions; títol del mapa; `enableGitInfo` → `lastmod` a les 964 URLs del sitemap
- ✅ **Segona passada SEO/IA (2 set)** — quick wins de l'informe verificades amb build de producció (`--environment production`: 963 URLs al sitemap, 672 aliases):
  - `og:image` per defecte ara **1200×630** (`static/img/og-default.jpg`, logo sobre fons blanc generat amb sips; `defaultOgImage` al config) — les ~315 fitxes sense foto i les pàgines hub ja tenen vista prèvia amb proporcions socials. ⚠️ Pendents: verificació visual humana (aquest model no llegeix imatges) i possible actiu dissenyat (Xavi)
  - `robots.txt` de producció: 13 bots d'IA i cercadors generatius explícitament permesos (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot...) — senyal GEO coherent amb el `llms.txt`
  - `404.html`: enllaç «Cerca un edifici al llistat alfabètic» → `/mapa/#llistat` (aprofita el filtre de cerca del mapa)
  - **SpeakableSpecification** (JSON-LD WebPage) a les fitxes amb descripció — `cssSelector: .fitxa-descripcio`, alineat amb el TTS «Escoltar» existent
  - **Duplicat `/elements/` eliminat**: la pàgina de secció `/elements/` (mateix títol «Mapa» i mateix contingut JS que `/mapa/`, restes del canvi d'URL del 31/8) ja no es renderitza (`build: render: never` a `elements/_index.md`) i `/elements/` redirigeix a `/mapa/` via `aliases` (meta-refresh + canonical, plantilla catalana). L'enllaç «Tots els elements» de les 660 fitxes ara apunta directe a `/mapa/?pub=X` (el JS del mapa ja llegia el paràmetre `pub`; abans anava al duplicat). Sitemap verificat sense `/elements/` i amb les 660 fitxes intactes
  - **sameAs social a l'Organization de la portada** (graf d'entitat): 6 perfils confirmats per Joan el 2 set (Instagram, Twitter/X, Bluesky, Facebook, LinkedIn, YouTube — Bluesky/LinkedIn/YouTube verificats vius) al paràmetre `social` del config; **Issuu exclòs: perfil 404** verificat el 2 set. El peu no té enllaços socials (canvi visible → Xavi/consens)
  - Fix de codi de pas: `.Site.Data`/`site.Data` deprecats (shortcode `portada-guia.html` i `imatges_dims` a `single.html`) → `hugo.Data`; el build de producció queda sense cap warning (Hugo ≥0.156)

### Accessibilitat (informe 30/8 — corregit 1 set)
- ✅ Declaració d'accessibilitat (`/accessibilitat/`) revisada i ajustada a la realitat (1 set): mesures aplicades sense sobreprometre, limitacions conegudes ampliades (carrusel amb teclat, focus dels filtres, contrast de 2 elements, skip link) i allotjament actualitzat. Les millores de la llista de sota s'han aplicat (1 set) i la declaració ja les mostra a "Mesures aplicades"
- ✅ Contrast insuficient: `.footer-powered-link` i `.footer-powered-services` #b3b3b3 → #6b6b6b (el segon tenia el mateix gris i també fallava AA — l'informe només llistava el primer), `::placeholder` #aaa → #767676 — `main.css`
- ✅ Carrusel: fletxes ArrowLeft/ArrowRight (keydown al contenidor: val amb el focus a qualsevol control), `aria-pressed` als dots i comptador «Diapositiva N de M» sr-only (`role="status"`) — `fitxa.js` + `single.html`
- ✅ Dots 44px: àrea de toc de 2.75rem amb el punt visual de 8px al centre (`::before`); retirat `role="tab"/"tablist"` (patró incomplet: no hi havia tabpanel) → `role="group"` + `aria-pressed` tal com demana l'informe
- ✅ Focus visible filtres: regles explícites a `.filtre-btn`/`.filtre-lateral`/`.filtre-btn-info` + arrel trobada: la regla global `:focus-visible` afegia `border-radius: 2px` i aixafava els botons píndola al rebre focus (per això "no s'heretava bé"); tret de la global
- ✅ Botó "i" de publicació: icona SVG d'info (aria-hidden) + `span.sr-only` amb l'etiqueta; CSS sense la tipografia serif itàlica — `mapa.js` + `main.css`
- ✅ Skip link a `baseof.html` (primer element del body) + `main id="main" tabindex="-1"` + CSS (apareix en rebre focus)
- ✅ `aria-current="page"` a l'entrada activa del menú (`header.html`, `$.RelPermalink` vs `.URL`)
- ✅ Pàgina `/accessibilitat/` actualitzada: les 4 limitacions corregides passen a «Mesures aplicades»; queden com a limitacions honestes el Leaflet i els formularis (informe §2.3)

### Pendent — seguretat (informe)
- ✅ URL `?tema=` whitelist explícita — `mapa.js` (1 set): només a/b/c, la resta cau a 'a'; abans un valor aliè podia trencar `classList.add` i deixar el mapa sense inicialitzar
- ⏳ CMS auth: OAuth GitHub App (Fase 1, ja prevista)
- ⏳ `analytics.json` públic: restringir o eliminar un cop migrat a Vercel/Netlify
- ✅ `unsafe = false` a Goldmark (1 set): l'únic HTML en cru del contingut (badges d'accessibilitat) mogut al shortcode `badges-accesibilitat`; build complet verificat idèntic (1.645 pàgines, només canvia el fingerprint del `mapa.min.js`)

### Pendent — rendiment (informe)
- ✅ **Imatges optimitzades in situ** (1 set, decisió de Joan: **JPG redimensionat i no WebP**, perquè WhatsApp/Telegram no llegeixen WebP com a `og:image` i caldria miniatures jpg que es mengen l'estalvi): màx 1.600px, qualitat 85, EXIF tret amb auto-orient — **837→144 MB (−83%)**: elements 818→134 (353 de 358; 5 ja optimitzades es mantenen) i publicacions 19→10 (37 de 50). Mateixos noms i URLs, cap canvi de plantilla; originals recuperables a la història de git. Commit `42337ff`
- ✅ **33 fotos de biblioteques enllaçades** (forat de migració: la foto era al disc però faltava el camp `foto:` a la fitxa) + 150 barres inicials de `foto:` normalitzades — entrada #6 del registre; 5 biblioteques sense imatge queden a pendents (cal aportar les fotos)
- ⏳ ~~`width`/`height` a `<img>` de fitxes~~ → ✅ FET (1 set): manifest `data/imatges_dims.json` (408 imatges, generat amb `scripts/genera-dims-imatges.py`, re-executable) i `single.html` el consulta — reserva l'espai de la foto abans de carregar (menys CLS)
- ✅ Foto única de fitxa `loading="lazy"` → `eager` + `fetchpriority="high"` (1 set): era la imatge principal/LCP; la primera diapositiva del carrusel també porta ara `fetchpriority`
- ✅ Leaflet verificat (1 set): `leaflet.js` **ja és la dist minificada oficial 1.9.4** — 147 KB en disc però **42 KB gzipades** en línia (GitHub Pages serveix gzip); l'entrada venia de confondre la mida en cru amb la transferida. Cap canvi necessari
- ✅ Verificar sitemap.xml a producció (build `--environment production`) — verificat a l'auditoria 1/9: 964 URLs correctes al domini final + `lastmod` a totes (enableGitInfo)

### Pendent — SEO (informe 30/8 + auditoria 1/9)
- ⏳ Google Search Console + Bing Webmaster/IndexNow — activar just després del tall del domini (pas 5 del pas a pas de l'informe del 1 set)
- ⏳ `hreflang` — preparar quan s'activin EN/ES
- ⏳ Auditar `envia.php` — **no és al repo Hugo** (herència del WordPress de producció, Hetzner): auditar-lo o substituir-lo (formulari de contacte) toca al dia de la migració/tall
- 🔴 SSR de llistes (arquitectes/publicacions) + headings al mapa — toca el renderitzat → Xavi/consens d'equip
- 🔴 FAQ + schema FAQPage + headings en forma de pregunta — contingut editorial → equip
- 🔴 `og:image` pròpia 1200×630 dissenyada — el placeholder actual (logo sobre blanc) ja és 1200×630 però és provisional → equip de disseny
- 🔴 Consistència de xifres portada/Presentació — semàntica aclarida (1 set): la portada compta fitxes **amb coordenades** (659 de 660) i les **13 guies del projecte** (11 amb pàgina web + New Babylon i Tàpies «en paper»); la Presentació mostra 660 «Punts» / 11 «Mapes» / 98 anys. Debat d'equip obert (també sobre el 1928 editorial); la verificació diària vigila que cap xifra canviï sense que ens adonem

---

## Infraestructura servidor

- 🔴 Rebre dades de Jorge (host, usuari, ruta, clau SSH)
- ⏳ Còpia del WordPress actual (wp-content + BD)
- ⏳ Pressupostar migració WordPress → Dinahosting
- ⏳ Decidir correu: IMAP propi / Etik / seguir amb Gmail informal
- ⏳ Configurar clau SSH LinuxBCN al servidor de Jorge
- ✅ Clau SSH LinuxBCN generada (~/.ssh/linuxbcn) i pujada a GitHub

---

## Correu Xavi — repàs de fitxes per plànol (2026-08-18)

Correu llarg, revisió plànol per plànol. Triatge fet, res aplicat encara. Confirmat amb mostres reals:
`mercat-de-canyelles.md` (cap camp `any`, l'any 1987 només dins el text lliure), `masia-can-basté.md`
("segle xviii"/"segle xx" en minúscules dins el text), fitxa combinada biblioteca+jardí de Càndida Pérez
(el blob de `descripcio` ja conté les etiquetes "Sobre els jardins:" / "Més info:" / "Sobre la biblioteca:"
barrejades en text pla — confirma que la info hi és, només cal extreure-la).

### 🔧 Mecànic — es pot fer sense esperar decisió
- ✅ "Data desconeguda" en lloc de "(sense any)" al llistat del mapa (`mapa.js`) quan no hi ha camp `any` — commit `ed96c94`.
- ✅ Segles en majúscules als textos (versaletes no aplicat, s'ha fet servir la variant que Xavi permetia com a alternativa) — 78 fitxes, "segle xix" → "segle XIX" a totes les masies i altres plànols. Script amb whitelist de numerals romans I-XXI per evitar falsos positius (paraules com "li"/"civil"/"mil"). Commit `ed96c94`.
- ✅ Bug del "2" al principi del text (jardins/places) — **arrel confirmada**: el símbol "m²" es va partir en la importació ("m" quedava al camp `superficie`, "2" migrava com a primer token de `descripcio` de la fitxa següent). 58 fitxes afectades (56 jardins + 2 places), totes corregides: `superficie` recupera el "²", `descripcio` perd el "2 " inicial. Commit `9fbff6d`.

### 🔍 Cal investigar abans d'actuar (abast/causa desconeguts)
- ✅ Format de foto: arrel confirmada — fotos originals gairebé quadrades (mostra: 1200x1200 majoritàriament, algunes 1200x1000), CSS forçava `aspect-ratio: 16/9` amb `object-fit: cover` (retallava ~44% vertical). Canviat a `1/1` a `.fitxa-imatge` i `.fitxa-carrusel-slide`. Portades de plànol-guia (2/3, format llibre) no tocades. Commit `b185b97`.
- ✅ Biblioteques — foto de portada del plànol en lloc de l'edifici: **confirmat per hash MD5**, no és bug de template. 33 de les 46 biblioteques tenien el camp `foto` apuntant a un duplicat exacte de `static/img/publicacions/biblioteques-cat.jpg` (bug d'importació). Només 2 tenien foto real (Sant Antoni, La Fraternitat); 11 ja no en tenien cap. Camp `foto` erroni tret de les 33 — passen a l'estat "sense foto" en lloc de mostrar la imatge incorrecta. Commit `eb76f92`. Importació de fotos de Xavi (149 noves) feta el 29-31 ago.
- ✅ Mercats: informació perduda — **no era pèrdua de dades, era bug de template**. `intervencions[].descripcio` mai es renderitzava a `elements/single.html` (només `tipus`/`autors`/`any`). Al Mercat de Felip II el "Projecte original: Estudi AGR..." hi era a les dades, no es mostrava mai. Bug del lloc sencer, no només mercats: **174 fitxes afectades** (23 mercats). `.descripcio` ja es mostra. Commit `e5a694b`.
- ✅ Biblioteques: imatges — **decisió Xavi (mail 31 ago 12:55)**: les fitxes que han quedat sense foto "no ens preocupen... de moment, ho deixem com està" (la foto mai ha estat prioritat de les guies; el debat és intern seu). Cap acció pendent per les sense foto. Documentat a `docs/2026-08-31-mail-xavi-resposta-import-fotos.md`.

### ⏳ Cal decisió (teva i/o de Xavi) abans d'aplicar

**Confirmat per Xavi (mail 2026-08-18) — implementat:**
- ✅ Jardins interiors d'illa: camp `obertura` → `any` (59 fitxes, script `rename-obertura.py`)
- ✅ Jardins interiors d'illa: `single.html` actualitzat per mostrar `any` en lloc d'`obertura`
- ⏳ Jardins interiors d'illa: separar text en seccions planes (Equipaments / Homenatge / + info) — **l'equip de Xavi ho farà ell** (mail 19 ago: "Ho poso a la llista de tasques nostres", encara no ha accedit a l'editor, no immediat). Format acordat: línies horitzontals amb títol gris + dada negra, no categories formals.
- ✅ Masies sense any: (a) segle extret del text → camp `any` (script `add-any-masies.py`) + (b) districte afegit via Nominatim + corregit a districtes oficials (168 fitxes)
- ✅ Biblioteques: districte afegit via Nominatim + corregit a districtes oficials (46 fitxes)
- ✅ Mercats: districte afegit via Nominatim + corregit a districtes oficials (39 fitxes)
- ✅ `term.html`: camp `districte` passat al JS, `LLISTAT_GRUP` condicional (masies/biblioteques/mercats → 'districte')
- ✅ `mapa.js`: agrupació per districte amb ordre oficial dels 10 districtes de Barcelona
- ✅ Fix acordió + posició llistat (2026-08-20): el commit d4c40fa va treure sense voler l'acordió de descripció i la injectació del llistat sota "## Llistat" a masies/biblioteques/mercats (la condició d'inici només cobria `grupPer === 'any'`). Corregit a `mapa.js` per cobrir també `'districte'`. Commit `1cfba79`.
- ✅ Mercats: agrupar per zona amb text introductori + desplegable per zona — **FET (2026-08-21)**: camp `zona` a les 42 fitxes + mode 'zona' al llistat. **Actualitzat 31 ao vespre amb la llista definitiva d'Xavi** (entrada #5 del REGISTRE): zones finals, camp `ordre` i sub-zones reordenades.
- ✅ Mercats: zones validades per Xavi (mail 2026-08-24): Tres Torres → **Sant Gervasi** ✓ | Bon Pastor → **Nou Barris** (canvi! estava a Sant Andreu) | Les Corts → **Nou Barris** (canvi! estava dins "Antics municipis" sense sub-grup) | Barceloneta i Born → Ciutat Vella ✓. Canvis aplicats a les fitxes (commit `4fdd097`, 29 ago). Nota (31 ago): el camp `zona` usa "Nous barris" (correcció d'usuari, commit `229d40d`); `districte` manté "Nou Barris" (nom oficial). **Xavi (mail 31 ago tarda): la forma visible correcta és "Nous barris"** — 🔴 pendent localitzar on es mostra "Nou Barris" i corregir (aprovació Joan).
- ✅ Mercats: sub-zones niuades dins el grup mare — resolt en dues fases: (1) acordions fills dins "Antics municipis" (commit `4fdd097`, 29 ago); (2) **llistat integrat amb el text explicatiu** (commit `ac21c18`, 31 ago): en mode `zona`, cada `<ul>` de mercats s'injecta sota l'encapçalament h3/h4 i el text explicatiu corresponent del `_index.md` (classe `.llistat-incrustat`, sense acordió propi). Els h4 de sub-zones queden dins la secció "Antics municipis" del text → estructura niuada natural. Fallback pels grups sense encapçalament al final. Modes `any`/`districte` (masies, biblioteques) mantenen el comportament anterior. Test jsdom: 23/23 + regressió masies OK.

**Pendent decisió — cal respondre a Xavi:**
- ⏳ Format intervencions (CaixaFòrum, Museu Picasso, CosmoCaixa): **Xavi respon (mail 2026-08-24)** — accepta usar el mecanisme d'intervencions ja existent. Cada edifici admet diverses intervencions cadascuna amb tipus, autors i any. Camps a mostrar: `Arquitectes` (tots els autors de totes les intervencions, clicables) + `Any` (tots els anys amb intervenció, números clicables → llistat de projectes de l'any — ampliació spec mail 31 ago) + `Projecte` (si no hi ha reforma; autors + any, no clicables) + `Projecte original` (si hi ha reforma; autors + any, no clicables) + `Reforma` (si hi ha reforma; autors + any, no clicables; pot aparèixer més d'una vegada si hi ha diverses reformes). Etiquetes flexibles per fitxa ("projecte", "reforma", "reforma i ampliació", "ampliació"...) — Xavi pregunta: automàtica o manual des de l'editor? Plural "arquitectes" també per a estudis (cas Bach-Mora: arquitectes = "Bach-Mora, Eugeni Bach, Gabriel Mora" tots clicables; projecte = "Bach-Mora" només). **Pendent: implementar** (spec completa: `docs/2026-08-31-mail-xavi-2-respostes-disseny.md`, punt 6).
- ✅ Camp `Any` a fitxes amb intervencions — **Xavi decideix opció 3 (mail 31 ago tarda)**: any d'ordenació invisible; per defecte el de la intervenció més recent; sobreescritible manualment des de l'editor. ⏳ Pendent: implementar.
- ✅ La Barceloneta — etiquetes Arquitectes/Artistes — **cas identificat (mail 31 ago tarda): Beverly Pepper**, autora del land-art "Sol i ombra" del **Parc de l'Estació del Nord** (`parc-de-lestacio-del-nord.md`, plànol 76-08; Arriola i Fiol, arquitectes). Xavi proposa mostrar alhora `Arquitectes` i `Autoria` (amb títol de l'obra). ⏳ Pendent de disseny i aprovació Joan.
- ✅ Districtes incerts: **confirmat per Xavi (2026-08-19)**: Canyelles → Nou Barris ✓, la Sagrera → Sant Andreu ✓. Ja estaven assignats així.
- ✅ Normalització arquitectes: ja aplicada (0 variants al contingut). Confirmat a Xavi.
- ✅ Helio Piñón: nom canònic **"Heliodoro Piñón Pallarés"** (decisió Xavi 19 ago) — aplicat 2026-08-21: pàgina curada renombrada i fusionada amb la taxonomia de les 4 fitxes.
- ⏳ Jardins interiors d'illa: **l'equip de Xavi ho farà ell** (mail 19 ago). Format: seccions planes amb línies horitzontals, títol gris + dada negra (no categories formals). No immediat.
- ✅ Formulari contacte: Xavi tria opció A (mailto:) fins al nou servidor. **FET (2026-08-21)**: secció "Correu directe" amb mailto info@elglobusvermell.org a /contacte/. El formulari s'activarà per SMTP a producció.

*Protocol general: per cada bloc "cal decisió", Joan/Xavi trien criteri → un cop clar, delegar l'extracció text→camps a una IA plànol a plànol (verificant mostra abans d'aplicar a tot el plànol) → `hugo build` + revisió visual → marcar fet. Xavi s'ofereix a fer comprovació exhaustiva fitxa per fitxa si cal.*

---

## Correu Xavi (31 ago, quatre mails) — fotos importades + disseny + mercats + reenvi Laia

Mails arxivats a `docs/2026-08-31-mail-xavi-resposta-import-fotos.md` (12:55), `docs/2026-08-31-mail-xavi-2-respostes-disseny.md` (tarda), `docs/2026-08-31-mail-xavi-3-mercats-zones.md` (vespre) i `docs/2026-08-31-mail-xavi-4-reenvi-respostes-laia.md` (mail 4: reenvia les respostes de la Laia a l'enquesta, original del 28 ago — marques confirmades per Joan: 1a 2a 3a 5a 6a 7b, 4 i 8 sense marca, 9 sí accés editora). Respostes de **Joan Vítoria** a l'enquesta: `docs/2026-08-31-mail-joan-vitoria-respostes.md` (marques confirmades per Joan el 31 ao nit: 1a 2a+b 3a 4c 5a 6c 7a 8a 9 sí + temes transversals i any clicable). Respostes de la **Mar**: `docs/2026-08-31-mail-mar-respostes-enquesta.md` (31 ago 18:16: 1a 2a 3 sense marca 4c 5e-CC-BY-NC 6 sense marca-inclina doble 7a+estendre 8c 9 sí + tots editors/2 admins; **observacions detallades del web PENDENTS** — el matxembrat per a Xavi s'hi espera). Fil dels mails del 19-24 ago recuperat i arxivat el 31 ao vespre (`docs/2026-08-19-mail-xavi-respostes.md`, `docs/2026-08-21-mail-xavi-ordre-manual.md`, `docs/2026-08-24-mail-xavi-respostes.md` — aquest últim és un dels "dos correus anteriors" amb la spec dels desplegables). El "mail del 28" d'Xavi = les seves respostes a l'enquesta (portada c, xifres a+b — decisions ja aplicades, cf. "Portada web" i "Xifres del projecte" més avall); text complet no arxivat. **Resposta de Joan a Xavi ENVIADA el 31 ao nit** (versió final de Joan, transcrita a `docs/esborrany-mail-resposta-xavi-31ago.md`, ara registre del mail enviat): sense el dubte Encants/Dominical a §3 (les dades es demanen a §7), §5 sense "Bones vacances!", tancament "Seguim quan tornis!" i firma LinuxBCN. Registre de canvis de fitxes i base de seguretat: `.ai/REGISTRE-CANVIS-FITXES.md`.

### Fet 31 ago ✅
- ✅ Importació de fotos completada (biblioteques + avantguarda, 29–31 ago); 326 fitxes amb foto
- ✅ Punt 0 (fitxes sense foto): decisió Xavi — es queden com estan, cap acció
- ✅ Investigació avantguarda amb els PDF de les dues edicions (2016: 47 ítems / reedició 2026: 43) — la numeració de la carpeta de fotos d'Xavi = reedició 2026. **Error nostre "#35 Rosselló 133" corregit**: el #35 és Enric Granados 133 i la fitxa existia. Creades `casa-roca-barallat.md` (#39, ítem nou de la reedició) i `casa-lluis-jara-urbano.md` (#38, Balmes 371, aprovada per Joan al vespre). `gatcpac` afegit a `fundacio-joan-miro.md` (#43) i `les-escales-park.md` (#42). gatcpac passa de 44 a 48 fitxes
- ✅ 4 ítems retirats del paper a la reedició 2026 (Botiga Cottet, àtic Provença 269, aula Química UB, convent CENU): fitxes MANTENGUDES al web (el web és font de veritat) — criteri Xavi pendent (preguntat al mail de resposta)
- ✅ **Desplegables del llistat de mercats: TANCAT** — Xavi el dona per bo ("ara ja apareixen com demanava. Gràcies!") després del deploy del commit `ac21c18`. L'acordió "Antics municipis" també
- ✅ **Fotos que retallen: corregit** (31 ao vespre) — `main.css`: proporció natural a `.fitxa-imatge` i `.fitxa-carrusel-slide` (tret aspect 1:1 + object-fit cover). Aprovat per Joan
- ✅ **"Nous barris" verificat**: totes les etiquetes de zona dels mercats ja la fan servir; "Nou Barris" (districte oficial) només apareix a l'agrupació per districte de masies/biblioteques, que es manté (Xavi: "no són districtes, més aviat són zones")
- ✅ **Google Maps API: el web no la fa servir** als mapes interactius (Leaflet + OpenStreetMap, sense clau). ⚠️ **Correcció (31 ao, mail 4 — Laia): l'enllaç extern de l'adreça de cada fitxa sí que va a Google Maps** (`single.html:135`, `https://maps.google.com/?q=` + **text** de l'adreça, sense clau d'API), amb un **bug detectat per Laia**: des de fora de BCN el text es resol malament ("Praga 5" → la ciutat de Praga). Correcció tècnica: enllaç per `lat,long` quan existeixin — és bug, no decisió de disseny; pendent decisió Joan si es fa abans del consens de l'enquesta. La clau era per a l'app Flutter antiga → al mail: proposar flutter_map/OSM a l'app nova
- ✅ **Paquet mercats aplicat** (31 ao vespre, aprovat per Joan via questionari; entrada #5 del REGISTRE): `zona` → "Nous barris" a 11 fitxes, camp `ordre` a les 42 fitxes (ordre del PDF; La Marina ×2 ordre 9, Bellcaire ordre 4 reservant 2-3 pels de Sant Antoni, Sant Gervasi ordre 3), creada `flors-de-la-rambla.md` **sense lat/long** (al llistat, sense punt al mapa), sub-zones reordenades (Sant Martí de Provençals abans d'Horta al `_index.md` i als arrays de `mapa.js`), `mapa.js` ordena per `ordre` amb desempat alfabètic, `term.html` passa el camp. Script: `scripts/mercats-zones-ordre.py`. Verificat al build: 43 elements de mercats al llistat, 42 punts al mapa
- ✅ **Deploy verificat en línia** (31 ao nit, github.io): `flors-de-la-rambla` 200, `casa-lluis-jara-urbano` 200, enllaç Boqueria per coords (`?q=41.38168,2.17159`) ✓. Tots els runs del dia `success`
- ✅ **Encants/Dominical verificats contra el WP mare** (`docs/2026-08-31-verificacio-mercats-no-alimentaris-wp.md`): només falten els dos de Sant Antoni (no existeixen enlloc); la Fira de Bellcaire hi era (WP + Hugo, ordre 4 correcte)
- ✅ **Mail de resposta a Xavi ENVIAT** (31 ao nit, versió final de Joan — registre a `docs/esborrany-mail-resposta-xavi-31ago.md`): queden pendents d'Xavi en tornar (~16 set) els dubtes de mercats (Sant Gervasi, Marina, dades Encants/Dominical), el mail del 28 sencer i les decisions de l'enquesta

### Pendent decisió Joan 🔴 (protocol REGISTRE-CANVIS-FITXES.md)
- 🔴 Crear fitxes **Encants de Sant Antoni** i **Dominical de Sant Antoni** (Xavi les cita; no existeixen — **verificat 31 ao nit: tampoc al WP mare** i l'Encants–Fira de Bellcaire SÍ que hi és amb ordre 4 correcte, `docs/2026-08-31-verificacio-mercats-no-alimentaris-wp.md`). Dades demanades a Xavi al mail enviat (§7); torna ~16 set
- 🔴 Duplicat `mercat-de-la-marina` + `placa-i-mercat-de-la-marina` (Xavi només llista "La Marina" un cop; el duplicat ja venia del WP mare — preguntat al mail enviat §3/§7)
- 🔴 Duplicats de migració: Navas 238+240 (+`edifici-dhabitatges-carrer-navas` invisible), `casa-unifamiliar-placa-mons` (+ `casa-unifamiliar` invisible), Pavelló (`biblioteca-crai-ub` visible amb frontmatter malmès vs `de-1937-replica` correcta però sense publicacions)
- ✅ ~~5 fitxes amb `publicacions` buit~~ — verificat 1 set (verificació diària de números): les 660 fitxes tenen `publicacions` amb contingut; l'entrada era desactualitzada. Els duplicats de migració de la línia anterior segueixen pendents

### Punts del mail 2 (disseny) pendents 🔴
- 🔴 Camp intervencions i etiquetes: spec definitiva confirmada (files corresponents a "Cal decisió"); preguntes obertes d'Xavi: etiquetes automàtiques o manuals, plural per a estudis — respostes al mail de tornada; **implementació pendent d'aprovació Joan**
- ⏳ Xifra "any" (portada/Presentació): Xavi pensa treure-la (el 1928 no és correcte, hi ha masies anteriors) — decisió interna Globus pendent
- ⏳ 73 arquitectes combinats: Xavi ho té pendent ("altres coses se m'han anat posint al davant")
- 🔴 3 fitxes curades d'arquitecte **òrfenes** (`albert-viaplana`, `toyo-ito`, `oab-(carlos-ferrater)`): el títol no coincideix amb el nom que usen les fitxes («Albert Viaplana i Veà», «Toyo Ito Associates», «OAB (Carlos Ferrater)») → cap edifici les enllaça i es generen pàgines de terme duplicades (276 pàgines vs 274 arquitectes). Trobat 1 set amb la verificació diària; tractar amb Xavi junt amb els 73

### Respostes de l'equip a l'enquesta — NO implementar sense consens 🔴
Instrucció de Joan (31 ao): "de moment no implementem res del que diu, esperarem a tenir consens
de l'equip del Globus Vermell o pararem bojos". Docs: `docs/2026-08-31-mail-xavi-4-reenvi-respostes-laia.md`
(Laia), `docs/2026-08-31-mail-joan-vitoria-respostes.md` (Joan Vítoria) i
`docs/2026-08-31-mail-mar-respostes-enquesta.md` (Mar).

**Estat (31 ao nit): els 4 membres han contestat** (Xavi parcialment constatat). ⚠️ La Mar està
revisant el web en detall i **enviarà observacions addicionals** — el matxembrat/resum per a Xavi
s'ha d'esperar (com ella mateixa suggereix).

| Pregunta | Xavi (28 ago)* | Laia (28 ago) | Joan Vítoria (31 ago) | Mar (31 ago) |
|---|---|---|---|---|
| 1 Colors | ? | a mantenir | a mantenir | **a mantenir** |
| 2 Portada | c (esc. nova + mòbil mapa) — implementat | a nova proposta | a i b (indecís) | **a nova proposta + mateix plantejament pc i mòbil** ⚠️ |
| 3 Xifres | a+b (portada + Presentació) | a portada | a portada | **sense marca** (qüestiona el missatge; propostes alternatives) |
| 4 Llicència | ? | sense marca | c BY-SA (ja al footer, `5732d72`) | **c BY-SA** (oberta a BY-NC) |
| 5 Fotos | ? | a © EGV | a © EGV (dubte: on mostrar-ho) | **e CC BY-NC** (opció afegida per ella) + nom d'arxiu/meta amb "elglobusvermell" |
| 6 Mapes adreça | ? | a Google | c doble opció | **sense marca** (inclina doble, reserva del clic extra) |
| 7 Veu alta | ? | b Piper **si llegeix català** | a actual suficient | **a actual** + estendre-la a les descripcions dels plànols-guia |
| 8 Estadístiques | ? | sense marca | a privat (ja està així) | **c indiferent** (inclina privat) |
| 9 CMS | ? | sí (laiabrelglobusvermell-design) | sí (demana instruccions) | **sí** + tot l'equip editors, 2 administradors (una + reserva) |

\* El mail del 28 d'Xavi no està arxivat sencer; només consten portada c i xifres a+b (aplicades).
**Conflictes a resoldre al consens:** 2 portada (Xavi c implementat vs. Laia/JV/Mar pro-nova; la
Mar demana el mateix plantejament a pc i mòbil, contrari al "mòbil→mapa" d'Xavi), 3 xifres (Mar
qüestiona "importa la quantitat?"; propostes JV+Laia+Mar divergents), 5 fotos (© EGV vs CC BY-NC
de la Mar), 6 mapes (Google vs doble), 7 veu alta (2-1 per l'actual, Laia condiciona Piper).
**Convergències:** 1 colors mantenir (unànime), 4 BY-SA, 8 privat, 9 tots editors.
**Peticions noves de la Mar:** veu alta també a les descripcions dels plànols-guia; crèdit
"elglobusvermell" al nom d'arxiu o metadades de les imatges descarregades; 2 administradors al CMS.

**Accions no bloquejades pel consens:**
- ✅ **Bug enllaç adreça (Praga 5 → Praga)**: CORREGIT 31 ao nit (aprovat per Joan) — `single.html` enllaça per `lat,long` quan existeixen (fallback text + "barcelona"); verificat al build
- 🟢 **Accés CMS Laia, JV i Mar**: tots tres volen accés d'editora (compte GitHub de la Laia: laiabrelglobusvermell-design; els de JV i Mar pendents de demanar) — **instruccions enviades l'1 set** (mail PAS a PAS + rectificatiu del token); **esperem els noms d'usuari per verificar-los a GitHub i convidar (rol Write)**; la Mar proposa 2 administradors (decisió d'equip)
- 🔴 Botons "(Web oficial)" i "(COAC)" de la pàgina d'arquitecte gairebé invisibles → fons gris clar (proposta Laia) — consens
- 🔴 Respondre a Laia: per què alguns colors de guia difereixen del paper (ex. La Marina) — cal investigar l'origen
- ⏳ Portada/xifres: millores proposades per Laia (franja estreta + portades de guies; botó "explorar guies"), labels de JV ("Guies temàtiques", "Període arquitectònic", inici 1400) i alternatives de la Mar (plànol immens + títol gegant zoom Catalunya; o títol + descripció) — a estudiar amb el consens

---

## Decisions — respostes Xavi (2026-08-17)

Respostes arxivades a `.ai/RESPOSTES-XAVI-2026-08-17.md`

- ✅ Preparar mail de decisions amb totes les preguntes pendents (9 punts en 4 blocs)
- ✅ Enviat a xavirg@elglobusvermell.org el 2026-08-11
- ✅ Respostes rebudes el 2026-08-17 — arxivades a `.ai/RESPOSTES-XAVI-2026-08-17.md`
- ✅ GitHub Xavi: invitació admin a `xavirg` **cancel·lada (2026-08-18)** — resulta ser un compte GitHub alié ("Javi Rodriguez", coincidència de nom d'usuari amb l'email `xavirg@elglobusvermell.org`). Xavi ja tenia accés real amb un altre compte (`xaviglobus`, rol editor/push). Provat pujar `xaviglobus` a admin: no ha estat possible (limitació de GitHub) — **conclusió: no cal rol admin per a les tasques d'edició de continguts de Xavi**, l'accés d'editor ja és suficient.
- ✅ Correu de Xavi (18 ago, 12:26) amb correccions del diccionari d'arquitectes + confirmació punts desubicats — revisat, aplicat i respost (`docs/esborrany-mail-confirmacio-arquitectes-punts-18ago.md`, enviat)
- ✅ Correu de Xavi (18 ago, 12:46) amb dubtes d'accés al CMS ("Javi Rodríguez", login penjat) — respost explicant l'error de compte, ús del PAT i contingut del hub `/admin/` (`docs/esborrany-mail-acces-cms-18ago.md`, enviat)

### Confirmats per Xavi ✅
- ✅ Signatura LinuxBCN al peu del web públic — aprovada per Xavi
- ✅ Citar COAC i Viquipèdia a pàgina de Crèdits — implementat a `content/ca/credits/_index.md` (secció "Fonts de dades")
- ✅ © + CC BY-SA 4.0 simultàniament al peu
- ✅ Nova portada (hero + guia i arquitecte aleatoris)
- ✅ Arquitectes al menú principal
- ✅ Peu de pàgina reorganitzat (Crèdits al peu, Contacte al menú)
- ✅ Formulari de contacte (rep correu)
- ⏳ Configurar enviament formulari per SMTP — Google Workspace o servidor de producció (Dinahosting). Fer al final del projecte, quan el servidor estigui definit. Afegir opció mailto: visible a la pàgina /contacte/ com a alternativa directa.
- ✅ New Babylon/Tàpies: sense punts al mapa, presència a "en paper"/portada
- ✅ Fotos: penjar directament al nou web (sense WordPress)
- ✅ PWA — instal·lar al mòbil: pàgina `static/admin/instal-la-al-mobil/` creada i targeta afegida al hub `/admin/`
- ⏳ Estudiar si exposar les instruccions d'instal·lació al web públic (ara només a /admin/). Podria ser útil per als visitants. Cal decidir on: peu de pàgina, /ajuda/, banner discret... Pendent de decisió.

### Pendents de consens ⏳
- ✅ Colors web: **opció a — mantenir colors actuals per guia** (Xavi, mail 2026-08-28). Queda oberta la pregunta de quin color mostrar als edificis que pertanyen a diversos plànols alhora. **Pendent de decidir i implementar.**
- ✅ Portada web: **opció c — nova portada en escriptori; mapa directe en mòbil** (Xavi, mail 2026-08-28; reconfirmat "Sí" al mail del 31 ago tarda). Implementat (commit `6b30c4f`, 31 ago): script inline al `head.html` (només `.IsHome`) amb `matchMedia('(max-width: 48rem)')` → `location.replace('mapa/')`, sense entrada a l'historial. La portada nova d'escriptori espera el consens de l'equip sobre l'enquesta: **els 4 membres han respost** (Xavi 28 ago, Laia 28 ago reenviades el 31, JV 31 ago, Mar 31 ago). ⚠️ La Mar enviarà observacions detallades del web (el resum/matxembrat per a Xavi s'hi espera). Conflicte viu: Xavi c (implementat) vs. Laia/JV/Mar pro-nova proposta; la Mar vol el mateix plantejament a pc i mòbil (contrari al "mòbil→mapa" d'Xavi). **Res no s'implementa fins a consens** (instrucció Joan 31 ao).
- ✅ Xifres del projecte: **opcions a+b — tant a portada com a Presentació** (Xavi, mail 2026-08-28). Ajustos implementats (commit `4fdd097`, 29 ago): anyMin = 1928 a Presentació (alineat amb portada), 2a fila de xifres suprimida. Comptabilitzar elements de temes transversals: pendent de consens.
- ✅ Llicència peu de pàgina: **CC BY-SA 4.0** confirmada per Xavi (mail 2026-08-28) — "és el que posem a les guies". Ja implementada al peu.
- ✅ Crèdit fotografies: **CC-BY-SA 4.0, "El Globus Vermell"** per a totes les fotos — no hi ha crèdit individual per fotògraf/a (Xavi, mail 2026-08-28). Implementat a `elements/single.html` (commit `4fdd097`, 29 ago).
- ✅ Mapes (adreça edifici): **opció a preferida (Google Maps), opció c (doble botó) també acceptable** (Xavi, mail 2026-08-28). Enllaç Google Maps implementat a l'adreça de la fitxa (commit `4fdd097`, 29 ago).
- ✅ TTS/Lectura en veu alta: **opció a — versió actual (Web Speech API) suficient** (Xavi, mail 2026-08-28). Documentat (commit `4fdd097`, 29 ago): "Web Speech API" a Crèdits/Tecnologia + "Lectura en veu alta de les fitxes" a Accessibilitat/Mesures aplicades.
- ✅ GoatCounter estadístiques: **opció c — indiferent** (Xavi, mail 2026-08-28). Mantenim privat (accés Joan + Xavi) fins nova decisió.
- ✅ CMS — accés Xavi: **vol ser administrador/a** (Xavi, mail 2026-08-28). Compte `xaviglobus` ja té accés editor. **Explorat l'1 set:** GitHub no ofereix rols diferenciats (admin/mantenidor/...) en repos de compte personal. L'alternativa és **migrar el repo a una organització** — donaria rols i, a més, els tokens fine-grained funcionarien per a tothom — però canvia l'URL `github.io` → **es valora amb el tall del domini, no abans**. Mentrestant, el token clàssic del mail rectificatiu funciona per a tots els convidats
- ✅ Camp "Projecte" a fitxes: **Xavi (mail 31 ago tarda): NO s'elimina** ("anem enrere"; no descarta eliminar-lo o amagar-lo més endavant). Es manté segons la spec d'intervencions.
- ⏳ Xavi: revisió llista arquitectes (73 combinats + normalització) — havia dit "aquesta setmana"
- ⏳ Xavi: criteris arquitectes vs estudis (Eugeni Bach, Soldevila...)
- ⏳ Arxiu Històric BCN: explorar col·laboració per fotos — iniciativa de Xavi, no urgent

---

## Pendents client (preguntes per Xavi / Jorge)

- 🔴 Jorge: dades d'accés al servidor actual
- ✅ Pressupost 3.900€ — **acceptat i 50% ja pagat** (Joan, 1 set). L'app Flutter queda desbloquejada finançament; s'iniciarà després de Rendiment i Seguretat
- ✅ Xavi: accés a guiesbarcelona.elglobusvermell.org — ja té accés (rol editor, compte `xaviglobus`); invitació admin errònia cancel·lada, no calia
- ✅ Xavi: clarificació "filtrar per publicacions" al mapa
- ✅ Xavi: decisió de disseny (colors publicació vs nou rebrand) — **colors per guia confirmats** (mail 2026-08-28)
- ⏳ Xavi: confirmar esquema de "En paper" (portada + botó PDF)
- ✅ Xavi: llicència del peu de pàgina — CC BY-SA 4.0 confirmada (mail 2026-08-28)
- ~~⏳ Xavi: confirmar contrasenya admin backoffice~~ — obsolet, ja no hi ha protecció per contrasenya al GitHub Pages de proves (comprovat 18 ago)
