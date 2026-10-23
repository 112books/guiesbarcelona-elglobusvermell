# Estat de la feina — 23/10/2026 (punt i seguit per a Claude)

Document de traspàs: què està desplegat, què queda pendent, què està trencat i com continuar.
Última actualització: 23/10/2026, ~13:30 (Europe/Madrid).

## 0. Estat del repositori

| Element | Valor |
|---|---|
| Branca local | `main` |
| `origin/main` | `06f750cd` (Xavi segueix editant des del CMS) |
| Commit local **NO pujat** | `c78022ae` — neteja de `tipus: individual` reintroduïts + versió de memòria cau del CMS |
| Últim commit desplegat | `a1933f0d` (ja dins d'origin/main) |
| CI del commit desplegat | Deploy → GitHub Pages: **verd** · Accessibilitat (pa11y-ci): **verd** |
| CI `Verificació diària dels números` | **vermell** — causa i solució al punt 4 |

⚠️ Abans de tocar res: `git pull --rebase origin main`. Xavi està editant arquitectes en directe i cada edició seva pot tornar a posar `tipus: individual` (vegeu punt 5).

## 1. Fet i desplegat (commit `a1933f0d`)

### 1.1 Etiqueta «Individual» fora (petició de Xavi, 23/10)
- Treta la línia `tipus: individual` de **totes** les fitxes d'arquitecte (eren 150; el mateix dia Xavi n'havia canviat una a `artista`, així que al final 149).
- `static/admin/cms/config.yml`: el camp «Tipus» torna a ser **opcional**, amb l'opció **«Cap (sense etiqueta)»** (`value: ""`) i sense «Individual» a la llista.
- `themes/guiesbcn-elglobusvermell/layouts/arquitectes/terms.html`: l'etiqueta només es pinta per a `estudi` i `artista`.
- Verificat al build de staging: **0** etiquetes «Individual», **47** «Estudi», **16** «Artista» (Xavi n'ha afegit un).
- Resposta de Xavi al mail: «Perfecte! Que individual no aparegui. M'és igual si d'amagat segueix tenint l'etiqueta.»

### 1.2 Tres fitxes de biblioteca noves (mail de Joan a Xavi, 23/10)
- Creades `biblioteca-esquerra-de-leixample-agusti-centelles`, `biblioteca-fort-pienc-ana-maria-moix` i `biblioteca-camp-de-larpa-caterina-albert` (ítems 5, 6 i 39 del llistat nou de Xavi).
- Tret `- biblioteques` de `edifici-collage-centre-cultural-teresa-pamies`, `illa-dequipaments-alchemika` i `illa-dequipaments-fort-pienc`, i traslladats els àlies `/biblioteques/...` a les fitxes noves. Motiu: eren el mateix edifici i sortien dues vegades al plànol (i dos fitxers amb el mateix àlies).
- El plànol de Biblioteques queda amb **51 fitxes**.
- Pendent de validar amb Xavi en la propera revisió (ell encara no ha vist aquests canvis publicats).

### 1.3 Fotos de la carpeta de Xavi
- 27 fotos aplicades (21 reemplaçades + 6 noves): Joan Miró (3, amb `fotos_addicionals`) i Dipòsit de les Aigües/UPF (2). La resta, una per biblioteca.
- Comprimides abans de pujar-les a **≤1.600 px i ≤400 KB** (27 fitxers, 9,1 MB en total).
- `data/imatges_dims.json` regenerat (428 imatges).
- **Descoberta important**: abans d'això, 33 fitxers `static/img/elements/biblioteca-*.jpg` eren **la mateixa imatge** (la portada del plànol, md5 `d0e19177…`). Ara 13 ja tenen foto real; **20 encara mostren la portada del plànol** perquè no eren a la carpeta que va enviar Xavi.

### 1.4 Tauler i registre
- `static/admin/revisio/tasques.json`: entrada nova `etiqueta-individual` i `biblioteques-noves-3`; `fotos-multiples` i `fotos-biblioteques-on` passen a «fet»; decisió nova `biblioteques-llistat-55` (pendent).
- `.ai/REGISTRE-CANVIS-FITXES.md`: entrades **#9** i **#10**.

## 2. Commit local `c78022ae` — NO pujat

Contingut:
- Neteja de `tipus: individual` **reintroduïts per Xavi** després del desplegament (21 fitxes en dues tandes: 13 + 8). El CMS del seu navegador encara anava amb la configuració antiga.
- `static/admin/cms/index.html`: `CMS_CACHE_VERSION` pujat a `'2026-10-23-1'` per forçar la recàrrega del CMS als editors i aturar els reintroduïments.
- `static/admin/revisio/tasques.json`: nota a l'`intro` («si el desplegable encara et surt amb "Individual", recarrega el CMS»).

Acció recomanada en reprendre: `git pull --rebase origin main`, comprovar que Xavi no hagi tornat a posar `tipus: individual` (`grep -rl '^tipus: individual' content/ca/arquitectes`), tornar a netejar si cal, i **pujar**.

## 3. Resposta a Xavi (esborrany, pendent d'enviar)

> Hola, Xavi!
>
> Respostes curtes:
>
> **Fotos múltiples** — Tenies raó: a staging encara no es veien perquè les fotos noves encara no estaven publicades. Ja hi són: la Biblioteca Joan Miró té 3 fotos (carrusel amb fletxes i punts) i el Dipòsit de les Aigües / UPF, 2. Refresca la pàgina i les veuràs.
>
> **Pes i resolució** — Cap problema: en publicar, el sistema les redueix a un màxim de 1.600 px d'amplada i 400 KB. Les originals de 2–9 MB queden ajustades totes soles; pots enviar-les com les tens.
>
> **Etiqueta «Individual»** — Fet: ja no surt enlloc. L'hem treta de les fitxes i, a l'editor, el camp «Tipus» torna a tenir l'opció «Cap (sense etiqueta)» (no és obligatori). Només es mostren «Estudi» i «Artista». Si el desplegable encara et surt amb «Individual», recarrega la pàgina del CMS.
>
> **Biblioteques noves** — Hem creat les tres fitxes que ens deies (Esquerra de l'Eixample – Agustí Centelles, Fort Pienc – Ana María Moix i Camp de l'Arpa – Caterina Albert) amb les teves fotos, i les hem tretes dels equipaments on sortien barrejades perquè no surtin dues vegades al plànol.
>
> Una cosa: el llistat nou té 55 ítems i al plànol n'hi ha 51. Falten les 5 de la «Xarxa de Biblioteques Socials» (Centre de Documentació de l'Ateneu Enciclopèdic Popular, Biblioteca Popular Josep Pons, Centre de Documentació Mercè Grenzner, Fundació Salvador Seguí i Biblioteca Nova Babilònia). Les creem? I la fitxa «Biblioteca Vall d'Hebron» (futura biblioteca) no surt al llistat: la traiem del plànol o la deixem?
>
> Gràcies!

## 4. Verificació diària dels números — VERMELL (preexistent, no causat per aquesta feina)

Estat: el workflow `Verificació diària dels números del web` falla des del 23/10 (l'última execució bona és del 22/10 a les 12:11 UTC).

**Causa**: el 22/10 (commit `46f142b6`) es va redissenyar la portada **sense xifres**. El script `scripts/verifica-numeros-web.py` encara llegeix les 4 xifres de la portada amb la marca `pa-stat-num`, que ja no existeix. Les xifres viuen ara a **`/presentacio/`** (`presentacio/list.html` + `partials/xifres-projecte.html`).

**Solució proposada** (provada a mitges, el canvi es va revertir per no deixar-ho a mitges):
1. Fer que `numeros_publicats()` llegeixi `urljoin(LIVE_URL, "presentacio/")`.
2. **Atenció amb el minify**: Hugo `--minify` treu les cometes; al web surt `<div class=stat-number data-target=659>659</div>`. El regex ha de ser `r'class="?stat-number"?[^>]*>\s*([^<]+?)\s*<'` (o similar), no `class="stat-number"`.
3. **Ordre a la pàgina**: guies, elements documentats, arquitectes, anys (abans era edificis, guies, arquitectes, anys).
4. Segona discrepància detectada: la pàgina publica **292** arquitectes i el repo en compta **290** (noms distints a les fitxes). Sospita: termes de la taxonomia duplicats (a `public/arquitectes/` hi ha 292 directoris, i el llistat en pinta 290). Cal decidir si la xifra publicada ha de comptar aquests duplicats o si s'han de fusionar els termes. No s'ha tocat res.
5. El workflow només té `on: schedule`; no té `workflow_dispatch`. Si es vol provar sense esperar l'endemà, afegir-hi `workflow_dispatch:`.

## 5. Risc actiu: Xavi reintrodueix `tipus: individual`

Mentre Xavi edita amb la memòria cau antiga del CMS, cada desada torna a escriure `tipus: individual` a la fitxa. És **invisible al web** (la plantilla només pinta Estudi/Artista), però embruta les dades. El bump de `CMS_CACHE_VERSION` del commit `c78022ae` ho hauria d'aturar quan es pugi. Mentrestant, comprovar-ho amb:
```
grep -rl '^tipus: individual' content/ca/arquitectes
```

## 6. Altres punts oberts (no bloquejants)

- **20 biblioteques** encara ensenyen la portada del plànol com a foto (no eren a la carpeta de Xavi). Llista per calcular amb el md5 `d0e19177b3a1eccd7ef9a3f7f8a3fd2c`.
- **5 biblioteques sense cap foto**: Bon Pastor – Josefina Castellví, Canyelles – Maria Àngels Rivas, Ateneu Barcelonès, Les Roquetes – Rafa Juncadella, Vallcarca i els Penitents – Maria Antonieta Cot. (I `biblioteca-vall-d-hebron`, futura biblioteca, tampoc no en té.)
- **Llistat de 55 ítems vs 51 fitxes**: 5 de la xarxa social sense fitxa; `Biblioteca Vall d'Hebron` és una fitxa que no surt al llistat. Decisió pendent (entrada `biblioteques-llistat-55` del tauler).
- La carpeta `Fotografies de les biblioteques/` (224 MB) és **fora de git** (untracked). No s'ha d'afegir mai.

## 7. Ordre suggerit per continuar

1. `git pull --rebase origin main`.
2. Netejar `tipus: individual` si n'hi ha; `hugo --minify --environment staging` i comprovar que no surt cap `arquitecte-tipus--individual` a `public/arquitectes/index.html`.
3. Pujar `c78022ae` (o el que en resulti) i comprovar amb `gh run list` que Deploy i Accessibilitat estan verds.
4. Arreglar `scripts/verifica-numeros-web.py` segons el punt 4 i validar amb `LIVE_URL=… python3 scripts/verifica-numeros-web.py` (revertir `.ai/VERIFICACIO-NUMEROS.md` i `.ai/numeros-web-history.json` després de provar-ho en local, perquè els actualitza el CI).
5. Enviar la resposta a Xavi (punt 3) i resoldre amb ell el tema dels 55 ítems.
