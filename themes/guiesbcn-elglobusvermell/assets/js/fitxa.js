(function () {
  var el   = document.getElementById("fitxa-mapa");
  var punt = window.FITXA_PUNT;
  if (!el || !punt || !window.L) return;

  var map = L.map(el, { zoomControl: true, scrollWheelZoom: false, gestureHandling: true });

  // Mateix tile CartoDB Light que el mapa principal (tema 'a')
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
    maxZoom: 19,
    subdomains: 'abcd'
  }).addTo(map);

  var latlng = [parseFloat(punt.lat), parseFloat(punt.long)];
  var color  = punt.color || '#888';

  // Cercle de color de publicació, igual que als marcadors del mapa principal
  L.circleMarker(latlng, {
    radius: 9,
    fillColor: color,
    color: '#fff',
    weight: 2,
    opacity: 1,
    fillOpacity: 0.9
  }).addTo(map).bindPopup(punt.title).openPopup();

  // Una sola crida setView per evitar tiles parcials
  setTimeout(function () {
    map.invalidateSize();
    map.setView(latlng, 17);
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
  var current = 0;

  function render() {
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    dots.forEach(function (dot, i) {
      dot.classList.toggle('is-active', i === current);
    });
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
