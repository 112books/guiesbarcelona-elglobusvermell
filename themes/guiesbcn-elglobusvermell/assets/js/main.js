// Header: contracte visual en fer scroll — logo petit + menú com a icones.
(function () {
  var header = document.querySelector(".site-header");
  if (!header) return;

  var threshold = 40;
  var ticking = false;

  function update() {
    var scrolled = window.scrollY > threshold;
    header.classList.toggle("is-scrolled", scrolled);
    document.documentElement.style.setProperty(
      '--header-actual-height',
      scrolled ? 'var(--header-height-scroll)' : 'var(--header-height)'
    );
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
