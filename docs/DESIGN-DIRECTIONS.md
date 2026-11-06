# Design directions

## November 6 redesign

The initial collection repeated a headline, side note, topic cards and split feature too often. Four themes now use separate information hierarchies and visual systems:

| Theme | Direction | Home composition | Feed and reading |
| --- | --- | --- | --- |
| Launchpad | shadcn-inspired product journal | Compact identity, neutral zinc surfaces, topic underline navigation, margin annotation and bordered feature | Horizontal update rows, small controls, restrained article headings |
| Lesson | shadcn-inspired documentation library | Learning-path sidebar, breadcrumb, reading-first guide and blue information callout | Text-first tutorial cards, code panels and reading navigation |
| Bench | Tailwind-inspired review publication | Slate/indigo typography, topic navigation with short explanations, rounded featured review | White review cards, clear comparison tables and generous reading surfaces |
| Studio | Tailwind-inspired independent portfolio | Large typographic cover, project navigation, full-width deep-green case study | Staggered two-column work grid and quieter process articles |

The remaining sixteen were redesigned in a second pass:

| Theme | Direction | Defining layout and reading choices |
| --- | --- | --- |
| Saffron | Kitchen recipe index | Supper-table feature, round recipe images, four-column recipe index, warm print-friendly recipe cards |
| Wayfarer | Travel field atlas | Numbered destination rail, large route illustration, portrait guide cards and itinerary reference boxes |
| Maker | Workshop manual | Project-file frame, graph-paper index, numbered build cards and materials/checklist panels |
| Muse | Fashion editorial folio | Oversized serif cover, arched portrait feature, staggered fashion grid and centred essay titles |
| Kinship | Family letter | Centred letter and seal, intimate thumbnail feature, topic note and single-column story letters |
| Companion | Pet-care hub | Illustrated dog/cat navigation, rounded resource feature, compact care cards and practical checklists |
| Shelf | Literary review | Bookmark spine, book-like feature, numbered reading ledger and generous serif prose |
| Playbook | Gaming dispatch | Dark high-contrast type, lime topic keys, controller artwork and a dense gaming feature/card feed |
| Soundboard | Listening room | Waveform channel rail, dark episode panel, numbered episode archive and transcript-friendly reading |
| Verdant | Botanical notebook | Specimen label, bound notebook frame, plant-profile cards and field-note reference panels |
| Pace | Movement journal | Athletic typography, starting-line rail, numbered session rows and personal routine sheets |
| Ledger | Finance reference desk | Compact concept navigation, explainer paper, text-first note matrix and a local arithmetic panel |
| Screen | Cinema criticism | Centred marquee, screening-frame feature, widescreen cards and cinematic serif essays |
| Borough | Neighbourhood newspaper | Double-rule masthead, lead story with noticeboard, column-divided news cards and event reference boxes |
| Ceremony | Wedding story album | Double-border invitation, arched album image, staggered portrait stories and credited event details |
| Cause | Nonprofit action desk | Mission panel, community story with participation rail, reporting cards and impact-context tables |

Preserve differences in hierarchy, density, typography, imagery and article presentation when revising them. A new palette alone is insufficient. Homepage teasers now describe individual stories instead of repeating the same theme demonstration sentence.

## Implementation

These are original Blogger layouts implemented as embedded CSS and semantic HTML. The design references are [Tailwind theme variables](https://tailwindcss.com/docs/theme) and [shadcn semantic theming](https://ui.shadcn.com/docs/theming). They are visual influences, not installed component libraries. No Tailwind CDN compiler, React runtime or third-party component scripts are loaded.

For all twenty themes, `themes/<slug>/home.html` owns a single `@@FEATURED@@` slot. The builder inserts a real Blogger post loop into XML and representative post HTML into local previews. This keeps the custom layout consistent across both outputs. `welcome.html` remains the owner-editable introduction widget.

Topic navigation uses real Blogger label URLs; controls retain native links and search forms. Styles cover the article, navigation, cards, tables, controls and mobile breakpoints as well as the homepage. Avoid fabricated dashboard data, reviews, testimonials or nonfunctional buttons as visual filler.

## Review

All 46 regressions and generated XML/JavaScript/schema checks pass after the redesign. Reviewed all twenty desktop homepages at 1100px and phone panels at 375px using five live comparison boards in each size. Automated home/article fixtures cover five widths. Added working per-label preview pages with a regression checking their exact article membership. Shared print rules follow theme overrides so dark article panels remain legible on paper. Static preview CSS, JavaScript and images have content-based URL versions so cached assets cannot conceal a saved redesign. This design review preceded native platform testing. Later Blogger installation, comment/mobile results and the published-package import retries are recorded in [validation status](VALIDATION.md) and the [current retry matrix](BLOGGER-RETRY.md).
