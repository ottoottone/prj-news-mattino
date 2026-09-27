# Distribution research: daily email + Instagram Stories

Research date: 2026-09-27
Project: *Germania, in breve*

## Starting point

The live site already exposes a working Atom feed:

`https://ottoottone.github.io/prj-news-mattino/feed.xml`

That means a managed newsletter service can read the same published edition without a second editorial workflow. The safest source of truth is the website feed, not a manually copied email.

## Decision summary

### Newsletter recommendation: test FeedToMail first

FeedToMail advertises a hosted RSS-to-email workflow with no installation, a hosted signup page, automatic delivery, and a free tier of 500 subscribers / 1,000 emails per month / one RSS feed. It is the closest match to “set it up once and leave it alone”. The free tier would cover one daily email to roughly 33 subscribers if the full 1,000 monthly-email allowance is enforced as recipient-deliveries; confirm this before launch.

Important limitation: it is a third-party service, so verify its current terms, EU data-processing terms, sender authentication, unsubscribe handling, and whether the free plan sends the full article or a truncated feed item.

### Newsletter fallback: MailerLite

MailerLite has a polished hosted product and RSS-to-email campaigns with daily, weekly, or monthly cadence. Its current free plan advertises up to 250 active subscribers and 2,500 monthly emails. However, the pricing page does not clearly show RSS campaigns as included in the free tier; the RSS feature page advertises a 14-day premium trial. Treat MailerLite as the strongest managed fallback, not as a confirmed permanently-free RSS solution.

### Newsletter quality option: Buttondown

Buttondown supports daily/weekly/monthly RSS automation and can either send automatically or create a draft. The first 100 subscribers are free, but RSS-to-email is listed as a $9/month add-on. It is a good editorial-control option, not the requested zero-cost option.

### Services not selected

- Mailchimp: mature and hosted, but current RSS-to-email availability and free-plan eligibility are not clear enough to recommend as the first no-cost path.
- Zapier/Make: flexible, but adds a second automation layer, quotas, failure modes, and usually a paid step once the workflow grows.
- Self-hosted Mailtrain/Listmonk: potentially cheap, but violates the requirement not to install or maintain software.

## Exact newsletter workflow

1. The cronjob publishes the new Jekyll edition to GitHub Pages.
2. The service polls `/feed.xml`.
3. The service detects the new item and sends the rendered email on its daily schedule.
4. The email links back to the exact briefing page.
5. The website remains canonical; no separate copy of the briefing is edited by hand.

Before activating a public list, run one private test to confirm: Italian encoding, links, source list, SVG/brand rendering, title, no removed metadata, unsubscribe link, and whether the feed contains the complete article.

## Instagram Stories: feasibility

A fully automatic five-card Story sequence is not the same as publishing a feed carousel. Meta's official publishing documentation supports professional accounts and Story containers, but requires a Meta app, permissions, access tokens, publicly reachable image URLs, and account/Page setup. A managed scheduler may hide some of this, but it still needs the Instagram account connected and may require a paid plan.

Meta's official sharing-to-Stories flow is a user-assisted mobile share flow: the app opens Instagram's composer with an image. It is not a silent server-side autopublisher.

Therefore there are three realistic levels:

### A. Free, no-code, human-confirmed (recommended POC)

Generate five 1080×1920 JPEG cards every morning, put them in one downloadable bundle, and use a phone share flow or Meta Business Suite to publish them. The user confirms the Story sequence. This is the lowest-risk free proof of concept.

### B. Managed scheduler, semi-automatic

Use a hosted social scheduler that supports Instagram Stories on the chosen plan. It can schedule assets and notify the user to finish publishing if Instagram does not permit full automation for that account/format. This removes local installation but is unlikely to be permanently free for five daily cards.

### C. Meta API automation

Build or commission a small hosted integration that creates five Story containers and publishes them. It needs professional-account setup, Meta app review/permissions as applicable, expiring-token management, public image hosting, retries, and monitoring. This is not a zero-maintenance free service, even if Meta API calls themselves do not have a per-post fee.

## Image sources: recommended hierarchy

Use only files whose individual record clearly states CC0, Public Domain, or a compatible license. “Free to download” is not enough.

1. **Openverse** — the largest discovery layer for openly licensed images and public-domain works; filter each result by license and retain the original source record.
2. **Wikimedia Commons** — very large, multilingual collection; excellent for Germany, institutions, places, maps, historical material, and public-domain works. License obligations vary file by file.
3. **Library of Congress Free to Use and Reuse** — strong public-domain historical/archive material; mostly US-centric but useful for historical context.
4. **Europeana** — excellent European cultural-heritage discovery. Check the rights label on every item; Europeana contains mixed rights statuses.
5. **Pexels** — convenient modern stock photography, but use its own Pexels license unless the individual record explicitly says CC0. Do not assume every Pexels image is CC0.
6. **Pixabay** — convenient stock library with its own license; do not label it CC0 unless the individual record explicitly does so.
7. **Unsplash** — not CC0. It can be legally usable under its own license, but it does not satisfy a strict “CC0-only” policy.

For the strictest workflow, prefer Openverse results that resolve to Wikimedia Commons or an explicit CC0/public-domain record. Store, for every image: source URL, author, license, attribution text if required, download date, and the story topic it illustrates.

## Editorial and legal guardrails

- Do not use a generic “Germany” photo for every topic.
- Match each image to the event: Bundestag for parliamentary politics, a German city/place for local policy, a relevant institution or document for regulation, and a neutral symbolic image for sensitive news.
- Avoid identifiable private people, minors, medical situations, disasters, and political endorsement implications unless the image and context are clearly appropriate.
- CC0 removes copyright restrictions to the extent of the dedication, but does not remove personality, privacy, trademark, or defamation risks.
- Keep an internal image ledger even when attribution is not legally required.

## Recommended next step

Approve the free POC as a two-part test:

- FeedToMail private newsletter test using the live `/feed.xml`.
- Five-card Instagram Story generator using the layouts in `instagram-story-layouts.html`, with manually selected CC0/Public Domain images and user-confirmed publishing.

Only after the five-card sequence has been reviewed for readability and licensing should we investigate a managed scheduler or Meta API automation.

## Sources

- [MailerLite RSS to email](https://www.mailerlite.com/features/rss-to-email)
- [MailerLite pricing](https://www.mailerlite.com/pricing)
- [Buttondown RSS automation](https://docs.buttondown.com/rss-to-email)
- [Buttondown pricing](https://buttondown.com/pricing?plan=free)
- [FeedToMail](https://feedtomail.com/)
- [Openverse](https://openverse.org/)
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_page)
- [Library of Congress Free to Use](https://www.loc.gov/free-to-use/)
- [Pexels CC0 clarification](https://www.pexels.com/creative-commons-images/)
- [Creative Commons CC0 deed](https://creativecommons.org/publicdomain/zero/1.0/)
- [Meta Content Publishing](https://developers.facebook.com/documentation/instagram-platform/content-publishing)
- [Meta IG media / Story containers](https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media/)
- [Meta Sharing to Stories](https://developers.facebook.com/docs/instagram-platform/sharing-to-stories)
