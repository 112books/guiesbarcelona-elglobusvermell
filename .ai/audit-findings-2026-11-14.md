# Audit Findings — Novembre 2026

Audits sistemàtics de cada punt que va reportar Xavi, **sense tocar res de codi**. Cada punt documenta la causa concreta i la ubicació exacta del codi.

---

## 1. 🔴 CRÍTICO: Link arquitecte a llistat (vai a pàgina general en lloc de fitxa individual)

**Ubicació:** `themes/guiesbcn-elglobusvermell/assets/js/mapa.js:1084`

**Codi actual:**
```javascript
arqLink.href = arqUrls[idx] || ((window.SITE_BASE || '/') + 'arquitectes/');
```

**Problema:**
- Quan `arqUrls[idx]` és undefined (no existeix URL per a aquest arquitecte), fa fallback a `/arquitectes/` (pàgina general)
- La variable `arqUrls` es passa de template (`arquitectes_urls`), però possiblement té índexs buits o no coincideix amb `arquitectes`
- Resultat: clics al nom d'arquitecte van a `/arquitectes/` en lloc de `/arquitectes/nom-arquitecte/`

**Verificació:**
- Template `elements/list.html:35` passa `arquitectes_urls` correctament
- Partial `arquitectes-urls.html` genera URLs correctes (urlize dels noms)
- El bug és en el fallback del JavaScript quan no hi ha URL

**Solució proposada:**
- Verificar si `arqUrls` és realment undefined o buit
- Opció A: Generar la URL al JavaScript si no existeix (usar mismo urlize logic)
- Opció B: Assegurar que `arqUrls` sempre té el mateix nombre d'elements que `arquitectes`

---

## 2. 🎨 DISSENY: Línia vertical a esquerra de biografies d'arquitectes

**Ubicació:** `themes/guiesbcn-elglobusvermell/assets/css/main.css:601`

**Codi actual:**
```css
.arquitecte-bio {
  margin: var(--space-md) 0;
  padding: var(--space-sm) var(--space-md);
  border-left: 3px solid var(--color-accent);
  color: var(--color-text);
}
```

**Problema:**
- Línia blava (o del color accent) a l'esquerra de cada biografia
- Xavi diu que no agrada

**Solució proposada:**
- **REQUEREIX APROVACIÓ EXPLÍCITA** per CLAUDE.md
- Opcions: eliminar `border-left` completament, o substituir per altra decoració
- Línea: una sola, que esborri aquesta propietat CSS

---

## 3. 🎨 DISSENY: Línia vertical a llistat d'arquitectes + falta de compacitat

**Ubicació:** `themes/guiesbcn-elglobusvermell/assets/css/main.css:1279`

**Codi actual:**
```css
.llistat-element-arquitectes {
  width: 100%;
  padding-left: 1.5rem;
  font-size: 0.8125rem;
  color: #767676;
  margin-top: 0.25rem;
  border-left: 2px solid var(--color-border, #e0e0e0);
}
```

**Problema:**
- Línia gris a l'esquerra dels noms d'arquitectes al llistat d'elements
- Spacing excessiu (padding-left: 1.5rem, margin-top: 0.25rem) provoca que les tres informacions (nom, adreça, arquitectes) estiguin allunyades

**Solució proposada:**
- **REQUEREIX APROVACIÓ EXPLÍCITA**
- Eliminar `border-left: 2px`
- Revisar spacing: reduir `padding-left` i ajustar `margin-top` per compacitat
- Considerar grid/flexbox layout més serrat

---

## 4. 🔴 CRÍTICO: Disposició visual quan no tenim arquitecte (layout broken)

**Ubicació:** `themes/guiesbcn-elglobusvermell/layouts/elements/single.html:240-243`

**Template actual:**
```html
<div class="fitxa-dada">
  <dt>{{ .tipus | title }}</dt>
  <dd>{{ with $autorsHTML }}{{ . | safeHTML }}{{ end }}{{ with .any }}{{ if $autors }}, {{ end }}{{ . }}{{ end }}{{ with .descripcio }}<br>{{ . }}{{ end }}</dd>
</div>
```

**Problema:**
- Quan no hi ha arquitecte/autors, el `<dd>` pot quedar buit o amb spacing irregular
- Flexbox/grid CSS pot causar misalignment

**Audit necessari:**
- Veure captura de Xavi: necessito verificar el CSS de `.fitxa-dada` i veïns
- CSS `main.css`: cercar `.fitxa-dada` per veure com s'estira o col·lapsa

**Solució proposada:**
- Revisar CSS de `.fitxa-dada` per assegurar que funciona bé quan `<dd>` és buit
- Afegir `display: contents` o similar si necessari

---

## 5. 🟡 FUNCIONALITAT: Intervencions: afegir tipus "ús actual" i "nom actual"

**Ubicació:** `content/ca/elements/*.md` — schema de `intervencions`

**Estructura actual:**
```yaml
intervencions:
  - tipus: Projecte
    autors: [...]
    any: '1933'
    descripcio: ''
```

**Problema:**
- El camp `tipus` actualment es limita a opcions com "Projecte", "reforma", etc.
- Xavi demanda poder afegir "ús actual" o "nom actual"

**Audit necessari:**
- Verificar quins `tipus` existeixen actualment (audit d'all `intervencions.tipus` únics)
- Decidir: és un dropdown predefinit o text lliure?
- Si és dropdown, quin és el llista completa que necessitem?

**Solució proposada:**
- Expandir schema: afegir més `tipus` autoritzats (o fer flexible)
- Decidir amb client sobre tots els `tipus` necessaris

---

## 6. 📋 FORMAT TEXT: Inconsistència a alguns elements

**Ubicació:** Múltiples fitxes `content/ca/elements/*.md`

**Problema:**
- Alguns camps de text tienen format HTML, d'altres Markdown, altres text pla
- Xavi reporta formato disparell en elements com "Casa Bloc"

**Audit necessari:**
- Revisar camps: `descripcio`, `descripcio_nomenclator`, `intervencions.descripcio`
- Verificar si contenen HTML tags (`<br>`, `<p>`, etc.) o Markdown

**Solució proposada:**
- Estandaritzar: escollit un format (preferiblement Markdown)
- Migrar tots els camps al format escollit
- Assegurar que template renderitza correctament

---

## 7. ❓ PREGUNTA: Llistat d'edificis a publicacions no apareix (GATCPAC)

**Ubicació:** `themes/guiesbcn-elglobusvermell/layouts/publicacions/term.html:18-27`

**Template actual:**
```html
{{ if .Pages }}
  <section class="publicacio-edificis">
    ...
  </section>
  ...
{{ else }}
  <p class="publicacio-buit">Encara no hi ha fitxes d'elements importades per aquesta publicació.</p>
{{ end }}
```

**Problema:**
- GATCPAC mostra missatge "Encara no hi ha fitxes"
- Però Xavi diu que hauria de tenir elements

**Audit necessari:**
- Verificar: Té GATCPAC elements associats?
- Fer audit: quants elements té `publicacions: ["gatcpac"]` en els seus front-matter?
- Si en té, per què no es mostren? (possiblement `.Pages` no és correcte?)

**Solució proposada:**
- Verificar count d'elements GATCPAC
- Si té elements, debugar per què `.Pages` és buit (problema de template/data)
- Si no en té, és comportament esperat

---

## 8. ✅ CONTINGUT: Canvi copiar portada

**Ubicació:** `content/ca/_index.md:3`

**Codi actual:**
```yaml
tagline: "Una eina crítica per llegir Barcelona a través de **la seva arquitectura**, l'art i els espais públics."
```

**Canvi demandada:**
```yaml
tagline: "Una eina crítica per llegir Barcelona a través de **l'arquitectura**, l'art i els espais públics."
```

**Severitat:** Trivial, directe, sense repercussions

---

## 9. 🎨 DISSENY: Franja color + text negre a publicacions

**Ubicació:** 
- Banda: `themes/guiesbcn-elglobusvermell/assets/css/main.css:2392-2396`
- Títol: `themes/guiesbcn-elglobusvermell/assets/css/main.css:2403-2406`

**Codi actual:**
```css
.publicacio-banda {
  height: 30px;
  background: var(--pub-color, var(--color-accent));
  margin: 0 calc(-1 * var(--space-md)) var(--space-lg);
}

.publicacio-cap h1 {
  margin: 0 0 0.25rem;
  color: color-mix(in srgb, var(--pub-color, var(--color-text)), #000 45%);
}
```

**Problema:**
- La banda de color es veu a la capçalera de cada publicació (exemple: Biblioteques = blau)
- El títol h1 usacolor-mix amb el pub-color i negre al 45%, que no pot ser 100% negre pla
- Xavi demanda: "El text també ha de ser negre"

**Solució proposada:**
- **REQUEREIX APROVACIÓ EXPLÍCITA**
- Cambiar: `color: #000;` per força negre pur
- O cambiar `color-mix(in srgb, var(--pub-color, var(--color-text)), #000 45%)` per `#000`

---

## 10. 🎨 DISSENY: Enllaços relacionats — estètica noms llargs

**Ubicació:** 
- Template: `themes/guiesbcn-elglobusvermell/layouts/elements/single.html` (sota plànol, nav relacionats)
- CSS: cercar `.fitxa-nav` o similar en `main.css`

**Problema:**
- Elements amb noms molt llargs (ex: "Biblioteca Pública Arus") trenquen l'estètica de la fila
- Elements amb noms curts (ex: "Biblioteca Prosperitat") van bé

**Audit necessari:**
- Trobar on es renderitzen els enllaços relacionats
- Verificar CSS: té word-wrap, overflow, max-width?
- Veure com es determinen els "relacionats"

**Solució proposada:**
- **POSSIBLEMENT REQUEREIX APROVACIÓ** si és canvi visual
- Opcions: truncar amb ellipsis, permitir wrap en múltiples línies, reduir font

---

## 11. ❓ ARQUITECTURA: Pèrdua de dades — llistat d'arquitectes esborrat

**Context:**
- Xavi estava fent llistat dels 92 arquitectes orfes
- En revisar, tot s'havia esborrat
- Ha hagut de tornar a comenzar

**Ubicació:** Editor Sveltia CMS (backend, no al repo)

**Audit necessari:**
- Verificar: on es desen les dades mentre Xavi edita?
- Hi ha persistència de sessió? Timeout?
- Hi ha historial/versions?
- Git/commits guardan l'estat anterior?

**Solució proposada:**
- Investigar arquitectura de Sveltia (possible buffer de memòria)
- Crear protocol de backup: exportar llistat a Markdown periòdicament
- Considerar si Sveltia té historial de versions que recuperar

---

## 12. ❓ PREGUNTA: Canviar nom d'edifici/element — passa alguna cosa?

**Context:**
- Xavi ha canviat uns quants noms d'elements
- Es pregunta si trencarà algo

**Audit necessari:**
- Verificar: els links usen slug (URL-friendly name) o ID?
- Fer audit de com es generen els links: `{{ .Slug }}` vs `{{ .ID }}`

**Solució proposada:**
- Si usen slug: renombrar trencarà les URLs externals (cal fer redirects 301)
- Si usen ID: renombrar és segur
- Documentar regla: si necessitat renombrar, és segur? NO o SÍ

---

## RESUMEN DE DESCOBERTES

### Bugs que trenquen funcionalitat (críticos)
- **Link arquitecte:** `mapa.js:1084` fallback a general page
- **Disposició sense arquitecte:** CSS issue amb `.fitxa-dada` (necessita verificació)

### Disseny (requereix aprovació client)
- **Línia vertical biografies:** `.arquitecte-bio:601`
- **Línia vertical llistat:** `.llistat-element-arquitectes:1279`
- **Franja color + text negre:** publicacions h1 needs `#000`
- **Noms llargs d'elements:** estètica de línea trencada

### Funcionalitat (necessita decisió client)
- **Intervencions: tipus flexibles** (ús actual, nom actual, etc.)
- **Arquitectes automàtiques vs manuals** (arquitectura principal)

### Contingut (trivial)
- **Copiar portada:** `_index.md:3` — eliminar "seva"

### Unclear/needs investigation
- **Pèrdua de dades:** Sveltia persistència
- **GATCPAC elements:** no surt llistat
- **Format text:** audit de fonts
- **Canvi noms:** slug vs ID determination

---

## ACCIONS PER DILLUNS

1. **Reunió amb Xavi (10:00 Nau Bostic)**
   - Revisar cada punt en pantalla
   - Mostra les línies verticals, fonts de text disparell, etc.
   - Aclarir decisions d'arquitectura (intervencions tipus, arquitectes automàtiques)

2. **Post-reunió: Pla de remediació**
   - Prioritzar: críticos primer, disseny si aprovació, resto si blocants menors
   - Assignar a tasques concretes amb línies de codi

