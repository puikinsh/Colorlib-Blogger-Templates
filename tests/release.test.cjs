const test=require('node:test'),assert=require('node:assert/strict');
const path=require('node:path');
const {spawnSync}=require('node:child_process');
const root=path.resolve(__dirname,'..');
function python(code){const run=spawnSync(process.env.PYTHON||'python3',['-c',code],{cwd:root,encoding:'utf8'});assert.equal(run.status,0,run.stderr||run.stdout);}
test('all twenty packages resolve their offline documentation and evidence links',()=>{
 python(`from pathlib import Path
from zipfile import ZipFile
import re,posixpath,json
from urllib.parse import unquote,urlsplit
catalog=json.loads(Path('catalog.json').read_text())
for row in catalog:
 config=json.loads((Path('themes')/row['slug']/'theme.json').read_text())
 version=config['version'] if '-' in config['version'] else config['version']+'-preview'
 with ZipFile(Path('build/packages')/(row['slug']+'-blogger-template-'+version+'.zip')) as archive:
  names=set(archive.namelist());prefix=row['name']+'-Blogger-Template/'
  assert prefix+'docs/NATIVE-MEDIA.md' in names
  assert prefix+'docs/evidence/native-media-2026-11-06.json' in names
  checked=0
  for name in names:
   if not name.endswith('.md'):continue
   for target in re.findall(r'\\]\\(([^)]+)\\)',archive.read(name).decode()):
    if urlsplit(target).scheme or target.startswith('#'):continue
    checked+=1
    local=unquote(target.split('#',1)[0])
    resolved=posixpath.normpath(posixpath.join(posixpath.dirname(name),local))
    assert resolved in names,(row['slug'],name,target)
  assert checked>=10,(row['slug'],'Too few offline links checked',checked)
 `);
});
test('staging refuses to overwrite a preview version and preserves its files',()=>{
 python(`import importlib.util,tempfile,json,sys
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('stage','tools/stage_release.py');stage=importlib.util.module_from_spec(spec);spec.loader.exec_module(stage)
with tempfile.TemporaryDirectory() as temporary:
 stage.ROOT=Path(temporary);(stage.ROOT/'catalog.json').write_text('[]')
 target=stage.ROOT/'build/releases/0.1.0-preview.3';target.mkdir(parents=True)
 marker=target/'existing.zip';marker.write_bytes(b'original release')
 with patch.object(stage.subprocess,'check_output',side_effect=['','a'*40]),patch.object(sys,'argv',['stage','--version','0.1.0-preview.3']):
  try:stage.main()
  except SystemExit as error:assert error.code==2
  else:raise AssertionError('Existing preview was accepted')
 assert marker.read_bytes()==b'original release'
 `);
});

test('standalone release notes pin report links to the source commit',()=>{
 python(`import importlib.util,tempfile
from pathlib import Path
spec=importlib.util.spec_from_file_location('stage','tools/stage_release.py');stage=importlib.util.module_from_spec(spec);spec.loader.exec_module(stage)
with tempfile.TemporaryDirectory() as temporary:
 stage.ROOT=Path(temporary);(stage.ROOT/'docs').mkdir()
 (stage.ROOT/'docs/RELEASE-READINESS.md').write_text('[Report](AUDIO-MOBILE.md#remaining) [External](https://example.com/report.md) [Section](#scope)')
 notes=stage.release_notes('0.1.0-preview.4','a'*40)
 assert '[Report](https://github.com/puikinsh/Colorlib-Blogger-Templates/blob/'+('a'*40)+'/docs/AUDIO-MOBILE.md#remaining)' in notes
 assert '[External](https://example.com/report.md)' in notes
 assert '[Section](#scope)' in notes
 assert 'Source commit: '+chr(96)+('a'*40)+chr(96) in notes
 `);
});
