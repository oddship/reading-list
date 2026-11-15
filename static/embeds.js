function loadXEmbeds() {
  var cards = document.querySelectorAll('[data-x-embed]');
  if (!cards.length) return;
  cards.forEach(function(card) {
    if (card.getAttribute('data-x-loaded') === 'true') return;
    var id = card.getAttribute('data-tweet-id');
    var url = card.getAttribute('data-tweet-url');
    if (!id || !url) return;
    var blockquote = document.createElement('blockquote');
    blockquote.className = 'twitter-tweet';
    blockquote.setAttribute('data-dnt', 'true');
    blockquote.setAttribute('data-conversation', 'none');
    var link = document.createElement('a');
    link.href = url;
    link.textContent = 'View this post on X';
    blockquote.appendChild(link);
    card.insertBefore(blockquote, card.querySelector('figcaption'));
    card.setAttribute('data-x-loaded', 'true');
    card.querySelector('[data-x-placeholder]').hidden = true;
  });
  if (!document.getElementById('twitter-wjs')) {
    var script = document.createElement('script');
    script.id = 'twitter-wjs';
    script.async = true;
    script.defer = true;
    script.src = 'https://platform.x.com/widgets.js';
    script.charset = 'utf-8';
    document.body.appendChild(script);
  } else if (window.twttr && window.twttr.widgets) {
    window.twttr.widgets.load();
  }
}
function enableXEmbeds() {
  try { localStorage.setItem('x-embeds-consent', 'true'); } catch (_) {}
  loadXEmbeds();
}
document.addEventListener('DOMContentLoaded', function() {
  try {
    if (localStorage.getItem('x-embeds-consent') === 'true') loadXEmbeds();
  } catch (_) {}
  document.querySelectorAll('[data-x-consent-button]').forEach(function(button) {
    button.addEventListener('click', enableXEmbeds);
  });
});
