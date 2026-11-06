# Blogger platform validation

November 6, 2026 · 0.1.0 development collection

[Public test lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/) · [Development source](https://github.com/puikinsh/Colorlib-Blogger-Templates)

All twenty generated theme XML files were installed through Blogger's native editor and checked sequentially on the same dedicated blog. The final lab uses a separate shadcn-inspired catalog hub. This is platform validation, not twenty independent production demos.

## Recorded matrix

Each desktop pass covers nine views: homepage, native Older page, native Newer return, component article, static page, Unicode label, native search, no-result search and missing page. Each mobile pass covers four actual Blogger pages at 320/375px: homepage, component article, text-only article and static page; the latter three use `?m=1`. Narrow checks embed the public pages in sized review frames; they are not static HTML emulation or physical-device certification.

| Theme | Desktop (9) | Narrow (4) |
| --- | --- | --- |
| Saffron | Pass | Pass |
| Wayfarer | Pass | Pass |
| Lesson | Pass | Pass |
| Bench | Pass | Pass |
| Maker | Pass | Pass |
| Muse | Pass | Pass |
| Kinship | Pass | Pass |
| Companion | Pass | Pass |
| Shelf | Pass | Pass |
| Playbook | Pass | Pass |
| Soundboard | Pass | Pass |
| Verdant | Pass | Pass |
| Pace | Pass | Pass |
| Ledger | Pass | Pass |
| Screen | Pass | Pass |
| Borough | Pass | Pass |
| Studio | Pass | Pass |
| Launchpad | Pass | Pass |
| Ceremony | Pass | Pass |
| Cause | Pass | Pass |

**Total: 180 desktop and 80 narrow view checks.** Assertions cover installed theme identity, one H1, canonical URLs, appropriate Open Graph type, parseable JSON-LD, unique IDs, TOC targets and horizontal overflow. Native two-post pagination visits all four posts without overlap and returns to the original pair. Article UI checks exercise recipe checkbox/reset and budget subtraction (100 − 250 = −150.00).

Four published posts and one static page supply the fixtures. One article contains all twenty niche feature blocks and 54 contents headings; another has Unicode/quotes and no image or labels. Text-only BlogPosting markup omits image; static pages omit BlogPosting and bylines. Original public artwork loads successfully. The empty-home state was also checked on all twenty themes before posts were published.

## Platform fixes

- Set root `b:responsive='true'`; without it Blogger substituted its built-in mobile theme on `?m=1`.
- Removed duplicate empty messages, the empty latest-post heading on one-post homes and empty topic footers.
- Added article/website Open Graph type and accessible native comment iframe titles.
- Constrained long contents lists so navigation remains usable on phones.
- Corrected demo export post-kind and label schemes, archive feed IDs and bounded post identifiers. Automated validation now checks these semantics.

## Limits and remaining release gates

- **Complete demo imports:** Blogger imported four posts, then refused further imports with “You are not allowed to import content to this blog. Please contact the blog admin.” The owner chose to continue with these fixtures. All twenty full twelve-post packaged exports still need successful clean imports; the service's exact refusal cause is unknown. Corrected source format alone does not establish import acceptance.
- **Native timestamp cursor:** at one post per page, posts sharing an identical publication timestamp can be skipped across a page boundary. The same native behavior was observed independently of theme navigation. Two posts per page keeps the tied pair together and passes the fixture round trip. Future lab exports stagger timestamps; no guessed feed-cursor workaround was added.
- **Comments:** native input now expands the composer. Saffron and Wayfarer publication/replies passed; Lesson’s top-level post passed, but its reply failed twice in Blogger. Further publication checks were stopped; moderation remains unverified. All twenty themes passed comment rendering on desktop/mobile routes. See the [follow-up matrix](COMMENTS-SCREEN-READER.md).
- **Owner controls:** the native edit pass is now complete for all twenty templates; scope and representative shared-control checks are in the [owner/accessibility review](OWNER-ACCESSIBILITY-REVIEW.md).
- **Production acceptance:** finish coherent per-theme demo editing, keyboard/screen-reader review, physical-device checks, measured live performance and optional media failure checks. Recipe samples have not been kitchen-tested. This report is not rich-result eligibility certification.

The four-post lab and public source support further testing without replacing any existing Colorlib production demo or download. Create a versioned production release only after the remaining gates pass.

## References and reproduction

Run `python3 tools/build.py --packages`, `python3 tools/check.py` and `node --test tests/*.test.cjs`. The automated suite has 51 passing tests, including 200 local home/article viewport cases; these are separate from the 260 native view checks above. `tools/lab_fixture.py` prepares a separate, ignored lab archive after a build; do not import it into a production blog.

Blogger documents [backup/import workflows and daily limits](https://support.google.com/blogger/answer/41387?hl=en) and [custom mobile templates](https://blogger.googleblog.com/2011/11/introducing-custom-mobile-templates.html). Google's [mobile indexing guidance](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) informs mobile metadata parity checks. Platform observations above are our own results, not guarantees from those documents.

## Follow-up review

All twenty templates passed native owner edits and live skip-link checks, with 40 additional home/article DOM audits. Shared fixes include usable Theme Designer groups, correct logo/description handling, named fallback links and broader focus styles. See the [detailed review](OWNER-ACCESSIBILITY-REVIEW.md) for limits. Live performance remains unmeasured at the owner's request because the required DevTools connection was unavailable.
