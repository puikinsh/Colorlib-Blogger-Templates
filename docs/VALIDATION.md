# Development validation status

Version 0.1.0 · Updated November 6, 2026

These are development previews. Generated-source checks and local browser results do not establish actual Blogger compatibility or production readiness.

## Completed checks

- All twenty source directories build into self-contained theme XML, separate twelve-post demo exports, original SVG cover sets, editable post-format examples, setup/license/provenance documents and preview ZIPs with SHA256SUMS.
- The checker validates 280 XML/SVG files, 400 static review pages, forty JSON-LD source blocks with optional fields present/absent, native include references, local preview links, image attributes and unique page IDs. Four distinct standalone JavaScript blocks pass syntax checks.
- **45 tests pass, zero failures or skips**: twenty-three source checks, two builder regressions and twenty Chrome tests. Browser tests exercise home/article pages at 320, 375, 768, 1024 and 1440px: 200 viewport cases, including TOC targets, native pagination preservation, recipe markup, checklists and calculator behavior.
- Reviewed Saffron, Wayfarer, Lesson and Bench home layouts visually on desktop and in 320/375/768px panels. Checked Saffron's jump-to-recipe and checklist reset, and Ledger arithmetic through the browser UI.
- Fixed heading overflow at 320px, repeated Blogger IDs across demo exports, and a single-theme rebuild removing other themes from the gallery/checksum index. Builder tests use an isolated temporary checkout to avoid racing browser fixtures.

## November 6 design review

Launchpad, Lesson, Bench and Studio now have distinct product-journal, documentation, review and portfolio layouts. All 45 regressions pass with their new home/article styles at the five tested widths. Shared `home.html` compositions generate both native and static views; see [design directions](DESIGN-DIRECTIONS.md). Preview assets use content-based versions to prevent stale styles and artwork.

## Actual Blogger validation pending

Creating a dedicated public test blog requires the requested account owner's approval. No existing live demo has been replaced with these development themes. Theme saves, content imports, native pagination under Blogger, comments, platform mobile routing and Theme Designer changes have not been verified.

The demo exports contain posts only; owners must create/configure their own static pages and menu links. Public artwork URLs currently target a planned source repository; publish owned assets and configure `BLOGGER_ASSET_BASE` before platform testing. Local review pages use bundled images.

## Production release gates

For every theme, record a successful real import and check home, subsequent pages, label/search, empty/error, posts, static pages, images absent/present, comments and mobile routes. Review keyboard/screen-reader behavior and measure performance on the actual demo. Complete niche-specific demo writing and editing; Saffron's original sample recipes are illustrative and have not been kitchen-tested. Check all optional integrations disabled and failing.

Publish assets and coherent demos, then create a versioned, checksummed release matching the installed XML. Only then add production Colorlib listings. The nine maintained existing templates retain their separate releases and download links.
