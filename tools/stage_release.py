#!/usr/bin/env python3
"""Stage immutable, checksummed development-preview packages from a clean commit."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True, help='For example 0.1.0-preview.3; production staging is not enabled.')
    args = parser.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+-preview\.\d+', args.version):
        parser.error('Use a numbered preview version while release acceptance gates remain open.')
    def git(*arguments):
        return subprocess.check_output(['git', *arguments], cwd=ROOT, text=True).strip()
    if git('status', '--porcelain'):
        parser.error('Commit source and documentation before staging; the working tree must be clean.')
    revision = git('rev-parse', 'HEAD')
    base = 'https://raw.githubusercontent.com/puikinsh/Colorlib-Blogger-Templates/' + revision + '/assets'
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    target = ROOT / 'build' / 'releases' / args.version
    if target.exists() and any(target.iterdir()):
        parser.error('This preview version is already staged. Choose a new version; existing packages must not be overwritten.')
    target.mkdir(parents=True, exist_ok=True)
    records = []
    with tempfile.TemporaryDirectory(prefix='colorlib-release-') as temporary:
        checkout = Path(temporary)
        for name in ['core', 'tools', 'themes', 'assets', 'docs', 'catalog.json', 'LICENSE']:
            source = ROOT / name
            if source.is_dir():
                shutil.copytree(source, checkout / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            else:
                shutil.copy2(source, checkout / name)
        for row in catalog:
            config_path = checkout / 'themes' / row['slug'] / 'theme.json'
            config = json.loads(config_path.read_text())
            config['version'] = args.version
            config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
        env = dict(os.environ, BLOGGER_ASSET_BASE=base)
        subprocess.run([sys.executable, 'tools/build.py', '--packages'], cwd=checkout, env=env, check=True)
        subprocess.run([sys.executable, 'tools/check.py'], cwd=checkout, env=env, check=True)
        for row in catalog:
            filename = row['slug'] + '-blogger-template-' + args.version + '.zip'
            data = (checkout / 'build' / 'packages' / filename).read_bytes()
            (target / filename).write_bytes(data)
            with ZipFile(target / filename) as archive:
                members = archive.namelist()
                assert all(not name.startswith('/') and '..' not in Path(name).parts for name in members)
                folder = row['name'] + '-Blogger-Template/'
                xml = archive.read(folder + row['name'] + '-Blogger-Template.xml')
                assert ('Version: ' + args.version).encode() in xml
                demo = archive.read(folder + row['name'] + ' Demo Content.xml')
                assert base.encode() in demo and b'/codex/collection-preview/assets' not in demo
                assert folder + 'RELEASE-STATUS.md' in members
                assert folder + 'LICENSE' in members
                assert len([name for name in members if '/assets/cover-' in name]) == 12
            records.append({'theme': row['slug'], 'filename': filename, 'bytes': len(data), 'sha256': sha256(data), 'template_sha256': sha256(xml)})
    notes = '# Colorlib Blogger ' + args.version + '\n\nSource commit: `' + revision + '`\n\n' + (ROOT / 'docs/RELEASE-READINESS.md').read_text()
    (target / 'RELEASE-NOTES.md').write_text(notes)
    manifest = {'version': args.version, 'prerelease': True, 'production_ready': False, 'source_commit': revision, 'asset_base': base, 'packages': records}
    (target / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    paths = [target / record['filename'] for record in records] + [target / 'manifest.json', target / 'RELEASE-NOTES.md']
    (target / 'SHA256SUMS').write_text(''.join(sha256(path.read_bytes()) + '  ' + path.name + '\n' for path in sorted(paths)))
    print(str(target) + ' — 20 preview ZIPs, manifest, release notes and SHA256SUMS')


if __name__ == '__main__':
    main()
