"""Credited demonstration photography and niche-specific editorial compositions."""
from pathlib import Path
from html import escape
import json

ROOT=Path(__file__).resolve().parents[1]
PHOTOS=json.loads((ROOT/'assets/photography.json').read_text())
DIRECTIONS={
 'saffron':('Kitchen notebook','Good things, in season.','A closer look at colour, texture and the little details around the table.','Ingredients','At the table','Finishing touches','gallery'),
 'wayfarer':('A Lisbon field journal','Take the slower street.','Street corners, changing light and a little space between destinations.','Street level','A different turn','City rhythms','atlas'),
 'lesson':('The learning desk','Make room for a new idea.','A notebook, a small example and the time to work through a question.','Find your focus','Build a habit','Try it yourself','workbench'),
 'bench':('Desk study','The details make the difference.','Look closer at the tools, materials and everyday setups behind a useful review.','The setup','The small details','Daily use','workbench'),
 'maker':('Inside the workshop','A little sawdust. A good idea.','From the first sketch to the workbench: keep a record of the process.','The workspace','Tools at hand','Work in progress','gallery'),
 'muse':('The visual edit','Shape. Texture. Everyday style.','A small collection of fabrics, silhouettes and details worth noticing.','The edit','Natural textures','A fresh colour','lookbook'),
 'kinship':('Weekend journal','Leave a little room for together.','Outdoor moments, everyday rituals and stories from family life.','Outside together','Simple pleasures','Slow afternoons','journal'),
 'companion':('Out and about','Good company, every day.','Walks, quiet moments and the small routines shared with a companion.','The daily walk','A little fresh air','Time to pause','journal'),
 'shelf':('Between the shelves','There is always another chapter.','A visual wander through the places where reading begins.','On the shelf','A quiet aisle','A place to stay','lookbook'),
 'playbook':('After hours','Your next session starts here.','Controllers, comfortable setups and the space around the game.','The controller','Settle in','Take a break','magazine'),
 'soundboard':('Behind the microphone','Every good story starts somewhere.','A look at the recording space, the tools and the work behind an episode.','In the studio','Behind the scenes','On the microphone','magazine'),
 'verdant':('The growing journal','Follow the light. Watch things grow.','Greenhouses, growing spaces and the pleasure of looking a little closer.','Under glass','A little care','Growing room','gallery'),
 'pace':('Outside the routine','Find a little more open space.','A visual journal of paths, fresh air and time outdoors.','A wooded path','A wider view','On the trail','atlas'),
 'ledger':('The planning desk','Make space for a clearer picture.','Simple notebooks and thoughtful workspaces for a useful financial journal.','Start on paper','A clear workspace','Keep a record','workbench'),
 'screen':('Behind the frame','Look at the story differently.','A visual study of cameras, craft and the people behind the image.','On location','The camera','Behind the frame','magazine'),
 'borough':('Street notebook','A neighbourhood is a thousand stories.','Storefronts, shared tables and the small details that make a street.','On the corner','Shared tables','Passing through','atlas'),
 'studio':('Process, not just polish','The work behind the work.','A glimpse into creative spaces, working notes and the making of an idea.','At the desk','Space to make','Working notes','lookbook'),
 'launchpad':('Inside the workspace','Good work is a team effort.','A closer look at collaboration, working spaces and the early shape of an idea.','Working together','A shared question','Making a plan','workbench'),
 'ceremony':('A gathering in detail','The moments between the big moments.','Flowers, thoughtful tables and the setting for a shared celebration.','The setting','Around the table','In the details','lookbook'),
 'cause':('A community notebook','Small actions. Shared spaces.','Growing places, shared time and the everyday work of coming together.','Growing together','A shared space','Showing up','journal')
}

def photo(c,index):
    return PHOTOS[c['slug']][(index-1)%3]

def media_name(c,index,small=False):
    name=photo(c,index)['file']
    return name.replace('.webp','-small.webp') if small else name

def photo_tag(c,index,base,priority=False,linked=False):
    p=photo(c,index);large=base+'/'+p['file'];small=base+'/'+p['file'].replace('.webp','-small.webp')
    loading='fetchpriority="high"' if priority else 'loading="lazy"'
    return '<img src="'+escape(large,quote=True)+'" srcset="'+escape(small,quote=True)+' 480w, '+escape(large,quote=True)+' 1200w" sizes="'+('(min-width: 900px) 55vw, 100vw' if priority else '(min-width: 900px) 33vw, 100vw')+'" width="1200" height="900" '+loading+' decoding="async" alt="'+('' if linked else escape(p['title'],quote=True))+'"/>'

def credit(c,index):
    p=photo(c,index)
    return '<a href="'+escape(p['page'],quote=True)+'">'+escape(p['author'])+' / Unsplash</a>'

def showcase(c,base):
    eyebrow,title,intro,a,b,d,layout=DIRECTIONS[c['slug']]
    figures=''.join('<figure>'+photo_tag(c,i+1,base)+'<figcaption><span class="cl-kicker">0'+str(i+1)+' / '+escape(label)+'</span>'+credit(c,i+1)+'</figcaption></figure>' for i,label in enumerate([a,b,d]))
    return '<section class="cl-visual-story cl-visual-'+layout+'" aria-label="'+escape(eyebrow,quote=True)+'"><header><div><p class="cl-kicker">'+escape(eyebrow)+'</p><h2>'+escape(title)+'</h2></div><p>'+escape(intro)+'</p></header><div class="cl-visual-grid">'+figures+'</div><p class="cl-visual-credit">Photography for visual inspiration; the people, places and objects are not the subjects of the fictional demo stories.</p></section>'

def article_visuals(c,post,image_url):
    base=image_url.rsplit('/',1)[0];index=post['index'];direction=DIRECTIONS[c['slug']]
    figures=''.join('<figure>'+photo_tag(c,index+offset,base)+'<figcaption>'+credit(c,index+offset)+'</figcaption></figure>' for offset in [1,2])
    return '<section class="cl-photo-notebook"><p class="cl-kicker">'+escape(direction[0])+'</p><h2>'+escape(direction[1])+'</h2><p>'+escape(direction[2])+'</p><div class="cl-photo-pair">'+figures+'</div><p class="cl-small">Illustrative photography, not evidence of the sample project, recipe or reported event.</p></section><aside class="cl-editor-note"><p class="cl-kicker">From the editing notebook</p><blockquote><p>'+escape(post['editorial_focus'])+'</p></blockquote></aside>'


def asset_notes(c):
    return '# Asset provenance\n\nThe twelve SVG covers are original Colorlib illustrations licensed under GPL v3. Photography has its own Unsplash License, not GPL; system fonts need no downloads. No premium Unsplash+ assets are included. Photos illustrate the design and do not document fictional demo stories.\n\n'+''.join('- `'+p['file']+'` and its small variant: ['+p['title']+']('+p['page']+') by '+p['author']+'. [License]('+p['license_url']+').\n' for p in PHOTOS[c['slug']])
