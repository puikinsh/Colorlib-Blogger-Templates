# Development validation status

Version 0.1.0 · Updated November 6, 2026

These are development previews. Generated-source checks and local browser results do not establish actual Blogger compatibility or production readiness.

## Completed checks

- All twenty source directories build into self-contained theme XML, separate twelve-post demo exports, original SVG cover sets, editable post-format examples, setup/license/provenance documents and preview ZIPs with SHA256SUMS.
- The checker validates 280 XML/SVG files, 461 static review pages, forty JSON-LD source blocks with optional fields present/absent, native include references, local preview links, image attributes and unique page IDs. Four distinct standalone JavaScript blocks pass syntax checks.
- **46 tests pass, zero failures or skips**: twenty-three source checks, three builder regressions and twenty Chrome tests. Browser tests exercise home/article pages at 320, 375, 768, 1024 and 1440px: 200 viewport cases, including TOC targets, native pagination preservation, recipe markup, checklists and calculator behavior.
- Reviewed Saffron, Wayfarer, Lesson and Bench home layouts visually on desktop and in 320/375/768px panels. Checked Saffron's jump-to-recipe and checklist reset, and Ledger arithmetic through the browser UI.
- Fixed heading overflow at 320px, repeated Blogger IDs across demo exports, and a single-theme rebuild removing other themes from the gallery/checksum index. Builder tests use an isolated temporary checkout to avoid racing browser fixtures.

## November 6 design review

All twenty themes now have individual home compositions, feeds, article typography and niche reference panels. Reviewed five desktop comparison boards (1100px pages) and five phone boards (375px pages), covering every theme. The first four redesigns remain intact; sixteen further themes gained their own hierarchy, writing and original artwork. All 46 regressions pass, including topic-page membership, 200 responsive home/article cases and non-submitting calculator behavior.

Every `home.html` composition generates native and static views. Dedicated topic previews replace the previous one-category placeholder. The checker validates 461 theme review pages, with ten additional collection comparison boards available from the catalog. Print rules are appended after theme overrides to prevent dark panels obscuring printed article text. See [design directions](DESIGN-DIRECTIONS.md) for the full matrix.

## Actual Blogger validation

All twenty generated theme XML files were saved through Blogger's theme editor on the [public lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/). Each passed nine desktop and four narrow-screen checks: **180 desktop + 80 narrow views**. Four published posts and one static page supplied native pagination, labels/search, missing-image/label cases, Unicode titles, long TOCs and all twenty niche article formats. The phone checks load actual Blogger pages, including `?m=1`, at 320/375px.

Fixed platform mobile routing, empty/single-post home states, missing Open Graph type, comment-frame accessible names, long contents navigation and demo-export semantics. Public artwork loads from the approved development repository. See [the platform matrix and limitations](PLATFORM-VALIDATION.md).

Blogger refused further content imports after four posts; the owner chose to continue with existing fixtures. Consequently, all twenty complete twelve-post demo imports remain unverified. Native comment text entry works, but publish controls did not expand in this session, including under the original Contempo theme. Comment publication/replies remain unverified. Native pagination also skips posts tied at an exact timestamp when that timestamp straddles a one-post page boundary; the two-post fixture round trip passes.

## Production release gates

Complete clean imports of every packaged demo export and verify native comment publication/replies in a working session. The installed-theme view matrix is complete; retain it when changing shared behavior. Review keyboard/screen-reader behavior and measure performance on the actual demo. Complete niche-specific demo writing and editing; Saffron's original sample recipes are illustrative and have not been kitchen-tested. Check all optional integrations disabled and failing.

Public development assets are available. Prepare coherent per-theme demos, then create a versioned, checksummed release matching the installed XML. Only then add production Colorlib listings. The nine maintained existing templates retain their separate releases and download links.
