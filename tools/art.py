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
    elif c['slug']=='maker':
        shapes=f'<rect x="150" y="130" width="900" height="640" rx="14" fill="{paper}" stroke="{ink}" stroke-width="3"/>'
        for y in range(190,740,65):
            for x in range(205,1020,65):shapes+=f'<circle cx="{x}" cy="{y}" r="5" fill="{ink}" opacity=".18"/>'
        shapes+=f'<g transform="rotate({-16+index%4*8} 600 450)"><rect x="280" y="260" width="85" height="390" rx="16" fill="{accent}"/><path d="M245 210H405V320H245Z" fill="{ink}"/><path d="M540 220L625 260L585 690L520 675Z" fill="{accent}"/><path d="M550 210L590 130L645 145L645 235L615 275Z" fill="{ink}"/><path d="M735 230H920V650H735Z" fill="{bg}" stroke="{ink}" stroke-width="4"/>'
        for n in range(6):shapes+=f'<path d="M740 {280+n*52}H{790 if n%2 else 825}" stroke="{ink}" stroke-width="4"/>'
        shapes+='</g>'
    elif c['slug']=='muse':
        shapes=f'<ellipse cx="630" cy="760" rx="280" ry="35" fill="{ink}" opacity=".08"/><path d="M535 185Q600 150 665 185L735 285L875 350L810 490L715 455L740 750H455L480 455L385 490L320 350L460 285Z" fill="{accent}"/><path d="M535 185Q600 280 665 185M600 260V730" fill="none" stroke="{paper}" stroke-width="5" opacity=".6"/><circle cx="615" cy="345" r="7" fill="{paper}"/><circle cx="615" cy="420" r="7" fill="{paper}"/><circle cx="615" cy="495" r="7" fill="{paper}"/><path d="M190 180V710M1030 180V710" stroke="{ink}" stroke-width="2" opacity=".3"/>'
    elif c['slug']=='kinship':
        for x,y,r in [(390,290,85),(620,240,100),(805,350,65)]:
            shapes+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{accent}" opacity=".8"/><path d="M{x-r*1.4} 730Q{x-r*1.7} {y+r} {x} {y+r}Q{x+r*1.7} {y+r} {x+r*1.4} 730Z" fill="{paper}" stroke="{ink}" stroke-width="3"/>'
        shapes+=f'<path d="M210 740Q600 810 1000 710" fill="none" stroke="{accent}" stroke-width="12" stroke-linecap="round"/>'
    elif c['slug']=='companion':
        shapes=f'<path d="M390 600Q380 460 500 455Q600 340 700 455Q825 455 810 600Q805 755 600 720Q395 755 390 600Z" fill="{accent}"/>'
        for x,y,angle in [(335,350,-25),(500,245,-8),(700,245,8),(865,350,25)]:shapes+=f'<ellipse cx="{x}" cy="{y}" rx="75" ry="100" transform="rotate({angle} {x} {y})" fill="{accent}"/>'
        shapes+=f'<path d="M560 555Q600 500 640 555Q675 595 600 650Q525 595 560 555Z" fill="{paper}"/>'
    elif c['slug']=='playbook':
        shapes=f'<circle cx="600" cy="440" r="310" fill="{accent}" opacity=".12"/><path d="M340 300Q600 245 860 300L1010 650Q1020 760 880 730L735 600H465L320 730Q180 760 190 650Z" fill="{ink}" stroke="{accent}" stroke-width="6"/><path d="M350 380H410V440H470V500H410V560H350V500H290V440H350Z" fill="{accent}"/><circle cx="795" cy="405" r="27" fill="{paper}"/><circle cx="865" cy="475" r="27" fill="{accent}"/><circle cx="725" cy="475" r="27" fill="{accent}"/><circle cx="795" cy="545" r="27" fill="{paper}"/><circle cx="510" cy="560" r="45" fill="{bg}" stroke="{accent}" stroke-width="3"/><circle cx="665" cy="560" r="45" fill="{bg}" stroke="{accent}" stroke-width="3"/>'
    elif c['slug']=='soundboard':
        shapes=f'<circle cx="600" cy="400" r="290" fill="{accent}" opacity=".12"/><rect x="500" y="150" width="200" height="400" rx="100" fill="{accent}"/><path d="M450 390V440Q450 610 600 610Q750 610 750 440V390M600 610V740M485 750H715" fill="none" stroke="{ink}" stroke-width="18" stroke-linecap="round"/>'
        for i in range(5):shapes+=f'<path d="M545 {230+i*48}H655" stroke="{paper}" stroke-width="9" stroke-linecap="round"/>'
        for x,h in [(245,90),(300,170),(355,120),(850,120),(905,170),(960,90)]:shapes+=f'<rect x="{x}" y="{440-h/2}" width="18" height="{h}" rx="9" fill="{accent}" opacity=".65"/>'
    elif c['slug']=='pace':
        shapes=f'<path d="M240 100H800Q1090 450 800 800H240Q-30 450 240 100Z" fill="none" stroke="{accent}" stroke-width="10"/><path d="M285 160H755Q985 450 755 740H285Q50 450 285 160Z" fill="none" stroke="{accent}" stroke-width="6" opacity=".5"/><path d="M330 220H710Q880 450 710 680H330Q145 450 330 220Z" fill="none" stroke="{accent}" stroke-width="4" opacity=".3"/><path d="M475 310L675 430L475 550" fill="none" stroke="{ink}" stroke-width="25" stroke-linejoin="round"/><path d="M755 100V270M800 640V800" stroke="{paper}" stroke-width="30"/>'
    elif c['slug']=='ledger':
        shapes=f'<rect x="220" y="140" width="760" height="630" rx="12" fill="{paper}" stroke="{ink}" stroke-width="3"/><path d="M220 250H980M430 250V770M720 250V770" stroke="{ink}" stroke-width="3"/><rect x="750" y="170" width="180" height="38" rx="8" fill="{accent}" opacity=".25"/>'
        for n in range(5):shapes+=f'<path d="M220 {330+n*85}H980" stroke="{ink}" opacity=".2" stroke-width="2"/><rect x="255" y="{285+n*85}" width="100" height="10" fill="{accent}" opacity=".6"/><rect x="475" y="{285+n*85}" width="{100+n*16}" height="10" fill="{accent}" opacity=".25"/>'
        shapes+=f'<path d="M795 665H890M842 618V713" stroke="{accent}" stroke-width="10"/>'
    elif c['slug']=='screen':
        shapes=f'<rect x="130" y="170" width="940" height="570" fill="{ink}" stroke="{accent}" stroke-width="3"/><rect x="205" y="245" width="790" height="420" fill="{accent}" opacity=".18"/><circle cx="600" cy="440" r="150" fill="{accent}" opacity=".7"/><path d="M300 665L570 390L800 665Z" fill="{ink}"/><path d="M610 665L800 440L970 665Z" fill="{ink}"/>'
        for x in range(165,1060,85):shapes+=f'<rect x="{x}" y="190" width="30" height="24" rx="3" fill="{paper}" opacity=".7"/><rect x="{x}" y="696" width="30" height="24" rx="3" fill="{paper}" opacity=".7"/>'
    elif c['slug']=='borough':
        for n in range(5):
            x=110+n*200;h=260+(n%3)*90;y=720-h
            shapes+=f'<rect x="{x}" y="{y}" width="170" height="{h}" fill="{paper}" stroke="{ink}" stroke-width="3"/><path d="M{x-10} {y}L{x+85} {y-90}L{x+180} {y}Z" fill="{accent}"/>'
            for r in range(2):shapes+=f'<rect x="{x+25}" y="{y+35+r*80}" width="42" height="50" fill="{accent}" opacity=".35"/><rect x="{x+100}" y="{y+35+r*80}" width="42" height="50" fill="{accent}" opacity=".35"/>'
            shapes+=f'<path d="M{x+65} 720V625H{x+105}V720" fill="{accent}"/>'
        shapes+=f'<path d="M60 740H1140" stroke="{ink}" stroke-width="5"/>'
    elif c['slug']=='ceremony':
        shapes=f'<rect x="350" y="140" width="500" height="650" fill="{paper}" stroke="{accent}" stroke-width="2"/><rect x="375" y="165" width="450" height="600" fill="none" stroke="{accent}" opacity=".4"/><path d="M300 760Q160 450 315 150M900 760Q1040 450 885 150" fill="none" stroke="{accent}" stroke-width="5"/>'
        for n in range(5):
            y=220+n*100
            shapes+=f'<ellipse cx="270" cy="{y}" rx="65" ry="25" fill="{accent}" opacity=".4" transform="rotate(-25 270 {y})"/><ellipse cx="930" cy="{y}" rx="65" ry="25" fill="{accent}" opacity=".4" transform="rotate(25 930 {y})"/>'
        shapes+=f'<circle cx="570" cy="385" r="65" fill="none" stroke="{accent}" stroke-width="7"/><circle cx="635" cy="385" r="65" fill="none" stroke="{accent}" stroke-width="7"/>'
        for n,w in enumerate([210,270,180]):shapes+=f'<rect x="{600-w/2}" y="{535+n*45}" width="{w}" height="7" fill="{accent}" opacity=".5"/>'
    elif c['slug']=='cause':
        shapes=f'<circle cx="600" cy="450" r="265" fill="{accent}" opacity=".12"/>'
        for n in range(6):
            angle=n*60
            shapes+=f'<g transform="rotate({angle} 600 450)"><circle cx="600" cy="190" r="54" fill="{accent}"/><path d="M520 290Q600 230 680 290L720 410H650L600 350L550 410H480Z" fill="{ink}" opacity=".8"/></g>'
        shapes+=f'<path d="M560 420Q600 375 640 420Q675 460 600 510Q525 460 560 420Z" fill="{accent}"/>'
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
