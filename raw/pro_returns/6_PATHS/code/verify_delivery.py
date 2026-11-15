#!/usr/bin/env python3
"""Check the final paper, result register, bibliography, and recorded outputs.

This is a delivery audit, not an independent proof checker.  It does not rerun
the expensive bounded path search or infer an infinite theorem from that search.
"""
from pathlib import Path
from collections import Counter
import ast
import csv
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout


def main():
    required = [
        'PATHS_paper.tex', 'PATHS_paper.pdf', 'PATHS_results.csv',
        'PATHS_references.bib', 'PATHS_report.md',
        'audit/assembly_check.json', 'audit/render_qa.json',
        'audit/visual_review.md', 'audit/bibtex.txt',
        'audit/lualatex_pass3.txt',
        'code/a_finite_checks_output.json', 'code/b_path_search_L3.jsonl',
        'code/b_path_search_L4.jsonl', 'code/b_crown_checks.txt',
        'code/d_finite_checks.txt', 'code/e_finite_checks.out',
        'code/e_category_tables.json', 'code/source_integrity_output.json',
        'code/b_reference_audit.txt', 'code/README.md',
    ]
    for name in required:
        assert (ROOT / name).is_file(), ('missing file', name)
        assert (ROOT / name).stat().st_size, ('empty file', name)

    with (ROOT / 'PATHS_results.csv').open(newline='') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == [
            'id', 'statement', 'status', 'where_proved', 'depends_on',
            'manuscript_rows_or_pages_settled', 'notes',
        ]
        rows = list(reader)
    source_results = []
    for path in (ROOT / 'sections').glob('*.tex'):
        source_results += re.findall(
            r'\\begin\{result\}\{([^}]+)\}\{([^}]+)\}', path.read_text())
    assert len(source_results) == len(rows)
    assert len({key for key, _ in source_results}) == len(rows)
    assert dict(source_results) == {row['id']: row['status'] for row in rows}
    counts = dict(Counter(row['status'] for row in rows))
    assert set(counts) <= {'Proved', 'Refuted', 'Known', 'Open'}
    assembly = json.loads((ROOT / 'audit/assembly_check.json').read_text())
    assert assembly['numbered_statements'] == len(rows)
    assert assembly['status_counts'] == counts

    bib = (ROOT / 'PATHS_references.bib').read_text()
    entries = re.split(r'(?m)(?=^@\w+\{)', bib)[1:]
    bib_statuses = []
    for entry in entries:
        actual = re.sub(r'(?m)^%.*$', '', entry)
        assert re.search(r'\b(?:verified|unverified)\b', actual, re.I)
        bib_statuses.append('unverified' if re.search(
            r'\bunverified\b', actual, re.I) else 'verified')
    assert len(entries) == assembly['bibliography_entries']

    log = (ROOT / 'PATHS_paper.log').read_text(errors='replace')
    bad_patterns = [r'(?m)^!', r'Undefined control sequence',
                    r'There were undefined references',
                    r'(?:Reference|Citation).*undefined',
                    r'Overfull \\[hv]box', r'LaTeX Warning:',
                    r'Package \S+ Warning:']
    for pattern in bad_patterns:
        assert not re.search(pattern, log), ('TeX diagnostic', pattern)
    assert 'Output written on PATHS_paper.pdf' in log
    biblog = (ROOT / 'audit/bibtex.txt').read_text()
    assert not re.search(r'Warning--|error message|I couldn.t open', biblog)

    pdf = ROOT / 'PATHS_paper.pdf'
    pdfinfo = run('pdfinfo', str(pdf))
    pages = int(re.search(r'(?m)^Pages:\s+(\d+)', pdfinfo).group(1))
    assert re.search(r'(?m)^Encrypted:\s+no', pdfinfo)
    assert 'A4' in pdfinfo
    assert 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)' in pdfinfo
    fonts = run('pdffonts', str(pdf)).splitlines()[2:]
    assert fonts and all(line.split()[-5] == 'yes' for line in fonts)
    rendered = json.loads((ROOT / 'audit/render_qa.json').read_text())
    assert pages == rendered['rendered_pages']

    pdftext = run('pdftotext', str(pdf), '-')
    assert 'AI-produced by GPT-6 Astra' in pdftext
    assert pdftext.count('\f') == pages
    report = (ROOT / 'PATHS_report.md').read_text()
    assert f'{len(rows)} numbered statements' in report
    for status, count in counts.items():
        assert f'{count} {status}' in report
    assert 'not settled in full' in report

    python_files = sorted((ROOT / 'code').glob('*.py'))
    for path in python_files:
        ast.parse(path.read_text(), filename=str(path))
    for name in ['a_finite_checks_output.json', 'e_category_tables.json',
                 'source_integrity_output.json']:
        json.loads((ROOT / 'code' / name).read_text())
    searches = []
    for length in [3, 4]:
        records = [json.loads(line) for line in
                (ROOT / f'code/b_path_search_L{length}.jsonl').read_text().splitlines()
                if line.strip()]
        data, summary = records[:-1], records[-1]
        assert summary['cases'] == len(data)
        assert all(item['same_h0_h1'] for item in data)
        assert all(item['max_word_length'] == length for item in data)
        searches += data
    assert 'PASS:' in (ROOT / 'code/e_finite_checks.out').read_text()

    out = {
        'passed': True,
        'pdf_pages': pages,
        'pdf_bytes': pdf.stat().st_size,
        'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'numbered_statements': len(rows),
        'status_counts': counts,
        'bibliography_entries': len(entries),
        'bibliography_statuses': dict(Counter(bib_statuses)),
        'pdf_font_entries': len(fonts),
        'all_pdf_fonts_embedded': True,
        'tex_errors': 0,
        'undefined_references_or_citations': 0,
        'overfull_boxes': 0,
        'latex_or_package_warnings': 0,
        'minor_underfull_boxes': len(re.findall(r'Underfull \\[hv]box', log)),
        'rendered_pages': rendered['rendered_pages'],
        'python_programs_syntax_checked': len(python_files),
        'recorded_bounded_path_comparisons': len(searches),
        'scope': 'Delivery checks only; proofs and finite computational scope remain as stated in the paper.',
    }
    (ROOT / 'audit/final_verification.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
