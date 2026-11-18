#!/usr/bin/env python3
"""Render checkpoint 07's new proofs and retain final PDF/log verification.

Run with 'render' after a successful build, then inspect the emitted PNGs.
Run with 'verify' on the final build to check that the inspected pixels agree.
The script does not substitute an automatic assertion for visual inspection.
"""
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
pages = [1, *range(36, 42), *range(48, 53), 75, 104, 105, 106, len(doc)]
pages = list(dict.fromkeys(pages))
qa = root / 'qa' / 'checkpoint7'
qa.mkdir(parents=True, exist_ok=True)
hashes = {}
for number in pages:
    pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.25, 1.25))
    hashes[str(number)] = hashlib.sha256(pix.samples).hexdigest()
    if mode == 'render':
        pix.save(qa / f'page_{number:03}.png')

locators = {}
for number, page in enumerate(doc, 1):
    text = page.get_text()
    for key in ['A34.6. A single', 'A4.7. Finite', 'A4.8. Finite', 'C.27. A flat']:
        if key in text:
            locators[key] = number

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
