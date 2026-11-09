# Final-three comment publishing follow-up

## Latest reliability follow-up — November 9, 13:11 UTC

All twenty themes received fresh-tab in-app and authenticated Safari comparisons. Recorded submissions persisted in 21/40 in-app cases and 29/40 Safari cases; the stock Blogger Simple Bold control also failed on a reply. Basic positive observations remain, but publishing reliability is still a release gate. Native Chrome control was unavailable. [Current matrix and evidence](COMMENT-RELIABILITY.md). Earlier sections retain their original scope and counts.


November 9, 2026, completed 12:37 UTC · [Public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/) · Frozen preview.5 XMLs from `e3e83b8b0ca5440a9e957b191ca6c6ab08056861`.

## Current result

**All twenty themes now have positive root-and-threaded-reply observations across sessions.** This closes the remaining basic publication rows; it does not close publishing reliability or establish a stable release. Earlier failures and retry outcomes remain in the [remaining-eight report](COMMENTS-REMAINING-EIGHT.md) and [sanitized final-three evidence](evidence/comments-final-three-2026-11-09.json).

| Theme | Root | Reply | This pass |
| --- | --- | --- | --- |
| Ledger | Persisted | Persisted under its new root | Both passed after reload |
| Screen | Persisted | Persisted under its new root after spaced retry | One unsent field replacement and one submitted reply failure retained |
| Launchpad | Earlier root retained | Persisted under its existing root | Reply target and persistence verified |

Five new QA comments/replies persisted. The photo-rich fixture increased from **29 to 34**, with each new test marker appearing exactly once. Together with ten comments/replies on the older article, the two checked fixtures contain 44. These totals describe the checked fixtures, not every comment on the blog.

## Investigation and scope

Each exact released template was installed through Blogger and its served body class verified. The native composer identified the expected article. Launchpad’s parent identifier matched its existing root; Screen’s matched its newly published root. The iframe retained its accessible name. Every pass required a reload and a persisted comment ID; replies additionally required the intended native ancestor thread.

The ten shared comment includables in Ledger, Screen and Launchpad serialize to identical SHA-256 hashes. Source inspection found no theme-specific comment-publishing override in their styles or shared runtime. This comparison and the correctly targeted successful submissions did not reproduce a template defect or explain the earlier intermittent errors. No theme XML/runtime, blog permission, post setting or frozen download asset changed.

Screen’s initial composer replacement cleared the entered value before submission. That was recorded as **unsent**, then prepared again. Its first actual reply submission returned **“Failed to publish comment. Please try again later.”** After source/target inspection, one spaced retry persisted under the correct root. Slower input or waiting is therefore not claimed as a permanent fix. No CAPTCHA challenge appeared, and the generic UI message does not establish a quota, account or provider-side cause.

The original hub was backed up and restored. Public status notices now distinguish completed basic publishing observations from unverified repeated-session/account/independent-browser reliability. Historical failures were not overwritten.

## Remaining release blockers

Review intermittent publishing reliability across sessions, accounts and independent browsers. Actual VoiceOver speech/rotor, measured live performance, fourteen photo-rich imports, intermittent YouTube/Vimeo reliability, physical devices/audible output/long sessions and final editorial approval remain open. See [release readiness](RELEASE-READINESS.md). Preview.5 remains a development prerelease.

Validation: XML/schema/source checks, all 61 regressions (zero failures or skips) and whitespace checks passed.
