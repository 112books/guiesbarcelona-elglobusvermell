(function () {
  var punts    = window.MAPA_PUNTS   || [];
  var pubs     = window.PUBLICACIONS  || {};
  var temes    = window.TEMES_TRANSVERSALS || [];
  var L        = window.L;

  // ══════════════════════════════════════════════════════════════════════════
  //  DADES
  // ══════════════════════════════════════════════════════════════════════════

  // Tots els elements (amb i sense coordenades): usa TOTS_ELEMENTS si el
  // template el publica (pàgines de publicació), si no, usa MAPA_PUNTS
  var totsElsElements = window.TOTS_ELEMENTS || punts.slice();

  // Elements amb coordenades vàlides (pel mapa): sempre des de MAPA_PUNTS
  // (TOTS_ELEMENTS no té lat/long, per això no s'usa aquí)
  var elementsMapa = punts.filter(function (p) {
    var lat = parseFloat(p.lat);
    var lng = parseFloat(p.long);
    return isFinite(lat) && isFinite(lng) && !(lat === 0 && lng === 0);
  });

  // ══════════════════════════════════════════════════════════════════════════
  //  SECCIÓ 1: MAPA + FILTRES DE MAPA
  // ══════════════════════════════════════════════════════════════════════════

  var mapaEl     = document.getElementById("mapa");
  var filtreMapa = document.getElementById("mapa-filtres");

  // Estat dels filtres de mapa
  var filtresMapa = {
    pub: {},
    tema: {}
  };
  Object.keys(pubs).forEach(function (s) { filtresMapa.pub[s] = true; });
  // Temes: comencen tots a false (cap filtre aplicat). Activar-ne un mostra
  // únicament els elements d'aquell tema.
  temes.forEach(function (t) { filtresMapa.tema[t.slug] = false; });

  if (mapaEl && L && elementsMapa.length > 0) {

    // ── Tema visual ──────────────────────────────────────────────────────
    var tema = (new URLSearchParams(window.location.search).get('tema') || 'a').toLowerCase();
    var contenidor = document.getElementById('mapa-contenidor');
    if (contenidor) contenidor.classList.add('tema-' + tema);
    document.documentElement.classList.add('tema-' + tema);

    document.querySelectorAll('.proposta-btn').forEach(function (btn) {
      if (btn.getAttribute('data-tema') === tema) btn.classList.add('actiu');
    });

    // ── Tile layers ──────────────────────────────────────────────────────
    var CARTO_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>';
    var tiles = {
      a: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
      b: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
      c: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png'
    };

    var map = L.map(mapaEl, { scrollWheelZoom: false });
    L.tileLayer(tiles[tema] || tiles.a, {
      attribution: CARTO_ATTR,
      maxZoom: 19,
      subdomains: 'abcd'
    }).addTo(map);

    // ── Marcadors ────────────────────────────────────────────────────────
    function markerOpts(color) {
      if (tema === 'b') return { radius: 8, fillColor: color, color: color, weight: 0, opacity: 0, fillOpacity: 0.92 };
      if (tema === 'c') return { radius: 10, fillColor: color, color: '#fff', weight: 2.5, opacity: 1, fillOpacity: 0.9 };
      return { radius: 7, fillColor: color, color: '#fff', weight: 1.5, opacity: 1, fillOpacity: 0.85 };
    }

    function colorPub(slug) {
      return (pubs[slug] && pubs[slug].color) ? pubs[slug].color : '#888';
    }
    function primerColor(publicacions) {
      return (publicacions && publicacions.length) ? colorPub(publicacions[0]) : '#888';
    }

    var allMarkers = [];
    elementsMapa.forEach(function (p) {
      var lat = parseFloat(p.lat);
      var lng = parseFloat(p.long);
      var color = primerColor(p.publicacions);
      var m = L.circleMarker([lat, lng], markerOpts(color));
      m.bindPopup('<a href="' + p.url + '">' + p.title + '</a>');
      m._dades = p;
      m.on('popupopen', function () {
        if (window.goatcounter && window.goatcounter.count) {
          window.goatcounter.count({ path: 'mapa-click' + p.url, title: p.title });
        }
      });
      allMarkers.push(m);
    });

    // ── Zoom inicial ─────────────────────────────────────────────────────
    var group = L.featureGroup(allMarkers).addTo(map);

    // Staticrypt carrega el CSS asíncronament: el contenidor pot tenir
    // amplada 0 fins que el CSS s'aplica. Esperem que tingui una amplada
    // real (> 200px) abans de fer fitBounds, per evitar tiles parcials.
    function fitMap() {
      map.invalidateSize();
      if (allMarkers.length === 1) {
        map.setView(allMarkers[0].getLatLng(), 16);
      } else if (allMarkers.length > 1) {
        map.fitBounds(group.getBounds(), { padding: [30, 30] });
      }
    }
    function fitWhenReady(attempt) {
      if (attempt > 20) { fitMap(); return; } // màxim 4s, llavors forcem
      if (mapaEl.offsetWidth > 200) {
        fitMap();
      } else {
        setTimeout(function () { fitWhenReady(attempt + 1); }, 200);
      }
    }
    fitWhenReady(0);

    // ── Filtrar mapa ─────────────────────────────────────────────────────
    function filtraMapa() {
      var hiHaPubs = Object.values(filtresMapa.pub).some(Boolean);
      var hiHaTemes = temes.some(function (t) { return filtresMapa.tema[t.slug]; });

      allMarkers.forEach(function (m) {
        var p = m._dades;
        var visible = true;

        // Filtre per publicació
        if (hiHaPubs) {
          if (!p.publicacions || !p.publicacions.length) {
            visible = false;
          } else {
            visible = p.publicacions.some(function (pub) { return filtresMapa.pub[pub]; });
          }
        }

        // Filtre per tema transversal
        if (visible && hiHaTemes) {
          if (!p.temes_transversals || !p.temes_transversals.length) {
            visible = false;
          } else {
            visible = p.temes_transversals.some(function (t) { return filtresMapa.tema[t]; });
          }
        }

        if (visible) {
          m.setStyle({ opacity: 1, fillOpacity: tema === 'b' ? 0.92 : (tema === 'c' ? 0.9 : 0.85) });
        } else {
          m.setStyle({ opacity: 0.15, fillOpacity: 0.15 });
        }
      });

      // Actualitzar estat dels botons
      filtreMapa.querySelectorAll('[data-pub]').forEach(function (btn) {
        var slug = btn.getAttribute('data-pub');
        btn.classList.toggle('actiu', !!filtresMapa.pub[slug]);
        btn.style.opacity = filtresMapa.pub[slug] ? '1' : '0.4';
      });
      var hiHaAlgunTemaActiu = temes.some(function (t) { return filtresMapa.tema[t.slug]; });
      filtreMapa.querySelectorAll('[data-tema]').forEach(function (btn) {
        var slug = btn.getAttribute('data-tema');
        var actiu = !!filtresMapa.tema[slug];
        btn.classList.toggle('actiu', actiu);
        // Si cap tema actiu: tots al 100% (no hi ha filtre). Si n'hi ha: inactius esvaïts.
        btn.style.opacity = (!hiHaAlgunTemaActiu || actiu) ? '1' : '0.4';
      });
      var totsBtn = filtreMapa.querySelector('.filtre-tots');
      if (totsBtn) {
        var totActiu = Object.values(filtresMapa.pub).every(Boolean);
        totsBtn.classList.toggle('actiu', totActiu);
        totsBtn.style.opacity = totActiu ? '1' : '0.4';
      }
    }

    // ── Construir filtres de mapa ────────────────────────────────────────
    if (filtreMapa) {
      // Publicacions
      var pubsGrup = document.createElement('div');
      pubsGrup.className = 'filtre-grup';
      var pubsLabel = document.createElement('label');
      pubsLabel.className = 'filtre-grup-label';
      pubsLabel.textContent = 'Publicacions';
      pubsGrup.appendChild(pubsLabel);
      var pubsBtns = document.createElement('div');
      pubsBtns.className = 'filtre-botos';

      var btnTots = document.createElement('button');
      btnTots.innerHTML = 'Tots <span class="filtre-btn-count">(' + totsElsElements.length + ')</span>';
      btnTots.className = 'filtre-btn filtre-tots actiu';
      btnTots.addEventListener('click', function () {
        var nouEstat = !Object.values(filtresMapa.pub).every(Boolean);
        Object.keys(filtresMapa.pub).forEach(function (s) { filtresMapa.pub[s] = nouEstat; });
        filtraMapa();
      });
      pubsBtns.appendChild(btnTots);

      // Precomputar nombre d'elements per publicació
      var comptesPerPub = {};
      elementsMapa.forEach(function (p) {
        (p.publicacions || []).forEach(function (s) {
          comptesPerPub[s] = (comptesPerPub[s] || 0) + 1;
        });
      });

      Object.keys(pubs).forEach(function (slug) {
        var btn = document.createElement('button');
        btn.setAttribute('data-pub', slug);
        btn.className = 'filtre-btn actiu';
        btn.style.setProperty('--pub-color', pubs[slug].color || '#888');
        var n = comptesPerPub[slug] || 0;
        btn.innerHTML = (pubs[slug].titol || slug) +
          (n ? ' <span class="filtre-btn-count">(' + n + ')</span>' : '');
        btn.addEventListener('click', function () {
          filtresMapa.pub[slug] = !filtresMapa.pub[slug];
          filtraMapa();
          if (window.goatcounter && window.goatcounter.count) {
            window.goatcounter.count({ path: 'mapa-filtre-pub/' + slug, title: 'Filtre pub: ' + slug });
          }
        });
        pubsBtns.appendChild(btn);
      });
      pubsGrup.appendChild(pubsBtns);
      filtreMapa.appendChild(pubsGrup);

      // Temes transversals
      if (temes.length > 0) {
        var temesGrup = document.createElement('div');
        temesGrup.className = 'filtre-grup';
        var temesLabel = document.createElement('label');
        temesLabel.className = 'filtre-grup-label';
        temesLabel.textContent = 'Temes transversals';
        temesGrup.appendChild(temesLabel);
        var temesBtns = document.createElement('div');
        temesBtns.className = 'filtre-botos';
        temes.forEach(function (t) {
          var btn = document.createElement('button');
          btn.setAttribute('data-tema', t.slug);
          btn.className = 'filtre-btn';
          btn.style.setProperty('--pub-color', t.color || '#888');
          btn.textContent = t.titol || t.slug;
          btn.addEventListener('click', function () {
            filtresMapa.tema[t.slug] = !filtresMapa.tema[t.slug];
            filtraMapa();
            if (window.goatcounter && window.goatcounter.count) {
              window.goatcounter.count({ path: 'mapa-filtre-tema/' + t.slug, title: 'Filtre tema: ' + t.slug });
            }
          });
          temesBtns.appendChild(btn);
        });
        temesGrup.appendChild(temesBtns);
        filtreMapa.appendChild(temesGrup);
      }
    }

    // ── Pre-filtre per URL: ?pub=slug (des de les fitxes al mapa) ─────────
    var urlPub = new URLSearchParams(window.location.search).get('pub');
    if (urlPub && filtresMapa.pub.hasOwnProperty(urlPub)) {
      Object.keys(filtresMapa.pub).forEach(function (s) { filtresMapa.pub[s] = false; });
      filtresMapa.pub[urlPub] = true;
      filtraMapa();
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  //  SECCIÓ 2: FILTRES DE CERCA + LLISTAT ALFABÈTIC
  // ══════════════════════════════════════════════════════════════════════════

  var cercaFiltres = document.getElementById("cerca-filtres");
  var llistatIndex = document.getElementById("llistat-index");
  var llistatGrups = document.getElementById("llistat-grups");

  // Estat dels filtres de cerca
  var grupPer = window.LLISTAT_GRUP || 'lletra'; // 'lletra' o 'any'

  var filtresCerca = {
    texte: '',
    decada: '',
    arquitecte: ''
  };

  // Recollir dades úniques per als selectors
  var decadesSet = {};
  var arquitectesSet = {};
  totsElsElements.forEach(function (p) {
    if (p.any) {
      var any = parseInt(p.any);
      if (!isNaN(any)) {
        var decada = Math.floor(any / 10) * 10;
        decadesSet[decada] = true;
      }
    }
    if (p.arquitectes && p.arquitectes.length) {
      p.arquitectes.forEach(function (a) { arquitectesSet[a] = true; });
    }
  });
  var decades = Object.keys(decadesSet).sort();
  var arquitectes = Object.keys(arquitectesSet).sort();

  // ── Construir filtres de cerca ─────────────────────────────────────────
  if (cercaFiltres) {
    var controls = document.createElement('div');
    controls.className = 'filtre-controls';

    // Cerca
    var cercaGrup = document.createElement('div');
    cercaGrup.className = 'filtre-grup';
    var cercaLabel = document.createElement('label');
    cercaLabel.className = 'filtre-grup-label';
    cercaLabel.textContent = 'Cerca';
    cercaGrup.appendChild(cercaLabel);
    var cercaInput = document.createElement('input');
    cercaInput.type = 'text';
    cercaInput.placeholder = "Nom d'element...";
    cercaInput.className = 'filtre-input';
    cercaInput.addEventListener('input', function () {
      filtresCerca.texte = this.value.toLowerCase();
      filtraLlistat();
    });
    cercaGrup.appendChild(cercaInput);
    controls.appendChild(cercaGrup);

    // Època
    if (decades.length > 0) {
      var decadaGrup = document.createElement('div');
      decadaGrup.className = 'filtre-grup';
      var decadaLabel = document.createElement('label');
      decadaLabel.className = 'filtre-grup-label';
      decadaLabel.textContent = 'Època';
      decadaGrup.appendChild(decadaLabel);
      var decadaSelect = document.createElement('select');
      decadaSelect.className = 'filtre-select';
      var optTotes = document.createElement('option');
      optTotes.value = '';
      optTotes.textContent = 'Totes';
      decadaSelect.appendChild(optTotes);
      decades.forEach(function (d) {
        var opt = document.createElement('option');
        opt.value = d;
        opt.textContent = d + 's';
        decadaSelect.appendChild(opt);
      });
      decadaSelect.addEventListener('change', function () {
        filtresCerca.decada = this.value;
        filtraLlistat();
      });
      decadaGrup.appendChild(decadaSelect);
      controls.appendChild(decadaGrup);
    }

    // Arquitecte
    if (arquitectes.length > 0) {
      var arqGrup = document.createElement('div');
      arqGrup.className = 'filtre-grup';
      var arqLabel = document.createElement('label');
      arqLabel.className = 'filtre-grup-label';
      arqLabel.textContent = 'Arquitecte';
      arqGrup.appendChild(arqLabel);
      var arqSelect = document.createElement('select');
      arqSelect.className = 'filtre-select';
      var optTots = document.createElement('option');
      optTots.value = '';
      optTots.textContent = 'Tots';
      arqSelect.appendChild(optTots);
      arquitectes.forEach(function (a) {
        var opt = document.createElement('option');
        opt.value = a;
        opt.textContent = a;
        arqSelect.appendChild(opt);
      });
      arqSelect.addEventListener('change', function () {
        filtresCerca.arquitecte = this.value;
        filtraLlistat();
      });
      arqGrup.appendChild(arqSelect);
      controls.appendChild(arqGrup);
    }

    cercaFiltres.appendChild(controls);
  }

  // ── Construir llistat (alfabètic o per any) ───────────────────────────
  function construeixLlistat() {
    if (!llistatGrups) return;

    var grups = {};
    var ordreClaus = [];

    if (grupPer === 'any') {
      // Agrupar per any, ordenat cronològicament
      totsElsElements.forEach(function (p) {
        var clau = p.any ? String(p.any) : '(sense any)';
        if (!grups[clau]) { grups[clau] = []; ordreClaus.push(clau); }
        grups[clau].push(p);
      });
      ordreClaus.sort(function (a, b) {
        var na = parseInt(a), nb = parseInt(b);
        if (isNaN(na) && isNaN(nb)) return 0;
        if (isNaN(na)) return 1;
        if (isNaN(nb)) return -1;
        return na - nb;
      });
    } else {
      // Agrupar per primera lletra
      totsElsElements.forEach(function (p) {
        var clau = p.title.charAt(0).toUpperCase();
        if (!/^[A-Z]$/.test(clau)) clau = '#';
        if (!grups[clau]) { grups[clau] = []; ordreClaus.push(clau); }
        grups[clau].push(p);
      });
      ordreClaus.sort();
    }

    // Index de lletres (sols en mode alfabètic)
    if (llistatIndex) {
      llistatIndex.innerHTML = '';
      if (grupPer !== 'any') {
        ordreClaus.forEach(function (clau) {
          if (clau === '#') return;
          var link = document.createElement('a');
          link.href = '#grup-' + clau;
          link.className = 'llistat-lletra';
          link.setAttribute('data-lletra', clau);
          link.innerHTML = clau + '<span class="llistat-lletra-count">' + grups[clau].length + '</span>';
          llistatIndex.appendChild(link);
        });
      }
    }

    // Grups
    llistatGrups.innerHTML = '';
    ordreClaus.forEach(function (clau) {
      var elements = grups[clau];

      var grup = document.createElement('div');
      grup.className = 'llistat-grup';
      grup.id = 'grup-' + clau;

      var capsalera = document.createElement('button');
      capsalera.className = 'llistat-grup-capsalera';
      capsalera.setAttribute('aria-expanded', 'false');

      if (grupPer === 'any') {
        capsalera.innerHTML =
          '<span class="llistat-grup-any">' + clau + '</span>' +
          '<span class="llistat-grup-count">' + elements.length + ' element' + (elements.length !== 1 ? 's' : '') + '</span>' +
          '<svg class="llistat-grup-fletxa" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>';
      } else {
        capsalera.innerHTML =
          '<span class="llistat-grup-lletra">' + clau + '</span>' +
          '<span class="llistat-grup-count">' + elements.length + ' elements</span>' +
          '<svg class="llistat-grup-fletxa" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>';
      }

      capsalera.addEventListener('click', function () {
        var expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', !expanded);
        grup.classList.toggle('obert', !expanded);
      });
      grup.appendChild(capsalera);

      var llista = document.createElement('ul');
      llista.className = 'llistat-grup-elements';
      llista.setAttribute('role', 'list');

      elements.forEach(function (p) {
        var li = document.createElement('li');
        li.className = 'llistat-element';
        li.setAttribute('data-title', p.title.toLowerCase());
        li.setAttribute('data-any', p.any || '');
        li.setAttribute('data-arquitectes', (p.arquitectes || []).join(','));

        var pubsHtml = '';
        if (grupPer !== 'any' && p.publicacions && p.publicacions.length) {
          pubsHtml = '<span class="llistat-element-pubs">' +
            p.publicacions.map(function (slug) {
              var c = (pubs[slug] && pubs[slug].color) ? pubs[slug].color : '#888';
              return '<span class="llistat-element-pub" style="background:' + c + '"></span>';
            }).join('') + '</span>';
        }

        var adrecaHtml = p.adreca ? '<span class="llistat-element-adreca">' + p.adreca + '</span>' : '';
        var anyHtml = (grupPer !== 'any' && p.any) ? '<span class="llistat-element-any">' + p.any + '</span>' : '';

        li.innerHTML =
          '<a href="' + p.url + '" class="llistat-element-link">' +
            '<span class="llistat-element-titol">' + p.title + '</span>' +
            '<span class="llistat-element-meta">' + adrecaHtml + anyHtml + '</span>' +
          '</a>' +
          pubsHtml;

        llista.appendChild(li);
      });

      grup.appendChild(llista);
      llistatGrups.appendChild(grup);
    });
  }

  // ── Filtrar llistat ────────────────────────────────────────────────────
  function filtraLlistat() {
    var elements = llistatGrups.querySelectorAll('.llistat-element');
    var grupsVisibles = {};

    elements.forEach(function (li) {
      var title = li.getAttribute('data-title') || '';
      var any = li.getAttribute('data-any') || '';
      var arquitectes = li.getAttribute('data-arquitectes') || '';
      var visible = true;

      // Cerca per text
      if (filtresCerca.texte && title.indexOf(filtresCerca.texte) === -1) {
        visible = false;
      }

      // Època
      if (visible && filtresCerca.decada && any) {
        var anyNum = parseInt(any);
        if (!isNaN(anyNum)) {
          var decada = Math.floor(anyNum / 10) * 10;
          if (String(decada) !== filtresCerca.decada) visible = false;
        } else {
          visible = false;
        }
      } else if (visible && filtresCerca.decada && !any) {
        visible = false;
      }

      // Arquitecte
      if (visible && filtresCerca.arquitecte) {
        if (arquitectes.indexOf(filtresCerca.arquitecte) === -1) {
          visible = false;
        }
      }

      li.style.display = visible ? '' : 'none';

      // Recollir grups visibles
      if (visible) {
        var grup = li.closest('.llistat-grup');
        if (grup) grupsVisibles[grup.id] = true;
      }
    });

    // Amagar grups sense elements visibles
    llistatGrups.querySelectorAll('.llistat-grup').forEach(function (grup) {
      var téVisibles = grup.querySelector('.llistat-element:not([style*="display: none"])');
      grup.style.display = téVisibles ? '' : 'none';
    });

    // Actualitzar comptadors de l'índex
    if (llistatIndex) {
      llistatIndex.querySelectorAll('.llistat-lletra').forEach(function (link) {
        var lletra = link.getAttribute('data-lletra');
        var grupId = 'lletra-' + lletra;
        link.style.opacity = grupsVisibles[grupId] ? '1' : '0.3';
      });
    }
  }

  // ── Acordió de la descripció de publicació ──────────────────────────────
  // Converteix els <h2> del .publicacio-descripcio en seccions plegables.
  // Funciona només a les pàgines de publicació (grupPer === 'any').
  function construeixDescripcioAccordio() {
    var desc = document.querySelector('.publicacio-descripcio');
    if (!desc) return;
    var h2s = Array.from(desc.querySelectorAll('h2'));
    if (h2s.length === 0) return;

    h2s.forEach(function (h2) {
      var grup = document.createElement('div');
      grup.className = 'llistat-grup';

      var btn = document.createElement('button');
      btn.className = 'llistat-grup-capsalera';
      btn.setAttribute('aria-expanded', 'false');
      btn.innerHTML =
        '<span class="llistat-grup-any">' + h2.textContent.trim() + '</span>' +
        '<svg class="llistat-grup-fletxa" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>';

      var cos = document.createElement('div');
      cos.className = 'llistat-grup-elements';
      cos.style.padding = '0 0 0.5rem';

      // Mou tots els nodes fins al proper h2 dins de cos
      var next = h2.nextSibling;
      while (next && !(next.nodeType === 1 && next.tagName === 'H2')) {
        var toMove = next;
        next = next.nextSibling;
        cos.appendChild(toMove);
      }

      btn.addEventListener('click', function () {
        var expanded = this.getAttribute('aria-expanded') === 'true';
        this.setAttribute('aria-expanded', String(!expanded));
        grup.classList.toggle('obert', !expanded);
      });

      grup.appendChild(btn);
      grup.appendChild(cos);
      h2.parentNode.replaceChild(grup, h2);
    });
  }

  // ── Inicialitzar ────────────────────────────────────────────────────────
  construeixLlistat();
  if (grupPer === 'any') {
    construeixDescripcioAccordio();
    // La primera secció de la descripció es mostra expandida per defecte
    var primerGrupDesc = document.querySelector('.publicacio-descripcio .llistat-grup');
    if (primerGrupDesc) {
      primerGrupDesc.querySelector('.llistat-grup-capsalera').setAttribute('aria-expanded', 'true');
      primerGrupDesc.classList.add('obert');
    }
  }
})();
