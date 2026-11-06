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
- **Comment publishing:** complete Lesson's reply and independent publication/reply checks for the other seventeen themes in a working Blogger session. The service's failure cause is unknown. No CAPTCHA challenge appeared in the completed attempts.
- **Complete demo imports:** Blogger refused further imports after four posts; the owner chose to retain the existing lab fixtures. All twenty complete demo exports still need clean import acceptance.
- **Live performance:** DevTools was unavailable; the owner chose to document the gap. No measured live Core Web Vitals or Lighthouse score is claimed.
- Physical-device review, third-party player playback/failure checks and coherent per-theme editorial acceptance remain open. Recipe samples have not been kitchen-tested.

Blogger's native timestamp cursor can skip a post when identical publication times straddle a pagination boundary. Keep demonstration publication timestamps distinct and verify page-size changes. The theme preserves native navigation URLs.

## Package integrity and publication

The normal gallery ZIPs are mutable development previews. `tools/stage_release.py --version 0.1.0-preview.2` stages a separate set from a clean source commit, pins demo artwork URLs to that commit and writes SHA256SUMS, a manifest and release notes. Each ZIP includes this status file. Verify with `shasum -a 256 -c SHA256SUMS` (or `sha256sum -c SHA256SUMS` on Linux).

A staged/draft preview is not a production release. Do not mark it production-ready or replace Colorlib production downloads until the outstanding acceptance checks pass. Current reports: [platform validation](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/PLATFORM-VALIDATION.md) and [comment/screen-reader checks](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/codex/collection-preview/docs/COMMENTS-SCREEN-READER.md).
