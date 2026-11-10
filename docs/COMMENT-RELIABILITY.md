# Comment publishing reliability

November 9, 2026, completed 13:11 UTC · [Public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/) · Exact frozen preview.5 XMLs.

## November 10 follow-up

All twenty in-app pairs passed (40/40 submissions persisted). Targeted native Safari pairs passed for all eight previously failing Safari themes plus Soundboard (18/18). Earlier failures remain retained below; no permanent cause/fix was established. Independent-account, further-session, full Safari repeat and additional-browser reliability remain open. [New matrix, import progress and evidence](RELEASE-FOLLOWUP-2026-11-10.md).

## November 9 release status

Earlier basic root/reply observations remain positive for all twenty themes. **Repeat-visit and cross-browser reliability remains open.** This pass reproduced explicit publication errors in both tested browsers and Blogger’s own stock theme; no collection-specific defect or permanent fix was established. Published preview.5 files remain unchanged.

| Recorded submissions | Persisted after reload | Explicit publish errors | Complete root/reply pairs |
| --- | ---: | ---: | ---: |
| In-app browser, fresh tabs under existing login | 21 / 40 | 19 | 5 / 20 |
| Native Safari, independently signed-in session | 29 / 40 | 11 | 12 / 20 |
| Stock Blogger Simple Bold control, in-app browser | 1 / 2 | 1 | 0 / 1 |

These are sequential observations, not a reliability benchmark or field success rate. The same lab account was used; no independent-account pass is claimed. Native Chrome’s app connection timed out, so Chrome publication remains untested. [Sanitized attempts, preparations, IDs and counts](evidence/comment-reliability-2026-11-09.json).

## Twenty-theme matrix

Each theme’s served body class was verified. Safari additionally showed the theme’s distinct footer. Every pass required persistence after reload; Safari submissions were verified in the other browser. Replies required the intended native ancestor thread.

| Theme | In-app root / reply | Safari root / reply |
| --- | --- | --- |
| Saffron | Persisted / Persisted | Persisted / Persisted |
| Wayfarer | Publish error / Publish error | Persisted / Persisted |
| Lesson | Persisted / Publish error | Persisted / Persisted |
| Bench | Publish error / Persisted (control) | Persisted / Persisted |
| Maker | Persisted / Persisted | Persisted / Persisted |
| Muse | Publish error / Persisted (control) | Persisted / Persisted |
| Kinship | Persisted / Persisted | Persisted / Persisted |
| Companion | Publish error / Persisted (control) | Persisted / Persisted |
| Shelf | Persisted / Persisted | Persisted / Publish error |
| Playbook | Publish error / Publish error | Persisted / Persisted |
| Soundboard | Publish error / Persisted (control) | Persisted / Persisted |
| Verdant | Publish error / Publish error | Persisted / Publish error |
| Pace | Publish error / Persisted (control) | Publish error / Publish error |
| Ledger | Persisted / Publish error | Persisted / Persisted |
| Screen | Publish error / Persisted (control) | Persisted / Publish error |
| Borough | Persisted / Publish error | Persisted / Publish error |
| Studio | Persisted / Publish error | Persisted / Persisted |
| Launchpad | Publish error / Publish error | Publish error / Persisted (control) |
| Ceremony | Persisted / Persisted | Publish error / Publish error |
| Cause | Publish error / Persisted (control) | Publish error / Publish error |

**Control** means the new root failed, so the reply was tested under an existing published Maker fixture root. Such replies are separate capability checks, not successful newly paired submissions. Originally unsent preparations were completed in a separate phase; their initial outcomes remain in the evidence.

## What the investigation established

All twenty in-app visits used new tabs/newly loaded composers under the existing login. This does not create twenty independent authentication sessions. An interrupted Lesson visit was recorded as browser-control interruption, excluded from publication denominators, then rerun.

Safari initially needed owner sign-in, then Blogger’s **Allow cookies** and site-specific storage prompt. After navigation, its native **Sign in with Google** button could re-establish the composer without another credential entry. No global privacy protection was disabled. Waiting for an expanded form and verifying the entered value prevented unsent drafts from being counted as publication failures, but did not eliminate actual errors.

The native UI returned **“Failed to publish comment. Please try again later.”** Failed texts were absent after reload. The same error occurred on Blogger’s stock **Simple Bold**: its root persisted and its reply failed. That control demonstrates the symptom outside this collection; it does not identify a quota, account, browser or service mechanism. No CAPTCHA challenge appeared.

The photo-rich fixture increased from **34 to 85 comments/replies**: 21 in-app, 29 Safari and one stock-control root. Earlier comment fixtures remain. Initial failures were retained; no automatic product retry or speculative source change was added.

## Lab state and remaining gates

The stock theme was temporary. The original hub was restored through Blogger’s Restore workflow after an editor save gave no result; a fresh editor then handled later theme installations. Twenty download cards and forty screenshot links are retained. Owner troubleshooting now covers the observed sign-in/cookie and textarea prerequisites.

Continue repeated-session, independent-account and additional-browser reliability review. Actual screen-reader speech/rotor, measured live performance, fourteen photo-rich imports, intermittent YouTube/Vimeo reliability, physical devices/audible output/long sessions and editorial acceptance remain open. [Release readiness](RELEASE-READINESS.md).

Validation: XML/schema/source checks, all 61 regressions (zero failures or skips) and whitespace checks passed.
