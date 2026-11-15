#!/usr/bin/env python3
"""Verify the supplied cumulative source archive against its supplied manifest.

Run from the conversation workspace, with upload/ and sources/ present.
This does not read or modify any source outside those supplied directories.
"""
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / 'upload' / '6_PATHS_background.zip'
MANIFEST = ROOT / 'upload' / 'MANIFEST(7).tsv'
manifest_lines = MANIFEST.read_text().splitlines()
expected_archive_hash = manifest_lines[1].split(': ', 1)[1]
digest = lambda data: hashlib.sha256(data).hexdigest()
actual_archive_hash = digest(ARCHIVE.read_bytes())
assert actual_archive_hash == expected_archive_hash
parsed = list(csv.DictReader(io.StringIO('\n'.join(manifest_lines[2:])), delimiter='\t'))
rows = [r for r in parsed if r.get('sha256') and len(r['sha256']) == 64
        and r.get('bytes', '').isdigit()]
notes = [r['path_in_zip'] for r in parsed if r not in rows]
out = []
with zipfile.ZipFile(ARCHIVE) as archive:
    actual_files = {n for n in archive.namelist() if not n.endswith('/')}
    assert actual_files == {r['path_in_zip'] for r in rows}
    for row in rows:
        name = row['path_in_zip']
        data = archive.read(name)
        assert digest(data) == row['sha256'], name
        assert len(data) == int(row['bytes']), name
        extracted = ROOT / 'sources' / name
        assert extracted.read_bytes() == data, name
        out.append({'path': name, 'bytes': len(data), 'sha256': digest(data)})
print(json.dumps({'archive': ARCHIVE.name, 'archive_sha256': actual_archive_hash,
    'manifest': MANIFEST.name, 'verified_files': len(out), 'uncompressed_bytes': sum(x['bytes'] for x in out),
    'all_archive_and_extracted_hashes_match': True,
    'manifest_nonfile_notes': notes, 'files': out}, indent=2))
