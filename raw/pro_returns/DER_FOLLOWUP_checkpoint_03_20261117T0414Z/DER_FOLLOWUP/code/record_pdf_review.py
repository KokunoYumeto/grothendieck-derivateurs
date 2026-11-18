#!/usr/bin/env python3
"""Record the completed visual review of the 2026-11-17 04:11 master build.

This is a record of actual inspection, not an automated visual-quality test.
If the PDFs change, rerender and reinspect before making a new review record.
"""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
docs={
 'DER_FOLLOWUP_paper.pdf':[1,3,8,13,18,23,28,34,39,42,43,44,45,46,47,48,49,50,51,52,56,60,64,68,71,72,73,74],
 'build/G_check/G_check.pdf':[1,7,11,13,14],
 'build/paper_check/paper_check.pdf':[1,30,55,59]}
review={'review_date_utc':'2026-11-17','reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
 'method':'Poppler page PNGs viewed as contact sheets for the 04:11 master, including all D.8–D.10 pages; new proof page49 additionally viewed at full rendered size. Byte-identical images retain their prior actual review, including master pages28,34,39,42–44 and the nine historical samples.',
 'documents':[{'file':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest(),'pages_viewed':pages} for p,pages in docs.items()],
 'findings':'Margins, mathematical displays, statement headings, manuscript table, references and URL/module breaks are legible and contained. No clipping, overlap or visual overflow was observed in the reviewed sample.',
 'previous_overflow_passages_reviewed':['G_check p11: module name','paper_check p59: bibliography URL','master p68: module name','master p73: bibliography URL'],
 'report_text':'The visual review covers 37 pages: current master pages 1, 3, 8, 13, 18, 23, 28, 34, 39, 42–52, 56, 60, 64, 68, and 71–74; G standalone pages 1, 7, 11, 13, 14; and the earlier combined check pages 1, 30, 55, 59. The current 28-page master sample includes every page of D.8–D.10. Changed pages were viewed after the 04:11 rebuild; unchanged page images retain the preceding actual review. New proof page49 was additionally viewed at full rendered size, as were D.8–D.9 pages45 and47 in their preceding identical renders. The formerly overflowing module-name and bibliography-URL passages are now on master pages68 and73 and were included. The nine historical sample images are byte-identical to their previously reviewed renders. No clipping, overlap or visual overflow was observed. Page images, contact sheets, exact PDF hashes and the review record are retained in `build/visual_qa/` and `code/outputs/pdf_visual_qa.json`. External primary-source PDFs and the bundled TeX manual are immutable source/runtime evidence, not newly typeset papers.'}
manifest=json.loads((R/'code/outputs/pdf_render_manifest.json').read_text())
assert all(x['identical_to_previous_render'] for x in manifest if x['document']!='DER_FOLLOWUP_paper.pdf')
assert all(x['identical_to_previous_render'] for x in manifest if x['document']=='DER_FOLLOWUP_paper.pdf' and x['page'] in [28,34,39,42,43,44])
(R/'code/outputs/pdf_visual_qa.json').write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'documents_reviewed':len(docs),'pages_viewed':sum(map(len,docs.values())),'visual_defects_observed':0},indent=2))
