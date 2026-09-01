# Registre de canvis de fitxes i punts dels mapes

**Regla de governança (aprovada per Joan, 31 ago 2026):** cap creació, esborrat o modificació
de fitxes o punts dels mapes sense **aprovació expressa de Joan** i entrada a aquest registre.
El web actual (Hugo) és la **font de veritat** de les dades; el WordPress antic i els plànols
en paper són referència històrica i mai no "corregeixen" el web sense aprovació.

Cada entrada del registre porta: data, canvi exacte (fitxa i camp), font de dades i
referència de l'aprovació. Davant dubte: **es pregunta primer, no es fa**.

---

## Base de seguretat — recompte (31 ago 2026, abans dels canvis d'avui)

- **Total fitxes:** 658 (657 elements + `_index`)
- **Fitxes amb foto:** 326
- **Recompte per publicació (plànol):**

| Publicació | Fitxes |
|---|---|
| 09-25 | 59 |
| 50-75 | 86 |
| 76-08 | 73 |
| barceloneta | 62 |
| biblioteques | 50 |
| gatcpac | 44 |
| interiors-illa | 79 |
| marina | 20 |
| masies | 88 |
| mercats | 42 |
| poblenou | 77 |
| new-babylon / tapies | 0 (cap fitxa els té com a publicació) |

**Fitxes amb `publicacions` buit (invisibles a tots els plànols):**
`casa-unifamiliar`, `edifici-dhabitatges-carrer-navas`, `jardins-ada-byron`,
`pavello-de-la-republica-de-1937-replica`, `placa-dolors-piera-isabel-vila`.

---

## Registre de canvis

| # | Data | Canvi | Font de dades | Aprovació |
|---|---|---|---|---|
| 1 | 2026-08-31 | Creada `content/ca/elements/casa-roca-barallat.md` — Casa Roca Barallat, Via Augusta 12, Carles Martínez Sánchez, 1935; coords 41.3967221 / 2.1551607 (Nominatim, validat: Via Augusta 61 OSM coincideix amb fitxa Rodriguez Arias a ~3 m); `publicacions: [gatcpac]` (ítem #39 reedició 2026) | PDF reedició 2026 *Arquitectura d'avantguarda* + Nominatim OSM | Joan, 31 ago: "Arregla doncs les fitxes que comenta en XAVI" (Xavi la cita com a pendent de crear) |
| 2 | 2026-08-31 | Afegida `- gatcpac` a `publicacions` de `fundacio-joan-miro.md` (ítem #43 avantguarda, present a les edicions 2016 #46 i 2026 #43) | PDF edicions 2016 i 2026 | Joan, mateixa instrucció |
| 3 | 2026-08-31 | Afegida `- gatcpac` a `publicacions` de `les-escales-park.md` (ítem #42 avantguarda, present a les edicions 2016 #47 i 2026 #42) | PDF edicions 2016 i 2026 | Joan, mateixa instrucció |
| 4 | 2026-08-31 | Creada `content/ca/elements/casa-lluis-jara-urbano.md` — Casa Lluís Jara Urbano, C. de Balmes 371, Josep Soteras Mauri, 1935 (reedició 2026; l'edició 2016 deia 1936); coords 41.4045422 / 2.1403092 (Nominatim, validat: Balmes 166 OSM coincideix amb fitxa existent a ~12 m); `publicacions: [gatcpac]` (ítem #38 de les dues edicions) | PDF reedició 2026 *Arquitectura d'avantguarda* + Nominatim OSM | Joan, 31 ago vespre: "Sí, crea-la" (questionari de decisions) |
| 5 | 2026-08-31 | **Paquet mercats** segons la llista definitiva d'Xavi: (a) `zona` → "Nous barris" a **11 fitxes** (Guinardó, Carmel, Vall d'Hebron–Teixonera, Estrella, Lesseps, Felip II, Provençals, Sant Martí, Besòs, La Marina ×2) via `scripts/mercats-zones-ordre.py`; (b) camp **`ordre`** (posició al PDF dins de cada zona) a les 42 fitxes de mercats — La Marina duplicada ordre 9 totes dues, Encants–Fira de Bellcaire ordre 4 (reserva 2-3 pels de Sant Antoni), Sant Gervasi ordre 3 (dubte pendent); (c) creada `content/ca/elements/flors-de-la-rambla.md` — **sense lat/long** (surts al llistat, sense punt al mapa, tal com demanava Xavi), descripció textual del plànol; (d) reordenades sub-zones: Sant Martí de Provençals abans d'Horta (`_index.md` + `ORDRE_ZONES_MERCATS` + `SUB_ZONES_ANTICS_MUNICIPIS`); (e) `mapa.js`: ordenació dins de zona pel camp `ordre` (desempat alfabètic) + `term.html` passa el camp | Mail Xavi 31 ago vespre (`docs/2026-08-31-mail-xavi-3-mercats-zones.md`), llista amb ordre del PDF | Joan, 31 ago vespre: "Sí, aplica'l ara" + "Fitxa sense punt" (questionari de decisions) |

**Estat després dels canvis 1-5:** total 661 fitxes; gatcpac 48 elements; mercats 43 (42 amb punt + Flors de la Rambla sense).

### Canvis de visualització aprovats (no toquen dades de fitxes)

| Data | Canvi | Aprovació |
|---|---|---|
| 2026-08-31 | `main.css`: fotos de fitxa (sola i carrusel) amb **proporció natural** — tret l'`aspect-ratio: 1/1` i l'`object-fit: cover` que retallaven les fotos noves (~127:110 els últims 5 plànols). Bug denunciat per Xavi (mail 2 del 31 ago, punt 5) | Joan, 31 ago vespre: "Fotos que retallen" (questionari) |
| 2026-08-31 | `single.html`: **bug de l'enllaç extern de l'adreça** — abans `https://maps.google.com/?q=` + text de l'adreça (des de fora de BCN obria llocs equivocats: "Praga 5" → Praga; detectat per Laia Borau, mail del 28 ago); ara enllaça per `lat,long` quan existeixen (fallback: text + "barcelona"). La plataforma (Google/OSM/doble) segueix pendent de l'enquesta | Joan, 31 ago nit: "Arregla'l ara" (questionari) |

Nota "Nous barris" (31 ago): verificat que totes les etiquetes de zona dels mercats ja fan
servir "Nous barris" (camp `zona` + `ORDRE_ZONES_MERCATS`). "Nou Barris" (nom oficial de
districte) només apareix a l'agrupació per districte de masies/biblioteques, que es manté.

### Millores SEO/GEO/AEO implementades — només metadades, sense tocar disseny ni contingut (1 set 2026)

Aprovació de Joan (1 set 2026): «Es molt important que no es toqui el disseny i que s'arregli
al màxim» + «Prefereixo lliurar-lo ja més decent i en positiu, explicant el que hi ha
implementat». **Cap fitxa creada ni esborrada: els 661 elements queden exactament iguals**;
els canvis són metadades d'indexació (front matter `aliases`/`description`/`foto` i plantilles
de capçalera). Informe complet de l'auditoria: `.ai/informe-seo-geo-aeo-2026-09-01.pdf`.

| # | Implementat | Detall |
|---|---|---|
| 1 | Dada estructurada JSON-LD corregida | Tota la dada era invàlida (l'auto-escaping de Go escapava les cometes del `jsonify` dins `<script>`); afegit `safeJS` arreu — l'idioma que el tema ja usa a `term.html`. Verificat als builds: `WebSite` (portada) i `LandmarksOrHistoricalBuildings` (fitxes) ara vàlids |
| 2 | Schema Person/Organization per als 277 arquitectes | Amb `sameAs` enllaçant l'Arxiu COAC, Viquipèdia i web oficial quan la fitxa en té; els estudis surten com a `Organization` |
| 3 | Redireccions de les 671 URLs del WordPress antic | Via `aliases` de Hugo a 660 fitxes (649 elements + 11 publicacions); 44 renoms verificats un per un contra els títols del WP i les fitxes Hugo, i les 11 pàgines `/text/` del WP apunten a les publicacions. Script idempotent `scripts/aliases-wordpress.py`; plantilla `alias.html` catalana (meta-refresh + canonical + noindex) |
| 4 | `robots.txt` de producció completat | `Sitemap:` + `Disallow: /admin/`. L'staging queda exactament com era (bloqueja tot, per disseny) |
| 5 | `llms.txt` nou | Resum del web en Markdown per als motors d'IA (estàndard llmstxt.org), amb el llistat de les 13 publicacions i notes de llicència i fonts |
| 6 | `404.html` propi | Amb el layout del tema (classes existents, cap disseny nou) i enllaços a portada, mapa, publicacions, arquitectes i contacte |
| 7 | Meta descriptions específiques | Les 13 publicacions (derivades del títol i any d'edició) + hubs: `arquitectes` i `accessibilitat` (noves), `presentacio` (millorada), i `publicacions/_index.md` nou amb títol «Publicacions» (abans el títol sortia «publicacions» en minúscula) |
| 8 | `og:image` a tot el web a producció | Logo del web com a imatge per defecte (`defaultOgImage`) + portada de cada plànol a la seva pàgina de publicació (13/13, la de mercats inclosa) |
| 9 | Títol de la pàgina del mapa | «Mapa» (l'anterior, amb el sufix del template, generava «Guies Barcelona — El Globus Vermell — Guies de Barcelona de El Globus Vermell») |
| 10 | `lastmod` a les 964 URLs del sitemap | `enableGitInfo = true` a la config (el workflow ja fa `fetch-depth: 0`, cap canvi més necessari) |
| 11 | `head.html`: títol net al 404 | Sense el separador buit « — » quan la pàgina no porta títol |

Verificació (builds locals staging + producció, 1 set): JSON-LD net als dos entorns, robots.txt
correcte per entorn, 671 pàgines d'alias generades amb canonical, sitemap amb 964 URLs (els
aliases no hi entren) i lastmod a totes, og:image present a producció, títols nous de mapa i
publicacions. Res canvia visualment: els dos builds només diferien a `<head>` i als fitxers nous.

---

## Pendents d'aprovació (NO executar sense confirmació expressa de Joan)

| Fitxa / canvi proposat | Motiu | Estat |
|---|---|---|
| ~~Crear `casa-lluis-jara-urbano.md`~~ | ✅ FET 31 ago vespre (aprovat per Joan, entrada #4 del registre) | ✅ |
| ~~Paquet mercats~~ (mail Xavi 31 ao vespre) | ✅ FET 31 ago vespre (aprovat per Joan, entrada #5 del registre): 11 canvis de zona, camp `ordre` a 42 fitxes, sub-zones reordenades | ✅ |
| Crear fitxes **Encants de Sant Antoni** i **Dominical de Sant Antoni** (mercats no alimentaris): Xavi diu que han de tenir fitxa però no existeixen; falten dades (adreça, any, coords) | Mail 31 ao vespre: "només tres dels quatre tindran fitxa" | 🔴 esperant dades de Xavi + aprovació Joan (ordre 2 i 3 reservats) |
| ~~Flors de la Rambla: dades sense punt al mapa~~ | ✅ FET 31 ago vespre: fitxa sense lat/long (entrada #5); surt al llistat de "Mercats no alimentaris", sense punt al mapa | ✅ |
| Duplicat `mercat-de-la-marina` + `placa-i-mercat-de-la-marina` (ara tots dos a "Nous barris", ordre 9 totes dues; Xavi només llista "La Marina" un cop) | Detectat 31 ao amb la llista de Xavi | 🔴 esperant decisió (preguntat al mail de resposta) |
| `mercat-de-sant-gervasi` no surt a la llista d'Xavi (sub-zona Sant Gervasi: només Galvany i Tres Torres) | Possible oblid d'Xavi | 🔴 preguntar a Xavi (al mail de resposta) |
| 5 fitxes amb `publicacions` buit (llista amunt) | Invisibles als plànols; 3 són duplicats de migració WordPress | 🔴 esperant decisió (implica Xavi) |
| Duplicats visibles: `edifici-dhabitatges-carrer-navas-238` + `-240` (el paper 2026 les fusiona en #7 Casa Nativitat Vedruna) i `casa-unifamiliar-placa-mons` vs `casa-unifamiliar` (#11 Casa Lluís Barangé) | Artefactes de migració | 🔴 esperant decisió |
| `pavello-de-la-republica-biblioteca-crai-ub.md` (visible, frontmatter malmès) vs `pavello-de-la-republica-de-1937-replica.md` (correcta però sense publicacions) | Duplicat de migració; el mapa mostra la malmesa | 🔴 esperant decisió |
| 4 fitxes d'ítems retirats del paper 2026 (`botiga-cottet`, `reforma-dun-atic`, `reforma-de-laula-de-quimica-a-la-ub`, `adaptacio-dun-convent-per-a-escola-del-cenu`) | Ja no són al plànol en paper però el web les manté (obra GATCPAC real) | 🔴 esperant criteri de Xavi (proposta: mantenir-les) |
