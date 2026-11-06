# Native audio and mobile media review

Tested November 6, 2026 on the public Blogger lab. These are **new development-source results**, not a replacement for the frozen preview.3 package-time reports. The audio-error feedback and minimum-player-height fixes below are **not included in preview.3 downloads**.

## Scope and method

All twenty complete candidate XMLs were saved through Blogger's Theme editor. The served `theme-<slug>` class and actual DOM viewport were verified. Each theme used the ordinary [QA post](https://colorlib-blogger-theme-lab-2026.blogspot.com/2026/11/native-media-playback-validation.html) at **375px**, and `?m=1` at **320px**, both 812px high. These are narrow desktop-browser viewports, not emulated iOS/Android devices or physical touch tests.

The browser override applied to the active tab, so preflight attempts with mismatched dimensions were discarded. Fixed test tabs then reported the requested dimensions before observations were recorded. The hub was backed up and restored afterwards.

[Original observations and retries](evidence/audio-mobile-2026-11-06.json), [candidate XML/runtime/CSS hashes](evidence/audio-mobile-candidate.json), and the [post HTML](fixtures/audio-mobile-post.html) are retained. Audio tests preceded the final CSS-only height correction; the audio runtime did not change between those phases. Every final candidate's dimensions and recovery controls were then rechecked natively.

## Native audio: completed

The original [QA signal](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/f5ffc19d90399f92e6fb984a6ad3b498ae7f1773/assets/qa/README.md) is twelve seconds of brief, low-amplitude tones and silence. Checked-in MP3 and WAV files have commit-pinned HTTPS URLs; no speech, music or personal recording is used.

All **80 format/route cases** (20 themes × 2 widths × MP3/WAV) eventually showed advancing playback time while unpaused with `readyState=4`, then a paused state and successful seeking near six seconds using browser controls. They started paused, without autoplay; native audio controls and direct-file links fitted the viewport.

Four initial 320px observations had out-of-sequence pause states: Lesson/Bench WAV and Maker/Kinship MP3. Focused native keyboard/control retries passed; original observations remain in the evidence rather than being overwritten. Companion's initial video-control lookup timed out and passed on a later full route retry. These retries do not establish the cause of the initial interruptions.

An intentionally unavailable source produced visible, associated `role="status"` feedback on every route. The shared runtime preserves existing descriptions, handles direct `src` and individual `<source>` failures, waits for all alternatives before reporting failure, and clears stale feedback after metadata loads successfully. Automated tests exercise a valid alternative and recovery as well as actual decode failures. [MDN's audio documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio) explains that inner fallback text is for browsers without audio-element support; ordinary recording links are therefore supplied outside the player.

## Mobile video: corrected layout, reliability still open

The original 16:9 frame was only about 158px high at 320px and 188px high at 375px. This violated [YouTube's documented 200px × 200px minimum viewport](https://developers.google.com/youtube/iframe_api_reference#Requirements). The shared CSS now reserves at least 200px of height. All **40 final native layout cases** measured a 200px-high frame, no horizontal overflow, correctly sized audio controls, removal of the iframe on close and return of focus to the load button. Automated regressions cover the minimum size across all twenty designs and five widths.

Initial narrow-video runs demonstrated playback on many routes, but several sampled paused states or buffering; later Maker/Muse retries stayed at time zero, and a final Saffron retry stalled on both widths even with the corrected dimensions. A visible-tab retry also buffered. An inline-playback experiment did not validate and was removed. Default provider behavior and existing URL filtering remain intact.

**Reliable narrow-width YouTube playback is not passed for the collection.** The sizing defect is fixed, but its correction does not prove that the buffering/interruption problem is solved. No CAPTCHA, browser-security override, provider API workaround or forced autoplay was used. The initial desktop results remain a separate historical record.

## Per-theme matrix

| Theme | MP3 + WAV at 375px / 320px | Final layout at both widths | Narrow-video acceptance |
| --- | --- | --- | --- |
| Saffron | Passed | Passed | Open: reliability recheck |
| Wayfarer | Passed | Passed | Open: reliability recheck |
| Lesson | Passed after focused audio retry | Passed | Open: reliability recheck |
| Bench | Passed after focused audio retry | Passed | Open: reliability recheck |
| Maker | Passed after focused audio retry | Passed | Open: reliability recheck |
| Muse | Passed | Passed | Open: reliability recheck |
| Kinship | Passed after focused audio retry | Passed | Open: reliability recheck |
| Companion | Passed | Passed | Open: reliability recheck |
| Shelf | Passed | Passed | Open: reliability recheck |
| Playbook | Passed | Passed | Open: reliability recheck |
| Soundboard | Passed | Passed | Open: reliability recheck |
| Verdant | Passed | Passed | Open: reliability recheck |
| Pace | Passed | Passed | Open: reliability recheck |
| Ledger | Passed | Passed | Open: reliability recheck |
| Screen | Passed | Passed | Open: reliability recheck |
| Borough | Passed | Passed | Open: reliability recheck |
| Studio | Passed | Passed | Open: reliability recheck |
| Launchpad | Passed | Passed | Open: reliability recheck |
| Ceremony | Passed | Passed | Open: reliability recheck |
| Cause | Passed | Passed | Open: reliability recheck |

## Remaining gates and release boundary

- **Blocked/unresolved:** reliable narrow-width YouTube playback after pauses/stalls; Vimeo's previously reproduced supported-browser error; actual screen-reader speech/rotor connection; measured live performance without DevTools; Blogger imports/comment publication listed in [the retry report](BLOGGER-RETRY.md).
- **Still unrun:** physical phones/tablets, touch gestures, Safari/Firefox and other codecs/streaming formats; actual audible output and audio routing; long owner podcast episodes, background/lock-screen playback, fullscreen/PiP, captions/transcript accuracy for owner recordings, private/deleted/region-restricted media and network/consent failures on supported devices.
- **Editorial:** samples remain editing briefs; owners must verify facts, permissions, credits and destinations. Recipes remain untested.
- **Preview.3 stays frozen:** public downloads retain their exact published bytes. These later fixes and reports are in development source/static previews and the lab hub. A future numbered preview is needed to distribute them as release packages. No stable-release claim is made.

Validation: XML/source checks, whitespace checks and all 57 automated tests passed. This includes native audio decode/fallback/recovery behavior, all twenty responsive designs, and offline package documentation links.
