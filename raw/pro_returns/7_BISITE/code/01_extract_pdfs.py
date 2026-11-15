"""Create searchable text for the supplied primary PDF sources."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[2]
files=list((ROOT/'background/papers').glob('*/*.pdf'))
files += list((ROOT/'background/grothendieck').glob('*/*_pages.pdf'))
cache=ROOT/'research/pdf_text'
cache.mkdir(parents=True,exist_ok=True)
lines=[]
for p in files:
    if p.stat().st_size < 150000:
        continue
    out=cache/(p.parent.name+'__'+p.stem+'.txt')
    result=subprocess.run(['pdftotext','-layout',str(p),str(out)],capture_output=True,text=True)
    lines.append(f'{p.relative_to(ROOT)} -> {out.relative_to(ROOT)}; exit={result.returncode}; {result.stderr.strip()}')
(ROOT/'BISITE/code/01_extract_pdfs.out.txt').write_text('\n'.join(lines)+'\n')
print(f'Converted {len(lines)} PDFs; see code/01_extract_pdfs.out.txt')
