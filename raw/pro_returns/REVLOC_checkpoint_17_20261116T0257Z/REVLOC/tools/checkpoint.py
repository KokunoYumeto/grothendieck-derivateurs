#!/usr/bin/env python3
"""Write one immutable hourly ZIP of every authored deliverable and work record."""
from pathlib import Path
from datetime import datetime,timezone
import zipfile,sys,json
p=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]);out=p.parent/f'REVLOC_checkpoint_{number:02d}.zip'
if out.exists():raise SystemExit('Refusing to replace an existing checkpoint.')
start=datetime(2026,11,15,9,57,tzinfo=timezone.utc)
if (datetime.now(timezone.utc)-start).total_seconds()<3600*number:raise SystemExit('Hourly checkpoint is not due yet.')
excluded={'notes/FGH_Mukai2001.pdf','notes/EH5_Cisinski.txt','notes/EH5_Rezk.txt','notes/FGH_GALOIS_paper.txt','notes/FGH_MayPonto.pdf','notes/FGH_Strom2003.pdf','notes/FGH_Strom2003_p7.png'}
files=[];omitted=[]
for x in sorted(p.rglob('*')):
    if not x.is_file():continue
    rel=x.relative_to(p).as_posix()
    if rel in excluded or rel.startswith('notes/I_sources/') or rel.startswith('notes/FGH_CLM_') or rel.startswith('notes/FGH_Mukai2001-'):
        omitted.append(rel);continue
    files.append(x)
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for x in files:z.write(x,Path('REVLOC')/x.relative_to(p))
with zipfile.ZipFile(out) as z:assert z.testzip() is None
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'files':len(files),'omitted_original_references':omitted}))
