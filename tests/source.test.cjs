const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));

test('twenty independent publishing formats, each with twelve distinct demo titles',()=>{
  assert.equal(catalog.length,20);
  assert.equal(new Set(catalog.map(c=>c.feature)).size,20);
  const home=new Set(),styles=new Set();
  for(const c of catalog){
    const folder=path.join(root,'themes',c.slug);
    const posts=JSON.parse(fs.readFileSync(path.join(folder,'demo.json'),'utf8'));
    assert.equal(new Set(posts.map(p=>p.title)).size,12,c.slug);
    home.add(fs.readFileSync(path.join(folder,'welcome.html'),'utf8'));
    styles.add(fs.readFileSync(path.join(folder,'style.css'),'utf8'));
  }
  assert.equal(home.size,20);assert.equal(styles.size,20);
});

function rgb(hex){return hex.slice(1).match(/../g).map(v=>parseInt(v,16)/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4);}
function luminance(hex){const [r,g,b]=rgb(hex);return .2126*r+.7152*g+.0722*b;}
function contrast(a,b){let x=luminance(a),y=luminance(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05);}
for(const c of catalog)test(c.name+' default text and accent contrast',()=>{
  const config=JSON.parse(fs.readFileSync(path.join(root,'themes',c.slug,'theme.json'),'utf8'));
  for(const bg of [config.paper,config.soft]){
    assert.ok(contrast(config.ink,bg)>=4.5,c.slug+' body text on '+bg);
    assert.ok(contrast(config.accent,bg)>=4.5,c.slug+' accent text on '+bg);
  }
});

test('the shared runtime cannot replace or recalculate native navigation',()=>{
  const runtime=fs.readFileSync(path.join(root,'core/runtime.js'),'utf8');
  assert.ok(!/document\.write|updated-max|start-index|location\.href\s*=|fetch\(/.test(runtime));
  assert.ok(!/innerHTML\s*=/.test(runtime),'dynamic headings and schema use DOM text');
});

test('local calculator has no form submission, no storage and no remote calls',()=>{
  const html=fs.readFileSync(path.join(root,'build/ledger/post-template.html'),'utf8');
  assert.ok(!/<form\b|type="submit"/.test(html));
  assert.ok(html.includes('data-budget-calculate'));
  const runtime=fs.readFileSync(path.join(root,'core/runtime.js'),'utf8');
  assert.ok(!/localStorage|sessionStorage|sendBeacon|XMLHttpRequest|fetch\(/.test(runtime));
});
