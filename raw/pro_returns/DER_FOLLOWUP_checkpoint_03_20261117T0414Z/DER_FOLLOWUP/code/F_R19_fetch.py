#!/usr/bin/env python3
"""Fetch public R19 formal-source files; no credentials and no Lean execution.

Raw repository files are checked against the already downloaded recursive tree.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json, urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'notes' / 'R19_public_sources'
TREE = json.loads((DEST / 'tree.json').read_text())
BLOBS = {row['path']: row['sha'] for row in TREE['tree'] if row['type'] == 'blob'}
PATHS = [
    'README.md', 'RIGHTS.md', 'lean/README.md', 'lean/lean-toolchain',
    'lean/lakefile.toml', 'lean/lake-manifest.json',
    'lean/Grothendieck/Folder104.lean', 'lean/Grothendieck/Folder106.lean',
    'docs/lean/sections/104.tex', 'docs/lean/sections/106.tex',
    'lean/Grothendieck/Upstream/SemiSimplexCategoryReedy.lean',
    '.github/workflows/lean.yml',
]
PIN = '08e7d549678e7434e4d21d95a2cefa8e74fd2acf'
URLS = {path: 'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/' + PIN + '/' + path
        for path in PATHS}
URLS.update({
    'repo_commit.json': 'https://api.github.com/repos/Commutator-IO/grothendieck-project/commits/' + PIN,
    'mathlib44731_files.json': 'https://api.github.com/repos/leanprover-community/mathlib4/pulls/44731/files',
    'mathlib44731_comments.json': 'https://api.github.com/repos/leanprover-community/mathlib4/issues/44731/comments',
    'mathlib44731_Direct.lean': 'https://raw.githubusercontent.com/mycaule/mathlib4/a38dc275ef15bfa207bd9cb3ac0f18fce7725c7c/Mathlib/AlgebraicTopology/Reedy/Direct.lean',
})

def fetch(item):
    path, url = item
    result = {'path': path, 'url': url}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'DER-FOLLOWUP-source-audit/1.0'})
        with urllib.request.urlopen(request, timeout=25) as response:
            data = response.read()
            result.update(status=response.status, bytes=len(data),
                          content_type=response.headers.get('content-type'))
        result['sha256'] = hashlib.sha256(data).hexdigest()
        actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        result['git_blob_sha1'] = actual
        if path in BLOBS:
            result['tree_blob_sha1'] = BLOBS[path]
            result['matches_tree'] = actual == BLOBS[path]
        output = DEST / path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
    except Exception as error:
        result['error'] = str(error)
    return result

with ThreadPoolExecutor(max_workers=6) as executor:
    rows = list(executor.map(fetch, URLS.items()))
report = {'date_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'tree_sha': TREE['sha'], 'attempts': rows}
(ROOT / 'code' / 'outputs' / 'F_R19_fetch.json').write_text(json.dumps(report, indent=2))
for row in rows:
    print(row['path'], row.get('status', row.get('error')), row.get('bytes', ''),
          'tree_match=' + str(row.get('matches_tree', 'n/a')))
