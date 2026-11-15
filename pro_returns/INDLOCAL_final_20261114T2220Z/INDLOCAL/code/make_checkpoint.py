#!/usr/bin/env python3
"""Create a new immutable checkpoint containing all authored work to date."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse, hashlib, json
from archive_policy import should_include
p=argparse.ArgumentParser();p.add_argument('number',type=int,nargs='?');p.add_argument('--final',action='store_true');a=p.parse_args()
if a.final == (a.number is not None):p.error('Use either a checkpoint number or --final')
r=Path(__file__).resolve().parents[1];out=r.parent/('INDLOCAL_final.zip' if a.final else f'INDLOCAL_checkpoint_{a.number:02d}.zip')
if out.exists():raise SystemExit(f'Refusing to overwrite {out}')
files=[]
qa_path=r/'logs/PDF_QA_PASSED.json'
if qa_path.exists():
 qa=json.loads(qa_path.read_text())
 pdf=r/'INDLOCAL_paper.pdf'
 if qa.get('status')!='PASSED' or not pdf.exists() or qa.get('pdf_sha256')!=hashlib.sha256(pdf.read_bytes()).hexdigest():
  raise SystemExit('Refusing to archive a PDF without a matching passed visual-review record')
for f in sorted(r.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(r)
 if not should_include(rel):continue
 if f.suffix=='.pdf' and not (r/'logs/PDF_QA_PASSED.json').exists():continue
 files.append((f,rel))
with ZipFile(out,'x',ZIP_DEFLATED) as z:
 for f,rel in files:z.write(f,Path('INDLOCAL')/rel)
print(json.dumps({'file':str(out),'members':len(files),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
