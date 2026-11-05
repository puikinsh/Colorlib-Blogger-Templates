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
    ids.push(...themeIds);
  }
  assert.equal(new Set(ids).size,260,'imports must not reuse another theme’s Blogger IDs');
});

test('single-theme package rebuild preserves the gallery, report and other checksums',()=>{
  const scratch=fs.mkdtempSync(path.join(os.tmpdir(),'cl-builder-'));
  try {
    for(const name of ['catalog.json','LICENSE','core','tools','themes'])fs.cpSync(path.join(root,name),path.join(scratch,name),{recursive:true});
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
  } finally {
    fs.rmSync(scratch,{recursive:true,force:true});
  }
});
