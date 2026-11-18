#!/usr/bin/env python3
"""Verify every retained earlier checkpoint byte before final packaging."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
records = json.loads((ROOT/'logs/checkpoint_content_history.json').read_text())
summary = {}
for archive, record in records.items():
    retained = 0
    omissions = []
    for item in record['files']:
        location = item['retained_at']
        if location is None:
            assert item['reason']
            omissions.append({'path':item['checkpoint_path'], 'reason':item['reason']})
            continue
        path = ROOT / location
        assert path.is_file(), (archive, location, 'missing')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == item['sha256'], (archive, location, 'hash mismatch')
        retained += 1
    summary[archive] = {'files_accounted_for':len(record['files']),
                        'exact_retained_files':retained,
                        'documented_source_omissions':omissions}
result = {'all_retained_hashes_match':True, 'checkpoints':summary}
(ROOT/'logs/final_preservation_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
