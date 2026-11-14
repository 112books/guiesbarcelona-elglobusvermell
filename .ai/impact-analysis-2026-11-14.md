# Impact Analysis — Novembre 2026

Análisis d'impacte complet per a cada fix proposat. Per cada punt:
- **Causa** del problema
- **Solució proposada**
- **Impacte estimat** (quines parts es veuran afectades)
- **Riscos de regressió** (potencials efectes secundaris)
- **Verificacions necessàries** (testing requerit)

**Objectiu:** Garantir que cada fix no trenca altre cosa.

---

## 1. 🔴 BUG CRÍTICO: Link arquitecte a llistat va a `/arquitectes/` general

### Causa
**Ubicació:** `mapa.js:1084`
```javascript
arqLink.href = arqUrls[idx] || ((window.SITE_BASE || '/') + 'arquitectes/');
```

Quan `arqUrls[idx]` és undefined (no existeix URL per a aquell arquitecte), fa fallback a `/arquitectes/`.

**Per què passa:**
- `arqUrls` es passa correctament desde template (4 fitxers: `elements/list.html`, `publicacions/term.html`, `mapa/list.html`, `temes/single.html`)
- Però quan es renderitza, possiblement hi ha mismatch entre índex i nombre d'URLs

### Solució proposada
**Opció A (recomanada):** Generar URL en JavaScript si `arqUrls[idx]` és undefined
```javascript
arqLink.href = arqUrls[idx] || (() => {
  // Usar same urlize que Hugo
  var slug = aName.toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
  return (window.SITE_BASE || '/') + 'arquitectes/' + slug + '/';
})();
```

**Opció B:** Assegurar que `arqUrls` sempre té exactament `arquitectes.length` elements (potser afegint fallbacks a template)

### Impacte estimat
**Components afectats:**
- `mapa.js`: línia 1079-1087 (loop que genera links)
- 4 fitxers template: `elements/list.html`, `publicacions/term.html`, `mapa/list.html`, `temes/single.html`
- Totes les pàgines que llisten arquitectes (mapa, publicacions, temes)

**Amplitud:** ALTA — els clicks d'arquitecte afecten tota la navegació

### Riscos de regressió
- **BAIX:** Si implementem Opció A (generar URL en JS)
  - El `urlize` ja es fa a Hugo (`arquitectes-urls.html`), però podem replicar-lo en JS
  - Risc: noms amb accents o puntuació podrien generar slugs diferents entre Hugo i JS
  - **Mitigació:** Usar la mateixa lògica de `urlize` de Hugo

- **BAIX-MEDI:** Si implementem Opció B (verificar template)
  - Risc: si modifiquem template, podria afectar altres usos de `arquitectes_urls`
  - **Mitigació:** Verificar que les 4 ubicacions function correctament

### Verificacions necessàries
1. **Audit:** Verificar que tots els arquitectes amb fitxa estan en `arquitectes_urls`
2. **Test:** Clicar 20-30 arquitectes de llistat i verificar que van a fitxa individual, NO a `/arquitectes/`
3. **Regressió:** Verificar que el mapa de fitxes d'elements segueix funcionant
4. **Regressió:** Verificar que el llistat de publicacions segueix funcionant
5. **Regressió:** Verificar que el llistat de temes segueix funcionant

---

## 2. 🔴 BUG CRÍTICO: Pèrdua de dades — llistat d'arquitectes a Sveltia

### Causa
**Ubicació:** Editor Sveltia CMS (backend)

**Per què passa:** Desconegut fins a investigar:
- Timeout de sessió sense guardar?
- Buffer en memòria que no es persista?
- Actualització de servidor que perd dades?
- Problema de Git/commits no guardats?

### Solució proposada
1. **Investigació dilluns:** Verificar com es guarden dades a Sveltia mentre s'edita
2. **Crear protocol:** Backup manual periòdic (exportar llistat a Markdown)
3. **Considerar:** Si Sveltia té historial de versions o git history per recuperar
4. **Potencial solució:** Implementar auto-save o guardar cada X minuts

### Impacte estimat
**Components afectats:**
- Sveltia CMS (backend)
- Git repository (potser)
- Workflow editorial (com Xavi edita)

**Amplitud:** CRÍTICA — afecta productivitat editorial

### Riscos de regressió
- **BAIX:** La solució és procedimental (protocol de backup), no canvis de codi
- Risc: Si canviem Sveltia config, podria afectar altres editors
- **Mitigació:** Documentar tots els canvis de config

### Verificacions necessàries
1. **Investigació:** On es desen les dades mentre Xavi edita?
2. **Verificació:** Hi ha git commits que guardaven l'estat anterior?
3. **Test:** Recrear scenario: fer edicions, tancar sessió, verificar si es desen
4. **Validació:** Xavi confirma que nova solució funciona sense perdre dades

---

## 3. 🎨 DISSENY: Eliminar línia vertical biografia arquitecte

### Causa
**Ubicació:** `main.css:601`
```css
.arquitecte-bio {
  border-left: 3px solid var(--color-accent);
}
```

Xavi diu que no agrada aquesta decoració.

### Solució proposada
Eliminar una línia CSS:
```diff
.arquitecte-bio {
  margin: var(--space-md) 0;
  padding: var(--space-sm) var(--space-md);
- border-left: 3px solid var(--color-accent);
  color: var(--color-text);
}
```

### Impacte estimat
**Components afectats:**
- Estil visual de biographies d'arquitectes únicament
- Ubicacions: fitxa d'arquitecte individual (`arquitectes/term.html`)

**Amplitud:** MUY BAJA — canvi purament estètic, aïllat

### Riscos de regressió
- **MOLT BAIX:** Eliminar `border-left` no afecta layout ni spacing
- Risc: Ningú — és CSS pur que ja no es veurà
- **Mitigació:** Screenshot before/after per confirmar

### Verificacions necessàries
1. **Visual:** Veure biografia d'arquitecte sense línia
2. **Responsive:** Verificar que es veu bé a mòbil/tablet
3. **Accessibility:** No hi ha contrast issues (la línia es va)
4. **WCAG:** Sense canvis, continua AA

---

## 4. 🎨 DISSENY: Eliminar línia vertical llistat arquitectes + compactat

### Causa
**Ubicació:** `main.css:1273-1289`
```css
.llistat-element-arquitectes {
  padding-left: 1.5rem;
  border-left: 2px solid var(--color-border, #e0e0e0);
}
```

Xavi diu que:
1. La línia no agrada
2. La separació excessive (padding-left) causa espai excessiu

### Solució proposada
```diff
.llistat-element-arquitectes {
  width: 100%;
- padding-left: 1.5rem;
+ padding-left: 0.5rem;  // ← més compacte
  font-size: 0.8125rem;
  color: #767676;
  margin-top: 0.25rem;
- border-left: 2px solid var(--color-border, #e0e0e0);
}
```

### Impacte estimat
**Components afectats:**
- Llistat d'elements (mapa + llistat): `mapa.js` renderitza aquestes clases
- Ubicacions on apareix: elements/list.html, publicacions/term.html, mapa/list.html, temes/single.html
- CSS del carrusel, grid del llistat

**Amplitud:** MEDI — afecta layout de llistats, visible a múltiples pàgines

### Riscos de regressió
- **BAIX:** Els canvis CSS són simples (eliminar propietats, reduir padding)
- Risc: El spacing podria ser tant compacte que perjudiqui legibilitat
- **Mitigació:** A/B testing visual amb Xavi dilluns

### Verificacions necessàries
1. **Visual:** Veure llistat d'elements a mapa, publicacions, temes
2. **Legibilitat:** Verificar que les 3 informacions (nom, adreça, arquitectes) es llegeixen bé
3. **Responsive:** Verificar que no es trenca a mòbil
4. **Touch targets:** Els links d'arquitectes segueixen sent clickables
5. **WCAG:** Contrast continua correcte

---

## 5. 🎨 DISSENY: Text h1 publicacions negre pur

### Causa
**Ubicació:** `main.css:2403-2406`
```css
.publicacio-cap h1 {
  color: color-mix(in srgb, var(--pub-color, var(--color-text)), #000 45%);
}
```

El `color-mix` barreja el pub-color (blau, verd, etc.) amb negre al 45%, resultant en un color que no és completament negre.

### Solució proposada
```diff
.publicacio-cap h1 {
  margin: 0 0 0.25rem;
- color: color-mix(in srgb, var(--pub-color, var(--color-text)), #000 45%);
+ color: #000;
}
```

### Impacte estimat
**Components afectats:**
- Títol h1 de cada publicació (GATCPAC, Biblioteques, etc.)
- Ubicacions: `publicacions/term.html:13`

**Amplitud:** BAJA — canvi estètic del títol

### Riscos de regressió
- **MOLT BAIX:** Canvi CSS simple, sense dependències de layout
- Risc: El negre pur podria "trencar" la identitat visual (pub-color era un intent de mantenir coherència)
- **Mitigació:** Confirmar amb Xavi/client que vol negre pur

### Verificacions necessàries
1. **Visual:** Veure títols de publicacions (GATCPAC, Biblioteques, etc.)
2. **Contrast:** Verificar contrast WCAG A (4.5:1) entre negre i fons blanc
3. **Identitat:** Confirmar que negre pur no trenca l'estil visual
4. **Responsive:** Verificar a mòbil

---

## 6. ✅ CONTINGUT: Eliminar "seva" portada

### Causa
**Ubicació:** `content/ca/_index.md:3`
```yaml
tagline: "Una eina crítica per llegir Barcelona a través de la seva arquitectura..."
```

Canvi demanat: eliminar "seva"

### Solució proposada
```diff
tagline: "Una eina crítica per llegir Barcelona a través de
- la seva arquitectura, l'art i els espais públics."
+ l'arquitectura, l'art i els espais públics."
```

### Impacte estimat
**Components afectats:**
- Tagline a portada principal (index)
- Ubicacions: `index.html` template

**Amplitud:** MOLT BAJA — canvi de text únicament

### Riscos de regressió
- **NUL:** És un canvi purament de contingut
- Risc: Ningú
- **Mitigació:** Res

### Verificacions necessàries
1. **Visual:** Veure portada i confirmar text correcte
2. **Typos:** Rellegir frase per verificar coherència
3. **SEO:** Si cal, actualitzar metes (no calen canvis)

---

## 7. 🟡 LAYOUT: Disposició visual sense arquitecte (fitxa-dada)

### Causa
**Ubicació:** `elements/single.html:240-243` template + `main.css` CSS `.fitxa-dada`

Quan no hi ha arquitecte, el `<dd>` pot quedar buit causant misalignment.

### Solució proposada
1. **Audit:** Trobar CSS de `.fitxa-dada` en `main.css`
2. **Verificar:** Si té `display: flex` o similar que causa col·lapse
3. **Corregir:** Possiblement afegir `min-height` o `display: contents`

### Impacte estimat
**Components afectats:**
- Layout de fitxa d'elements (banda de dades)
- Múltiples fitxes: elements arquitectònics, obres d'art, etc.

**Amplitud:** MEDIA — afecta moltes fitxes

### Riscos de regressió
- **BAIX-MEDI:** Canvi CSS que podria afectar totes les files de dades
- Risc: Si canviem `.fitxa-dada` malament, pot trencar layout de TOTES les fitxes
- **Mitigació:** Verificar totes les combinacions (arquitectes sí/no, any sí/no, etc.)

### Verificacions necessàries
1. **Visual:** Fitxes amb arquitecte (verificar que no canvia)
2. **Visual:** Fitxes sense arquitecte (verificar que està alineada)
3. **Visual:** Fitxes amb intervencions sense arquitecte
4. **Responsive:** A mòbil/tablet
5. **Regressió:** 10+ fitxes variades

---

## 8. ❓ FUNCIONALITAT: Intervencions — afegir tipus "ús actual"

### Causa
**Ubicació:** Frontmatter schema d'elements (`content/ca/elements/*.md`)

Actualment els `intervencions.tipus` són limitats (Projecte, Reforma, etc.).

### Solució proposada
1. **Audit:** Llistar tots els `tipus` únics que existeixen actualment
2. **Decidir:** Quins tipus nous necessitem (ús actual, nom actual, etc.)
3. **Actualitzar schema:** Si és dropdown predefinit o text lliure
4. **Migrar:** Actualitzar Sveltia CMS schema si necessari

### Impacte estimat
**Components afectats:**
- Schema de dades (editor + frontmatter)
- Múltiples fitxes (310+)
- Template de rendering (`elements/single.html` renderitza intervencions)

**Amplitud:** ALTA — afecta estructura de dades

### Riscos de regressió
- **MEDI:** Si canviem schema, els editors hauran de readaptar
- Risc: Intervencions existents podrien no renderitzar si el schema es trenca
- **Mitigació:** Fer canvi retrocompatible (tipos nous + vells segueixen funcionant)

### Verificacions necessàries
1. **Data integrity:** Verificar que intervencions existents segueixen vàlides
2. **Editor:** Verificar que Sveltia CMS schema s'actualitza correctament
3. **Rendering:** 20+ fitxes amb intervencions noves
4. **Template:** Verificar que `elements/single.html` renderitza nous tipus correctament

---

## 9. 📋 FORMAT TEXT: Inconsistència — audit + estandaritzar

### Causa
**Ubicació:** Múltiples camps en `content/ca/elements/*.md` (descripcio, intervencions.descripcio, etc.)

Alguns camps son HTML, d'altres Markdown, d'altres text pla.

### Solució proposada
1. **Audit:** Verificar format de tots els camps (grep per tags HTML)
2. **Decidir:** Markdown o HTML (recomanació: Markdown)
3. **Migrar:** Convertir tots els camps al format escollit
4. **Verificar:** Template renderitza correctament

### Impacte estimat
**Components afectats:**
- 310+ fitxes d'elements
- Template rendering (`elements/single.html`)
- Possiblement editor Sveltia CMS

**Amplitud:** MOLT ALTA — afecta tota la base de dades

### Riscos de regressió
- **ALT:** Si migrem format incorrectament, els continguts podrien no renderitzar
- Risc: HTML tags podrien renderitzar-se com a text pla, o vice-versa
- **Mitigació:** Test complet de 50+ fitxes post-migració

### Verificacions necessàries
1. **Audit:** Llistar tots els formats actuals (quants HTML, quants Markdown, quants plain)
2. **Migració:** Convertir conservativament (probablement script automàtic)
3. **Visual:** 50+ fitxes verificar rendering correcte
4. **Buscar:** Verificar que la busca segueix funcionant (possibles issues si text canvia format)

---

## 10. ❓ TEMPLATE: Llistat GATCPAC — no apareix

### Causa
**Ubicació:** `publicacions/term.html:18-27`

Template verifica `{{ if .Pages }}` — si buit, mostra "Encara no hi ha fitxes."

**Per què passa:**
- Possiblement GATCPAC no té elements associats
- O `.Pages` no està correctament poblat

### Solució proposada
1. **Audit:** Quants elements tienen `publicacions: ["gatcpac"]`?
2. **Verificar:** Si `.Pages` funciona correctament en template
3. **Debug:** Si no funciona, revisar com es carreguen les pàgines a template

### Impacte estimat
**Components afectats:**
- Template `publicacions/term.html`
- Possiblement la manera que s'associen elements a publicacions

**Amplitud:** BAJA — probablement issue de dades, no de codi

### Riscos de regressió
- **MOLT BAIX:** Si és issue de dades, cap canvi de codi
- Risc: Si necessita canvi template, podria afectar altres publicacions
- **Mitigació:** Verificar que totes les publicacions segueixen funcionant

### Verificacions necessàries
1. **Data:** Quants elements tiene GATCPAC assignats?
2. **Template:** Verificar que `.Pages` es carrega correctament
3. **Visual:** Veure GATCPAC amb elements (si en té)
4. **Regressió:** Verificar que altres publicacions segueixen mostrant elements

---

## MATRIU DE RISC

| Fix | Criticitat | Amplitud | Risc Regressió | Prioritat | Data Target |
|-----|-----------|----------|----------------|-----------|------------|
| Link arquitecte | 🔴 CRÍTICO | ALTA | BAIX | P1 | Post reunió |
| Pèrdua dades | 🔴 CRÍTICO | MEDIA | BAIX | P1 | Post reunió |
| Línia biografia | 🎨 Disseny | BAJA | MOLT BAIX | P3 | Setmana 1 |
| Línia llistat | 🎨 Disseny | MEDIA | BAIX | P3 | Setmana 1 |
| Text h1 negre | 🎨 Disseny | BAJA | MOLT BAIX | P3 | Setmana 1 |
| Tagline portada | ✅ Contingut | BAJA | NUL | P4 | Immediat |
| Disposició s/arq | 🟡 Layout | MEDIA | BAIX-MEDI | P2 | Setmana 1 |
| Intervencions tipus | 🟡 Funcionalitat | ALTA | MEDI | P2 | Setmana 2 |
| Format text | 📋 Audit | MOLT ALTA | ALT | P2 | Setmana 2-3 |
| GATCPAC | ❓ Pregunta | BAJA | MOLT BAIX | P3 | Setmana 1 |

---

## RECOMANACIONS

### Per a dilluns (reunió Xavi)
1. **Validar causes:** Xavi confirma que els findings són correctes
2. **Prioritzar:** Decidir amb client quin és el ordre: P1 → P2 → P3 → P4
3. **Aprovar disseny:** Les 3 changes de disseny (línies, text negre)

### Per a setmana 1
1. **Fix P1:** Link arquitecte (`mapa.js:1084`)
2. **Fix P1:** Investigar pèrdua de dades Sveltia
3. **Fix P3:** Eliminar línies CSS (biografia + llistat)
4. **Fix P3:** Text h1 negre
5. **Fix P4:** Tagline portada

### Per a setmana 2+
1. **Audit P2:** Format text (potencialmet script automàtic)
2. **Audit P2:** Intervencions — afegir tipus
3. **Audit P3:** GATCPAC — verificar data

### Testing post-fix
**Per cada fix:**
1. Build Hugo en staging
2. Verificar visually que funciona
3. Verificar regressió (10+ fitxes vàries)
4. Verificar WCAG a pa11y-ci
5. Xavi valida visualmente a staging

