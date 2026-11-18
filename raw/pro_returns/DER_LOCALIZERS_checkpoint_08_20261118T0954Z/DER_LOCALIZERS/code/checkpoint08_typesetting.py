#!/usr/bin/env python3
"""Render the eighth checkpoint's added proofs and verify inspected pixels."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys
import fitz

root = Path(__file__).resolve().parents[1]
mode = sys.argv[1]
pdf = root / 'build' / 'DER_LOCALIZERS_paper.pdf'
doc = fitz.open(pdf)
locators = {}
bibliography_pages = []
for number, page in enumerate(doc, 1):
    text = ' '.join(page.get_text().split())
    if 'Abdulwahid' in text or 'Kihara' in text:
        bibliography_pages.append(number)
    for key in ['C.27. A flat', 'C.28. Neither', 'C.29. Finite',
                'Finite-dimensional local systems and schematization']:
        if key in text:
            locators[key] = number
assert {'C.27. A flat', 'C.28. Neither', 'C.29. Finite'} <= set(locators), locators
start = locators['C.27. A flat']
end = locators['C.29. Finite'] + 3
pages = list(dict.fromkeys([1, 31, 60, 90, *range(start, end + 1), *bibliography_pages, len(doc)]))
qa = root / 'qa' / 'checkpoint8'
qa.mkdir(parents=True, exist_ok=True)
hashes = {}
for number in pages:
    pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.25, 1.25))
    hashes[str(number)] = hashlib.sha256(pix.samples).hexdigest()
    if mode == 'render':
        pix.save(qa / f'page_{number:03}.png')
record = {
    'pages': len(doc),
    'bytes': pdf.stat().st_size,
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'claim_start_pages': locators,
    'rendered_pages': pages,
    'render_scale': 1.25,
    'render_pixel_sha256': hashes,
}
prior = qa / 'render_manifest.json'
if mode == 'render':
    if prior.exists():
        old = json.loads(prior.read_text())['render_pixel_sha256']
        record['changed_or_added_rendered_pages'] = [int(p) for p, value in hashes.items() if old.get(p) != value]
    prior.write_text(json.dumps(record, indent=2) + '\n')
elif mode == 'verify':
    original = json.loads(prior.read_text())
    assert original['render_pixel_sha256'] == hashes, 'Inspected page pixels changed'
    log = (root / 'build' / 'checkpoint_pass4.stdout').read_text()
    bib = (root / 'build' / 'checkpoint_bibtex.stdout').read_text()
    bad = re.findall(r'^.*(?:Overfull|Missing character|Warning|undefined).*$', log, re.M)
    assert not bad, bad
    assert 'Warning' not in bib
    record.update({
        'overfull_boxes': 0,
        'undefined_references_or_citations': 0,
        'missing_characters': 0,
        'latex_or_natbib_warnings': 0,
        'bibtex_warnings': 0,
        'underfull_boxes': len(re.findall(r'^Underfull', log, re.M)),
        'inspected_pixels_match_final': True,
    })
    with (root / 'DER_LOCALIZERS_results.csv').open(newline='') as f:
        results = list(csv.DictReader(f))
    with (root / 'CHECK_EVENTS.tsv').open(newline='') as f:
        checks = list(csv.DictReader(f, delimiter='\t'))
    record.update({
        'result_rows': len(results),
        'open_rows': [r['id'] for r in results if r['status'] == 'Open'],
        'check_events': len(checks),
        'bibliography_records': len(re.findall(r'@\w+\s*\{', (root / 'DER_LOCALIZERS_references.bib').read_text())),
    })
else:
    raise SystemExit('Expected render or verify')
print(json.dumps(record, indent=2))
