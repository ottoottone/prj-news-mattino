---
layout: page
title: Temi
permalink: /temi/
---

<p class="eyebrow">Naviga per argomento</p>
<h1>Le lenti del briefing.</h1>
<div class="principles-grid">{% for theme in site.data.taxonomy.themes %}<article><span class="principle-number">{{ forloop.index | prepend: '0' }}</span><h2><a href="{{ '/categories/' | relative_url }}#{{ theme.categories.first | slugify }}">{{ theme.title }}</a></h2><p>{{ theme.categories | join: ', ' }}</p></article>{% endfor %}</div>
