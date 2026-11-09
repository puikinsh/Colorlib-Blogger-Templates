#!/usr/bin/env python3
"""Build the dedicated Blogger lab hub, separate from the twenty product themes."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json,re,shutil
import xml.etree.ElementTree as ET
from build import ROOT, OUT, substitute, ASSET_BASE

REPO='https://github.com/puikinsh/Colorlib-Blogger-Templates'
SOURCE=REPO+'/blob/codex/collection-preview/'
PREVIEW='https://puikinsh.github.io/Colorlib-Blogger-Templates'
RELEASE_VERSION='0.1.0-preview.5'
RELEASE_URL=REPO+'/releases/tag/v'+RELEASE_VERSION
DOWNLOAD_BASE=REPO+'/releases/download/v'+RELEASE_VERSION
GROUPS={
    'lifestyle':('Lifestyle', ['saffron','wayfarer','muse','kinship','companion','verdant','pace','ceremony']),
    'culture':('Arts & culture', ['shelf','playbook','soundboard','screen']),
    'work':('Work & learning', ['lesson','bench','maker','ledger','studio','launchpad']),
    'community':('Community', ['borough','cause'])
}

def release_notice():
    return f'''<section class="hub-release" aria-labelledby="release-heading"><div class="hub-release-heading"><h2 id="release-heading">Before you download</h2><span>Development preview</span></div><p>Version {RELEASE_VERSION} is for testing. These checks remain incomplete:</p><ul role="list"><li><strong>Screen readers</strong>Actual speech and rotor output remains unverified after the latest VoiceOver connection timeout.</li><li><strong>Comment publishing</strong>Root/reply publication was observed for seventeen themes across sessions. Bench’s older-post pair recovered without permission changes. Ledger/Screen roots and Launchpad’s reply still failed; publishing reliability remains open.</li><li><strong>Blogger imports and performance</strong>Complete demo imports: six updated photo-rich exports passed (Lesson, Bench, Maker, Muse, Kinship and Companion; 72 posts). Blogger refused Shelf with an import-frequency limit; a fresh retry returned the same refusal and accepted no new posts. The remaining fourteen updated exports are unverified. Measured live performance remains unverified.</li><li><strong>Final acceptance</strong>All 20 designs passed native MP3/WAV and 320px/375px layout checks, including recorded retries. Reliable video playback at narrow widths remains unresolved after stalls. Vimeo remains blocked in the in-app browser. Safari playback was observed across all 20 templates after recorded retries, but intermittent pauses remain unresolved. Physical devices, audible output and final editorial approval remain open.</li></ul><p>Preview.5 adds sixty credited photographs, responsive visual notebooks and editable homepage galleries. All twenty new galleries were checked natively at 375px. Earlier audio/mobile fixes and all test reports are included. This is a development prerelease; the remaining gates above are not passed.</p><nav aria-label="Preview release information"><a href="{RELEASE_URL}">Release notes and full test status<span aria-hidden="true"> ↗</span></a><a href="{SOURCE}docs/COMMENTS-REMAINING-EIGHT.md">Latest comment results and Bench investigation</a><a href="{SOURCE}docs/ACCESSIBILITY-COMMENTS-FOLLOWUP.md">Accessibility results</a><a href="{SOURCE}docs/BLOGGER-RETRY.md">Earlier import/comment results</a><a href="{SOURCE}docs/NATIVE-MEDIA.md">Desktop media results</a><a href="{SOURCE}docs/AUDIO-MOBILE.md">Audio/mobile results</a><a href="{SOURCE}docs/VISUAL-REFRESH.md">Visual refresh and photo credits</a><a href="{SOURCE}docs/PHOTO-IMPORTS.md">Photo import and screenshot checks</a><a href="{SOURCE}docs/PROVIDER-SAFARI.md">Latest Safari playback results</a><a href="{DOWNLOAD_BASE}/SHA256SUMS">SHA-256 checksums</a></nav></section>'''

def hub_markup(local=False):
    catalog=json.loads((ROOT/'catalog.json').read_text())
    captures=json.loads((ROOT/'assets/previews/manifest.json').read_text())['captures']
    cards=[]
    for i,row in enumerate(catalog,1):
        c=json.loads((ROOT/'themes'/row['slug']/'theme.json').read_text())
        group=next(k for k,(_,slugs) in GROUPS.items() if c['slug'] in slugs)
        preview=('../'+c['slug']+'/index.html') if local else PREVIEW+'/'+c['slug']+'/'
        image=('previews/' if local else ASSET_BASE+'/previews/')+c['slug']+'-desktop.webp'
        mobile=('previews/' if local else ASSET_BASE+'/previews/')+c['slug']+'-mobile.webp'
        package=DOWNLOAD_BASE+'/'+c['slug']+'-blogger-template-'+RELEASE_VERSION+'.zip'
        name=escape(c['name'])
        capture=next(r for r in captures if r['slug']==c['slug'] and r['mode']=='desktop')
        width,height=capture['size']
        cards.append(f'''<article class="hub-card" data-hub-card="true" data-category="{group}"><a class="hub-preview" href="{preview}" aria-label="Preview {name}"><img src="{image}" alt="{name} desktop template layout" width="{width}" height="{height}" loading="{'eager' if i<3 else 'lazy'}" decoding="async"/><span class="hub-preview-label">{escape(c.get('design_family','Original layout').replace('-',' ').capitalize())}</span></a><div class="hub-card-body"><nav class="hub-capture-links" aria-label="{name} screenshots"><a href="{image}">Full desktop<span class="cl-sr-only"> screenshot of {name}</span></a><a href="{mobile}">Mobile<span class="cl-sr-only"> screenshot of {name}</span></a></nav><div class="hub-card-title"><h3><a href="{preview}">{name}</a></h3><span class="hub-card-number">{i:02d}</span></div><p>{escape(c['audience'])}</p><div class="hub-card-actions"><a class="hub-button" href="{preview}">Preview<span class="cl-sr-only"> {name}</span><span aria-hidden="true">↗</span></a><a class="hub-button" href="{package}">Download preview<span class="cl-sr-only"> {name} {RELEASE_VERSION}</span></a></div></div></article>''')
    filters='<button aria-pressed="true" class="hub-filter" data-hub-filter="all" type="button">All themes<span>20</span></button>'
    for key,(name,slugs) in GROUPS.items():filters+=f'<button aria-pressed="false" class="hub-filter" data-hub-filter="{key}" type="button">{escape(name)}<span>{len(slugs)}</span></button>'
    return f'''<div data-hub="true"><section class="hub-hero" aria-labelledby="hub-title"><div><span class="hub-eyebrow"><span aria-hidden="true" class="hub-dot"></span>The Colorlib Blogger collection</span><h1 id="hub-title">A home for every kind of story.</h1><p>Twenty distinct starting points for your next publication. These are real desktop captures of each static demo. Open a full desktop or mobile screenshot, then explore the working preview.</p><div class="hub-actions"><a class="hub-button hub-button-primary" href="#theme-collection">Explore themes<span aria-hidden="true">↓</span></a><a class="hub-button" href="{SOURCE}docs/OWNER-EDITING.md">Setup guide<span aria-hidden="true">↗</span></a></div></div><span class="hub-version">v{RELEASE_VERSION}</span></section>{release_notice()}<div class="hub-workspace"><aside class="hub-sidebar" aria-label="Collection filters"><div data-hub-controls="true" hidden="hidden"><h2>Browse by interest</h2><div class="hub-filters">{filters}</div></div><div class="hub-note"><strong>Built for Blogger</strong>Photography, original artwork and responsive native layouts. No framework runtime.<a href="{SOURCE}docs/PLATFORM-VALIDATION.md">Read the validation report<span aria-hidden="true"> ↗</span></a></div></aside><section class="hub-catalog" id="theme-collection" aria-labelledby="collection-title"><div class="hub-toolbar"><div><h2 id="collection-title">Theme collection</h2><p class="hub-count" data-hub-count="true" role="status" aria-atomic="true">20 themes · Development previews</p></div><div class="hub-search" data-hub-controls="true" hidden="hidden"><label class="cl-sr-only" for="hub-search">Find a theme</label><input id="hub-search" data-hub-search="true" type="search" placeholder="Search themes or interests…"/></div></div><div class="hub-grid">{''.join(cards)}</div><div class="hub-empty" data-hub-empty="true" hidden="hidden"><h3>No themes match yet.</h3><p>Try another interest or a broader search.</p><button class="hub-button" data-hub-reset="true" type="button">Clear filters</button></div></section></div><section class="hub-fixtures" aria-labelledby="fixtures-title"><h2 id="fixtures-title">Inside the test lab</h2><p>These are development previews. Static previews show each design; this Blogger lab checks native behavior. Testing is incomplete. See the release status above for the remaining acceptance checks.</p><nav aria-label="Test fixtures"><a href="/2026/09/platform-edge-case-heading-identifiers.html">Article formats</a><a href="/2026/09/platform-edge-case-quotes-cafe-riga.html">Text-only article</a><a href="/p/about-this-test-lab.html">About the lab</a><a href="{REPO}">Source on GitHub<span aria-hidden="true"> ↗</span></a></nav></section></div>'''

def main():
    dest=OUT/'lab';dest.mkdir(parents=True,exist_ok=True)
    shutil.copytree(ROOT/'assets/previews',dest/'previews',dirs_exist_ok=True)
    c=json.loads((ROOT/'themes/launchpad/theme.json').read_text())
    c.update(name='Colorlib Blogger Lab',slug='lab',footer_copy='Original themes. Thoughtful publishing.')
    values={k.upper():escape(str(v),quote=True) for k,v in c.items() if isinstance(v,(str,int))}
    base=(ROOT/'core/base.css').read_text();css=(ROOT/'lab/hub.css').read_text();js=(ROOT/'core/runtime.js').read_text()+'\n'+(ROOT/'lab/hub.js').read_text();printing=(ROOT/'core/print.css').read_text()
    values.update(VISUALS='',CSS=base,THEME_CSS=css,PRINT_CSS=printing,JS=js,HOME='',WELCOME='',COMMENTS=(ROOT/'core/comments.xml').read_text(),HEADING_FONT=c['heading_font'],BODY_FONT=c['body_font'])
    source=(ROOT/'core/theme.xml').read_text()
    source=re.sub(r"    <b:if cond='data:blog.url == data:blog.homepageUrl'>\n      <b:section class='cl-visual-section'[\s\S]*?    </b:if>\n",'',source)
    source=source.replace("<body class='theme-@@SLUG@@'>", "<body class='theme-@@SLUG@@'><b:class cond='data:blog.url == data:blog.homepageUrl' name='lab-home'/>")
    source=source.replace("data:blog.pageType not in {&quot;item&quot;,&quot;static_page&quot;,&quot;error_page&quot;}","data:blog.pageType not in {&quot;item&quot;,&quot;static_page&quot;,&quot;error_page&quot;} and data:blog.url != data:blog.homepageUrl")
    needle="          <b:else/>\n            <b:if cond='data:blog.url == data:blog.homepageUrl and data:numPosts &gt; 0'>"
    source=source.replace(needle,"          <b:elseif cond='data:blog.url == data:blog.homepageUrl'/><b:include name='lab-hub'/>\n          <b:else/>\n            <b:if cond='data:blog.url == data:blog.homepageUrl and data:numPosts &gt; 0'>")
    source=source.replace("        <b:includable id='home-hero'>","        <b:includable id='lab-hub'>"+hub_markup()+"</b:includable>\n        <b:includable id='home-hero'>")
    xml=substitute(source,values);ET.fromstring(xml);(dest/'Colorlib-Lab-Blogger-Template.xml').write_text(xml)
    static_css=':root{--accent:#18181b;--paper:#fff;--ink:#18181b;--soft:#f4f4f5;--heading:ui-sans-serif,system-ui,sans-serif;--body:ui-sans-serif,system-ui,sans-serif}\n'+base+'\n'+css+'\n'+printing
    (dest/'hub.css').write_text(static_css);(dest/'hub.js').write_text(js)
    (dest/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Colorlib Blogger Theme Lab</title><link rel="stylesheet" href="hub.css"></head><body class="theme-lab lab-home"><a class="cl-skip" href="#main-content">Skip to content</a><div class="cl-shell"><header class="cl-header"><p class="cl-brand"><a href="index.html">Colorlib / Blogger</a></p><nav class="cl-primary-nav" aria-label="Main menu"><ul><li><a href="'+SOURCE+'docs/OWNER-EDITING.md">Documentation</a></li><li><a href="'+REPO+'">GitHub ↗</a></li></ul></nav></header><main id="main-content" tabindex="-1">'+hub_markup(local=True)+'</main><footer class="cl-footer"><p>© 2026 Colorlib · Open source under GPL v3</p><p>Development collection</p></footer></div><script src="hub.js" defer></script></body></html>')
    print('Lab: native Blogger hub + local catalog preview')

if __name__=='__main__':main()
