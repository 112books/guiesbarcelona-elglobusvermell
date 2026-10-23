# Tres correus per dilluns (26/10/2026)

Esborranys a punt per copiar i enviar. Ordre recomanat: **1 → 3 → 2**.
El correu 1 ha de sortir abans que escriguem a en Jorge: primer el vistiplau d'en Xavi.

---

## 1 · A en Xavi — permís per parlar amb en Jorge

**Assumpte:** Guies de Barcelona — parlar amb en Jorge per tancar el desplegament

Hola, Xavi!

El web nou ja està acabat i funcionant a l'entorn de proves. El que ens falta
per tancar-lo és la part final: penjar-lo al subdomini de debò i que el formulari
de contacte torni a enviar correus.

Per fer-ho ens cal parlar amb en Jorge, que és qui té el servidor on ara viu el
WordPress. Li volem plantejar dues coses:

1. **Muntar ja el formulari de contacte al seu servidor**, sense tocar res més del
   que hi ha ara. Així el formulari funciona mentre acabem de validar el web.
2. **Quan el web estigui validat, traslladar-ho tot** al subdomini
   `guiesbarcelona.elglobusvermell.org`, fent abans una **còpia de seguretat
   completa del WordPress actual** (fitxers i base de dades), per si mai calgués
   tornar enrere.

I li volem demanar un **informe tècnic del servidor**: si és un servidor que
gestiona ell o un allotjament amb panell, què hi ha instal·lat i amb quines
versions, quant espai i quin cost té, com es fan les còpies de seguretat, i com
teniu muntat el correu d'El Globus Vermell. Veiem que feu servir Gmail i adreces
«normals» i ens agradaria entendre com està configurat abans de tocar res.

Amb aquest informe us podrem portar les dues opcions per decidir: **quedar-nos el
servidor actual amb un pla d'ús que cobreixi el web i tot el correu d'El Globus**,
o **migrar-ho a un altre lloc** que puguem gestionar nosaltres.

El que et demano:

- Que ens autoritzis a contactar-hi directament.
- O, si ho prefereixes, que ens facis tu la presentació per correu.
- El seu correu i telèfon.

No es tocarà res del que hi ha ara fins que el web no estigui validat i la còpia
de seguretat estigui feta.

Gràcies!

---

## 2 · A en Xavi — estat i què necessitem del vostre vistiplau

**Assumpte:** Guies de Barcelona — què tenim pendent de la vostra mirada

Hola, Xavi!

Hem avançat molt aquests dies i hi ha força coses esperant que les veieu. Us faig
un resum curt; si voleu, ho repassem junts en una trucada de mitja hora.

**Ja és fet i us toca verificar-ho** (35 canvis)

Els més visibles: fora l'etiqueta «Individual» dels arquitectes; l'adreça ja no es
repeteix a l'inici de les descripcions; hem tret l'etiqueta «Categoria:» que havia
deixat el WordPress (aquesta dada ara surt al camp «Tipologia»); la fila «Projecte»
ja no surt dues vegades; i 27 biblioteques tenen ara foto pròpia.

**Esperant una decisió vostra** (les set darreres)

1. «Edifici original»: el convertim en una intervenció «Projecte original»?
2. Les 48 fitxes que encara tenen l'adreça dins del text: la traiem tota, només la
   primera, o la deixem?
3. Intervencions que són dues obres («Vora. 2013 + 2019»): se separen?
4. Els 4 premis que surten dins del text: els movem al camp «Premis»?
5. Les 4 fitxes que ja no surten al plànol en paper: les mantenim al web?
6. Una fitxa d'arquitecte que no lliga amb cap obra («oab-(carlos-ferrater)»):
   la unifiquem?
7. Mercats: «mercat-de-la-marina» i «placa-i-mercat-de-la-marina» són el mateix.
   I el Mercat de Sant Gervasi no apareix a la vostra llista: ha de sortir?

**Bloquejat per dades vostres**

- **Fotos**: 26 biblioteques encara no tenen foto de la biblioteca (20 ensenyen la
  portada del plànol). Tenim la llista feta.
- **Paleta definitiva** per als plànols.
- **«En paper»**: la portada retallada que ens heu de fer arribar.
- **Biblioteques**: el llistat té 55 ítems i el plànol 51 (les 5 de la xarxa
  social no tenen fitxa; la Vall d'Hebron hi és i al llistat no).
- **Tipografia**: si la Public Sans que ja està aplicada us sembla bé, tanquem les
  dues preguntes que teníem obertes sobre tipografia.

Tot és al tauler, preguntes incloses, amb les opcions i la nostra recomanació:
https://112books.github.io/guiesbarcelona-elglobusvermell/admin/revisio/

Gràcies!

---

## 3 · A en Jorge — formulari de contacte i informe del servidor

**Assumpte:** Guies de Barcelona (El Globus Vermell) — formulari de contacte i informe del servidor

Hola, Jorge!

Soc en Joan, de l'equip que està fent el web nou de les Guies de Barcelona per a
El Globus Vermell. En Xavi ens ha donat el vistiplau per escriure't.

Us explico la situació: estem substituint el WordPress actual per un web nou, ja
acabat i en funcionament a un entorn de proves. Per posar-lo en marxa ens calen
dues coses teves.

**1. Fer servir el servidor per al formulari de contacte**

El formulari és una pàgina que enviarà les dades a un sol fitxer PHP que envia el
correu. Necessitaríem saber:

- Si podem tenir accés (SSH o SFTP) i amb quin usuari.
- La ruta del document root del subdomini `guiesbarcelona.elglobusvermell.org`
  (on hauria d'anar el web nou).
- Si el servidor té PHP i des de quina versió, i si pot enviar correu (amb
  `mail()` o amb un servidor SMTP).

**2. Un informe tècnic del servidor**

Per decidir com ho plantegem a partir d'ara:

- Proveïdor, pla i cost. És un servidor que gestiones tu o un allotjament amb
  panell de control?
- Sistema operatiu, servidor web (Apache/Nginx), versió de PHP i de base de dades.
- Espai en disc i amplada de banda.
- Certificats TLS: com es renoven.
- Còpies de seguretat: qui les fa, cada quant i on es guarden.
- Domini i DNS: a nom de qui estan i qui els gestiona.

**3. El correu**

Ens interessa entendre com teniu muntat el correu d'El Globus Vermell, perquè
veiem que es fa servir Gmail i adreces «normals»:

- On són els registres MX del domini (Google Workspace, un altre proveïdor…)?
- Com surten els correus que envia el web? Teniu SPF, DKIM i DMARC configurats?
  Ho preguntem perquè el formulari de contacte no acabi a la bústia de brossa.
- Hi ha alguna raó concreta per fer servir Gmail per a unes adreces i el correu
  «normal» per a unes altres?

**4. Còpia de seguretat abans de res**

Abans de traslladar el web volem una còpia completa del WordPress actual (fitxers
i base de dades), per poder tornar enrere si calgués.

Amb tot això podrem valorar dues opcions i portar-les a en Xavi perquè decideixi:
mantenir el servidor amb un pla d'ús que cobreixi el web i tot el correu d'El
Globus, o migrar-ho a un altre lloc. **De moment no canviem res.**

Gràcies!

---

## Notes per a nosaltres (no enviar)

- `envia.php` no és al repo: s'ha de fer de zero (llegeix `nom`, `email`, `missatge`,
  `rgpd`, honeypot `web`; envia a `info@elglobusvermell.org`). ~50 línies.
- Si el formulari queda al servidor de Jorge i el web a GitHub Pages, cal
  parametritzar l'`action` per entorn (`config/production/params.toml`).
- La clau pública SSH de LinuxBCN ja és a GitHub com a deploy key; cal que en
  Jorge la instal·li al servidor (enviar-li el text de la clau quan demanem accés).
- Si anem a l'escenari de servidor propi: `deploy-prod.yml` amb `rsync` + secrets.
- Informe de referència: `.ai/informe-desplegament-produccio-2026-10.md`.
