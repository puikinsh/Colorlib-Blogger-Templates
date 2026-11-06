# Comment publishing and screen-reader status

November 6, 2026 · Development preview acceptance

All twenty themes were installed sequentially on the dedicated [public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/). The installed body class was checked after each save; stale platform responses were refreshed before recording a result. Each theme was inspected on the native desktop article and its `?m=1` route. These route checks are not physical-device certification.

| Theme | Desktop comment view | Mobile route | New comment / reply publication | Actual screen-reader speech |
| --- | --- | --- | --- | --- |
| Saffron | Pass | Pass | Pass / pass | Blocked |
| Wayfarer | Pass | Pass | Pass / pass | Blocked |
| Lesson | Pass | Pass | Pass / blocked | Blocked |
| Bench | Pass | Pass | Retry failed / not reached | Blocked |
| Maker | Pass | Pass | Not attempted after failure | Blocked |
| Muse | Pass | Pass | Not attempted after failure | Blocked |
| Kinship | Pass | Pass | Not attempted after failure | Blocked |
| Companion | Pass | Pass | Not attempted after failure | Blocked |
| Shelf | Pass | Pass | Not attempted after failure | Blocked |
| Playbook | Pass | Pass | Not attempted after failure | Blocked |
| Soundboard | Pass | Pass | Not attempted after failure | Blocked |
| Verdant | Pass | Pass | Not attempted after failure | Blocked |
| Pace | Pass | Pass | Not attempted after failure | Blocked |
| Ledger | Pass | Pass | Not attempted after failure | Blocked |
| Screen | Pass | Pass | Not attempted after failure | Blocked |
| Borough | Pass | Pass | Not attempted after failure | Blocked |
| Studio | Pass | Pass | Not attempted after failure | Blocked |
| Launchpad | Pass | Pass | Not attempted after failure | Blocked |
| Ceremony | Pass | Pass | Not attempted after failure | Blocked |
| Cause | Pass | Pass | Not attempted after failure | Blocked |

## What passed

All forty comment views render the seven persisted lab comments/replies, retain the named comment region and H2 heading, give the composer iframe an accessible title, omit the internal relay link from the accessibility tree, and hide inactive native reply/load-more controls. Existing Saffron and Wayfarer replies remain attached to their parent threads across all twenty designs. Sampled DOM contrast/control-name checks found no failures. No raw Google RPC URLs or tokens are published with this report.

Saffron and Wayfarer each published a new top-level test comment and a threaded reply; both persisted after reload. Lesson's top-level comment also persisted. A baseline hub comment/reply succeeded before that matrix. Labels identify every test comment as release QA. These are deliberately retained test fixtures.

The earlier composer-expansion block was resolved by native click-and-type interaction. Programmatic input had not reliably expanded Blogger's controls; the theme was not changed to simulate publication. Wait for the expanded composer before typing, because Blogger can replace its initial textarea.

## Fixes and regression coverage

- Replaced level-four comment headings with a section H2 and form H3. The comment region is named only when its heading exists.
- Kept Blogger's required relay anchors in the DOM while hiding them from navigation and assistive technology.
- Labeled moderation iframes and replaced paragraph wrappers that contained block-level forms.
- Added the native `.hidden` state omitted when global Blogger CSS is disabled. Empty reply threads and inactive load-more controls no longer appear as unusable controls.
- Added responsive spacing for author/timestamp lines, actions, avatars and threaded replies, with wrapping for long comment text.

The shared comment CSS was also checked on actual published content at 320/375/768px with no horizontal overflow. Two new regressions check generated comment hooks and forty local comment-layout cases (twenty themes at 320/768px). The initial comment pass had **51 passing tests** (the later hub-link check brings the suite to 52); the existing 200 home/article viewport cases remain covered.

## Blocked checks

**Blogger publication:** Lesson's reply returned “Failed to publish comment. Please try again later.” One later retry returned the same message. Further posting attempts were stopped. No CAPTCHA challenge appeared. The failure's service-side cause is unknown; it is not established as a template defect, quota or permission problem. Publication/replies for the remaining seventeen themes are unverified, despite successful rendering of existing threads.

**Actual screen reader:** VoiceOver Utility opened with its caption panel already enabled, but native Chrome and Safari app connections timed out; the Codex native app is unavailable to computer-use control. VoiceOver was not enabled, no speech/rotor pass was performed, and no VoiceOver preference was changed. The utility was closed after inspection. Accessibility-tree and keyboard results must not be reported as a VoiceOver pass. This remains blocked for all twenty themes.

When a native browser/screen-reader connection is available, test headings/landmarks rotor navigation, one spoken logo/title, TOC targets, form labels, validation/status announcements and comment/reply entry. When Blogger publishing recovers, finish Lesson's reply and the remaining publication rows. Existing import, measured-performance, physical-device and editorial gates remain listed in [release readiness](RELEASE-READINESS.md).

## Published-package retry

The [latest retry report](BLOGGER-RETRY.md) records another failed Lesson reply and a failed new top-level Bench comment. All twenty released XML files were installed and their visible named comment forms and earlier persisted replies rechecked. Further publishing submissions stopped after those failures. The Saffron/Wayfarer publication passes were rechecked for persistence, not duplicated. No actual screen-reader speech pass is claimed.
