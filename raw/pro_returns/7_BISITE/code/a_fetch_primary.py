"""Retrieve and OCR the two pages of Brown actually used in A.17.

The original PDF remains in research, not in the deliverable archive.
"""
from pathlib import Path
import hashlib
import subprocess
import urllib.request

root=Path(__file__).resolve().parents[2]
dest=root/'research'/'a_primary'
dest.mkdir(parents=True,exist_ok=True)
url='https://pi.math.cornell.edu/~kbrown/scan/1973.0186.pdf'
pdf=dest/'brown_1973.pdf'
log=[]
try:
    if not pdf.exists():
        with urllib.request.urlopen(url,timeout=25) as response:
            pdf.write_bytes(response.read())
    log.append('Retrieved '+url)
    log.append('SHA256 '+hashlib.sha256(pdf.read_bytes()).hexdigest())
    for page in (10,11):
        stem=dest/f'brown_pdfpage_{page}'
        subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','150','-png','-singlefile',str(pdf),str(stem)],check=True,capture_output=True)
        subprocess.run(['tesseract',str(stem)+'.png',str(stem)],check=True,capture_output=True)
        log.append('OCR PDF page '+str(page)+' to '+str(stem)+'.txt')
except Exception as exc:
    log.append(type(exc).__name__+': '+str(exc))
out=Path(__file__).with_suffix('.out.txt')
out.write_text('\n'.join(log)+'\n')
print('\n'.join(log))
