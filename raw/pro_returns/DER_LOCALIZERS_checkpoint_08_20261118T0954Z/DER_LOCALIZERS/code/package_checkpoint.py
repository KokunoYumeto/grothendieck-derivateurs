#!/usr/bin/env python3
"""Create a unique hourly archive of original current deliverables."""
from pathlib import Path
import argparse,hashlib,json,zipfile,datetime
ap=argparse.ArgumentParser();ap.add_argument('number',type=int);args=ap.parse_args()
root=Path(__file__).resolve().parents[1]
out=root.parent/f'DER_LOCALIZERS_checkpoint_{args.number:02}.zip'
if out.exists():raise SystemExit('Refusing to overwrite existing checkpoint')
files=[]
for p in sorted(root.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(root)
 if rel.parts[0] in {'sources','build','qa','__pycache__'}:continue
 if p.suffix in {'.zip','.png','.pyc'}:continue
 files.append(p)
# Keep the original build record, not runtime caches or third-party inputs.
for name in ['DER_LOCALIZERS_paper.log','checkpoint_pass4.stdout','checkpoint_bibtex.stdout','DER_LOCALIZERS_paper.bbl']:
 p=root/'build'/name
 if p.exists():files.append(p)
payloads={p.relative_to(root).as_posix():p.read_bytes() for p in files}
manifest={'archive':out.name,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'policy':'All current original deliverables and own programs/outputs; supplied and downloaded third-party inputs, runtime dependencies and inspection images excluded.','files':[{'path':k,'bytes':len(v),'sha256':hashlib.sha256(v).hexdigest(),'status':'current; included'} for k,v in payloads.items()],'unchanged_files_in_prior_checkpoints':[]}
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for k,v in payloads.items():z.writestr('DER_LOCALIZERS/'+k,v)
 z.writestr('DER_LOCALIZERS/FILE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
if out.stat().st_size>=500_000_000:raise SystemExit('Archive exceeds 500 MB bound')
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
print(json.dumps({'archive':str(out),'bytes':out.stat().st_size,'files':len(payloads)+1,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
