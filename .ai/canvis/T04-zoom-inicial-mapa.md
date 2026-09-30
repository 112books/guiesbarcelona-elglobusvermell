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

---

## Revisió 2026-09-30 (v2) — zoom fraccionari perquè tots els punts quedin ajustats

**Motiu:** Joan indica que el mapa encara queda massa allunyat i que els punts
han de quedar "just" dins la vista.

**Diagnosi:** el `fitBounds` de Leaflet arrodonia el zoom a un enter
(`zoomSnap` per defecte = 1). Amb els punts actuals (lat 41.334–41.466,
lng 2.100–2.225), el zoom exacte és ~11,75 en escriptori; amb `zoomSnap: 1`
s'aplicava 11 i sobrava gairebé un 45% d'espai. Per això reduir el padding de
30 a 10 px no canviava el zoom percebut.

**Solució:** `zoomSnap: 0` a les opcions del mapa, de manera que `fitBounds`
pugui triar un zoom fraccionari i ajusti els punts al màxim. Padding afinat a
`[8, 8]` (radi del marcador + traç) perquè no es tallin els punts de la vora.

**Fitxers:** `themes/guiesbcn-elglobusvermell/assets/js/mapa.js`
- `L.map(mapaEl, { scrollWheelZoom: false, gestureHandling: true, zoomSnap: 0 })`
- `map.fitBounds(group.getBounds(), { padding: [8, 8] })`

**Resultat:** en escriptori el zoom inicial passa d'11 a ~11,75 (×1,69 de zoom
visual), amb tots els punts visibles. En mòbil l'efecte és petit perquè
l'amplada ja era el factor limitant.

**Estat:** aprovat per Joan (2026-09-30); pendent de validació Xavi.
