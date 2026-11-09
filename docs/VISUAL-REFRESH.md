# Richer visual demonstrations

Updated November 9, 2026. The new development previews add sixty curated photographs, two responsive sizes per photograph, twenty niche-specific visual notebooks and photo-pair sections in all 240 demo articles. Original SVG covers remain in each package.

## What changed

Lead stories and cards now use real editorial photography. Food notebooks, travel panoramas, fashion/portfolio lookbooks, workspace studies, magazine layouts and community journals use different compositions and niche-specific copy. A separate **Layout → Homepage visual notebook** HTML gadget lets owners edit or remove the native homepage gallery. The post list, featured story and native pagination retain their existing behavior.

Every theme has three distinct photographs, reused throughout its twelve illustrative stories. The photos demonstrate the layout; they do not document fictional recipes, projects, events or participants. Credit links are visible, and `assets/photography.json`, `assets/photo-credits.json` and package `ASSETS.md` record sources. Photography retains the [Unsplash License](https://unsplash.com/license), separately from GPL v3 source and original SVG illustrations. No Unsplash+ assets are included.

Images are bundled locally and served from our public repository for Blogger. Each photo has 1200×900 and 480×360 WebP versions, with dimensions and responsive `srcset`; non-lead images load lazily. All 120 files together total about 13.7 MiB. No remote photo service or carousel script runs in visitors’ browsers. See [owner editing](OWNER-EDITING.md) for replacement instructions.

## Validation and release boundary

[Recorded local observations](evidence/visual-refresh-2026-11-09.json) cover all twenty homepages at actual 1280px/375px widths and all twenty article photo pairs at 375px. Every observed gallery image decoded and no horizontal overflow was found. Existing XML/source/schema checks and 58 regressions passed; two new asset/credit/package checks passed separately. Source checks cover all twenty native XMLs and exports.

Native Blogger validation of this new gallery gadget is pending before a new numbered preview is staged. Previously published preview.4 packages remain frozen. Older native playback evidence applies to the unchanged player runtime, but it does not establish complete acceptance for the revised visual layouts.

Intermittent YouTube/Vimeo reliability, remaining demo imports and comment publication, real screen-reader speech/rotor, measured live performance, physical devices and final editorial approval remain open. See [release readiness](RELEASE-READINESS.md).
