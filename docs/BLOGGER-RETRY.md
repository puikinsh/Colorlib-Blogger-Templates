# Blogger import and publishing retry

November 6, 2026 · Published release `v0.1.0-preview.2`

The retry used the XML and demo exports extracted from the published, checksummed preview ZIPs. The original hub was backed up before installing the released themes; it is restored after testing. Published package assets remain frozen.

## Results for all twenty templates

| Theme | Full demo export import | Released comment view/form | Publishing/reply retry |
| --- | --- | --- | --- |
| Saffron | 12/12 accepted | Pass | Earlier pass; persistence rechecked |
| Wayfarer | 12/12 accepted | Pass | Earlier pass; persistence rechecked |
| Lesson | Attempt limit; later retry also refused | Pass | Existing top-level post; reply retry failed |
| Bench | Queue stopped at import limit | Pass | New-comment retry failed |
| Maker | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Muse | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Kinship | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Companion | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Shelf | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Playbook | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Soundboard | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Verdant | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Pace | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Ledger | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Screen | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Borough | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Studio | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Launchpad | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Ceremony | Queue stopped at import limit | Pass | Not retried after repeated publish failures |
| Cause | Queue stopped at import limit | Pass | Not retried after repeated publish failures |

## Import progress

Saffron and Wayfarer each added all twelve posts to the existing shared lab. The published count increased from 4 to 16, then 28. The blog's advertised public Atom feed independently confirmed all 24 imported titles, labels, publication timestamps, feature blocks and commit-pinned image URLs. These were merges into an existing blog, not isolated empty-blog tests.

The first and last imported articles from both themes also passed native rendered checks: correct title, loaded artwork, article format, contents links and BlogPosting metadata. Saffron's imported recipes additionally produced valid Recipe metadata.

Lesson's import was refused with **“Seems like you tried to import too many times. Please try again later.”** One later retry, after independent comment checks, returned the same refusal. The count stayed at 28. The reset interval was not provided. The other seventeen imports were not attempted after that shared import gate. Two complete exports are accepted; the remaining eighteen still require acceptance.

Import processing is asynchronous. A closed upload dialog or an initial timeout does not establish success/failure; post counts and imported content were checked before recording results or considering another upload.

## Publishing retry

Lesson's previously failed reply was retried under its released template and returned **“Failed to publish comment. Please try again later.”** The iframe's parent identifier matched the existing Lesson comment. A new top-level comment under the released Bench template returned the same failure. No CAPTCHA challenge appeared. The cause remains unknown; the UI does not establish a template defect, session problem or comment quota.

Further submissions stopped after failures in those two distinct flows. The failed drafts were not counted as published comments. All twenty released themes were then checked for the visible named composer and persisted comment/reply rendering. The seven earlier comments remain, including the successful Saffron/Wayfarer threads. Rendering/form availability is not a publishing pass for the other themes.

A native Chrome connection was also attempted for independent browser reproduction, but it timed out. No independent-browser publication result is claimed.

## What still blocks a stable release

1. Accept the remaining eighteen full demo exports after Blogger's import attempt limit clears.
2. Complete Lesson's reply and new-comment/reply acceptance for the other seventeen themes, including Bench. Earlier Saffron/Wayfarer passes remain valid; they were not reposted during this retry.
3. Complete actual screen-reader speech/rotor checks. The prior native browser connection problem remains; accessibility-tree checks do not replace this gate.
4. Measure live performance when DevTools is available. No live Core Web Vitals or Lighthouse scores are claimed.
5. Finish physical-device, third-party media playback/failure and per-theme editorial review. Recipe samples still require kitchen testing before factual recipe publication.

No additional template defect was reproduced during this retry. The existing timestamp-cursor limitation remains documented: publication timestamps shared across imported collections can straddle a native pagination boundary. Individual packaged exports already use distinct publication dates within each theme.

See [release readiness](RELEASE-READINESS.md), [the earlier comment/screen-reader matrix](COMMENTS-SCREEN-READER.md) and [platform validation](PLATFORM-VALIDATION.md). The public hub should show these partial results and the remaining gates before downloads.
