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

**Estat després dels canvis 1-4:** total 660 fitxes; gatcpac 48 elements.

### Canvis de visualització aprovats (no toquen dades de fitxes)

| Data | Canvi | Aprovació |
|---|---|---|
| 2026-08-31 | `main.css`: fotos de fitxa (sola i carrusel) amb **proporció natural** — tret l'`aspect-ratio: 1/1` i l'`object-fit: cover` que retallaven les fotos noves (~127:110 els últims 5 plànols). Bug denunciat per Xavi (mail 2 del 31 ago, punt 5) | Joan, 31 ago vespre: "Fotos que retallen" (questionari) |

Nota "Nous barris" (31 ago): verificat que totes les etiquetes de zona dels mercats ja fan
servir "Nous barris" (camp `zona` + `ORDRE_ZONES_MERCATS`). "Nou Barris" (nom oficial de
districte) només apareix a l'agrupació per districte de masies/biblioteques, que es manté.

---

## Pendents d'aprovació (NO executar sense confirmació expressa de Joan)

| Fitxa / canvi proposat | Motiu | Estat |
|---|---|---|
| ~~Crear `casa-lluis-jara-urbano.md`~~ | ✅ FET 31 ago vespre (aprovat per Joan, entrada #4 del registre) | ✅ |
| **Paquet mercats** (mail Xavi 31 ao vespre, `docs/2026-08-31-mail-xavi-3-mercats-zones.md`): (a) canviar `zona` → "Nous barris" a 11 fitxes (Guinardó, Carmel, Vall d'Hebron–Teixonera, Estrella, Lesseps —actualment "Horta"/"Gràcia"—; Felip II, Provençals, Sant Martí, Besòs —actualment "Sant Martí de Provençals"—; La Marina ×2 —actualment "Sants"—); (b) afegir camp `ordre` a totes les fitxes de mercats (ordre del PDF, no alfabètic); (c) reordenar sub-zones: Sant Martí de Provençals abans d'Horta (text `_index.md` + `SUB_ZONES_ANTICS_MUNICIPIS`/`ORDRE_ZONES_MERCATS` de `mapa.js`) | Llista definitiva de zones d'Xavi | 🔴 esperant aprovació de Joan |
| Crear fitxes **Encants de Sant Antoni** i **Dominical de Sant Antoni** (mercats no alimentaris): Xavi diu que han de tenir fitxa però no existeixen; falten dades (adreça, any, coords) | Mail 31 ao vespre: "només tres dels quatre tindran fitxa" | 🔴 esperant dades de Xavi + aprovació Joan |
| **Flors de la Rambla**: mostrar les dades sense punt al mapa | Mail 31 ao vespre | 🔴 pendent decisió Joan (fitxa sense lat/long o esment al text de la zona) |
| Duplicat `mercat-de-la-marina` + `placa-i-mercat-de-la-marina` (tots dos a "Sants"; Xavi només llista "La Marina" un cop) | Detectat 31 ao amb la llista de Xavi | 🔴 esperant decisió |
| `mercat-de-sant-gervasi` no surt a la llista d'Xavi (sub-zona Sant Gervasi: només Galvany i Tres Torres) | Possible oblid d'Xavi | 🔴 preguntar a Xavi (al mail de resposta) |
| 5 fitxes amb `publicacions` buit (llista amunt) | Invisibles als plànols; 3 són duplicats de migració WordPress | 🔴 esperant decisió (implica Xavi) |
| Duplicats visibles: `edifici-dhabitatges-carrer-navas-238` + `-240` (el paper 2026 les fusiona en #7 Casa Nativitat Vedruna) i `casa-unifamiliar-placa-mons` vs `casa-unifamiliar` (#11 Casa Lluís Barangé) | Artefactes de migració | 🔴 esperant decisió |
| `pavello-de-la-republica-biblioteca-crai-ub.md` (visible, frontmatter malmès) vs `pavello-de-la-republica-de-1937-replica.md` (correcta però sense publicacions) | Duplicat de migració; el mapa mostra la malmesa | 🔴 esperant decisió |
| 4 fitxes d'ítems retirats del paper 2026 (`botiga-cottet`, `reforma-dun-atic`, `reforma-de-laula-de-quimica-a-la-ub`, `adaptacio-dun-convent-per-a-escola-del-cenu`) | Ja no són al plànol en paper però el web les manté (obra GATCPAC real) | 🔴 esperant criteri de Xavi (proposta: mantenir-les) |
