# Colorlib Blogger Collection

Twenty original niche themes, built from one shared Blogger core. **Version 0.1.0 is a development collection, not a production-ready launch.** The [validation report](docs/VALIDATION.md) records completed checks and release gates. The nine existing Colorlib Blogger products remain independent maintained releases.

## Build and review

Python 3.9+ and Node.js 22+ are sufficient; no npm install is needed. Install Chrome/Chromium for browser regressions; set `CHROME_BIN` if automatic detection does not find it. CI requires Chrome rather than skipping those tests.

```sh
python3 tools/build.py --packages
python3 tools/build_lab.py
python3 tools/check.py
node --test tests/*.test.cjs
python3 -m http.server 8765 --directory build
```

Open `http://localhost:8765/` for the catalog. Each theme has home, article, archive, search, static, empty and error review views, plus `responsive.html` with 320/375/768px review panels; twelve distinct article titles and an original SVG cover set; a self-contained theme XML; a separate demo-content export; an owner-editable post-format example; setup and asset documentation. The static views demonstrate the design and do not emulate Blogger's template engine.

`build/packages/` contains twenty preview ZIPs and `SHA256SUMS`. These are intentionally named preview packages. Do not replace the maintained nine templates' production downloads with them.

The [public development repository](https://github.com/puikinsh/Colorlib-Blogger-Templates) now hosts the original artwork on `codex/collection-preview`; default demo image URLs are live. To use another owned HTTPS host, rebuild with `BLOGGER_ASSET_BASE=https://your-host/assets python3 tools/build.py --packages`. Local previews use bundled assets.

All twenty themes have been installed and checked on the [public Blogger lab](https://colorlib-blogger-theme-lab-2026.blogspot.com/), which now serves a dedicated shadcn-inspired collection hub. The [platform report](docs/PLATFORM-VALIDATION.md) records 260 live view checks, fixes and outstanding import/comment checks. The lab is a shared development fixture, not twenty finished production demos. [Static design previews](https://puikinsh.github.io/Colorlib-Blogger-Templates/lab/) and preview ZIPs are published after successful validation on the development branch. See the [owner/accessibility review](docs/OWNER-ACCESSIBILITY-REVIEW.md) for the completed control checks and the explicitly unmeasured performance gate.

The [design directions](docs/DESIGN-DIRECTIONS.md) record the individual layouts, typography, artwork and article treatments for all twenty themes. Open the catalog’s design-board link to compare live desktop and mobile layouts in groups of four.

## Source organization

- `lab/`: the lab-only catalog design and filtering runtime; `tools/build_lab.py` creates its Blogger XML and static preview.
- `core/`: shared XML structure, native comment includables, base/print CSS and progressive enhancements.
- `themes/<slug>/`: independent palette/type settings, `home.html` featured-post composition, CSS, topics, content format and demo text.
- `assets/<slug>/`: original vector artwork, also copied into local previews and packages.
- `tools/`: build, content/art generation and validation. Normal builds do not overwrite the theme configuration, welcome HTML or CSS.
- `tests/`: runtime/structure regressions and browser checks.
- `docs/`: approved roadmap, owner editing, architecture and validation status.

The catalog spans recipes, travel, education, technology reviews, DIY, fashion/beauty, parenting, pets, books, gaming, podcasts/video, gardening, fitness/wellbeing, finance education, film/TV, community publishing, freelance portfolios, product/company blogs, events and nonprofit publishing. See [the roadmap](docs/ROADMAP.md) for individual briefs and batch order.

## Owner configuration

The header title/description, logo and pages use native Blogger widgets/settings. The homepage introduction and topic links live in a Layout HTML widget; the featured article is Blogger's first rendered post. Color controls are exposed through Theme Designer. Post formats are ordinary HTML that owners can paste into a post or save as a Blogger post template.

Pagination always uses Blogger's crawlable Older/Newer URLs. The base theme does not depend on feed requests, a CSS framework, an icon font or a JavaScript framework. Optional article enhancements use DOM text and native controls. Payment, bookings, donation checkout, podcast hosting and gated learning platforms remain external services chosen by the owner.

## Published preview

[Download version 0.1.0-preview.2](https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/tag/v0.1.0-preview.2). The public Blogger hub and static catalog link directly to its twenty versioned packages. They include release-status notes, commit-pinned artwork and SHA-256 checksums. This is a prerelease for testing; the hub displays incomplete acceptance checks before its download cards.

The published assets are frozen from source commit `a672d7a1bca99d776f66322deead9d7ececf80c4`. Use a new preview number when staging changed source; do not replace these published assets with a later rebuild.

Latest platform retry: Saffron/Wayfarer added all 24 demo posts; Blogger then limited imports. Lesson/Bench comment retries still fail. See the [current stable-release blockers](docs/BLOGGER-RETRY.md). Published packages remain unchanged.

## Release staging

After committing a validated source revision, run `python3 tools/stage_release.py --version 0.1.0-preview.2`. It builds twenty separately versioned preview ZIPs under `build/releases/`, pins artwork to that exact source commit and writes a manifest, release notes and SHA256SUMS. Every ZIP includes `RELEASE-STATUS.md`. See [release readiness](docs/RELEASE-READINESS.md) and the [comment/screen-reader matrix](docs/COMMENTS-SCREEN-READER.md) before publishing. Staging does not publish a production release.

## Release gates

Every theme needs XML/JS/schema checks; phone/desktop and keyboard checks; an actual Blogger import; review of native comments and mobile rendering; realistic, owner-ready demo content; and a checksummed package matching its public demo. Original demonstration identities, projects and editorial templates must not be presented as actual reporting, tests, endorsements or professional instructions. Search markup is derived only from supplied content, without invented ratings or results.

Shared fixes belong in `core/`, followed by rebuilding and verifying the full catalog. Individual theme layout changes belong in that theme's source directory. GPL v3 license text is included; original vector illustrations share the package's license.
