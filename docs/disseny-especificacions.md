# Especificacions de disseny — guiesbarcelona.elglobusvermell.org

> Document intern de referència per a revisions de disseny amb el client.
> Versió actual: provisional. Els elements marcats ⚠️ estan pendents de confirmació.

---

## 1. Tipografia

| Element | Família | Mida | Pes | Notes |
|---------|---------|------|-----|-------|
| Cos de text | System font stack¹ | 18px (1.125rem) | 400 | Alçada de línia 1.6 |
| H1 (títols de pàgina) | ídem | fluid 32–56px² | 700 | `clamp(2rem, 4vw, 3.5rem)` |
| H2 (seccions) | ídem | fluid 24–36px² | 700 | `clamp(1.5rem, 3vw, 2.25rem)` |
| H3 (subseccions) | ídem | 20px (1.25rem) | 700 | — |
| Text secundari/meta | ídem | 13px (0.8125rem) | 400 | Filtres, etiquetes |
| Peu de pàgina | ídem | ~14px | 400 | Color `#b3b3b3` |

¹ **System font stack** (sense dependència externa, zero Google Fonts):
`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`
→ cada usuari veu la font del seu sistema operatiu (SF Pro a Mac/iOS, Segoe UI a Windows, Roboto a Android).

² Els títols s'adapten proporcionalment a l'amplada de pantalla (CSS `clamp`).

⚠️ **Pendent de decisió**: el client pot triar una tipografia pròpia (Google Fonts, Adobe Fonts o fitxer personalitzat). Canvi estimat: 1h.

---

## 2. Colors base

| Variable | Hex | Ús |
|----------|-----|----|
| `--color-bg` | `#ffffff` | Fons general |
| `--color-text` | `#111111` | Text principal |
| `--color-muted` | `#555555` | Text secundari |
| `--color-border` | `#e5e5e5` | Vores i separadors |
| `--color-accent` | `#c81e1e` | Accent de marca ⚠️ provisional |

⚠️ **Color d'accent pendent de confirmació**: s'ha usat `#c81e1e` (vermell) com a referència al nom "El Globus Vermell". Cal que el client confirmi o substitueixi per un color de marca oficial.

---

## 3. Colors de publicació

Cada publicació té un color identificatiu extret de la portada física del plànol-guia. S'usa als marcadors del mapa, a les pastilles de filtre i a la banda lateral de les fitxes d'edifici.

| Publicació | Any | Color | Hex | Origen |
|------------|-----|-------|-----|--------|
| Arquitectura d'avantguarda (GATCPAC) | 2016 | 🟡 | `#eca647` | Portada (amber/gualda) |
| Jardins interiors d'illa de l'Eixample | 2018 | 🟢 | `#8fca6a` | Web actual |
| El patrimoni industrial del Poblenou | 2019 | 🔴 | `#dd4b1a` | Web actual |
| Arquitectura Moderna 1950–1975 | 2019 | 🔵 | `#050d9e` | Web actual |
| Mercats de Barcelona | 2019 | 🟣 | `#880064` | Web actual |
| La Barceloneta | 2020 | 🟠 | `#f99d1c` | Web actual |
| La Marina del Port i del Prat Vermell | 2023 | 🩷 | `#e9a9a6` | Portada (rosa) |
| La Barcelona de Tàpies | 2024 | ⬛ | `#565658` | Portada (carbó) |
| Masies de Barcelona | 2025⚠️ | 🌿 | `#5a8577` | Portada (sage) |
| Biblioteques de Barcelona | 2025⚠️ | 🩵 | `#0797c3` | Portada (cyan) |
| New Babylon Barcelona | 2026⚠️ | 🩶 | `#f06961` | Portada (coral) |
| De l'esperança a la crisi 1975–2008 | 2026⚠️ | 🔘 | `#a7b4bb` | Portada (blau-gris) |
| La revolució tranquil·la 2010–2025 | 2026⚠️ | 🫒 | `#abc268` | Portada (oliva) |

⚠️ Les publicacions pendents d'edició (2025–2026) poden canviar de color quan surtin les portades definitives.

---

## 4. Espaiat i estructura

| Variable | Valor | Ús |
|----------|-------|----|
| `--space-sm` | 12px (0.75rem) | Espaiat petit (padding intern) |
| `--space-md` | 24px (1.5rem) | Espaiat mitjà (entre elements) |
| `--space-lg` | 48px (3rem) | Espaiat gran (entre seccions) |
| Amplada màxima contingut | 72rem (≈1152px) | Contenidor central |
| Header altura | 80px → 56px en scroll | Col·lapse en desplaçar |

---

## 5. Components principals

### Header
- Fons blanc, vora inferior `#e5e5e5`
- Logo complet visible en repòs; versió compacta quan l'usuari fa scroll
- Navegació horitzontal: Presentació · En paper · Crèdits

### Mapa
- Proveïdor: **Leaflet + OpenStreetMap / CartoDB**
- Tema A (defecte): CartoDB Light — fons clar, marcadors de color
- Tema B: CartoDB Dark — fons fosc, marcadors lluminosos
- Tema C: CartoDB Voyager — estil mapa turístic, sidebar lateral
- Marcadors: cercles amb color de la publicació corresponent
- Altura: 28rem (escriptori), 22rem (tauleta), 18rem (mòbil)

### Pastilles de filtre (publicació)
- Fons `#f0f0f0` en repòs
- Quan actives: fons i vora del color de la publicació, text blanc
- Mida text: 13px

### Fitxes d'edifici
- Banda lateral esquerra del color de la publicació (`--pub-color`)
- Quadrícula de dades (adreça, any, arquitectes, protecció...)
- Mini-mapa individual (Leaflet)
- Navegació ← anterior · → següent dins la mateixa publicació

### Llistat alfabètic (portada)
- Fila d'índex A–Z, enganxada a la capçalera en scroll
- Grups plegables (acordió), tancats per defecte
- Cada element mostra: títol · adreça · any

### Pàgines de publicació (`/publicacions/<slug>/`)
- Banda de color de la publicació a la capçalera
- Mapa de tots els edificis de la publicació
- Llistat cronològic per any (acordió), tancats per defecte
- Descripció de la publicació al final

---

## 6. Paleta de tons neutrals en ús (valors literals)

Fora de les variables, el CSS usa directament:

| Hex | Ús |
|-----|----|
| `#f8f9fa` | Fons de l'índex alfabètic |
| `#f0f0f0` | Fons pastilles filtre inactives |
| `#888` | Color per defecte sense publicació assignada |
| `#666` | Text de metadades (etiquetes dades) |
| `#333` | Botó "Tots" quan actiu |
| `#aaa` | Text desactivat, placeholder |
| `#b3b3b3` | Peu de pàgina |

---

## 7. Canvis de disseny: com demanar-los

Per a cada modificació, indiqueu:

1. **Element**: quin component (header, mapa, fitxa, llistat…)
2. **Propietat**: color / mida / tipografia / espaiat / comportament
3. **Valor actual** (podeu copiar de les taules d'aquest document)
4. **Valor desitjat**: hex, nom de font, píxels, etc.

Exemple:
> "El color d'accent (`#c81e1e`) → substituir per `#8b1a1a` (vermell més fosc)"
> "La tipografia del cos → afegir 'Playfair Display' com a tipografia serif per als títols"

Estimació de temps per a canvis habituals:
- Color d'accent o color de publicació: **15 min**
- Canvi de tipografia (Google Fonts): **30–45 min**
- Mida de text o espaiat global: **15–30 min**
- Nou component o secció: **2–4h** depenent de complexitat
