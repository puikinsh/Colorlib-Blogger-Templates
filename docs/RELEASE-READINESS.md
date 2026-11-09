# Development preview release status

Updated November 9, 2026. These packages are prepared for development testing, not production acceptance. They are not replacements for the nine separately maintained Colorlib Blogger releases.

## Published preview.5 visual refresh

[Preview.5](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.5) is published as a development prerelease from `e3e83b8b0ca5440a9e957b191ca6c6ab08056861`. It includes sixty credited photographs, responsive WebP variants, twenty distinct visual notebooks, richer article galleries and a Layout-editable homepage gallery gadget. All twenty new gallery widgets and their sixty photos were checked natively at 375px; forty local homepage and twenty article image-rendering cases passed, along with all 60 automated tests. See [visual refresh](VISUAL-REFRESH.md).

Six updated photo-rich exports now passed (72 posts); fourteen await acceptance after Blogger’s import-frequency limit. All twenty installed themes passed photo-rich story rendering at 375px; all 72 accepted stories passed at 320px. Both Labs show actual desktop/mobile template screenshots. See [current import and screenshot results](PHOTO-IMPORTS.md). Older import/playback evidence remains historical, and all speech, measured-performance, media reliability, service-limit, physical-device and editorial gates below remain open. Previous preview.4 packages remain unchanged.

## Preview.4 scope

Preview.4 includes the audio-error feedback and minimum player-height fixes, native audio/mobile evidence, offline documentation and original QA signals in the source repository. The twenty theme XMLs retain the validated behavior; only their release version label changes during staging. Publication does not close the unresolved narrow-video, Vimeo or other gates below. Preview.3 stays frozen.

## Included and verified

- Twenty distinct theme XML files, twelve-post demo exports, original artwork, editable article formats, setup instructions and GPL v3 license text.
- Native theme installation, owner controls, responsive views and native two-post Older/Newer round trips across all twenty templates.
- Comment rendering and accessibility-tree checks on desktop and `?m=1` routes across all twenty themes. Shared comment headings, region labels, hidden relay links, inactive controls and author/date spacing were fixed.
- Root/reply publication has positive observations under eleven themes across sessions. The November 9 follow-up completed Lesson’s reply and eight new paired publishing checks; Verdant’s root passed but its reply failed. Bench’s legacy-article root still failed despite success on a photo-rich article. Eight publishing/reply rows remain unverified. See the [current matrix](ACCESSIBILITY-COMMENTS-FOLLOWUP.md).
- Native controls, optional-player URL/focus checks and automated responsive regressions. See the repository validation reports for exact coverage and test counts.

## Blocked or outstanding acceptance

- **Screen-reader speech:** Accessibility-tree/keyboard checks are completed. Native Safari control became available for the provider follow-up, but actual VoiceOver speech/rotor verification has not been completed for any theme. The November 9 OS-switch test was restored to off after the VoiceOver app connection timed out.
- **Comment publishing:** eleven themes have positive root/reply observations across sessions. Verdant’s root passed but its reply failed; eight other themes remain unverified. Bench’s root on the legacy article still failed despite its photo-rich root/reply pass. Complete the [current matrix and reliability follow-up](ACCESSIBILITY-COMMENTS-FOLLOWUP.md); the generic Blogger error’s cause is unknown.
- **Complete demo imports:** six preview.5 exports accepted (Lesson, Bench, Maker, Muse, Kinship, Companion; 72 posts). Shelf hit Blogger’s import-frequency limit and the queue stopped. Fourteen updated exports remain unverified. A fresh Shelf retry at 11:32 UTC returned the same limit; no new posts were accepted. Earlier Saffron/Wayfarer acceptances cover older content only. See the [current matrix](PHOTO-IMPORTS.md).
- **Live performance:** DevTools was unavailable; the owner chose to document the gap. No measured live Core Web Vitals or Lighthouse score is claimed.
- **Media/editorial:** all twenty local previews passed YouTube playback and shared recovery checks; Vimeo returned a supported-browser error. All twenty revised XMLs also passed native Blogger YouTube playback/recovery on the ordinary and `?m=1` routes at 1280px; see the [native media matrix](NATIVE-MEDIA.md). Vimeo, reliable narrow-video playback, audible output, physical-device/provider acceptance and final editorial approval remain open. All 240 samples are explicitly editing briefs; recipes remain untested. See the [media/editorial review](MEDIA-EDITORIAL-REVIEW.md).

Blogger's native timestamp cursor can skip a post when identical publication times straddle a pagination boundary. Keep demonstration publication timestamps distinct and verify page-size changes. The theme preserves native navigation URLs.

## Historical November 6 retry

The [published-package retry](BLOGGER-RETRY.md) records 24 accepted demo posts, the repeated import limit, the Lesson/Bench publish failures and current comment-form checks across all twenty released templates. These partial results do not close the stable-release gates above.

## Earlier published preview.4

[v0.1.0-preview.4](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.4) is published as a development prerelease. Its twenty ZIPs, release notes, manifest and checksums are frozen from commit `e3af8d5c6745c624d452d347e98447e921e7c0e1`. They include audio failure feedback, the minimum mobile player height, media/editorial fixes, offline documentation and native test evidence. The hubs now point to preview.5; this paragraph records the earlier preview.4 publication. All twenty rendered Blogger download links and the checksum link were verified November 8, 2026. The incomplete checks remain visible before the cards; publication does not close them.

Preview.2 and preview.3 remain available unchanged. Embedded package status files record their preparation-time state; this page and the release description carry the current publication status.

## Package integrity and publication

The normal gallery ZIPs are mutable development previews. `tools/stage_release.py --version 0.1.0-preview.6` stages a separate set from a clean source commit, pins demo artwork URLs to that commit and writes SHA256SUMS, a manifest and release notes. Each ZIP includes this status file. Verify with `shasum -a 256 -c SHA256SUMS` (or `sha256sum -c SHA256SUMS` on Linux).

A published preview is not a production release. Do not mark it production-ready or replace Colorlib production downloads until the outstanding acceptance checks pass. Current reports: [platform validation](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/PLATFORM-VALIDATION.md) and [comment/screen-reader checks](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/COMMENTS-SCREEN-READER.md).

## Audio/mobile checks included in preview.4

All twenty candidates passed native MP3/WAV playback, pause and seek checks at 375px and 320px, with focused retries retained in the evidence. Audio failure feedback and a 200px minimum player height were fixed; final narrow layouts/recovery passed all forty native cases. Reliable narrow-width YouTube playback remains unresolved after pauses/stalls. These fixes and evidence are included in preview.4; preview.3 ZIPs remain unchanged. See the [audio/mobile matrix](AUDIO-MOBILE.md) for exact scope, retries and remaining gates.

## November 8 provider reliability follow-up

All twenty XMLs passed forty new native YouTube startup checks at 375px/320px; Maker/Muse also advanced beyond 22 seconds. Vimeo reproduced its supported-browser failure under all twenty and on its standalone player page. No new runtime defect or permanent stall fix was established. Keep repeated-session reliability and Vimeo acceptance open. [Method, evidence and troubleshooting](PROVIDER-RELIABILITY.md) are newer than the frozen preview.4 packages.

## Supported-browser follow-up, November 8

All twenty templates now have positive native Safari 27.2 YouTube/Vimeo observations after retained retries. Initial YouTube cycles advanced in 36/40 cases; Vimeo advanced in 18/20 initial checks. Companion, Shelf and Playbook's focused retries passed. Standalone Vimeo also later paused near one second. This closes the absence of a supported-browser comparison, not reliable playback acceptance: intermittent pauses, IAB Vimeo, independent instrumented browsers, long sessions and narrow/physical-device checks remain open. No new runtime defect or parameter fix was confirmed. See [the exact matrix, evidence and remaining gates](PROVIDER-SAFARI.md). Published preview.4 packages remain unchanged.
