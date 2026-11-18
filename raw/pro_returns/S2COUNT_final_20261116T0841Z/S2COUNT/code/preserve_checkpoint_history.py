#!/usr/bin/env python3
"""Retain every superseded checkpoint file without duplicating unchanged files.

This reads only explicitly named, already-created checkpoint archives. It never
creates, changes, or removes a checkpoint. The provenance manifest records where
each old file can be recovered in the current deliverable directory.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('archives', nargs='+', type=Path)
args = parser.parse_args()
manifest_path = ROOT / 'logs' / 'checkpoint_content_history.json'
old_manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

def digest(data):
    return hashlib.sha256(data).hexdigest()

for archive in args.archives:
    archive = archive.resolve()
    stem = archive.stem
    records = []
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip()
        if bad:
            raise SystemExit('CRC failure in ' + str(archive) + ': ' + bad)
        for entry in z.infolist():
            path = PurePosixPath(entry.filename)
            if entry.is_dir():
                continue
            if path.is_absolute() or '..' in path.parts or path.parts[0] != 'S2COUNT':
                raise SystemExit('Unexpected archive path: ' + entry.filename)
            relative = Path(*path.parts[1:])
            current = ROOT / relative
            data = z.read(entry)
            expected = digest(data)
            if relative.name in {
                'E_KlyachkoMikheenkoOlshanskii_v3.pdf',
                'E_KlyachkoMikheenkoOlshanskii_v3.txt',
            }:
                records.append({'checkpoint_path': entry.filename,
                    'sha256': expected, 'retained_at': None,
                    'reason': 'Full-text public source inadvertently included in checkpoint 02; omitted from later archives as a duplicate source input. Exact source and authored audit remain in the bibliography and research notes.'})
                continue
            packaging_mutates = relative in {
                Path('logs/package_manifest.json'),
                Path('logs/checkpoint_content_history.json'),
            }
            if (not packaging_mutates and current.is_file()
                    and digest(current.read_bytes()) == expected):
                location = relative
                reason = 'Unchanged checkpoint content retained at its current path'
            else:
                location = Path('history') / stem / relative
                target = ROOT / location
                if target.exists():
                    if digest(target.read_bytes()) != expected:
                        raise SystemExit('Conflicting immutable history file: ' + str(target))
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                reason = 'Superseded working version; exact checkpoint content retained here'
            records.append({'checkpoint_path': entry.filename, 'sha256': expected,
                            'retained_at': str(location), 'reason': reason})
    old_manifest[archive.name] = {
        'archive_sha256': digest(archive.read_bytes()),
        'files': records,
    }

manifest_path.parent.mkdir(parents=True, exist_ok=True)
manifest_path.write_text(json.dumps(old_manifest, indent=2) + '\n')
for name, record in old_manifest.items():
    restored = sum(bool(r['retained_at']) and r['retained_at'].startswith('history/') for r in record['files'])
    omitted = sum(r['retained_at'] is None for r in record['files'])
    print(f'{name}: {len(record["files"])} files accounted for; {restored} historical copies; {omitted} documented source omissions')
