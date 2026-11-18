#!/usr/bin/env python3
"""Refresh the one-entry-per-source opening ledger from the checked records."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]


def braced(text, start):
    assert text[start] == '{'
    depth, i = 1, start + 1
    while depth:
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
        i += 1
    return text[start + 1:i - 1], i


def fields(entry):
    result = {}
    pos = 0
    while True:
        m = re.search(r'(\w+)\s*=\s*\{', entry[pos:])
        if not m:
            return result
        opening = pos + m.end() - 1
        result[m.group(1).lower()], pos = braced(entry, opening)


records = []
for path in sorted((root / 'notes').glob('*_references.bib')):
    text = path.read_text()
    for m in re.finditer(r'@\w+\s*\{\s*([^,]+),', text):
        body, _ = braced(text, text.index('{', m.start()))
        record = fields(body)
        record['key'] = m.group(1).strip()
        assert 'note' in record, record['key']
        assert re.search(r'opened|obtained', record['note'], re.I), record['key']
        records.append(record)

# The same opened source has two citation keys in the independently authored
# sections. Keep the keys but give that source only one ledger entry.
grouped = {}
for r in records:
    identity = r.get('url') or r['title'] + r.get('year', '')
    grouped.setdefault(identity, []).append(r)

lines = [(root / 'notes/SOURCE_LEDGER_named.md').read_text(),
         '\n## Primary-source entries from the bibliography\n']
for group in grouped.values():
    r = group[0]
    title = r['title'].replace('{', '').replace('}', '')
    label = ', '.join(x['key'] for x in group)
    notes = list(dict.fromkeys(x['note'] for x in group))
    link = f" [Source]({r['url']})." if r.get('url') else ''
    lines.append(f"- **{label}: {title}** — {' '.join(notes)}{link}\n")
target = root / 'DER_LOCALIZERS_source_ledger.md'
target.write_text('\n'.join(lines))
print(f'{len(records)} bibliography records; {len(grouped)} distinct primary-source entries.')
print('Updated DER_LOCALIZERS_source_ledger.md; named-record and retrieval-attempt entries retained.')
