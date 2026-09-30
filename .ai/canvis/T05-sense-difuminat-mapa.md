# T05 — Eliminar difuminat d'elements en seleccionar un plànol

**Data:** 2026-09-30
**Estat:** Aplicat

## 1. Tasca demanada

> "Preferim que quan selecciones un plànol guia no quedin la resta d'elements difuminats."

Font: correu Xavi, secció MAPA, feedback 30/9/2026.

## 2. Solució prevista

Igualar `OPACITAT_ATENUADA` a `OPACITAT_RESSALTADA`. El filtre continua funcionant internament (el codi sap quins elements pertanyen a quin plànol) però visualment tots els marcadors mantenen sempre la mateixa opacitat, sigui quin sigui l'estat del filtre.

## 3. Estat de l'execució

Aplicat el 2026-09-30.

## 4. Fitxers modificats

### `themes/guiesbcn-elglobusvermell/assets/js/mapa.js`

**Línia 321:**
```js
// Abans
var OPACITAT_ATENUADA   = { opacity: 0.12, fillOpacity: 0.12 };

// Després
var OPACITAT_ATENUADA   = OPACITAT_RESSALTADA;
```

## 5. Resultat final

Quan es selecciona un plànol, tots els elements del mapa mantenen la plena opacitat. Ja no hi ha difuminat.

## 6. Aprovació

Pendent de validació Xavi.

---

**Nota de criteri:** Joan i LinuxBCN no comparteixen aquesta decisió. El difuminat dels elements no pertanyents al plànol seleccionat ajudava l'usuari a distingir clarament els elements de la guia activa sense perdre la visió del volum total del projecte. S'aplica per decisió explícita del client.
