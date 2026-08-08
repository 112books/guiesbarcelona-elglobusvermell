# Formulari de votació — Decisions pendents del projecte

**Per a:** El Globus Vermell (Xavi, Jorge) + LinuxBCN (Joan)
**Eina recomanada:** Tally.so — gratuït, sense compte per votar, resultats agregats
**Com crear-lo:** tally.so → "New form" → copiar les preguntes per blocs

---

## BLOC 1 — Estètica i disseny

### 1.1 Disseny del web de guies
*El web actual usa colors per identificar cada guia (groc per GATCPAC, blau per biblioteques, etc.).*
- [ ] A) **Mantenir els colors per guia** — cada publicació té la seva identitat de color
- [ ] B) **Nou rebrand unificat** — un sol disseny per a totes les guies, amb més coherència
- [ ] C) **Indiferent / que ho decideixi l'equip tècnic**

### 1.2 Portada del web
*Ara la portada posa el mapa en primer pla.*
- [ ] A) **Mantenir el mapa com a element central** — és el corazón del projecte
- [ ] B) **Nova portada de presentació** — frase contundent, guia destacada, accés al mapa des de la navegació
- [ ] C) **Indiferent**

### 1.3 "El projecte en xifres" (número d'edificis, guies, anys)
*On ha d'aparèixer aquest element?*
- [ ] A) **Portada** — impacte visual immediat
- [ ] B) **Pàgina Presentació** — coherent amb l'explicació del projecte
- [ ] C) **Pàgina Crèdits** — on ja hi ha tota la informació del projecte
- [ ] D) **No mostrar-ho**

---

## BLOC 2 — Contingut i drets

### 2.1 Llicència del peu de pàgina
*Ara apareix © El Globus Vermell. Algunes guies alternatives uses Creative Commons.*
- [ ] A) **© tots els drets reservats** — control total sobre l'ús del contingut
- [ ] B) **Creative Commons BY-NC** — permet compartir amb crèdit, sense ús comercial
- [ ] C) **Creative Commons BY-SA** — permet compartir i adaptar amb les mateixes condicions
- [ ] D) **Decidir per cada guia per separat**

### 2.2 Autoria de les fotografies
*Cal afegir crèdit a les fotos de les fitxes dels edificis.*
- [ ] A) **© El Globus Vermell** per a totes les fotos pròpies
- [ ] B) **Crèdit individual per fotògraf/a** — si hi ha autors/es identificats
- [ ] C) **Cap crèdit visible** — missió purament informativa
- [ ] D) **Decidir cas per cas**

### 2.3 Arquitectes combinats
*Hi ha ~73 fitxes d'edifici on els arquitectes apareixen agrupats (ex: "Clotet-Paricio"). Cal separar-los en camps individuals per a les pàgines d'arquitecte.*
- [ ] A) **LinuxBCN fa la separació automàticament** — ràpid però pot tenir errors
- [ ] B) **Xavi revisa la llista primer i confirma** — més precís però requereix temps de Xavi
- [ ] C) **Indiferent / que ho decideixi LinuxBCN**

---

## BLOC 3 — Funcionalitats

### 3.1 Mapes (adreça de cada edifici)
*Quan es fa clic sobre l'adreça d'un edifici, s'obre un mapa extern. Vegeu .ai/DECISIO-MAPES-ADRECES.md per als arguments complets.*
- [ ] A) **Google Maps** — el més familiar, obre l'app mòbil, té Street View
- [ ] B) **OpenStreetMap** — coherent amb el web, privadesa, sense dependència comercial
- [ ] C) **Doble opció** — dos botons: un per a OSM i un per a Google Maps
- [ ] D) **Indiferent**

### 3.2 Text a veu (accessibilitat per a persones amb dificultats visuals)
*Permet escoltar el contingut de les fitxes d'edifici en veu alta. WCAG 2.1 ho recomana.*
- [ ] A) **Web Speech API** — gratuïta, veu del sistema operatiu, implementació: 1-2 dies
- [ ] B) **Piper TTS** — veu neutra de qualitat, programari lliure, requereix servidor (3-5 dies + cost)
- [ ] C) **No implementar ara** — es pot afegir en una fase posterior
- [ ] D) **Indiferent / que ho decideixi l'equip tècnic**

### 3.3 Secció "En paper"
*La pàgina que llista les guies impreses. Ara té portada de cada guia.*
- [ ] A) **Portada + botó de descàrrega PDF** per a cada guia i idioma
- [ ] B) **Només la portada** — sense PDF descarregable per ara
- [ ] C) **Portada + informació ampliada** (descripció de la guia, preu, on comprar)

### 3.4 Estadístiques d'ús (GoatCounter)
*El sistema de seguiment de visites (sense cookies, respectuós amb la privadesa) ja és actiu.*
- [ ] A) **Mantenir-lo privat** — només el veuen Xavi i Joan
- [ ] B) **Fer el dashboard públic** — qualsevol pot veure les estadístiques del web
- [ ] C) **Indiferent**

---

## BLOC 4 — Tècnic i infraestructura

### 4.1 Correu electrònic del projecte
*Ara s'usa un Gmail informal. Quan el servidor estigui llest, cal decidir.*
- [ ] A) **IMAP al servidor propi** (Dinahosting) — correu @elglobusvermell.org, control total
- [ ] B) **Etik** — proveïdor de correu ètic europeu, ~3€/mes
- [ ] C) **Seguir amb Gmail** — zero canvis, zero cost
- [ ] D) **Decidir quan tinguem el servidor**

### 4.2 Backoffice de l'app (gestor de contingut intern)
*Ara existeix un backoffice en Node.js per gestionar les dades de l'app.*
- [ ] A) **Mantenir el Node.js actual** — menys canvis, però cal manteniment
- [ ] B) **Substituir-lo per Sveltia CMS** — ja integrat al web de guies, una sola eina
- [ ] C) **Reescriure de zero** — si el Node.js actual té deute tècnic significatiu
- [ ] D) **Decidir en la fase de Flutter**

### 4.3 Base de dades de l'app
*Cal decidir l'arquitectura quan s'iniciï el sprint Flutter.*
- [ ] A) **PostgreSQL** — potent, escalable, estàndard professional
- [ ] B) **SQLite** — simple, sense servidor, suficient per a aquest volum de dades
- [ ] C) **Decidir en la fase de Flutter amb més context**

---

## BLOC 5 — Recursos i calendari

### 5.1 Pressupost app Flutter (3.900€)
- [ ] A) **Confirmat** — podem iniciar quan tinguem el servidor i la Google Maps API Key
- [ ] B) **Cal revisar-lo** — vull parlar-ne amb Joan abans de confirmar
- [ ] C) **En espera** — fins que resolem els blocants (Jorge, Google Maps Key)

### 5.2 Bestreta del 50% per iniciar Flutter
- [ ] A) **La pago ara** — per reservar el sprint
- [ ] B) **La pago quan iniciem el sprint** — quan tots els blocants estiguin resolts
- [ ] C) **Prefereixo una altra estructura de pagament**

---

## Notes lliures

*Espai per a comentaris, matisos o idees que no caben en les opcions anteriors.*

[camp de text obert]

---

*Aquest formulari es pot crear a **tally.so** en ~20 minuts copiant les preguntes bloc a bloc.*
*Resultats: exportables a CSV o visualitzables en temps real al dashboard de Tally.*
