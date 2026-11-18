#!/usr/bin/env python3
"""Build the manuscript with LuaLaTeX, including a local format if needed."""
from pathlib import Path
import os,subprocess,json,re
p=Path(__file__).resolve().parents[1]
b=p/'build';b.mkdir(exist_ok=True)
env=os.environ.copy()
env.update(TEXMF='{.,/usr/share/texlive/texmf-dist,/usr/share/texmf}',TEXMFCACHE=str(b/'texcache'),TEXMFVAR=str(b/'texmf-var'),TEXMFCONFIG=str(b/'texmf-config'))
for key in ['TEXMFCACHE','TEXMFVAR','TEXMFCONFIG']:Path(env[key]).mkdir(exist_ok=True)
def run(cmd,log,cwd=p):
    q=subprocess.run(cmd,cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (b/log).write_text(q.stdout)
    if q.returncode:
        print(q.stdout[-4000:]);raise SystemExit(q.returncode)
if not (b/'lualatex.fmt').exists():run(['luahbtex','--ini','--jobname=lualatex','--progname=lualatex','lualatex.ini'],'format-build.log',b)
cmd=['lualatex','--fmt=build/lualatex.fmt','-interaction=nonstopmode','-halt-on-error','REVLOC_paper.tex']
run(cmd,'latex-pass1.log')
run(['bibtex','REVLOC_paper'],'bibtex.log')
run(cmd,'latex-pass2.log');run(cmd,'latex-pass3.log')
log=(p/'REVLOC_paper.log').read_text()
boxes=[float(n) for n in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)',log)]
result={'overfull_boxes':len(boxes),'overfull_over_2pt':sum(n>2 for n in boxes),'max_overfull_pt':max(boxes,default=0),'undefined_citations':bool(re.search('Citation .* undefined',log)),'missing_characters':len(re.findall('Missing character:',log))}
(b/'layout_check.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
