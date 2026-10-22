// Carrusel de portades de plànols-guia (reutilitzable: «En paper» i portada).
// Fletxes, arrossegar amb el cursor i, opcionalment, bucle infinit.
// 22/10: l'arrossegament s'ajusta al de referencia d'en Xavi (Swiper): la fila
// segueix el punter 1:1, i en deixar anar es desa suaument fins a la portada
// més propera (amb una mica d'inèrcia segons la velocitat del gest).
(function () {
  var track = document.querySelector('[data-carroussel]');
  if (!track) return;
  var infinite = track.getAttribute('data-infinite') !== 'false';

  function gapTrack() {
    return parseFloat(getComputedStyle(track).columnGap) || 16;
  }
  function items() {
    return Array.prototype.slice.call(track.querySelectorAll('.en-paper-carroussel-item'));
  }
  // Posició de cada portada dins el contingut desplaçable.
  function posicio(estira) {
    var baseX = track.getBoundingClientRect().left;
    return estira.getBoundingClientRect().left - baseX + track.scrollLeft;
  }
  // Desa fins a la portada més propera (o la de la projecció del gest).
  function ajusta(projeccio) {
    var llista = items();
    if (!llista.length) return;
    var objectiu = track.scrollLeft + (projeccio || 0);
    var millor = null, dist = Infinity;
    for (var i = 0; i < llista.length; i++) {
      var p = posicio(llista[i]);
      var d = Math.abs(p - objectiu);
      if (d < dist) { dist = d; millor = p; }
    }
    if (millor === null) return;
    track.scrollTo({ left: Math.max(0, Math.round(millor)), behavior: 'smooth' });
  }

  // Fletxes: avancen una portada (amplada real de la targeta + separació).
  var prevBtn = document.querySelector('[data-carroussel-prev]');
  var nextBtn = document.querySelector('[data-carroussel-next]');
  function passa(dir) {
    var it = items()[0];
    var w = it ? it.getBoundingClientRect().width + gapTrack() : track.clientWidth * 0.8;
    track.scrollBy({ left: dir * Math.round(w), behavior: 'smooth' });
  }
  if (prevBtn) prevBtn.addEventListener('click', function () { passa(-1); });
  if (nextBtn) nextBtn.addEventListener('click', function () { passa(1); });

  // Arrossegar amb el cursor a escriptori.
  var arrossegant = false, mogut = false, iniciX = 0, iniciScroll = 0;
  var mostres = []; // {x, t} per calcular la velocitat del gest
  track.addEventListener('pointerdown', function (e) {
    if (e.pointerType === 'touch') return; // al mòbil mana el scroll natiu
    arrossegant = true; mogut = false; iniciX = e.clientX; iniciScroll = track.scrollLeft;
    mostres = [{ x: e.clientX, t: Date.now() }];
  });
  track.addEventListener('pointermove', function (e) {
    if (!arrossegant) return;
    var dx = e.clientX - iniciX;
    // Captura el punter només quan ja és un arrossegament: si es captura al
    // pointerdown, el clic va al track i no a la portada (bug 21/10).
    if (!mogut && Math.abs(dx) > 4) {
      mogut = true;
      track.classList.add('is-arrossegant');
      // Mentre arrosseguem, el snap no ha de tibar: el fem nosaltres al final.
      track.style.scrollSnapType = 'none';
      if (track.setPointerCapture) track.setPointerCapture(e.pointerId);
    }
    if (mogut) {
      track.scrollLeft = iniciScroll - dx;
      mostres.push({ x: e.clientX, t: Date.now() });
      if (mostres.length > 6) mostres.shift();
    }
  });
  function projeccio() {
    if (mostres.length < 2) return 0;
    var a = mostres[0], b = mostres[mostres.length - 1];
    var dt = b.t - a.t;
    if (dt <= 0) return 0;
    var vel = (b.x - a.x) / dt; // px/ms
    if (Math.abs(vel) < 0.05) return 0; // gest lent: res d'inèrcia
    return Math.max(-window.innerWidth, Math.min(window.innerWidth, vel * 180));
  }
  function fiArrossegament(e) {
    if (!arrossegant) return;
    arrossegant = false;
    track.classList.remove('is-arrossegant');
    if (e && track.hasPointerCapture && track.hasPointerCapture(e.pointerId)) track.releasePointerCapture(e.pointerId);
    if (mogut) {
      track.style.scrollSnapType = '';
      ajusta(projeccio());
    }
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
