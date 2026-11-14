# Feedback Xavi — Novembre 2026

Registre estructurat de tots els punts que Xavi ha plantejat en els mails del 12-14 de novembre sobre l'editor de fitxes d'arquitectes i el web.

---

## MAIL 1: Problemes d'arquitectura de l'editor (12 de novembre)

### 1. Llistat d'arquitectes orfes esborrat
**Categoria:** Bug / Pèrdua de dades
**Context:** Xavi havia començat a fer el llistat d'arquitectes sense fitxa. Quan va revisar, va veure que tot s'havia esborrat.
**Causa probable:** No documentada. Verificar si es va sobrescriure manualment o si hi ha un problema de persistència a l'editor.
**Solució:** 
- Investigar si el llistat es desa a alguna capa intermèdia que es pot perdre
- Crear una còpia de seguretat del llistat (markdown o JSON)
- Confirmar amb Xavi si l'editor té backup o historial

### 2. Llistat incomplet d'arquitectes
**Categoria:** Funcionalitat faltant
**Context:** El llistat actual no inclou tots els arquitectes que apareixen a la web.
**Causa probable:** Migració incompleta de WordPress o dades incompletes al dataset inicial.
**Solució:**
- Fer audit complet: arquitectes únics que apareixen en totes les intervencions de tots els elements
- Generar llistat definitiu de tots els noms únics
- Comparar amb dades de WordPress per verificar si falten noms

### 3. Poder eliminar arquitectes d'una fitxa (inclosos orfes)
**Categoria:** Funcionalitat demandada
**Context:** Xavi no pot eliminar arquitectes d'una fitxa si no tenen fitxa pròpia. Els dos únics camins són eliminar la fitxa sencera o crear una fitxa temporal de l'arquitecte.
**Causa probable:** Disseny de l'editor que requereix que tot arquitecte tingui fitxa per poder-se seleccionar/desseleccionar.
**Solució:**
- Modificar el camp "Arquitectes" perquè permeti eliminar items inclús sense fitxa associada
- Mantenir la referència de text però fer-la "deletable"
- Verificar que això no trencarà links existents

### 4. Assegurar que informació d'arquitectes NO surt a la fitxa pública
**Categoria:** Bug de visibilitat
**Context:** Exemple trobat: https://112books.github.io/guiesbarcelona-elglobusvermell/elements/edifici-dhabitatges-casa-dels-braus/ mostra informació d'arquitectes que no hauria de sortir.
**Causa probable:** La plantilla està mostrant el camp "Arquitectes" directament en lloc de només mostrar les "Intervencions".
**Solució:**
- Revisar template: `content/ca/elements/*.md` → la sortida pública NOMÉS ha de venir de "Intervencions", mai del camp "Arquitectes"
- El camp "Arquitectes" és metadata interna per a l'editor, no per a públic
- Audit: verificar totes les fitxes per assegurar que no surt aquesta informació

### 5. Modificar nom d'arquitecte trencarà els links?
**Categoria:** Pregunta d'arquitectura
**Context:** Xavi demana si canviar el nom d'una fitxa d'arquitecte trencarà els links que ja l'apunten.
**Resposta esperada:** Depèn de com es fan els links:
- Si els links són per `slug` (URL amigable), renombrar trencarà els links existents
- Si els links són per `id` (GUID), podrem renombrar sense problemes
**Solució:**
- Definir si els links d'arquitectes usen `slug` o `id`
- Si és `slug`, documentar el procés: never rename existing architects, only create new ones
- Consideracions SEO: redirects 301 si canviem slugs

### 6. No poder eliminar autors d'intervencions sense fitxa
**Categoria:** Funcionalitat faltant
**Context:** Exemple: intervencions amb autors com "Llorenç Garcia-Barbón. 1970 (espai) Blancj & Conca...." que no es poden eliminar perquè no tenen fitxa.
**Causa probable:** El campo d'autors a intervencions requereix una fitxa existent.
**Solució:**
- Permetre afegir / eliminar autors text lliure a intervencions, independentment de si tienen fitxa
- Els autors amb fitxa han de mostrar el link
- Els autors sense fitxa es mostren com a text plain

### 7. Arquitectes a intervencions: filtrar per "Arquitectes" de la fitxa?
**Categoria:** Funcionalitat demandada
**Context:** Xavi demana: "Podem fer que a les intervencions, quan es desplega el llistat, només surtin els arquitectes que anteriorment hem posat a l'apartat arquitectes?"
**Causa probable:** Actualment el dropdown mostra TOTS els arquitectes, causant confusió.
**Solució:**
- Opció A: Filtrar el dropdown de "Intervencions" als arquitectes ja triats a "Arquitectes"
- Opció B: Eliminar el campo "Arquitectes" sencera (veure punt 8)
- Decidir amb client quin és el flux correcte

### 8. Alternativa: "Arquitectes" s'ompli automàticament
**Categoria:** Funcionalitat alternativa
**Context:** Xavi suggereix: "Una altra opció que se m'acut: Que no hàgim d'omplir mai l'apartat Arquitectes, sinó que s'ompli automàticament amb la informació de les intervencions."
**Causa probable:** Duplication de la mateixa informació (Arquitectes manualment + Arquitectes a intervencions).
**Solució:**
- Aquesta és una decisió d'arquitectura major
- Si "Arquitectes" és sempre derivat de "Intervencions", pots eliminar el campo manual
- Si "Arquitectes" és metadata editorial diferent (per exemple, per ordenar o destacar), cal mantenir-lo
- **DECISIÓ PENDENT AMB CLIENT**

### 9. Eliminar apartat "Nomenclàtor"
**Categoria:** Demanda de UI
**Context:** Xavi en demanava anteriorment eliminar aquest camp.
**Causa probable:** Sembla que no s'utilitza o causa confusió.
**Solució:**
- Verificar si hi ha dades guardades al campo "Nomenclàtor"
- Si està buit a totes les fitxes, pot eliminar-se directament
- Si té dades, decidir on moure-les (potser a contingut?)

### 10. Finalitat de "Contingut Addicional"
**Categoria:** Clarificació
**Context:** Xavi pregunta per quin serveix aquest campo, especialment en relació a "Descripció".
**Context actual:** "Descripció" no té editor de text, mentre que "Contingut Addicional" sí.
**Solució:**
- Documentar la finalitat de cada campo
- Si "Descripció" necessita editor de text (que sembla que sí), afegir-lo
- Potser "Contingut Addicional" hauria de renombrar-se a "Informació Extra" o similar
- **DECISIÓ: Revisar amb client per clarificar l'estructura final**

---

## MAIL 2: Observacions pràctiques (14 de novembre)

### 11. Canviar nom d'edifici/element — passa alguna cosa?
**Categoria:** Pregunta
**Context:** Xavi n'ha canviat "uns quants" i es pregunta si trencarà algo.
**Causa probable:** Mateixa situació que els arquitectes (slug vs id).
**Solució:**
- Confirmar com funcionen els slugs d'elements
- Si s'han renombrat ja, verificar que els links existents segueixen funcionant
- Audit de links interns que apuntin a elements per slug

### 12. Intervencions: afegir tipus "ús actual" i "nom actual"
**Categoria:** Funcionalitat demandada
**Context:** Xavi veurà útil poder especificar no només la intervenció, sinó també l'ús actual o nom actual de l'edifici.
**Solució:**
- Expandir el schema de "Intervencions" per permetre més tipos
- Exempls: construcció, reforma, ús actual, nom actual, etc.
- **DECISIÓ: Verificar quins tipos són necessaris amb client**

### 13. Dubte: poder triar paraules flexibles a intervencions
**Categoria:** Funcionalitat demandada
**Context:** "Seria útil poder posar una que fos "ús actual". Dubtes sobre si, a intervencions, hauríem de poder triar cada vegada la paraula que necessitem."
**Solució:**
- Definir si "tipus d'intervenció" és un dropdown predefinit o text lliure
- Si és dropdown: llistar tots els tipos necessaris
- Si és text lliure: permetre entrada flexible

### 14. Disposició visual quando falta arquitecte
**Categoria:** Bug de disseny / UI
**Context:** Exemple captura: quan una intervenció no té arquitecte, tot es desplaça visualment (layout broken).
**Causa probable:** El template assumeix que sempre hi ha arquitecte, i la seva absència causa flexbox/grid issues.
**Solució:**
- Revisar el template de "Intervencions" a les fitxes
- Assegurar que funciona correctament amb:
  - Arquitecte present
  - Arquitecte absent
  - Arquitecte parcial (només cognoms, data sense nom, etc.)

### 15. Format de text disparell en alguns elements
**Categoria:** Bug / Inconsistència
**Context:** Xavi dona exemples:
- https://112books.github.io/guiesbarcelona-elglobusvermell/elements/casa-bloc/?color=eca647
- Sembla que alguns textos tienen format inconsistent.
**Causa probable:** Migració de WordPress amb formats HTML / Markdown mixtes.
**Solució:**
- Audit: verificar tots els camps de text (descripció, contingut addicional)
- Estandaritzar format (Markdown o HTML)
- Verificar que l'editor genera output consistent

### 16. Llistat d'edificis a publicacions no apareix
**Categoria:** Bug / Funcionalitat faltant
**Context:** Exemple: https://112books.github.io/guiesbarcelona-elglobusvermell/publicacions/gatcpac/
**Causa probable:** Possiblement la publicació no té elements associats, o el template no està mostrant-los.
**Solució:**
- Verificar: té la publicació elements associats?
- Si sí: revisar template perquè els mostri
- Si no: és esperat? Verificar amb client

### 17. Línia vertical a esquerra de biografies d'arquitectes (disseny)
**Categoria:** Disseny / UI
**Context:** Captura de la fitxa de Josep Lluís Sert i López: apareix una línia vertical a l'esquerra de la biografia.
**Causa probable:** Estil CSS de decoració / accent visual que ara no agrada.
**Solució:**
- ⚠️ **REQUEREIX APROVACIÓ EXPLÍCITA** per CLAUDE.md
- Preguntar a client si vol eliminar-la completament o modificar-la
- Decisions: color, gruix, o eliminar del tot

### 18. Línia vertical a llistat d'arquitectes + compacitat
**Categoria:** Disseny / UI + Funcionalitat
**Context:** Quan es llisten elements amb els seus arquitectes, apareix una línia vertical. Xavi diu que les "tres informacions" (nom element, adreça, arquitectes) podrien estar més juntes i equidistants.
**Causa probable:** Layout amb demasiada separació visual, línies decoratives que causen dispersió.
**Solució:**
- ⚠️ **REQUEREIX APROVACIÓ EXPLÍCITA** per CLAUDE.md
- Revisar layout del llistat
- Opcions: eliminar línies, ajustar spacing, fer design més compacte
- Preguntar a client sobre les preferències de compacitat

### 19. Arquitecte a llistat no porta a fitxa individual (bug)
**Categoria:** Bug de navegació
**Context:** "Quan es llisten elements, quan cliques un arquitecte no porta a la pàgina de l'arquitecte, sinó a la pàgina general d'arquitectes."
**Causa probable:** El link está configurat malament (apunta a /arquitectes/ en lloc de /arquitectes/nom-arquitecre/).
**Solució:**
- Revisar template: on es genera el link?
- Canviar `href="/arquitectes/"` per `href="/arquitectes/{{ .Slug }}/"` (o similar)
- Audit: verificar que TOTS els links d'arquitectes en llistats apunten a fitxa individual

### 20. Canvi copiar portada
**Categoria:** Contingut / Redacció
**Context:** Frasse actual: "Una eina crítica per llegir Barcelona a través de la seva arquitectura, l'art i els espais públics."
**Demanada:** Canviar a: "Una eina crítica per llegir Barcelona a través de l'arquitectura, l'art i els espais públics." (eliminar "seva")
**Solució:**
- Buscar on es defineix aquest text (probable: `config/*/params.toml` o `content/_index.md`)
- Fer el canvi
- Verificar que es mostra correctament a portada

### 21. Franja color + text negre a temes
**Categoria:** Disseny / UI
**Context:** Exemple: https://112books.github.io/guiesbarcelona-elglobusvermell/publicacions/biblioteques/
Apareix franja blava dalt. "El text també ha de ser negre."
**Causa probable:** Template de publicacions/temes té una franja de color de fons amb text en color que no és legible.
**Solució:**
- ⚠️ **REQUEREIX APROVACIÓ EXPLÍCITA** per CLAUDE.md (és canvi de disseny visual)
- Revisar quin és l'estatus actual: franja visible? Text color?
- Preguntar: vol eliminar franja completament, o mantenir-la amb text negre?
- Verificar contrast WCAG si es canvia

### 22. Enllaços sota plànol es trenquen estètica
**Categoria:** Disseny / UI
**Context:** Exemples:
- https://112books.github.io/guiesbarcelona-elglobusvermell/elements/biblioteca-publica-arus/ (es trenca estètica)
- https://112books.github.io/guiesbarcelona-elglobusvermell/elements/biblioteca-prosperitat-ideal-plastica-flor/ (OK)
**Problema:** Noms molt llargs causen que la fila "es trenci".
**Causa probable:** Falta word-wrap o text overflow handling al CSS.
**Solució:**
- Revisar template i CSS dels enllaços relacionats
- Preguntar: com vol Xavi que es comporti el text long?
  - Truncar amb ellipsis (...)?
  - Wrapping en múltiples línies?
  - Reduir mida de font?
- ⚠️ **POSSIBLEMENT REQUEREIX APROVACIÓ** si és canvi visual

### 23. Problema: com estan triats els enllaços relacionats?
**Categoria:** Pregunta / Funcionalitat
**Context:** "Primer, no sé com estan triats."
**Causa probable:** Xavi no entén la lògica de selecció d'elements relacionats.
**Solució:**
- Documentar la lògica: és automàtica (per tags, mateixa guia)? Manual?
- Si manual: qui els pot editar?
- Si automàtica: verificar que funciona correctament

---

## RESUMEN PER PRIORITAT

### 🔴 CRÍTICO (bugs que afecten funcionalitat)
1. **Llistat d'arquitectes esborrat** — Pèrdua de dades
2. **Disposició visual quan no hi ha arquitecte** — Layout broken
3. **Arquitecte a llistat no porta a fitxa individual** — Bug de navegació
4. **Format de text disparell** — Inconsistència de dades
5. **Llistat d'edificis a publicacions no apareix** — Funcionalitat mancant

### 🟡 IMPORTANT (funcionalitat demandada, decisions necessàries)
1. **Poder eliminar arquitectes** — Per limpieza de dades
2. **Poder eliminar autors d'intervencions** — Per limpieza de dades
3. **Intervencions: tipus flexibles** — Necessita decisió de client
4. **Arquitectes: automàtiques vs manuals** — Decisió d'arquitectura
5. **Clarificar "Arquitectes" vs "Intervencions"** — Decisió d'arquitectura

### 🟢 DISSENY (requereix aprovació explícita per CLAUDE.md)
1. **Eliminar línia vertical a biografies** — Aproval client
2. **Eliminar línia vertical a llistat + compacitat** — Aprovació client
3. **Franja color + text negre a temes** — Aprovació client
4. **Stètica dels enllaços relacionats** — Possiblement aprovació

### 📋 CONTINGUT / CLARIFICACIÓ
1. **Canvi copiar portada** — Directe, sense problemes
2. **Nomenclàtor: eliminar?** — Verificar si té dades
3. **Finalitat "Contingut Addicional"** — Clarificació de estructura
4. **Com estan triats els relacionats?** — Documentació

---

## ACCIONS IMMEDIATES (sense codi)

1. **Reunió dilluns (10:00 Nau Bostic) amb Xavi**
   - Revisar els punts críticos en pantalla
   - Decidir prioritat
   - Clarificar decisions d'arquitectura (Arquitectes vs Intervencions)
   - Obtenir aprovacions de disseny

2. **Post-reunió: crear "Pla de remediació"**
   - Priorització final
   - Assignació a sprints
   - Decisions de client documentades

