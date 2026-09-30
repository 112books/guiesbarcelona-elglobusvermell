# Correu (fil) — MAPATGE-URLS.md no adjuntat

**De:** Joan (LinuxBCN) → Xavi (El Globus Vermell)
**Data:** 2026-09-03 (Xavi respon)
**Assumpte:** Eina de control de la migració — MAPATGE-URLS.md
**Origen:** enganxat per Joan (sessió 2026-09-30)

> Text literal del fil. No editar ni resumir.

---

Meu Bon dia Xavi,

T'envio adjunt el document MAPATGE-URLS.md que hem preparat com a eina de control de la migració del web.

Per a que serveix

El document recull totes les adreces (URLs) que existeixen al web actual de producció (WordPress) i les creua amb les equivalents al nou web (Hugo). L'objectiu és doble:

Verificar que cap pàgina s'ha perdut en el procés de migració.
Disposar d'una referència clara de quina adreça té cada contingut, tant a l'actual com al nou, per configurar els redireccionaments automàtics en el moment del canvi de servidor.
Resum dels números

El web actual (WordPress) té 666 adreces indexades:

649 fitxes d'edificis
11 textos de guia (presentació de cada publicació)
6 pàgines estàtiques (portada, En paper, Crèdits, política de privacitat, etc.)
Al nou web (Hugo) totes aquestes adreces queden cobertes:

3 adreces són idèntiques (portada, En paper, Crèdits): no cal res.
660 adreces canvien d'estructura (per exemple, /mercats/mercat-de-la-boqueria/ passa a /elements/mercat-de-la-boqueria/): el sistema de redireccionament ja està configurat al codi, de manera que qualsevol enllaç extern o resultat de cercador continuarà funcionant.
2 adreces s'eliminen: la pàgina anti-spam de WordPress i el sitemap.html, que no tenen equivalent perquè no eren contingut real.
A més, el nou web incorpora ~221 adreces noves que no existien al WordPress: les pàgines individuals dels 197 arquitectes, les noves publicacions i les pàgines legals.

Com llegir el document

El fitxer és una taula per a cada secció (pàgines estàtiques, textos de guia, fitxes per categoria de plànol, contingut nou). Cada fila mostra:

L'adreça al WordPress actual
L'adreça equivalent al nou Hugo
Un indicador d'estat: si és idèntica, si canvia (i per tant cal redirect) o si s'elimina
Propers passos relacionats

Quan fem el canvi de servidor (el «tall de domini»), hem de configurar les redireccions 301 (les permanents, que traslladen el posicionament als cercadors) al servidor. El document serveix com a base per generar automàticament la llista de regles. D'aquesta manera, qualsevol persona que arribi al web des d'un resultat de cerca antic, un enllaç extern o un marcador del navegador serà redirigida a la nova adreça de forma transparent, sense errors ni pèrdua de posicionament.

Quedo a la teva disposició per qualsevol dubte.

->
———————————————————
Joan Linux Mz Serres
joan@linuxbcn.com
http://linuxbcn.com
https://t.me/Linuxbcn
Resposta d'en Xavi: Bon dia!

Aquí deies que adjuntaves un document, però no hi havia document adjunt...

Gràcies,
