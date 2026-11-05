"""Original vector covers. No stock-image licensing or runtime asset service."""
from html import escape
import random

def cover(c,index):
    rng=random.Random(c['slug']+'-'+str(index));bg=c['soft'];ink=c['ink'];accent=c['accent'];paper=c['paper']
    top=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900" role="img"><title>{escape(c["name"])} — original editorial illustration {index}</title><rect width="1200" height="900" fill="{bg}"/>'
    shapes=''
    if c['slug']=='saffron':
        shapes=f'<path d="M0 690L1200 540V900H0Z" fill="{paper}"/><ellipse cx="600" cy="505" rx="340" ry="260" fill="{ink}" opacity=".1"/><ellipse cx="600" cy="450" rx="340" ry="260" fill="{paper}"/><ellipse cx="600" cy="450" rx="270" ry="200" fill="#d6b47b"/>'
        for i in range(32):
            x=rng.randint(390,810);y=rng.randint(310,580);r=rng.randint(20,42)
            shapes+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{[accent,"#8eaa66","#ead8a1","#b9633c"][i%4]}" stroke="{paper}" stroke-width="3"/>'
        shapes+=f'<path d="M935 240L850 690M985 255L900 705" stroke="{ink}" stroke-width="15" stroke-linecap="round"/><path d="M270 230L210 720" stroke="{accent}" stroke-width="6"/>'
    elif c['slug']=='wayfarer':
        shapes=f'<path d="M0 640Q240 450 390 640T800 560T1200 610V900H0Z" fill="{accent}" opacity=".24"/><path d="M0 740Q240 600 460 710T900 690T1200 720V900H0Z" fill="{accent}" opacity=".4"/><circle cx="940" cy="190" r="74" fill="#e9bb65"/>'
        for i in range(8):
            x=170+i*95;y=300+rng.randint(-80,140);h=rng.randint(140,290)
            shapes+=f'<rect x="{x}" y="{y}" width="82" height="{h}" fill="{paper}" stroke="{ink}" stroke-width="3"/><path d="M{x-8} {y}L{x+41} {y-54}L{x+90} {y}Z" fill="{accent}"/>'
        shapes+=f'<path d="M80 820C80 540 300 790 550 650S880 740 1140 460" fill="none" stroke="{ink}" stroke-width="6" stroke-dasharray="14 14"/>'
    elif c['slug']=='lesson':
        shapes=f'<rect x="160" y="150" width="880" height="600" rx="18" fill="{paper}" stroke="{ink}" stroke-width="4"/><path d="M160 230H1040" stroke="{ink}" stroke-width="4"/><circle cx="200" cy="190" r="9" fill="{accent}"/><circle cx="230" cy="190" r="9" fill="{accent}" opacity=".5"/><circle cx="260" cy="190" r="9" fill="{accent}" opacity=".25"/>'
        shapes+=f'<rect x="215" y="285" width="310" height="360" rx="10" fill="{bg}"/><text x="255" y="470" fill="{accent}" font-family="monospace" font-size="85">&lt;/&gt;</text>'
        for j,w in enumerate([320,380,250,350,290,185]):shapes+=f'<rect x="585" y="{300+j*53}" width="{w}" height="14" rx="7" fill="{accent}" opacity="{.85 if j==0 else .28}"/>'
    elif c['slug']=='bench':
        shapes=f'<path d="M0 750L1200 600V900H0Z" fill="{ink}" opacity=".1"/><g transform="rotate(-8 600 450)"><rect x="170" y="280" width="860" height="390" rx="26" fill="{ink}"/>'
        for r in range(4):
            for k in range(12):shapes+=f'<rect x="{200+k*67}" y="{315+r*72}" width="55" height="55" rx="7" fill="{accent if (r+k+index)%11==0 else paper}"/>'
        shapes+=f'<rect x="410" y="610" width="370" height="32" rx="7" fill="{paper}"/></g><path d="M1000 260C1050 150 900 180 920 80" stroke="{ink}" stroke-width="8" fill="none"/>'
    else:
        # Each sector has its own composition rather than substituting a logo on a stock photograph.
        kind=c['feature']
        if kind in ['plant','care','routine']:
            shapes=f'<path d="M460 630H780L735 835H505Z" fill="{accent}"/><path d="M620 665V230" stroke="{ink}" stroke-width="13"/>'
            for x,y,angle in [(470,340,-35),(770,420,35),(450,530,-50),(770,220,45)]:shapes+=f'<ellipse cx="{x}" cy="{y}" rx="150" ry="75" fill="{accent}" opacity=".7" transform="rotate({angle} {x} {y})"/>'
        elif kind in ['book','lesson','release']:
            for i in range(4):shapes+=f'<rect x="{220+i*170}" y="{220+(i%2)*45}" width="145" height="{480-(i%2)*45}" rx="4" fill="{accent if i%2 else paper}" stroke="{ink}" stroke-width="3"/><path d="M{250+i*170} 290V640" stroke="{ink}" opacity=".3" stroke-width="3"/>'
        elif kind in ['episode','spoiler','game']:
            shapes=f'<circle cx="600" cy="450" r="270" fill="{ink}"/><circle cx="600" cy="450" r="190" fill="none" stroke="{paper}" stroke-width="2" opacity=".4"/><circle cx="600" cy="450" r="85" fill="{accent}"/><path d="M580 400L660 450L580 500Z" fill="{paper}"/>'
            for i in range(14):shapes+=f'<rect x="{125+i*70}" y="{720-rng.randint(10,90)}" width="22" height="100" fill="{accent}"/>'
        elif kind in ['budget','review','impact']:
            shapes=f'<rect x="170" y="150" width="860" height="610" fill="{paper}" stroke="{ink}" stroke-width="4"/>'
            for i in range(5):shapes+=f'<rect x="{260+i*135}" y="{630-(i+1)*65}" width="75" height="{(i+1)*65}" fill="{accent}" opacity="{.3+i*.15}"/>'
            shapes+=f'<path d="M220 630H970" stroke="{ink}" stroke-width="3"/>'
        else:
            # A folded editorial spread with distinct cut-paper shapes and a consistent limited palette.
            shapes=f'<path d="M160 200L580 150L1040 215V730L620 785L160 720Z" fill="{paper}" stroke="{ink}" stroke-width="3"/><path d="M600 160L620 785" stroke="{ink}" stroke-width="3"/>'
            shapes+=f'<rect x="220" y="280" width="300" height="290" rx="{140 if index%2 else 0}" fill="{accent}"/>'
            for j,w in enumerate([280,240,290,190,260]):shapes+=f'<rect x="680" y="{300+j*65}" width="{w}" height="12" fill="{ink}" opacity=".4"/>'
    return top+shapes+'</svg>'
