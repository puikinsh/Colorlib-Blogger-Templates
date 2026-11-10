# Release blocker follow-up — November 10, 2026

Tested the exact frozen preview.5 XMLs and exports; all forty input hashes match the staged release ZIPs. No theme runtime or published package changed. [Sanitized evidence](evidence/release-followup-2026-11-10.json).

## Comment publishing

**All twenty in-app root/reply pairs passed: 40/40 submissions persisted after reload.** Safari targeted every theme with a failure in the November 9 Safari matrix, plus Soundboard: all nine pairs passed (18/18 submissions). All replies were verified under their intended root after reload; Safari submissions were additionally checked in the in-app browser. The fixture rose from 85 to 143 comments.

These are sequential observations, not an estimated field success rate. Both browsers used the same lab account; the in-app login was retained, and Safari reused its earlier independently authenticated session. Safari repeatedly required its native Google sign-in button to re-establish the embedded composer. No credentials were re-entered or global privacy setting changed.

| Theme | In-app root / reply | Safari root / reply |
| --- | --- | --- |
| Saffron | Passed / Passed | Not repeated this pass |
| Wayfarer | Passed / Passed | Not repeated this pass |
| Lesson | Passed / Passed | Not repeated this pass |
| Bench | Passed / Passed | Not repeated this pass |
| Maker | Passed / Passed | Not repeated this pass |
| Muse | Passed / Passed | Not repeated this pass |
| Kinship | Passed / Passed | Not repeated this pass |
| Companion | Passed / Passed | Not repeated this pass |
| Shelf | Passed / Passed | Passed / Passed |
| Playbook | Passed / Passed | Not repeated this pass |
| Soundboard | Passed / Passed | Passed / Passed |
| Verdant | Passed / Passed | Passed / Passed |
| Pace | Passed / Passed | Passed / Passed |
| Ledger | Passed / Passed | Not repeated this pass |
| Screen | Passed / Passed | Passed / Passed |
| Borough | Passed / Passed | Passed / Passed |
| Studio | Passed / Passed | Not repeated this pass |
| Launchpad | Passed / Passed | Passed / Passed |
| Ceremony | Passed / Passed | Passed / Passed |
| Cause | Passed / Passed | Passed / Passed |

Earlier 21/40 in-app and 29/40 Safari runs, and the stock Blogger reply failure, remain in [the reliability report](COMMENT-RELIABILITY.md). Today did not reproduce those publishing failures or establish a permanent fix. Independent-account, further-session, full twenty-theme Safari repeat and additional-browser reliability remain open. Browser/iframe hydration interruptions were resolved before submission and are excluded from publishing denominators.

## Demo imports and mobile images

**Six additional exports passed:** Shelf, Playbook, Soundboard, Verdant, Pace and Ledger, twelve stories each. Public Atom-feed verification checked every expected title/label, three responsive images, dimensions/srcset, photo-pair section and three credit URLs. The lab now has **173 public posts, including 144 photo-rich posts from twelve accepted updated exports**.

Screen then returned “Seems like you tried to import too many times. Please try again later.” The queue stopped. **Eight updated exports remain unverified:** Saffron, Wayfarer, Screen, Borough, Studio, Launchpad, Ceremony and Cause. Historical Saffron/Wayfarer imports cover older content. No new blog/account, fixture deletion or timestamp change was used to evade the limit.

All 72 newly accepted stories passed under their own installed themes at 320px: 216 photos decoded, responsive small variants were selected, and no horizontal overflow occurred. Previous-theme responses after switches were refreshed before acceptance. One Soundboard article returned Blogger “Service Unavailable / Error 503”; its later retry recovered. Both initial response and successful retry are retained. This was a transient service observation, not a reproduced template defect. Together with the earlier 72-story pass, all 144 accepted photo-rich stories have own-theme 320px observations.

## Remaining release gates

Keep the eight imports, independent-account/further-session comment reliability, actual screen-reader speech/rotor, measured live performance, media/device/audible-output/long-session and editorial acceptance open. Instrumented performance tools remain unavailable; no measured score is claimed. Recipes remain untested. Static screenshots and previews remain distinct from finished native Blogger demos.

The public Lab and Colorlib roundup disclose this progress and remaining gaps. Preview.5 stays a development prerelease; its download bytes are unchanged.
