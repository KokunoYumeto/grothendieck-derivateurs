"""Check the delivered research record and build a reproducible ZIP.

This checks coverage, file consistency, and recorded numerical certificates.
It does not replace the proofs or rerun the expensive AKR computations.
Run ``python code/verify_package.py --zip`` from any working directory.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / 'code'
OUT = CODE / 'outputs'
MAIN = ['TOTEX_paper.tex', 'TOTEX_paper.pdf', 'TOTEX_results.csv',
        'TOTEX_references.bib', 'TOTEX_report.md']
COLUMNS = ['id', 'statement', 'status', 'where_proved', 'depends_on',
           'manuscript_pages_settled', 'notes']
ENVS = 'theorem|proposition|lemma|corollary|definition|example|obstruction|audit|remark'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_files(paths):
    for path in paths:
        assert path.is_file() and path.stat().st_size, f'Missing or empty: {path}'


require_files([ROOT / name for name in MAIN])
tex = (ROOT / MAIN[0]).read_text(encoding='utf-8')
assert not re.search(r'\\(?:input|include)\{', tex), 'The paper must be self-contained.'
assert not any(ord(c) < 32 and c not in '\n\r' for c in tex), 'Unexpected TeX control character.'
begins = list(re.finditer(r'\\begin\{(' + ENVS + r')\}(?:\[([^\]]*)\])?', tex))
cache = read_json(CODE / 'totex_labels_cache.json')
label_map = cache['labels']
source_statements = []
for match in begins:
    environment, title = match.groups()
    end = tex.index('\\end{' + environment + '}', match.end())
    labels = re.findall(r'\\label\{([^}]+)\}', tex[match.end():end])
    assert len(labels) == 1, (environment, title, labels)
    label = labels[0]
    status = re.match(r'(Proved|Refuted|Known|Open)\b', title or '')
    assert status and label in label_map, label
    source_statements.append((label, label_map[label]['id'],
                              label_map[label]['page'], status.group(1)))
assert len(source_statements) == 58
assert len(set(x[0] for x in source_statements)) == len(source_statements)
with (ROOT / 'TOTEX_results.csv').open(newline='', encoding='utf-8') as stream:
    reader = csv.DictReader(stream)
    assert reader.fieldnames == COLUMNS, reader.fieldnames
    rows = list(reader)
assert len(rows) == len(source_statements)
for row, (label, number, page, status) in zip(rows, source_statements):
    assert None not in row and all(value is not None for value in row.values())
    assert row['id'] == number and row['status'] == status, label
    assert f'p. {page};' in row['where_proved'], label
    assert f'label {label}' in row['where_proved'], label
    assert row['statement'] and row['depends_on'] and row['notes'], label
if (ROOT / 'TOTEX_paper.aux').is_file():
    assert digest(ROOT / 'TOTEX_paper.aux') == cache['aux_sha256']

all_labels = set(re.findall(r'\\label\{([^}]+)\}', tex))
references = set(re.findall(r'\\(?:ref|eqref|pageref)\{([^}]+)\}', tex))
assert references <= all_labels, sorted(references - all_labels)
bib = (ROOT / 'TOTEX_references.bib').read_text(encoding='utf-8')
entries = re.findall(r'(?ms)^@\w+\{([^,]+),\s*(.*?)(?=^@|\Z)', bib)
assert len(entries) == 17
access = {}
for key, body in entries:
    note = re.search(r'(?i)\bnote\s*=\s*\{([^\n]+)', body)
    assert note and re.search(r'(?i)\bopened\b', note.group(1)), key
    access[key] = 'Not opened' if re.search(r'(?i)\bnot opened\b', note.group(1)) else 'Opened'
assert sorted(key for key, status in access.items() if status == 'Not opened') == [
    'GabrielUlmer1971', 'IsbellMitchell1976', 'Oberst1968']
bib_keys = set(access)
manual_keys = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', tex))
assert manual_keys == bib_keys, (manual_keys - bib_keys, bib_keys - manual_keys)
citations = set()
for match in re.finditer(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}', tex):
    citations.update(key.strip() for key in match.group(1).split(','))
assert citations <= bib_keys, citations - bib_keys

recorded = {}
for filename in ['akr_stages_output.json', 'akr_stages_triple_output.json',
                 'akr_stages_critical_output.json']:
    stages = read_json(CODE / filename)
    for stage in stages:
        assert not stage['source_rule_failures'], (filename, stage['label'])
        assert len(stage['nondegenerate_nerve_simplex_counts']) == len(stage['integral_homology_free_ranks'])
        if 'independent_mod_101_betti' in stage:
            assert stage['independent_mod_101_betti'] == stage['integral_homology_free_ranks']
        if 'relative_to_previous' in stage:
            assert not any(stage['relative_to_previous']['integral_homology_free_ranks'])
    recorded[filename] = [dict(label=s['label'],
        ranks=s['integral_homology_free_ranks'], objects=s['objects'],
        arrows=s['arrows_including_identities']) for s in stages]
assert recorded['akr_stages_output.json'][1]['ranks'] == [1, 0, 1]
assert recorded['akr_stages_output.json'][2]['ranks'] == [1, 0, 1, 0]
assert recorded['akr_stages_triple_output.json'][1]['ranks'] == [1, 0, 4]
assert recorded['akr_stages_critical_output.json'][-1]['ranks'] == [1, 0, 1, 0, 0]
literal = read_json(CODE / 'akr_stages_literal_output.json')
assert [len(s['source_rule_failures']) for s in literal] == [0, 12, 14]
assert all(f['rule'] == 'AKR (11)' for s in literal for f in s['source_rule_failures'])
assert literal[1]['integral_homology_free_ranks'] == [1, 0, 3]
assert literal[2]['integral_homology_free_ranks'] == [1, 0, 2, 1]
assert literal[2]['relative_to_previous']['integral_homology_free_ranks'] == [0, 0, 0, 2]
literal_triple = read_json(CODE / 'akr_stages_triple_literal_output.json')
assert literal_triple[1]['integral_homology_free_ranks'] == [1, 0, 10]

required_outputs = [
    'akr_stages.out', 'akr_stages_triple.out', 'akr_stages_critical.out',
    'akr_stages_literal.out', 'akr_stages_triple_literal.out', 'akr_component_checks.out',
    'examples_colored_words.out', 'examples_support_orbits.out', 'source_fetch.out',
    'outputs/basic_shape_checks.json', 'outputs/main_sign_reflection_check.json',
    'outputs/build_pdf.out', 'outputs/latex_final.out', 'outputs/pdf_layout_audit.json',
    'outputs/totex_results_audit.json', 'outputs/totex_results_source_records.json',
    'outputs/totex_results_values.json', 'outputs/totex_results_preview.png',
    'pretot_audit/outputs/independent_certificate_audit.out',
    'pretot_audit/outputs/main_counterexample.out',
    'pretot_audit/outputs/semisimplicial_affine_checks.out',
    'pretot_audit/outputs/projectivity_certificate.json',
    'pretot_audit/outputs/main_counterexample_data.json',
]
require_files([CODE / name for name in required_outputs])
ledger = read_json(OUT / 'totex_results_audit.json')
assert ledger['complete_statement_coverage'] and ledger['complete_prompt_item_coverage']
assert ledger['exact_artifact_csv_import_roundtrip']
assert ledger['csv_sha256'] == digest(ROOT / 'TOTEX_results.csv')
assert ledger['source_mode'] == 'flattened-paper'
assert any(x['file'] == 'TOTEX_paper.tex' and x['sha256'] == digest(ROOT / 'TOTEX_paper.tex')
           for x in ledger['inputs'])
log = (OUT / 'latex_final.out').read_text(encoding='utf-8')
for bad in ['undefined references', 'undefined citations', 'multiply defined',
            'Overfull \\hbox', 'Overfull \\vbox', 'LaTeX Error:']:
    assert bad.lower() not in log.lower(), bad
pdf_info = subprocess.check_output(['pdfinfo', str(ROOT / 'TOTEX_paper.pdf')], text=True)
pages = int(re.search(r'^Pages:\s+(\d+)', pdf_info, re.M).group(1))
layout = read_json(OUT / 'pdf_layout_audit.json')
assert layout['pages'] == pages == layout['rendered_pages']
assert not layout['words_outside_page']
assert layout['pdf_sha256'] == digest(ROOT / 'TOTEX_paper.pdf')
credit = 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)'
assert credit in tex and credit in (ROOT / 'TOTEX_report.md').read_text(encoding='utf-8')

audit = {
    'checks': 'PASS', 'scope': 'Coverage and file/certificate consistency, not an independent proof checker.',
    'numbered_statements': len(rows), 'status_counts': dict(Counter(r['status'] for r in rows)),
    'exact_columns': COLUMNS, 'pdf_pages': pages,
    'self_contained_tex': True, 'cross_references_resolved': True,
    'bibliography_entries': len(entries), 'source_access': access,
    'recorded_repaired_AKR_computations': recorded,
    'common_n_scope': 'Verified general B.9 substages with rank-one H2 class death; fails (11), so no C.1 certificate is inferred.',
    'main_file_sha256': {name: digest(ROOT / name) for name in MAIN},
    'required_computation_outputs': required_outputs,
}
(OUT / 'package_audit.json').write_text(json.dumps(audit, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: audit[k] for k in ['checks', 'numbered_statements', 'status_counts',
                                      'pdf_pages', 'bibliography_entries']}, indent=2))

if '--zip' in sys.argv:
    files = [ROOT / name for name in MAIN]
    files += sorted(p for p in CODE.rglob('*') if p.is_file()
                    and '__pycache__' not in p.parts and p.suffix != '.pyc'
                    and p.name != 'zip_audit.json')
    archive = ROOT / 'TOTEX_return.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in files:
            entry = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 11, 12, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, path.read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert sorted(z.namelist()) == sorted(p.relative_to(ROOT).as_posix() for p in files)
        for path in files:
            assert z.read(path.relative_to(ROOT).as_posix()) == path.read_bytes()
    zipped = {'archive': archive.name, 'members': len(files),
              'bytes': archive.stat().st_size, 'sha256': digest(archive),
              'crc_and_exact_byte_checks': 'PASS'}
    (OUT / 'zip_audit.json').write_text(json.dumps(zipped, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(zipped, indent=2))
