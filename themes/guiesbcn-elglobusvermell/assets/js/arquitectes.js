(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var input = document.getElementById('cerca-arquitectes');
    var abecedari = document.querySelector('.arquitectes-abecedari');
    var senceResultats = document.getElementById('arquitectes-sense-resultats');
    var grups = document.querySelectorAll('.arquitectes-grup');

    if (!input || !grups.length) return;

    input.addEventListener('input', function () {
      var terme = input.value.trim().toLowerCase();
      var actiu = terme.length > 0;
      var totalVisible = 0;

      if (abecedari) {
        abecedari.style.display = actiu ? 'none' : '';
      }

      grups.forEach(function (grup) {
        var items = grup.querySelectorAll('li[data-nom]');
        var visiblesAlGrup = 0;

        items.forEach(function (li) {
          var nom = li.getAttribute('data-nom') || '';
          var coincideix = !actiu || nom.indexOf(terme) !== -1;
          li.hidden = !coincideix;
          if (coincideix) {
            visiblesAlGrup++;
            totalVisible++;
          }
        });

        grup.hidden = actiu && visiblesAlGrup === 0;
      });

      if (senceResultats) {
        senceResultats.hidden = totalVisible > 0 || !actiu;
      }
    });
  });
})();
