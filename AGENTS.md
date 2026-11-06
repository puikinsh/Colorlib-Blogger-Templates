# Repository Guidelines

## Project Structure

`core/` is the shared Blogger XML/CSS/JavaScript source. Each `themes/<slug>/` directory owns its configuration, layout, styles and demo articles. `assets/` contains original SVG illustrations. `tools/` builds and validates; `tests/` covers regressions; `docs/` records editing instructions, architecture and release status. `build/` is generated and ignored. Every theme’s `home.html` contains one `@@FEATURED@@` slot shared by native XML and static review output.

## Development Commands

Use Python 3.9+ and Node.js 22+. No npm dependencies are required.

- `python3 tools/build.py --packages`: generate all theme XML, demo exports, review pages and preview ZIPs.
- `python3 tools/build.py --theme saffron`: build one theme for iteration.
- `python3 tools/check.py`: validate catalog completeness, XML, standalone JavaScript and schema fixtures.
- `node --test tests/*.test.cjs`: exercise shared runtime and responsive fixtures.
- `python3 -m http.server 8765 --directory build`: serve local review pages.
- `git diff --check`: verify changed-line whitespace.

## Style and Safety

Use two-space indentation for expanded XML/JS/CSS and four spaces for Python. Keep runtime JavaScript vanilla. Preserve Blogger namespaces, CDATA boundaries and widget IDs. Escape generated HTML/attributes and use `.jsonEscaped`/`.jsEscaped` for Blogger values in scripts. Never replace native pagination with guessed feed cursors. Critical content must remain usable without JavaScript.

Change shared behavior in `core/` and regenerate every affected theme. Do not edit generated build files. `tools/bootstrap_catalog.py` is a one-time scaffolder that overwrites source; do not run it over subsequent theme edits.

## Validation and Releases

Static previews are not a Blogger emulator. Import the complete generated XML into a dedicated test blog before marking a theme ready. Check home, later pages, labels/search, posts/static pages, comments, empty/error states, keyboard controls and narrow screens. Test missing images and failed optional integrations. Record measured results in `docs/VALIDATION.md`; do not claim acceptance checks that have not run.

Use short imperative commit messages. Describe the behavior, validation and remaining release gates. Keep development preview packages distinct from public production releases; update documentation and provenance when assets or owner editing contracts change.
