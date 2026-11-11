"""Validate and package the complete STRATA deliverable.

The inclusion list deliberately excludes supplied attachments, downloaded
third-party papers, temporary TeX runtime files and rendered QA images.
All authored section/audit inputs and every retained program output are
included. The SHA-256 manifest covers every ZIP member except itself.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
target = ROOT.parent / 'STRATA.zip'
required = ('STRATA_paper.tex', 'STRATA_paper.pdf', 'STRATA_results.csv',
            'STRATA_references.bib', 'STRATA_report.md')
for name in required:
    assert (ROOT / name).is_file() and (ROOT / name).stat().st_size > 100, name

with (ROOT / 'STRATA_results.csv').open(newline='') as stream:
    reader = csv.DictReader(stream)
    assert reader.fieldnames == ['id', 'statement', 'status', 'where_proved',
                                'depends_on', 'manuscript_rows_or_pages_settled',
                                'notes']
    rows = list(reader)
claims = {}
for source in sorted((ROOT / 'sections').glob('*.tex')):
    for ident, status in re.findall(r'\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}',
                                    source.read_text()):
        assert ident not in claims, ident
        claims[ident] = status
assert len(rows) == len(claims)
assert {row['id']: row['status'] for row in rows} == claims
assert all('STRATA_paper.pdf p. ' in row['where_proved'] for row in rows)
assert set(claims.values()) <= {'Proved', 'Known', 'Refuted', 'Open'}

quality = json.loads((ROOT / 'code' / 'build_quality.json').read_text())
for key in ('errors', 'undefined_citations_or_references', 'missing_characters',
            'overfull_boxes', 'underfull_boxes'):
    assert not quality[key], (key, quality[key])
pdf_hash = hashlib.sha256((ROOT / 'STRATA_paper.pdf').read_bytes()).hexdigest()
qa = json.loads((ROOT / 'code' / 'pdf_qa_output.json').read_text())
visual = json.loads((ROOT / 'code' / 'visual_qa_output.json').read_text())
assert qa['sha256'] == visual['pdf_sha256'] == pdf_hash
assert not qa['fonts_not_embedded']
assert not visual['unresolved_layout_issues']
assert sorted(visual['pages_reviewed']) == list(range(1, qa['pages'] + 1))
assert len(qa['statement_pages']) == len(claims)
report = (ROOT / 'STRATA_report.md').read_text()
assert pdf_hash in report
assert 'rectangular-band monoid' in report
assert 'All finite posets with fewer than six' not in report
assert 'unresolved finite-poset test' not in report
assert 'every small poset' in report.lower()

assembly = json.loads((ROOT / 'code' / 'assemble_output.json').read_text())
assert not assembly['missing_citation_keys']
assert assembly['statements'] == len(claims)

base_files = [ROOT / name for name in required]
base_files += sorted((ROOT / 'sections').glob('*.tex'))
for pattern in ('*_report.md', '*_references.bib', '*_results.csv'):
    base_files += sorted((ROOT / 'audit').glob(pattern))
for pattern in ('*.py', '*.txt', '*.json'):
    base_files += sorted((ROOT / 'code').glob(pattern))
output_path = ROOT / 'code' / 'package_output.json'
base_files = sorted(set(base_files + [output_path]))
summary = {
    'archive': target.name,
    'member_count_including_manifest': len(base_files) + 1,
    'paper_pages': qa['pages'],
    'paper_sha256': pdf_hash,
    'statement_count': len(claims),
    'status_counts': dict(Counter(claims.values())),
    'open_statements': sorted(k for k, v in claims.items() if v == 'Open'),
    'bibliography_entries': assembly['bibliography_entries'],
    'explicitly_unverified_entries': assembly['unverified_entries'],
    'complete_page_visual_review': True,
    'compilation_clean': True,
    'all_statement_pages_recorded': True,
    'included_programs': [p.name for p in base_files if p.suffix == '.py'],
    'excluded': ['original attachments', 'downloaded third-party sources',
                 'temporary TeX runtime', 'rendered QA images',
                 'Python bytecode', 'TeX auxiliary files'],
}
output_path.write_text(json.dumps(summary, indent=2) + '\n')
manifest = ROOT / 'STRATA_manifest.sha256'
manifest.write_text(''.join(
    hashlib.sha256(path.read_bytes()).hexdigest() + '  '
    + str(path.relative_to(ROOT)) + '\n' for path in base_files))
files = base_files + [manifest]
with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as archive:
    for path in files:
        archive.write(path, Path('STRATA') / path.relative_to(ROOT))
with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(files)
    for path in files:
        data = archive.read(str(Path('STRATA') / path.relative_to(ROOT)))
        assert data == path.read_bytes(), str(path)
print(json.dumps(summary, indent=2))
print('ZIP size:', target.stat().st_size)
print('ZIP SHA-256:', hashlib.sha256(target.read_bytes()).hexdigest())
