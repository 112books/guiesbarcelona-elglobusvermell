// Header: contracte visual en fer scroll — logo petit + menú com a icones.
(function () {
  var header = document.querySelector(".site-header");
  if (!header) return;

  var threshold = 40;
  var ticking = false;

  function update() {
    header.classList.toggle("is-scrolled", window.scrollY > threshold);
    ticking = false;
  }

  window.addEventListener("scroll", function () {
    if (!ticking) {
      window.requestAnimationFrame(update);
      ticking = true;
    }
  });

  update();
})();
