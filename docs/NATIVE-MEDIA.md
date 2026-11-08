# Native Blogger media validation

Tested November 6, 2026 using the development XMLs from `e1579c78bbe8f1648cc16b72f49d3dd4f23ec628`. A dedicated [public media fixture post](https://colorlib-blogger-theme-lab-2026.blogspot.com/2026/11/native-media-playback-validation.html) was published through Blogger's native HTML editor. Its [HTML](fixtures/native-media-post.html) and [sanitized observations](evidence/native-media-2026-11-06.json) are included for reproduction.

## Method and results

Each complete theme XML was saved through Blogger's Theme editor. The rendered `theme-<slug>` body class was checked before testing. Every theme was tested on the ordinary post URL and `?m=1`, at a **1280px desktop viewport**. The query route check is not a physical-mobile or narrow-viewport playback test. The original catalog hub was backed up and restored afterwards. The lab now has 29 posts, including this clearly labeled QA fixture.

On both routes, no optional-player iframe existed before activation. The official YouTube sample was activated using its own Play control; all forty route checks eventually returned positive playback time, `paused=false` and `readyState=4`. An initial Saffron run advanced beyond four seconds. Muse's first `?m=1` sample was taken before decoding began (`readyState=0`); its focused retry advanced beyond nine seconds with `readyState=4`. The initial observation remains in the evidence file.

Every route displayed invalid-URL feedback, provided the correct public YouTube watch-page fallback, removed the player on close, restored focus to the load button and created exactly one player on retry. No horizontal page overflow was observed at the test viewport. Native Blogger preserved the post's media attributes and the revised shared runtime behaved as in local previews. **No additional theme-specific defect was confirmed.**

The Vimeo sample was also activated under each of the twenty installed themes. Every run returned **“Unable to play video. Please try again in a supported browser.”** Playback is not passed for Vimeo. Its initial Saffron run had `readyState=0` and time zero. No error log, provider API workaround or browser-security change was used.

## Per-template matrix

| Theme | Ordinary Blogger route | `?m=1` route | Vimeo |
| --- | --- | --- | --- |
| Saffron | Passed | Passed | Blocked: browser error |
| Wayfarer | Passed | Passed | Blocked: browser error |
| Lesson | Passed | Passed | Blocked: browser error |
| Bench | Passed | Passed | Blocked: browser error |
| Maker | Passed | Passed | Blocked: browser error |
| Muse | Passed | Passed after retry | Blocked: browser error |
| Kinship | Passed | Passed | Blocked: browser error |
| Companion | Passed | Passed | Blocked: browser error |
| Shelf | Passed | Passed | Blocked: browser error |
| Playbook | Passed | Passed | Blocked: browser error |
| Soundboard | Passed | Passed | Blocked: browser error |
| Verdant | Passed | Passed | Blocked: browser error |
| Pace | Passed | Passed | Blocked: browser error |
| Ledger | Passed | Passed | Blocked: browser error |
| Screen | Passed | Passed | Blocked: browser error |
| Borough | Passed | Passed | Blocked: browser error |
| Studio | Passed | Passed | Blocked: browser error |
| Launchpad | Passed | Passed | Blocked: browser error |
| Ceremony | Passed | Passed | Blocked: browser error |
| Cause | Passed | Passed | Blocked: browser error |

“Passed” covers YouTube playback and the shared recovery/URL/focus checks above, not every media feature or provider. Both URL variants were checked using the same desktop browser.

## Remaining acceptance gates

- **Blocked:** Vimeo playback in this browser; actual screen-reader speech/rotor connection; measured live performance without DevTools; outstanding Blogger imports and comment publication described in [the retry report](BLOGGER-RETRY.md). Import/comment checks were not retried in this media pass.
- **Unrun:** physical phones/tablets, Safari/Firefox, narrow-viewport native playback, audible output, fullscreen/PiP, captions/transcript accuracy for owner-owned recordings, native audio-file/podcast playback, private/deleted/region-restricted media and network/consent failures in supported browsers.
- **Editorial:** all samples remain editing briefs. Verify real facts, rights, credits and external services; recipes still require kitchen testing.

## Updated preview preparation

Preview.3 includes the shared media recovery and editorial fixes from the preceding source pass, this native validation record, bundled offline documentation and protection against overwriting an already staged version. It remains a development prerelease, not a stable release. At package time, preview.3 was prepared as a draft and preview.2 downloads stayed active. Preview.3 is now published as a development prerelease and both hubs link to its new packages; preview.2 assets remain unchanged.

Validation: the XML/source checker and all 56 automated tests passed, including offline documentation links in all twenty ZIPs and refusal to overwrite a staged version.

## Subsequent audio/mobile pass

The [new development-source review](AUDIO-MOBILE.md) records completed MP3/WAV checks at 375px and 320px for all twenty themes, audio-error and player-height fixes, and unresolved narrow-video reliability. It supersedes the earlier unrun audio/narrow checks above; physical-device and audible-output acceptance remains open. Preview.3 assets are unchanged.

Publication follow-up: preview.4 now includes the audio-error and minimum-player-height fixes and the audio/mobile evidence. The unresolved gates in that follow-up remain open.

## Later narrow-width provider checks

The [November 8 follow-up](PROVIDER-RELIABILITY.md) records forty successful native YouTube startup checks at 375px/320px, longer Maker/Muse observations, and Vimeo failures both inside all twenty templates and outside Blogger. It supplements this historical desktop report; reliable playback, independent browsers and physical devices remain open.
