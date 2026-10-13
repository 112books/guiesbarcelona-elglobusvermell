// P3 — Mapa navegable de la portada (sense filtres; el botó duu a /mapa/).
(function () {
  var el = document.getElementById('portada-mapa-el');
  if (!el || !window.L) return;
  var map = L.map(el, { zoomControl: true, scrollWheelZoom: false, gestureHandling: true });
  L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>',
    maxZoom: 20
  }).addTo(map);
  var punts = window.MAPA_PUNTS || [];
  var pubs = window.PUBLICACIONS || {};
  var capa = L.featureGroup().addTo(map);
  var bounds = [];
  punts.forEach(function (p) {
    var lat = parseFloat(p.lat), lng = parseFloat(p.long);
    if (isNaN(lat) || isNaN(lng)) return;
    var color = '#888';
    var ps = p.publicacions || [];
    if (ps.length) { var info = pubs[ps[0]]; if (info && info.color) color = info.color; }
    var m = L.circleMarker([lat, lng], { radius: 6, fillColor: color, color: '#fff', weight: 1.5, opacity: 1, fillOpacity: 0.9 });
    if (p.url) m.bindPopup('<a href="' + p.url + '">' + (p.title || '') + '</a>');
    m.addTo(capa);
    bounds.push([lat, lng]);
  });
  if (bounds.length) map.fitBounds(bounds, { padding: [20, 20] });
  else map.setView([41.39, 2.16], 12);
  setTimeout(function () { map.invalidateSize(); }, 300);
}());
