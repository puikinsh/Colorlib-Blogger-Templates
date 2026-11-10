#!/usr/bin/env python3
"""Write the visual catalog and exact-file install guides for a staged release."""
from pathlib import Path
from html import escape
from zipfile import ZipFile
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/puikinsh/Colorlib-Blogger-Templates'
PAGES = 'https://puikinsh.github.io/Colorlib-Blogger-Templates'
FORMATS = {
    'recipe': 'Recipe cards with ingredients, method, checklists and a print action.',
    'itinerary': 'Travel itineraries with stops, practical notes and planning sections.',
    'lesson': 'Lesson pages with objectives, examples and a learning checklist.',
    'review': 'Review pages for specifications, comparisons, benefits and trade-offs.',
    'project': 'Project planners with materials, preparation and progress checklists.',
    'lookbook': 'Lookbook pages for image-led stories, outfit notes and credits.',
    'checklist': 'Reusable checklists alongside family stories and journal entries.',
    'care': 'Care checklists for routines, notes and useful pet resources.',
    'book': 'Book notes with edition details, reading notes and review prompts.',
    'game': 'Gaming guides with walkthrough notes and reference sections.',
    'episode': 'Episode pages with show notes, guest information and transcript sections.',
    'plant': 'Plant profiles with growing conditions, care notes and observations.',
    'routine': 'Routine pages with preparation, session notes and reflection.',
    'budget': 'Budget examples with a local income-minus-expenses calculator.',
    'spoiler': 'Viewing notes with an expandable spoiler discussion.',
    'event': 'Community bulletins with dates, places and useful links.',
    'case-study': 'Project case studies with the brief, process and outcome.',
    'release': 'Release notes and product updates in a changelog format.',
    'event-story': 'Event stories with venue, photographer and collaborator credits.',
    'impact': 'Campaign updates with impact notes and links to your chosen services.',
}


def guide(c, version):
    name, slug = c['name'], c['slug']
    package = f'{slug}-blogger-template-{version}.zip'
    theme = f'{name}-Blogger-Template.xml'
    demo = f'{name} Demo Content.xml'
    folder = f'{name}-Blogger-Template/'
    release = f'{REPO}/releases/tag/v{version}'
    return f'''# {name} Blogger Template

{c['intro']}

**Best for:** {c['audience']}. **Design:** {c['design_family']}.

[Live preview]({PAGES}/{slug}/) · [Full desktop screenshot](../../assets/previews/{slug}-desktop.webp) · [Mobile screenshot](../../assets/previews/{slug}-mobile.webp)

![{name} Blogger template homepage](../../assets/previews/{slug}-card.webp)

## Download

**Choose this exact package:** `{package}`

[Open the GitHub release downloads]({release}) and expand **Assets** if needed. Select **`{package}`** from the list.

Use the named template package. GitHub's **Source code (zip)** and **Code → Download ZIP** contain the development repository, rather than the installable theme package.

## Which files do I need?

After extracting the package, open **`{folder}`**.

| File | Use |
| --- | --- |
| **`{theme}`** | **Install this file in Blogger → Theme → Restore → Upload.** |
| `{demo}` | Optional sample posts: Blogger → Settings → Manage Blog → Import content. |
| `post-template.html` | Optional starting layout to copy into a post's HTML editor. |
| `README.md` | Package setup and customization instructions. |
| `ASSETS.md` | Artwork and photography credits and license information. |

Do not upload the ZIP or the demo-content XML as your theme.

## Installation

1. Back up your current theme from **Blogger → Theme → menu beside Customize → Backup**.
2. Extract **`{package}`** on your computer.
3. In **Theme → menu beside Customize → Restore → Upload**, select **`{theme}`** inside **`{folder}`**.
4. If you want sample posts, use **Settings → Manage Blog → Import content** and choose **`{demo}`**. Importing sample posts is optional.
5. In **Layout**, edit your header, pages, homepage introduction and visual notebook. Adjust colors through **Theme → Customize → Advanced**.

## What you can publish

{FORMATS[c['feature']]}

The theme also includes responsive article layouts, photo galleries, native Older/Newer navigation, Blogger comments, search and editable homepage widgets. Replace sample text and use images you have permission to publish.

## Documentation

[Customization guide](../../docs/OWNER-EDITING.md) · [Release notes]({release}) · [Testing status](../../docs/RELEASE-READINESS.md) · [License](../../LICENSE)

Current package: **{version}**, a development preview. Photography retains its separate credited licenses.

[← Browse all twenty templates](../../README.md#choose-your-template)
'''


def catalog_readme(themes, version):
    cells = []
    for c in themes:
        slug, name = c['slug'], c['name']
        detail = f'themes/{slug}/README.md'
        cells.append(f'<td width="50%"><a href="{detail}"><img src="assets/previews/{slug}-card.webp" alt="{escape(name)} Blogger template homepage" width="440"></a><br><strong>{escape(name)}</strong><br>{escape(c["audience"])}<br><a href="{detail}#download">Details &amp; download</a> · <a href="{PAGES}/{slug}/">Live preview</a></td>')
    rows = ['<tr>' + ''.join(cells[i:i + 2]) + '</tr>' for i in range(0, len(cells), 2)]
    grid = '<table>\n<tbody>\n' + '\n'.join(rows) + '\n</tbody>\n</table>'
    return f'''# Colorlib Blogger Templates

Twenty free Blogger / Blogspot themes for recipes, travel, magazines, learning, portfolios and more. Each theme has its own layout, sample content and editable article format.

[Browse live previews]({PAGES}/lab/) · [Installation guide](#install-a-template) · [Release downloads]({REPO}/releases/tag/v{version})

## Choose your template

Click a screenshot or **Details & download** to open that template's guide. Every guide names the exact ZIP and XML files to use.

{grid}

## Install a template

1. Choose a design above and open its **Details & download** guide.
2. On the linked GitHub release, expand **Assets** and download the exact ZIP named in that guide. For Wayfarer, choose **`wayfarer-blogger-template-{version}.zip`**.
3. Extract the ZIP. In Blogger, back up your current theme, then open **Theme → menu beside Customize → Restore → Upload**.
4. Upload the **theme XML**: for Wayfarer, **`Wayfarer-Blogger-Template.xml`** inside **`Wayfarer-Blogger-Template/`**.
5. Sample posts are optional. Import **`Wayfarer Demo Content.xml`** separately through **Settings → Manage Blog → Import content**.

| What you downloaded | What to do with it |
| --- | --- |
| `<slug>-blogger-template-{version}.zip` | Extract it first. This is the packaged template. |
| `<Name>-Blogger-Template.xml` | Upload through **Theme → Restore**. |
| `<Name> Demo Content.xml` | Optional sample posts, imported through **Settings**. |
| `post-template.html` | Optional article layout for the post HTML editor. |

GitHub's **Code → Download ZIP** and **Source code (zip)** downloads are for developers. Use the named template package from **Releases** to install a Blogger theme.

## Published preview

Current packages: **{version}**. [Release notes and all twenty packages]({REPO}/releases/tag/v{version}) · [Checksums]({REPO}/releases/download/v{version}/SHA256SUMS).

These packages are development previews. [Testing status](docs/RELEASE-READINESS.md) records the current validation results. Published assets are versioned and remain unchanged.

## Documentation and licensing

- [Customize your theme](docs/OWNER-EDITING.md): header, menus, colors, homepage widgets and article formats.
- [Developer setup and project status](docs/DEVELOPMENT.md): builds, source layout, regression checks and validation history.
- [Design directions](docs/DESIGN-DIRECTIONS.md): the layouts and publishing use cases behind the collection.
- [GPL v3 license](LICENSE) for the theme code and original vector artwork; [photography credits](assets/photography.json) record separate photo licenses.

The screenshots link to the actual design previews. Full desktop and mobile captures are available in each theme's guide.
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True, help='Published/staged release version without v')
    args = parser.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?', args.version):
        parser.error('Use a release version such as 0.1.0-preview.5')
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    captures = json.loads((ROOT / 'assets/previews/cards.json').read_text())['captures']
    configs = []
    # Validate every input before writing anything, so incomplete staging cannot update half the guides.
    for row in catalog:
        slug, name = row['slug'], row['name']
        config = json.loads((ROOT / 'themes' / slug / 'theme.json').read_text())
        assert config['name'] == name and config['feature'] in FORMATS
        shot = next(c for c in captures if c['slug'] == slug)
        assert hashlib.sha256((ROOT / 'assets/previews' / shot['file']).read_bytes()).hexdigest() == shot['sha256']
        package = ROOT / 'build/releases' / args.version / f'{slug}-blogger-template-{args.version}.zip'
        with ZipFile(package) as z:
            required = [f'{name}-Blogger-Template.xml', f'{name} Demo Content.xml', 'post-template.html', 'README.md', 'ASSETS.md']
            for filename in required:
                assert f'{name}-Blogger-Template/{filename}' in z.namelist(), (slug, filename)
        configs.append(config)
    for config in configs:
        (ROOT / 'themes' / config['slug'] / 'README.md').write_text(guide(config, args.version))
    (ROOT / 'README.md').write_text(catalog_readme(configs, args.version))
    print(f'Wrote {len(configs)} exact-file download guides and the visual README catalog for {args.version}.')


if __name__ == '__main__':
    main()
