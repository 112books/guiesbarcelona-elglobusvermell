# Formulari de votació — Decisions pendents del projecte

**Per a:** El Globus Vermell (Xavi, Jorge) + LinuxBCN (Joan)
**Eina recomanada:** Tally.so — gratuït, sense compte per votar, resultats agregats
**Com crear-lo:** tally.so → "New form" → copiar les preguntes per blocs

---

## BLOC 1 — Estètica i disseny

### 1.1 Disseny del web de guies
*El web actual hereta els colors de cada guia en paper (groc per GATCPAC, blau per biblioteques, etc.), seguint una lògica clara. Però es podria plantejar un canvi.*
- [ ] A) **Mantenir la proposta que es veu ara** — cada publicació conserva la seva identitat de color
- [ ] B) **Indicar una paleta de colors nova** — proposareu una nova gamma i l'equip la implementarà
- [ ] C) **Indiferent / que ho decideixi l'equip de disseny**

### 1.2 Portada del web
*Proposem replantejar la portada per posar en valor que el projecte és molt més que un recull de guies o la seva versió web/webapp: és un arxiu viu de l'arquitectura barcelonina. Aquesta és una primera idea i els continguts exactes s'haurien de consensuar. Ara mateix la portada mostra directament el mapa.*
- [ ] A) **Sí, m'agrada la idea — consensuem els continguts exactes** que hi apareixeran
- [ ] B) **No, prefereixo el mapa en primer pla** — la resta d'informació accessible pels menús, com al web de producció actual
- [ ] C) **Depèn del dispositiu** — en escriptori la nova portada de presentació; en mòbil, directament el mapa

### 1.3 "El projecte en xifres"
*Una secció que mostra dades del projecte (ex: 564 edificis, 13 guies, 30 anys de recorregut). Caldria saber:*

**1.3a — On ha d'aparèixer?**
- [ ] A) **Portada** — impacte visual immediat al primer accés
- [ ] B) **Pàgina Presentació** — coherent amb l'explicació del projecte per a qui arriba per primer cop
- [ ] C) **Pàgina Crèdits** — on ja hi ha tota la informació del projecte
- [ ] D) **No mostrar-ho**

**1.3b — Quines dades voleu destacar?** *(camp de text obert — ex: nombre d'edificis, de guies, d'arquitectes, anys de recorregut, idiomes, etc.)*

---

## BLOC 2 — Contingut i drets

### 2.1 Llicència del peu de pàgina
*Ara apareix © El Globus Vermell. Algunes guies culturals usen Creative Commons.*
- [ ] A) **© tots els drets reservats** — control total sobre l'ús del contingut
- [ ] B) **Creative Commons BY-NC** — permet compartir amb crèdit, sense ús comercial
- [ ] C) **Creative Commons BY-SA** — permet compartir i adaptar amb les mateixes condicions
- [ ] D) **Decidir per cada guia per separat**

### 2.2 Autoria de les fotografies
*Cal definir com s'acrediten les fotos a les fitxes dels edificis.*
- [ ] A) **© El Globus Vermell** per a totes les fotos pròpies
- [ ] B) **Crèdit individual per fotògraf/a** — si hi ha autors/es identificats
- [ ] C) **Cap crèdit visible** — missió purament informativa
- [ ] D) **Decidir cas per cas**

### 2.3 Arquitectes combinats
*S'enviarà un document separat amb la llista de casos a revisar (arquitectes que apareixen agrupats a les fitxes i cal separar en entrades individuals). No cal decidir-ho aquí.*

→ **Pendent: document de verificació enviat a part.**

---

## BLOC 3 — Funcionalitats

### 3.1 Mapes (adreça de cada edifici)
*Quan es fa clic sobre l'adreça d'un edifici, s'obre un mapa extern. S'ha preparat un document comparat amb arguments per a cadascuna de les opcions (.ai/DECISIO-MAPES-ADRECES.md).*
- [ ] A) **Google Maps** — el més familiar, obre l'app mòbil, té Street View
- [ ] B) **OpenStreetMap** — coherent amb el web, privadesa, sense dependència comercial
- [ ] C) **Doble opció** — dos botons visibles: un per a OSM i un per a Google Maps
- [ ] D) **Indiferent**

### 3.2 Text a veu (accessibilitat per a persones amb dificultats visuals)
*Permet escoltar el contingut de les fitxes d'edifici en veu alta (WCAG 2.1). Ja hi ha una versió de prova activa al web — us recomanem que l'escolteu abans de votar: és una mica robòtica però passable.*

**Opció actual de prova:** Web Speech API — veu del sistema operatiu, zero cost.

- [ ] A) **Deixar la versió actual** — és suficient per a l'objectiu d'accessibilitat
- [ ] B) **Millorar-la amb Piper TTS** — veu neutra de qualitat, programari lliure, requereix servidor (cost addicional ~3-5 dies de feina)
- [ ] C) **No implementar text a veu** — es pot eliminar o afegir en una fase posterior
- [ ] D) **Indiferent / que ho decideixi l'equip tècnic**

### 3.3 Estadístiques d'ús (GoatCounter)
*El sistema de seguiment de visites ja és actiu: sense cookies, respectuós amb la privadesa. Ara mateix les dades les veuen Joan i Xavi.*
- [ ] A) **Mantenir-lo privat** — només accessible a l'equip
- [ ] B) **Fer el dashboard públic** — qualsevol pot veure les estadístiques del web
- [ ] C) **Indiferent**

---

## BLOC 4 — Accés al gestor de continguts (CMS)

*El web de guies té un gestor de continguts integrat que permet editar fitxes d'edificis, afegir fotos i actualitzar informació directament des del navegador, sense necessitat de coneixements tècnics. Hi ha guies senzilles per a tots els procediments, accessibles des del mateix web.*

### 4.1 Necessites un compte d'editor/a al CMS?
*Si respons que sí, t'enviarem les instruccions per crear el teu usuari a GitHub (gratuït) i t'afegirem al sistema. Rebràs la guia d'edició.*
- [ ] **Sí, vull poder editar continguts** — m'envieu les instruccions
- [ ] **No, de moment no** — ja m'ho demaneu quan calgui
- [ ] **Ja en tinc un** — tot bé

### 4.2 Necessites ser administrador/a del CMS?
*L'administrador/a pot gestionar els comptes d'altres editors/es (afegir-ne, treure'n). Sol ser una sola persona per projecte.*
- [ ] **Sí, vull ser administrador/a**
- [ ] **No, editor/a és suficient**
- [ ] **No tinc compte al CMS (vegeu 4.1)**

---

## Notes lliures

*Espai per a comentaris, matisos o idees que no caben en les opcions anteriors.*

[camp de text obert]

---

*Aquest formulari es pot crear a **tally.so** en ~20 minuts copiant les preguntes bloc a bloc.*
*Resultats: exportables a CSV o visualitzables en temps real al dashboard de Tally.*
