#!/usr/bin/env python3
"""Validate every generated deliverable; this does not emulate Blogger rendering."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,shutil,subprocess,tempfile,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
HTML='{http://www.w3.org/1999/xhtml}'
B='{http://www.google.com/2005/gml/b}'
DATA='{http://www.google.com/2005/gml/data}'

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.h1=0;self.scripts=[];self.json=False;self.current='';self.images=[];self.links=[]
    def handle_starttag(self,tag,attributes):
        a=dict(attributes)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='script' and a.get('type')=='application/ld+json':self.json=True;self.current=''
        if tag=='img':self.images.append(a)
        if tag=='a':self.links.append(a.get('href',''))
    def handle_data(self,text):
        if self.json:self.current+=text
    def handle_endtag(self,tag):
        if tag=='script' and self.json:self.scripts.append(json.loads(self.current));self.json=False

def render_schema(node,present):
    if node.tag.startswith(DATA):
        field=node.tag[len(DATA):];assert field.endswith('.jsonEscaped'),field
        key=field.removesuffix('.jsonEscaped');value='A "quoted" title \\ Rīga & notes\nsecond line'
        if 'Url' in key or '.url' in key:value='https://example.com/2026/10/post.html?a=1&b=2'
        if 'ISO8601' in key:value='2026-10-25T10:00:00Z'
        return json.dumps(value,ensure_ascii=False)[1:-1]
    active=present if node.tag==B+'if' else True
    result=(node.text or '') if active else ''
    for child in node:
        if child.tag==B+'else':active=not active
        elif active:result+=render_schema(child,present)
        if active:result+=child.tail or ''
    return result

def main():
    node=shutil.which('node');assert node,'Node.js is required'
    catalog=json.loads((ROOT/'catalog.json').read_text());assert len(catalog)==20
    assert len({c['slug'] for c in catalog})==20
    checked_scripts=set();xml_count=0;page_count=0;schema_count=0
    with tempfile.TemporaryDirectory(prefix='cl-blogger-check-') as temp:
        for row in catalog:
            config=json.loads((ROOT/'themes'/row['slug']/'theme.json').read_text());folder=ROOT/'build'/row['slug']
            source=(folder/(config['name']+'-Blogger-Template.xml')).read_text();assert '@@' not in source
            tree=ET.fromstring(source);xml_count+=1
            assert tree.get(B+'responsive')=='true',(row['slug'],'responsive routing flag')
            assert all(frame.get('title') for frame in tree.iter(HTML+'iframe') if frame.get('id')=='comment-editor'),(row['slug'],'comment iframe title')
            widgets=list(tree.iter(B+'widget'));assert len({w.get('id') for w in widgets})==len(widgets)
            assert {w.get('type') for w in widgets}=={'Header','PageList','HTML','Blog'}
            blog=next(w for w in widgets if w.get('id')=='Blog1')
            includes={x.get('id'):x for x in blog.iter(B+'includable')}
            for x in blog.iter(B+'include'):
                assert x.get('name') in includes,(row['slug'],x.get('name'))
            assert len([x for x in includes['post'].iter(B+'include') if x.get('name')=='article-schema'])==1
            assert any(x.get('name')=='post' for x in includes['mobile-post'].iter(B+'include'))
            assert all(x.get('property')=='og:type' for x in tree.iter(HTML+'meta') if x.get('property','').startswith('og:'))
            for index,script in enumerate(tree.iter(HTML+'script')):
                if script.get('type')=='application/ld+json':
                    for present in [False,True]:
                        data=json.loads(render_schema(script,present));assert data['@context']=='https://schema.org'
                        if data['@type']=='BlogPosting':assert ('image' in data)==present;assert ('dateModified' in data)==present
                    schema_count+=1;continue
                if script.get('src') or len(script):continue
                js=''.join(script.itertext())
                if js not in checked_scripts:
                    file=Path(temp)/'runtime.js';file.write_text(js);subprocess.run([node,'--check',str(file)],check=True,capture_output=True);checked_scripts.add(js)
            export=ET.parse(folder/(config['name']+' Demo Content.xml'));xml_count+=1
            entries=list(export.iter('{http://www.w3.org/2005/Atom}entry'));assert len(entries)==12
            for entry in entries:
                identifier=entry.find('{http://www.w3.org/2005/Atom}id').text
                assert 0<int(identifier.split('.post-')[1])<=9223372036854775807,(row['slug'],'64-bit post ID')
                categories=[c.attrib for c in entry.findall('{http://www.w3.org/2005/Atom}category')]
                assert {'scheme':'http://schemas.google.com/g/2005#kind','term':'http://schemas.google.com/blogger/2008/kind#post'} in categories,(row['slug'],'Blogger post kind')
                assert any(c.get('scheme')=='http://www.blogger.com/atom/ns#' and c.get('term') for c in categories),(row['slug'],'Blogger label namespace')
            for asset in (folder/'assets').glob('*.svg'):
                art=ET.parse(asset);assert not list(art.iter('{http://www.w3.org/2000/svg}script'));xml_count+=1
            for page_path in folder.glob('*.html'):
                if page_path.name=='post-template.html':continue
                page=Page();page.feed(page_path.read_text());page_count+=1
                assert page.h1==1,(row['slug'],page_path.name,'h1',page.h1)
                assert len(page.ids)==len(set(page.ids)),(row['slug'],page_path.name,'duplicate ID')
                assert all('alt' in image and 'width' in image and 'height' in image for image in page.images)
                for href in page.links:
                    if not href or href.startswith(('https:','http:','#','mailto:')):continue
                    target=href.split('?',1)[0].split('#',1)[0];assert (folder/target).exists(),(row['slug'],page_path.name,href)
            print(config['name']+': XML, native include references, schemas, demo content, assets and preview links OK')
    print(f'{xml_count} XML/SVG files; {page_count} review pages; {schema_count} schema blocks; {len(checked_scripts)} unique standalone JS blocks checked.')

if __name__=='__main__':main()
