#!/usr/bin/env python3
"""Compile the actual LuaLaTeX deliverable and retain diagnostics by run.

Use the workspace-local runtime restored by G_setup_tex.py. This script
does not change mathematical content or mask overfull/undefined warnings.
"""
from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,re,json,shutil
ROOT=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
DEST=ROOT/'build'/'master_runs'/stamp
DEST.mkdir(parents=True,exist_ok=True)
env=os.environ.copy()
env.update(json.loads((ROOT/'build'/'tex_runtime'/'environment.json').read_text()))
cmds=[['lualatex','-file-line-error','-interaction=nonstopmode','-halt-on-error','DER_FOLLOWUP_paper.tex'],
      ['bibtex','DER_FOLLOWUP_paper'],
      ['lualatex','-file-line-error','-interaction=nonstopmode','-halt-on-error','DER_FOLLOWUP_paper.tex'],
      ['lualatex','-file-line-error','-interaction=nonstopmode','-halt-on-error','DER_FOLLOWUP_paper.tex']]
runs=[]
for i,cmd in enumerate(cmds,1):
    r=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (DEST/f'run_{i}.txt').write_text(r.stdout)
    runs.append({'command':cmd,'exit_code':r.returncode})
    if r.returncode:
        print(r.stdout[-12000:])
        break
for suffix in ['log','blg','aux','bbl','toc','out']:
    f=ROOT/f'DER_FOLLOWUP_paper.{suffix}'
    if f.exists():shutil.copy2(f,DEST/f.name)
log=(ROOT/'DER_FOLLOWUP_paper.log').read_text(errors='replace')
over=[]
for m in re.finditer(r'Overfull \\[hv]box \((\d+(?:\.\d+)?)pt too (?:wide|high)\)',log):
    before=log[:m.start()]
    shipped=re.findall(r'\[(\d+)(?:\{|\])',before)
    after=re.search(r'\[(\d+)(?:\{|\])',log[m.end():])
    over.append({'points':float(m.group(1)),
                 'previous_shipped_page':int(shipped[-1]) if shipped else None,
                 'next_shipped_page':int(after.group(1)) if after else None,
                 'context':'\n'.join(log[m.start():].splitlines()[:10])})
warn=[line for line in log.splitlines() if 'Warning:' in line or 'undefined' in line]
pages=re.search(r'Output written on .*?\((\d+) pages, (\d+) bytes\)',log,re.S)
out={'timestamp_utc':stamp,'commands':runs,'overfull_boxes':over,
     'over_2pt':sum(x['points']>2 for x in over),'warnings':warn,
     'pages':int(pages.group(1)) if pages else None,'log_directory':str(DEST.relative_to(ROOT))}
(DEST/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'code'/'outputs'/'master_build.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
if any(x['exit_code'] for x in runs):raise SystemExit(1)
