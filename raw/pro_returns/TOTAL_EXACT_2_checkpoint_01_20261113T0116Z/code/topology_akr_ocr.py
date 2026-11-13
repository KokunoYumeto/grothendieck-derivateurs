"""OCR selected AKR1981 scan pages for source inspection. No mathematical claims are inferred from OCR alone."""
from pathlib import Path
import fitz,subprocess,json
root=Path(__file__).resolve().parents[1]
p=fitz.open(root.parent/'background/papers/AdamekKoubekReiterman1981.pdf')
out=root/'work/akr_ocr';out.mkdir(exist_ok=True)
records=[]
for i in list(range(5,15))+list(range(16,len(p))):
    im=out/f'page_{i+1}.png'
    p[i].get_pixmap(matrix=fitz.Matrix(2,2)).save(im)
    r=subprocess.run(['tesseract',str(im),'stdout'],text=True,capture_output=True,check=True)
    txt=out/f'page_{i+1}.txt';txt.write_text(r.stdout)
    records.append({'pdf_page':i+1,'printed_page':367+i,'characters':len(r.stdout),'text_file':str(txt.relative_to(root))})
print(json.dumps(records,indent=2))
