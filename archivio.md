---
layout: page
title: Archivio
permalink: /archivio/
---

<p class="eyebrow">Tutte le edizioni</p>
<h1>Il briefing, giorno dopo giorno.</h1>
<ul class="post-feed archive-feed">{% for issue in site.newsletter reversed %}<li class="post-feed-item"><div class="post-feed-meta"><time datetime="{{ issue.date | date_to_xmlschema }}">{{ issue.date | date: "%d.%m.%Y" }}</time></div><h2 class="post-feed-title"><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h2><p class="post-feed-excerpt">{{ issue.description }}</p></li>{% endfor %}</ul>
