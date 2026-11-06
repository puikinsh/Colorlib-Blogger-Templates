/* Colorlib Blogger core. Native navigation is deliberately never replaced. */
(function () {
  'use strict';
  document.querySelectorAll('[data-current-year]').forEach(function (node) {
    node.textContent = String(new Date().getFullYear());
  });
  document.querySelectorAll('.cl-article').forEach(function (article) {
    var prose = article.querySelector('.cl-prose');
    var toc = article.querySelector('.cl-toc');
    if (!prose || !toc) return;
    var headings = Array.from(prose.querySelectorAll('h2,h3')).filter(function (heading) {
      return heading.textContent.trim() && !heading.closest('[data-no-toc]');
    });
    if (headings.length < 3) return;
    var title = document.createElement('strong');
    title.textContent = 'On this page';
    var list = document.createElement('ol');
    headings.forEach(function (heading, index) {
      if (!heading.id) {
        var base = 'section-' + (index + 1), candidate = base, suffix = 1;
        while (document.getElementById(candidate)) candidate = base + '-' + suffix++;
        heading.id = candidate;
      }
      var item = document.createElement('li');
      var link = document.createElement('a');
      link.href = '#' + encodeURIComponent(heading.id);
      link.textContent = heading.textContent;
      item.appendChild(link);
      list.appendChild(item);
    });
    toc.appendChild(title);
    toc.appendChild(list);
    toc.hidden = false;
  });
  document.querySelectorAll('[data-print]').forEach(function (button) {
    button.hidden = false;
    button.addEventListener('click', function () { window.print(); });
  });
  document.querySelectorAll('[data-reset-checklist]').forEach(function (button) {
    button.hidden = false;
    button.addEventListener('click', function () {
      var container = button.closest('.cl-feature-box') || button.closest('.cl-prose');
      if (container) container.querySelectorAll('input[type="checkbox"]').forEach(function (input) { input.checked = false; });
    });
  });
  document.querySelectorAll('[data-recipe]').forEach(function (recipe) {
    if (recipe.hasAttribute('data-recipe-demo')) return;
    var article = recipe.closest('.cl-article');
    var heading = recipe.querySelector('.recipe-name');
    var image = article && article.querySelector('.cl-prose img');
    var ingredients = Array.from(recipe.querySelectorAll('.recipe-ingredients label')).map(function (node) { return node.textContent.trim(); }).filter(Boolean);
    var instructions = Array.from(recipe.querySelectorAll('.recipe-instructions li')).map(function (node) { return node.textContent.trim(); }).filter(Boolean);
    if (!article || !heading || !heading.textContent.trim() || !image || !image.getAttribute('src') || !ingredients.length || !instructions.length) return;
    var src;
    try { src = new URL(image.getAttribute('src'), location.href); } catch (_) { return; }
    if (!/^https?:$/.test(src.protocol)) return;
    var schema = {
      '@context':'https://schema.org', '@type':'Recipe', name:heading.textContent.trim(),
      image:[src.href], recipeIngredient:ingredients,
      recipeInstructions:instructions.map(function (text) { return {'@type':'HowToStep', text:text}; })
    };
    var author = article.getAttribute('data-author');
    if (author) schema.author = {'@type':'Person', name:author};
    var canonical = article.getAttribute('data-canonical');
    if (canonical) schema.url = canonical;
    ['prepTime','cookTime','totalTime'].forEach(function (field) {
      var value = recipe.getAttribute('data-' + field.replace(/[A-Z]/g, function (letter) { return '-' + letter.toLowerCase(); }));
      if (value && /^P(?=\d|T\d)(?:\d+D)?(?:T(?:\d+H)?(?:\d+M)?(?:\d+S)?)?$/.test(value)) schema[field] = value;
    });
    var yieldNode = recipe.querySelector('.recipe-yield');
    if (yieldNode && yieldNode.textContent.trim()) schema.recipeYield = yieldNode.textContent.trim();
    var script = document.createElement('script');
    script.type = 'application/ld+json';
    script.setAttribute('data-recipe-schema', 'true');
    script.textContent = JSON.stringify(schema);
    recipe.appendChild(script);
  });
  document.querySelectorAll('[data-budget]').forEach(function (form) {
    var income = form.querySelector('[name="income"]');
    var expenses = form.querySelector('[name="expenses"]');
    var output = form.querySelector('output');
    if (!income || !expenses || !output) return;
    function update() {
      var a = Number(income.value), b = Number(expenses.value);
      if (!income.value || !expenses.value || !Number.isFinite(a) || !Number.isFinite(b) || a < 0 || b < 0) {
        output.textContent = 'Enter two non-negative amounts.';
        return;
      }
      output.textContent = 'Income minus expenses: ' + (a - b).toLocaleString(undefined, {minimumFractionDigits:2, maximumFractionDigits:2});
    }
    var calculate = form.querySelector('[data-budget-calculate]');
    if (calculate) calculate.addEventListener('click', update);
    form.addEventListener('input', update);
    update();
  });
  document.querySelectorAll('button[data-video-src]').forEach(function (button) {
    var player = document.createElement('div');
    player.className = 'cl-media-player';
    button.before(player);
    player.appendChild(button);
    var status = document.createElement('p');
    status.className = 'cl-small';
    status.setAttribute('role', 'status');
    player.appendChild(status);
    button.type = 'button';
    button.addEventListener('click', function () {
      var url;
      try { url = new URL(button.getAttribute('data-video-src')); } catch (_) { url = null; }
      if (!url || url.protocol !== 'https:' || url.username || url.password || (url.port && url.port !== '443') || !((url.hostname === 'www.youtube-nocookie.com' && /^\/embed\/[\w-]+$/.test(url.pathname)) || (url.hostname === 'player.vimeo.com' && /^\/video\/\d+$/.test(url.pathname)))) {
        status.textContent = 'This video link is unavailable. Ask the publisher to check its HTTPS embed URL.';
        return;
      }
      // Do not accept autoplay, tracking or provider API parameters from pasted URLs.
      var hash = url.hostname === 'player.vimeo.com' && url.searchParams.get('h');
      url.search = '';
      url.hash = '';
      if (hash && /^[a-zA-Z0-9]+$/.test(hash)) url.searchParams.set('h', hash);
      var frame = document.createElement('iframe');
      frame.src = url.href;
      frame.title = button.getAttribute('data-video-title') || 'Video player';
      frame.allowFullscreen = true;
      frame.setAttribute('allow', 'fullscreen; picture-in-picture; encrypted-media');
      frame.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
      frame.tabIndex = 0;
      var fallback = document.createElement('a');
      var videoId = url.pathname.split('/').pop();
      fallback.href = url.hostname === 'www.youtube-nocookie.com' ? 'https://www.youtube.com/watch?v=' + videoId : 'https://vimeo.com/' + videoId + (hash && /^[a-zA-Z0-9]+$/.test(hash) ? '/' + hash : '');
      fallback.target = '_blank';
      fallback.rel = 'noopener noreferrer';
      fallback.textContent = 'Open video on provider (new tab)';
      var stop = document.createElement('button');
      stop.type = 'button';
      stop.textContent = 'Stop and close video';
      var actions = document.createElement('div');
      actions.className = 'cl-actions';
      actions.appendChild(fallback);
      actions.appendChild(stop);
      button.hidden = true;
      player.appendChild(frame);
      player.appendChild(actions);
      status.textContent = 'Player requested. If playback is unavailable, open the provider link or close and retry.';
      stop.addEventListener('click', function () {
        frame.remove();
        actions.remove();
        button.hidden = false;
        status.textContent = 'Video closed. You can load it again.';
        button.focus();
      });
      frame.focus();
    });
  });
})();
