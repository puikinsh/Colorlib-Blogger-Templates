const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {spawnSync}=require('node:child_process'),{pathToFileURL}=require('node:url');
const root=path.resolve(__dirname,'..');
const chrome=process.env.CHROME_BIN||['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','/usr/bin/google-chrome','/usr/bin/chromium'].find(fs.existsSync);
test('native audio reports failures, respects alternative sources and clears recovered errors',{skip:!chrome},()=>{
 const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'cl-audio-'));
 try{
  const pcm=Buffer.alloc(3244);pcm.write('RIFF');pcm.writeUInt32LE(3236,4);pcm.write('WAVEfmt ',8);pcm.writeUInt32LE(16,16);pcm.writeUInt16LE(1,20);pcm.writeUInt16LE(1,22);pcm.writeUInt32LE(16000,24);pcm.writeUInt32LE(32000,28);pcm.writeUInt16LE(2,32);pcm.writeUInt16LE(16,34);pcm.write('data',36);pcm.writeUInt32LE(3200,40);
  const good='data:audio/wav;base64,'+pcm.toString('base64'),bad='data:audio/wav;base64,AAAA';
  const html='<!doctype html><html lang="en"><head><meta http-equiv="Content-Security-Policy" content="default-src \'none\';media-src data:;script-src \'unsafe-inline\'"><title>Audio failures</title></head><body><p id="original">Original description</p><p id="cl-audio-status-1">Existing identifier</p><div class="cl-prose"><audio id="direct" controls preload="auto" aria-describedby="original" src="'+bad+'"></audio><audio id="alternatives" controls preload="auto"><source src="'+bad+'"><source src="'+good+'"></audio><audio id="failed" controls preload="auto"><source src="'+bad+'"><source src="'+bad+'"></audio></div><script>'+fs.readFileSync(path.join(root,'core/runtime.js'),'utf8')+`
var valid=${JSON.stringify(good)};
function check(ok,message){if(!ok)throw Error(message);}
function fail(e){document.body.dataset.result='failed';document.body.dataset.failure=e.message;}
setTimeout(function(){try{
 var direct=document.getElementById('direct'),fallback=document.getElementById('alternatives'),failed=document.getElementById('failed');
 check(!direct.nextElementSibling.hidden&&direct.nextElementSibling.textContent.includes('Audio is unavailable'),'direct source failure needs visible feedback');
 check(!failed.nextElementSibling.hidden,'all failed alternatives need visible feedback');
 check(fallback.readyState>=1&&fallback.nextElementSibling.hidden,'a working alternative must not produce a false failure');
 check(direct.getAttribute('aria-describedby').includes('original'),'preserve author description');
 check(document.getElementById(direct.getAttribute('aria-describedby').split(' ').pop())===direct.nextElementSibling,'associate feedback with affected player');
 var ids=Array.from(document.querySelectorAll('[id]')).map(e=>e.id);check(new Set(ids).size===ids.length,'avoid identifier collisions');
 direct.addEventListener('loadedmetadata',function(){try{check(direct.nextElementSibling.hidden,'clear stale failure after recovery');document.body.dataset.result='passed';}catch(e){fail(e);}});
 direct.src=valid;direct.load();
 }catch(e){fail(e);}},700);
</script></body></html>`;
  fs.writeFileSync(path.join(scratch,'index.html'),html);
  const result=spawnSync(chrome,['--headless','--disable-gpu','--no-first-run','--disable-background-networking','--user-data-dir='+path.join(scratch,'profile'),'--virtual-time-budget=2500','--dump-dom',pathToFileURL(path.join(scratch,'index.html')).href],{encoding:'utf8',timeout:30000,maxBuffer:4*1024*1024});
  assert.equal(result.status,0,result.stderr);assert.match(result.stdout,/<body[^>]*data-result="passed"/,result.stdout.match(/<body[^>]*>/)?.[0]);
 }finally{fs.rmSync(scratch,{recursive:true,force:true});}
});
