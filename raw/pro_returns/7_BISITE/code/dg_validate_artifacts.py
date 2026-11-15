"""Check D/G register identity, status labels, citations and proof delimiters."""
from pathlib import Path
import collections
import csv
import re

sections = Path(__file__).resolve().parents[1] / 'sections'
all_ids = []
used = set()
for part in ['D', 'G']:
    tex = (sections / f'{part}.tex').read_text()
    claims = re.findall(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}', tex)
    with (sections / f'{part}_results.csv').open() as handle:
        rows = list(csv.DictReader(handle))
    print(part, 'claims=', len(claims), 'rows=', len(rows),
          'statuses=', dict(collections.Counter(s for _, s in claims)))
    assert [(r['id'], r['status']) for r in rows] == claims
    assert all(None not in r for r in rows)
    assert tex.count(r'\begin{proof}') == tex.count(r'\end{proof}')
    all_ids.extend(a for a, _ in claims)
    for group in re.findall(r'\\cite[tp](?:\[[^]]*\])?\{([^}]+)\}', tex):
        used.update(group.split(','))
bib = (sections / 'DG_references.bib').read_text()
keys = set(re.findall(r'@[a-z]+\{([^,]+),', bib))
assert used <= keys
assert len(all_ids) == len(set(all_ids))
assert bib.count('note = {verified:') == len(keys)
print('citation keys:', sorted(used))
print('bibliography entries:', len(keys), '; every entry has a verified note')
print('All register and citation checks passed.')
