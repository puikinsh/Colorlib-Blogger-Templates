# Photo-rich import and preview checks

Updated November 10, 2026. Tested the exact XML/demo files extracted from frozen [preview.5](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.5), source `e3e83b8b0ca5440a9e957b191ca6c6ab08056861`, on the [public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/).

## November 10 follow-up

Six more exports passed: Shelf, Playbook, Soundboard, Verdant, Pace and Ledger (72 new posts). Twelve updated exports are now accepted, with 144 photo-rich posts among 173 public posts. All 72 new stories passed own-theme 320px image/layout checks. Screen then hit the import-frequency refusal; eight updated exports remain pending: Saffron, Wayfarer, Screen, Borough, Studio, Launchpad, Ceremony and Cause. The queue stopped. [Current results, retained 503/retries and evidence](RELEASE-FOLLOWUP-2026-11-10.md).

The sections and matrix below retain their November 9 scope; use the current follow-up above for acceptance totals.

## November 9 results and import limit

Blogger accepted Lesson, Bench, Maker, Muse, Kinship and Companion: **72 photo-rich posts, 12 per export**. The public Atom feed was traversed through its advertised next links; every expected title/label, three responsive image elements (dimensions and srcset), photo-pair section and three credit URLs were verified. The lab now contains 101 public posts, including older fixtures.

Shelf then returned **“Seems like you tried to import too many times. Please try again later.”** We stopped the queue. Fourteen updated exports remain unverified, including the updated Saffron/Wayfarer exports; their earlier imports do not establish acceptance of the new photo content. Do not create extra blogs or remove established fixtures to circumvent the limit.

## Follow-up retry at 11:32 UTC

The owner requested another pass on November 9. We retried the exact released Shelf export in a separate signed-in import tab. Blogger again returned **“Seems like you tried to import too many times. Please try again later.”** Public feed snapshots before/after remained at **101 total posts / 72 photo-rich posts**. No new posts were accepted. We stopped after that refusal; the other thirteen pending exports were not submitted again. The fourteen-export native acceptance gap remains open. No new blog, account, timestamp changes or fixture deletion was used to evade the limit.

As a fallback, all **84 unique release-pinned photo URLs** referenced by those fourteen exports (168 stories, six variants per theme) were downloaded and matched source bytes. Fresh local home/sample-article checks passed for all fourteen at **320px and 375px: 56 cases**, all rendered images decoded and no horizontal overflow. Text-feed designs intentionally hide some thumbnails. These are local rendering and public-asset checks, not native Blogger import acceptance. No image/mobile defect was reproduced, and frozen preview.5 packages remain unchanged. [Retry evidence, exact asset URLs and viewport results](evidence/photo-import-retry-2026-11-09.json).

The matrix below still applies: Shelf was retried and refused again; the other thirteen updated exports remain pending. Existing actual screenshot cards stay available in both Labs. Source/XML/schema validation and all 61 regressions passed again (zero failures or skips).

| Template | Updated export | Native 375px layout fixture |
| --- | --- | --- |
| Saffron | Updated export pending; older export accepted historically | Shared photo-rich fixture |
| Wayfarer | Updated export pending; older export accepted historically | Shared photo-rich fixture |
| Lesson | 12/12 accepted; own articles checked | Own imported story |
| Bench | 12/12 accepted; own articles checked | Own imported story |
| Maker | 12/12 accepted; own articles checked | Own imported story |
| Muse | 12/12 accepted; own articles checked | Own imported story |
| Kinship | 12/12 accepted; own articles checked | Own imported story |
| Companion | 12/12 accepted; own articles checked | Own imported story |
| Shelf | Blocked by import-frequency limit | Shared photo-rich fixture |
| Playbook | Not retried after limit | Shared photo-rich fixture |
| Soundboard | Not retried after limit | Shared photo-rich fixture |
| Verdant | Not retried after limit | Shared photo-rich fixture |
| Pace | Not retried after limit | Shared photo-rich fixture |
| Ledger | Not retried after limit | Shared photo-rich fixture |
| Screen | Not retried after limit | Shared photo-rich fixture |
| Borough | Not retried after limit | Shared photo-rich fixture |
| Studio | Not retried after limit | Shared photo-rich fixture |
| Launchpad | Not retried after limit | Shared photo-rich fixture |
| Ceremony | Not retried after limit | Shared photo-rich fixture |
| Cause | Not retried after limit | Shared photo-rich fixture |

## Native images and mobile layouts

All twenty released theme XMLs were installed through Blogger. One imported photo-rich story per theme passed at an actual 375px viewport: correct served theme class, three decoded images, responsive small-image URLs, visible photo pair and no horizontal overflow. Six used their own imported story; fourteen used shared fixtures. These fourteen checks validate theme rendering, **not their export imports**.

All 72 accepted stories were additionally opened under their own themes at 320px. All 216 article photos decoded after scrolling; no horizontal overflow occurred. Native lazy loading was exercised through ordinary image clicks/scrolling. An initial cached previous-theme response was refreshed before its result was accepted. No product image/mobile defect was reproduced; no theme runtime or frozen ZIP was changed. [Sanitized evidence and exact URLs](evidence/photo-imports-2026-11-09.json).

## Actual screenshots in both Labs

Both catalogs now use real screenshots of the static template previews, rather than a single cover photograph. Each card offers a working preview, a full desktop capture and a mobile capture. Desktop captures were taken at 1440px (full page); mobile captures at 375×900. All forty captures loaded visible images without overflow. Text-only feed layouts intentionally retain their hidden thumbnails.

The optimized WebP files and capture provenance are committed in `assets/previews/manifest.json` (about 3.4 MB total). They show the actual static layouts; they do not claim to be live Blogger screenshots. Builds copy them locally for GitHub Pages; Blogger uses the public repository assets. Enlarged two-column cards and reduced-motion-aware hover/focus panning reveal more of each design. Direct screenshot links work without JavaScript. Preview.5 downloads remain unchanged.

## Remaining stable-release gates

Retry fourteen updated imports when Blogger allows them. Complete the existing comment publishing/reply, actual screen-reader speech/rotor, measured live performance, intermittent YouTube/Vimeo reliability, physical-device/audible-output/long-session and final editorial checks. See [release readiness](RELEASE-READINESS.md). Passing image rendering does not close these gates. XML/schema/source validation, all 61 regressions (zero skips) and whitespace checks passed for this update.
