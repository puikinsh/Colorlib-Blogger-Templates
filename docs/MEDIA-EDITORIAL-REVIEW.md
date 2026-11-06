# Media and editorial review

Reviewed November 6, 2026. This is a development-source review, not stable-release acceptance. The published `v0.1.0-preview.2` ZIPs remain frozen and do **not** contain these later fixes.

## Media results and fixes

Every generated theme now has a `media.html` review page with explicitly labeled public provider examples. The fixtures use the [official YouTube iframe example](https://developers.google.com/youtube/iframe_api_reference) and [Vimeo SDK example](https://github.com/vimeo/player.js/). Normal demo articles still make no media-provider requests.

In the interactive browser at 1155px, all twenty local theme previews loaded the YouTube example after activation. Each returned `paused=false`, `readyState=4` and a positive playback time. The initial Soundboard run advanced beyond 15 seconds. Every theme displayed the invalid-URL message, removed its iframe on close, returned focus to the load button and had no page-width overflow. This establishes local browser playback, not audible sound or Blogger-hosted playback.

Vimeo's official sample loaded its controls under Soundboard, but activation returned **“Unable to play video. Please try again in a supported browser.”** Its video had `readyState=0` and time zero. A retry reproduced the provider error. Vimeo playback remains blocked in this browser; it is not passed for any theme. No error log was submitted.

Shared fixes:

- Invalid URLs produce a visible `role="status"` message instead of a silent dead button.
- Loaded players retain a provider watch-page link and a stop/close button; closing removes the iframe and restores focus. Retrying creates one player.
- Pasted autoplay/API/tracking parameters are removed; a Vimeo unlisted `h` value is retained. HTTPS host/path restrictions remain in place.
- Player dimensions are reserved; controls remain outside the player viewport and readable in light/dark themes.
- No iframe load event is treated as proof of playback. The status says “Player requested.”

## Editorial review matrix

All 240 titles, teasers, generated bodies and niche feature formats were reviewed for demonstration labeling and subject alignment. Each article now has its own editing focus; repeated scaffold teasers were replaced. Bodies remain reusable editing briefs, not completed factual reporting.

| Theme | Specific review or correction | Owner acceptance still needed |
| --- | --- | --- |
| Saffron | Visible cooking time, untested disclosure; demo Recipe schema suppressed | Kitchen tests, quantities, handling, dish images |
| Wayfarer | Packing/museum/rain/notebook posts use planning notes rather than unrelated day itineraries | Actual routes, access, dated official details |
| Lesson | Twelve subject-specific code examples replace two repeated examples | Full lessons and learner exercises |
| Bench | Per-article evidence briefs; illustrative review disclosure retained | Real device tests and sourced specifications |
| Maker | Measurements, materials and condition briefs | Safe, tested project instructions |
| Muse | Credits, provenance and image-permission briefs | Actual products and usage rights |
| Kinship | Privacy-aware activity and journal briefs | Consent and appropriate activity details |
| Companion | Individual care-record briefs; no invented treatment advice | Owner/veterinary review of actual instructions |
| Shelf | Unattributed blockquote changed to an explicit review prompt | Real editions, quotations and permissions |
| Playbook | Platform/version, spoiler and testing briefs | Actual games and observed results |
| Soundboard | Fictional script labeled; no implied published episode | Real recording, consent, transcript and chapters |
| Verdant | Dated observation and identification briefs | Plant identification and sourced care details |
| Pace | Personal-reflection briefs without outcome claims | Author review of any actual instruction |
| Ledger | Currency, dates and assumptions briefs | Real sourced examples; no account data |
| Screen | Fictional/real reporting and spoiler boundaries | Actual viewing notes and credits |
| Borough | Event-source, interview and consent briefs | Confirmed dates, timezone and local reporting |
| Studio | Fictional case-study and evidence briefs | Client permission and actual outcomes |
| Launchpad | Versioned tutorial and change-description briefs | Real product behavior and working destinations |
| Ceremony | Imagined-event and collaborator-credit briefs | Permissions, actual schedules and credits |
| Cause | Evidence, methodology and donation-destination briefs | Genuine organization details and verified figures |

## Regression evidence

The suite covers 300 home/article/media-page cases at 320, 375, 768, 1024 and 1440px, including 100 active-player/failure-recovery article cases. Provider requests are blocked in automated fixtures: those cases establish layout, URL filtering, focus, close/retry and fallback behavior, **not** playback. All 54 tests passed, along with the XML/source checker and whitespace check. Separate tests check all 240 distinct briefs, lesson subject examples, travel format alignment and demo/owner Recipe schema behavior.

## Outstanding and blocked

- **Blocked:** Vimeo playback in the current browser; actual screen-reader speech/rotor access; measured live performance without DevTools; Blogger import/publishing restrictions recorded in [the retry report](BLOGGER-RETRY.md).
- **Still to run:** native Blogger playback with these revised XMLs, physical devices/Safari/Firefox, audible output, fullscreen/PiP, captions and transcript accuracy against owner-owned recordings, unavailable/private/region-restricted media and network/consent failures on supported browsers. No all-provider acceptance is claimed.
- **Editorial acceptance:** owners must replace briefs with coherent original reporting and verify claims, sources, permissions and external destinations. Recipes remain untested. No template is declared production-ready.

Rebuild development packages to test these fixes. Publish a new numbered preview after native checks; never replace the existing release assets under their old version.
