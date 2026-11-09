# Accessibility, comments and performance follow-up

November 9, 2026 · Frozen preview.5 XMLs · [Public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/)

## Current matrix

All twenty released XMLs were installed sequentially. Public body classes were verified after saves, including refreshed stale responses. The hub was backed up and restored; screenshots/downloads and the fourteen-import gap are retained. No theme-source defect was reproduced and no published package changed. XML/schema/source checks and all 61 regressions passed (zero failures or skips).

| Theme | Native keyboard/DOM | Root / reply publication | VoiceOver speech/rotor | Live performance |
| --- | --- | --- | --- | --- |
| Saffron | Pass (3 views) | Earlier root/reply pass retained | Unverified | Unmeasured |
| Wayfarer | Pass (3 views) | Earlier root/reply pass retained | Unverified | Unmeasured |
| Lesson | Pass (3 views) | Earlier root; new reply persisted | Unverified | Unmeasured |
| Bench | Pass (3 views) | New root/reply persisted; legacy root failed | Unverified | Unmeasured |
| Maker | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Muse | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Kinship | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Companion | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Shelf | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Playbook | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Soundboard | Pass (3 views) | New root/reply persisted | Unverified | Unmeasured |
| Verdant | Pass (3 views) | New root persisted; reply failed | Unverified | Unmeasured |
| Pace | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Ledger | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Screen | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Borough | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Studio | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Launchpad | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Ceremony | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |
| Cause | Pass (3 views) | Not submitted after renewed failure | Unverified | Unmeasured |

## Native accessibility observations

**60 native 375px cases** cover each theme’s homepage, photo-rich article and older text-only article on `?m=1`. All twenty skip links received a visible solid outline and Enter focused `main-content`. All forty article TOCs resolved every target. Each document had one H1 and one main landmark; sampled leaf-text contrast and visible control names had no failures. Rendered outer iframes were named, photo alt attributes were present, and no horizontal overflow appeared. Photo-rich comment views rendered seventeen persisted comments/replies; legacy views rendered eight. These checks exclude iframe-internal contrast, artwork compositing, untested interactions and full accessibility conformance. [Sanitized evidence](evidence/accessibility-comments-2026-11-09.json).

Native Safari is available again. System Settings confirmed VoiceOver initially off, then on during the attempt. Its application connection timed out; no reliable speech/caption or rotor output was verified. VoiceOver was restored to **off**, the temporary Safari tab was closed, and no VoiceOver Utility preference changed. Actual screen-reader verification remains open for all twenty; the earlier statement that Safari itself is unavailable is no longer current.

## Comment publishing progress and renewed failure

Lesson’s previously failed reply published and persisted under its existing parent. Maker, Bench, Muse, Kinship, Companion, Shelf, Playbook and Soundboard each published a root and correctly nested reply on a shared photo-rich article; every submission was checked after reload. Together with earlier Saffron/Wayfarer passes and Lesson’s earlier root, **eleven themes now have positive root/reply observations**. These are capability observations, not a reliability guarantee across all posts, browsers or accounts.

Bench’s root retry on the old text-only article still returned **“Failed to publish comment. Please try again later.”** The same theme succeeded on the photo-rich fixture. Verdant later published its root, but its reply returned that same error. Submissions stopped there; Pace, Ledger, Screen, Borough, Studio, Launchpad, Ceremony and Cause remain unverified for publication/replies. No CAPTCHA challenge appeared; the normal reCAPTCHA privacy notice is not a challenge. No quota, permission or template cause is established by this generic error.

Eighteen new QA comments/replies persisted: one Lesson reply, sixteen paired submissions and one Verdant root. Together with seven earlier fixtures, the two checked articles now contain 25 comments/replies. Test labels are retained publicly; no provider RPC URL, session token or draft is presented as proof of publication.

Blogger replaces its initial textarea when expanding the composer. Native activation was followed by waiting for expanded controls and confirming the entered value before Publish. A replaced/empty field was corrected before submission; this was an automation synchronization issue, not a reproduced theme defect. Reply placement was checked through the native ancestor thread, which may include an additional Blogger wrapper.

## Performance scope

Chrome DevTools MCP is still absent from the available tools. The owner previously chose to document that gap. No live performance trace, LCP, INP, CLS, TBT or Lighthouse score is claimed. All twenty retain measured-performance acceptance gates.

A fresh source inventory records per-theme XML/CSS, separately gzipped CSS/runtime and bundled photo bytes. Source inspection confirms system fonts, inline theme styles/runtime, explicit photo dimensions/srcset and lazy secondary photos; it does not establish transfer size, critical-path timing or field performance. No unmeasured speed-up claim or speculative dependency removal was made. The inventory in the evidence supersedes the November 6 source-size figures, whose photo-rich source has since changed.

## Remaining release gates

Finish Verdant’s reply and the eight untested publishing/reply rows; investigate Bench’s old-fixture failure and repeated-session reliability. Complete actual screen-reader speech/rotor, measured performance, fourteen photo-rich imports, intermittent YouTube/Vimeo reliability, physical devices, audible output/long sessions and final editorial approval. [Release readiness](RELEASE-READINESS.md). Preview.5 assets remain frozen.
