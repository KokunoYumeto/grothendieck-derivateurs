#!/usr/bin/env python3
"""Preserve exact superseded bytes from every prior hourly checkpoint.

The original ZIPs are never modified. Unchanged bytes remain at their original
relative paths; changed/missing files are retained in history/checkpoint_NN/.
This script does not create checkpoints and must not be used to change cadence.
"""
from pathlib import Path
import csv,hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
PARENT=ROOT.parent
history=ROOT/'history'
history.mkdir(exist_ok=True)
rows=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
for archive in sorted(PARENT.glob('DER_FOLLOWUP_checkpoint_[0-9][0-9].zip')):
    tag=archive.stem.removeprefix('DER_FOLLOWUP_')
    with zipfile.ZipFile(archive) as z:
        for item in z.infolist():
            if item.is_dir():continue
            path=Path(item.filename)
            assert path.parts[0]=='DER_FOLLOWUP',item.filename
            rel=Path(*path.parts[1:])
            assert not rel.is_absolute() and '..' not in rel.parts
            data=z.read(item)
            live=ROOT/rel
            # These current records are rewritten during/after this audit.
            # Always retain their checkpoint bytes to avoid a self-reference
            # that would become false as soon as the new manifest is written.
            regenerated={'history/preservation_manifest.csv',
                         'code/outputs/checkpoint_preservation.json',
                         'DER_FOLLOWUP_report.md','code/outputs/assemble_report.json'}
            same=(rel.as_posix() not in regenerated and live.exists()
                  and live.is_file() and live.read_bytes()==data)
            if same:
                retained=rel;reason='Unchanged; exact original bytes retained at current path.'
            else:
                retained=Path('history')/tag/rel
                target=ROOT/retained
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(data)
                reason=('Superseded by current '+rel.as_posix()+'. Exact prior version retained here.'
                        if live.exists() else 'Removed from active layout; exact prior version retained here.')
                if rel.as_posix()=='sections/B.tex':
                    reason+=' Later B.10 clarifies VII ms.112 and the weaker parallel-map homotopy assumption.'
            rows.append({'checkpoint':archive.name,'original_file':rel.as_posix(),
                         'preserved_file':retained.as_posix(),'sha256':sha(data),'reason':reason})
out=history/'preservation_manifest.csv'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['checkpoint','original_file','preserved_file','sha256','reason'])
    w.writeheader();w.writerows(rows)
summary={'checkpoint_archives':len({r['checkpoint'] for r in rows}),
         'entries_checked':len(rows),
         'superseded_versions_preserved':sum(r['preserved_file'].startswith('history/') for r in rows),
         'intentionally_omitted_files':0,'manifest':'history/preservation_manifest.csv'}
(ROOT/'code'/'outputs'/'checkpoint_preservation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
