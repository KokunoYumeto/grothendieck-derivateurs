#!/usr/bin/env python3
"""Read-only audit of the assembled CATHOT source and statement register."""
from pathlib import Path
import collections
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
seen = []

def expand(rel):
    path = ROOT / rel
    if rel in seen:
        print("REPEATED_INPUT", rel)
    seen.append(rel)
    text = path.read_text()
    def replace(match):
        child = match.group(1)
        if not child.endswith('.tex'):
            child += '.tex'
        if not (ROOT / child).is_file():
            print("MISSING_INPUT", child)
            return ''
        return expand(child)
    return re.sub(r'\\input\{([^}]+)\}', replace, text)

text = expand('CATHOT_paper.tex')
claim_re = re.compile(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{claim\}', re.S)
claims = list(claim_re.finditer(text))
by_id = {m[1]: m for m in claims}
counts = collections.Counter(m[1] for m in claims)
print('INPUTS', ', '.join(seen))
print('CLAIMS', len(claims), 'UNIQUE', len(by_id))
print('PART_COUNTS', dict(collections.Counter(m[1].split('.')[0] for m in claims)))
print('STATUSES', dict(collections.Counter(m[2] for m in claims)))
print('DUPLICATE_IDS', [key for key, n in counts.items() if n > 1])
print('OPEN_IDS', [m[1] for m in claims if m[2] == 'Open'])
print('E_IDS', [m[1] for m in claims if m[1].startswith('E.')])

with (ROOT / 'CATHOT_results.csv').open(newline='') as stream:
    reader = csv.DictReader(stream)
    headers = reader.fieldnames
    rows = list(reader)
print('CSV_HEADERS', headers)
print('CSV_ROWS', len(rows))
csv_counts = collections.Counter(row['id'] for row in rows)
print('DUPLICATE_CSV_IDS', [key for key, n in csv_counts.items() if n > 1])
print('MISSING_CSV_IDS', sorted(set(by_id) - set(csv_counts)))
print('EXTRA_CSV_IDS', sorted(set(csv_counts) - set(by_id)))
norm = lambda value: re.sub(r'\s+', ' ', value).strip()
for row in rows:
    if row['id'] not in by_id:
        continue
    claim = by_id[row['id']]
    if row['status'] != claim[2]:
        print('STATUS_MISMATCH', row['id'], row['status'], claim[2])
    expected = norm(claim[3] + ': ' + claim[4])
    if norm(row['statement']) != expected:
        print('STATEMENT_TEXT_MISMATCH', row['id'])
        print('CSV_TEXT', norm(row['statement']))
        print('TEX_TEXT', expected)
    location = row['where_proved'].split(',')[0]
    if not (ROOT / location).is_file():
        print('BAD_LOCATION', row['id'], location)
    if row['status'] not in {'Proved', 'Refuted', 'Known', 'Open'}:
        print('INVALID_STATUS', row['id'], row['status'])

bib = (ROOT / 'CATHOT_references.bib').read_text()
entries = list(re.finditer(r'@([A-Za-z]+)\s*\{\s*([^,]+),', bib))
bib_counts = collections.Counter(match[2].strip() for match in entries)
keys = set(bib_counts)
citations = set()
for match in re.finditer(r'\\cite[a-zA-Z*]*(?:\s*\[[^\]]*\])*\s*\{([^}]+)\}', text):
    citations.update(key.strip() for key in match[1].split(','))
print('BIB_ENTRIES', len(entries))
print('DUPLICATE_BIB_KEYS', [key for key, n in bib_counts.items() if n > 1])
print('CITED_KEYS', len(citations))
print('UNDEFINED_CITATION_KEYS', sorted(citations - keys))
print('UNCITED_BIB_KEYS', sorted(keys - citations))
for i, entry in enumerate(entries):
    end = entries[i + 1].start() if i + 1 < len(entries) else len(bib)
    body = bib[entry.end():end]
    if not re.search(r'note\s*=\s*\{\s*(?:unverified|verified)\b', body, re.I):
        print('MISSING_VERIFICATION_NOTE', entry[2])

labels = set(re.findall(r'\\label\{([^}]+)\}', text)) | {'stmt:' + key for key in by_id}
refs = set(re.findall(r'\\(?:eqref|ref|autoref|pageref)\{([^}]+)\}', text))
print('UNDEFINED_REFERENCE_LABELS', sorted(refs - labels))
report = (ROOT / 'CATHOT_report.md').read_text()
mentioned_ids = set(re.findall(r'\b[A-G]\.\d+\b', text + '\n' + report))
print('UNDEFINED_LITERAL_STATEMENT_IDS', sorted(mentioned_ids - set(by_id)))
for filename in ('assemble.py', 'build.py', 'validate_package.py'):
    if filename in report and not (ROOT / 'code' / filename).is_file():
        print('REPORT_REFERENCES_MISSING_PROGRAM', filename)
print('AUDIT_FINISHED')
