// Mapa Leaflet + OpenStreetMap (sense Google). Pinta window.MAPA_PUNTS
// definit inline a layouts/elements/list.html.
(function () {
  var el = document.getElementById("mapa");
  var punts = window.MAPA_PUNTS || [];
  if (!el || !window.L || punts.length === 0) return;

  var map = L.map(el);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
  }).addTo(map);

  var markers = [];
  punts.forEach(function (p) {
    var m = L.marker([parseFloat(p.lat), parseFloat(p.long)]).addTo(map);
    m.bindPopup('<a href="' + p.url + '">' + p.title + "</a>");
    markers.push(m);
  });

  if (markers.length === 1) {
    map.setView(markers[0].getLatLng(), 16);
  } else {
    map.fitBounds(L.featureGroup(markers).getBounds(), { padding: [30, 30] });
  }
})();
