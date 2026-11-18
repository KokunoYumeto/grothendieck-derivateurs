#!/usr/bin/env python3
"""Locate mathematical additions and formerly overflowing passages for visual QA."""
from pathlib import Path
import json,fitz
R=Path(__file__).resolve().parents[1]
doc=fitz.open(R/'DER_FOLLOWUP_paper.pdf')
needles=['D.8','D.9','Mathlib','github.com','DGCastiglione','Free hulls','A free filtered limit']
out={s:[] for s in needles}
for i,page in enumerate(doc,1):
    txt=page.get_text()
    for s in needles:
        if s in txt:out[s].append(i)
(R/'code/outputs/pdf_section_locations.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
