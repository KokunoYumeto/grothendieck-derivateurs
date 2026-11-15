"""Validate CATHOT document structure and, optionally, its delivered ZIP.

This checks artifact integrity, not the truth of mathematical proofs.
"""
from pathlib import Path, PurePosixPath
from collections import Counter
from hashlib import sha256
import argparse
import csv
import json
import re
import stat
import zipfile
import fitz

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--archive', type=Path)
args = parser.parse_args()
expected_open = {'D.6', 'E.6', 'E.17', 'E.26', 'E.27', 'G.17'}
expected_counts = {'Proved': 59, 'Refuted': 14, 'Known': 11, 'Open': 6}
expected_columns = ['id', 'statement', 'status', 'where_proved', 'depends_on',
                    'manuscript_rows_or_pages_settled', 'notes']
seen_inputs = []

def read_tex(relative):
    assert relative not in seen_inputs, f'Repeated TeX input: {relative}'
    seen_inputs.append(relative)
    path = ROOT / relative
    assert path.is_file(), f'Missing TeX input: {relative}'
    text = path.read_text()
    def replace(match):
        child = match[1]
        if not child.endswith('.tex'):
            child += '.tex'
        return read_tex(child)
    return re.sub(r'\\input\{([^}]+)\}', replace, text)

text = read_tex('CATHOT_paper.tex')
pattern = re.compile(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}\s*(.*?)\\end\{claim\}', re.S)
matches = list(pattern.finditer(text))
assert len(matches) == 90, f'Unexpected claim count: {len(matches)}'
claims = {m[1]: m for m in matches}
assert len(claims) == 90, 'Duplicate claim ID'
assert dict(Counter(m[2] for m in matches)) == expected_counts
assert {m[1] for m in matches if m[2] == 'Open'} == expected_open
with (ROOT / 'CATHOT_results.csv').open(newline='') as stream:
    reader = csv.DictReader(stream)
    assert reader.fieldnames == expected_columns
    rows = list(reader)
assert len(rows) == 90 and {r['id'] for r in rows} == set(claims)
normalize = lambda value: re.sub(r'\s+', ' ', value).strip()
for row in rows:
    claim = claims[row['id']]
    assert row['status'] == claim[2], row['id']
    assert normalize(row['statement']) == normalize(claim[3] + ': ' + claim[4]), row['id']
    assert (ROOT / row['where_proved'].split(',')[0]).is_file(), row['id']
    assert re.search(r'; PDF p\. \d+', row['where_proved']), row['id']
    assert row['manuscript_rows_or_pages_settled'], row['id']
print('PASS: 90 unique claims and full CSV statements match; statuses 59/14/11/6.')
print('PASS: exact Open IDs D.6, E.6, E.17, E.26, E.27, G.17; all proof locations and PDF pages recorded.')

bib = (ROOT / 'CATHOT_references.bib').read_text()
entries = list(re.finditer(r'@\w+\s*\{\s*([^,]+),', bib))
keys = [match[1].strip() for match in entries]
assert len(keys) == len(set(keys)) == 33
for index, match in enumerate(entries):
    body = bib[match.end():entries[index + 1].start() if index + 1 < len(entries) else len(bib)]
    assert re.search(r'note\s*=\s*\{\s*(?:unverified|verified)\b', body, re.I), match[1]
cites = set()
for match in re.finditer(r'\\cite\w*\*?(?:\[[^]]*\])*\{([^}]+)\}', text):
    cites.update(key.strip() for key in match[1].split(','))
assert cites <= set(keys), cites - set(keys)
labels = set(re.findall(r'\\label\{([^}]+)\}', text)) | {'stmt:' + sid for sid in claims}
references = set(re.findall(r'\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}', text))
assert references <= labels, references - labels
aux_path = ROOT / 'CATHOT_paper.aux'
if aux_path.exists():
    aux_pages = dict(re.findall(r'\\newlabel\{stmt:([^}]+)\}\{\{[^}]*\}\{([^}]+)\}', aux_path.read_text()))
    assert set(aux_pages) == set(claims)
    for row in rows:
        assert f"; PDF p. {aux_pages[row['id']]}" in row['where_proved']
print(f'PASS: {len(seen_inputs)} TeX inputs, {len(cites)} cited keys, 33 annotated bibliography entries, and internal references.')

pdf_path = ROOT / 'CATHOT_paper.pdf'
assert pdf_path.read_bytes().startswith(b'%PDF-')
with fitz.open(pdf_path) as doc:
    assert len(doc) == 63
    assert 'LuaTeX' in doc.metadata.get('producer', '')
    assert 'GPT-6 Astra' in doc.metadata.get('author', '')
    pdf_text = '\n'.join(page.get_text() for page in doc)
    assert all(sid in pdf_text for sid in claims)
    assert 'AI-produced by GPT-6 Astra' in pdf_text
    print(f"PASS: PDF has 63 pages; producer {doc.metadata['producer']}; all claim IDs and required credit are present.")
log = (ROOT / 'code' / 'final_lualatex.log').read_text()
assert 'Output written on CATHOT_paper.pdf' in log
for forbidden in ['Warning', 'Overfull', 'Underfull', 'Missing character', 'Undefined control sequence', 'Fatal error']:
    assert forbidden not in log, f'Final TeX diagnostic: {forbidden}'
build = (ROOT / 'code' / 'build_final.out').read_text()
assert build.count('exit=0') == 4 and 'Build finished successfully.' in build
assert all((ROOT / 'code' / f'build_pass_{i}.out').is_file() for i in range(1, 5))
qa = json.loads((ROOT / 'code' / 'render_pdf_qa.json').read_text())
assert qa['pages'] == 63
assert all(not row['out_of_page_text_blocks'] for row in qa['page_checks'])
assert all((ROOT / 'research' / f'pdf_visual_review_part{i}.md').is_file() for i in (1, 2))
print('PASS: all four build commands succeeded; final log has no warnings or box/font/reference diagnostics; rendering and visual-review records present.')

if args.archive:
    archive_path = args.archive.resolve()
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names)), 'Duplicate ZIP member'
        assert archive.testzip() is None, 'ZIP CRC failure'
        for item in archive.infolist():
            member = PurePosixPath(item.filename)
            assert not member.is_absolute() and '..' not in member.parts
            assert member.parts[0] == 'CATHOT'
            assert not stat.S_ISLNK(item.external_attr >> 16)
            assert '__pycache__' not in member.parts and 'tex_runtime' not in member.parts
            assert member.suffix != '.pyc'
            assert not ('research' in member.parts and member.suffix.lower() in {'.pdf', '.txt'})
        required = {'CATHOT_paper.tex', 'CATHOT_paper.pdf', 'CATHOT_results.csv',
                    'CATHOT_references.bib', 'CATHOT_report.md', 'README.md', 'CATHOT_paper.bbl'}
        assert {'CATHOT/' + name for name in required} <= set(names)
        assert {'CATHOT/' + name for name in seen_inputs} <= set(names)
        for path in (ROOT / 'code').rglob('*.py'):
            assert 'CATHOT/' + str(path.relative_to(ROOT)) in names
        manifest_name = 'CATHOT/ARCHIVE_MANIFEST.json'
        manifest = json.loads(archive.read(manifest_name))
        assert manifest['schema'] == 'cathot-sha256-v1'
        hashes = manifest['hashes']
        assert {'CATHOT/' + name for name in hashes} == set(names) - {manifest_name}
        for relative, digest in hashes.items():
            assert sha256(archive.read('CATHOT/' + relative)).hexdigest() == digest, relative
        print(f'PASS: ZIP has {len(names)} safe members; all {len(hashes)} content hashes match; no excluded third-party texts or runtime caches.')
else:
    print('Archive check not requested in this source-tree run.')
print('All requested structural checks passed. Mathematical proofs are not mechanically certified by this program.')
