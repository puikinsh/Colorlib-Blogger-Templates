const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const {spawnSync}=require('node:child_process');
const {pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
const chrome=process.env.CHROME_BIN||['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium','/usr/bin/chromium-browser'].find(fs.existsSync);
const collectionAudit=require('./helpers/accessibility.cjs');
const runtime=fs.readFileSync(path.join(root,'core/runtime.js'),'utf8');

function runTheme(theme){
  const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'cl-collection-'));
  const folder=path.join(root,'build',theme.slug);
  const css=fs.readFileSync(path.join(folder,'assets/theme.css'),'utf8');
  const checks=`
function check(ok,message){if(!ok)throw Error(message);}
try{
 var accessibility=(${collectionAudit.toString()})();
 check(accessibility.unnamed.length===0,'unnamed controls '+JSON.stringify(accessibility.unnamed));
 check(accessibility.contrast.length===0,'text contrast '+JSON.stringify(accessibility.contrast));
 check(document.querySelectorAll('h1').length===1,'exactly one page heading');
 check(document.documentElement.scrollWidth<=innerWidth,'horizontal overflow '+document.documentElement.scrollWidth+'/'+innerWidth+' '+JSON.stringify(Array.from(document.querySelectorAll('body *')).filter(function(e){return e.getBoundingClientRect().right>innerWidth+.5;}).slice(0,3).map(function(e){return {tag:e.tagName,class:e.className,right:e.getBoundingClientRect().right};})));
 check(Array.from(document.querySelectorAll('#blog-pager a')).map(function(a){return a.getAttribute('href');}).join('|')===nativeBefore,'native page links remain intact');
 if(document.querySelector('.cl-article')&&!document.title.startsWith('Media validation')){
  var toc=document.querySelector('.cl-toc');check(toc&&!toc.hidden,'article table of contents');
  var ids=Array.from(document.querySelectorAll('[id]')).map(function(e){return e.id;});check(ids.length===new Set(ids).size,'no duplicate generated IDs');
  toc.querySelectorAll('a').forEach(function(a){check(document.getElementById(decodeURIComponent(a.hash.slice(1))),'TOC target exists');});
  var checklist=document.querySelector('.cl-checklist input');
  if(checklist){checklist.click();check(checklist.checked,'native ingredient/checklist checkbox');var reset=document.querySelector('[data-reset-checklist]');if(reset){reset.click();check(!checklist.checked,'reset works');}}
  var recipe=document.querySelector('[data-recipe]');
  if(recipe){check(recipe.hasAttribute('data-recipe-demo'),'untested demos explicitly marked');check(!recipe.querySelector('script[data-recipe-schema]'),'untested demos omit Recipe schema');}
  var audio=document.querySelector('audio');check(audio.getBoundingClientRect().width>0&&audio.getBoundingClientRect().right<=innerWidth,'native audio fits viewport');
  check(!audio.autoplay&&audio.controls,'native audio requires manual playback and retains controls');
  var media=document.querySelector('[data-video-src]');
  media.focus();media.click();var frame=document.querySelector('.cl-media-player iframe');
  check(frame&&document.activeElement===frame,'media frame receives keyboard focus');
  check(frame.getBoundingClientRect().width<=innerWidth,'media frame fits viewport');
  check(frame.getBoundingClientRect().height>=200,'embedded player retains minimum control height on narrow screens');
  check(frame.getAttribute('src')==='https://player.vimeo.com/video/76979871','autoplay and pasted API parameters removed');
  var fallback=document.querySelector('.cl-media-player .cl-actions a');check(fallback&&fallback.target==='_blank'&&fallback.rel.includes('noopener'),'blocked-player recovery link');
  check(document.querySelector('.cl-media-player [role=status]').textContent.includes('Player requested'),'no false playing claim');
  document.querySelector('.cl-media-player .cl-actions button').click();
  check(!document.querySelector('.cl-media-player iframe')&&!media.hidden&&document.activeElement===media,'close stops media and restores focus');
  media.click();check(document.querySelectorAll('.cl-media-player iframe').length===1,'retry creates one player');
  document.querySelector('.cl-media-player .cl-actions button').click();

  var budget=document.querySelector('[data-budget]');
  if(budget){var a=budget.querySelector('[name=income]'),b=budget.querySelector('[name=expenses]'),out=budget.querySelector('output');a.value='100';b.value='250';a.dispatchEvent(new Event('input',{bubbles:true}));check(out.textContent.includes('-150'),'negative difference');a.value='';a.dispatchEvent(new Event('input',{bubbles:true}));check(out.textContent.includes('Enter two'),'empty inputs');check(!budget.closest('form'),'calculator cannot submit personal values');}
 }
 document.body.dataset.testResult='passed';
}catch(error){document.body.dataset.testResult='failed';var pre=document.createElement('pre');pre.id='failure';pre.textContent=error.message;document.body.appendChild(pre);}
`;
  try{
    let frames=[];
    for(const width of [320,375,768,1024,1440])for(const page of ['index.html','article.html','media.html']){
      let html=fs.readFileSync(path.join(folder,page),'utf8')
        .replace('<head>','<head><meta http-equiv="Content-Security-Policy" content="default-src \'none\';style-src \'unsafe-inline\';script-src \'unsafe-inline\';img-src data:">')
        .replace(/<link rel="stylesheet" href="assets\/theme.css(?:\?v=[a-f0-9]+)?">/,'<style>'+css+'\n*{animation:none!important;transition:none!important}</style>')
        .replace(/<script src="assets\/runtime.js(?:\?v=[a-f0-9]+)?" defer><\/script>/,'')
        .replace(/src="assets\/cover-[^"]+"/g,'src="https://example.com/illustration.svg"');
      if(page==='article.html')html=html.replace('</div></div><footer class="cl-article-footer">','<audio controls preload="none" aria-label="Sample audio"><source src="https://example.invalid/sample.mp3" type="audio/mpeg"></audio><p><a href="https://example.invalid/sample.mp3">Open audio directly</a></p><div class="cl-video"><button data-video-src="https://player.vimeo.com/video/76979871?autoplay=1&amp;api=1" data-video-title="Official Vimeo sample">Load sample video</button></div></div></div><footer class="cl-article-footer">');
      html=html.replace('</body>','<script>var nativeBefore=Array.from(document.querySelectorAll("#blog-pager a")).map(function(a){return a.getAttribute("href");}).join("|");'+runtime+'\n'+checks+'</script></body>');
      frames.push({width,page,html});
    }
    const fixture='<!doctype html><html><body><script>var cases='+JSON.stringify(frames).replace(/</g,'\\u003c')+';cases.forEach(function(c,i){var frame=document.createElement("iframe");frame.style.cssText="display:block;width:"+c.width+"px;height:1000px;border:0";frame.dataset.case=c.page+" at "+c.width;document.body.appendChild(frame);frame.srcdoc=c.html;});setInterval(function(){var frames=Array.from(document.querySelectorAll("iframe"));var failure=frames.find(function(f){return f.contentDocument&&f.contentDocument.body&&f.contentDocument.body.dataset.testResult==="failed";});if(failure){document.body.dataset.result="failed";var pre=document.getElementById("failure")||document.createElement("pre");pre.id="failure";pre.textContent=failure.dataset.case+": "+failure.contentDocument.getElementById("failure").textContent;if(!pre.parentNode)document.body.appendChild(pre);}else if(frames.every(function(f){return f.contentDocument&&f.contentDocument.body&&f.contentDocument.body.dataset.testResult==="passed";})){document.body.dataset.result="passed";}},20);</script></body></html>';
    const file=path.join(scratch,'fixture.html');fs.writeFileSync(file,fixture);
    const r=spawnSync(chrome,['--headless','--disable-gpu','--no-first-run','--disable-background-networking','--disable-component-update','--disable-sync','--no-default-browser-check','--window-size=1440,1000','--virtual-time-budget=3500','--user-data-dir='+path.join(scratch,'profile'),'--dump-dom',pathToFileURL(file).href],{encoding:'utf8',timeout:30000,maxBuffer:8*1024*1024});
    assert.equal(r.status,0,r.error?.message||r.stderr);
    const failure=r.stdout.match(/<pre id="failure">([\s\S]*?)<\/pre>/);
    assert.ok(/<body[^>]*data-result="passed"/.test(r.stdout),failure?failure[1]:'Browser fixtures did not finish');
  }finally{fs.rmSync(scratch,{recursive:true,force:true});}
}

for(const theme of catalog)test(theme.name+' home/article at five responsive widths and progressive features',{skip:!chrome},()=>runTheme(theme));
