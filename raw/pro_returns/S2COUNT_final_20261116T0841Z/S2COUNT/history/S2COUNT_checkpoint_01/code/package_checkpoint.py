#!/usr/bin/env python3
"""Create a new immutable ZIP of the authored deliverable directory.

Source inputs and copies of downloaded papers are excluded and listed.
The caller controls checkpoint timing; this program never schedules itself.
"""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('destination', type=Path)
args = parser.parse_args()
destination = args.destination.resolve()
if destination.exists():
    raise SystemExit('Refusing to overwrite an existing checkpoint')
included, excluded = [], []
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if '_source.' in p.name or p.name == 'CD_Hatcher_text.txt':
        excluded.append({'path':str(rel), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                         'reason':'Full-text source input; bibliographic URL and verification notes retained'})
    elif p.suffix == '.zip' or '__pycache__' in p.parts:
        excluded.append({'path':str(rel), 'reason':'Generated archive or reproducible Python bytecode'})
    else:
        included.append(p)
manifest = ROOT/'logs'/'package_manifest.json'
manifest.write_text(json.dumps({'archive':destination.name,
    'included':[str(p.relative_to(ROOT)) for p in included],
    'excluded':excluded}, indent=2)+'\n')
if manifest not in included:
    included.append(manifest)
with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in included:
        z.write(p, 'S2COUNT/'+str(p.relative_to(ROOT)))
with zipfile.ZipFile(destination) as z:
    bad=z.testzip()
    if bad:
        raise SystemExit('CRC failure: '+bad)
print(json.dumps({'path':str(destination),'files':len(included),'bytes':destination.stat().st_size,
                  'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()}))
