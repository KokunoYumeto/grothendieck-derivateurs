#!/usr/bin/env python3
"""Record the completed visual review of the 2026-11-17 03:09 master build.

This is a record of actual inspection, not an automated visual-quality test.
If the PDFs change, rerender and reinspect before making a new review record.
"""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
docs={
 'DER_FOLLOWUP_paper.pdf':[1,3,8,13,18,23,28,34,39,42,45,49,52,56,60,63,64,65,66],
 'build/G_check/G_check.pdf':[1,7,11,13,14],
 'build/paper_check/paper_check.pdf':[1,30,55,59]}
review={'review_date_utc':'2026-11-17','reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
 'method':'Poppler page PNGs viewed as contact sheets; master pages 60 and 65 also viewed at full rendered size. After the 03:09 rebuild, 26 sampled images were byte-identical; changed master p45 and newly sampled p42 were viewed at full rendered size.',
 'documents':[{'file':p,'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest(),'pages_viewed':pages} for p,pages in docs.items()],
 'findings':'Margins, mathematical displays, statement headings, manuscript table, references and URL/module breaks are legible and contained. No clipping, overlap or visual overflow was observed in the reviewed sample.',
 'previous_overflow_passages_reviewed':['G_check p11: module name','paper_check p59: bibliography URL','master p60: module name','master p65: bibliography URL'],
 'report_text':'We rendered and visually inspected 28 pages: master pages 1, 3, 8, 13, 18, 23, 28, 34, 39, 42, 45, 49, 52, 56, 60, 63–66; G standalone pages 1, 7, 11, 13, 14; and the earlier combined check pages 1, 30, 55, 59. The formerly overflowing module-name and bibliography-URL passages were included, with master pages 60 and 65 additionally viewed at full rendered size. After the 03:09 rebuild, 26 sampled images were byte-identical to the previously inspected render; changed page 45 and new sample page 42 were viewed at full rendered size. No clipping, overlap or visual overflow was observed. The page images, contact sheets, exact PDF hashes and review record are retained in `build/visual_qa/` and `code/outputs/pdf_visual_qa.json`. External primary-source PDFs and the bundled TeX manual are immutable source/runtime evidence, not newly typeset papers.'}
(R/'code/outputs/pdf_visual_qa.json').write_text(json.dumps(review,indent=2)+'\n')
print(json.dumps({'documents_reviewed':len(docs),'pages_viewed':sum(map(len,docs.values())),'visual_defects_observed':0},indent=2))
