(function () {
  var el      = document.getElementById("mapa");
  var filtreEl = document.getElementById("mapa-filtres");
  var punts   = window.MAPA_PUNTS   || [];
  var pubs    = window.PUBLICACIONS  || {};

  if (!el || !window.L || punts.length === 0) return;

  // ── Mapa ──────────────────────────────────────────────────────────────────
  var map = L.map(el);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
  }).addTo(map);

  // ── Color per publicació ──────────────────────────────────────────────────
  function colorPub(slug) {
    return (pubs[slug] && pubs[slug].color) ? pubs[slug].color : "#888";
  }

  function primerColor(publicacions) {
    if (!publicacions || publicacions.length === 0) return "#888";
    return colorPub(publicacions[0]);
  }

  // ── Capes per publicació ──────────────────────────────────────────────────
  var capes = {};   // slug → L.LayerGroup
  Object.keys(pubs).forEach(function (slug) {
    capes[slug] = L.layerGroup().addTo(map);
  });
  var capaResta = L.layerGroup().addTo(map); // edificis sense publicació coneguda

  // ── Marcadors ─────────────────────────────────────────────────────────────
  var allMarkers = [];
  punts.forEach(function (p) {
    var color = primerColor(p.publicacions);
    var m = L.circleMarker([parseFloat(p.lat), parseFloat(p.long)], {
      radius: 7,
      fillColor: color,
      color: "#fff",
      weight: 1.5,
      opacity: 1,
      fillOpacity: 0.85
    });
    m.bindPopup('<a href="' + p.url + '">' + p.title + "</a>");
    allMarkers.push(m);

    var capa = (p.publicacions && p.publicacions[0] && capes[p.publicacions[0]])
      ? capes[p.publicacions[0]]
      : capaResta;
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
    filtreEl.querySelectorAll("[data-pub]").forEach(function (btn) {
      var slug = btn.getAttribute("data-pub");
      btn.classList.toggle("actiu", !!actius[slug]);
      btn.style.opacity = actius[slug] ? "1" : "0.4";
    });
  }

  function togglePub(slug) {
    actius[slug] = !actius[slug];
    if (actius[slug]) {
      map.addLayer(capes[slug]);
    } else {
      map.removeLayer(capes[slug]);
    }
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

  // Botó "Tots"
  var btnTots = document.createElement("button");
  btnTots.textContent = "Tots";
  btnTots.className = "filtre-btn filtre-tots actiu";
  btnTots.addEventListener("click", function () {
    var algunActiu = Object.values(actius).some(Boolean);
    toggleTots(!algunActiu);
  });
  filtreEl.appendChild(btnTots);

  // Un botó per publicació
  Object.keys(pubs).forEach(function (slug) {
    var btn = document.createElement("button");
    btn.setAttribute("data-pub", slug);
    btn.className = "filtre-btn actiu";
    btn.style.setProperty("--pub-color", pubs[slug].color || "#888");
    btn.textContent = pubs[slug].titol || slug;
    btn.addEventListener("click", function () { togglePub(slug); });
    filtreEl.appendChild(btn);
  });

  actualitzaBotons();
})();
