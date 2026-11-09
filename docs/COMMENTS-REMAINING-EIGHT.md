# Remaining-eight comment publishing checks

## Latest reliability follow-up — November 9, 13:11 UTC

All twenty themes received fresh-tab in-app and authenticated Safari comparisons. Recorded submissions persisted in 21/40 in-app cases and 29/40 Safari cases; the stock Blogger Simple Bold control also failed on a reply. Basic positive observations remain, but publishing reliability is still a release gate. Native Chrome control was unavailable. [Current matrix and evidence](COMMENT-RELIABILITY.md). Earlier sections retain their original scope and counts.

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
