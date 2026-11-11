"""Combine the authored audit records and append the final reproduction record.

Run after build.py, pdf_qa.py and the recorded visual inspection. This script
does not read the attached manuscripts or fetch any external source.
"""
from pathlib import Path
from collections import Counter
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / 'STRATA_results.csv').open(newline='') as stream:
    rows = list(csv.DictReader(stream))
counts = dict(Counter(row['status'] for row in rows))
quality = json.loads((ROOT / 'code' / 'build_quality.json').read_text())
qa = json.loads((ROOT / 'code' / 'pdf_qa_output.json').read_text())
visual = json.loads((ROOT / 'code' / 'visual_qa_output.json').read_text())
assert visual['pdf_sha256'] == qa['sha256']
assert sorted(visual['pages_reviewed']) == list(range(1, qa['pages'] + 1))
assert visual['unresolved_layout_issues'] == []
for key in ('errors', 'undefined_citations_or_references', 'missing_characters',
            'overfull_boxes', 'underfull_boxes'):
    assert not quality[key], (key, quality[key])

parts = [(ROOT / 'audit' / 'root_report.md').read_text().rstrip()]
for name, title in (('CD', 'Detailed record for gluing and base change'),
                    ('E', 'Detailed record for bifibrations'),
                    ('F', 'Detailed record for the moduli calculation')):
    fragment = (ROOT / 'audit' / f'{name}_report.md').read_text().strip()
    # Keep the original local headings under a single top-level report title.
    fragment = '\n'.join('#' + line if line.startswith('#') else line
                         for line in fragment.splitlines())
    parts.append(f'## {title}\n\n{fragment}')

parts.append(f'''## Reproduction and final artifact verification

The final paper has **{qa['pages']} pages**. Its SHA-256 is
`{qa['sha256']}`. The register contains **{len(rows)} statements**,
with the status counts `{json.dumps(counts, sort_keys=True)}`. Every numbered
statement has a location in the compiled PDF. All {qa['font_rows']} PDF font
records are embedded. The final LuaLaTeX log contains no compilation errors,
unresolved references or citations, missing characters, overfull boxes or
underfull boxes. Every page was rendered and visually inspected; the exact
hash, page coverage and observations are recorded in
`code/pdf_qa_output.json` and `code/visual_qa_output.json`.

From the extracted `STRATA` directory, the mathematical finite checks are:

```sh
python3 code/AB_checks.py
python3 code/CD_checks.py
python3 code/E_finite_checks.py
python3 code/F_checks.py
python3 code/G_checks.py
```

Python 3 and SymPy supply the exact finite-category, chain-complex and
integer-matrix calculations. The PDF inspection additionally uses Pillow,
pypdf, and the Poppler commands `pdftoppm` and `pdffonts`. All captured
outputs are included. `00_sources.py` and `F_source_audit.py` audit the
separately supplied background, so they require the original attachments;
the mathematical verification programs above do not. Their source paths
and assumptions are explicit in the scripts.

The paper uses standard LuaLaTeX packages, including `fontspec`, the Latin
Modern fonts, the AMS packages, `mathrsfs`, `microtype`, `needspace`,
`hyperref`, and `apacite`. On a complete TeX installation, rebuild the
paper, APA references and paginated CSV with:

```sh
python3 code/build.py
python3 code/pdf_qa.py
```

`build.py` runs the actual LuaLaTeX engine, BibTeX, and two further
LuaLaTeX passes. `code/E_texenv.py` records the workspace repair used
for the minimal environment of this audit; `--local-tex` is an optional
build mode for that repaired environment, not a requirement for a normal
TeX installation. It downloads TeX runtime support, not mathematical
proofs. The separate temporary runtime and rendered inspection images
are not part of the deliverable.

`code/assemble.py` regenerates the bibliography and result register from
the authored section and audit inputs. The scripts `CD_metadata.py`,
`E_make_register.py` and `F_build_catalog.py` retain the corresponding
section metadata sources. `finish_report.py` combines the authored audit
reports and verifies the final inspection record. `package.py` performs
the final consistency checks, writes a file-hash manifest and creates
the single deliverable ZIP. A newly rebuilt PDF should be rendered and
inspected again before regenerating a final visual-inspection record;
the recorded observations concern the exact hash above.
''')

target = ROOT / 'STRATA_report.md'
target.write_text('\n\n'.join(parts) + '\n')
print(json.dumps({'report': target.name, 'bytes': target.stat().st_size,
                  'statement_count': len(rows), 'status_counts': counts,
                  'pdf_pages': qa['pages'], 'pdf_sha256': qa['sha256'],
                  'visual_page_coverage_complete': True}, indent=2))
