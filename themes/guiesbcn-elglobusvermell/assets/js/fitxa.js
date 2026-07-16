(function () {
  var el   = document.getElementById("fitxa-mapa");
  var punt = window.FITXA_PUNT;
  if (!el || !punt || !window.L) return;

  var map = L.map(el, { zoomControl: true, scrollWheelZoom: false });
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
  }).addTo(map);

  var latlng = [parseFloat(punt.lat), parseFloat(punt.long)];
  L.marker(latlng).addTo(map).bindPopup(punt.title).openPopup();
  map.setView(latlng, 17);
})();
