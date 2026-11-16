# Informe — jornada del 16/11/2026

**Data:** 16/11/2026
**Autoria:** Joan (LinuxBCN) amb assistència d'IA
**Context:** reunió amb en Xavi a les 10:00 (Nau Bòstik) i jornada de feina fins al vespre.
**Commits:** `0d2b7480`, `bad131e2`, `73a44064`, `ddee61eb`, `081e28cb`, `12f77e00`, `2295ea15`, `9d3127cf`, `60bc302a`, `318cf52b`, `22d26cfe` (repo públic) · `fc2568f`, `3729629`, `7694200`, `0537146`, `9d9849f`, `65010b7` (control de temps, repo privat) · `2c16c2d`, `c0ccae1`, `06bc421` (mails, repo intern)

---

## 1. Què s'ha fet

### 1.1 Sincronització
El repo públic anava 103 commits endarrerit (26 automàtics, 75 de `xaviglobus` i 2 edicions fetes des de la web de GitHub). Fast-forward sense conflictes i build de comprovació correcte. Els altres tres repositoris ja estaven al dia.

### 1.2 Tauler de revisió (`bad131e2`)
Símptoma: la pàgina es quedava en «No s'han pogut carregar les tasques».
Causa: la fitxa `arquitectes-orfes-pendents` (llista dels 92 noms) no tenia ni `opcions` ni `resposta`, i el pintat feia `item.opcions.length` → excepció dins del `.then` → el `.catch` mostrava l'error i la resta de seccions no es pintaven.
Solució: les fitxes informatives es pinten sense opcions; `enllacos` cau a `dades` quan n'hi ha; `etiquetaOpcio` i el comptador fan servir llistes per defecte.
Verificació: banc de proves en Node amb DOM simulat (33 decisions, 79 canvis) i Chrome headless contra staging.

### 1.3 Disseny aprovat a la reunió (`73a44064`, `081e28cb`)
- Fora `border-left` de `.arquitecte-bio` (biografia).
- Fora `border-left` de `.llistat-element-arquitectes` i `padding-left` de 1,5rem a 0,5rem.
- `.publicacio-banda` passa a `display:none` i s'elimina el `<div>` de la plantilla.
- Portada: «a través de l'arquitectura» (sense «la seva»).
- `.publicacio-cap h1` deixa de fer `color-mix` amb el color del plànol.

### 1.4 Peu de la fitxa (`73a44064`)
Títols llargs del `fitxa-nav` amb `text-overflow: ellipsis`; la fletxa queda en un `span` a part perquè el retall no se la mengi, amb `title` per veure el nom sencer. Navegació amb `ArrowLeft`/`ArrowRight` al document, ignorant els events ja agafats pel carrusel (`defaultPrevented`), els camps de text i els modificadors.

### 1.5 Llistat dels plànols (`ddee61eb`)
Causa: el commit `61292ff5` (M6/T06, 6/11) va treure el llistat del mapa general —que era el que demanava Xavi— i, de passada, el contenidor `#llistat-grups` de `publicacions/term.html` i `temes/single.html`. Els 13 textos de plànol tenen l'apartat «## Llistat» i es quedava buit.
Solució: contenidor restaurat, sense l'`aria-hidden` que duia (amagava la llista als lectors de pantalla).
Verificació: Poblenou 77 fitxes, GATCPAC 43, tema Espai públic 114.

### 1.6 Arquitectes (`12f77e00`, `2295ea15`)
- **A&EB**: la fitxa curada era a `content/ca/arquitectes/aeb/` i la taxonomia genera el terme amb el caràcter literal (`a&eb`). Dues entrades al llistat —«(1 edifici)» i «Estudi (0 edificis)»— i l'edifici (Set Vides) no sortia enlloc. `git mv` a `a&eb` amb `aliases` a `/arquitectes/aeb/`.
- **Duplicats del mateix origen**: la llista d'arquitectes descarta les entrades que comparteixen adreça i conserva el `tipus`. Resol Arriola & Fiol Arquitectes, OAB, Prince Smith & Son i SV60. Resultat: 297 entrades, cap adreça repetida.
- **Enllaços**: `arquitectes/term.html` no passava `arquitectes_urls` al JavaScript (les altres quatre llistes sí), i el valor per defecte de `mapa.js` era `/arquitectes/`. Ara les rep, i si un nom no té fitxa es mostra com a text.
- Registre: `.ai/REGISTRE-CANVIS-FITXES.md` #19. Cap fitxa d'element tocada.

### 1.7 Paràgrafs de les descripcions (`9d3127cf`)
La migració va aplanar els paràgrafs: 111 fitxes tenien la descripció en un sol bloc (Ca l'Alier, 1.977 caràcters seguits).
Mètode: parseig del dump `wp_full-20260729.sql` (2.456 entrades), conversió de l'HTML a text amb marca de paràgraf, i **alineació paraula a paraula** (sense distingir majúscules) entre la descripció del fitxer i el text del WordPress. Només s'insereixen salts on l'original en tenia.
Garanties: el text resultant és idèntic paraula per paraula (verificat als 111 fitxers, 0 diferències); 262 paràgrafs; 105 textos que no coincideixen exactament **no s'han tocat**; còpia prèvia en branca `backup/paragrafs-abans-20261116` i tarball `/tmp/elements-backup-20261116.tgz`.
Complement: `descripcio` es pinta amb `markdownify` i l'editor del CMS passa a `widget: markdown` (fitxa i intervencions).

### 1.8 Tipus d'intervenció (`22d26cfe`)
«Ús actual» i «Nom actual» afegits a la llista de tipus de l'editor, perquè es pugui indicar l'ús o el nom actual de l'edifici com una intervenció més. Ajustada la condició que amaga la fila «Arquitectes»: aquests dos tipus no són obres. Build idèntic abans i després (només difereixen les 3 pàgines d'arquitecte amb «&», que canvien entre dues builds iguals: bug conegut de Hugo).

### 1.9 Documentació i traçabilitat
- Tauler: 82 «fets» i 42 decisions, amb enllaç a cada canvi per verificar.
- Full de ruta: bloc de sessió 16/11 amb els pendents.
- Mail de final de dia: `docs/2026-11-16-mail-xavi-feina-feta-i-pendents.md` (esborrany).
- Control horari: 13 tasques, 6h 45 (aprox.), amb commit per tasca.

## 2. Incidència d'infraestructura
El deploy a GitHub Pages del commit `318cf52b` va fallar amb **HTTP 500** («is githubstatus.com reporting a Pages outage? Please re-run the deployment at a later time»). Rellançat amb `gh run rerun` i verd. És el mateix símptoma que els del 5 i 6/11; si es repeteix, cal revisar la configuració de Pages del repositori.

## 3. Pendent
1. A/B de les dues columnes de la pàgina final de cada plànol (retocs de Xavi inclosos).
2. Disposició de la intervenció sense arquitecte.
3. Revisió dels 105 textos que no coincideixen amb el WordPress.
4. Redireccions automàtiques en renombrar.
5. Nou decisions pendents de Xavi (les 7 del mail).
