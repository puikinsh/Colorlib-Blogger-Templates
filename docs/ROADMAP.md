# Colorlib Blogger expansion: implementation roadmap

Prepared November 5, 2026. The user approved implementation of all twenty themes on November 5, 2026. Batch order and release acceptance gates remain in force; this is not a validated search-volume ranking. Working names need availability checks before release. Semrush keyword-volume research was unavailable because the connected account lacked API units; demand and revenue estimates are intentionally omitted.

## Positioning

The current nine templates mostly cover magazines/news, personal writing and photography. Expand into task-specific publishing: recipes, lessons, reviews, guides, projects, episodes and community updates. Each new theme should change the information hierarchy and post experience, with its own demo content and documentation. A palette/font change alone does not count as another template.

Twenty themes can cover a broad editorial market, not every website business model. Treat checkout, bookings, donations, memberships, email delivery and course access as clearly documented external integrations. Blogger's [API resources](https://developers.google.com/blogger/docs/3.0/reference) center on blogs, posts, pages and comments; a theme should not imply that it adds those transactional systems.

## Proposed catalog and delivery order

Batch order reflects gaps in our catalog and distinct technical patterns, not measured keyword popularity. Four themes per batch make it possible to validate the shared core before multiplying maintenance work.

| Batch | Working name | Audience/use case | Distinct layout and useful feature |
| --- | --- | --- | --- |
| 1 | Saffron | Food and recipes | Recipe index, compact cooking metadata, jump-to-recipe, print view and ingredient checklists |
| 1 | Wayfarer | Destination and travel guides | Destination-first navigation, itinerary sections, practical-info cards and optional external map links |
| 1 | Lesson | Teachers, tutorials and learning resources | Ordered learning paths, lesson TOC, prerequisites, exercises and printable/downloadable resource links |
| 1 | Bench | Technology and product reviewers | Specification tables, pros/cons, clearly attributed review scores, comparisons and affiliate disclosures |
| 2 | Maker | Home improvement and DIY | Project difficulty/time/materials cards, step layouts, before/after media and print checklists |
| 2 | Muse | Fashion and beauty | Lookbooks, outfit/product credits, routine/tutorial layouts and external shopping links |
| 2 | Kinship | Parenting and family blogs | Age/topic navigation, story-led homepage, practical checklists and family-safe demo imagery |
| 2 | Companion | Pet care and animal enthusiasts | Species/topic guides, care checklists, author context and resource pages |
| 3 | Shelf | Book reviewers, readers and authors | Book-detail cards, reading lists, review methodology and author/book landing pages |
| 3 | Playbook | Gaming news, reviews and guides | Platform/topic navigation, guide indexes, review summaries and prominent spoiler notices |
| 3 | Soundboard | Podcast and video creators | Episode-first homepage, click-to-load players, transcripts, chapters and external subscription links |
| 3 | Verdant | Gardening and plants | Plant profiles, seasonal indexes, growing-condition summaries and project diaries |
| 4 | Pace | Fitness and wellbeing publishers | Program/routine indexes, session tables, printable plans and clear author/source context |
| 4 | Ledger | Personal finance education | Explainers, comparison tables, dated methodology/source panels and optional local-only calculators |
| 4 | Screen | Film, television and entertainment | Review/recap distinction, release metadata, spoiler controls and viewing-guide indexes |
| 4 | Borough | Local news and community organizations | Location/topic navigation, manually maintained event cards, community resources and external RSVP links |
| 5 | Studio | Freelancers and creative services | Project case studies, service pages, testimonials with attribution and inquiry links |
| 5 | Launchpad | Startup, SaaS and consultancy content | Product/company blog, tutorial/FAQ indexes, release notes and external trial/contact CTAs |
| 5 | Ceremony | Wedding and event professionals | Real-event stories, galleries, vendor credits, service/inquiry pages and external booking links |
| 5 | Cause | Nonprofits and volunteer groups | Campaign stories, impact reports, volunteer information and clearly external donation links |

## First-batch briefs

### Saffron

Warm cookbook typography and a readable recipe index rather than a magazine slider. Ship reusable post markup for ingredients, instructions, preparation/cooking times and yield, with a print stylesheet and keyboard-operable checklists. Owners enter recipe facts through a documented post template; emit `Recipe` metadata only when the required real data is supplied. Never invent ratings or nutrition facts. Follow Google's [Recipe structured-data guidance](https://developers.google.com/search/docs/appearance/structured-data/recipe) and test actual rendered examples.

Minimum demo: twelve distinct recipes, dietary/topic labels, one long recipe, one recipe without optional nutrition, an About page, contact instructions and a clear editing example. Serving adjustment is an optional enhancement after fractional ingredient handling is tested.

### Wayfarer

Use an atlas-like region/destination hierarchy, image-led guide cards and generous itinerary typography. The first screen should show real server-rendered content while images load. Guides include editable time/budget/transport summaries, related destinations and optional map links; no map API key is required for the baseline theme.

Minimum demo: three destinations, two itineraries per destination, packing/logistics articles and one guide without a hero image. Explain how destinations map to Blogger labels and how to change the home sections without editing JavaScript.

### Lesson

Prioritize learning sequence and resource discovery. Give lessons a TOC, learning objectives, prerequisites, exercises and a restrained reading layout. Sequence links must come from owner-maintained course indexes rather than pretending chronological posts form a learning-management system. Files and restricted course access remain external.

Minimum demo: two complete learning paths, six lessons each, a resource page and mixed text/code/image lessons. Keyboard users must reach every sequence and disclosure control, and print output should remain useful.

### Bench

Use a compact testing-lab aesthetic: an editorial review summary, accessible specification/comparison tables, evidence images, methodology and update dates. Separate product facts, owner opinions and affiliate calls to action. A displayed score must be supplied and explained by the author; do not create artificial `AggregateRating` markup or promises of Google review stars.

Minimum demo: three detailed reviews, two comparison articles, a buying-guide index and methodology/disclosure pages. Test long model names, missing product images, wide tables and updates to prices supplied by the owner.

## Shared implementation foundation

Create a shared source core for navigation/fallbacks, safe feed rendering, metadata, accessible menus, typography primitives, contact-widget styling and release checks. Build each deliverable into a self-contained Blogger XML file. Keep the source modular so a pagination fix can be tested once and regenerated across the catalog; do not create twenty manually diverging copies of the existing monoliths.

Use Blogger settings, Layout widgets, labels, pages and documented post templates for owner-editable content. Google's guides describe [theme HTML/CSS customization](https://support.google.com/blogger/answer/176245/change-the-design-of-your-blog) and [post templates in blog settings](https://support.google.com/blogger/answer/9691230). Keep shared runtime code vanilla and critical assets self-contained where practical. Load optional video/maps/comment integrations only when used. Prefer server-rendered hero content over a blank feed-dependent first screen.

Give every theme a distinct type scale, spacing rhythm, header, home composition, archive card and article layout. Use legitimately licensed demo assets, real proofreading, consistent author identities and niche-appropriate sample content; avoid the duplicated placeholder posts in the older demos.

## Release acceptance criteria

- Validate home, subsequent pages, labels with spaces/Unicode, search, posts with/without images, static pages, empty blogs and error pages in Blogger. Test small and larger archives, including identical publication timestamps and Blogger-shortened pages.
- Keep native navigation usable with JavaScript disabled, feeds unavailable and network requests failing. Exercise timeout/retry, race conditions and the last page of infinite loading.
- Check 320, 375, 768, 1024 and 1440px layouts, wide tables/embeds/code, long titles and keyboard focus. Document a manual screen-reader check; target WCAG 2.2 AA contrast and interaction requirements.
- Validate rendered JSON-LD and metadata using quoted/Unicode titles and absent optional fields. Structured data must describe visible, owner-supplied content, with no duplicate canonical/Open Graph tags or invented ratings.
- Measure performance with a fixed demo, device and network profile. Target LCP at or below 2.5 seconds and CLS at or below 0.1 in the chosen lab profile, reporting conditions and results rather than promising a universal score.
- Ship the theme XML, demo content, asset/license manifest, setup/customization examples, upgrade/rollback instructions, changelog and checksummed release ZIP. Import that exact XML into the public demo and verify the Colorlib Download/Preview/Documentation links against the same release.

## Decide the next batch using evidence

Release the first four after their acceptance checks pass. Then compare existing Colorlib download-click data, setup/support questions and demo engagement using a defined observation period and existing consent-aware analytics. Collect keyword demand when research access is available. Reorder the remaining batches based on this evidence; do not assume twenty launches deserve equal effort.

The next concrete implementation deliverable is a shared-core prototype plus Saffron's complete home/index/article layouts and a real Blogger import. The other first-batch themes should reuse the validated core while keeping their own content models and visual systems.
