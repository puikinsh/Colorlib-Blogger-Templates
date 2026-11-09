# Richer visual demonstrations

## Latest photo-rich follow-up — November 9

Six updated exports passed (72 posts); Blogger then limited Shelf and the queue stopped, leaving fourteen updated exports unverified. All twenty native themes passed photo rendering at 375px, and all 72 accepted stories passed at 320px. Both Labs now use forty actual static-demo desktop/mobile screenshots. No theme image/mobile defect was reproduced. [Exact matrix, scope and remaining gates](PHOTO-IMPORTS.md). Historical entries below retain their original test dates and scope.

Updated November 9, 2026. The new development previews add sixty curated photographs, two responsive sizes per photograph, twenty niche-specific visual notebooks and photo-pair sections in all 240 demo articles. Original SVG covers remain in each package.

## What changed

Lead stories and cards now use real editorial photography. Food notebooks, travel panoramas, fashion/portfolio lookbooks, workspace studies, magazine layouts and community journals use different compositions and niche-specific copy. A separate **Layout → Homepage visual notebook** HTML gadget lets owners edit or remove the native homepage gallery. The post list, featured story and native pagination retain their existing behavior.

Every theme has three distinct photographs, reused throughout its twelve illustrative stories. The photos demonstrate the layout; they do not document fictional recipes, projects, events or participants. Credit links are visible, and `assets/photography.json`, `assets/photo-credits.json` and package `ASSETS.md` record sources. Photography retains the [Unsplash License](https://unsplash.com/license), separately from GPL v3 source and original SVG illustrations. No Unsplash+ assets are included.

Images are bundled locally and served from our public repository for Blogger. Each photo has 1200×900 and 480×360 WebP versions, with dimensions and responsive `srcset`; non-lead images load lazily. All 120 files together total about 13.7 MiB. No remote photo service or carousel script runs in visitors’ browsers. See [owner editing](OWNER-EDITING.md) for replacement instructions.

## Validation and release boundary

[Recorded local observations](evidence/visual-refresh-2026-11-09.json) cover all twenty homepages at actual 1280px/375px widths and all twenty article photo pairs at 375px. Every observed gallery image decoded and no horizontal overflow was found. XML/source/schema checks and all 60 regressions passed locally and on GitHub, including the new asset/credit/package checks. Source checks cover all twenty native XMLs and exports.

All twenty complete XMLs were then installed through Blogger. Each served theme class, distinct gallery heading, actual 375px viewport and `HTML2` widget was verified; all sixty gallery photos decoded without horizontal overflow. Native Older Posts URLs remained present. Updated photo-rich demo exports were not re-imported; earlier import evidence covers the older fixtures only. Preview.5 packages carry this visual refresh from the validated source. Previously published preview.4 packages remain frozen. Older native playback evidence applies to the unchanged player runtime, but it does not establish complete acceptance for the revised visual layouts.

Intermittent YouTube/Vimeo reliability, remaining demo imports and comment publication, real screen-reader speech/rotor, measured live performance, physical devices and final editorial approval remain open. See [release readiness](RELEASE-READINESS.md).

## Preview.5 publication

[Preview.5 is public](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.5), with twenty immutable ZIPs from `e3e83b8b0ca5440a9e957b191ca6c6ab08056861`, release notes, manifest and checksums. All twenty published downloads matched staged bytes/checksums, and release XMLs matched native-tested candidates after version/asset-host normalization. Both generated hub formats point to preview.5; the live Blogger hub’s twenty links and photo cards were verified. [Publication evidence](evidence/preview5-publication-2026-11-09.json) records exact destinations and the retained visible testing notice. Older releases remain unchanged.
