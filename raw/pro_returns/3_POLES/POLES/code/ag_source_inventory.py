"""Index every explicit reverse-excision marker in the supplied transcription.

This lexical inventory is a navigation aid, not a proof of semantic exhaustiveness.
Run from the workspace root. No files outside the supplied source tree are read.
"""
from pathlib import Path
import csv, json, re

BASE = Path(__file__).resolve().parents[2]
sources = BASE / 'sources' / 'grothendieck'
pattern = re.compile(r'W\s*\(7|7 bis|6 b|6 c|6 C|6\$?\x27|conservati|inhabituelle|facteurs directs|136\]')
records = []
for file in sorted(sources.glob('DER_XII*/*_text.tex')) + sorted(sources.glob('DER_XVI/*_text.tex')):
    lines = file.read_text().splitlines()
    page = '?'
    for index, line in enumerate(lines):
        page_matches = re.findall(r'\\msp\{(?:page\s*)?([^}]+)\}', line)
        if page_matches:
            page = page_matches[-1]
        if pattern.search(line):
            records.append({'file': str(file.relative_to(BASE)), 'line': index+1,
                            'manuscript_page': page,
                            'text': '\n'.join(lines[max(0,index-1):min(len(lines),index+2)])})
out = BASE / 'POLES' / 'verification' / 'ag_source_inventory.json'
out.write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
print('Explicit-marker occurrences:',len(records))
for file in dict.fromkeys(row['file'] for row in records):
    selected=[row for row in records if row['file']==file]
    print(file, len(selected), 'pages:', ', '.join(dict.fromkeys(row['manuscript_page'] for row in selected)))
print('Index:',out.relative_to(BASE))
