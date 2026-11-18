#!/usr/bin/env python3
"""Create one new full hourly checkpoint; never alter an earlier archive."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import argparse,json,zipfile,hashlib
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--number',required=True,type=int);args=p.parse_args()
assert 1<=args.number<=99
now=datetime.now(timezone.utc)
started=datetime(2026,11,17,1,14,17,tzinfo=timezone.utc)
due=started+timedelta(hours=args.number)
if now<due:raise SystemExit(f'Hourly checkpoint {args.number:02d} is not due until {due.isoformat()}.')
dest=R.parent/f'DER_FOLLOWUP_checkpoint_{args.number:02d}.zip'
if dest.exists():raise SystemExit(f'Refusing to overwrite existing checkpoint: {dest}')
record=R/'notes'/f'checkpoint_{args.number:02d}.md'
record.write_text(f'# Hourly checkpoint {args.number:02d}\n\nCreated {now.isoformat()}.\n\n'
 'This archive contains the full current work directory, including mathematical source, '
 'master PDF, report, register, annotated bibliography, proof/source/attempt notes, '
 'verification programs and outputs, build records, visual-review evidence and all '
 'preserved earlier versions. Attached input files are excluded.\n\n'
 'The current report records every item and Lead. The explicitly requested C_delta '
 'free-monoid comparison remains under investigation; its pending state is not '
 'overridden by the refutation of the principal filteredness assertion.\n')
files=sorted(p for p in R.rglob('*') if p.is_file())
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for path in files:z.write(path,Path('DER_FOLLOWUP')/path.relative_to(R))
summary={'archive':dest.name,'created_utc':now.isoformat(),'files':len(files),
         'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
         'attached_inputs_included':False}
# This newly written packing receipt is included in the next checkpoint and final
# package; the archive itself contains the prewritten full checkpoint record.
(R/'code/outputs'/f'checkpoint_{args.number:02d}_pack.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
