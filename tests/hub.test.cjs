const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {spawnSync}=require('node:child_process');
const {pathToFileURL}=require('node:url');
const audit=require('./helpers/accessibility.cjs');
const root=path.resolve(__dirname,'..');
const chrome=process.env.CHROME_BIN||['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(fs.existsSync);
test('owner controls expose grouped colors, named fallback links and native header placement',()=>{
 const source=fs.readFileSync(path.join(root,'core/theme.xml'),'utf8');
 assert.match(source,/<Group description="Theme colors" selector="body">[\s\S]*?<\/Group>/);
 assert.match(source,/data:imagePlacement == &quot;BEHIND&quot;/);
 assert.match(source,/data:imagePlacement != &quot;REPLACE&quot;/);
 for(const name of ['cl-featured-image','cl-card-image'])assert.match(source,new RegExp("class='"+name+"' expr:aria-label='data:post.title'"));
 assert.doesNotMatch(source,/<span class='cl-sr-only'><data:title\/><\/span>/);
});
test('both hub formats link every download to the versioned preview and show open checks',()=>{
 const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
 const version='0.1.0-preview.5',base='https://github.com/puikinsh/Colorlib-Blogger-Templates/releases/download/v'+version+'/';
 for(const file of ['index.html','Colorlib-Lab-Blogger-Template.xml']){
  const html=fs.readFileSync(path.join(root,'build/lab',file),'utf8');
  const links=Array.from(html.matchAll(/href="(https:\/\/github.com\/puikinsh\/Colorlib-Blogger-Templates\/releases\/download\/[^"]+\.zip)"/g),m=>m[1]);
  assert.deepEqual(links.sort(),catalog.map(c=>base+c.slug+'-blogger-template-'+version+'.zip').sort(),file);
  assert.ok(html.indexOf('Before you download')<html.indexOf('data-hub-card="true"'),file+' must disclose open testing before downloads');
  for(const text of ['Screen readers','Comment publishing','Complete demo imports','measured live performance','Physical devices'])assert.ok(html.toLowerCase().includes(text.toLowerCase()),file+' missing '+text);
  assert.ok(html.includes(base+'SHA256SUMS'));
  assert.ok(html.includes('Vimeo remains blocked')&&html.includes('audible output')&&html.includes('final editorial approval'),file+' must keep media/editorial gates visible');
  assert.doesNotMatch(html,/being prepared|preview\.2 download|not these frozen download packages/);
  assert.doesNotMatch(html,/packages\/[^"]+\.zip/);
 }
});
test('lab filters, reset and responsive accessibility at five widths',{skip:!chrome},()=>{
 const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'colorlib-hub-'));
 try{
  const folder=path.join(root,'build/lab'),css=fs.readFileSync(path.join(folder,'hub.css'),'utf8'),js=fs.readFileSync(path.join(folder,'hub.js'),'utf8');
  const source=fs.readFileSync(path.join(folder,'index.html'),'utf8');
  assert.equal((source.match(/data-hub-card="true"/g)||[]).length,20);
  const checks=`function check(ok,msg){if(!ok)throw Error(msg);}try{
   check(document.documentElement.scrollWidth<=innerWidth,'horizontal overflow');
   check(document.querySelectorAll('h1').length===1,'one h1');
   var result=(${audit.toString()})();check(!result.unnamed.length,'unnamed '+JSON.stringify(result.unnamed));check(!result.contrast.length,'contrast '+JSON.stringify(result.contrast));
   var cards=[...document.querySelectorAll('[data-hub-card]')],search=document.querySelector('[data-hub-search]'),visible=()=>cards.filter(c=>!c.hidden).length;
   check(visible()===20,'all themes available');search.value='Wayfarer';search.dispatchEvent(new Event('input',{bubbles:true}));check(visible()===1,'search by theme');
   document.querySelector('[data-hub-filter="culture"]').click();check(visible()===0&&!document.querySelector('[data-hub-empty]').hidden,'combined no results');
   document.querySelector('[data-hub-reset]').click();check(visible()===20&&document.activeElement===search,'reset all and return focus');
   document.querySelector('[data-hub-filter="community"]').click();check(visible()===2,'niche filter');check(document.querySelector('[data-hub-filter="community"]').getAttribute('aria-pressed')==='true','announced selection');
   document.body.dataset.result='passed';
  }catch(e){document.body.dataset.result='failed';document.body.dataset.failure=e.message;}`;
  let html=source.replace('<link rel="stylesheet" href="hub.css">','<style>'+css+'</style>').replace('<script src="hub.js" defer></script>','<script>'+js+'\n'+checks+'</script>');
  let frames=[320,375,768,1024,1440].map(width=>({width,html}));
  const parent='<!doctype html><html><body><script>var cases='+JSON.stringify(frames).replace(/</g,'\\u003c')+';cases.forEach(c=>{var f=document.createElement("iframe");f.dataset.width=c.width;f.style="width:"+c.width+"px;height:1000px";document.body.appendChild(f);f.srcdoc=c.html;});setInterval(()=>{var frames=[...document.querySelectorAll("iframe")];if(frames.every(f=>f.contentDocument?.body?.dataset.result)){var failed=frames.filter(f=>f.contentDocument.body.dataset.result!=="passed");document.body.dataset.result=failed.length?"failed":"passed";document.body.dataset.failure=failed.map(f=>f.dataset.width+":"+f.contentDocument.body.dataset.failure).join("|");}},20);</script></body></html>';
  fs.writeFileSync(path.join(scratch,'test.html'),parent);
  const run=spawnSync(chrome,['--headless','--disable-gpu','--no-first-run','--disable-background-networking','--user-data-dir='+path.join(scratch,'profile'),'--virtual-time-budget=4000','--dump-dom',pathToFileURL(path.join(scratch,'test.html')).href],{encoding:'utf8',timeout:30000,maxBuffer:16*1024*1024});
  assert.equal(run.status,0,run.stderr);assert.match(run.stdout,/<body[^>]*data-result="passed"/,run.stdout.match(/<body[^>]*>/)?.[0]);
 }finally{fs.rmSync(scratch,{recursive:true,force:true});}
});

test('both Labs show actual layout screenshots with direct mobile alternatives',()=>{
 const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
 const manifest=JSON.parse(fs.readFileSync(path.join(root,'assets/previews/manifest.json'),'utf8'));
 assert.equal(manifest.captures.length,40);
 for(const file of ['index.html','Colorlib-Lab-Blogger-Template.xml']){
  const html=fs.readFileSync(path.join(root,'build/lab',file),'utf8');
  for(const c of catalog){
   assert.ok(html.includes(c.slug+'-desktop.webp'),file+' desktop '+c.slug);
   assert.ok(html.includes(c.slug+'-mobile.webp'),file+' mobile '+c.slug);
  }
  assert.doesNotMatch(html,/photo-01-small.webp/);
 }
 for(const c of manifest.captures){
  const bytes=fs.readFileSync(path.join(root,'assets/previews',c.file));
  assert.equal(require('node:crypto').createHash('sha256').update(bytes).digest('hex'),c.sha256);
  assert.ok(fs.existsSync(path.join(root,'build/lab/previews',c.file)));
 }
});
