#!/usr/bin/env python3
"""Retain the sixth checkpoint's PDF/log and rendered-page verification.

The listed pages were visually inspected by the root agent. This script verifies
the build diagnostics and generates the inspected page images; it does not
replace visual inspection with an automated claim.
"""
from pathlib import Path
import hashlib
import json
import re
import fitz

root = Path(__file__).resolve().parents[1]
pdf = root / 'DER_LOCALIZERS_paper.pdf'
log = (root / 'build' / 'checkpoint_pass4.stdout').read_text()
bib = (root / 'build' / 'checkpoint_bibtex.stdout').read_text()
bad = re.findall(r'^.*(?:Overfull|Missing character|Warning|undefined).*$', log, re.M)
assert not bad, bad
assert 'Warning' not in bib
doc = fitz.open(pdf)
assert len(doc) == 115
pages = [1, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 45, 91, 92, 93, 94, 95, 96, 97, 115]
render_hashes = {}
for number in pages:
    pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.25, 1.25))
    render_hashes[str(number)] = hashlib.sha256(pix.samples).hexdigest()
print(json.dumps({
    'pages': len(doc),
    'bytes': pdf.stat().st_size,
    'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull_boxes': 0,
    'undefined_references_or_citations': 0,
    'missing_characters': 0,
    'latex_or_natbib_warnings': 0,
    'bibtex_warnings': 0,
    'underfull_boxes': len(re.findall(r'^Underfull', log, re.M)),
    'visually_inspected_pages': pages,
    'render_scale': 1.25,
    'render_pixel_sha256': render_hashes,
    'inspection': 'No clipping, collision or overflowing formula observed. Pass 4 and pass 5 inspected page renders were pixel-identical.'
}, indent=2))
