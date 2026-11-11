"""OCR the primary-source pages needed for the follow-up; cache excluded from deliverables."""
from pathlib import Path
import subprocess
root=Path(__file__).resolve().parents[2]
p=root/'source_followup'
subprocess.run(['pdftoppm','-f','2','-l','23','-r','160','-png',str(p/'AKR1981.pdf'),str(p/'AKR')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
files=sorted(p.glob('AKR-*.png'))
for f in files:
    if not f.with_suffix('.txt').exists():
        subprocess.run(['tesseract',str(f),str(f.with_suffix(''))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
print('OCR pages:',[f.name for f in files])
