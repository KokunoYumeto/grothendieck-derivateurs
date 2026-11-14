#!/usr/bin/env python3
"""Create a new immutable checkpoint containing all authored work to date."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse, hashlib, json
p=argparse.ArgumentParser();p.add_argument('number',type=int);a=p.parse_args()
r=Path(__file__).resolve().parents[1];out=r.parent/f'INDLOCAL_checkpoint_{a.number:02d}.zip'
if out.exists():raise SystemExit(f'Refusing to overwrite {out}')
source_reproductions={'A_BDH1980.pdf','A_PalmerWu.txt','A_HH1979.txt','A_BDH1980.txt','A_BDH_p38.png','D_Thomason.txt','D_MSZ.txt','D_Raptis.txt','D_Cisinski.txt','D_CATHOT.txt','Cpaths_DwyerKan1980Calculating.txt','Cpaths_DwyerKan1980Simplicial.txt','Cpaths_DwyerKan1980Function.txt'}
files=[]
for f in sorted(r.rglob('*')):
 if not f.is_file():continue
 rel=f.relative_to(r)
 if any(part in ('.build','__pycache__') for part in rel.parts):continue
 if f.name in source_reproductions:continue
 if f.suffix=='.pdf' and not (r/'logs/PDF_QA_PASSED.json').exists():continue
 files.append((f,rel))
with ZipFile(out,'x',ZIP_DEFLATED) as z:
 for f,rel in files:z.write(f,Path('INDLOCAL')/rel)
print(json.dumps({'file':str(out),'members':len(files),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
