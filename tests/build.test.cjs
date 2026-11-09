const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const {spawnSync}=require('node:child_process');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));

test('demo imports have unique stable identities across all twenty themes',()=>{
  const ids=[];
  for(const c of catalog){
    const xml=fs.readFileSync(path.join(root,'build',c.slug,c.name+' Demo Content.xml'),'utf8');
    const themeIds=Array.from(xml.matchAll(/<id>([^<]+)<\/id>/g),m=>m[1]);
    assert.equal(themeIds.length,13,c.slug);
    for(const id of themeIds.slice(1)){const value=BigInt(id.split('.post-')[1]);assert.ok(value>0n&&value<=9223372036854775807n,c.slug+' post IDs must fit Blogger’s signed 64-bit field');}
    ids.push(...themeIds);
  }
  assert.equal(new Set(ids).size,260,'imports must not reuse another theme’s Blogger IDs');
});

test('single-theme package rebuild preserves the gallery, report and other checksums',()=>{
  const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'cl-builder-'));
  try {
    for(const name of ['catalog.json','LICENSE','core','tools','themes','docs','assets'])fs.cpSync(path.join(root,name),path.join(scratch,name),{recursive:true});
    const build=(args)=>{
      const run=spawnSync(process.env.PYTHON||'python3',['tools/build.py',...args],{cwd:scratch,encoding:'utf8'});
      assert.equal(run.status,0,run.stderr);
    };
    build(['--packages']);
    const reportPath=path.join(scratch,'build/build-report.json');
    const sumsPath=path.join(scratch,'build/packages/SHA256SUMS');
    const report=fs.readFileSync(reportPath,'utf8');
    const sums=fs.readFileSync(sumsPath,'utf8');
    build(['--theme','saffron','--packages']);
    assert.equal(fs.readFileSync(reportPath,'utf8'),report);
    assert.equal(fs.readFileSync(sumsPath,'utf8'),sums);
    const gallery=fs.readFileSync(path.join(scratch,'build/index.html'),'utf8');
    assert.equal((gallery.match(/class="catalog-card"/g)||[]).length,20);
    const homePath=path.join(scratch,'themes/saffron/home.html');
    fs.writeFileSync(homePath,fs.readFileSync(homePath,'utf8').replace('@@FEATURED@@',''));
    const broken=spawnSync(process.env.PYTHON||'python3',['tools/build.py','--theme','saffron'],{cwd:scratch,encoding:'utf8'});
    assert.notEqual(broken.status,0,'a missing featured slot must fail instead of silently losing the first post');
    assert.match(broken.stderr,/exactly one featured-post slot/);
  } finally {
    fs.rmSync(scratch,{recursive:true,force:true});
  }
});

test('topic previews contain exactly the articles assigned to each label',()=>{
  for(const row of catalog){
    const config=JSON.parse(fs.readFileSync(path.join(root,'themes',row.slug,'theme.json'),'utf8'));
    const posts=JSON.parse(fs.readFileSync(path.join(root,'themes',row.slug,'demo.json'),'utf8'));
    for(const label of new Set([...config.topics,...posts.map(p=>p.label)])){
      const filename='label-'+label.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')+'.html';
      const html=fs.readFileSync(path.join(root,'build',row.slug,filename),'utf8');
      const actual=Array.from(html.matchAll(/<h3><a href="([^"]+)">/g),m=>m[1]).sort();
      const expected=posts.filter(p=>p.label===label).map(p=>p.index===1?'article.html':'article-'+String(p.index).padStart(2,'0')+'.html').sort();
      assert.deepEqual(actual,expected,row.slug+' / '+label);
    }
  }
});
