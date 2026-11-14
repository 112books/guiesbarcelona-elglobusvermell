# Prep Dilluns 15 de novembre — Reunió amb Xavi a Nau Bòstik (10:00)

Preparació completa per a la reunió.

---

## OBJECTIUS DILLUNS

1. **Validar causes:** Xavi confirma que els findings son correctes
2. **Prioritzar:** Decidir l'ordre de fixatge (P1/P2/P3/P4)
3. **Aprovar disseny:** Les 3 changes CSS (línies + text negre)
4. **Planificar:** Com continuarem setmana que ve

---

## MATERIAL A PORTAR (en pantalla)

### 1. URLs de les issues reportades (verificar en pantalla)

**Línies verticals:**
- Biografia arquitecte: https://112books.github.io/guiesbarcelona-elglobusvermell/arquitectes/josep-lluis-sert-i-lopez/
- Llistat arquitectes: https://112books.github.io/guiesbarcelona-elglobusvermell/elements/ (veure coluna arquitectes)

**Text portada:**
- Portada: https://112books.github.io/guiesbarcelona-elglobusvermell/

**Franja color + text:**
- Publicació: https://112books.github.io/guiesbarcelona-elglobusvermell/publicacions/biblioteques/

**GATCPAC elements:**
- GATCPAC: https://112books.github.io/guiesbarcelona-elglobusvermell/publicacions/gatcpac/

**Link arquitecte (bug):**
- Elements: https://112books.github.io/guiesbarcelona-elglobusvermell/elements/ (clicar architect name)

---

## CHECKLIST REUNIÓ

### Validacions amb Xavi

- [ ] **Pèrdua de dades:** Confirma que és issue crítico
- [ ] **Link arquitecte:** Confirma que va a `/arquitectes/` en lloc de fitxa individual
- [ ] **Línies CSS:** Confirma que no agrada la decoració vertical
- [ ] **Text negre:** Confirma que vol títols completament negres
- [ ] **Compacitat llistat:** Confirma que vols spacing més compacte

### Preguntes per al client (El Globus Vermell)

- [ ] **Intervencions tipus:** Quins tipus nous necessiteu exactament?
- [ ] **Franja publicacions:** Mantenir franja de color o eliminar-la completament?
- [ ] **Arquitectes automàtiques:** Vol que "Arquitectes" s'ompli automàticament desde intervencions?

### Priorització

Acordar amb Xavi quin ordre:

**Críticos (setmana 1):**
- [ ] P1: Fix link arquitecte
- [ ] P1: Investigar pèrdua de dades

**Disseny (necessita OK):**
- [ ] P3: Eliminar línies CSS (si aprova)
- [ ] P3: Text h1 negre (si aprova)
- [ ] P3: Tagline portada (trivial, es pot fer immediatament)

**Audits/verificacions:**
- [ ] P2: Format text (audit complet)
- [ ] P2: Intervencions schema (ampliar tipos)
- [ ] P3: GATCPAC (verificar dades)

---

## TESTING TEMPLATE — Per a cada fix post-implementació

### Fix: Link arquitecte (P1)

**Pre-fix:**
- [ ] Snapshot: llistat elements, click arquitecte va a `/arquitectes/`

**Post-fix (verificacions):**
- [ ] [ ] 5 clicks aleatori: van a fitxa individual de l'arquitecte
- [ ] [ ] 5 clicks aleatori: URL correcta (exemple: `/arquitectes/josep-lluis-sert-i-lopez/`)
- [ ] [ ] Mapa elements: segueix funcionant
- [ ] [ ] Mapa publicacions: segueix funcionant
- [ ] [ ] Mapa temes: segueix funcionant
- [ ] [ ] Firefox/Chrome/Safari: funcionan tots

**Regressió (verificar que no canvia):**
- [ ] [ ] Link d'element des de fitxa — segueix funcionant
- [ ] [ ] Link de publicació — segueix funcionant
- [ ] [ ] Llistat alfabètic arquitectes — segueix funcionant

**WCAG:**
- [ ] [ ] pa11y-ci passa

---

### Fix: Eliminar línia vertical biografia (P3)

**Pre-fix:**
- [ ] Screenshot: biografia amb línia blava

**Post-fix:**
- [ ] Screenshot: biografia sense línia
- [ ] A/B: Xavi confirma que millor sense línia

**Responsive:**
- [ ] [ ] Desktop: biografia es veu bé
- [ ] [ ] Tablet (iPad): biografia es veu bé
- [ ] [ ] Mobile (iPhone): biografia es veu bé

**Regressió:**
- [ ] [ ] Altres elements de `.arquitecte-bio` segueixen estilats correctament
- [ ] [ ] Layout padding/margin no ha canviat

**WCAG:**
- [ ] [ ] pa11y-ci passa

---

### Fix: Eliminar línia + compactat llistat arquitectes (P3)

**Pre-fix:**
- [ ] Screenshot: llistat amb línia i padding excessiu

**Post-fix:**
- [ ] Screenshot: llistat sense línia i més compacte
- [ ] A/B: Xavi confirma que és millor

**Legibilitat:**
- [ ] [ ] Les 3 informacions (nom, adreça, arquitectes) segueixen llegibles
- [ ] [ ] Els links dels arquitectes són clickables
- [ ] [ ] No és massa apretada

**Responsive:**
- [ ] [ ] Desktop: es veu bé
- [ ] [ ] Tablet: es veu bé
- [ ] [ ] Mobile: es veu bé

**Regressió:**
- [ ] [ ] Mapa elements: segueix funcionant
- [ ] [ ] Mapa publicacions: segueix funcionant
- [ ] [ ] Mapa temes: segueix funcionant

**WCAG:**
- [ ] [ ] pa11y-ci passa

---

### Fix: Text h1 negre (P3)

**Pre-fix:**
- [ ] Screenshot: publicacions amb títol grisàs

**Post-fix:**
- [ ] Screenshot: publicacions amb títol negre pur
- [ ] A/B: Xavi confirma que és millor

**Contrast WCAG:**
- [ ] [ ] pa11y-ci: contrast 4.5:1 (AA) entre negre i fons blanc
- [ ] [ ] pa11y-ci: contrast 7:1 (AAA) si possible

**Responsive:**
- [ ] [ ] Desktop: text negre és visible
- [ ] [ ] Mobile: text negre és visible

**Regressió:**
- [ ] [ ] Altres elements de `.publicacio-cap` no han canviat
- [ ] [ ] Layout de publicacions segueix igual

**WCAG:**
- [ ] [ ] pa11y-ci passa

---

### Fix: Tagline portada (P4)

**Pre-fix:**
- [ ] Screenshot: portada amb "seva"

**Post-fix:**
- [ ] Screenshot: portada sense "seva"
- [ ] Verificar: "Una eina crítica per llegir Barcelona a través de l'arquitectura..."

**SEO:**
- [ ] [ ] Title/meta no afectats (és tagline, no title)

**Responsive:**
- [ ] [ ] Desktop: es veu correcte
- [ ] [ ] Mobile: es veu correcte

**Regressió:**
- [ ] [ ] Layout portada no ha canviat

**WCAG:**
- [ ] [ ] pa11y-ci passa

---

## COMANDES QUE USAREM DILLUNS

### Build local
```bash
hugo server -D
```
Veure en `http://localhost:1313/`

### Build staging (post-fix)
```bash
hugo --minify --environment staging
```

### Verificar pa11y-ci
```bash
pa11y-ci --config .pa11yci.json
```

### Git workflow (post-fix)
```bash
git status
git diff themes/guiesbcn-elglobusvermell/assets/css/main.css
git add [fitxers]
git commit -m "fix: <descripció>"
```

### Check GitHub Actions
```bash
gh run list
```

---

## ORDRE PROPOSAT DE FIXES

### Immediat (setmana 1)
1. **Fix link arquitecte** — `mapa.js:1084`
2. **Tagline portada** — `_index.md:3` (trivial, es pot fer junt amb 1)
3. **Investigar pèrdua de dades** — Sveltia backend

### Setmana 1 (si OK client)
4. **Eliminar línia biografia** — `main.css:601`
5. **Eliminar línia llistat + compactat** — `main.css:1273-1289`
6. **Text h1 negre** — `main.css:2405`

### Setmana 2+ (audits)
7. **Format text** — Audit + migració
8. **Intervencions schema** — Ampliar tipos
9. **GATCPAC** — Verificar dades

---

## MATERIAL DE SUPORT EN PANTALLA

### 1. Documents disponibles (mostrar a Xavi)
- `.ai/feedback-xavi-2026-11-14.md` — 23 punts estructurats
- `.ai/audit-findings-2026-11-14.md` — Audit detallat
- `.ai/impact-analysis-2026-11-14.md` — Risc i impacte per fix

### 2. Terminals preparades
- Terminal 1: `hugo server -D` (veure localhost:1313)
- Terminal 2: `git` (fer commits)
- Terminal 3: `gh run list` (verificar actions)

### 3. URLs a mostrar
- Staging: https://112books.github.io/guiesbarcelona-elglobusvermell/
- Todas les issues que Xavi reportà

---

## TIMING REUNIÓ

- **10:00:** Obre
- **10:05:** Validar causes (15 min)
- **10:20:** Revisar pantalla (issues actuals) (20 min)
- **10:40:** Prioritzar (10 min)
- **10:50:** Decidir disseny (10 min)
- **11:00:** Planificar setmana que ve (10 min)
- **11:10:** Tancament

Joan: "Sortirà a les 13 dentista, tornarà sobre les 5"

---

## SEGUIMENT POST-REUNIÓ

**Immediat (dilluns post-reunió):**
- Crear branches/commits per a cada fix acordat
- Build + test en staging
- Passar pa11y-ci

**Setmana que ve:**
- Testing completa (checklist de dalt)
- Xavi validació visual
- Deploy a producció si OK

