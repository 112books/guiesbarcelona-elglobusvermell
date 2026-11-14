# Resposta a Xavi — Mail 14 de novembre (observacions pràctiques)

**NOTA:** Aquesta és la resposta que enviarà Joan. Documentada aquí per a revisió prèvia.

---

Bon dia, Xavi,

He revisat totes les observacions que has enviat. Són molt útils i concises. Et deixo explicat cada punt, la probable causa, i com ho veurem de solucionar. **Insistint: no hem tocat res del projecte — tot això és només documentació de com ho farem.**

La **pèrdua de dades del llistat d'arquitectes** és el que més ens preocupa ara mateix. Et l'adreso primer.

---

## 1. **PÈRDUA DE DADES: Llistat d'arquitectes esborrat** 🔴

**Que ha passat:**
El llistat que havies començat a fer dels 92 arquitectes orfes va desaparèixer. Has hagut de tornar a començar.

**Per què probablement ha passat:**
- L'editor de Sveltia pot tenir un buffer temporal que no es desa si la sessió es tanca malament
- O els canvis no estaven guardats al servidor i s'han perdut en una actualització
- O hi ha un bug de persistència que no estàvem monitoritzant

**Com ho solventarem:**
- Dilluns, investigarem on es guarden les dades mentre estàs editant
- Veurem si hi ha un historial o backup que recuperar
- Crearem un protocol per fer backups locals dels llistats importantes (exportar a Markdown)
- Si l'editor de Sveltia no té suficient seguretat de dades, avaluarem alternatives o millores

**Urgència:** Crítica. No podem perdre treball. Prioritat número 1.

---

## 2. **Canviar nom d'edifici/element — passa alguna cosa?**

**Que vols saber:**
N'has canviat uns quants noms d'elements. Vols confirmar si trencarà algo.

**Per què pot passar:**
- Si els links interns usen el nom (slug) de l'element, renombrar-lo trencarà els links
- Si usen un ID intern, els links seguiran funcionant

**Com ho solventarem:**
- Dilluns, verificarem com estàn fets els links (slug vs ID)
- Si has canviat noms i algo s'ha trencat, ho corregim
- Documentarem la regla: si heu de renombrar, és segur; si no, cal fer redirects

---

## 3. **Intervencions: "ús actual" i "nom actual"** 

**Que demandes:**
Afegir tipus d'intervencions més flexibles. Exemple: en lloc de només "construcció", "reforma", poder dir "ús actual" o "nom actual".

**Per què és útil:**
Perquè molts edificis han canviat de funció o de nom, i això és informació important.

**Com ho solventarem:**
- Dilluns, parlarem amb El Globus Vermell sobre quins tipus d'intervencions necessiteu
- Ampliar la llista de tipos: construcció, reforma, ús actual, nom actual, etc.
- Decidir si és un dropdown de opcions fixes, o si podem afegir-ne de noves

---

## 4. **Disposició visual quan no tenim arquitecte**

**Que passa:**
Quan una intervenció no té arquitecte assignat, el layout es desplaça i es veu trencat. (Captura adjunta)

**Per què passa:**
Probable: CSS de `.fitxa-dada` (estil de les files d'informació) no maneja bé les cel·les buides. El template renderitza bé (`elements/single.html:240-243`), però el CSS pot tenir spacing rígid o flexbox que col·lapsa.

**Com ho solventarem:**
- Revisar CSS de `.fitxa-dada` en `main.css` 
- Assegurar que `<dd>` buida no causa misalignment
- Test: verificar fitxes sense arquitecte (ex: obres d'art on no hi ha arquitecte, només autoria)

---

## 5. **Format de text disparell**

**Que has vist:**
Alguns elements tienen format inconsistent (veure els exemples que has marcat).

**Per què passa:**
Probable: migració de WordPress amb HTML i Markdown barrejats, o l'editor genera formats diferents segons l'entrada.

**Com ho solventarem:**
- Audit de tots els camps de text (descripció, contingut, intervencions)
- Estandaritzar: Markdown o HTML, no barreja
- Verificar que l'editor genera output consistent

---

## 6. **Llistat d'edificis a publicacions no apareix (GATCPAC)**

**Que passa:**
A la publicació GATCPAC no apareix el llistat d'edificis. Mostra: "Encara no hi ha fitxes d'elements importades per aquesta publicació."

**On està el template:**
`publicacions/term.html:18-27`

```html
{{ if .Pages }}
  <section class="publicacio-edificis">
    ...llistat d'elements...
  </section>
  ...
{{ else }}
  <p class="publicacio-buit">Encara no hi ha fitxes d'elements importades per aquesta publicació.</p>
{{ end }}
```

**Per què passa (possibles causes):**
1. GATCPAC no té elements associats (`.Pages` és buit)
2. Els elements sí que tienen `publicacions: [gatcpac]`, però `.Pages` no els trova

**Audit necessari (dilluns):**
- Fer audit: quants elements tienen `publicacions: ["gatcpac"]`?
- Si en té: debugar per què `.Pages` no els trova
- Si no en té: comportament és correcte (mostra "sense fitxes")

---

## 7. **Línia vertical a esquerra de biografies d'arquitectes** 🎨

**Que no agrada:**
La línia vertical que surt a l'esquerra de la biografia (exemple: Josep Lluís Sert).

**On està:**
CSS `main.css:601` — Classe `.arquitecte-bio`

```css
.arquitecte-bio {
  margin: var(--space-md) 0;
  padding: var(--space-sm) var(--space-md);
  border-left: 3px solid var(--color-accent);  /* ← aquesta línia */
  color: var(--color-text);
}
```

**Per què la tenim:**
Element de disseny visual com a accent / decoració a les biografies.

**Com ho solventarem:**
- **REQUEREIX APROVACIÓ TEVA I D'EL GLOBUS VERMELL**
- Solució: eliminar `border-left: 3px solid var(--color-accent);` de la classe
- Dilluns ho mirem en pantalla per decidir si vol altre decoració

---

## 8. **Línia vertical a llistat d'arquitectes + falta de compacitat** 🎨

**Que no agrada:**
Quan es llisten elements amb els seus arquitectes, surt una línia vertical. A més, les tres informacions (nom element, adreça, arquitectes) està molt separades.

**On està:**
CSS `main.css:1273-1289` — Classe `.llistat-element-arquitectes`

```css
.llistat-element-arquitectes {
  width: 100%;
  padding-left: 1.5rem;        /* ← causa separació */
  font-size: 0.8125rem;
  color: #767676;
  margin-top: 0.25rem;
  border-left: 2px solid var(--color-border, #e0e0e0);  /* ← aquesta línia */
}
```

**Per què passa:**
- Línia decorativa lateral
- Padding-left i margin-top causaven espai excessiu

**Com ho solventarem:**
- **REQUEREIX APROVACIÓ TEVA I D'EL GLOBUS VERMELL**
- Eliminar `border-left: 2px`
- Reduir `padding-left` (actualment 1.5rem)
- Ajustar `margin-top` per compactat
- Dilluns ho mirem en pantalla

---

## 9. **Arquitecte a llistat no porta a fitxa individual** 🔴

**Que passa:**
Quan cliques en un arquitecte dins d'un llistat d'elements, no vas a la fitxa de l'arquitecte, sinó a la pàgina general /arquitectes/.

**Per què passa:**
Bug de JavaScript a `mapa.js:1084`. Quan l'array `arqUrls` no té URL per a un arquitecte, fa fallback a `/arquitectes/` (pàgina general).

```javascript
// mapa.js:1084
arqLink.href = arqUrls[idx] || ((window.SITE_BASE || '/') + 'arquitectes/');
```

El problema és que `arqUrls[idx]` pot ser undefined si no hi ha URL per a aquell índex, causant el fallback.

**Com ho solventarem:**
- Opció A: Assegurar que `arqUrls` sempre té exactament el mateix nombre d'elements que `arquitectes`
- Opció B: Generar la URL en JavaScript si no existeix (usar same urlize logic)
- Resultat: cada click va a `/arquitectes/nom-arquitecte/` correctamente

---

## 10. **Canvi copiar portada**

**Que demandes:**
Canviar "Una eina crítica per llegir Barcelona a través de **la seva arquitectura**, l'art..."
Per: "Una eina crítica per llegir Barcelona a través de **l'arquitectura**, l'art..."

**Com ho solventarem:**
- Trobar on es defineix aquest text (probable: config/*/params.toml o content/_index.md)
- Fer el canvi
- Verificar que es mostra correctament

---

## 11. **Franja color + text negre a temes** 🎨

**Que passa:**
Apareix una franja de color (exemple: blau a Biblioteques) dalt de la pàgina de la publicació. El títol no és completament negre.

**On està:**
CSS `main.css:2392-2406` — Classes `.publicacio-banda` i `.publicacio-cap h1`

```css
.publicacio-banda {
  height: 30px;
  background: var(--pub-color, var(--color-accent));  /* ← franja de color */
  margin: 0 calc(-1 * var(--space-md)) var(--space-lg);
}

.publicacio-cap h1 {
  margin: 0 0 0.25rem;
  color: color-mix(in srgb, var(--pub-color, var(--color-text)), #000 45%);  /* ← no és 100% negre */
}
```

**Per què passa:**
- Franja de color heretada del pub-color (blau per biblioteques, etc.)
- Títol h1 usa `color-mix` que barreja el color de la publicació amb negre al 45%, no llegeix com a negre pur

**Com ho solventarem:**
- **REQUEREIX APROVACIÓ TEVA I D'EL GLOBUS VERMELL**
- Canviar h1 color a `#000` (negre pur)
- Decidir: mantenir franja o eliminar-la?
- Revisar contrast WCAG si canviem
- Dilluns ho mirem en pantalla

---

## 12. **Enllaços relacionats: selecció i estètica**

**Que passes:**
Primers, no saps com estan triats els enllaços relacionats (sota del plànol).
Segons, quan el nom de l'element és molt llarg, la fila es trenca estèticament.
Exemples: [biblioteca pública Arus] es trenca, [biblioteca Prosperitat] va bé.

**Per què passa:**
- Lògica de selecció: probablement automàtica (per tags, mateixa guia)
- Estètica: falta word-wrap o overflow handling

**Com ho solventarem:**
- Documentar: com es seleccionen els relacionats? Automàtica? Manual?
- Revisar CSS: com es comporta el text long? Truncar? Wrap? Reduir font?
- **POSSIBLEMENT REQUEREIX APROVACIÓ** si és canvi de disseny
- Dilluns ho mirem en pantalla

---

## RESUM I PRÒXIMS PASSOS

| Punt | Categoria | Crítico? | Ubicació | Acció |
|------|-----------|----------|----------|-------|
| **Link arquitecte** | Bug | 🔴 | `mapa.js:1084` | Corregir fallback href a `/arquitectes/` |
| **Pèrdua dades** | Bug | 🔴 | Sveltia backend | Investigar + backup protocol |
| Disposició s/arq | Layout | 🟡 | `main.css` `.fitxa-dada` | Revisar spacing CSS |
| GATCPAC elements | Pregunta | 🟡 | `publicacions/term.html:18` | Verificar `.Pages` |
| Format text | Inconsistència | 🟡 | Múltiples `.md` | Audit + estandaritzar |
| Intervencions tipus | Funcionalitat | 🟡 | `content/*.md` schema | Decidir amb client |
| **Línia biografia** | Disseny | 🎨 | `main.css:601` `.arquitecte-bio` | Eliminar `border-left: 3px` |
| **Línia llistat** | Disseny | 🎨 | `main.css:1279` `.llistat-element-arquitectes` | Eliminar `border-left: 2px` + ajustar padding |
| **Franja + text** | Disseny | 🎨 | `main.css:2405` `.publicacio-cap h1` | Canviar color a `#000` pur |
| Noms llargs | Estètica | 🟢 | CSS links | Decidir truncar/wrap |
| Copiar portada | Contingut | ✅ | `_index.md:3` | Eliminar "seva" del tagline |
| Canvi nom element | Pregunta | ✅ | Estructura slugs | Confirmar funciona bé |

**Bloqejos críticos:** Link arquitecte (línies 1079-1087) + pèrdua de dades

**Requereixen aprovació client (disseny):** Punts 7, 8, 9

---

## DILLUNS A NAU BOSTIC (10:00)

Mirarem en pantalla tots aquests punts, prioritzarem, i decidiran quins es fan primer.

Recomanació: porta una llista dels 92 arquitectes orfes en cas que la perdis de nou (o la fem backup aquí).

Seguim!

