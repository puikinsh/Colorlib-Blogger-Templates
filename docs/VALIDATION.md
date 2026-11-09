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

## Native media follow-up

All twenty revised XMLs passed native YouTube playback/recovery on both Blogger URL routes at 1280px; Muse passed after a focused decoding retry. Vimeo failed with the supported-browser message under every theme. The [native matrix](NATIVE-MEDIA.md) includes fixture/evidence files, exact scope and unrun audio/device/provider checks. The lab hub was restored. Preview.3 is prepared as a separate draft; preview.2 stays frozen.

## Preview.3 publication

Published the verified preview.3 packages from `adf4ded8b81b79a7275b8d57431fa47dcbb34ff0` as a development prerelease. Both hubs now link all twenty downloads and SHA256SUMS to preview.3 and retain visible speech, comment, import, performance, Vimeo, device/audio and editorial gates. Release assets remain the exact staged bytes; package-time reports are preserved.

## Audio and narrow-viewport source pass

The [audio/mobile matrix](AUDIO-MOBILE.md) records eighty native audio format/route checks and forty final Blogger layout/recovery checks across all twenty themes at verified 375px/320px viewports. Focused retries remain visible in the evidence. Shared failed-audio feedback and the minimum video-player height were fixed. Reliable narrow-video playback remains open after intermittent pauses/stalls; physical-device, audible-output and all earlier service/tool blockers remain. Published preview.3 assets were preserved.

## Preview.4 publication

Preview.4 packages the verified audio/mobile candidate from `e3af8d5c6745c624d452d347e98447e921e7c0e1`. Version-normalized XML hashes match the native-tested candidate for every theme. The generated/static hubs point all twenty downloads and checksums to preview.4 and retain the full blocker notice. Live Blogger synchronization completed November 8, 2026; all twenty package links and the checksum link were verified. Older release assets are unchanged.

The preview.4 hub deployment initially stopped when the asynchronous audio regression exited before its recovery event. The fixture now waits for the expected source states and metadata event with a bounded deadline, instead of a fixed initial delay and redundant reload. The published template assets are unchanged by this test-only correction.

## Live Blogger preview.4 synchronization

On November 8, 2026, the restored computer-use controls opened the signed-in Blogger Theme editor. The existing hub XML was backed up, the prepared preview.4 hub XML was saved, and the rendered public hub was inspected.

All twenty download URLs exactly matched the catalog's versioned preview.4 filenames. The checksum URL also used preview.4. Browser downloads of every linked ZIP and SHA256SUMS matched the frozen files; the [verification record](evidence/preview4-live-hub-2026-11-08.json) records canonical URLs and hashes.

The notice remained visible before the download cards, retaining speech/rotor, comment, import, measured-performance, narrow-video, Vimeo, physical-device, audible-output and editorial gates. Browser control and hub synchronization are resolved; none of those acceptance gates is marked passed by this update. Release assets were not replaced.

## November 8 provider isolation and retry

Installed all twenty full XMLs through Blogger; verified theme classes and actual 375px/320px widths. All forty YouTube startup cases advanced while unpaused with final readyState 4; close/focus recovery and overflow checks passed. Maker/Muse longer runs reached 24.93s/22.62s. Vimeo failed under all twenty, including two focused message-wait retries, and outside Blogger on its standalone player page. Independent Chrome control timed out. No new runtime change was justified; intermittent reliability and all existing acceptance gates remain open. The hub was restored with twenty preview.4 links. See [the provider report](PROVIDER-RELIABILITY.md) and its retained observations.

## Supported-browser follow-up, November 8

All twenty templates now have positive native Safari 27.2 YouTube/Vimeo observations after retained retries. Initial YouTube cycles advanced in 36/40 cases; Vimeo advanced in 18/20 initial checks. Companion, Shelf and Playbook's focused retries passed. Standalone Vimeo also later paused near one second. This closes the absence of a supported-browser comparison, not reliable playback acceptance: intermittent pauses, IAB Vimeo, independent instrumented browsers, long sessions and narrow/physical-device checks remain open. No new runtime defect or parameter fix was confirmed. See [the exact matrix, evidence and remaining gates](PROVIDER-SAFARI.md). Published preview.4 packages remain unchanged.

## November 9 visual refresh

Added sixty credited photographs, responsive image variants, twenty visual compositions and photo notebooks in 240 demo articles. Forty actual-image homepage checks at 1280px/375px and twenty article checks at 375px passed without overflow. All twenty complete XMLs then passed native 375px gallery rendering, theme/widget identity and sixty decoded photo checks; native Older Posts URLs remained intact. All 60 automated regressions passed. Updated demo exports were not re-imported; provider reliability, service, speech, performance, device and editorial gates remain. See [the visual report and evidence](VISUAL-REFRESH.md).
