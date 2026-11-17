# Informe — bug de «&» a les pàgines d'arquitecte

**Data:** 17/11/2026 · **Estat:** arreglat i publicat (`1920fc77`) · **Fitxers:** `themes/guiesbcn-elglobusvermell/layouts/arquitectes/term.html`

## Símptoma

Les pàgines d'arquitecte amb «&» al nom (Arriola & Fiol Arquitectes, Prince Smith & Son, SV60 Cordón & Liñán Arquitectos, Clotet, Paricio & Associats, A&EB) sortien **a vegades** sense la llista d'edificis i sense cap punt al mapa. En el moment de la investigació es veia en producció a Arriola & Fiol i a SV60 (0 edificis); Prince Smith i A&EB estaven bé. La resta de les ~283 pàgines d'arquitecte no s'hi veien afectades.

## Causa

No és cap problema de les dades ni del caràcter «&» en si. Quan un terme de la taxonomia **té fitxa pròpia** (`content/ca/arquitectes/<carpeta>/_index.md`) i la carpeta coincideix amb l'adreça del terme, Hugo 0.159–0.168 crea **dos nodes per a la mateixa adreça**:

1. el terme de la taxonomia (`term` = «Arriola & Fiol Arquitectes», amb `.Pages` = 2 edificis);
2. un node derivat de la carpeta, que agafa el nom de la carpeta com a terme (`term` = «arriola--fiol-arquitectes», `.Pages` buit).

Els dos tenen `kind: term` i la mateixa `RelPermalink`. Quin guanya depèn de l'ordre intern de mapes de Hugo: **no és determinista** (la documentació del projecte ja ho havia patit el 18/08 i el 16/11 sense arribar a la causa). Quan guanya el node de la carpeta, la plantilla rep `len .Pages == 0` i publica la pàgina amb el mapa i el llistat buits; els paràmetres de la fitxa (tipus, enllaços, descripció) sí que es fusionen, per això la capçalera i la bio sortien bé.

## Evidència

8 compilacions seguides de la mateixa versió del codi (Hugo 0.168 local; el CI fa servir 0.159), comptant edificis a `window.MAPA_PUNTS`:

| Pàgina | Compilacions amb edificis |
|---|---|
| `arriola--fiol-arquitectes` | 2 de 8 |
| `prince-smith--son` | 4 de 8 |
| `sv60-cordón--liñán-arquitectos` | 2 de 8 |
| `clotet-paricio--associats` | 0 de 8 |
| `aeb` | 8 de 8 |

Amb una sonda temporal a la plantilla es va veure que, a les compilacions dolentes, `.Data.Term` era el nom de la carpeta (en minúscules i amb guions) i `.Pages` era buit, mentre que `.Title`, els paràmetres i `site.Taxonomies.arquitectes.Get .Title` seguien sent correctes.

Dos casos són **dada, no bug**:

* `clotet-paricio--associats` («Clotet, Paricio & Associats») té 0 edificis sempre perquè cap fitxa cita aquest nom exacte; l'edifici de la Diagonal Mar cita «Clotet-Paricio» (una altra fitxa). Preguntat a Xavi al tauler.
* `aeb` no col·lideix perquè la carpeta és `a&eb` i l'adreça del terme és `aeb` (Hugo conserva el «&» quan no està envoltat d'espais).

## Arreglo

A `arquitectes/term.html`:

* si `.Pages` és buit, es busquen les pàgines a `site.Taxonomies.arquitectes` agafant el terme la pàgina del qual apunta a la mateixa `RelPermalink` (així funciona tant si guanya un node com l'altre);
* la bio d'`data/arquitectes-bio-extra.yaml` es compara amb `.Title` (que sempre és el nom bo) i no amb `.Data.Term`;
* el bucle que genera dades pel JavaScript passa a fer servir aquesta llista.

És una solució de plantilla: no toca cap fitxa, no canvia cap adreça i no depèn de la versió de Hugo.

## Verificació

* 6 compilacions seguides: Arriola 2/2, Prince Smith 1, SV60 1, A&EB 1, Sert 8, Toyo Ito 2 (estables).
* 1315 pàgines i 768 àlies, idèntics a abans.
* Deploy i Accessibilitat (pa11y-ci) en verd; verificat en viu al staging.

## Pendent

* Decidir si es pot eliminar la causa (moure les fitxes d'arquitecte fora de l'arbre de contingut de la taxonomia) — no es fa perquè afectaria l'editor i l'organització del contingut.
* Reportar-ho a Hugo si es vol: els dos nodes no haurien de competir per la mateixa adreça.
