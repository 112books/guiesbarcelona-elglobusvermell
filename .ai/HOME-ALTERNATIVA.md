# HOME-ALTERNATIVA.md — Portada alternativa per a guiesbarcelona

Data: 2026-08-06
Estat: ⏳ Pla aprovat internament, pendent validació Xavi

---

## Objectiu

L'actual portada és el mapa interactiu amb totes les guies. Útil per a visitants
recurrents, però desorientadora per a qui arriba per primer cop sense saber
de quin projecte es tracta.

La portada alternativa ha de respondre en 3 segons a: "Qui sou? Què feu? Per on
començo?"

---

## Estructura de seccions (mobile-first, de dalt a baix)

### 1. Hero — frase contundent + dades del projecte
- Frase editorial breu i directa (a definir amb Xavi):
  ex. *"Tota l'arquitectura i l'urbanisme de Barcelona, guia a guia."*
- Tres xifres en gran: **N edificis · N guies · N anys de recerca**
  (generades automàticament des del contingut Hugo)
- CTA principal: → **Explorar el mapa**

### 2. Guia destacada (aleatòria o per visites)
- Una publicació destacada cada vegada que es carrega la pàgina
- Mostra: portada de la guia, títol, any, breu descripció, nombre d'edificis
- Dins la guia: **un edifici aleatori** amb foto (si en té) i adreça
- CTA: → **Veure tots els edificis d'aquesta guia**
- *Tècnica:* aleatori per JavaScript al client (la pàgina és estàtica).
  Futur: si tenim GoatCounter, prioritzar la guia amb més visites recents.

### 3. Accés a totes les guies
- Graella de miniatures de les 13 guies ("En paper")
- Cada targeta: portada, títol, any, nombre d'edificis
- CTA: → **Totes les guies**

### 4. Arquitecte o estudi destacat (opcional, aleatori)
- Un arquitecte o estudi aleatori de la taxonomia
- Mostra: nom, nombre d'edificis, llista dels més destacats
- Missatge implícit: el projecte va més enllà dels mapes, hi ha recerca autoral
- *Es pot ometre si Xavi considera que distreu del fil principal*

### 5. Recursos educatius *(segon nivell, mida reduïda)*
- Secció compacta, discreta
- Text breu explicant que hi ha materials per a escoles i instituts
- Llista de recursos disponibles (a definir — per ara és un placeholder)
- CTA: → **Recursos per a docents** (pàgina pendent de crear)

### 6. Tornada al mapa
- Banner o botó gran cap al mapa interactiu
- Missatge: "El mapa és la porta d'entrada a tots els edificis"

---

## Decisió de navegació: portada fixa o selector?

Dues opcions:

**A) Substituir la portada actual** per la nova i moure el mapa a `/mapa/`
— Avantatge: URL arrel = millor SEO i presentació institucional
— Inconvenient: trenca l'hàbit dels usuaris actuals

**B) Mantenir les dues portades** amb un selector discret (ja tenim el mecanisme
de propostes A/B/C al web) i decidir quin és el default
— Avantatge: no trenca res, permet provar amb usuaris reals
— Recomanat per a la fase inicial

---

## Tècnica d'implementació (Hugo estàtic)

| Element | Solució |
|---------|---------|
| Xifres automàtiques | `len (where site.Pages "Type" "elements")` al template |
| Guia aleatòria | JavaScript: `Math.random()` sobre array de guies injectat per Hugo |
| Edifici aleatori dins la guia | JavaScript: `Math.random()` sobre array d'edificis de la guia |
| Prioritat per visites | GoatCounter analytics.json (ja disponible) — fase 2 |
| Arquitecte aleatori | JavaScript: `Math.random()` sobre array de la taxonomia |
| Portada de la guia | Imatges ja a `static/img/portades/` (si existeixen) |

---

## Pendents de validació amb Xavi

- [ ] Frase editorial del hero (el text és seu)
- [ ] Vol la secció d'arquitecte aleatori?
- [ ] Vol la secció de recursos educatius ara o la deixem per més endavant?
- [ ] Opció A o B per a la navegació?
- [ ] Color/estil: neutres fins que decideixi la paleta, o tirar amb el vermell provisional?

---

## Relació amb altres tasques

- Depèn de: imatges de portada de les guies (algunes potser no existeixen)
- Facilita: SEO, presentació institucional, sol·licituds de subvenció
- Complementa: GoatCounter (si es vol prioritat per visites a la guia destacada)
