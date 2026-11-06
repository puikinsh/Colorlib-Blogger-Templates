# Development preview release status

Updated November 6, 2026. These packages are prepared for development testing, not production acceptance. They are not replacements for the nine separately maintained Colorlib Blogger releases.

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
- **Media/editorial:** all twenty local previews passed YouTube playback and shared recovery checks; Vimeo returned a supported-browser error. All twenty revised XMLs also passed native Blogger YouTube playback/recovery on the ordinary and `?m=1` routes at 1280px; see the [native media matrix](NATIVE-MEDIA.md). Vimeo, audible output, narrow/device/provider acceptance and final editorial approval remain open. All 240 samples are explicitly editing briefs; recipes remain untested. See the [media/editorial review](MEDIA-EDITORIAL-REVIEW.md).

Blogger's native timestamp cursor can skip a post when identical publication times straddle a pagination boundary. Keep demonstration publication timestamps distinct and verify page-size changes. The theme preserves native navigation URLs.

## Latest retry

The [published-package retry](BLOGGER-RETRY.md) records 24 accepted demo posts, the repeated import limit, the Lesson/Bench publish failures and current comment-form checks across all twenty released templates. These partial results do not close the stable-release gates above.

## Published preview

[v0.1.0-preview.3](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.3) is published as a development prerelease. Its twenty ZIPs, release notes, manifest and checksums are frozen from commit `adf4ded8b81b79a7275b8d57431fa47dcbb34ff0`. They include media recovery, editorial corrections, offline documentation and the native-media evidence. The Blogger/static hub download buttons point to these exact packages and display the incomplete checks before the cards. Publishing the preview does not close any acceptance gate above.

Preview.2 remains available unchanged from commit `a672d7a1bca99d776f66322deead9d7ececf80c4`. Embedded package status files record their preparation-time state; this page and the release description carry the current publication status.

## Package integrity and publication

The normal gallery ZIPs are mutable development previews. `tools/stage_release.py --version 0.1.0-preview.4` stages a separate set from a clean source commit, pins demo artwork URLs to that commit and writes SHA256SUMS, a manifest and release notes. Each ZIP includes this status file. Verify with `shasum -a 256 -c SHA256SUMS` (or `sha256sum -c SHA256SUMS` on Linux).

A published preview is not a production release. Do not mark it production-ready or replace Colorlib production downloads until the outstanding acceptance checks pass. Current reports: [platform validation](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/PLATFORM-VALIDATION.md) and [comment/screen-reader checks](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/COMMENTS-SCREEN-READER.md).
