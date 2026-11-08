# YouTube and Vimeo reliability follow-up

**Later supported-browser results:** [Safari follow-up](PROVIDER-SAFARI.md) records positive playback under all twenty after retries, plus retained interruptions and a later standalone Vimeo pause. Earlier observations below remain historical evidence; reliability is still open.

Tested November 8, 2026 against source `ff2d5b9e1a1409409c01c5d41b5ec7b5e3da5db5`. [Sanitized observations and candidate hashes](evidence/provider-retry-2026-11-08.json) retain initial results, focused retries and the standalone-provider comparison. No runtime or stylesheet change was made in this pass. Published preview.4 assets remain unchanged; this follow-up is newer than their bundled reports.

## Native Blogger results

All twenty full theme XMLs were installed through Blogger's Theme editor. Before each check, the served `theme-<slug>` class and actual viewport were verified. The ordinary [media fixture](https://colorlib-blogger-theme-lab-2026.blogspot.com/2026/11/native-media-playback-validation.html) used 375px; `?m=1` used 320px, both 812px high. These are desktop IAB viewports, not physical mobile devices.

- **YouTube: 40/40 startup checks advanced.** After the provider's Play activation, two state samples separated by 1.2 seconds showed increasing time while unpaused. Each final sample had `readyState=4`. Maker at 375px and Muse at 320px, which stalled previously, also advanced to 24.93s and 22.62s in a focused longer run. No additional retry was needed for today's YouTube cases.
- **Recovery: 40/40 passed.** Close removed the optional iframe and returned focus to its load button. No horizontal page overflow was observed.
- **Vimeo: blocked under all twenty themes.** Eighteen initial observations displayed “Unable to play video” with a supported-browser link. Shelf and Launchpad were initially sampled before the message appeared; focused retries waited for the visible error and confirmed the same failure. The video stayed at time zero and `readyState=0`.
- **Standalone comparison:** opening the same official Vimeo sample directly at `https://player.vimeo.com/video/76979871`, without Blogger or our wrapper, reproduced the supported-browser error and zero playback. Native Google Chrome's control connection timed out, so no independent-browser comparison was obtained. No error log was submitted.

The lab hub was backed up and restored. Its `theme-lab lab-home` body class, twenty preview.4 ZIP links and visible blocked-check notice were verified afterwards.

## Interpretation and owner troubleshooting

Today's YouTube success does **not** establish the cause or permanent resolution of the November 6 stalls. The earlier failures remain in [the audio/mobile report](AUDIO-MOBILE.md). Short startup checks and two longer samples do not cover long videos, repeated sessions or different networks. No new theme-specific defect was confirmed, so provider parameters, permissions and playback behavior were left unchanged.

Vimeo's failure outside the template shows that the wrapper is not necessary to reproduce it; it does not identify a codec, network, provider or browser defect. [Vimeo's error guidance](https://help.vimeo.com/hc/en-us/articles/12425812280081-Troubleshoot-player-error-messages) and [system requirements](https://help.vimeo.com/hc/en-us/articles/12425777758609-System-Requirements-for-viewing-browsing-and-apps) describe the supported playback environment. A new comparison in a supported, independently controlled browser is still required.

When checking an owner's recording:

1. Use its real HTTPS embed URL; preserve Vimeo's required unlisted `h` value. Confirm embedding permissions and restrictions with the owner.
2. Activate Load, then the provider's Play control. Confirm increasing playback time; an iframe, spinner or Pause button alone is not proof of playback.
3. If it stalls, use the visible provider link and compare the same recording in an up-to-date supported browser. Record URL, browser/version, viewport, exact message and timeline behavior. Keep initial failures alongside retries.
4. Close the player before retrying. Do not force autoplay, disable browser security or infer provider errors from iframe load events.

The existing frame meets [YouTube's 200px minimum](https://developers.google.com/youtube/player_parameters); its explicit cross-origin referrer policy remains intact. The previous unsuccessful inline-playback experiment remains reverted.

## Release gates retained

Reliable repeated-session/narrow-width YouTube playback and Vimeo playback remain open. Physical devices, independent supported-browser playback, audible output, fullscreen/PiP, long episodes, private/regional media and captions/transcript acceptance remain unverified. Screen-reader speech/rotor, measured live performance, Blogger import/comment service failures and final editorial approval are unchanged; see [release readiness](RELEASE-READINESS.md). This is evidence for continued preview testing, not stable-release acceptance.

Validation: all twenty development ZIPs were regenerated and checked for this report/evidence; source/XML/link checks, whitespace checks and all 58 automated regressions passed. These local development ZIPs do not replace published preview.4 assets.
