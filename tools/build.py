#!/usr/bin/env python3
"""Build self-contained Blogger XML, original demo exports and static review previews."""
from pathlib import Path
from html import escape
from urllib.parse import quote,unquote
from datetime import datetime,timedelta,timezone
import argparse,json,re,shutil,hashlib,os,xml.etree.ElementTree as ET
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
from content import body,feature
from art import cover
from review import boards
from visuals import photo_tag, media_name, showcase, asset_notes, PHOTOS

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'build'
ASSET_BASE=os.environ.get('BLOGGER_ASSET_BASE','https://raw.githubusercontent.com/puikinsh/Colorlib-Blogger-Templates/codex/collection-preview/assets')
ATOM='http://www.w3.org/2005/Atom'
BLOGGER='http://schemas.google.com/blogger/2008'
ET.register_namespace('',ATOM)
ET.register_namespace('blogger',BLOGGER)

def substitute(source,values):
    used=set(re.findall(r'@@([A-Z_]+)@@',source))
    missing=used-values.keys()
    if missing:raise ValueError('Missing tokens: '+','.join(sorted(missing)))
    return re.sub(r'@@([A-Z_]+)@@',lambda m:values[m[1]],source)

def css_for_preview(c,css):
    return css.replace('$(brand.accent)',c['accent']).replace('$(brand.paper)',c['paper']).replace('$(brand.ink)',c['ink'])

def post_path(post):
    slug=re.sub('[^a-z0-9]+','-',post['title'].lower()).strip('-')
    return '2026/10/'+slug+'.html'

def label_path(label):
    return 'label-'+re.sub('[^a-z0-9]+','-',label.lower()).strip('-')+'.html'

def preview_topic_links(markup):
    return re.sub(r'href="/search/label/([^"]+)"',lambda m:'href="'+label_path(unquote(m[1]))+'"',markup)

def card(c,post):
    image='assets/'+media_name(c,post['index'])
    title=escape(post['title']);url='article.html' if post['index']==1 else f'article-{post["index"]:02d}.html'
    return f'<article class="cl-card"><a class="cl-card-image" href="{url}" aria-label="{title}">{photo_tag(c,post["index"],"assets",linked=True)}</a><div class="cl-card-copy"><p class="cl-kicker"><a href="{label_path(post["label"])}">{escape(post["label"])}</a></p><h3><a href="{url}">{title}</a></h3><p>{escape(post["intro"])}</p><div class="cl-card-meta"><span>Colorlib Demo Editor</span><time datetime="2026-10-25T10:00:00Z">25 October 2026</time></div></div></article>'

def featured(c,post):
    title=escape(post['title'])
    return f'<article class="cl-featured"><a class="cl-featured-image" href="article.html" aria-label="{title}">{photo_tag(c,1,"assets",priority=True,linked=True)}</a><div class="cl-featured-copy"><p class="cl-kicker">Editor’s pick</p><h3><a href="article.html">{title}</a></h3><p>{escape(post["intro"])}</p><a class="cl-text-link" href="article.html">{escape(c["read_label"])} ↗</a></div></article>'

def nav(page=1):
    return '<nav aria-label="Post navigation" class="cl-pager" id="blog-pager">'+('<a class="blog-pager-newer-link" href="index.html">← Newer Posts</a>' if page>1 else '')+'<a class="cl-pager-home" href="index.html">Home</a>'+('<a class="blog-pager-older-link" href="page-2.html">Older Posts →</a>' if page==1 else '')+'</nav>'

def header(c,listing=True):
    tag='h1' if listing else 'p'
    return f'<header class="cl-header"><div class="cl-brand-section"><{tag} class="cl-brand"><a href="index.html">{c["name"]}</a></{tag}><p class="cl-brand-description">{escape(c["audience"])}</p></div><nav aria-label="Main menu" class="cl-primary-nav"><ul><li><a href="index.html">Home</a></li><li><a href="page.html">About</a></li><li><a href="label.html">Explore</a></li></ul></nav><form action="search.html" class="cl-search" role="search"><label class="cl-sr-only" for="cl-search">Search this blog</label><input id="cl-search" name="q" type="search" placeholder="Search stories…"/><button type="submit">Search</button></form></header>'

def feed(c,posts):
    return '<section aria-labelledby="feed-heading" class="cl-feed" id="post-feed"><div class="cl-section-heading"><div><p class="cl-kicker">'+escape(c['feed_kicker'])+'</p><h2 id="feed-heading">'+escape(c['feed_title'])+'</h2></div><span class="cl-small">'+escape(c['feed_note'])+'</span></div><div class="cl-post-grid">'+''.join(card(c,p) for p in posts)+'</div></section>'

def page_html(c,title,content,css,runtime,listing=True,schema=None):
    asset_version=hashlib.sha256((css+runtime+(ROOT/'tools/art.py').read_text()).encode()).hexdigest()[:12]
    web={'@context':'https://schema.org','@type':'WebSite','name':c['name'],'url':'https://example.com/'}
    jsonld='<script type="application/ld+json">'+json.dumps(web).replace('<','\\u003c')+'</script>'
    if schema:jsonld+='<script type="application/ld+json">'+json.dumps(schema).replace('<','\\u003c')+'</script>'
    html='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+' — '+c['name']+'</title><meta name="description" content="'+escape(c['intro'],quote=True)+'"><link rel="stylesheet" href="assets/theme.css?v='+asset_version+'">'+jsonld+'</head><body class="theme-'+c['slug']+'"><a class="cl-skip" href="#main-content">Skip to content</a><div class="cl-shell">'+header(c,listing)+'<main id="main-content" tabindex="-1">'+content+'</main><footer class="cl-footer"><div><a class="cl-footer-brand" href="index.html">'+c['name']+'</a><p>'+escape(c['footer_copy'])+'</p></div><p>© <span data-current-year>2026</span> · Theme by <a href="https://colorlib.com/">Colorlib</a></p></footer></div><script src="assets/runtime.js?v='+asset_version+'" defer></script></body></html>'

    return re.sub(r'(src="assets/cover-[^"]+\.svg)"',lambda m:m[1]+'?v='+asset_version+'"',html)

def compose_home(c,feature_markup):
    source=(ROOT/'themes'/c['slug']/'home.html').read_text()
    if source.count('@@FEATURED@@')!=1:
        raise ValueError(c['slug']+': home.html must contain exactly one featured-post slot')
    return source.replace('@@FEATURED@@',feature_markup)

def preview(c,posts,dest,css,runtime):
    welcome=(ROOT/'themes'/c['slug']/'welcome.html').read_text()
    # Preview-only links mirror Blogger label pages without needing a Blogger renderer locally.
    welcome=preview_topic_links(welcome)
    first=posts[0]
    home=compose_home(c,featured(c,first))
    home=preview_topic_links(home).replace(ASSET_BASE+'/'+c['slug']+'/', 'assets/')
    homepage=welcome+home+feed(c,posts[1:7])+nav()+showcase(c,'assets')
    pages={'index.html':('Home',homepage,True),'page-2.html':('More stories',feed(c,posts[7:])+nav(2),True),'label.html':(c['topics'][0],'<p class="cl-status">Stories in '+escape(c['topics'][0])+'</p>'+feed(c,[p for p in posts if p['label']==c['topics'][0]])+nav(),True),'search.html':('Search results','<p class="cl-status">Search results · demonstration view</p>'+feed(c,posts[:3])+nav(),True),'empty.html':('No stories','<section class="cl-empty"><h2>No stories here yet.</h2><p>Choose another topic or return to the home page.</p><a href="index.html">Browse all stories</a></section>',True),'404.html':('Not found','<section class="cl-empty"><p class="cl-kicker">A small detour</p><h1>This page has moved on.</h1><p>Try the search above, or return to the latest stories.</p><a class="cl-button" href="index.html">Back to the journal</a></section>',False)}
    media='<article class="cl-article"><header class="cl-article-header"><h1>Media validation fixtures</h1><p>Public provider examples, not recordings owned by this demonstration theme. No player loads before activation.</p></header><div class="cl-reading-layout"><aside class="cl-toc" hidden></aside><div class="cl-prose"><h2>YouTube sample</h2><p>Loading connects to YouTube. Playback may require another Play activation inside the player.</p><div class="cl-video"><button type="button" data-video-src="https://www.youtube-nocookie.com/embed/M7lc1UVf-VE" data-video-title="YouTube official iframe example">Load YouTube sample</button></div><h2>Vimeo sample</h2><p>Loading connects to Vimeo. Use its Play control to start playback.</p><div class="cl-video"><button type="button" data-video-src="https://player.vimeo.com/video/76979871" data-video-title="Vimeo official SDK example">Load Vimeo sample</button></div><h2>Invalid destination</h2><button type="button" data-video-src="https://example.invalid/video">Check invalid video link</button><p>Expect an announced error without a player or provider request.</p><h2>Validation limits</h2><p>Check captions, transcript accuracy and rights against your own recording. A visible iframe is not proof of playback or audible sound. This fixture is a static preview, not a Blogger import test.</p></div></div></article>'
    media=media.replace('<h2>YouTube sample</h2>',(ROOT/'docs/fixtures/audio-samples.html').read_text()+'<h2>YouTube sample</h2>')
    pages['media.html']=('Media validation',media,False)
    for topic in dict.fromkeys(c['topics']+[post['label'] for post in posts]):
        pages[label_path(topic)]=(topic,'<p class="cl-status">Stories in '+escape(topic)+'</p>'+feed(c,[p for p in posts if p['label']==topic])+'<nav aria-label="Post navigation" class="cl-pager" id="blog-pager"><a href="index.html">Home</a></nav>',True)
    for filename,(title,html,listing) in pages.items():(dest/filename).write_text(page_html(c,title,html,css,runtime,listing))
    for p in posts:
        html=body(c,p,'assets/'+media_name(c,p['index']))
        article='<article class="cl-article" data-author="Colorlib Demo Editor" data-canonical="https://example.com/'+post_path(p)+'"><header class="cl-article-header"><a class="cl-back-link" href="index.html">← All stories</a><div class="cl-tags"><a href="label.html">'+escape(p['label'])+'</a></div><h1>'+escape(p['title'])+'</h1><p class="cl-byline">By Colorlib Demo Editor · <time datetime="2026-10-25T10:00:00Z">25 October 2026</time></p></header><div class="cl-reading-layout"><aside class="cl-toc" aria-label="On this page" hidden></aside><div class="cl-prose post-body">'+html+'</div></div><footer class="cl-article-footer"><p>Continue exploring</p><div class="cl-tags"><a href="label.html">'+escape(p['label'])+'</a></div></footer>'+nav()+'</article>'
        schema={'@context':'https://schema.org','@type':'BlogPosting','headline':p['title'],'datePublished':'2026-10-25T10:00:00Z','author':{'@type':'Person','name':'Colorlib Demo Editor'},'mainEntityOfPage':{'@type':'WebPage','@id':'https://example.com/'+post_path(p)}}
        (dest/('article.html' if p['index']==1 else f'article-{p["index"]:02d}.html')).write_text(page_html(c,p['title'],article,css,runtime,False,schema))
    about='<article class="cl-article"><header class="cl-article-header"><h1>About this journal</h1></header><div class="cl-reading-layout"><aside class="cl-toc" hidden></aside><div class="cl-prose"><p>'+escape(c['intro'])+'</p><h2>Made for a useful story</h2><p>This is an original Colorlib Blogger theme demonstration. Replace the example author, pages and content with your own before publishing a real site.</p><h2>Contact & credits</h2><p>Use your own contact details or a Blogger Contact Form gadget. All vector illustrations in this package were created for the collection.</p></div></div></article>'
    (dest/'page.html').write_text(page_html(c,'About this journal',about,css,runtime,False))
    devices=''.join('<section><h2>'+str(width)+'px</h2><iframe title="'+escape(c['name'])+' home at '+str(width)+' pixels" src="index.html" style="width:'+str(width)+'px;height:820px"></iframe></section>' for width in [320,375,768])
    (dest/'responsive.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(c['name'])+' responsive review</title><style>body{margin:24px;font:16px system-ui;background:#e8e8e8;color:#222}main{display:flex;gap:24px;align-items:start}h1{font-size:24px}h2{font-size:16px}iframe{border:1px solid #aaa;background:white}</style></head><body><h1>'+escape(c['name'])+' · responsive review</h1><p>Real page layouts at fixed viewport widths. Each panel scrolls independently.</p><main>'+devices+'</main></body></html>')


def demo_export(c,posts,dest):
    feed=ET.Element('{'+ATOM+'}feed')
    # Stable, distinct identities prevent cross-theme imports being deduplicated.
    blog_id=str(int(hashlib.sha256(c['slug'].encode()).hexdigest()[:15],16))
    feed_id='tag:blogger.com,1999:blog-'+blog_id
    ET.SubElement(feed,'{'+ATOM+'}id').text=feed_id+'.archive'
    ET.SubElement(feed,'{'+ATOM+'}title').text=c['name']+' demonstration content'
    ET.SubElement(feed,'{'+ATOM+'}updated').text='2026-11-05T10:00:00Z'
    for p in posts:
        entry=ET.SubElement(feed,'{'+ATOM+'}entry')
        ET.SubElement(entry,'{'+ATOM+'}id').text=feed_id+'.post-'+str(int(hashlib.sha256((c['slug']+'-'+str(p['index'])).encode()).hexdigest()[:15],16))
        stamp=(datetime(2026,10,25,10,tzinfo=timezone.utc)-timedelta(days=p['index']-1)).isoformat()
        ET.SubElement(entry,'{'+ATOM+'}published').text=stamp
        ET.SubElement(entry,'{'+ATOM+'}updated').text=stamp
        ET.SubElement(entry,'{'+ATOM+'}category',{'scheme':'http://schemas.google.com/g/2005#kind','term':BLOGGER+'/kind#post'})
        ET.SubElement(entry,'{'+ATOM+'}category',{'scheme':'http://www.blogger.com/atom/ns#','term':p['label']})
        ET.SubElement(entry,'{'+ATOM+'}title',{'type':'text'}).text=p['title']
        ET.SubElement(entry,'{'+ATOM+'}content',{'type':'html'}).text=body(c,p,ASSET_BASE+'/'+c['slug']+'/'+media_name(c,p['index']))
        author=ET.SubElement(entry,'{'+ATOM+'}author');ET.SubElement(author,'{'+ATOM+'}name').text='Colorlib Demo Editor'
        ET.SubElement(entry,'{'+ATOM+'}link',{'rel':'alternate','type':'text/html','href':'https://example.com/'+post_path(p)})
    ET.ElementTree(feed).write(dest,encoding='utf-8',xml_declaration=True)

def theme_readme(c):
    return f'''# {c['name']} — {c['audience']} Blogger theme

Version {c['version']} · Development preview · GPL v3

{c['promise']} {c['intro']}

## Install and configure

1. Back up your existing Blogger theme and widget settings. Use a test blog for this development build.
2. Open **Theme → Edit HTML** and replace the complete source with `{c['name']}-Blogger-Template.xml`.
3. Check the published page on desktop and with `?m=1` on a phone. Keep the root `b:responsive='true'` flag so Blogger serves this theme on mobile.
4. Set your title/description in Blogger Settings. Edit the header logo and pages in Layout, and the colors in **Theme Designer → Advanced → Theme colors**.
5. In **Layout → Homepage introduction**, edit the welcome copy and topic links. The default topics are {', '.join(c['topics'])}; use labels matching your actual posts.
6. Native Older/Newer links provide pagination. Featured content is the first post on the home page and is rendered by Blogger rather than fetched after load.

## Niche post format

The package includes `post-template.html` for the {c['feature'].replace('-',' ')} format. Paste the markup into a post's HTML view and replace example details with your own. You can also save it as a Blogger post template in Settings. Keep the documented classes/data attributes when using the optional controls.

All article content remains readable without JavaScript. The optional table of contents, checklist reset, printing and relevant niche enhancements are progressive enhancements. Ratings, product facts, medical/financial claims, event details and third-party services are never invented by the theme.

## Demo and assets

`{c['name']} Demo Content.xml` is a separate post-content import, not a theme. It contains twelve original illustrative articles, credited photography and the collection's original vector artwork. See `ASSETS.md` for photograph sources and their separate license. Default public artwork URLs use the live development repository; local previews include local copies. Demo identities and projects are illustrative. Do not publish the sample as factual reporting.

## Preview and validation

Open the generated `index.html` and `article.html` through the collection's local preview server. These static previews demonstrate layout; they are not a Blogger emulator. XML/JS/schema/browser checks and a real Blogger import are required before changing the status from development to a public release.

Back up the installed source before upgrades; restore that backup and your recorded widget settings to roll back. See the collection README and validation report for current status.
'''

def build_one(c):
    source=ROOT/'themes'/c['slug'];dest=OUT/c['slug'];dest.mkdir(parents=True,exist_ok=True)
    assets=dest/'assets';assets.mkdir(exist_ok=True)
    posts=json.loads((source/'demo.json').read_text())
    core_css=(ROOT/'core/base.css').read_text();theme_css=(source/'style.css').read_text();runtime=(ROOT/'core/runtime.js').read_text()
    values={k.upper():escape(str(v),quote=True) for k,v in c.items() if isinstance(v,(str,int))}
    values.update(VISUALS=showcase(c,ASSET_BASE+'/'+c['slug']),CSS=core_css,THEME_CSS=theme_css,PRINT_CSS=(ROOT/'core/print.css').read_text(),JS=runtime,HOME='',WELCOME=(source/'welcome.html').read_text(),COMMENTS=(ROOT/'core/comments.xml').read_text(),HEADING_FONT=c['heading_font'],BODY_FONT=c['body_font'])
    native="<b:loop values='data:posts' var='post'><b:if cond='data:post.isFirstPost'><b:include data='post' name='featured-post'/></b:if></b:loop>"
    values['HOME']=compose_home(c,native)
    xml=substitute((ROOT/'core/theme.xml').read_text(),values)
    ET.fromstring(xml)
    (dest/(c['name']+'-Blogger-Template.xml')).write_text(xml)
    preview_css=':root{--accent:'+c['accent']+';--paper:'+c['paper']+';--ink:'+c['ink']+';--soft:'+c['soft']+';--heading:'+c['heading_font']+';--body:'+c['body_font']+'}\n'+core_css+'\n'+theme_css+'\n'+(ROOT/'core/print.css').read_text()
    (assets/'theme.css').write_text(preview_css);(assets/'runtime.js').write_text(runtime)
    for p in posts:
        svg=cover(c,p['index']);(assets/f'cover-{p["index"]:02d}.svg').write_text(svg)
        published=ROOT/'assets'/c['slug'];published.mkdir(parents=True,exist_ok=True);(published/f'cover-{p["index"]:02d}.svg').write_text(svg)
    for image in (ROOT/'assets'/c['slug']).glob('photo-*.webp'):
        shutil.copy(image,assets/image.name)
    (assets/'photo-credits.json').write_text(json.dumps(PHOTOS[c['slug']],indent=2)+'\n')
    (dest/'post-template.html').write_text(feature(c,posts[0])+'\n')
    (dest/'README.md').write_text(theme_readme(c));shutil.copy(ROOT/'LICENSE',dest/'LICENSE')
    (dest/'ASSETS.md').write_text(asset_notes(c))
    demo_export(c,posts,dest/(c['name']+' Demo Content.xml'))
    preview(c,posts,dest,preview_css,runtime)
    return {'name':c['name'],'slug':c['slug'],'stage':c['stage'],'posts':len(posts),'xml':str((dest/(c['name']+'-Blogger-Template.xml')).relative_to(ROOT))}

def bundle(c):
    dest=OUT/c['slug'];target=OUT/'packages';target.mkdir(exist_ok=True)
    status=(ROOT/'docs/RELEASE-READINESS.md').read_text()
    status=re.sub(r'\]\((?!https?://)([^)#]+\.md)(#[^)]*)?\)',lambda m:'](docs/'+m[1]+(m[2] or '')+')',status)
    (dest/'RELEASE-STATUS.md').write_text(status)
    files=[dest/'RELEASE-STATUS.md',dest/(c['name']+'-Blogger-Template.xml'),dest/(c['name']+' Demo Content.xml'),dest/'README.md',dest/'LICENSE',dest/'ASSETS.md',dest/'post-template.html']+list((dest/'assets').glob('cover-*.svg'))+list((dest/'assets').glob('photo-*'))+[file for file in (ROOT/'docs').rglob('*') if file.is_file()]
    package_version=c['version'] if '-' in c['version'] else c['version']+'-preview'
    zip_path=target/(c['slug']+'-blogger-template-'+package_version+'.zip')
    with ZipFile(zip_path,'w',compression=ZIP_DEFLATED,compresslevel=9) as archive:
        for file in sorted(files):
            info=ZipInfo(c['name']+'-Blogger-Template/'+(file.relative_to(dest) if file.is_relative_to(dest) else file.relative_to(ROOT)).as_posix(),(2026,11,5,0,0,0));info.compress_type=ZIP_DEFLATED;info.external_attr=0o644<<16;archive.writestr(info,file.read_bytes())
    return hashlib.sha256(zip_path.read_bytes()).hexdigest()+'  '+zip_path.name

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--theme',help='Build one theme slug');parser.add_argument('--packages',action='store_true');args=parser.parse_args()
    catalog=json.loads((ROOT/'catalog.json').read_text());report=[];sums=[]
    for row in catalog:
        if args.theme and row['slug']!=args.theme:continue
        c=json.loads((ROOT/'themes'/row['slug']/'theme.json').read_text());report.append(build_one(c))
        if args.packages:sums.append(bundle(c))
        print(c['name']+': XML + 12 articles + 23 review views')
    if not report:parser.error('Unknown theme slug')
    boards(ROOT,OUT,[row for row in catalog if (OUT/row['slug']/'index.html').exists()])
    OUT.mkdir(exist_ok=True)
    if args.theme and (OUT/'build-report.json').exists():
        previous=json.loads((OUT/'build-report.json').read_text())
        combined={r['slug']:r for r in previous+report}
        report=[combined[r['slug']] for r in catalog if r['slug'] in combined]
    (OUT/'build-report.json').write_text(json.dumps(report,indent=2))
    if sums:
        checksum_path=OUT/'packages/SHA256SUMS'
        if args.theme and checksum_path.exists():
            current={line.split('  ',1)[1]:line for line in checksum_path.read_text().splitlines() if '  ' in line}
            current.update({line.split('  ',1)[1]:line for line in sums})
            sums=[current[key] for key in sorted(current)]
        checksum_path.write_text('\n'.join(sorted(sums,key=lambda line:line.split('  ',1)[1]))+'\n')
    cards=''.join('<a class="catalog-card" href="'+r['slug']+'/index.html"><img src="'+r['slug']+'/assets/photo-01-small.webp" width="400" height="300" loading="lazy" alt="'+r['name']+' illustration"><div><small>Development preview</small><h2>'+r['name']+'</h2><p>'+next(x['audience'] for x in catalog if x['slug']==r['slug'])+'</p></div></a>' for r in report)
    (OUT/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Colorlib — New Blogger Collection</title><style>*{box-sizing:border-box}body{margin:0;padding:40px;font:16px/1.5 system-ui;background:#f7f5ef;color:#242722}header{max-width:900px;margin-bottom:40px}h1{font-size:clamp(36px,5vw,70px);line-height:1.05;letter-spacing:-.05em}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}a{color:inherit;text-decoration:none;border:1px solid #ccc;background:white}a:focus-visible{outline:3px solid #245e4b;outline-offset:4px}img{width:100%;height:auto}a>div{padding:22px}h2{margin:6px 0}small{font-size:10px;text-transform:uppercase;letter-spacing:.1em}p{margin:0}header p{max-width:70ch}@media(max-width:400px){body{padding:20px}}</style></head><body><header><p>COLORLIB / BLOGGER COLLECTION</p><h1>Twenty different ways<br>to tell a useful story.</h1><p>Original niche templates built on one dependable core. These are development previews; the validation report records the checks still needed before public release.</p><p style="margin-top:18px"><a href="design-board-1-desktop.html">Compare desktop and mobile design boards →</a></p></header><main>'+cards+'</main></body></html>')

if __name__=='__main__':main()
