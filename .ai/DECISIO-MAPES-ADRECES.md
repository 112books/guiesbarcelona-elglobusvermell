# Decisió: Google Maps vs OpenStreetMap per als enllaços d'adreça

**Context:** Quan un usuari fa clic sobre l'adreça d'un edifici a la fitxa, s'obre un mapa extern. Ara mateix l'enllaç apunta a Google Maps. Cal decidir si mantenir-ho o canviar a OpenStreetMap.

---

## Opció A — Google Maps

**URL exemple:**
`https://www.google.com/maps/search/?api=1&query=Pg.+Joan+de+Borbó+43,+Barcelona`

### Arguments a favor

- **Adopció massiva.** És el mapa que la gran majoria d'usuaris coneixen i esperen. Menys fricció, zero aprenentatge.
- **Obre l'app nativa en mòbil.** En Android i iOS, el link de Google Maps llança directament l'aplicació instal·lada al dispositiu, amb navegació pas a pas.
- **Dades molt riques.** Fotos de Street View, horaris de negocis propers, transport públic, ressenyes. Útil si l'usuari vol orientar-se visualment al voltant de l'edifici.
- **Geocodificació robusta.** Google troba adreces ambigües o mal formatades amb molta més fiabilitat que OSM.
- **Expectativa de l'usuari.** En webs de cultura, guies i patrimoni, l'enllaç "Com arribar-hi" apunta quasi sempre a Google Maps.

### Arguments en contra

- **Privacitat.** Google registra cada clic, l'adreça IP i el perfil d'usuari. No és anònim.
- **Dependència comercial.** Google pot canviar les condicions de les URLs d'enllaç directe en qualsevol moment (ho ha fet). Ara és gratuït; podria deixar de ser-ho.
- **Incoherència interna.** El mapa principal del web usa OpenStreetMap i Leaflet. Enviar l'usuari a Google per a les fitxes trenca la coherència de la identitat tecnològica del projecte.
- **No alineat amb els valors del projecte.** Un projecte de cultura barcelonina amb vocació pública pot voler evitar afavorir un monopoli privat.

---

## Opció B — OpenStreetMap

**URL exemple:**
`https://www.openstreetmap.org/search?query=Pg.+Joan+de+Borbó+43,+Barcelona`

o amb coordenades exactes (millor):
`https://www.openstreetmap.org/?mlat=41.3779&mlon=2.1885&zoom=17`

### Arguments a favor

- **Coherència total.** El mapa principal del web ja usa OSM. L'usuari segueix en el mateix ecosistema cartogràfic.
- **Privacitat.** OpenStreetMap no fa seguiment dels usuaris.
- **Valors oberts.** OSM és un projecte comunitari sense ànim de lucre. Molt coherent amb la vocació cultural i pública d'El Globus Vermell.
- **Coordenades exactes disponibles.** Ja tenim `lat` i `long` a cada edifici. Podem generar un link amb marcador precís, sense dependre de la geocodificació de l'adreça.
- **Sense dependència comercial.** Cap risc de canvis de condicions o desaparició de l'API.

### Arguments en contra

- **Menys familiar per a l'usuari mitjà.** Molts usuaris no reconeixen OSM i poden sentir-se desorientats.
- **No obre l'app nativa en mòbil.** Un link d'OSM obre el navegador, no cap aplicació de navegació. L'usuari haurà d'obrir Google Maps o Apple Maps manualment per navegar.
- **Menys funcionalitats de context.** Sense Street View, sense transport públic integrat, sense indicacions de ruta senzilles per a l'usuari final.
- **Percepció de qualitat.** En alguns barris de Barcelona, OSM és menys detallat que Google Maps (menys POI, menys noms de comerços).

---

## Opció C — Geo URI (link universal) *(alternativa tècnica)*

**URL:** `geo:41.3779,2.1885?z=17`

En mòbil, obre el selector d'apps del sistema (Google Maps, Apple Maps, OsmAnd...). En escriptori, no funciona.
**Poc recomanable** com a única opció per la incompatibilitat d'escriptori.

---

## Opció D — Doble enllaç *(compromís)*

Mostrar dos botons a la fitxa:

> [Veure a OpenStreetMap] [Veure a Google Maps]

- Respecta la llibertat de l'usuari.
- Afegeix complexitat visual menor.
- Permet mantenir la coherència (OSM primer) sense sacrificar usabilitat (Google Maps disponible).

---

## Resum comparatiu

| Criteri                        | Google Maps | OpenStreetMap | Doble enllaç |
|-------------------------------|:-----------:|:-------------:|:------------:|
| Familiar per a l'usuari        | ✅ Sí       | ⚠️ Menys      | ✅ Sí        |
| Obre app mòbil                 | ✅ Sí       | ❌ No         | ✅ (Google)  |
| Privacitat                     | ❌ No       | ✅ Sí         | ⚠️ Parcial   |
| Coherència amb el web          | ❌ No       | ✅ Sí         | ⚠️ Parcial   |
| Valors oberts                  | ❌ No       | ✅ Sí         | ⚠️ Parcial   |
| Marcador precís (coordenades)  | ✅ Sí       | ✅ Sí         | ✅ Sí        |
| Dependència comercial          | ⚠️ Risc     | ❌ Cap        | ⚠️ Parcial   |
| Cost d'implementació           | Baix        | Baix          | Baix         |

---

## Recomanació tècnica (LinuxBCN)

**Opció B (OpenStreetMap)** amb URL de coordenades exactes, ja que tots els edificis tenen `lat`/`long`. Coherència total, privacitat i zero dependència comercial, sense cost addicional.

Si la prioritat és la usabilitat mòbil i no hi ha objecció a Google, **Opció A**.

Si El Globus Vermell vol una posició de compromís visible, **Opció D** és la més transparent amb l'usuari.

---

*Document elaborat: 2026-08-08 · LinuxBCN per a El Globus Vermell*
