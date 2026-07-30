(function () {
  var el   = document.getElementById("fitxa-mapa");
  var punt = window.FITXA_PUNT;
  if (!el || !punt || !window.L) return;

  var map = L.map(el, { zoomControl: true, scrollWheelZoom: false });

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
(function () {
  var carrusel = document.querySelector('[data-fitxa-carrusel]');
  if (!carrusel) return;

  var track = carrusel.querySelector('[data-carrusel-track]');
  var slides = track.children;
  var dots = carrusel.querySelectorAll('[data-carrusel-dot]');
  var prevBtn = carrusel.querySelector('[data-carrusel-prev]');
  var nextBtn = carrusel.querySelector('[data-carrusel-next]');

  function activeIndex() {
    var scrollLeft = track.scrollLeft;
    var width = track.clientWidth;
    return Math.round(scrollLeft / width);
  }

  function goTo(index) {
    var clamped = Math.max(0, Math.min(index, slides.length - 1));
    track.scrollTo({ left: clamped * track.clientWidth, behavior: 'smooth' });
  }

  function updateDots() {
    var i = activeIndex();
    dots.forEach(function (dot, di) {
      dot.classList.toggle('is-active', di === i);
    });
  }

  prevBtn.addEventListener('click', function () { goTo(activeIndex() - 1); });
  nextBtn.addEventListener('click', function () { goTo(activeIndex() + 1); });
  dots.forEach(function (dot, i) {
    dot.addEventListener('click', function () { goTo(i); });
  });

  var scrollTimeout;
  track.addEventListener('scroll', function () {
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(updateDots, 100);
  });
})();
