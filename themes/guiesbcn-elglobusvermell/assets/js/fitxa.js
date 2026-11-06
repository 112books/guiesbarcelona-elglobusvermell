// Si s'arriba des d'un mapa concret (?color=), la fitxa adopta la identitat
// visual d'aquell mapa en lloc del primer de la llista de publicacions.
(function () {
  var hex = new URLSearchParams(location.search).get('color');
  if (hex && /^[0-9a-fA-F]{3,8}$/.test(hex)) {
    var fitxa = document.querySelector('.fitxa');
    if (fitxa) fitxa.style.setProperty('--pub-color', '#' + hex);
  }
})();

(function () {
  var el   = document.getElementById("fitxa-mapa");
  var punt = window.FITXA_PUNT;
  if (!el || !punt || !window.L) return;

  var map = L.map(el, { zoomControl: true, scrollWheelZoom: false, gestureHandling: true });

  // Mateix tile Stadia Alidade Smooth que el mapa principal (tema 'a')
  L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
    maxZoom: 20
  }).addTo(map);

  var latlng = [parseFloat(punt.lat), parseFloat(punt.long)];
  var color  = punt.color || '#888';
  var pubs   = window.PUBLICACIONS || {};

  // Color del marcador segons la primera publicació (igual que al mapa general).
  function colorDe(p) {
    var pr = p.publicacions || [];
    for (var i = 0; i < pr.length; i++) {
      if (pubs[pr[i]] && pubs[pr[i]].color) return pubs[pr[i]].color;
    }
    return '#888';
  }

  // Tots els punts del mapa amb coordenades; el de la fitxa es destaca i porta
  // el nom sempre visible (Xavi, 6/11: la fitxa també ha de servir per navegar).
  var punts = (window.MAPA_PUNTS || []).filter(function (p) {
    var la = parseFloat(p.lat), lo = parseFloat(p.long);
    return isFinite(la) && isFinite(lo) && !(la === 0 && lo === 0);
  });

  punts.forEach(function (p) {
    var ll = [parseFloat(p.lat), parseFloat(p.long)];
    var esActual = Math.abs(ll[0] - latlng[0]) < 1e-7 && Math.abs(ll[1] - latlng[1]) < 1e-7;
    var m = L.circleMarker(ll, {
      radius: esActual ? 11 : 5,
      fillColor: esActual ? color : colorDe(p),
      color: '#fff',
      weight: esActual ? 3 : 1.5,
      opacity: esActual ? 1 : 0.9,
      fillOpacity: esActual ? 0.95 : 0.8
    }).addTo(map);

    if (esActual) {
      // El nom, sempre a la vista, com el tooltip del ratolí.
      m.bindTooltip(punt.title, {
        permanent: true, direction: 'top', offset: [0, -12], className: 'fitxa-mapa-etiqueta'
      });
    } else {
      m.bindTooltip(p.title, { direction: 'top', offset: [0, -8] });
      m.on('click', function () { if (p.url) window.location.href = p.url; });
    }
  });

  // Una sola crida setView per evitar tiles parcials. Zoom 16 (una mica més
  // obert que el 17 d'abans) perquè es vegin els punts propers.
  setTimeout(function () {
    map.invalidateSize();
    map.setView(latlng, 16);
  }, 300);
})();

// ── Carrusel de fotos (portada + addicionals) ──────────────────────────────
// Desplaçament amb transform (no amb scroll natiu del contenidor) perquè
// funcioni de manera fiable amb els botons i amb el gest de lliscar al mòbil.
(function () {
  var carrusel = document.querySelector('[data-fitxa-carrusel]');
  if (!carrusel) return;

  var track = carrusel.querySelector('[data-carrusel-track]');
  var slideCount = track.children.length;
  var dots = carrusel.querySelectorAll('[data-carrusel-dot]');
  var prevBtn = carrusel.querySelector('[data-carrusel-prev]');
  var nextBtn = carrusel.querySelector('[data-carrusel-next]');
  var contador = document.getElementById('carrusel-contador');
  var current = 0;

  function render() {
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    dots.forEach(function (dot, i) {
      var actiu = i === current;
      dot.classList.toggle('is-active', actiu);
      dot.setAttribute('aria-pressed', actiu ? 'true' : 'false');
    });
    if (contador) {
      contador.textContent = 'Diapositiva ' + (current + 1) + ' de ' + slideCount;
    }
  }

  function goTo(index) {
    current = Math.max(0, Math.min(index, slideCount - 1));
    render();
  }

  prevBtn.addEventListener('click', function () { goTo(current - 1); });
  nextBtn.addEventListener('click', function () { goTo(current + 1); });
  dots.forEach(function (dot, i) {
    dot.addEventListener('click', function () { goTo(i); });
  });

  // Fletxes del teclat: valen amb el focus a qualsevol control del carrusel
  // (botons anterior/següent o selectors). Enter i Espai ja són natius.
  carrusel.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      goTo(current - 1);
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      goTo(current + 1);
    }
  });

  // Lliscar amb el dit (mòbil) o ratolí
  var startX = null;
  track.addEventListener('touchstart', function (e) {
    startX = e.touches[0].clientX;
  }, { passive: true });
  track.addEventListener('touchend', function (e) {
    if (startX === null) return;
    var deltaX = e.changedTouches[0].clientX - startX;
    if (Math.abs(deltaX) > 40) {
      goTo(current + (deltaX < 0 ? 1 : -1));
    }
    startX = null;
  });
})();
