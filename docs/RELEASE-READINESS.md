# Development preview release status

Updated November 7, 2026. These packages are prepared for development testing, not production acceptance. They are not replacements for the nine separately maintained Colorlib Blogger releases.

## Preview.4 scope

Preview.4 includes the audio-error feedback and minimum player-height fixes, native audio/mobile evidence, offline documentation and original QA signals in the source repository. The twenty theme XMLs retain the validated behavior; only their release version label changes during staging. Publication does not close the unresolved narrow-video, Vimeo or other gates below. Preview.3 stays frozen.

## Included and verified

- Twenty distinct theme XML files, twelve-post demo exports, original artwork, editable article formats, setup instructions and GPL v3 license text.
- Native theme installation, owner controls, responsive views and native two-post Older/Newer round trips across all twenty templates.
- Comment rendering and accessibility-tree checks on desktop and `?m=1` routes across all twenty themes. Shared comment headings, region labels, hidden relay links, inactive controls and author/date spacing were fixed.
- New-comment and threaded-reply publication persisted after reload under Saffron and Wayfarer. Lesson's top-level comment published; its reply failed twice with Blogger's “Failed to publish comment. Please try again later.” Further publication attempts were stopped. Rendering existing comments does not establish publishing success for the other seventeen themes.
- Native controls, optional-player URL/focus checks and automated responsive regressions. See the repository validation reports for exact coverage and test counts.

## Blocked or outstanding acceptance

- **Screen-reader speech:** VoiceOver Utility is available, but native Chrome/Safari connections timed out. Accessibility-tree/keyboard checks are completed; actual VoiceOver speech/rotor verification is blocked for every theme.
- **Comment publishing:** Lesson’s reply failed again during the retry; a new-comment attempt under Bench returned the same Blogger failure. Complete Lesson’s reply and publication/reply checks for the other seventeen themes. The cause remains unknown; no CAPTCHA challenge appeared.
- **Complete demo imports:** the retry accepted all twelve Saffron posts and all twelve Wayfarer posts into the shared lab; titles, labels, timestamps, feature blocks and pinned artwork URLs were verified. Lesson then hit Blogger’s import attempt limit twice. The remaining eighteen exports are unverified. See the [retry matrix](BLOGGER-RETRY.md).
- **Live performance:** DevTools was unavailable; the owner chose to document the gap. No measured live Core Web Vitals or Lighthouse score is claimed.
- **Media/editorial:** all twenty local previews passed YouTube playback and shared recovery checks; Vimeo returned a supported-browser error. All twenty revised XMLs also passed native Blogger YouTube playback/recovery on the ordinary and `?m=1` routes at 1280px; see the [native media matrix](NATIVE-MEDIA.md). Vimeo, reliable narrow-video playback, audible output, physical-device/provider acceptance and final editorial approval remain open. All 240 samples are explicitly editing briefs; recipes remain untested. See the [media/editorial review](MEDIA-EDITORIAL-REVIEW.md).

Blogger's native timestamp cursor can skip a post when identical publication times straddle a pagination boundary. Keep demonstration publication timestamps distinct and verify page-size changes. The theme preserves native navigation URLs.

## Latest retry

The [published-package retry](BLOGGER-RETRY.md) records 24 accepted demo posts, the repeated import limit, the Lesson/Bench publish failures and current comment-form checks across all twenty released templates. These partial results do not close the stable-release gates above.

## Published preview

[v0.1.0-preview.4](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.4) is published as a development prerelease. Its twenty ZIPs, release notes, manifest and checksums are frozen from commit `e3af8d5c6745c624d452d347e98447e921e7c0e1`. They include audio failure feedback, the minimum mobile player height, media/editorial fixes, offline documentation and native test evidence. The static catalog and generated Blogger hub XML point to these exact packages. Live Blogger synchronization is pending restoration of browser control. The incomplete checks remain visible before the cards; publication does not close them.

Preview.2 and preview.3 remain available unchanged. Embedded package status files record their preparation-time state; this page and the release description carry the current publication status.

## Package integrity and publication

The normal gallery ZIPs are mutable development previews. `tools/stage_release.py --version 0.1.0-preview.5` stages a separate set from a clean source commit, pins demo artwork URLs to that commit and writes SHA256SUMS, a manifest and release notes. Each ZIP includes this status file. Verify with `shasum -a 256 -c SHA256SUMS` (or `sha256sum -c SHA256SUMS` on Linux).

A published preview is not a production release. Do not mark it production-ready or replace Colorlib production downloads until the outstanding acceptance checks pass. Current reports: [platform validation](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/PLATFORM-VALIDATION.md) and [comment/screen-reader checks](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/COMMENTS-SCREEN-READER.md).

## Audio/mobile checks included in preview.4

All twenty candidates passed native MP3/WAV playback, pause and seek checks at 375px and 320px, with focused retries retained in the evidence. Audio failure feedback and a 200px minimum player height were fixed; final narrow layouts/recovery passed all forty native cases. Reliable narrow-width YouTube playback remains unresolved after pauses/stalls. These fixes and evidence are included in preview.4; preview.3 ZIPs remain unchanged. See the [audio/mobile matrix](AUDIO-MOBILE.md) for exact scope, retries and remaining gates.
