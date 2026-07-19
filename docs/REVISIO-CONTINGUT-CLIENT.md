# Revisió de contingut — guiesbarcelona.elglobusvermell.org

**Document per al client: El Globus Vermell**
**Darrera actualització:** 2026-07-19
**Estat general:** En revisió

Aquest document recull **tots els canvis editorials** fets al web nou respecte al web original de WordPress, pàgina per pàgina. El client ha de revisar cada secció i marcar l'estat de cada canvi.

---

## Com fer la revisió

Per cada canvi pots indicar:
- ✅ **Confirmat** — el canvi és correcte, es pot deixar així
- 🔄 **A corregir** — caldria canviar-ho; afegeix una nota explicant com
- ❓ **Dubte** — cal discussió

Pots editar directament aquest document o enviar els comentaris per correu/missatge.

---

## Llegenda de tipus de canvi

| Icona | Significat |
|-------|-----------|
| ✏️ | Text modificat o reformatat |
| ➕ | Contingut afegit (no estava al WP original) |
| ➖ | Contingut eliminat |
| 🔗 | URL o link canviat |
| 🏗️ | Canvi d'estructura (h2/h3, ordre de seccions) |
| ⚠️ | Requereix confirmació urgent |

---

## 1. Pàgina d'inici (Mapa)

**URL:** `/` (arrel del web)
**URL original WP:** `https://guiesbarcelona.elglobusvermell.org/`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | 🏗️ | La home era una pàgina de text amb presentació del projecte | La home és ara directament el mapa interactiu amb tots els edificis | Pendent |
| 2 | ➕ | — | Filtres per publicació i tema transversal al mapa | Pendent |
| 3 | ➕ | — | Llistat alfabètic de tots els edificis sota el mapa | Pendent |

---

## 2. Presentació

**URL:** `/presentacio/`
**URL original WP:** `https://guiesbarcelona.elglobusvermell.org/presentacio/`
**Fitxer:** `content/ca/presentacio/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Text original del WP (diverses pàgines de text) | Text importat i adaptat | Pendent — **cal revisar que tot el text sigui igual** |

---

## 3. En paper (llista de publicacions)

**URL:** `/en-paper/`
**URL original WP:** `https://guiesbarcelona.elglobusvermell.org/en-paper/`
**Fitxer:** `content/ca/en-paper/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Introducció general sobre les publicacions en paper | Importada, revisar fidelitat | Pendent |
| 2 | ➕ | Masies de Barcelona: descripció existent al WP | Descripció afegida manualment basant-se en el text introductori de la pàgina de la publicació | Pendent |
| 3 | ➕ | New Babylon: descripció al WP | Revisar si existia al WP | Pendent |
| 4 | ✏️ | Ordre de les publicacions | S'ha mantingut l'ordre cronològic del WP | Pendent |

---

## 4. Publicació: GATCPAC — Arquitectura d'avantguarda. 1928–1939

**URL:** `/publicacions/gatcpac/`
**URL original WP:** `https://guiesbarcelona.elglobusvermell.org/category/architectura-d-avantguarda-gatcpac/` (404)
**Fitxer:** `content/ca/publicacions/gatcpac/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | `UNA IMMERSIÓ EN L'ARQUITECTURA DE SERT I ELS ARQUITECTES DEL GATCPAC` (majúscules) | `Una immersió en l'arquitectura de Sert i els arquitectes del GATCPAC` | Pendent |
| 2 | 🏗️ | "El GATCPAC" era text pla (no títol de secció) | `## El GATCPAC` (secció d'acordió) | Pendent |
| 3 | ➖ | Frase eliminada de la introducció: *"Alhora, es fixen en l'arquitectura vernacular..."* (es manté dins l'acordió) | — | Pendent |
| 4 | ✏️ | `## Josep Lluís Sert I López` (majúscula errònia a "I") | `## Josep Lluís Sert i López` | Pendent |
| 5 | 🏗️ | Noms dels arquitectes coautors (Torres, Subirana, Lacasa) eren text pla | `### Josep Torres i Clavé`, etc. (h3) | Pendent |
| 6 | 🏗️ | Noms dels altres arquitectes + dates en una sola línia | Nom com `### ` i dates en línia separada | Pendent |
| 7 | ➖ | Anys `1928 / 1929 / ... / 1938` dins `## Llistat` | Eliminats (el llistat real es genera des de les fitxes individuals) | Pendent |
| 8 | ✏️ | `## Plànol Descarregable` | `## Plànol descarregable` | Pendent |
| 9 | ✏️ | `## Més Informació Sobre Josep Lluís Sert I El Gatcpac` | `## Més informació sobre Josep Lluís Sert i el GATCPAC` | Pendent |
| 10 | ⚠️ | `Visites:` (incomplet, sense links) | Afegits: Casa Bloc → museudeldisseny.cat / Fundació Joan Miró → fmirobcn.org / Pavelló de la República → ub.edu | **Confirmar URLs correctes** |

---

## 5. Publicació: Interiors d'illa — Jardins interiors de l'Eixample. 2018

**URL:** `/publicacions/interiors-illa/`
**Fitxer:** `content/ca/publicacions/interiors-illa/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols de secció en Title Case: `## La Ciutat Emmurallada`, `## El Pla D'Eixample De Cerdà`, `## La Perversió Del Pla`, `## Les Primeres Reivindicacions`, `## La Recuperació De L'Esperit De Cerdà`, `## Horaris D'Obertura Habituals` | Corregits a minúscules correctes en català | Pendent |
| 2 | ➖ | `## Llistat` (buit) | Mantingut buit (el llistat es genera dinàmicament) | Pendent |

---

## 6. Publicació: Poblenou — Patrimoni industrial. 2019

**URL:** `/publicacions/poblenou/`
**Fitxer:** `content/ca/publicacions/poblenou/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols en Title Case: `## Nivells De Protecció Del Patrimoni`, `## Llegenda Categories`, `## Recursos Relacionats` | Corregits a minúscules | Pendent |
| 2 | ➖ | `## Llistat` contenia 5 categories de placeholder (Xemeneies, Fàbriques, Fàbriques amb xemeneia, Recintes industrials, Altres edificis) | Eliminats (el llistat es genera dinàmicament) | Pendent |

---

## 7. Publicació: 50–75 — Arquitectura Moderna a Barcelona. 2019

**URL:** `/publicacions/50-75/`
**Fitxer:** `content/ca/publicacions/50-75/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols en Title Case: `## Escola De Barcelona`, `## Llista D'Acrònims`, `## Quaderns / Cuadernos De Arquitectura…` | Corregits a minúscules | Pendent |
| 2 | 🏗️ | Noms de citants (Francesc Mitjans, Josep M. Sostres, José Antonio Coderch) en text pla | Convertits a `### ` (h3) | Pendent |
| 3 | 🏗️ | 7 acrònims en text pla (CIAM, FAD, ETSAB...) | Convertits a `### ` (h3) | Pendent |
| 4 | ➖ | `## Llistat` contenia 26 anys (1950–1975) com a marcadors | Eliminats (el llistat es genera dinàmicament) | Pendent |

---

## 8. Publicació: Mercats — Mercats de Barcelona. 2019

**URL:** `/publicacions/mercats/`
**Fitxer:** `content/ca/publicacions/mercats/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Text en MAJÚSCULES `L'EVOLUCIÓ URBANA…` | Convertit a cursiva i minúscules | Pendent |
| 2 | ✏️ | Títols en Title Case: `## L'Arquitectura Dels Mercats`, `## Els Mercats No Alimentaris`, `## Dades Estadístiques` | Corregits a minúscules | Pendent |
| 3 | 🏗️ | 4 subtipologies arquitectòniques en text pla | Convertides a `### ` (h3) | Pendent |
| 4 | 🏗️ | Barris de primer nivell dins `## Llistat` (Ciutat Vella, Eixample, Antics municipis…) en text pla | Convertits a `### ` (h3) amb contingut explicatiu conservat | Pendent |
| 5 | 🏗️ | Barris de segon nivell (Sants, Sarrià, Sant Gervasi, Gràcia, Horta, Sant Andreu, Sant Martí) | Convertits a `#### ` (h4) | Pendent |

---

## 9. Publicació: Barceloneta — La Barceloneta. 2020

**URL:** `/publicacions/barceloneta/`
**Fitxer:** `content/ca/publicacions/barceloneta/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols en Title Case: `## El Naixement D'Un Nou Barri`, `## El Projecte Urbanístic`, `## La Industrialització Del Segle Xix`, `## Les Transformacions Pels Jocs Olímpics`, `## «Configuracions Urbanes»…`, `## Nivells De Protecció Del Patrimoni` | Corregits a minúscules (`XIX` mantingut en majúscules) | Pendent |
| 2 | ➖ | `## Llistat` contenia placeholders "Arquitectura" i "Art públic" | Eliminats (el llistat es genera dinàmicament) | Pendent |

---

## 10. Publicació: Marina — La Marina del Port. 2023

**URL:** `/publicacions/marina/`
**Fitxer:** `content/ca/publicacions/marina/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols en Title Case: `## Evolució Històrica`, `## Nivells De Protecció Del Patrimoni`, `## Crèdits I Agraïments` | Corregits a minúscules | Pendent |
| 2 | ✏️ | Text LLEGENDA + VERD/VERMELL en majúscules | Convertit a cursiva i minúscules | Pendent |
| 3 | 🏗️ | 3 subseccions de Crèdits en text pla (Alumnes participants, Docents, Agraïments) | Convertides a `### ` (h3) | Pendent |
| 4 | ➖ | `## Llistat` (buit) | Mantingut buit (el llistat es genera dinàmicament) | Pendent |

---

## 11. Publicació: Tàpies — La Barcelona de Tàpies. 2024

**URL:** `/publicacions/tapies/`
**Fitxer:** `content/ca/publicacions/tapies/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ⚠️ | El fitxer tenia un únic paràgraf introductori sense cap secció `## ` | Afegit `## Introducció` per al paràgraf existent | **Confirmar si el contingut és complet** |
| 2 | ➕ | No existien seccions `## Llistat`, `## Plànol Descarregable`, `## Bibliografia Relacionada` | Afegides com a seccions buides (marcades com PENDENT) | **Cal afegir contingut** |

---

## 12. Publicació: Masies — Masies de Barcelona. 2025

**URL:** `/publicacions/masies/`
**Fitxer:** `content/ca/publicacions/masies/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Text en MAJÚSCULES `LES MASIES DE BARCELONA…` | Convertit a cursiva i minúscules | Pendent |
| 2 | ✏️ | Títols en Title Case: `## Informació Històrica`, `## El Graó Barceloní…`, `## Tipologies Arquitectòniques…`, `## Els Rellotges De Sol…` | Corregits a minúscules | Pendent |
| 3 | 🏗️ | 3 tipologies arquitectòniques en text pla | Convertides a `### ` (h3) | Pendent |
| 4 | ➖ | `## Llistat` contenia 8 noms de barri (Sants-Montjuïc, Les Corts, Sarrià–Sant Gervasi, Gràcia, Horta-Guinardó, Nou Barris, Sant Andreu, Sant Martí) | Eliminats (el llistat es genera dinàmicament) | Pendent |
| 5 | ➕ | Descripció a `/en-paper/` incompleta | Afegida basant-se en el text introductori de la pàgina de la publicació | Pendent |

---

## 13. Publicació: Biblioteques — Biblioteques de Barcelona. 2025

**URL:** `/publicacions/biblioteques/`
**Fitxer:** `content/ca/publicacions/biblioteques/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Text en MAJÚSCULES `HISTÒRIA DE LES BIBLIOTEQUES…` i `ELS NOMS DE LES BIBLIOTEQUES…` | Convertits a cursiva i minúscules | Pendent |
| 2 | 🏗️ | 2 títols `## Model I Objectius` i `## Arquitectura Al Servei Del Coneixement` (subseccions de "La xarxa de biblioteques") | Convertits a `### ` (h3) | Pendent |
| 3 | 🏗️ | 2 títols `## Biblioteques Singulars` i `## Les Biblioteques Socials` (subseccions de "Altres biblioteques") | Convertits a `### ` (h3) | Pendent |
| 4 | ➖ | `## Llistat` contenia 10 noms de districte (Ciutat Vella, Eixample, Sants–Montjuïc…) | Eliminats (el llistat es genera dinàmicament) | Pendent |

---

## 14. Publicació: New Babylon — La New Babylon de Constant. 2026

**URL:** `/publicacions/new-babylon/`
**Fitxer:** `content/ca/publicacions/new-babylon/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ⚠️ | El fitxer tenia un únic paràgraf introductori sense cap secció `## ` | Afegit `## Introducció` per al paràgraf existent | **Confirmar si el contingut és complet** |
| 2 | ➕ | No existien seccions `## Llistat`, `## Plànol Descarregable`, `## Bibliografia Relacionada` | Afegides com a seccions buides (marcades com PENDENT) | **Cal afegir contingut** |

---

## 15. Publicació: 76–08 — Arquitectura a Barcelona 1975–2008. 2026

**URL:** `/publicacions/76-08/`
**Fitxer:** `content/ca/publicacions/76-08/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols en Title Case: `## Model Barcelona`, `## El Restabliment Democràtic`, `## La Recuperació De L'Espai Públic`, `## Àrees De Nova Centralitat`, `## Els Grans Esdeveniments` | Corregits a minúscules | Pendent |
| 2 | ➖ | `## Llistat` (buit) | Mantingut buit (el llistat es genera dinàmicament) | Pendent |

---

## 16. Publicació: 09–25 — Arquitectura a Barcelona 2010–2025. 2026

**URL:** `/publicacions/09-25/`
**Fitxer:** `content/ca/publicacions/09-25/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Títols en Title Case: `## La Crisi Del 2008`, i 4 més | Corregits a minúscules | Pendent |
| 2 | ✏️ | Text en MAJÚSCULES `RECUPERAR, REHABILITAR…` | Convertit a cursiva | Pendent |
| 3 | 🏗️ | 3 títols d'exposicions en text pla | Convertits a `### ` (h3) | Pendent |
| 4 | ➖ | `## Llistat` (buit) | Mantingut buit (el llistat es genera dinàmicament) | Pendent |

---

## 17. Fitxes individuals d'elements (657 edificis)

**URL:** `/elements/<slug>/`
**URL original WP:** `https://guiesbarcelona.elglobusvermell.org/<categoria>/<nom-edifici>/`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ➕ | Sense geolocalització | Afegides coordenades lat/long i adreça per a ~570 dels 657 edificis via Nominatim/OpenStreetMap | Pendent |
| 2 | ⚠️ | 86 masies sense adreça de carrer | No geocodificades (Nominatim no les troba). Coordenades absents. | **Cal geocodificació manual** |
| 3 | ➖ | Imatges de cada edifici al WP | **No importades** — pendent d'accés al servidor (Jorge Vitoria) | ⚠️ **Pendent** |
| 4 | ✏️ | Camps del WP: nom, adreça, any, arquitectes, descripció... | Mateixos camps, amb algunes adreces normalitzades per Nominatim | Pendent |
| 5 | ⚠️ | Format original dels elements (TOML manual vs YAML automàtic) | ~67 fitxers TOML curats a mà, la resta YAML importat. Possible diferència de format. | Cal revisar |

---

## 18. Crèdits

**URL:** `/credits/`
**Fitxer:** `content/ca/credits/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ✏️ | Pàgina de crèdits del WP | Adaptat per incloure crèdit a LinuxBCN com a desenvolupadors | **Cal confirmar el text definitiu** |
| 2 | ➕ | — | Link d'administració ocult al peu (visible sols si saps que és allà) | Pendent |

---

## 19. Llicència

**URL:** `/llicencia/`
**Fitxer:** `content/ca/llicencia/_index.md`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ➖ | Secció "Codi font i dades en obert" | Eliminada per decisió de l'equip | Pendent de confirmació client |
| 2 | ⚠️ | El WP original mostrava © i CC BY-SA 4.0 simultàniament | Al web nou s'ha optat per CC BY-SA 4.0 | **Cal aclarir amb El Globus Vermell quina llicència s'aplica** |

---

## 20. Estadístiques (GoatCounter)

**URL:** `/estadistiques/`

| # | Tipus | Original | Nou | Estat |
|---|-------|----------|-----|-------|
| 1 | ➕ | No existia al WP | Pàgina nova amb dashboard d'anàlítica | Pendent |
| 2 | ⚠️ | — | Cal crear compte GoatCounter i configurar URL | Pendent tècnic |

---

## 21. Proposta: pàgina «Col·labora» ❓

**URL proposada:** `/colabora/`
**Estat:** Proposta per decidir — no implementada

### Descripció de la proposta

Afegir una pàgina de participació ciutadana on els usuaris del web puguin contribuir a millorar la qualitat de les dades del mapa. L'accés seria des d'un link discret al peu de cada fitxa d'element i/o al footer general.

### Funcionalitats possibles

| Prioritat | Funcionalitat | Descripció |
|-----------|--------------|------------|
| Alta | Notificar adreça incorrecta | L'usuari indica que les coordenades o l'adreça d'un punt del mapa no són correctes |
| Alta | Notificar informació incorrecta | L'usuari detecta un error en el nom, any, arquitectes o descripció d'un edifici |
| Mitjana | Suggerir informació nova | L'usuari proposa afegir dades que falten (foto, descripció, data, etc.) |
| Baixa | Suggerència general | Canal obert per a qualsevol altre comentari sobre el projecte |

### Implementació tècnica (si s'aprova)

Com que el web és estàtic (sense servidor propi), el formulari s'implementaria via un servei extern:

- **Formspree** (recomanat): Formulari HTML que envia els resultats a una adreça de correu. Pla gratuït suficient per al volum esperat. Sense base de dades externa.
- **Opció alternativa simple**: Link `mailto:` amb assumpte i cos pre-emplenats. Menys usable però zero dependències externes.

El formulari inclouria:
- Desplegable o cerca per seleccionar l'element afectat (nom + publicació)
- Tipus de notificació (adreça, informació, suggerència...)
- Camp de text lliure
- Correu de contacte (opcional)

### Preguntes per al client

1. **Voleu aquesta funcionalitat?** És un valor afegit per als usuaris, però requereix gestionar les notificacions rebudes.
2. **Qui gestionaria les notificacions?** Els correus arribarien a `info@elglobusvermell.org` (o altra adreça). Cal que algú les revisi periòdicament.
3. **Voleu que els usuaris puguin pujar fotos?** Afegeix complexitat. Potser millor limitar a text en una primera versió.

---

## Notes globals

### Canvis tipogràfics sistemàtics (afecten totes les publicacions)

L'import automàtic de WordPress ha convertit tots els títols de secció a "Title Case" (Primera Lletra De Cada Paraula En Majúscula), que **no és el sistema tipogràfic estàndard en català**. S'han anat corregint a mesura que s'editen les pàgines. Afecta especialment els `## Títols De Secció`.

### Contingut del Llistat a cada publicació

La secció `## Llistat` de cada publicació al WP contenia una llista estàtica d'edificis (o anys, o barris com a marcadors). Al web nou, **el llistat es genera dinàmicament** a partir de les 657 fitxes individuals importades. Si un edifici del llistat original no apareix al web nou, és perquè no s'ha importat la seva fitxa.

### Imatges

Les imatges dels edificis (fotos de portada de cada fitxa) **no s'han importat** perquè el WP original no les exposa de forma accessible via scraping. Estan pendents de l'accés al servidor de producció (Jorge Vitoria / Jordi). Fins que no s'importin, cada fitxa mostra un placeholder "Imatge pendent".
