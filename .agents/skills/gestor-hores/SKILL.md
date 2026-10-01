---
name: time-tracker
description: >
  Automatically track time spent on tasks per project. Use this skill whenever you're working on tasks and need to log hours, generate time reports, or sync tracking with GitHub commits. Also triggers on project work sessions, code development, or when the user asks about time spent, project costs, or budget tracking. Handles automatic session tracking (SessionStart → SessionEnd), per-task logging, subagent time summation, and GitHub commit detection. Generates daily markdown logs and comprehensive reports with totals, daily/weekly averages, and percentage-of-budget evolution.
---

# Time Tracker Skill

Track time spent on tasks automatically, generate reports, and monitor project budgets.

## Quick Start

**Manual entry** (whenever):
```
/time-log [task description] [hours] [optional: notes]
```

**View report** (whenever):
```
/time-report [projecte] [period: today|week|month|all]
```

**Automatic tracking** (Claude Code: SessionStart/SessionEnd hooks · OpenCode: plugin `gestor-hores.js`):
- Sessió comença → tasca nova es crea automàticament
- Inactivitat 30min → tasca es tanca i es registra el temps
- Cada demanda usuari = tasca nova dins la sessió
- **OpenCode:** el plugin escriu marques START/IDLE a `.taques/{projecte}/.sessions.jsonl` (detalls a § OpenCode Integration)

---

## OpenCode Integration

Aquest skill és **multi-plataforma**: funciona amb Claude Code i amb OpenCode sense canvis de behavior. La diferència és *on* s'executa l'auto-tracking:

| Capa | Claude Code | OpenCode |
|------|-------------|----------|
| Hooks de sessió | `SessionStart`/`SessionEnd` (settings.json) | Plugin `gestor-hores.js` (events `session.created`/`session.idle`) |
| Slash commands | `/time-log` etc. (skill purs) | `.md` a `~/.config/opencode/command/time-*.md` |
| Fitxer de sessions | (no) | `.taques/{projecte}/.sessions.jsonl` |
| Logs diaris | `.taques/{projecte}/YYYY-MM-DD.md` | idem (compartits) |

### Com funciona el plugin OpenCode

- Este fitxer: `~/.config/opencode/plugins/gestor-hores.js`
- Escriu una línia JSON per event (append-only, mai esborra):
  ```json
  {"type":"START","sessionID":"...","at":"2026-08-11T18:24:00.000Z"}
  {"type":"IDLE","sessionID":"...","at":"2026-08-11T18:52:00.000Z"}
  ```
- A `.taques/{projecte}/.sessions.jsonl` (gitignored).

### Com usar les sessions per calcular temps reals

Per calcular durada d'una sessió automàtica:
1. Llegeix `.sessions.jsonl`.
2. Aparella cada parell START→IDLE consecutiu (mateix `sessionID`).
3. Durada = `at(END) − at(START)`; si falta parell (IDLE pendent) marca com "oberta".
4. Ignora pauses > 30 min dins d'una sessió (tall en tasques).

Quan hi ha durades automàtiques, registra-les al `.md` diari com:
```
### Tasca: [auto] Session descriptiva
- **Hora inici:** (de START)
- **Durada:** (durada calculada)
- **Font:** plugin OpenCode · .sessions.jsonl
```

---

## How It Works

### Automatic Session Tracking

1. **SessionStart** → Crea entrada tasca automàtica: `[Projecte] — Session started`
2. **User requests** → Cada demanda ("help me redact email", "create function", etc.) genera subtasca automàtica dins sessió
3. **SessionEnd o 30min inactivitat** → Tanca tasca actual + registra temps total
4. Temps = timestamp inici a timestamp fi

### Manual Override

Si necessites registrar temps fora de Claude (tasques fora, GitHub work):

```
/time-log "Redactar proposta" 2.5 "Canvis pressupost Roser SBB"
/time-log "Disseny banner" 1 "External Figma work, no Claude"
```

Registra immediatament a .taques/{projecte}/YYYY-MM-DD.md.

### GitHub Commit Sync

Detecta commits automàticament:
- Llegeix timestamps últims commits
- Si commit feta dur Session obert → suma temps a tasca
- Format: `[GitHub] Commit message — 15 min auto-detected`

(Manual fallback si no pot sincronitzar)

### Subagent Time Summation

Si delegues tasques a agents/subagents:
- Agent exit message conté temps: `total_time: 45min`
- Skill suma automàticament a tasca delegada
- Registra: `[Delegat a OpenCode] [nom tasca] — 45 min`

---

## Directory Structure

```
.taques/                          # Project-specific tracking
├── {projecte}/
│   ├── YYYY-MM-DD.md            # Daily log
│   ├── weekly-report.md          # Aggregated weekly
│   ├── monthly-report.md         # Aggregated monthly
│   └── .sessions.jsonl           # Auto-sessions (OpenCode plugin, append-only)

.taques-central/                  # Global tracking (all projects)
├── YYYY-MM-DD.md                 # Daily log (all projects)
├── weekly-summary.md
└── monthly-summary.md
```

### Daily Log Format (.taques/{projecte}/YYYY-MM-DD.md)

```markdown
# Tracking — [Projecte] — 2026-08-10

## Tasques

### Tasca 1: [Descripció]
- **Hora inici:** 10:00
- **Durada:** 1h 30min
- **Descripció:** [Detalls]
- **Estat:** Completada
- **Notes:** [Opcional]

### Tasca 2: [Descripció]
- **Hora inici:** 11:45
- **Durada:** 45 min
- ...

## Resum diari

| Mètrica | Valor |
|---------|-------|
| Tasques completades | 2 |
| En progres | 0 |
| Hores totals | 2.25h |
| Mitja per tasca | 1h 7min |
```

### Central Log Format (.taques-central/YYYY-MM-DD.md)

```markdown
# Tracking centralitzat — 2026-08-10

| Projecte | Tasques | Hores | Mitjana/tasca |
|----------|---------|-------|---------------|
| guia-globus-vermell | 4 | 7h | 1h 45min |
| altre-projecte | 2 | 3.5h | 1h 45min |
| **TOTAL** | **6** | **10.5h** | **1h 45min** |
```

---

## Reports

### /time-report [projecte] [period]

**Periods:** `today`, `week` (últims 7 dies), `month`, `all`

**Output complet — inclou sempre 5 blocs:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 gestor-hores · Resum 2026-08-11
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① TOTALS
   Hores totals      18.5h
   Dies treballats    5
   Sessions           8
   Tasques            24
   Mitja / dia        3.7h
   Mitja / tasca      46min

② HORES PER DIA  (últims 14 dies, max = 20 blocs)
   dl 11/08  ████████████░░░░░░░░  3.5h
   dv 10/08  ████████░░░░░░░░░░░░  2.0h
   dj 09/08  ─                     0.0h
   dc 08/08  ████████████████████  5.0h
   dm 07/08  ██████████░░░░░░░░░░  2.5h
   dl 06/08  ██████████████░░░░░░  3.5h
   dv 05/08  ████████████░░░░░░░░  2.0h  ← fi de setmana anterior
             [dies anteriors sense activitat omesos]

③ ACTIVITAT PER DIA DE LA SETMANA
   Dl  ██████████████  7.0h  (2 dies)  ★ més actiu
   Dm  ██████          2.5h  (1 dia)
   Dc  ██████████      5.0h  (1 dia)
   Dj  ░░░░░░░░░░░░░░  0.0h  (0 dies)
   Dv  ████████████    4.0h  (2 dies)
   Ds  ░░░░░░░░░░░░░░  0.0h
   Dg  ░░░░░░░░░░░░░░  0.0h

④ EVOLUCIÓ ACUMULADA
   20h │                              ╭──●
   15h │                    ╭─────────╯
   10h │          ╭─────────╯
    5h │  ╭───────╯
    0h └──┴────────┴────────┴────────┴────
         ago 4    ago 7    ago 10   ago 11

⑤ PRESSUPOST (si definit)
   ████████████████░░░░  40h → 18.5h usades (46%)
   Restant: 21.5h · Ritme: On track ✓
   Projecció fi: ~ago 25 (al ritme actual de 3.7h/dia)

⑥ RENTABILITAT (si tarifa i pressupost client definits)
   Tarifa:          65 €/h
   Hores reals:     18.5h  →  cost intern: 1.202 €
   Pressupost client: 2.600 €
   ──────────────────────────────
   Marge brut:      1.398 €  (54%)  ✓ GUANYEM
   Hores disponibles fins a 0 marge: 21.5h restants
   Alerta si marge < 20%: NO ✓

   [Si marge negatiu]
   Marge:          −320 €  (−12%)  ⚠️ PERDENT DINERS
   Hores facturables restants: 0 (pressupost exhaurit)
   Recomanació: revisar abast o renegociar
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Regles de construcció dels gràfics

**Barres horitzontals (blocs ②, ③, ⑤):**
- Caràcter ple: `█`  Caràcter buit: `░`  Buit total: `─`
- Amplada màxima: 20 blocs = valor màxim del període
- Cada bloc = `max_hores / 20` hores
- Etiqueta dia de la setmana en català abreujat: dl dm dc dj dv ds dg

**Gràfic evolució (bloc ④):**
- Eix Y: 5 nivells, de 0 fins al total acumulat arrodonit
- Eix X: dates reals dels dies amb activitat
- Traç: `╭ ─ ╯ ●` per marcar el punt final
- Si només hi ha 1 dia, mostra una línia horitzontal simple

**Bloc pressupost (bloc ⑤):**
- Només apareix si s'ha definit `/time-config [projecte] [hores]`
- Alert ⚠️ si > 80% consumit
- Projecció: `hores_restants / mitja_diaria` → data estimada de fi

### Report Assertions

If pressupost definit:
- Flag si hores > 80% pressupost
- Alert si ritme suggereix overflow
- Suggest si on track (< 50% temps usat)

---

## Commands Reference

```
/time-log [task] [hours] [notes]
  — Registra hores manuals

/time-report [projecte] [period]
  — Genera report complet (6 blocs): today|week|month|all

/time-config [projecte] [pressupost-hores] [tarifa-hora-€] [pressupost-client-€]
  — Definir pressupost d'hores, tarifa i pressupost del client
  — Exemple: /time-config guia-globus-vermell 40 65 2600
  — Guarda a .taques/{projecte}/config.md

/time-export [projecte] [format]
  — Export CSV o JSON per anàlisis

/time-reset [projecte] [date]
  — Reinicia tracking des de data (si necessari)
```

> **OpenCode:** aquests comandaments estan registrats com a slash commands a
> `~/.config/opencode/command/time-*.md`. En OpenCode s'executen amb el mateix
> `/time-*`. En Claude Code funcionen com a ordres directes del skill.

### Config format (.taques/{projecte}/config.md)

```markdown
# Config — [Projecte]

- **Pressupost hores:** 40h
- **Tarifa:** 65 €/h
- **Pressupost client:** 2.600 €
- **Moneda:** EUR
```

---

## Behavior Rules

### Always do:
1. Iniciar tracking a inici de sessió (hook Claude o plugin OpenCode)
2. Detectar cada user request com nova tasca
3. Sumar temps fi de sessió
4. Registrar .md amb durada exacta i descripció
5. Sincronitzar GitHub commits si possible
6. Sumar temps subagents automàtic
7. Generar reportes amb totals + mitjanes + evolució %

### En OpenCode (derivat de § OpenCode Integration):
1. Llegeix `.taques/{projecte}/.sessions.jsonl` per calcula durades reals de sessió.
2. Registra les sessions automàtiques al `.md` diari amb font `plugin OpenCode`.
3. Accepta `$ARGUMENTS` dels slash commands com ja programats (`~/config/opencode/command/time-*.md`).

### Never:
- Comptar temps fora de sessió sense `/time-log`
- Sobreescriure entrades existents (append només)
- Perdre precisió de timestamps
- Deixar tasques sense descripció

---

## Examples

### Example 1: Mail Redaction Task
```
User: "Help me redact response email to Xavier"

[Auto-create task]
Tasca: Help redact response email
Hora inici: 10:00 (auto)

[30 min after user finishes]
SessionEnd detected → registra:
Durada: 30 min
Status: Completed
Entry in .taques/guia-globus-vermell/2026-08-10.md
```

### Example 2: Manual Override (External Work)
```
User: "/time-log 'Design banner mockups' 2 'Figma, no Claude'"

Registra immediatament:
- Tasca: Design banner mockups
- Durada: 2h
- Notes: Figma, no Claude
- Data: today
- Estat: Completed
```

### Example 3: GitHub Sync
```
User commits to GitHub: "feat(layout): add responsive grid"
Commit timestamp: 14:30

[Skill detects commit during open session]
Auto-create: [GitHub] feat(layout): add responsive grid
Durada: auto-detect (15 min based on commit proximity)
Registra a tracking log
```

### Example 4: Report Query
```
User: "/time-report guia-globus-vermell month"

Output: Markdown report complet amb 5 blocs:
① Totals: 45h, 12 dies, 28 tasques, mitja 3.75h/dia
② Barres per dia (últims 14 dies visibles)
③ Heatmap per dia de la setmana (dl–dg)
④ Gràfic evolució acumulada
⑤ Pressupost: 40h → 5h restant (88%) ⚠️ ATENCIÓ
```

---

## Edge Cases

**Multiple sessions same day:**
- Cada SessionStart → nova entrada
- Consolidat al resum diari final

**Delegat a subagent:**
- Marca tasca: `[Delegat a {agent-name}]`
- Suma temps automàtic quan agent completa
- Registra agent name + temps

**No internet / GitHub unavailable:**
- Continua tracking local
- Sincronitza commits quan reconnecta

**Manual time entry after session closed:**
- Append a fitting día dins .md
- Mantenir cronologia clara

---

## Integration Points

- **Claude Code:** `SessionStart`/`SessionEnd` hooks inicia/tanca tracking.
- **OpenCode:** plugin `gestor-hores.js` captura `session.created`/`session.idle` i escriu `.sessions.jsonl`.
- **Slash commands:** OpenCode (`~/.config/opencode/command/time-*.md`) + Claude (ordres directes).
- **TaskCreate/TaskComplete:** Detecta nuevas tasques
- **Git commits:** Sync timestamps (si .git/ accessible)
- **Subagent exit:** Captura temps automàticament
- **Manual command:** `/time-log` always works (ambdós)

---

## Notes for Implementation

- Timestamps precisos (HH:MM format)
- Markdown append-only (no overwrites)
- OpenCode: `.sessions.jsonl` és append-only i gitignored; no esborrar manualment.
- Auto-detect inactivitat: >30min sense user input = SessionEnd (o IDLE al plugin)
- Pressupost tracking: opcional, però if defined, sempre reporta vs budget
- CSV export per analyses externos (costos, trends, etc.)
