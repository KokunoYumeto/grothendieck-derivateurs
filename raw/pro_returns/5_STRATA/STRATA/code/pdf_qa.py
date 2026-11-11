"""Render every PDF page and create contact sheets for visual inspection.

Output images are temporary QA material outside the deliverable directory.
The report records the exact PDF hash and detects empty pages/font issues.
"""
from pathlib import Path
import hashlib
import json
import math
import re
import subprocess
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'STRATA_paper.pdf'
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
qa=ROOT.parent/'STRATA_build'/'pdf_qa'/digest[:12]
qa.mkdir(parents=True,exist_ok=True)
reader=PdfReader(pdf)
pages=len(reader.pages)
proc=subprocess.run(['pdftoppm','-r','100','-png',str(pdf),str(qa/'page')],
                    text=True,capture_output=True)
if proc.returncode:
    raise RuntimeError(proc.stderr)
images=sorted(qa.glob('page-*.png'),key=lambda f:int(f.stem.split('-')[-1]))
assert len(images)==pages,(len(images),pages)
page_records=[]
for index,file in enumerate(images,1):
    with Image.open(file) as im:
        gray=ImageOps.grayscale(im)
        ink=gray.point(lambda p:255 if p<240 else 0)
        bounds=ink.getbbox()
        assert bounds is not None,('empty page',index)
        page_records.append({'page':index,'size':im.size,'ink_bounds':bounds})
contacts=[]
for start in range(0,pages,4):
    sheet=Image.new('RGB',(1280,1850),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for offset,file in enumerate(images[start:start+4]):
        with Image.open(file) as im:
            im.thumbnail((615,870),Image.Resampling.LANCZOS)
            col,row=offset%2,offset//2
            x,y=15+col*640,34+row*925
            sheet.paste(im,(x,y))
            draw.text((x,y-22),f'Page {start+offset+1}',fill='black')
    path=qa/f'contact-{start+1:02d}-{min(start+4,pages):02d}.png'
    sheet.save(path)
    contacts.append(str(path))
fonts=subprocess.run(['pdffonts',str(pdf)],text=True,capture_output=True,check=True)
(ROOT/'code'/'pdf_fonts.txt').write_text(fonts.stdout)
font_rows=[s for s in fonts.stdout.splitlines()[2:] if s.strip()]
not_embedded=[]
for row in font_rows:
    # Name/type fields have variable widths; the final yes/no flags precede IDs.
    flags=re.findall(r'\b(?:yes|no)\b',row)
    if flags and flags[0]!='yes': not_embedded.append(row)
aux=(ROOT/'STRATA_paper.aux').read_text()
statement_pages=dict(re.findall(r'\\newlabel\{st:([^}]+)\}\{\{[^}]*\}\{([^}]+)\}',aux))
report={'sha256':digest,'pages':pages,'page_media_boxes':sorted(set(
    (float(p.mediabox.width),float(p.mediabox.height)) for p in reader.pages)),
    'font_rows':len(font_rows),'fonts_not_embedded':not_embedded,
    'page_records':page_records,'contact_sheets':contacts,'statement_pages':statement_pages}
(ROOT/'code'/'pdf_qa_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'sha256':digest,'pages':pages,'font_rows':len(font_rows),
                  'fonts_not_embedded':not_embedded,'contact_sheets':contacts},indent=2))
assert not not_embedded
