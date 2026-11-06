const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {spawnSync}=require('node:child_process'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..');
const chrome=process.env.CHROME_BIN||['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(fs.existsSync);
test('optional players reject unsafe destinations and preserve keyboard focus',{skip:!chrome},()=>{
 const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'cl-media-'));
 try{
  const controls=['http://www.youtube-nocookie.com/embed/example','https://www.youtube-nocookie.com.evil.example/embed/example','https://name:password@www.youtube-nocookie.com/embed/example','https://player.vimeo.com:8443/video/123','https://player.vimeo.com/video/123?h=abc123&autoplay=1'].map((url,i)=>'<button type="button" id="video-'+i+'" data-video-src="'+url+'" data-video-title="Sample episode">Play episode '+i+'</button>').join('');
  const recipes='<article class="cl-article"><div class="cl-prose"><img src="https://example.com/dish.jpg" alt="Dish"><section data-recipe><h2 class="recipe-name">Owner recipe</h2><ul class="recipe-ingredients"><li><label>One ingredient</label></li></ul><ol class="recipe-instructions"><li>One step</li></ol></section><section data-recipe data-recipe-demo><h2 class="recipe-name">Untested sample</h2><ul class="recipe-ingredients"><li><label>One ingredient</label></li></ul><ol class="recipe-instructions"><li>One step</li></ol></section></div></article>';
  const html='<!doctype html><html lang="en"><head><meta http-equiv="Content-Security-Policy" content="default-src \'none\';script-src \'unsafe-inline\';frame-src \'none\'"><title>Optional player behavior</title></head><body>'+recipes+controls+'<script>'+fs.readFileSync(path.join(root,'core/runtime.js'),'utf8')+`\ntry{
   var schemas=document.querySelectorAll('[data-recipe-schema]');if(schemas.length!==1||JSON.parse(schemas[0].textContent).name!=='Owner recipe')throw Error('Recipe schema must require non-demo content');
   for(var i=0;i<4;i++){document.getElementById('video-'+i).click();if(document.querySelector('iframe'))throw Error('Rejected destination loaded '+i);}
   if(document.querySelectorAll('[role=status]').length!==5||!document.querySelector('[role=status]').textContent.includes('unavailable'))throw Error('Invalid URL needs an announced error');
   var button=document.getElementById('video-4');button.focus();button.click();var frame=document.querySelector('iframe');
   if(!frame||frame.title!=='Sample episode'||document.activeElement!==frame||frame.tabIndex!==0)throw Error('Player lost its accessible name or keyboard focus');
   if(frame.src!=='https://player.vimeo.com/video/123?h=abc123')throw Error('Unlisted hash must survive without autoplay');
   if(document.querySelector('.cl-media-player .cl-actions a').href!=='https://vimeo.com/123/abc123')throw Error('Fallback must open the provider watch page');
   document.querySelector('.cl-media-player .cl-actions button').click();
   if(document.querySelector('iframe')||button.hidden||document.activeElement!==button)throw Error('Close must remove playback and restore focus');
   button.click();if(document.querySelectorAll('iframe').length!==1)throw Error('Retry duplicated player');
   document.body.dataset.result='passed';
  }catch(e){document.body.dataset.result='failed';document.body.dataset.failure=e.message;}</script></body></html>`;
  fs.writeFileSync(path.join(scratch,'index.html'),html);
  const run=spawnSync(chrome,['--headless','--disable-gpu','--no-first-run','--disable-background-networking','--user-data-dir='+path.join(scratch,'profile'),'--virtual-time-budget=1500','--dump-dom',pathToFileURL(path.join(scratch,'index.html')).href],{encoding:'utf8',timeout:30000});
  assert.equal(run.status,0,run.stderr);assert.match(run.stdout,/<body[^>]*data-result="passed"/,run.stdout.match(/<body[^>]*>/)?.[0]);
 }finally{fs.rmSync(scratch,{recursive:true,force:true});}
});
