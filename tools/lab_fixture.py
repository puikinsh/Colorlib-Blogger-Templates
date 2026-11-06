#!/usr/bin/env python3
"""Create an isolated public-lab fixture without changing packaged demo exports."""
from pathlib import Path
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json,hashlib,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
ATOM='{http://www.w3.org/2005/Atom}'
BLOGGER='http://schemas.google.com/blogger/2008'
ET.register_namespace('',ATOM[1:-1])
ET.register_namespace('blogger',BLOGGER)

def main():
    catalog=json.loads((ROOT/'catalog.json').read_text())
    feed=ET.Element(ATOM+'feed')
    source_id='tag:blogger.com,1999:blog-8600639340000000000'
    ET.SubElement(feed,ATOM+'id').text=source_id+'.archive'
    ET.SubElement(feed,ATOM+'title').text='Colorlib Blogger Theme Lab — platform fixtures'
    ET.SubElement(feed,ATOM+'updated').text='2026-11-06T12:00:00Z'
    manifest=[]
    for row in catalog:
        tree=ET.parse(ROOT/'build'/row['slug']/(row['name']+' Demo Content.xml'))
        entries=list(tree.iter(ATOM+'entry'))
        for source in entries if row['slug']=='saffron' else entries[:1]:
            entry=deepcopy(source)
            entry.find(ATOM+'id').text=source_id+'.post-'+str(int(hashlib.sha256(source.find(ATOM+'id').text.encode()).hexdigest()[:15],16))
            entry.find(ATOM+'title').text='['+row['name']+'] '+entry.find(ATOM+'title').text
            timestamp=(datetime(2026,10,25,10,tzinfo=timezone.utc)-timedelta(hours=len(manifest))).isoformat().replace('+00:00','Z')
            for field in ['published','updated']:entry.find(ATOM+field).text=timestamp
            ET.SubElement(entry,ATOM+'category',{'scheme':'http://www.blogger.com/atom/ns#','term':'Theme '+row['name']})
            feed.append(entry)
            manifest.append({'theme':row['slug'],'title':entry.find(ATOM+'title').text,'source_id':entry.find(ATOM+'id').text})
    for index,(title,html,label) in enumerate([
        ('Platform edge case: "Quotes", café & Rīga','<p>A text-only validation post with no labels or image.</p><h2>One useful heading</h2><p>Native text remains readable.</p><h2>A second heading</h2><p>Optional metadata must be omitted when absent.</p><h2>A final heading</h2><p>The contents links should resolve correctly.</p>',None),
        ('Platform edge case: heading identifiers','<p>A validation post for existing and generated heading identifiers.</p><h2 id="section-1">An existing identifier</h2><p>Keep owner-defined IDs.</p><h2>Another section</h2><p>Generate a unique target.</p><h3>A nested section</h3><p>Avoid collisions with the first heading.</p>','Rīga & notes')
    ],start=1):
        e=ET.SubElement(feed,ATOM+'entry')
        ET.SubElement(e,ATOM+'id').text=source_id+'.post-'+str(2026110600+index)
        for field in ['published','updated']:ET.SubElement(e,ATOM+field).text=f'2026-09-{20-index:02d}T10:00:00Z'
        ET.SubElement(e,ATOM+'category',{'scheme':'http://schemas.google.com/g/2005#kind','term':BLOGGER+'/kind#post'})
        if label:ET.SubElement(e,ATOM+'category',{'scheme':'http://www.blogger.com/atom/ns#','term':label})
        ET.SubElement(e,ATOM+'title',{'type':'text'}).text=title
        ET.SubElement(e,ATOM+'content',{'type':'html'}).text=html
        author=ET.SubElement(e,ATOM+'author');ET.SubElement(author,ATOM+'name').text='Colorlib Demo Editor'
        manifest.append({'theme':'edge-case','title':title,'source_id':e.find(ATOM+'id').text})
    target=ROOT/'.local-backups'/'blogger-lab';target.mkdir(parents=True,exist_ok=True)
    ET.ElementTree(feed).write(target/'platform-fixtures.xml',encoding='utf-8',xml_declaration=True)
    (target/'fixture-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(str(target/'platform-fixtures.xml')+' — '+str(len(manifest))+' posts')

if __name__=='__main__':main()
