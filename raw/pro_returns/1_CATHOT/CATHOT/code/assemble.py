"""Assemble the current bibliography, full statement ledger, and audit report."""
from pathlib import Path
import csv
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'
HEADER = ['id', 'statement', 'status', 'where_proved', 'depends_on',
          'manuscript_rows_or_pages_settled', 'notes']

bib_files = ['ROOT_references.bib', 'BC_references.bib', 'F_references.bib',
             'G_references.bib', 'E_path_references.bib']
bib = '\n\n'.join((RESEARCH / name).read_text().strip() for name in bib_files) + '\n'
keys = re.findall(r'@\w+\s*\{\s*([^,]+),', bib)
assert len(keys) == len(set(keys)), 'Duplicate bibliography keys'
entries = re.split(r'(?=@\w+\s*\{)', bib)
assert all('verified' in entry.lower() for entry in entries if entry.lstrip().startswith('@'))
(ROOT / 'CATHOT_references.bib').write_text(bib)

contributions = {}
for name in ['BC_results.csv', 'F_results.csv', 'G_results.csv',
             'E_path_results.csv', 'E_ind_results.csv']:
    path = RESEARCH / name
    if path.exists():
        for row in csv.DictReader(path.open(newline='')):
            assert row['id'] not in contributions, row['id']
            contributions[row['id']] = row

sections = ['A.tex', 'BC.tex', 'D.tex', 'D_model.tex', 'E.tex',
            'E_ind.tex', 'E_local_union.tex', 'E_derived.tex', 'E_path.tex', 'F.tex', 'G.tex']
pattern = re.compile(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}\s*(.*?)\\end\{claim\}', re.S)
rows = []
sources = {}
page_numbers = {}
aux = ROOT / 'CATHOT_paper.aux'
if aux.exists():
    for sid, page in re.findall(r'\\newlabel\{stmt:([^}]+)\}\{\{[^}]*\}\{([^}]+)\}', aux.read_text()):
        page_numbers[sid] = page
root_pages = {
 'A.1':'V ms.11–13; V ms.37', 'A.2':'Conventions; XVI §1 Loc(1)–(3)',
 'A.3':'V ms.37–40, Proposition 1 and corollary',
 'A.4':'V ms.40–42, Proposition 2', 'A.5':'VII ms.128–136',
 'A.6':'VII ms.136; companion fibrancy counterexamples',
 'A.7':'V ms.44–46,50–52; IX ms.9–13',
 'D.1':'Part D(i); V ms.42–46', 'D.2':'Part D(i)–(ii)',
 'D.3':'Part D(ii); V ms.43–46', 'D.4':'Part D(ii); V ms.43–46',
 'D.5':'Part D(ii), K(C2,2)', 'D.6':'Part D(ii), S2',
 'D.7':'Part D(iii)', 'D.8':'Part D(iii); V ms.37–46',
 'D.9':'Part D(i); Raptis bounded model structures',
 'E.1':'V ms.37–44', 'E.2':'V ms.45', 'E.3':'V ms.43,46',
 'E.4':'V ms.46–49', 'E.5':'V ms.48', 'E.6':'V ms.48, extra fibrancy version',
 'E.7':'V ms.49–52', 'E.8':'VII ms.108–124',
 'E.9':'V ms.44–46,50–52; VII ms.128–136; IX ms.22–23',
 'E.10':'VII ms.128–136', 'E.11':'VII ms.127,150–156; IX ms.13',
 'E.12':'IX ms.9–13', 'E.13':'IX ms.10', 'E.14':'IX ms.22–23',
 'E.15':'IX ms.22–25', 'E.16':'All requested Part E ranges',
 'E.17':'V ms.46', 'E.18':'V ms.47–49, genuinely local unions',
 'E.19':'V ms.49–52; VII ms.108–127; IX ms.9–13'
}
root_notes = {
 'A.5':'Exact model-cylinder relation; the source is replaced and the target is fibrant.',
 'A.6':'Two distinct counterexamples; finite ingredient checks in a_finite_checks.py.',
 'D.1':'Explicit at-most-2^lambda arrow bound; natural comparison proved for all sources within lambda.',
 'D.3':'Index is arbitrary small filtered; no unsupported strictification of a general filtered Cathot diagram.',
 'D.4':'Sequential strictification only; the colimit is locally finite without requiring injective transitions.',
 'D.6':'Open in this audit; not a claim of absence of a result in the literature.',
 'D.8':'Rules out any U-small indexing category, not merely filtered ones.',
 'D.9':'Known existence route; explicit bounded cardinal construction is D.1.',
 'E.4':'Finite full stages local and fibrant; union fibrant but nonlocal. Independent local-union hypothesis is treated in E.18.',
 'E.5':'Exhaustive 729-map check; target is local but not Thomason-fibrant.',
 'E.6':'Strict retraction in the same Hot class is proved; preservation of the original Cathot class remains undecided.',
 'E.9':'Retains exact diagram-rectification and universe hypotheses.',
 'E.10':'Absolute arrow comparison is true; strict endpoint-fibre comparison can fail.',
 'E.14':'Five-arrow finite pointed example; finite products are a separate additional hypothesis.',
 'E.16':'Crosswalk records conditional and open corrections without promoting them to unconditional proofs.'
}
for filename in sections:
    path = ROOT / 'sections' / filename
    if not path.exists():
        continue
    text = path.read_text()
    matches = list(pattern.finditer(text))
    for k, match in enumerate(matches):
        sid, status, title, body = match.groups()
        assert status in {'Proved', 'Refuted', 'Known', 'Open'}, (sid, status)
        assert sid not in sources, f'Duplicate statement {sid}'
        sources[sid] = filename
        span = text[match.end():matches[k + 1].start() if k + 1 < len(matches) else len(text)]
        # Cross-references are useful audit dependencies, not a formal proof DAG.
        refs = sorted(set(re.findall(r'\b[A-G]\.\d+\b', body + '\n' + span)) - {sid},
                      key=lambda x: (x[0], int(x.split('.')[1])))
        cited = []
        for citation in re.findall(r'\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}', body + '\n' + span):
            cited.extend(x.strip() for x in citation.split(','))
        prior = contributions.get(sid, {})
        dependencies = '; '.join(dict.fromkeys(refs + cited))
        if prior.get('depends_on'):
            dependencies = prior['depends_on'] + ('; ' + dependencies if dependencies else '')
        where = f'sections/{filename}, statement {sid} and following proof/discussion'
        if sid in page_numbers:
            where += f'; PDF p. {page_numbers[sid]}'
        notes = prior.get('notes', '')
        if sid in root_notes:
            notes = (notes + ' ' + root_notes[sid]).strip()
        rows.append(dict(zip(HEADER, [sid,
            title + ': ' + re.sub(r'\s+', ' ', body).strip(), status, where,
            dependencies, prior.get('manuscript_rows_or_pages_settled') or root_pages.get(sid, ''),
            notes])))
assert rows
with (ROOT / 'CATHOT_results.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=HEADER)
    writer.writeheader()
    writer.writerows(rows)

report = (RESEARCH / 'ROOT_report.md').read_text().rstrip()
tally = Counter(row['status'] for row in rows)
report += '\n\n## Final statement inventory\n\n'
report += f"The assembled paper has {len(rows)} numbered statements: "
report += ', '.join(f'{tally[status]} {status}' for status in ['Proved','Refuted','Known','Open']) + '.\n'
report += '\nThe exact Open statement identifiers are ' + ', '.join(row['id'] for row in rows if row['status']=='Open') + '.\n'
for name in ['BC_report.md', 'F_report.md', 'G_report.md', 'E_ind_report.md', 'E_path_report.md']:
    path = RESEARCH / name
    if path.exists():
        contribution = path.read_text().strip()
        contribution = re.sub(r'^(#+) ', r'#\1 ', contribution, flags=re.M)
        report += '\n\n---\n\n' + contribution
(ROOT / 'CATHOT_report.md').write_text(report + '\n')

print(f'Bibliography: {len(keys)} unique entries, all with verification labels.')
print(f'Ledger: {len(rows)} unique statements: {dict(tally)}.')
print('Open identifiers:', ', '.join(row['id'] for row in rows if row['status']=='Open'))
print(f'Report: {len(report.split())} words.')
print('All assembly checks passed.')
