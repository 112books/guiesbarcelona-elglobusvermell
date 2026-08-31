# TASKS.md — Llista de tasques

Llegenda: ✅ Fet | 🔄 En curs | ⏳ Pendent | 🔴 Bloquejat (espera info externa)

---

## Web guies (guiesbarcelona.elglobusvermell.org)

### Infraestructura
- ✅ Repositori GitHub + deploy automàtic a GitHub Pages
- ✅ Dominis: funcionant a https://112books.github.io/guiesbarcelona-elglobusvermell/
- ⏳ Configurar domini propi guiesbarcelona.elglobusvermell.org a GitHub Pages (espera control del domini)

### Contingut
- ✅ Importació de 66 edificis des del dump SQL (7 publicacions)
- ✅ Pàgina Presentació
- ✅ Pàgina En paper (13 publicacions)
- ✅ Pàgina Crèdits (amb LinuxBCN)
- 🔴 Importació de les 564 entrades del WordPress real (espera accés servidor Jorge)
- 🔴 Imatges dels edificis (espera accés servidor Jorge)
- ⏳ Geocodificació automàtica dels edificis sense coordenades
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
- ⏳ Verificar CMS a GitHub Pages amb PAT de prova
- ⏳ Invitar compte GitHub Globus Vermell al repo (rol: Write)
- ⏳ Guia ràpida per a editors: crear PAT i accedir al CMS

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
- ⏳ **Crèdits → Tecnologia**: afegir entrada de la tecnologia TTS un cop confirmada l'opció (Web Speech API o Piper TTS)
- ⏳ **Accessibilitat → Mesures aplicades**: afegir "Lectura en veu alta de les fitxes d'edifici (text a veu)" i "Peu de foto amb text descriptiu (alt text)" un cop confirmada la implementació definitiva
- ⏳ **Accessibilitat → Tecnologia**: afegir la tecnologia TTS usada (Web Speech API del navegador o Piper TTS)
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

### Pendent — accessibilitat (informe: 6-8h estimades)
- ⏳ Contrast insuficient: `.footer-powered-link` (#b3b3b3 → #6b6b6b), `::placeholder` (#aaa → #767676) — `main.css:302,532`
- ⏳ Carrusel: `keydown` ArrowLeft/ArrowRight, dots 44px, `aria-pressed` als dots — `fitxa.js:45-90`
- ⏳ Focus visible filtres mapa: `:focus-visible` explícit a `.filtre-btn`, `.filtre-lateral` — `main.css:~550`
- ⏳ Botó "i" de publicació: substituir per SVG + `sr-only` — `mapa.js:451-466`
- ⏳ Carrusel: indicador "Diapositiva N de M" per a sr-only
- ⏳ Skip link `<a href="#main">` a `baseof.html`
- ⏳ `aria-current="page"` al menú de navegació actiu

### Pendent — seguretat (informe)
- ⏳ URL `?tema=` whitelist explícita — `mapa.js:46-49` (2 línies de codi)
- ⏳ CMS auth: OAuth GitHub App (Fase 1, ja prevista)
- ⏳ `analytics.json` públic: restringir o eliminar un cop migrat a Vercel/Netlify
- ⏳ `unsafe=true` Markdown: avaluar si es pot desactivar (`config/_default/hugo.toml`)

### Pendent — rendiment (informe)
- ⏳ **Imatges WebP** — conversió batch de 880 MB d'imatges originals a WebP (<200 KB/foto). Impacte crític: LCP de >4s a <2,5s. Comanda: `cwebp -q 82 + mogrify -resize 1200>`
- ⏳ `width`/`height` a `<img>` de fitxes — evitar CLS — `elements/single.html`
- ⏳ Leaflet.min.js en lloc de leaflet.js — `static/vendor/leaflet/` (~42 KB vs 147 KB)
- ⏳ Verificar sitemap.xml a producció (build `--environment production`)

### Pendent — SEO (informe)
- ⏳ Google Search Console — activar quan el domini de producció estigui llest
- ⏳ `hreflang` — preparar quan s'activin EN/ES
- ⏳ Auditar `envia.php` — validació CSRF, sanitització (RGPD + seguretat)

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

## Correu Xavi (31 ago, tres mails) — fotos importades + disseny + mercats

Mails arxivats a `docs/2026-08-31-mail-xavi-resposta-import-fotos.md` (12:55),
`docs/2026-08-31-mail-xavi-2-respostes-disseny.md` (tarda) i `docs/2026-08-31-mail-xavi-3-mercats-zones.md` (vespre). Fil dels mails del 19-24 ago recuperat i arxivat el 31 ao vespre (`docs/2026-08-19-mail-xavi-respostes.md`, `docs/2026-08-21-mail-xavi-ordre-manual.md`, `docs/2026-08-24-mail-xavi-respostes.md` — aquest últim és un dels "dos correus anteriors" amb la spec dels desplegables); **falta el mail del 28 ago** (l'altre). Registre de canvis de fitxes i base de seguretat: `.ai/REGISTRE-CANVIS-FITXES.md`.

### Fet 31 ago ✅
- ✅ Importació de fotos completada (biblioteques + avantguarda, 29–31 ago); 326 fitxes amb foto
- ✅ Punt 0 (fitxes sense foto): decisió Xavi — es queden com estan, cap acció
- ✅ Investigació avantguarda amb els PDF de les dues edicions (2016: 47 ítems / reedició 2026: 43) — la numeració de la carpeta de fotos d'Xavi = reedició 2026. **Error nostre "#35 Rosselló 133" corregit**: el #35 és Enric Granados 133 i la fitxa existia. Creades `casa-roca-barallat.md` (#39, ítem nou de la reedició) i `casa-lluis-jara-urbano.md` (#38, Balmes 371, aprovada per Joan al vespre). `gatcpac` afegit a `fundacio-joan-miro.md` (#43) i `les-escales-park.md` (#42). gatcpac passa de 44 a 48 fitxes
- ✅ 4 ítems retirats del paper a la reedició 2026 (Botiga Cottet, àtic Provença 269, aula Química UB, convent CENU): fitxes MANTENGUDES al web (el web és font de veritat) — criteri Xavi pendent (preguntat al mail de resposta)
- ✅ **Desplegables del llistat de mercats: TANCAT** — Xavi el dona per bo ("ara ja apareixen com demanava. Gràcies!") després del deploy del commit `ac21c18`. L'acordió "Antics municipis" també
- ✅ **Fotos que retallen: corregit** (31 ao vespre) — `main.css`: proporció natural a `.fitxa-imatge` i `.fitxa-carrusel-slide` (tret aspect 1:1 + object-fit cover). Aprovat per Joan
- ✅ **"Nous barris" verificat**: totes les etiquetes de zona dels mercats ja la fan servir; "Nou Barris" (districte oficial) només apareix a l'agrupació per districte de masies/biblioteques, que es manté (Xavi: "no són districtes, més aviat són zones")
- ✅ **Google Maps API: el web NO la fa servir** (verificat al codi: Leaflet + OpenStreetMap; l'única referència és un text d'ajuda de l'admin). La clau era per a l'app Flutter antiga → resposta al mail: proposar mapes lliures (flutter_map/OSM) a l'app nova; cap urgència llevat que l'app antiga hagi de seguir funcionant
- ✅ **Paquet mercats aplicat** (31 ao vespre, aprovat per Joan via questionari; entrada #5 del REGISTRE): `zona` → "Nous barris" a 11 fitxes, camp `ordre` a les 42 fitxes (ordre del PDF; La Marina ×2 ordre 9, Bellcaire ordre 4 reservant 2-3 pels de Sant Antoni, Sant Gervasi ordre 3), creada `flors-de-la-rambla.md` **sense lat/long** (al llistat, sense punt al mapa), sub-zones reordenades (Sant Martí de Provençals abans d'Horta al `_index.md` i als arrays de `mapa.js`), `mapa.js` ordena per `ordre` amb desempat alfabètic, `term.html` passa el camp. Script: `scripts/mercats-zones-ordre.py`. Verificat al build: 43 elements de mercats al llistat, 42 punts al mapa

### Pendent decisió Joan 🔴 (protocol REGISTRE-CANVIS-FITXES.md)
- 🔴 Crear fitxes **Encants de Sant Antoni** i **Dominical de Sant Antoni** (Xavi les cita; no existeixen; falten dades)
- 🔴 Duplicat `mercat-de-la-marina` + `placa-i-mercat-de-la-marina` (Xavi només llista "La Marina" un cop)
- 🔴 Duplicats de migració: Navas 238+240 (+`edifici-dhabitatges-carrer-navas` invisible), `casa-unifamiliar-placa-mons` (+ `casa-unifamiliar` invisible), Pavelló (`biblioteca-crai-ub` visible amb frontmatter malmès vs `de-1937-replica` correcta però sense publicacions)
- 🔴 5 fitxes amb `publicacions` buit (invisibles al mapa): casa-unifamiliar, edifici-dhabitatges-carrer-navas, jardins-ada-byron, pavello-de-la-republica-de-1937-replica, placa-dolors-piera-isabel-vila

### Punts del mail 2 (disseny) pendents 🔴
- 🔴 Camp intervencions i etiquetes: spec definitiva confirmada (files corresponents a "Cal decisió"); preguntes obertes d'Xavi: etiquetes automàtiques o manuals, plural per a estudis — respostes al mail de tornada; **implementació pendent d'aprovació Joan**
- ⏳ Xifra "any" (portada/Presentació): Xavi pensa treure-la (el 1928 no és correcte, hi ha masies anteriors) — decisió interna Globus pendent
- ⏳ 73 arquitectes combinats: Xavi ho té pendent ("altres coses se m'han anat posint al davant")

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
- ✅ Portada web: **opció c — nova portada en escriptori; mapa directe en mòbil** (Xavi, mail 2026-08-28; reconfirmat "Sí" al mail del 31 ago tarda). Implementat (commit `6b30c4f`, 31 ago): script inline al `head.html` (només `.IsHome`) amb `matchMedia('(max-width: 48rem)')` → `location.replace('mapa/')`, sense entrada a l'historial. La portada nova d'escriptori espera les respostes de l'enquesta de l'equip (Xavi ja ha respost; els altres "els pròxims dies", termini el 4 de setembre).
- ✅ Xifres del projecte: **opcions a+b — tant a portada com a Presentació** (Xavi, mail 2026-08-28). Ajustos implementats (commit `4fdd097`, 29 ago): anyMin = 1928 a Presentació (alineat amb portada), 2a fila de xifres suprimida. Comptabilitzar elements de temes transversals: pendent de consens.
- ✅ Llicència peu de pàgina: **CC BY-SA 4.0** confirmada per Xavi (mail 2026-08-28) — "és el que posem a les guies". Ja implementada al peu.
- ✅ Crèdit fotografies: **CC-BY-SA 4.0, "El Globus Vermell"** per a totes les fotos — no hi ha crèdit individual per fotògraf/a (Xavi, mail 2026-08-28). Implementat a `elements/single.html` (commit `4fdd097`, 29 ago).
- ✅ Mapes (adreça edifici): **opció a preferida (Google Maps), opció c (doble botó) també acceptable** (Xavi, mail 2026-08-28). Enllaç Google Maps implementat a l'adreça de la fitxa (commit `4fdd097`, 29 ago).
- ✅ TTS/Lectura en veu alta: **opció a — versió actual (Web Speech API) suficient** (Xavi, mail 2026-08-28). Documentat (commit `4fdd097`, 29 ago): "Web Speech API" a Crèdits/Tecnologia + "Lectura en veu alta de les fitxes" a Accessibilitat/Mesures aplicades.
- ✅ GoatCounter estadístiques: **opció c — indiferent** (Xavi, mail 2026-08-28). Mantenim privat (accés Joan + Xavi) fins nova decisió.
- ✅ CMS — accés Xavi: **vol ser administrador/a** (Xavi, mail 2026-08-28). Compte `xaviglobus` ja té accés editor; cal explorar si GitHub permet pujar a admin en repos personals o si cal alternativa. **Pendent.**
- ✅ Camp "Projecte" a fitxes: **Xavi (mail 31 ago tarda): NO s'elimina** ("anem enrere"; no descarta eliminar-lo o amagar-lo més endavant). Es manté segons la spec d'intervencions.
- ⏳ Xavi: revisió llista arquitectes (73 combinats + normalització) — havia dit "aquesta setmana"
- ⏳ Xavi: criteris arquitectes vs estudis (Eugeni Bach, Soldevila...)
- ⏳ Arxiu Històric BCN: explorar col·laboració per fotos — iniciativa de Xavi, no urgent

---

## Pendents client (preguntes per Xavi / Jorge)

- 🔴 Jorge: dades d'accés al servidor actual
- ⏳ Xavi: confirmar pressupost 3.900€
- ⏳ Xavi: 50% de bestreta per iniciar Flutter
- ✅ Xavi: accés a guiesbarcelona.elglobusvermell.org — ja té accés (rol editor, compte `xaviglobus`); invitació admin errònia cancel·lada, no calia
- ✅ Xavi: clarificació "filtrar per publicacions" al mapa
- ✅ Xavi: decisió de disseny (colors publicació vs nou rebrand) — **colors per guia confirmats** (mail 2026-08-28)
- ⏳ Xavi: confirmar esquema de "En paper" (portada + botó PDF)
- ✅ Xavi: llicència del peu de pàgina — CC BY-SA 4.0 confirmada (mail 2026-08-28)
- ~~⏳ Xavi: confirmar contrasenya admin backoffice~~ — obsolet, ja no hi ha protecció per contrasenya al GitHub Pages de proves (comprovat 18 ago)
