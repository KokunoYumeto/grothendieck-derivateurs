#!/usr/bin/env python3
"""Render every PDF page and prepare contact sheets for visual inspection."""
from pathlib import Path
import argparse
import json
import subprocess
from PIL import Image, ImageOps, ImageDraw

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--output',default=str(root/'.build'/'rendered'))
args=parser.parse_args()
dest=Path(args.output).resolve()
dest.mkdir(parents=True,exist_ok=True)
for pattern in ['page-*.png','contact-*.png']:
    for prior in dest.glob(pattern):
        prior.unlink()
pdf=root/'PATHS_paper.pdf'
subprocess.run(['pdftoppm','-r','90','-png',str(pdf),str(dest/'page')],check=True)
pages=sorted(dest.glob('page-*.png'))
assert pages
for first in range(0,len(pages),8):
    group=pages[first:first+8]
    sheet=Image.new('RGB',(800,4*585),'#e5e7eb')
    draw=ImageDraw.Draw(sheet)
    for n,p in enumerate(group):
        im=Image.open(p).convert('RGB')
        thumb=ImageOps.contain(im,(380,548))
        x=(n%2)*400+10+(380-thumb.width)//2
        y=(n//2)*585+25
        sheet.paste(thumb,(x,y))
        draw.text(((n%2)*400+14,(n//2)*585+7),p.stem,fill='black')
    sheet.save(dest/f'contact-{first//8+1:02d}.png')
out={'pdf':pdf.name,'rendered_pages':len(pages),'dpi':90,
     'contact_sheets':len(list(dest.glob('contact-*.png'))),
     'page_pixel_sizes':sorted({Image.open(p).size for p in pages})}
(root/'audit/render_qa.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
