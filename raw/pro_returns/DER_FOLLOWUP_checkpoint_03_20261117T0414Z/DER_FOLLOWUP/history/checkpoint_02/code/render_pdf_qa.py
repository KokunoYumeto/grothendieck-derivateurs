#!/usr/bin/env python3
"""Render a distributed paper sample and all formerly overflowing passages.

Poppler produces the page images. Contact sheets aid visual inspection; they
do not certify that inspection happened. The reviewed manifest is written only
after the pages have actually been viewed.
"""
from pathlib import Path
import subprocess,json,hashlib
from PIL import Image,ImageOps,ImageDraw
R=Path(__file__).resolve().parents[1]
OUT=R/'build'/'visual_qa';OUT.mkdir(parents=True,exist_ok=True)
docs=[('master','DER_FOLLOWUP_paper.pdf',[1,3,8,13,18,23,28,34,39,42,45,49,52,56,60,63,64,65,66]),
      ('G_check','build/G_check/G_check.pdf',[1,7,11,13,14]),
      ('paper_check','build/paper_check/paper_check.pdf',[1,30,55,59])]
rendered=[]
for tag,rel,pages in docs:
    paths=[]
    for p in pages:
        dest=OUT/f'{tag}_p{p:03d}'
        previous=dest.with_suffix('.png')
        old=hashlib.sha256(previous.read_bytes()).hexdigest() if previous.exists() else None
        cmd=['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-r','110','-png',str(R/rel),str(dest)]
        subprocess.run(cmd,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        paths.append(dest.with_suffix('.png'))
        new=hashlib.sha256(paths[-1].read_bytes()).hexdigest()
        rendered.append({'document':rel,'page':p,'image':str(paths[-1].relative_to(R)),
                         'image_sha256':new,'identical_to_previous_render':new==old if old else None})
    for batch in range(0,len(paths),6):
        subset=paths[batch:batch+6];thumbs=[]
        for path in subset:
            im=Image.open(path).convert('RGB');im.thumbnail((530,770))
            tile=Image.new('RGB',(550,800),'#dadada')
            tile.paste(im,((550-im.width)//2,25))
            ImageDraw.Draw(tile).text((10,6),path.stem,fill='black')
            thumbs.append(tile)
        sheet=Image.new('RGB',(1650,800*((len(thumbs)+2)//3)),'white')
        for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*550,(i//3)*800))
        sheet.save(OUT/f'{tag}_sheet_{batch//6+1}.png')
(R/'code/outputs/pdf_render_manifest.json').write_text(json.dumps(rendered,indent=2)+'\n')
print(json.dumps({'pages_rendered':len(rendered),'output_directory':str(OUT.relative_to(R))},indent=2))
