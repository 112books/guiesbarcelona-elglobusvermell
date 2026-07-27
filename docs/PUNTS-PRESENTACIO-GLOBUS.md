# Punts per a la primera presentació a El Globus Vermell

**Data:** 2026-07-27
**Objectiu:** és la primera vegada que Globus veu l'esborrany de Hugo — ensenyar per on van els trets, no és versió final. Aquest document recull els punts a confirmar amb ells, organitzats per bloc.

---

## 1. Direcció estètica

Idea aplicada: cada guia ("publicació") té un color propi (veure `data/publicacions.yaml`, extret de la portada del llibre), i aquest color s'usa per pintar la seva categoria/capa corresponent al mapa.

**Confirmar:** anem ben encaminats estèticament amb aquesta idea?

---

## 2. Navegació del mapa i accés a la informació de cada submapa

Estat actual:

- **Portada**: mapa general amb totes les categories pintades alhora.
- Just a sota, llistat de **"Publicacions"** (nom provisional — no seguríem que aquest sigui el nom definitiu; entenem que és una relació directa mapa = publicació, amb l'excepció de New Babylon i Tàpies — veure `DUBTES-PENDENTS-EQUIP.md` punt 1).
- **"TOTS"**: marca/desmarca de cop totes les categories del mapa.
- Cada categoria mostra el **nombre de punts** que conté.
- **Proposta**: icona "i" a cada categoria → porta a la pàgina final d'aquell mapa concret (mateix mapa però filtrat només amb els seus punts, amb tota la informació presentada tal com es veu ara a l'esborrany).
- **Filtre de Temes transversals**: mateix comportament (marcar/desmarcar), en paral·lel al de categories.
- Per a usuaris menys "de mapa": **cercador lliure** + filtres per **Època** i **Arquitecte**.
- Al final de la pàgina: **llista alfabètica amb efecte acordió**, tots els punts ordenats per lletra.

**Confirmar:** aquest patró de navegació (categories pintades → icona "i" → pàgina de submapa; TOTS; cercador+filtres; llista alfabètica) els sembla bé, o proposen una altra manera d'arribar a la informació de cada mapa? Recordar: **mobile-first** — ha de funcionar còmodament amb el dit en pantalla petita.

---

## 3. Capçalera (header)

| Element | Estat |
|---|---|
| Logo | Idèntic a l'actual, link a home |
| "Mapa" | Element principal de la capçalera, també link a home |
| "Presentació" | Text breu — revisar si cal actualitzar-lo |
| "En Paper" | **Canviat**: cada guia en paper mostra ara una explicació breu + la portada del llibre; en fer clic a la portada, porta a la pàgina completa d'informació d'aquell mapa. Cal revisar que hi hagi tota la informació de cada guia (falta contrastar-ho mapa per mapa). Pendent decidir si aquí també s'han d'enllaçar les guies descarregables en PDF. |
| "Crèdits" | Revisar què ha canviat respecte l'actual |

**Pregunta oberta:** creuen oportú afegir-hi més informació a la capçalera, o es queda així?

---

## 4. Peu de pàgina (footer)

**Bloc esquerre:**
- Logotip
- Copyright
- Links a textos legals (revisar contingut)
- Decidir: **Creative Commons o ©** — quin dels dos (o combinació)

**Bloc dret:**
- Contacte: ara és un link `mailto:`. Alternativa: formulari de contacte.
- Pàgina d'accessibilitat.

**Part inferior:**
- Signatura "LinuxBCN" (com és habitual), si no hi ha cap objecció per part seva.

---

## Resum de confirmacions necessàries

- [ ] Direcció estètica (colors per guia/categoria)
- [ ] Patró de navegació del mapa (icona "i", TOTS, cercador+filtres, llista alfabètica)
- [ ] Nom definitiu de la secció "Publicacions" (o es queda així)
- [ ] Contingut de "Presentació" i "Crèdits" — revisar si cal actualitzar
- [ ] "En Paper": confirmar que cada guia té tota la seva info, i si calen enllaços a PDFs descarregables
- [ ] CC vs © al footer
- [ ] Contacte: mailto o formulari
- [ ] Conformitat amb signatura LinuxBCN al footer

*Veure també `DUBTES-PENDENTS-EQUIP.md` per als dubtes de contingut/tècnics (fotos pendents, New Babylon/Tàpies, accessos servidor).*
