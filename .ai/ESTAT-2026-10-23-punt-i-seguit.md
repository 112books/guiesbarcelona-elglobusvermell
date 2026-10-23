# Estat de la feina — 23/10/2026 (fi de jornada)

Document de traspàs: què està desplegat, què queda pendent, què està trencat i com
continuar. Substitueix la versió de mig matí del mateix dia (aquest document n'és
l'actualització).

Última actualització: 23/10/2026, 24:00 (Europe/Madrid).

## 0. Estat del repositori

| Element | Valor |
|---|---|
| Branca local | `main` = `origin/main` (cap commit pendent de pujar) |
| Últim commit | `acf25730` — docs(mails): tres esborranys per dilluns |
| CI de l'últim push | Deploy → GitHub Pages: **verd** · Accessibilitat (pa11y-ci): **verd** |
| Build local | `hugo --minify --environment staging` net · 1.299 pàgines · 681 àlies |
| Fora de git (mai afegir) | `Fotografies de les biblioteques/` (224 MB), `originals/` |

Xavi ha estat editant arquitectes en directe tota la tarda (centenars de commits
«Update Arquitecte»). Cada cop que es reprèn: `git pull --rebase origin main`,
comprovar `grep -rl '^tipus: individual' content/ca/arquitectes` i tornar a pujar.

## 1. Fet al matí (`ca49d26b`, `e0f00bac`, `a1933f0d`)

- Etiqueta «Individual» fora de totes les fitxes d'arquitecte; el camp «Tipus» del
  CMS és opcional, amb l'opció «Cap (sense etiqueta)».
- Tres fitxes de biblioteca noves creades — **revertides a la tarda** (vegeu §2).
- 27 fotos de biblioteques aplicades (21 reemplaçades + 6 noves), amb
  `fotos_addicionals` a Joan Miró (3) i Dipòsit de les Aigües (2).

## 2. Fet a la tarda

| Commit | Què |
|---|---|
| `ab45f18b` | `tipus: individual` fora de les **50 fitxes** que en quedaven (43 + 7 que Xavi va tornar a desar). `CMS_CACHE_VERSION` → `2026-10-23-3`. |
| `71e7b575` | **B3**: adreça repetida fora de **37 descripcions** (només casos inequívocs). |
| `fc501e3f` | **B2**: **75 fitxes**. Fora l'etiqueta «Categoria:» de 66 textos, `tipologia` omplerta a 64, autor i any separats en 11 intervencions, i la fila «Projecte» amagada quan duplica una intervenció (`single.html`). |
| `531b7fbe` | Tauler: **7 preguntes noves** al Xavi + esborrany de correu (`.ai/PREGUNTES-XAVI-2026-10-23.md`). |
| `43773642` | Fotos: dues orfes col·locades (Fort Pienc, Edifici Collage) i recuperada la de l'Edifici d'oficines Llull 122, que sortia trencada. |
| `a16fa9ae` | Tauler: tretes de «pendent de fer» les tasques de B3 i B2 que ja eren als canvis. |
| `acf25730` | Tres esborranys de correu per dilluns (`.ai/MAILS-PER-DILLUNS-2026-10-26.md`). |

Detall complet, amb xifres i criteris, al `.ai/REGISTRE-CANVIS-FITXES.md`
(entrades **#11 – #15**).

### Coses que han quedat arreglades de pas

- **Cap fitxa amb una imatge trencada**: `edifici-doficines-llull-122` apuntava a un
  fitxer que no era al disc.
- Cap referència a imatges inexistents a la resta de fitxes (comprovat sobre les 658).

## 3. Risc actiu: el CMS reintrodueix `tipus: individual`

El select del CMS **conserva el valor que troba al fitxer** encara que ja no sigui a
la llista d'opcions. Per això, mentre el navegador de l'editor tingui la versió
antiga en memòria cau, cada desada el torna a escriure. S'ha netejat dues vegades i
s'ha pujat `CMS_CACHE_VERSION` a `2026-10-23-3` perquè l'editor es netegi sol en
obrir-se. És **invisible al web** (les plantilles només pinten «Estudi» i «Artista»),
però embruta les dades.

Comprovació ràpida:

```
grep -rl '^tipus: individual' content/ca/arquitectes
```

## 4. Verificació diària dels números — RESOLT

El bug del 22/10 (el script llegia les xifres de la portada, que ja no hi són) està
arreglat al commit `1469cb45`: apunta a `/presentacio/` i el regex funciona amb el
HTML minificat. L'execució manual del 23/10 a les 12:46 UTC va sortir **tota verda**
(659 / 13 / 292 / 1928–2026). Pendent només de veure el pròxim run programat
(06:30 UTC) per donar-ho per tancat del tot.

## 5. Coses obertes (cap dins del repositori)

- **Tauler de revisió**: 29 decisions pendents (7 de noves avui), 7 tasques nostres
  i **35 canvis** que esperen el «Verificat i OK» de Xavi.
  `https://112books.github.io/guiesbarcelona-elglobusvermell/admin/revisio/`
- **Fotos**: 26 fitxes del plànol de Biblioteques sense foto pròpia (20 amb la
  portada del plànol, 6 sense cap imatge). La llista és a la decisió
  `fotos-biblioteques-on` i al punt 8 de l'esborrany de correu.
- **Desplegament a producció**: informe a `.ai/informe-desplegament-produccio-2026-10.md`
  (ja versionat). Falten les credencials de Jorge i decidir escenari (GitHub Pages +
  formulari al servidor vell, o tot al servidor). Tres correus preparats a
  `.ai/MAILS-PER-DILLUNS-2026-10-26.md`.
- **B2/B3 pendents de dades**: 45 casos de B2 per revisar a ull, 46 de text tallat a
  la migració (calen les dades del WordPress) i 48 adreces (depenen de la decisió
  `b3-adreces-restants`).

## 6. Avisos per a la propera sessió

- **No afegir mai** `Fotografies de les biblioteques/` al repositori (224 MB de fotos
  rebudes de Xavi). `originals/` ja és al `.gitignore`.
- `scripts/redimensiona-imatges.py` passejat per `static/img/elements` toca **149
  imatges** que passen de 400 KB (estalvi ~35 MB, només recomprimir). Si es fa,
  ha de ser en un commit propi i amb l'OK de Joan: no barrejar-ho amb contingut.
- El build no falla si una fitxa apunta a una imatge inexistent: la pàgina surt amb
  la imatge trencada. Val la pena comprovar-ho abans de tancar qualsevol tanda:
  `grep -rh -o '/img/elements/[a-z0-9.-]*\.jpg' content/ca/elements/*.md | sort -u | while read p; do [ -f "static$p" ] || echo "FALTA: $p"; done`

## 7. Ordre suggerit per continuar

1. `git pull --rebase origin main` i netejar `tipus: individual` si n'hi ha; pujar.
2. Enviar els correus 1 i 2 de `.ai/MAILS-PER-DILLUNS-2026-10-26.md` (Xavi) i, quan
   contesti, el 3 (Jorge).
3. Els 45 casos de B2 (feina nostra, es nota al web, no depèn de ningú).
4. Quan Xavi respongui: aplicar les decisions del tauler (les 7 noves primer) i
   tancar la llista de fotos de biblioteques.
