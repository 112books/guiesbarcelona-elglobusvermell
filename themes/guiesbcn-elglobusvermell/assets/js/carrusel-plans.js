// Carrusel de portades de plànols-guia (reutilitzable: «En paper» i portada).
// Fletxes, arrossegar amb el cursor i, opcionalment, bucle infinit.
(function () {
  var track = document.querySelector('[data-carroussel]');
  if (!track) return;
  var infinite = track.getAttribute('data-infinite') !== 'false';

  // Fletxes: avancen una portada (amplada real de la targeta + separació).
  var prevBtn = document.querySelector('[data-carroussel-prev]');
  var nextBtn = document.querySelector('[data-carroussel-next]');
  function passa(dir) {
    var it = track.querySelector('.en-paper-carroussel-item');
    var gap = parseFloat(getComputedStyle(track).columnGap) || 16;
    var w = it ? it.getBoundingClientRect().width + gap : track.clientWidth * 0.8;
    track.scrollBy({ left: dir * Math.round(w), behavior: 'smooth' });
  }
  if (prevBtn) prevBtn.addEventListener('click', function () { passa(-1); });
  if (nextBtn) nextBtn.addEventListener('click', function () { passa(1); });

  // Arrossegar amb el cursor a escriptori.
  var arrossegant = false, iniciX = 0, iniciScroll = 0, mogut = false;
  track.addEventListener('pointerdown', function (e) {
    if (e.pointerType === 'touch') return;
    arrossegant = true; mogut = false; iniciX = e.clientX; iniciScroll = track.scrollLeft;
    track.classList.add('is-arrossegant');
  });
  track.addEventListener('pointermove', function (e) {
    if (!arrossegant) return;
    var dx = e.clientX - iniciX;
    // Captura el punter només quan ja és un arrossegament: si es captura al
    // pointerdown, el clic va al track i no a la portada (bug 21/10).
    if (!mogut && Math.abs(dx) > 4) {
      mogut = true;
      if (track.setPointerCapture) track.setPointerCapture(e.pointerId);
    }
    if (mogut) track.scrollLeft = iniciScroll - dx;
  });
  function fiArrossegament(e) {
    arrossegant = false; track.classList.remove('is-arrossegant');
    if (e && track.hasPointerCapture && track.hasPointerCapture(e.pointerId)) track.releasePointerCapture(e.pointerId);
  }
  track.addEventListener('pointerup', fiArrossegament);
  track.addEventListener('pointercancel', fiArrossegament);
  track.addEventListener('pointerleave', fiArrossegament);
  track.addEventListener('click', function (e) { if (mogut) { e.preventDefault(); e.stopPropagation(); mogut = false; } }, true);

  if (!infinite) return;
  var originals = Array.prototype.slice.call(track.children);
  if (originals.length <= 1) return;
  // EP3 — bucle infinit: tres còpies i salt en arribar a un extrem.
  originals.forEach(function (it) { var c = it.cloneNode(true); c.setAttribute('aria-hidden', 'true'); c.setAttribute('tabindex', '-1'); track.appendChild(c); });
  originals.slice().reverse().forEach(function (it) { var c = it.cloneNode(true); c.setAttribute('aria-hidden', 'true'); c.setAttribute('tabindex', '-1'); track.insertBefore(c, track.firstChild); });
  var ajustant = false;
  function situaInici() { track.scrollLeft = track.scrollWidth / 3; }
  function embolica() {
    if (ajustant) return;
    var setW = track.scrollWidth / 3;
    if (setW <= 0) return;
    if (track.scrollLeft < setW * 0.5 || track.scrollLeft > setW * 1.5) {
      ajustant = true;
      track.style.scrollSnapType = 'none';
      track.scrollLeft = track.scrollLeft < setW * 0.5 ? track.scrollLeft + setW : track.scrollLeft - setW;
      requestAnimationFrame(function () { track.style.scrollSnapType = ''; ajustant = false; });
    }
  }
  track.addEventListener('scroll', embolica, { passive: true });
  requestAnimationFrame(situaInici);
}());
