#!/usr/bin/env python3
"""Render explicitly selected physical PDF pages for visual review.

Example from the release extraction directory:
  python output/records/scripts/render_pdf_qa.py output/FR/DER_FR_corrige_apparat.pdf --pages 1 3 252 929 1083
The source PDF is opened read-only. PNGs are temporary review outputs, outside
the delivery whitelist. Requires PyMuPDF and Pillow for the contact sheet.
"""
import argparse, hashlib, json
from pathlib import Path
import fitz

ROOT=Path(__file__).resolve().parents[3]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('pdf',type=Path)
    ap.add_argument('--pages',nargs='+',required=True,type=int)
    ap.add_argument('--scale',type=float,default=1.5)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--contact-columns',type=int,default=2)
    args=ap.parse_args()
    out=args.output or ROOT/'work/pdf_visual_qa'/args.pdf.stem
    out.mkdir(parents=True,exist_ok=True)
    rendered=[]
    with fitz.open(args.pdf) as doc:
        for number in args.pages:
            if not 1<=number<=doc.page_count:raise ValueError('Physical page outside PDF: '+str(number))
            target=out/f'page_{number:04d}.png'
            doc[number-1].get_pixmap(matrix=fitz.Matrix(args.scale,args.scale),alpha=False).save(target)
            rendered.append({'physical_page':number,'png':target.name})
    if args.contact_columns:
        from PIL import Image, ImageDraw
        columns=args.contact_columns;cellw=800;cellh=1156
        sheet=Image.new('RGB',(columns*cellw,((len(rendered)+columns-1)//columns)*cellh),'#e7e7e7')
        draw=ImageDraw.Draw(sheet)
        for index,row in enumerate(rendered):
            img=Image.open(out/row['png']).convert('RGB');img.thumbnail((cellw-20,cellh-42))
            x=(index%columns)*cellw;y=(index//columns)*cellh
            draw.text((x+10,y+9),f"{args.pdf.stem} / physical page {row['physical_page']}",fill='black')
            sheet.paste(img,(x+(cellw-img.width)//2,y+32))
        sheet.save(out/'contact_sheet.png')
    result={'source_pdf':args.pdf.name,'pdf_sha256':hashlib.sha256(args.pdf.read_bytes()).hexdigest(),'scale':args.scale,'rendered':rendered}
    (out/'rendered_pages.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
