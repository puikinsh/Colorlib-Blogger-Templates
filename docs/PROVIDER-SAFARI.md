# Supported-browser provider follow-up

Tested November 8, 2026 against source `4534b3d2d51fba74b975874d37cbf2f01ba9cd3c`. [Sanitized evidence and candidate hashes](evidence/provider-safari-2026-11-08.json) supplement the [earlier IAB investigation](PROVIDER-RELIABILITY.md). Runtime/CSS and published preview.4 assets are unchanged. These observations are newer than the reports bundled in preview.4.

## Scope and method

Native Safari **27.2 (22625.2.8.11.9)** was verified through About Safari. Safari is among [Vimeo's supported browsers](https://help.vimeo.com/hc/en-us/articles/12425777758609-System-Requirements-for-viewing-browsing-and-apps). Chrome control still timed out; it was not tested.

Each full XML was installed through Blogger's Theme editor. The served theme class was verified in IAB, then the same public fixture was reloaded in Safari. Safari's native desktop window was used; its DOM class and narrow viewport were not instrumented. Native accessibility controls supplied elapsed time and Play/Pause state, not DOM `readyState` or a network trace.

Each theme received two YouTube load/play/close cycles and one Vimeo cycle. Samples were taken immediately and about five seconds later; a positive timeline plus Pause control was required. Close removed the player controls and returned focus to Load. Initial control-targeting errors and a batch timeout were recovered separately from playback failures; retained evidence explains Bench's recovered observations. No browser security, codec, autoplay or provider API setting was changed.

## Results and retries

YouTube advanced in **36/40 initial cycles**. Shelf and Playbook paused near one/two seconds in both cycles. Vimeo advanced in **18/20 initial theme checks**: Companion remained at zero in its initial sample; Shelf paused near one second. Companion's extended reload/resume attempts also paused near one/two seconds. No supported-browser error appeared in these Safari observations.

Full focused retries of Companion, Shelf and Playbook, with Safari explicitly foregrounded before reload, all advanced: six YouTube cycles and three Vimeo checks. Original failures remain. This does not establish that foregrounding caused the recovery.

| Theme | Initial YouTube cycles | Initial Vimeo check |
| --- | --- | --- |
| Saffron | Advanced twice | Advanced |
| Wayfarer | Advanced twice | Advanced |
| Lesson | Advanced twice | Advanced |
| Bench | Advanced twice | Advanced |
| Maker | Advanced twice | Advanced |
| Muse | Advanced twice | Advanced |
| Kinship | Advanced twice | Advanced |
| Companion | Advanced twice | Incomplete/paused; focused retry advanced |
| Shelf | Paused; focused retry advanced twice | Incomplete/paused; focused retry advanced |
| Playbook | Paused; focused retry advanced twice | Advanced |
| Soundboard | Advanced twice | Advanced |
| Verdant | Advanced twice | Advanced |
| Pace | Advanced twice | Advanced |
| Ledger | Advanced twice | Advanced |
| Screen | Advanced twice | Advanced |
| Borough | Advanced twice | Advanced |
| Studio | Advanced twice | Advanced |
| Launchpad | Advanced twice | Advanced |
| Ceremony | Advanced twice | Advanced |
| Cause | Advanced twice | Advanced |

Standalone Vimeo initially advanced beyond 26 seconds in Safari. A later fresh standalone tab paused near one second, reproducing an interruption without Blogger or the shared runtime. Bench's recovered embedded player advanced from 14 to 35 seconds. These observations narrow the investigation but do not establish the cause of the pauses or the earlier IAB buffering.

## Findings and release boundary

No new template-specific defect or safe, evidence-backed runtime correction was confirmed. All twenty now have positive supported-browser observations after recorded retries, but reliable repeated-session playback is **not passed**. IAB's Vimeo supported-browser failure remains unresolved. A visible iframe or a Pause button at time zero still does not count as playback.

Next checks require independently instrumented Chrome/Firefox, network/player diagnostics during a reproduced interruption, sustained sessions and native narrow/physical-device checks. Actual audible output, captions/transcripts, fullscreen/PiP and owner-specific private/regional recordings remain unverified. Screen-reader speech/rotor, measured performance, Blogger import/comment service limits and editorial approval are unchanged; see [release readiness](RELEASE-READINESS.md).

The live hub was restored with the clarified Safari/IAB notice and a link to this report. All twenty preview.4 download destinations were checked against the catalog. Twenty local development ZIPs include the new report/evidence; XML/source/link checks, whitespace checks and all 58 automated regressions passed. Published preview.4 assets were not replaced.
