"""Audit the user-supplied archive manifest without redistributing source files."""
from pathlib import Path
import csv
import hashlib
import json
import platform
import sympy

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = WORK / 'background/MANIFEST.tsv'
    assert manifest.exists(), 'Place the supplied background extraction beside RESIDUE.'
    lines = manifest.read_text(encoding='utf-8-sig').splitlines()
    rows = list(csv.DictReader(lines[1:], delimiter='\t'))
    failures = []
    for row in rows:
        path = WORK / 'background' / row['path_in_zip']
        assert path.resolve().is_relative_to((WORK / 'background').resolve())
        if not path.exists() or path.stat().st_size != int(row['bytes']) or digest(path) != row['sha256']:
            failures.append(row['path_in_zip'])
    inputs = []
    for pattern in ['PROMPT*.md', '*RESIDUE_background.zip']:
        for path in sorted((WORK / 'upload').glob(pattern)):
            inputs.append({'name': path.name, 'bytes': path.stat().st_size, 'sha256': digest(path)})
    result = {'manifest_members': len(rows), 'hash_and_size_failures': failures,
              'status': 'PASS' if not failures else 'FAIL', 'inputs': inputs,
              'python': platform.python_version(), 'sympy': sympy.__version__,
              'platform': platform.platform(),
              'note': 'Input sources are user supplied and are not redistributed in this package.'}
    Path(__file__).with_name('input_provenance.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    assert not failures


if __name__ == '__main__':
    main()
