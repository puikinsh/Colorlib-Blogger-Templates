/* Progressive catalog filtering. All links and cards work without JavaScript. */
(function () {
  'use strict';
  var root = document.querySelector('[data-hub]');
  if (!root) return;
  var search = root.querySelector('[data-hub-search]');
  var filters = Array.from(root.querySelectorAll('[data-hub-filter]'));
  var cards = Array.from(root.querySelectorAll('[data-hub-card]'));
  var count = root.querySelector('[data-hub-count]');
  var empty = root.querySelector('[data-hub-empty]');
  var category = 'all';
  function update() {
    var query = search.value.trim().toLocaleLowerCase();
    var visible = 0;
    cards.forEach(function (card) {
      card.hidden = !(category === 'all' || card.getAttribute('data-category') === category) || !card.textContent.toLocaleLowerCase().includes(query);
      if (!card.hidden) visible++;
    });
    filters.forEach(function (button) { button.setAttribute('aria-pressed', String(button.getAttribute('data-hub-filter') === category)); });
    count.textContent = visible + (visible === 1 ? ' theme' : ' themes') + ' · Development previews';
    empty.hidden = visible !== 0;
  }
  filters.forEach(function (button) { button.addEventListener('click', function () { category = button.getAttribute('data-hub-filter'); update(); }); });
  search.addEventListener('input', update);
  root.querySelector('[data-hub-reset]').addEventListener('click', function () { category = 'all'; search.value = ''; update(); search.focus(); });
  root.querySelectorAll('[data-hub-controls]').forEach(function (node) { node.hidden = false; });
  update();
})();
