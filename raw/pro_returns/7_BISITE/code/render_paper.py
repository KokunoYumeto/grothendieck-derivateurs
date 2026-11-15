"""Render every PDF page and produce labelled contact sheets for visual QA."""
from pathlib import Path
import hashlib
import json
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parent/"research/BISITE_render"
DEST.mkdir(parents=True,exist_ok=True)
pdf=ROOT/"BISITE_paper.pdf"
subprocess.run(["pdftoppm","-scale-to","1400","-png",
                str(pdf),str(DEST/"page")],check=True,capture_output=True)
pages=sorted(DEST.glob("page-*.png"))
assert pages
try:font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",18)
except OSError:font=ImageFont.load_default()
sheets=[]
for offset in range(0,len(pages),9):
    group=pages[offset:offset+9]
    canvas=Image.new("RGB",(990,1510),"#d7dce2")
    draw=ImageDraw.Draw(canvas)
    for j,path in enumerate(group):
        im=Image.open(path).convert("RGB")
        im.thumbnail((310,450))
        x=10+(j%3)*330;y=30+(j//3)*500
        canvas.paste(im,(x+(310-im.width)//2,y))
        draw.text((x+8,y+455),f"Page {offset+j+1}",font=font,fill="#162335")
    target=DEST/f"contact-{offset//9+1:02d}.png"
    canvas.save(target)
    sheets.append(str(target))
result={"pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "pages_rendered":len(pages),"page_image_directory":str(DEST),
        "contact_sheets":sheets,
        "scope":"Rendering completed; the visual observations are recorded separately after inspection."}
Path(__file__).with_suffix(".out.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
