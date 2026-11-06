# Design directions

## November 6 redesign

The initial collection repeated a headline, side note, topic cards and split feature too often. Four themes now use separate information hierarchies and visual systems:

| Theme | Direction | Home composition | Feed and reading |
| --- | --- | --- | --- |
| Launchpad | shadcn-inspired product journal | Compact identity, neutral zinc surfaces, topic underline navigation, margin annotation and bordered feature | Horizontal update rows, small controls, restrained article headings |
| Lesson | shadcn-inspired documentation library | Learning-path sidebar, breadcrumb, reading-first guide and blue information callout | Text-first tutorial cards, code panels and reading navigation |
| Bench | Tailwind-inspired review publication | Slate/indigo typography, topic navigation with short explanations, rounded featured review | White review cards, clear comparison tables and generous reading surfaces |
| Studio | Tailwind-inspired independent portfolio | Large typographic cover, project navigation, full-width deep-green case study | Staggered two-column work grid and quieter process articles |

The other sixteen retain their current directions for now. Preserve meaningful differences in hierarchy, density, typography, imagery and article presentation when revising them; a new palette alone is insufficient.

## Implementation

These are original Blogger layouts implemented as embedded CSS and semantic HTML. The design references are [Tailwind theme variables](https://tailwindcss.com/docs/theme) and [shadcn semantic theming](https://ui.shadcn.com/docs/theming). They are visual influences, not installed component libraries. No Tailwind CDN compiler, React runtime or third-party component scripts are loaded.

For these four themes, `themes/<slug>/home.html` owns a single `@@FEATURED@@` slot. The builder inserts a real Blogger post loop into XML and representative post HTML into local previews. This keeps the custom layout consistent across both outputs. Other themes still use `home.xml` and the existing preview composition. `welcome.html` remains the owner-editable introduction widget.

Topic navigation uses real Blogger label URLs; controls retain native links and search forms. Styles cover the article, navigation, cards, tables, controls and mobile breakpoints as well as the homepage. Avoid fabricated dashboard data, reviews, testimonials or nonfunctional buttons as visual filler.

## Review

All 45 regressions and generated XML/JavaScript/schema checks pass after the redesign. Reviewed desktop homepages and fixed-width phone panels. Static preview CSS, JavaScript and images have content-based URL versions so cached assets cannot conceal a saved redesign. Actual Blogger import and comment/mobile platform checks remain pending, as recorded in `VALIDATION.md`.
