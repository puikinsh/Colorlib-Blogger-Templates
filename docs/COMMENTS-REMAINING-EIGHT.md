# Remaining-eight comment publishing checks

## Latest final-three follow-up — November 9, 12:37 UTC

Ledger and Screen’s root/reply pairs and Launchpad’s reply persisted, including a recorded Screen failure and successful spaced retry. All twenty themes now have positive paired observations across sessions; no basic publication row remains incomplete. Intermittent publishing reliability and all other stable-release gates remain open. [Current report and retained evidence](COMMENTS-FINAL-THREE.md). Earlier sections retain their original scope and counts.


November 9, 2026, completed 12:22 UTC · [Public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/) · Exact frozen preview.5 XMLs from `e3e83b8b0ca5440a9e957b191ca6c6ab08056861`.

## Results at 12:22 UTC

Each of the eight released themes was installed and its served body class verified. Root comments and replies were submitted through the native composer; a pass requires persistence after reload, and replies must remain under their intended root. The hub was backed up and restored. Initial failures, unsent preparation failures and bounded retries are recorded separately in the [sanitized evidence](evidence/comments-remaining-eight-2026-11-09.json).

| Theme | Root comment | Threaded reply | Retained initial/retry result |
| --- | --- | --- | --- |
| Pace | Persisted | Persisted on retry | Initial reply failed |
| Ledger | Failed twice | Not reached | Both submitted roots returned the generic publish error |
| Screen | Failed twice | Not reached | Initial and staged submitted roots failed |
| Borough | Persisted | Persisted | First pair passed |
| Studio | Persisted | Persisted on retry | Initial reply failed |
| Launchpad | Persisted | Failed twice | Both submitted replies failed |
| Ceremony | Persisted on staged retry | Persisted | Initial submitted root failed |
| Cause | Persisted on staged retry | Persisted | Initial submitted root failed |

Five of the eight now have positive root/reply observations; Launchpad remains partial, while Ledger/Screen remain blocked at root publication. Combined with previous results, **seventeen of twenty themes have positive paired observations across sessions**. These are capability observations, not a reliability guarantee. **Three complete publication rows remained open in that pass: Ledger, Screen and Launchpad.**

## Bench’s older-post investigation

On the older text-only article, Blogger’s native post editor showed **Reader comments → Allow** selected, with Update disabled. The public composer’s post identifier matched that article, its iframe was named, and eight existing comments/replies were present. No post or blog setting was changed.

Under the exact released Bench XML, a fresh root comment and a correctly nested reply both published and persisted after reload. That article now contains ten comments/replies. This recovers the previously failed older-post capability check. It does not establish why the earlier submissions failed or prove that future attempts will be reliable. No theme-source fix or lasting permission fault was established.

## Publication totals and input synchronization

Thirteen new QA comments/replies persisted in this pass: eleven on the shared photo-rich article and the two Bench older-post checks. The fixtures increased from **18 + 8 to 29 + 10 comments/replies**. Test labels are intentionally retained publicly.

Blogger can replace its initial textarea as the composer expands. Unsent drafts whose value disappeared were recorded as preparation failures, not failed publications. Staged retries separated expansion from verified text entry and submission. Native text entry and staged input still produced genuine publish failures for Ledger, Screen and Launchpad, so slower interaction alone is not a demonstrated fix. The UI returned **“Failed to publish comment. Please try again later.”** No CAPTCHA challenge appeared, and no quota, account or template cause was established.

## Remaining release blockers

Complete Ledger/Screen root-and-reply and Launchpad’s reply checks, then review repeated-session/account/browser reliability while retaining initial failures and recoveries. Actual VoiceOver speech/rotor, measured live performance, fourteen photo-rich imports, intermittent YouTube/Vimeo reliability, physical devices/audible output/long sessions and final editorial approval remain open. See [release readiness](RELEASE-READINESS.md) and the [earlier accessibility matrix](ACCESSIBILITY-COMMENTS-FOLLOWUP.md).

XML/schema/source checks, all 61 regressions (zero failures or skips) and whitespace validation passed. No product XML, shared runtime or frozen preview.5 asset was changed. Documentation, evidence and both Labs’ status notices were updated; existing twenty downloads and forty screenshot links are retained.
