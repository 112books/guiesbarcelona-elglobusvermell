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

*(Verificat 1 set amb el control diari de números: totes cinc tenen ja `publicacions` assignades
— gatcpac/interiors-illa; el pendent que queda són els duplicats de migració, a la taula de pendents.)*

---

## Registre de canvis

| # | Data | Canvi | Font de dades | Aprovació |
|---|---|---|---|---|
| 1 | 2026-08-31 | Creada `content/ca/elements/casa-roca-barallat.md` — Casa Roca Barallat, Via Augusta 12, Carles Martínez Sánchez, 1935; coords 41.3967221 / 2.1551607 (Nominatim, validat: Via Augusta 61 OSM coincideix amb fitxa Rodriguez Arias a ~3 m); `publicacions: [gatcpac]` (ítem #39 reedició 2026) | PDF reedició 2026 *Arquitectura d'avantguarda* + Nominatim OSM | Joan, 31 ago: "Arregla doncs les fitxes que comenta en XAVI" (Xavi la cita com a pendent de crear) |
| 2 | 2026-08-31 | Afegida `- gatcpac` a `publicacions` de `fundacio-joan-miro.md` (ítem #43 avantguarda, present a les edicions 2016 #46 i 2026 #43) | PDF edicions 2016 i 2026 | Joan, mateixa instrucció |
| 3 | 2026-08-31 | Afegida `- gatcpac` a `publicacions` de `les-escales-park.md` (ítem #42 avantguarda, present a les edicions 2016 #47 i 2026 #42) | PDF edicions 2016 i 2026 | Joan, mateixa instrucció |
| 4 | 2026-08-31 | Creada `content/ca/elements/casa-lluis-jara-urbano.md` — Casa Lluís Jara Urbano, C. de Balmes 371, Josep Soteras Mauri, 1935 (reedició 2026; l'edició 2016 deia 1936); coords 41.4045422 / 2.1403092 (Nominatim, validat: Balmes 166 OSM coincideix amb fitxa existent a ~12 m); `publicacions: [gatcpac]` (ítem #38 de les dues edicions) | PDF reedició 2026 *Arquitectura d'avantguarda* + Nominatim OSM | Joan, 31 ago vespre: "Sí, crea-la" (questionari de decisions) |
| 5 | 2026-08-31 | **Paquet mercats** segons la llista definitiva d'Xavi: (a) `zona` → "Nous barris" a **11 fitxes** (Guinardó, Carmel, Vall d'Hebron–Teixonera, Estrella, Lesseps, Felip II, Provençals, Sant Martí, Besòs, La Marina ×2) via `scripts/mercats-zones-ordre.py`; (b) camp **`ordre`** (posició al PDF dins de cada zona) a les 42 fitxes de mercats — La Marina duplicada ordre 9 totes dues, Encants–Fira de Bellcaire ordre 4 (reserva 2-3 pels de Sant Antoni), Sant Gervasi ordre 3 (dubte pendent); (c) creada `content/ca/elements/flors-de-la-rambla.md` — **sense lat/long** (surts al llistat, sense punt al mapa, tal com demanava Xavi), descripció textual del plànol; (d) reordenades sub-zones: Sant Martí de Provençals abans d'Horta (`_index.md` + `ORDRE_ZONES_MERCATS` + `SUB_ZONES_ANTICS_MUNICIPIS`); (e) `mapa.js`: ordenació dins de zona pel camp `ordre` (desempat alfabètic) + `term.html` passa el camp | Mail Xavi 31 ago vespre (`docs/2026-08-31-mail-xavi-3-mercats-zones.md`), llista amb ordre del PDF | Joan, 31 ago vespre: "Sí, aplica'l ara" + "Fitxa sense punt" (questionari de decisions) |
| 6 | 2026-09-01 | **Fotos de 33 fitxes de biblioteques enllaçades**: tenien la imatge al disc (`static/img/elements/<slug>.jpg`) però no el camp `foto:` (forat de migració: les pàgines es veien sense foto; 38 de 46 en mancaven, 33 amb imatge coincident). Afegit `foto: /img/elements/<slug>.jpg` després de `draft:`; també normalitzada la barra inicial de `foto:` a 150 fitxes (cosmètic: `single.html` ja la resolia amb `TrimPrefix`+`relURL`). Ara 359 fitxes tenen foto (41 de 46 biblioteques) | Detecció pròpia 1 set durant el treball d'imatges: dry-run + diff de build (34 pàgines canviades: les 33 + la portada, que mostra fitxes amb foto) | Joan, 1 set: "Sí, enllaça-les totes" (decisió per escrit) |

**Estat després dels canvis 1-5:** total 660 fitxes (correcció 1 set: el 661 comptava el `_index` de la secció); gatcpac 48 elements; mercats 43 (42 amb punt + Flors de la Rambla sense).

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
implementat». **Cap fitxa creada ni esborrada: els 660 elements queden exactament iguals**;
els canvis són metadades d'indexació (front matter `aliases`/`description`/`foto` i plantilles
de capçalera). Informe complet de l'auditoria: `.ai/informe-seo-geo-aeo-2026-09-01.pdf`.

| # | Implementat | Detall |
|---|---|---|
| 1 | Dada estructurada JSON-LD corregida | Tota la dada era invàlida (l'auto-escaping de Go escapava les cometes del `jsonify` dins `<script>`); afegit `safeJS` arreu — l'idioma que el tema ja usa a `term.html`. Verificat als builds: `WebSite` (portada) i `LandmarksOrHistoricalBuildings` (fitxes) ara vàlids |
| 2 | Schema Person/Organization per als 274 arquitectes de la taxonomia | Amb `sameAs` enllaçant l'Arxiu COAC, Viquipèdia i web oficial quan la fitxa en té; els estudis surten com a `Organization` |
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
Correccions derivades de la verificació de números (1 set vespre): el recompte real és **660 fitxes**
(i 661 pàgines `.md` comptant el `_index` de la secció) i **274 arquitectes** (les xifres 661/277
de l'informe original venien de comptar URLs del sitemap; PDF regenerat amb els números exactes);
identificades **3 fitxes curades d'arquitecte òrfenes** (vegeu pendents).

### Seguretat — validació de paràmetres d'URL i HTML en cru (1 set 2026)

Aprovació: prioritat 2 de Joan (1 set): «1) Rendiment, 2) Seguretat». Cap canvi visual ni cap dada
de fitxes: només validació de JavaScript i configuració de renderitzat.

| # | Canvi | Detall |
|---|---|---|
| 1 | Whitelist del paràmetre `?tema=` (`mapa.js`) | Abans el valor de la URL es ficava directament com a classe (`tema-<valor>`): un valor amb caràcters invàlids feia llançar a `classList.add` una excepció i **el mapa no arribava a inicialitzar-se** (i generava classes arbitràries indexables). Ara només s'accepten `a`/`b`/`c` (els tres temes de tiles reals); qualsevol altre valor cau a `a` |
| 2 | `unsafe = false` a Goldmark (`hugo.toml`) + shortcode `badges-accesibilitat` | L'única pàgina amb HTML en cru al contingut era la d'accessibilitat (badges de normatives, escrits per nosaltres); el bloc passa al shortcode `shortcodes/badges-accesibilitat.html` i el Markdown ja no pot injectar HTML arbitrari (rellevant amb l'entrada del CMS per a l'equip). Verificat amb diff de build complet: **1.645 pàgines idèntiques** llevat del fingerprint del `mapa.min.js` (canvia per la validació nova) i un salt de línia a l'accessibilitat |
| 3 | Revisats `?pub=` i `?color=` — ja eren segurs | `mapa.js:508` valida amb `hasOwnProperty` contra les publicacions reals; `fitxa.js:5` valida el color amb regex hex. Cap canvi necessari |
| 4 | `envia.php` — no actuable aquí | El fitxer no existeix al repo Hugo: és del WordPress de producció (Hetzner). Auditar-lo o substituir-lo (formulari de contacte) toca al dia de la migració |

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
| ~~5 fitxes amb `publicacions` buit~~ (llista amunt) | ✅ Resolt (verificat 1 set): totes cinc tenen `publicacions` assignades; el pendent que queda són els **duplicats de migració** (files de sota) | ✅ |
| Duplicats visibles: `edifici-dhabitatges-carrer-navas-238` + `-240` (el paper 2026 les fusiona en #7 Casa Nativitat Vedruna) i `casa-unifamiliar-placa-mons` vs `casa-unifamiliar` (#11 Casa Lluís Barangé) | Artefactes de migració | 🔴 esperant decisió |
| `pavello-de-la-republica-biblioteca-crai-ub.md` (visible, frontmatter malmès) vs `pavello-de-la-republica-de-1937-replica.md` (correcta però sense publicacions) | Duplicat de migració; el mapa mostra la malmesa | 🔴 esperant decisió |
| 4 fitxes d'ítems retirats del paper 2026 (`botiga-cottet`, `reforma-dun-atic`, `reforma-de-laula-de-quimica-a-la-ub`, `adaptacio-dun-convent-per-a-escola-del-cenu`) | Ja no són al plànol en paper però el web les manté (obra GATCPAC real) | 🔴 esperant criteri de Xavi (proposta: mantenir-les) |
| 3 fitxes curades d'arquitecte **òrfenes**: `albert-viaplana`, `toyo-ito`, `oab-(carlos-ferrater)` — el títol no coincideix amb el nom que usen les fitxes («Albert Viaplana i Veà», «Toyo Ito Associates», «OAB (Carlos Ferrater)») → queden sense cap edifici que les enllaci i generen pàgines de terme duplicades | Trobat 1 set amb la verificació diària de números (276 pàgines de terme al sitemap vs 274 arquitectes) | 🔴 esperant criteri de Xavi (relacionat amb els 73 arquitectes a separar) |
| 5 fitxes de biblioteques **sense cap imatge** al disc: `bon-pastor-josefina-castellvi`, `canyelles-maria-angels-rivas`, `de-lateneu-barcelones`, `les-roquetes-rafa-juncadella`, `vallcarca-i-els-penitents-maria-antonieta-cot` | La foto no existeix al repo (no és un problema d'enllaç, com les 33 anteriors) | 🔴 pendent per a l'equip (cal aportar les fotos) |
