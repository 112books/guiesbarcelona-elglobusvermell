(function () {
  var punts    = window.MAPA_PUNTS   || [];
  var pubs     = window.PUBLICACIONS  || {};
  var temes    = window.TEMES_TRANSVERSALS || [];
  var L        = window.L;

  // ══════════════════════════════════════════════════════════════════════════
  //  DADES
  // ══════════════════════════════════════════════════════════════════════════

  // Tots els elements (amb i sense coordenades)
  var totsElsElements = punts.slice();

  // Elements amb coordenades vàlides (pel mapa)
  var elementsMapa = totsElsElements.filter(function (p) {
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
  temes.forEach(function (t) { filtresMapa.tema[t.slug] = true; });

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
      allMarkers.push(m);
    });

    // ── Zoom inicial ─────────────────────────────────────────────────────
    var group = L.featureGroup(allMarkers).addTo(map);
    if (allMarkers.length === 1) {
      map.setView(allMarkers[0].getLatLng(), 16);
    } else if (allMarkers.length > 1) {
      map.fitBounds(group.getBounds(), { padding: [30, 30] });
    }

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
      filtreMapa.querySelectorAll('[data-tema]').forEach(function (btn) {
        var slug = btn.getAttribute('data-tema');
        btn.classList.toggle('actiu', !!filtresMapa.tema[slug]);
        btn.style.opacity = filtresMapa.tema[slug] ? '1' : '0.4';
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
      btnTots.textContent = 'Tots';
      btnTots.className = 'filtre-btn filtre-tots actiu';
      btnTots.addEventListener('click', function () {
        var nouEstat = !Object.values(filtresMapa.pub).every(Boolean);
        Object.keys(filtresMapa.pub).forEach(function (s) { filtresMapa.pub[s] = nouEstat; });
        filtraMapa();
      });
      pubsBtns.appendChild(btnTots);

      Object.keys(pubs).forEach(function (slug) {
        var btn = document.createElement('button');
        btn.setAttribute('data-pub', slug);
        btn.className = 'filtre-btn actiu';
        btn.style.setProperty('--pub-color', pubs[slug].color || '#888');
        btn.textContent = pubs[slug].titol || slug;
        btn.addEventListener('click', function () {
          filtresMapa.pub[slug] = !filtresMapa.pub[slug];
          filtraMapa();
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
          btn.className = 'filtre-btn actiu';
          btn.style.setProperty('--pub-color', t.color || '#888');
          btn.textContent = t.titol || t.slug;
          btn.addEventListener('click', function () {
            filtresMapa.tema[t.slug] = !filtresMapa.tema[t.slug];
            filtraMapa();
          });
          temesBtns.appendChild(btn);
        });
        temesGrup.appendChild(temesBtns);
        filtreMapa.appendChild(temesGrup);
      }
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  //  SECCIÓ 2: FILTRES DE CERCA + LLISTAT ALFABÈTIC
  // ══════════════════════════════════════════════════════════════════════════

  var cercaFiltres = document.getElementById("cerca-filtres");
  var llistatIndex = document.getElementById("llistat-index");
  var llistatGrups = document.getElementById("llistat-grups");

  // Estat dels filtres de cerca
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

  // ── Construir llistat alfabètic ────────────────────────────────────────
  function construeixLlistat() {
    if (!llistatGrups) return;

    // Agrupar per lletra
    var grups = {};
    var ordreLletres = [];
    totsElsElements.forEach(function (p) {
      var lletra = p.title.charAt(0).toUpperCase();
      if (!/^[A-Z]$/.test(lletra)) lletra = '#';
      if (!grups[lletra]) {
        grups[lletra] = [];
        ordreLletres.push(lletra);
      }
      grups[lletra].push(p);
    });

    ordreLletres.sort();

    // Index de lletres
    if (llistatIndex) {
      llistatIndex.innerHTML = '';
      ordreLletres.forEach(function (lletra) {
        if (lletra === '#') return;
        var link = document.createElement('a');
        link.href = '#lletra-' + lletra;
        link.className = 'llistat-lletra';
        link.setAttribute('data-lletra', lletra);
        link.innerHTML = lletra + '<span class="llistat-lletra-count">' + grups[lletra].length + '</span>';
        llistatIndex.appendChild(link);
      });
    }

    // Grups
    llistatGrups.innerHTML = '';
    ordreLletres.forEach(function (lletra) {
      var elements = grups[lletra];

      var grup = document.createElement('div');
      grup.className = 'llistat-grup';
      grup.id = 'lletra-' + lletra;

      var capsalera = document.createElement('button');
      capsalera.className = 'llistat-grup-capsalera';
      capsalera.setAttribute('aria-expanded', 'false');
      capsalera.innerHTML =
        '<span class="llistat-grup-lletra">' + lletra + '</span>' +
        '<span class="llistat-grup-count">' + elements.length + ' elements</span>' +
        '<svg class="llistat-grup-fletxa" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>';
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
        if (p.publicacions && p.publicacions.length) {
          pubsHtml = '<span class="llistat-element-pubs">' +
            p.publicacions.map(function (slug) {
              var c = (pubs[slug] && pubs[slug].color) ? pubs[slug].color : '#888';
              return '<span class="llistat-element-pub" style="background:' + c + '"></span>';
            }).join('') + '</span>';
        }

        var adrecaHtml = p.adreca ? '<span class="llistat-element-adreca">' + p.adreca + '</span>' : '';
        var anyHtml = p.any ? '<span class="llistat-element-any">' + p.any + '</span>' : '';

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

  // ── Inicialitzar ────────────────────────────────────────────────────────
  construeixLlistat();
})();
