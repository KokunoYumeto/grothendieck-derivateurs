#!/usr/bin/env python3
"""Inspect the final PDF/log/ledger and render every page for visual review."""
from pathlib import Path
import collections
import csv
import importlib.metadata
import json
import re
import subprocess
import sys

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'build/qa'
PAGES = OUT/'pages'
PAGES.mkdir(parents=True, exist_ok=True)

pdf = fitz.open(ROOT/'TOTASPH_paper.pdf')
log = (ROOT/'build/TOTASPH_paper.log').read_text(errors='replace')
warnings = [line for line in log.splitlines()
            if re.search(r'Warning|Overfull|Underfull|^!|Missing character:', line)]
rows = list(csv.DictReader((ROOT/'TOTASPH_results.csv').open(newline='')))
index = json.loads((ROOT/'research/statement_index.json').read_text())
assert len(rows) == len(index)
assert len({r['id'] for r in rows}) == len(rows)
assert set(r['status'] for r in rows) <= {'Proved','Refuted','Known','Open'}

outside_page = []
outside_body_margin = []
replacement_glyphs = []
unresolved_markers = []
page_summary = []
for number, page in enumerate(pdf, 1):
    text = page.get_text()
    if '\ufffd' in text:
        replacement_glyphs.append(number)
    if '??' in text:
        unresolved_markers.append(number)
    words = page.get_text('words')
    for word in words:
        x0,y0,x1,y1,token,*_ = word
        if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width+0.5 or y1 > page.rect.height+0.5:
            outside_page.append({'page':number,'token':token,'bbox':[x0,y0,x1,y1]})
        if x0 < 57 or x1 > page.rect.width-57:
            outside_body_margin.append({'page':number,'token':token,'bbox':[x0,y0,x1,y1]})
    page_summary.append({'page':number,'width_pt':page.rect.width,
                         'height_pt':page.rect.height,'words':len(words)})

subprocess.run(['pdftoppm','-r','96','-png',str(ROOT/'TOTASPH_paper.pdf'),
                str(PAGES/'page')],check=True,stdout=subprocess.DEVNULL,
               stderr=subprocess.PIPE)
images = sorted(PAGES.glob('page-*.png'))
assert len(images) == len(pdf), (len(images),len(pdf))
contact_sheets=[]
cell_w,cell_h=350,520
for start in range(0,len(images),9):
    subset=images[start:start+9]
    sheet=Image.new('RGB',(cell_w*3,cell_h*3),(229,232,237))
    draw=ImageDraw.Draw(sheet)
    for k,path in enumerate(subset):
        img=Image.open(path).convert('RGB')
        img.thumbnail((cell_w-18,cell_h-36),Image.Resampling.LANCZOS)
        x=(k%3)*cell_w+(cell_w-img.width)//2
        y=(k//3)*cell_h+25
        sheet.paste(img,(x,y))
        draw.text(((k%3)*cell_w+12,(k//3)*cell_h+7),
                  f'Page {start+k+1}',fill=(20,30,50))
    target=OUT/f'contact-{start//9+1:02d}.png'
    sheet.save(target)
    contact_sheets.append(str(target.relative_to(ROOT)))

data={
    'pdf_pages':len(pdf),
    'numbered_statements':len(rows),
    'status_counts':dict(collections.Counter(r['status'] for r in rows)),
    'final_engine_warnings':warnings,
    'out_of_page_text':outside_page,
    'text_outside_57pt_horizontal_margin':outside_body_margin,
    'replacement_glyph_pages':replacement_glyphs,
    'unresolved_reference_marker_pages':unresolved_markers,
    'all_pages_rendered':True,
    'contact_sheets':contact_sheets,
    'page_summary':page_summary,
    'runtime':{'python':sys.version.split()[0],
               'sympy':importlib.metadata.version('sympy'),
               'pymupdf':importlib.metadata.version('PyMuPDF'),
               'pillow':importlib.metadata.version('Pillow')},
    'visual_review':'Contact sheets and selected full pages are reviewed after this run; see code/root_visual_review.json.'
}
(ROOT/'code/root_qa.out.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='page_summary'},indent=2))
assert not warnings, 'Final TeX engine has warnings to review.'
assert not outside_page, 'Text extends beyond PDF page.'
assert not replacement_glyphs, 'Missing/replacement glyphs in extracted text.'
assert not unresolved_markers, 'Unresolved reference marker in PDF.'
