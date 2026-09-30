# T04 — Zoom inicial del mapa: tots els elements visibles sense espai buit

**Data:** 2026-09-30
**Estat:** Aplicat

## 1. Tasca demanada

> "Ens agradaria que el mapa inicial aparegués amb una mica més de zoom, ara està una mica massa allunyat."

Font: correu Xavi, secció MAPA, feedback 30/9/2026.
Criteri addicional Joan: que capiguen tots els punts però sense espai sobrant.

## 2. Solució prevista

El mapa ja usava `fitBounds` per ajustar la vista a tots els elements automàticament. El padding de 30px per costat afegia marge innecessari que feia baixar el nivell de zoom. Reduint el padding a 10px s'obté el zoom màxim possible que encara mostra tots els elements, amb un marge mínim per no tallar els marcadors dels cantons.

## 3. Estat de l'execució

Aplicat el 2026-09-30.

## 4. Fitxers modificats

### `themes/guiesbcn-elglobusvermell/assets/js/mapa.js`

**Línia 183:**
```js
// Abans
map.fitBounds(group.getBounds(), { padding: [30, 30] });

// Després
map.fitBounds(group.getBounds(), { padding: [10, 10] });
```

## 5. Resultat final

El mapa s'obre amb el zoom més ajustat possible que mostra tots els elements del projecte, sense espai buit excessiu als marges.

## 6. Aprovació

Pendent de validació Xavi.
