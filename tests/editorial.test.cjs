const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..');
const catalog=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
test('all 240 demo articles have distinct editorial briefs and visible demonstration disclosure',()=>{
 const focuses=new Set();
 for(const theme of catalog){
  const posts=JSON.parse(fs.readFileSync(path.join(root,'themes',theme.slug,'demo.json'),'utf8'));
  assert.equal(posts.length,12,theme.slug);
  assert.equal(new Set(posts.map(p=>p.intro)).size,12,theme.slug+' teaser repetition');
  for(const post of posts){
   assert.ok(post.editorial_focus&&post.editorial_focus.trim().length>0,theme.slug+' / '+post.title);
   assert.ok(!focuses.has(post.editorial_focus),'duplicate brief '+post.editorial_focus);focuses.add(post.editorial_focus);
   const file=post.index===1?'article.html':'article-'+String(post.index).padStart(2,'0')+'.html';
   const html=fs.readFileSync(path.join(root,'build',theme.slug,file),'utf8');
   assert.match(html,/Demonstration editing brief, not a reported article/);
   assert.ok(html.includes(post.editorial_focus.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#x27;')),theme.slug+' missing article brief');
  }
 }
 assert.equal(focuses.size,240);
});
test('lesson examples follow their subjects and later travel briefs avoid unrelated day itineraries',()=>{
 const examples=JSON.parse(fs.readFileSync(path.join(root,'tools/lesson-examples.json'),'utf8'));
 assert.equal(new Set(examples).size,12);
 for(const [index,pattern] of [[2,/<nav/],[3,/alt=/],[4,/<label/],[8,/auto-fit/],[9,/65ch/],[10,/:focus-visible/]])assert.match(examples[index],pattern);
 for(let i=7;i<=12;i++){
  const html=fs.readFileSync(path.join(root,'build/wayfarer','article-'+String(i).padStart(2,'0')+'.html'),'utf8');
  assert.match(html,/Travel planning notebook/);assert.doesNotMatch(html,/A day in Your next destination/);
 }
 const recipe=fs.readFileSync(path.join(root,'build/saffron/article-10.html'),'utf8');
 assert.match(recipe,/<dt>Cooking<\/dt><dd>30 minutes/);assert.match(recipe,/data-recipe-demo="true"/);
 assert.doesNotMatch(recipe,/Season to taste/);
});
