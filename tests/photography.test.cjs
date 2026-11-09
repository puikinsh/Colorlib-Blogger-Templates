const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),{spawnSync}=require('node:child_process');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
const photos=JSON.parse(fs.readFileSync(path.join(root,'assets/photography.json'),'utf8'));
test('photographic demos retain local responsive assets, meaningful captions and editable native galleries',()=>{
 const unique=new Set();
 for(const c of catalog){
  assert.equal(photos[c.slug].length,3,c.slug);
  const home=fs.readFileSync(path.join(root,'build',c.slug,'index.html'),'utf8');
  const native=fs.readFileSync(path.join(root,'build',c.slug,c.name+'-Blogger-Template.xml'),'utf8');
  const article=fs.readFileSync(path.join(root,'build',c.slug,'article.html'),'utf8');
  assert.match(home,/cl-visual-story cl-visual-/);assert.match(article,/cl-photo-pair/);
  assert.match(native,/name='Homepage visual notebook'/);assert.match(native,/id='HTML2' locked='false'/);
  assert.match(article,/Illustrative photography, not evidence/);
  for(const p of photos[c.slug]){
   assert.match(p.page,/^https:\/\/unsplash.com\/photos\//);assert.equal(p.license,'Unsplash License');
   assert.ok(p.author&&p.title);assert.ok(!unique.has(p.original_image));unique.add(p.original_image);
   assert.ok(home.includes(p.page));
   for(const file of [p.file,p.file.replace('.webp','-small.webp')]){
    const source=fs.readFileSync(path.join(root,'assets',c.slug,file));
    assert.equal(source.subarray(8,12).toString(),'WEBP');assert.ok(source.length<600000,c.slug+' image budget');
    assert.deepEqual(fs.readFileSync(path.join(root,'build',c.slug,'assets',file)),source);
   }
  }
  assert.match(home,/srcset="assets\/photo-\d+-small.webp 480w, assets\/photo-\d+.webp 1200w"/);
  assert.doesNotMatch(home,/src="https:\/\/images.unsplash.com/,'previews must use bundled files');
 }
 assert.equal(unique.size,60);
});
test('all twenty development packages include photographs, small variants and their separate license credits',()=>{
 const script=`from pathlib import Path\nimport json,zipfile\nr=Path('.')\nfor c in json.loads((r/'catalog.json').read_text()):\n p=next((r/'build/packages').glob(c['slug']+'-blogger-template-*.zip'))\n with zipfile.ZipFile(p) as z:\n  prefix=c['name']+'-Blogger-Template/'\n  credits=json.loads(z.read(prefix+'assets/photo-credits.json'))\n  assert len(credits)==3\n  assert b'Unsplash License' in z.read(prefix+'ASSETS.md')\n  for item in credits:\n   for name in [item['file'],item['file'].replace('.webp','-small.webp')]:\n    assert z.read(prefix+'assets/'+name)==(r/'assets'/c['slug']/name).read_bytes(),name\n`;
 const run=spawnSync(process.env.PYTHON||'python3',['-c',script],{cwd:root,encoding:'utf8'});
 assert.equal(run.status,0,run.stderr);
});
