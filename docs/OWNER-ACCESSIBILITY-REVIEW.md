# Owner controls and accessibility review

## Latest reliability follow-up — November 9, 13:11 UTC

All twenty themes received fresh-tab in-app and authenticated Safari comparisons. Recorded submissions persisted in 21/40 in-app cases and 29/40 Safari cases; the stock Blogger Simple Bold control also failed on a reply. Basic positive observations remain, but publishing reliability is still a release gate. Native Chrome control was unavailable. [Current matrix and evidence](COMMENT-RELIABILITY.md). Earlier sections retain their original scope and counts.

## Earlier November 9 follow-up

All twenty themes passed 60 fresh native keyboard/DOM views. Twelve now have positive root/reply observations across sessions. Verdant’s reply passed a spaced retry; Pace’s subsequent root and Bench’s legacy-article root failed. Eight publication/reply rows remain unverified. Native Safari works; actual VoiceOver output remains unverified after its app connection timed out. Measured live performance is still unavailable. [Current matrix, evidence and release blockers](ACCESSIBILITY-COMMENTS-FOLLOWUP.md). The report below is historical.

November 6, 2026 · Development previews

All twenty templates were installed sequentially on the public Blogger lab. Native controls were edited through Blogger's UI; successful saves were verified on the public blog.

| Theme | Native owner controls | Live keyboard / DOM checks | CSS source (KiB) |
| --- | --- | --- | ---: |
| Saffron | Pass | Pass | 15.9 |
| Wayfarer | Pass | Pass | 15.9 |
| Lesson | Pass | Pass | 18.2 |
| Bench | Pass | Pass | 17.5 |
| Maker | Pass | Pass | 16.8 |
| Muse | Pass | Pass | 16.4 |
| Kinship | Pass | Pass | 16.5 |
| Companion | Pass | Pass | 16.9 |
| Shelf | Pass | Pass | 16.8 |
| Playbook | Pass | Pass | 16.8 |
| Soundboard | Pass | Pass | 17.2 |
| Verdant | Pass | Pass | 17.0 |
| Pace | Pass | Pass | 17.3 |
| Ledger | Pass | Pass | 17.9 |
| Screen | Pass | Pass | 16.8 |
| Borough | Pass | Pass | 17.0 |
| Studio | Pass | Pass | 17.5 |
| Launchpad | Pass | Pass | 17.4 |
| Ceremony | Pass | Pass | 17.0 |
| Cause | Pass | Pass | 17.1 |

## Native owner controls

Each row verifies a saved homepage introduction marker, a real logo URL with description placed after the image, a saved accent change, one H1 and preservation of the native About page-menu link. The About link was added once using PageList and persisted across all twenty installations; this is not twenty independent menu edits. Accent changes were reset before default-color accessibility checks. Temporary markers, logos and descriptions are removed from the final hub.

On the shared Cause header, also verified image-behind-title (decorative image, one spoken title), image-replaces-title (image alt supplies the name, description omitted), and shrink-to-fit. Native Background and Text color changes were saved and verified separately. These representative shared-control checks supplement, rather than replace, each theme's saved accent/logo/introduction checks.

Fixed a missing Theme Designer group that left color variables listed without usable inputs. The three controls now appear in **Advanced → Theme colors**. Fixed header placement/description handling, hidden owner descriptions, duplicate logo announcements and shrink-to-fit support. Custom palettes still require an owner contrast review; fixed decorative panel colors do not automatically adapt to arbitrary palette changes.

## Accessibility checks

- All twenty live homepages: the first Tab exposes the skip link with a visible 3px focus outline; Enter focuses `main-content`.
- All twenty live homepage/component-article pairs: no unnamed visible controls or sampled text-contrast failures in the DOM audit. Live color sampling uses leaf elements; it does not certify text over artwork, complex compositing or cross-origin Google interfaces.
- The automated Chrome suite audits text-node contrast and control names on home/article fixtures at 320, 375, 768, 1024 and 1440px (200 cases). This is a focused regression check, not axe/Lighthouse or a complete WCAG audit.
- Generalized focus-visible styling to include textareas, selects and other focusable elements. Added accessible names to image links even when their fallback artwork is decorative.
- Optional player regression: rejected insecure, lookalike, credential-bearing and nonstandard-port destinations; accepted allowlisted players retain their title and keyboard focus. Network access is blocked in this test, so provider availability/playback is not verified.
- Hub regression: filtering, combined search, no-result state, reset focus and responsive geometry/contrast at five widths. Cards and links remain available without JavaScript; filtering controls appear only when active. The installed public Blogger hub also passes actual 320/375/768px geometry checks, native article/search/About views, keyboard entry and sampled contrast/name checks. Its native search description and matching Open Graph description were saved and verified.
- All twenty hosted static preview pages and twenty ZIP downloads return HTTP 200. Every downloaded ZIP matches the generated SHA256SUMS. GitHub validation and the approved preview deployment passed.

The [follow-up comment/screen-reader report](COMMENTS-SCREEN-READER.md) records forty additional live comment views, successful Saffron/Wayfarer publication/replies, Lesson’s partial success and the repeated Blogger publication failure. Actual VoiceOver speech remains blocked by unavailable native browser connections. Physical-device and third-party playback checks remain open; these results do not establish full accessibility conformance.

## Performance scope

Chrome DevTools MCP was unavailable. The owner explicitly chose to continue and document the gap. **No measured live LCP, INP, CLS, TBT or Lighthouse score is claimed for any of the twenty themes.** All twenty retain a measured-performance release gate.

The table records generated CSS source bytes divided by 1024, not network transfer or load time. Shared runtime is 5,883 bytes (5.7 KiB); separately gzipping it yields 1,942 bytes. CSS separately gzips to approximately 4.1–4.6 KiB. Blogger serves these inline in the document, so these isolated compression figures are illustrative. They exclude Blogger's own HTML/widgets/scripts, content, images, comments and optional players.

Source review confirms system fonts, inline theme CSS/runtime, reserved dimensions on generated story artwork, lazy below-fold card images and no CSS/JavaScript framework requests. The hub also lazy-loads later thumbnails. No speed improvement percentage or field-vitals conclusion can be inferred from those properties. After DevTools is available, record cold mobile/desktop home and article traces for every theme, including actual media and comments; investigate observed regressions before release.
