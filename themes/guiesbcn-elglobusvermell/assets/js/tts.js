(function () {
  'use strict';
  if (!('speechSynthesis' in window)) return;

  var btn = document.querySelector('.tts-btn');
  if (!btn) return;
  var sel = btn.getAttribute('data-tts-target') || 'main';
  var nodes = document.querySelectorAll(sel);
  if (!nodes.length) return;

  btn.hidden = false;

  var iconPlay = btn.querySelector('.tts-icon-play');
  var iconStop = btn.querySelector('.tts-icon-stop');
  var label    = btn.querySelector('.tts-label');
  var parlant  = false;
  var pausat   = false;

  function getText() {
    var parts = [];
    Array.prototype.forEach.call(nodes, function (n) {
      var clon = n.cloneNode(true);
      Array.prototype.forEach.call(clon.querySelectorAll('.tts-btn'), function (b) {
        if (b.parentNode) b.parentNode.removeChild(b);
      });
      var t = clon.textContent.replace(/\s+/g, ' ').trim();
      if (t) parts.push(t);
    });
    return parts.join('. ');
  }

  function atura() {
    window.speechSynthesis.cancel();
    parlant = false;
    pausat = false;
    iconPlay.hidden = false;
    iconStop.hidden = true;
    label.textContent = 'Escoltar';
    btn.setAttribute('aria-label', 'Escoltar aquesta pàgina en veu alta');
  }

  function pausa() {
    window.speechSynthesis.pause();
    pausat = true;
    iconPlay.hidden = false;
    iconStop.hidden = true;
    label.textContent = 'Continua';
    btn.setAttribute('aria-label', 'Continuar la lectura');
  }

  function continua() {
    window.speechSynthesis.resume();
    pausat = false;
    iconPlay.hidden = true;
    iconStop.hidden = false;
    label.textContent = 'Pausa';
    btn.setAttribute('aria-label', 'Pausar la lectura');
  }

  function llegeix() {
    var text = getText();
    if (!text) return;
    var utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'ca-ES';
    utterance.rate = 0.95;
    utterance.pitch = 1;
    var voices = window.speechSynthesis.getVoices();
    var veu = voices.find(function (v) { return v.lang === 'ca-ES'; })
           || voices.find(function (v) { return v.lang.indexOf('ca') === 0; })
           || voices.find(function (v) { return v.lang === 'es-ES'; })
           || null;
    if (veu) utterance.voice = veu;
    utterance.onend = atura;
    utterance.onerror = atura;
    window.speechSynthesis.speak(utterance);
    parlant = true;
    pausat = false;
    iconPlay.hidden = true;
    iconStop.hidden = false;
    label.textContent = 'Pausa';
    btn.setAttribute('aria-label', 'Pausar la lectura');
  }

  btn.addEventListener('click', function () {
    if (!parlant) { llegeix(); }
    else if (pausat) { continua(); }
    else { pausa(); }
  });

  window.addEventListener('pagehide', atura);
}());
