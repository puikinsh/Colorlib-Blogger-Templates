const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {spawnSync}=require('node:child_process'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..'),catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json')));
const chrome=process.env.CHROME_BIN||['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(fs.existsSync);
test('all generated templates preserve accessible native comment hooks',()=>{
 for(const row of catalog){const xml=fs.readFileSync(path.join(root,'build',row.slug,row.name+'-Blogger-Template.xml'),'utf8');
  assert.match(xml,/<h2 id='comments-heading'>/);assert.match(xml,/<h3 id='comment-post-message'>/);
  for(const anchor of xml.matchAll(/<a[^>]*id='comment-editor-src'[^>]*\/>/g)){assert.match(anchor[0],/hidden='hidden'/);assert.match(anchor[0],/tabindex='-1'/);}
  assert.equal([...xml.matchAll(/<iframe[^>]*id='comment-editor'/g)].length,4);
  for(const frame of xml.matchAll(/<iframe[^>]*\/>/g))if(frame[0].includes("id='comment-editor'"))assert.match(frame[0],/title='Post a comment'/);
 }
});
test('native comment threads retain hidden states, spacing and narrow layouts for all themes',{skip:!chrome},()=>{
 const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'cl-comments-'));
 try{
  const body=fs.readFileSync(path.join(__dirname,'fixtures-comment-thread.html'),'utf8');
  const checks=`try{function check(ok,msg){if(!ok)throw Error(msg);}
   check(document.documentElement.scrollWidth<=innerWidth,'comment overflow');
   document.querySelectorAll('.comments .hidden').forEach(e=>check(getComputedStyle(e).display==='none','inactive controls exposed'));
   check(getComputedStyle(document.getElementById('comment-editor-src')).display==='none','relay link exposed');
   var header=document.querySelector('.comment-header'),author=header.querySelector('.user').getBoundingClientRect(),date=header.querySelector('.datetime').getBoundingClientRect();
   check(date.top>=author.bottom-1||date.left>=author.right+1,'author and date must not run together');
   check(document.getElementById('comments-heading').tagName==='H2','comment heading');
   document.body.dataset.result='passed';
  }catch(e){document.body.dataset.result='failed';document.body.dataset.failure=e.message;}`;
  let cases=[];for(const row of catalog)for(const width of [320,768]){let css=fs.readFileSync(path.join(root,'build',row.slug,'assets/theme.css'),'utf8');cases.push({name:row.slug+' at '+width,width,html:'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>'+css+'</style></head><body class="theme-'+row.slug+'"><div class="cl-shell">'+body+'</div><script>'+checks+'</script></body></html>'});}
  const outer='<!doctype html><html><body><script>var cases='+JSON.stringify(cases).replace(/</g,'\\u003c')+';cases.forEach(c=>{var f=document.createElement("iframe");f.dataset.name=c.name;f.style="width:"+c.width+"px;height:1200px";document.body.appendChild(f);f.srcdoc=c.html;});setInterval(()=>{var fs=[...document.querySelectorAll("iframe")];if(fs.every(f=>f.contentDocument?.body?.dataset.result)){var failed=fs.filter(f=>f.contentDocument.body.dataset.result!=="passed");document.body.dataset.result=failed.length?"failed":"passed";document.body.dataset.failure=failed.map(f=>f.dataset.name+":"+f.contentDocument.body.dataset.failure).join("|");}},20);</script></body></html>';
  fs.writeFileSync(path.join(scratch,'test.html'),outer);const run=spawnSync(chrome,['--headless','--disable-gpu','--no-first-run','--disable-background-networking','--user-data-dir='+path.join(scratch,'profile'),'--virtual-time-budget=4000','--dump-dom',pathToFileURL(path.join(scratch,'test.html')).href],{encoding:'utf8',timeout:30000,maxBuffer:20*1024*1024});
  assert.equal(run.status,0,run.stderr);assert.match(run.stdout,/<body[^>]*data-result="passed"/,run.stdout.match(/<body[^>]*>/)?.[0]);
 }finally{fs.rmSync(scratch,{recursive:true,force:true});}
});
