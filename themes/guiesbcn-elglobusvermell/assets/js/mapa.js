(function () {
  var el       = document.getElementById("mapa");
  var filtreEl = document.getElementById("mapa-filtres");
  var punts    = window.MAPA_PUNTS   || [];
  var pubs     = window.PUBLICACIONS  || {};

  if (!el || !window.L || punts.length === 0) return;

  // ── Tema ──────────────────────────────────────────────────────────────────
  var tema = (new URLSearchParams(window.location.search).get('tema') || 'a').toLowerCase();
  var contenidor = document.getElementById('mapa-contenidor');
  if (contenidor) contenidor.classList.add('tema-' + tema);
  document.documentElement.classList.add('tema-' + tema);

  // Marca el botó actiu al selector
  document.querySelectorAll('.proposta-btn').forEach(function (btn) {
    if (btn.getAttribute('data-tema') === tema) btn.classList.add('actiu');
  });

  // ── Tile layers ────────────────────────────────────────────────────────────
  var CARTO_ATTR = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>';
  var tiles = {
    a: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    b: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
    c: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png'
  };

  // ── Mapa ──────────────────────────────────────────────────────────────────
  var map = L.map(el, { scrollWheelZoom: false });
  L.tileLayer(tiles[tema] || tiles.a, {
    attribution: CARTO_ATTR,
    maxZoom: 19,
    subdomains: 'abcd'
  }).addTo(map);

  // ── Opcions de marcador per tema ──────────────────────────────────────────
  function markerOpts(color) {
    if (tema === 'b') {
      return { radius: 8, fillColor: color, color: color,  weight: 0,   opacity: 0,   fillOpacity: 0.92 };
    } else if (tema === 'c') {
      return { radius: 10, fillColor: color, color: '#fff', weight: 2.5, opacity: 1,   fillOpacity: 0.9  };
    } else {
      return { radius: 7,  fillColor: color, color: '#fff', weight: 1.5, opacity: 1,   fillOpacity: 0.85 };
    }
  }

  // ── Color per publicació ──────────────────────────────────────────────────
  function colorPub(slug) {
    return (pubs[slug] && pubs[slug].color) ? pubs[slug].color : '#888';
  }
  function primerColor(publicacions) {
    return (publicacions && publicacions.length) ? colorPub(publicacions[0]) : '#888';
  }

  // ── Capes per publicació ──────────────────────────────────────────────────
  var capes = {};
  Object.keys(pubs).forEach(function (slug) {
    capes[slug] = L.layerGroup().addTo(map);
  });
  var capaResta = L.layerGroup().addTo(map);

  // ── Marcadors ─────────────────────────────────────────────────────────────
  var allMarkers = [];
  punts.forEach(function (p) {
    var color = primerColor(p.publicacions);
    var opts  = markerOpts(color);
    var m     = L.circleMarker([parseFloat(p.lat), parseFloat(p.long)], opts);
    m.bindPopup('<a href="' + p.url + '">' + p.title + '</a>');
    allMarkers.push(m);
    var capa = (p.publicacions && p.publicacions[0] && capes[p.publicacions[0]])
      ? capes[p.publicacions[0]] : capaResta;
    capa.addLayer(m);
  });

  // ── Zoom inicial ──────────────────────────────────────────────────────────
  var group = L.featureGroup(allMarkers);
  if (allMarkers.length === 1) {
    map.setView(allMarkers[0].getLatLng(), 16);
  } else if (allMarkers.length > 1) {
    map.fitBounds(group.getBounds(), { padding: [30, 30] });
  }

  // ── Botons de filtre ──────────────────────────────────────────────────────
  if (!filtreEl || Object.keys(pubs).length === 0) return;

  var actius = {};
  Object.keys(pubs).forEach(function (slug) { actius[slug] = true; });

  function actualitzaBotons() {
    filtreEl.querySelectorAll('[data-pub]').forEach(function (btn) {
      var slug = btn.getAttribute('data-pub');
      btn.classList.toggle('actiu', !!actius[slug]);
      btn.style.opacity = actius[slug] ? '1' : '0.4';
    });
    var totsBtn = filtreEl.querySelector('.filtre-tots');
    if (totsBtn) {
      var algunActiu = Object.values(actius).some(Boolean);
      var totActiu   = Object.values(actius).every(Boolean);
      totsBtn.classList.toggle('actiu', totActiu);
      totsBtn.style.opacity = algunActiu ? '1' : '0.4';
    }
  }

  function togglePub(slug) {
    actius[slug] = !actius[slug];
    if (actius[slug]) { map.addLayer(capes[slug]); }
    else              { map.removeLayer(capes[slug]); }
    actualitzaBotons();
  }

  function toggleTots(activar) {
    Object.keys(pubs).forEach(function (slug) {
      actius[slug] = activar;
      if (activar) { map.addLayer(capes[slug]); }
      else         { map.removeLayer(capes[slug]); }
    });
    actualitzaBotons();
  }

  // ── Botó / ítem "Tots" ────────────────────────────────────────────────────
  var btnTots = document.createElement(tema === 'c' ? 'button' : 'button');
  btnTots.textContent = tema === 'c' ? '— Tots els edificis' : 'Tots';
  btnTots.className = tema === 'c' ? 'filtre-lateral filtre-tots actiu' : 'filtre-btn filtre-tots actiu';
  btnTots.addEventListener('click', function () {
    var algunActiu = Object.values(actius).some(Boolean);
    toggleTots(!algunActiu);
  });
  filtreEl.appendChild(btnTots);

  // ── Un botó per publicació ────────────────────────────────────────────────
  Object.keys(pubs).forEach(function (slug) {
    var btn = document.createElement('button');
    btn.setAttribute('data-pub', slug);
    if (tema === 'c') {
      btn.className = 'filtre-lateral actiu';
      btn.innerHTML = '<span class="filtre-lateral-color" style="background:' + (pubs[slug].color || '#888') + '"></span>'
                    + '<span class="filtre-lateral-titol">' + (pubs[slug].titol || slug) + '</span>';
    } else {
      btn.className = 'filtre-btn actiu';
      btn.style.setProperty('--pub-color', pubs[slug].color || '#888');
      btn.textContent = pubs[slug].titol || slug;
    }
    btn.addEventListener('click', function () { togglePub(slug); });
    filtreEl.appendChild(btn);
  });

  actualitzaBotons();
})();
