# Development validation status

Version 0.1.0 · Updated November 6, 2026

These are development previews. Generated-source checks and local browser results do not establish actual Blogger compatibility or production readiness.

## Completed checks

- All twenty source directories build into self-contained theme XML, separate twelve-post demo exports, original SVG cover sets, editable post-format examples, setup/license/provenance documents and preview ZIPs with SHA256SUMS.
- The checker validates 280 XML/SVG files, 461 static review pages, forty JSON-LD source blocks with optional fields present/absent, native include references, local preview links, image attributes and unique page IDs. Four distinct standalone JavaScript blocks pass syntax checks.
- **52 tests pass, zero failures or skips**: the original forty-six checks plus owner-contract, optional-player, hub-browser, two comment regressions and the published-release hub-link check. Browser tests exercise home/article pages at 320, 375, 768, 1024 and 1440px: 200 viewport cases, including TOC targets, native pagination preservation, recipe markup, checklists and calculator behavior.
- Reviewed Saffron, Wayfarer, Lesson and Bench home layouts visually on desktop and in 320/375/768px panels. Checked Saffron's jump-to-recipe and checklist reset, and Ledger arithmetic through the browser UI.
- Fixed heading overflow at 320px, repeated Blogger IDs across demo exports, and a single-theme rebuild removing other themes from the gallery/checksum index. Builder tests use an isolated temporary checkout to avoid racing browser fixtures.

## November 6 design review

All twenty themes now have individual home compositions, feeds, article typography and niche reference panels. Reviewed five desktop comparison boards (1100px pages) and five phone boards (375px pages), covering every theme. The first four redesigns remain intact; sixteen further themes gained their own hierarchy, writing and original artwork. All 46 regressions pass, including topic-page membership, 200 responsive home/article cases and non-submitting calculator behavior.

Every `home.html` composition generates native and static views. Dedicated topic previews replace the previous one-category placeholder. The checker validates 461 theme review pages, with ten additional collection comparison boards available from the catalog. Print rules are appended after theme overrides to prevent dark panels obscuring printed article text. See [design directions](DESIGN-DIRECTIONS.md) for the full matrix.

## Actual Blogger validation

All twenty generated theme XML files were saved through Blogger's theme editor on the [public lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/). Each passed nine desktop and four narrow-screen checks: **180 desktop + 80 narrow views**. Four published posts and one static page supplied native pagination, labels/search, missing-image/label cases, Unicode titles, long TOCs and all twenty niche article formats. The phone checks load actual Blogger pages, including `?m=1`, at 320/375px.

Fixed platform mobile routing, empty/single-post home states, missing Open Graph type, comment-frame accessible names, long contents navigation and demo-export semantics. Public artwork loads from the approved development repository. See [the platform matrix and limitations](PLATFORM-VALIDATION.md).

The initial import refusal left four posts. The published-package retry subsequently accepted all twelve Saffron posts and all twelve Wayfarer posts into the shared lab, with content and dates independently verified. Blogger then imposed an import attempt limit twice; eighteen full exports remain unverified. Native input resolved the composer expansion problem. Saffron/Wayfarer publication and replies passed; Lesson’s top-level comment passed, but its reply failed twice with Blogger’s generic publish error. Remaining publication checks are blocked; see the [comment/screen-reader matrix](COMMENTS-SCREEN-READER.md). Native pagination also skips posts tied at an exact timestamp when that timestamp straddles a one-post page boundary; the two-post fixture round trip passes.

## Production release gates

Accept the remaining eighteen packaged demo exports and complete native comment publication/reply checks in a working session. The installed-theme view matrix is complete; retain it when changing shared behavior. Review keyboard/screen-reader behavior and measure performance on the actual demo. Complete niche-specific demo writing and editing; Saffron's original sample recipes are illustrative and have not been kitchen-tested. Check all optional integrations disabled and failing.

Public development assets are available. Prepare coherent per-theme demos, then create a versioned, checksummed release matching the installed XML. Only then add production Colorlib listings. The nine maintained existing templates retain their separate releases and download links.

## Owner controls and accessibility follow-up

Native introduction/logo/accent changes and menu persistence passed on all twenty templates. All twenty live skip links show visible focus and reach main content; 40 live homepage/article DOM checks passed the sampled contrast/control-name audit. Local tests now also check rendered contrast and names across the existing 200 viewport cases. The separate hub passes filtering/reset and five-width checks. See [scope, fixes and source-size figures](OWNER-ACCESSIBILITY-REVIEW.md).

The public lab is a dedicated shadcn-inspired catalog, with development previews published through the approved Pages workflow after validation. No production release is implied. Measured live performance, screen-reader/physical-device review, full demo imports and comment publication/replies remain acceptance gates.

All twenty hosted preview pages and ZIP downloads were verified after deployment; downloaded packages match their generated SHA-256 checksums. The installed hub also passes actual Blogger phone/tablet checks at 320/375/768px and native article/search/About routes.

## Comment and release-package follow-up

All twenty templates passed forty desktop/mobile-route comment rendering and accessibility-tree checks after fixes to headings, region labels, hidden relay links, native visibility states and comment spacing. Actual VoiceOver speech is blocked by native browser connection timeouts. The new release-staging command prepares a separate numbered preview from a clean source commit with pinned artwork, manifest/checksums and explicit release-status notes in every ZIP. These packages remain development previews while acceptance gates are open.

## Published preview and hub downloads

Published [v0.1.0-preview.2](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.2) as a prerelease. Its twenty ZIPs remain frozen from commit `a672d7a1bca99d776f66322deead9d7ececf80c4`, whose suite passed 51 tests. The later hub update adds one URL/disclosure regression (52 total) and links both Blogger and static catalogs to those immutable assets. The hub visibly lists incomplete checks before visitors reach the download cards. Existing blocked checks remain open; publication does not imply production acceptance.

## Retrying the published imports and publishing flows

The [latest retry matrix](BLOGGER-RETRY.md) uses files extracted from the published preview packages. Saffron/Wayfarer full exports passed merging into the shared lab: all 24 titles, labels, publication dates, feature blocks and pinned artwork URLs verified; four sampled imported article views passed. Lesson's import hit Blogger's attempt limit twice, leaving eighteen export acceptances open. Lesson's reply and Bench's new-comment retry failed. All twenty released comment views/forms and earlier persisted replies passed reinspection; this does not close their remaining publication gates. No additional template defect was reproduced.

## Media and editorial source pass

The [media/editorial review](MEDIA-EDITORIAL-REVIEW.md) records local YouTube playback and recovery under all twenty themes, Vimeo’s supported-browser failure, 240 distinct editorial briefs, topic-specific lesson/travel fixes and the outstanding native/device/factual acceptance gates. These changes are later than the frozen preview.2 packages.
