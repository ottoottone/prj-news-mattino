# Morning Briefing implementation queue

Queue was reprioritized after each completed improvement. Target: 25 implemented improvements.

- [x] 01. Bootstrap Nord Newsletter theme and local Jekyll build
- [x] 02. Configure the site identity in Italian
- [x] 03. Add a daily briefing homepage hierarchy
- [x] 04. Add a real Italian morning briefing issue
- [x] 05. Add editorial category taxonomy
- [x] 06. Add a visual masthead with Germany/Italy identity
- [x] 07. Add color tokens and fresh accent treatment
- [x] 08. Improve typography and reading rhythm
- [x] 09. Add a briefing metadata strip
- [x] 10. Add source links and source-card styling
- [x] 11. Add “in breve” summary blocks
- [x] 12. Add practical impact section for Italians in Germany
- [x] 13. Add archive and issue navigation in Italian
- [x] 14. Add responsive mobile navigation labels
- [x] 15. Add accessibility language and focus improvements
- [x] 16. Add Italian search suggestions and UI copy
- [x] 17. Add homepage welcome/positioning panel
- [x] 18. Add empty-state and 404 Italian copy
- [x] 19. Add favicon/manifest/site metadata
- [x] 20. Add editorial footer and contact links
- [x] 21. Add social/share labels in Italian
- [x] 22. Add a “come leggere” explainer page
- [x] 23. Add responsive visual QA at desktop and mobile widths
- [x] 24. Run build, link, HTML and accessibility checks
- [x] 25. Final polish, update README, and commit the working site

## Reprioritization notes

After the initial scaffold, visual identity and Italian editorial hierarchy moved ahead of auxiliary theme features. Verification then covered the rendered routes, search/theme controls, Italian copy, desktop/mobile widths and horizontal overflow before the final commit.

## Verification record

- `bundle exec jekyll build --trace` passed.
- 12 HTML pages generated.
- 12 local generated links checked; all returned HTTP 200.
- No horizontal overflow at 390px mobile width.
- Search overlay and theme menu inspected in the browser.
- English UI hit-list check returned no configured visible phrases.
