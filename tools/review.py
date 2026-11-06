"""Static comparison boards with real desktop/mobile page viewports."""
from html import escape
from pathlib import Path
import json

def boards(root, out, catalog):
    for index in range(0,len(catalog),4):
        group=catalog[index:index+4]
        for mode,width,height,scale in [('desktop',1100,1250,.4),('mobile',375,1100,1)]:
            cards=[]
            for row in group:
                c=json.loads((root/'themes'/row['slug']/'theme.json').read_text())
                url=row['slug']+'/index.html'
                cards.append('<section><h2><a href="'+url+'">'+escape(c['name'])+' ↗</a></h2><p>'+escape(c['design_family'])+'</p><div class="viewport" style="width:'+str(width*scale)+'px;height:'+str(height*scale)+'px"><iframe title="'+escape(c['name'])+' '+mode+' layout" src="'+url+'" style="width:'+str(width)+'px;height:'+str(height)+'px;transform:scale('+str(scale)+')"></iframe></div></section>')
            nav=' '.join('<a href="design-board-'+str(i+1)+'-'+mode+'.html">Board '+str(i+1)+'</a>' for i in range((len(catalog)+3)//4))
            switch='mobile' if mode=='desktop' else 'desktop'
            page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Colorlib design board '+str(index//4+1)+'</title><style>*{box-sizing:border-box}body{margin:24px;background:#e8e8e8;color:#222;font:14px/1.5 system-ui}h1{font-size:24px;margin:0 0 8px}h2{font-size:18px;margin:0}a{color:inherit;text-underline-offset:3px}nav{display:flex;gap:20px;flex-wrap:wrap;margin:16px 0 24px}main{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px;max-width:960px}section{min-width:0}section>p{font-size:12px;margin:4px 0 12px}.viewport{overflow:hidden;border:1px solid #ccc;background:white;max-width:100%}iframe{border:0;display:block;transform-origin:top left}@media(max-width:700px){main{grid-template-columns:1fr}}</style></head><body><h1>Colorlib · '+mode+' design board '+str(index//4+1)+'</h1><p>Live pages at '+str(width)+'px. Select a name to open the full template.</p><nav><a href="index.html">Catalog</a><a href="design-board-'+str(index//4+1)+'-'+switch+'.html">'+switch.title()+' views</a>'+nav+'</nav><main>'+''.join(cards)+'</main></body></html>'
            (out/('design-board-'+str(index//4+1)+'-'+mode+'.html')).write_text(page)
