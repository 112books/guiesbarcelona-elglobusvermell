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
| 7 | 2026-10-22 | **Artistes i «Autoria» a 19 fitxes d'art públic** (petició de Xavi del 21/10). (a) Afegit `intervencions: [{tipus: Autoria, autors: <artista>, any: <any>}]` a les 19 fitxes que tenien «Autoria: X. any» només dins `descripcio`; (b) afegit `arquitectes: [<artista>]` a 18 d'elles (no a `mitgera-dels-objectes`: «Alumnes de Ciutat Vella» no és una persona); (c) creades 16 pàgines a `content/ca/arquitectes/`: 15 amb `tipus: artista` (Alfredo Lanz, Antoni Llena, Francesc Abad, Frederic Amat, Jannis Kounellis, Joan Gardy Artigas, Josep Maria Subirachs, Juan Muñoz, Julio Maragall, Lothar Baumgarten, Mario Merz, Pete Sans, Rafael Solanich, Rebecca Horn, Salvador Aulèstia) i Frank Gehry com a `individual`. Bofill: es fa servir la pàgina existent «Ricardo Bofill Levi» (la descripció diu «Ricard»; no s'ha canviat cap nom). **No s'ha esborrat res**: el text «Autoria: …» de cada descripció es manté. No canvia cap punt del mapa (ni coordenades, ni `publicacions`). | `descripcio` de cada fitxa («Autoria: X. any») | Joan, 22/10: «Tot: CMS + plantilles + 19 fitxes» |

| 8 | 2026-10-22 | **Restablert el camp `tipus` a 18 fitxes d'arquitecte** (`adolf-florensa`, `albert-de-pineda-álvarez`, `albert-viaplana-i-veà`, `alfonso-de-luna`, `alfonso-milà`, `amadeu-llopart`). Les edicions fetes al CMS el 22/10 el desaven buit (`tipus: ''`) i la fitxa quedava fora del seu grup a la pàgina d'Arquitectes. Comprovat a la història de git que les sis eren `individual`; restablert **només** aquest camp (la resta de l'edició d'Xavi es manté intacta). Causa probable: el desplegable «Tipus» es va canviar el 22/10 (s'hi va afegir «Artista») i el navegador dels editors anava amb la memòria cau antiga; s'ha pujat `CMS_CACHE_VERSION`, el camp s'ha fet obligatori (`required: true`, per defecte `individual`) i s'hi ha afegit una pista. Com que Xavi seguia editant mentre ho arreglàvem, la restauració s'ha fet dues vegades (6 + 12 fitxes); totes eren `individual`. | `git log` dels fitxers + `static/admin/cms/config.yml` | Joan, 22/10 («sí, clar») |
| 9 | 2026-10-23 | **Tret `tipus: individual` de 150 fitxes d'arquitecte** (petició d'Xavi del 23/10: «no farem servir l'etiqueta individual»). Eliminada només la línia `tipus: individual` del frontmatter; es mantenen les 47 `estudi` i les 15 `artista`. El camp «Tipus» del CMS torna a ser opcional, amb l'opció **«Cap (sense etiqueta)»** (`value: ""`) i sense «Individual» a la llista. `layouts/arquitectes/terms.html` només pinta l'etiqueta per a «Estudi» i «Artista». Verificat al build de staging: 0 etiquetes «Individual», 47 «Estudi», 15 «Artista». No s'ha esborrat cap fitxa ni cap altra dada. | `content/ca/arquitectes/*/_index.md` + `static/admin/cms/config.yml` | Xavi, 23/10 (mail) + Joan, 23/10 («seguim») |
| 10 | 2026-10-23 | **Fotos de biblioteques i tres fitxes noves** (carpeta rebuda de Xavi el 23/10). (a) Creades `biblioteca-esquerra-de-leixample-agusti-centelles`, `biblioteca-fort-pienc-ana-maria-moix` i `biblioteca-camp-de-larpa-caterina-albert` (ítems 5, 6 i 39 del llistat nou) amb foto, adreça, arquitecte i any; (b) tret `- biblioteques` de `edifici-collage-centre-cultural-teresa-pamies`, `illa-dequipaments-alchemika` i `illa-dequipaments-fort-pienc` i moguts els àlies `/biblioteques/...` a les fitxes noves (evita ítems duplicats i àlies en conflicte); (c) 27 fotos aplicades (21 reemplaçades + 6 noves), amb `fotos_addicionals` a Joan Miró (3) i Dipòsit de les Aigües (2); (d) `data/imatges_dims.json` regenerat (428 imatges). Les 27 fotos s'han comprimit a ≤1.600 px i ≤400 KB abans de pujar-les. Cap fitxa esborrada. | Carpeta `Fotografies de les biblioteques` (PDF «Les biblioteques de Barcelona · LLISTAT» del 23/10) | Joan, 23/10 («seguim»); Xavi va dir que enviaria totes les fotos |

| 11 | 2026-10-23 | **Marxa enrere de les tres fitxes de biblioteca (correcció del #10) i autocompletat d'arquitectes al CMS.** Les tres fitxes creades al #10 eren el mateix edifici que tres fitxes que ja existien i sortien dues vegades al plànol. Eliminades, restaurats els àlies `/biblioteques/...` a `edifici-collage-centre-cultural-teresa-pamies`, `illa-dequipaments-alchemika` i `illa-dequipaments-fort-pienc`, i tornada la inclusió `- biblioteques` a les tres (el plànol queda amb **51 fitxes**, 681 àlies al build). Al CMS, el camp «Arquitectes» passa de llista lliure a `relation` amb autocompletat sobre la col·lecció d'arquitectes (desa el títol, compatible amb el que ja estava desat); `CMS_CACHE_VERSION` → `2026-10-23-2`. | Revisió del plànol (38 àlies `/biblioteques/` en conflicte) i mail de Joan a Xavi | Joan, 23/10 tarda |
| 12 | 2026-10-23 | **Segona tongada de `tipus: individual`: 50 fitxes.** El CMS escrivia el camp a cada desada mentre el navegador de l'editor anava amb la configuració antiga: 43 fitxes als primers minuts de la tarda i 7 més en desades de 15:58–16:03, ja amb la configuració nova desplegada (el select conserva el valor que troba al fitxer). Tretes totes dues vegades i `CMS_CACHE_VERSION` → `2026-10-23-3` perquè l'editor es netegi sol en obrir-se. **Resultat: 0 fitxes amb `tipus: individual`**, 48 `estudi` i 16 `artista`. | `grep -rl '^tipus: individual' content/ca/arquitectes` + `git log` de les desades de Xavi | Joan, 23/10 tarda |
| 13 | 2026-10-23 | **B3 — adreça repetida fora de 37 descripcions.** La fitxa ja mostra l'adreça en un camp propi, però moltes descripcions la tornaven a començar («C. Comte d'Urgell, 145-147 ...»). Tret el prefix només als casos inequívocs (el text comença exactament per l'adreça guardada i continua amb una frase, no amb una segona adreça ni amb guions o barres), aplicat amb el criteri de `scripts/normalitza-adreces.py`. **No s'ha esborrat cap text**: només el prefix duplicat. Queden **48 casos** per fer a mà (dues o tres adreces seguides, descripcions que només són l'adreça, fitxes sense camp d'adreça), a `.ai/informe-adreces-descripcio-2026-10-13.md`. | `scripts/normalitza-adreces.py` + informe del 13/10 | Xavi, 21/10: «Endavant!» |
| 14 | 2026-10-23 | **B2 — informació encallada dins «projecte» (75 fitxes).** (a) Treta l'etiqueta «Categoria: …» del WordPress de **66 textos** de descripció (al principi del text o dins seu); (b) camp `tipologia` omplert a **64 fitxes** que el tenien buit (Fàbrica, Fàbrica amb xemeneia, Recinte industrial, Altres edificis, Xemeneia); (c) **11 intervencions** amb l'autor dins del camp `any` separades en `autors` + `any` («Josep Graner i Prat. 1910, aprox.» → autor i any), només quan l'any era inequívoc (les de diverses fases o amb «?» queden a l'informe); (d) `layouts/elements/single.html`: la fila «Projecte» s'amaga quan el text és el mateix que el d'una intervenció (es pintava dues vegades); el camp es conserva al fitxer. **No s'ha esborrat cap text**: cada dada s'ha mogut al camp que li toca. Queden **45 casos** per revisar a ull i **46** de text tallat a la migració, a `.ai/informe-neteja-projecte-2026-10-14.md`. | `scripts/proposa-neteja-projecte.py` + informe del 14/10 | Xavi, 21/10: «Endavant! Igualment després nosaltres haurem de fer una bona repassada i correccions finals» |
| 15 | 2026-10-23 | **Fotos: dues orfes col·locades i la de l'Edifici d'oficines Llull 122 recuperada.** Les fotos importades per a les fitxes de biblioteca del #10 (ara eliminades) no es perden: la de la Fort Pienc passa a ser la foto principal d'`illa-dequipaments-fort-pienc` (era l'única fitxa del plànol de Biblioteques sense imatge) i la de l'Esquerra de l'Eixample, la segona foto (carrusel) d'`edifici-collage-centre-cultural-teresa-pamies`. A més, `edifici-doficines-llull-122` apuntava a una imatge que no era al disc (sortia trencada): recuperada de `originals/Fotos-web-app/2010-2025/64_oficines llull.jpg` i reduïda a 1.296 px. `data/imatges_dims.json` regenerat (429 imatges). **Cap fitxa queda amb una imatge trencada.** | Carpeta `Fotografies de les biblioteques` + `originals/` | Joan, 23/10: «endavant amb les fotos» |

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

### Rendiment — imatges i càrrega (1 set 2026)

Aprovació: prioritat 1 de Joan (1 set). Els punts 3-4 no canvien res visualment: només reserven
l'espai de la foto abans que carregui (menys salts de pàgina) i en priorititzen la descàrrega.

| # | Canvi | Detall |
|---|---|---|
| 1 | 390 imatges optimitzades in situ | Decisió de Joan: **JPG redimensionat** (màx 1.600px, qualitat 85, EXIF tret amb auto-orient) i no WebP, perquè WhatsApp/Telegram no llegeixen WebP com a `og:image` i les miniatures necessàries es mengen l'estalvi. **837→144 MB (−83%)**: elements 818→134 (353 de 358; 5 ja optimitzades es mantenen) i publicacions 19→10 (37 de 50). Mateixos noms i URLs, cap canvi de plantilla; originals recuperables a la història de git. Commit `42337ff` |
| 2 | 33 fotos de biblioteques enllaçades | Forat de migració detectat durant aquesta feina — vegeu l'entrada **#6** del registre de canvis |
| 3 | `width`/`height` als `<img>` de fitxa | Manifest `data/imatges_dims.json` (408 imatges) generat amb `scripts/genera-dims-imatges.py` (re-executable); `single.html` el consulta per a la foto única i el carrusel — evita salts de pàgina en carregar (CLS) |
| 4 | Foto única `loading="eager"` + `fetchpriority="high"` | Abans era `lazy` (penalitzava el LCP, la foto és l'element principal de la fitxa); la primera diapositiva del carrusel, que ja era `eager`, ara també porta `fetchpriority`. Verificat amb diff de build: l'únic que canvien són atributs d'`<img>` i `lastmod` |
| 5 | Leaflet verificat — cap canvi | `leaflet.js` ja és la dist minificada oficial 1.9.4: 147 KB en disc però **42 KB gzipades** en línia (GitHub Pages serveix gzip); el pendent venia de confondre la mida en cru amb la transferida |

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
