#!/usr/bin/env python3
"""Copy a built Oatbase checkout and record its revision and asset checksums."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('checkout', type=Path, help='Clean Oatbase checkout after npm ci and make dist')
args = parser.parse_args()
source = args.checkout.resolve()
revision = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
status = subprocess.check_output(['git', '-C', str(source), 'status', '--porcelain', '--untracked-files=no'], text=True)
if status:
    parser.error('Commit source and distribution changes before vendoring')
files = {
    'dist/oatbase.min.css': 'oatbase.min.css',
    'dist/theme-switcher.js': 'theme-switcher.js',
    'dist/aspect-ratio.css': 'aspect-ratio.css',
    'LICENSE': 'LICENSE',
    'THIRD_PARTY_NOTICES.md': 'THIRD_PARTY_NOTICES.md',
}
# Read everything first so an incomplete build cannot partially overwrite the vendor tree.
assets = {target: (source / origin).read_bytes() for origin, target in files.items()}
destination = Path(__file__).resolve().parents[1] / 'static/vendor/oatbase'
destination.mkdir(parents=True, exist_ok=True)
for name, content in assets.items():
    (destination / name).write_bytes(content)
manifest = {
    'repository': 'https://github.com/oddship/oatbase',
    'revision': revision,
    'version': json.loads((source / 'package.json').read_text())['version'],
    'sha256': {name: hashlib.sha256(content).hexdigest() for name, content in assets.items()},
}
(destination / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(f'Vendored Oatbase {revision}')
