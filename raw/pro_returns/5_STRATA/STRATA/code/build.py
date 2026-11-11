"""Rebuild the LuaLaTeX paper, APA bibliography, and paginated result register.

Use an ordinary complete TeX installation by default. Pass --local-tex for
the workspace-only environment repaired by E_texenv.py in this session.
The final compilation log is checked for errors, unresolved references,
missing characters, and overfull boxes. No substitute PDF engine is used.
"""
from pathlib import Path
import argparse
import os
import subprocess
import sys
import json
import re

ROOT = Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--local-tex',action='store_true')
args=p.parse_args()
env=os.environ.copy()
if args.local_tex:
    from E_texenv import environment
    env=environment()

def command(argv,logname):
    print('Running: '+' '.join(argv),flush=True)
    proc=subprocess.run(argv,cwd=ROOT,env=env,stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,text=True)
    (ROOT/'code'/logname).write_text(proc.stdout)
    if proc.returncode:
        print(proc.stdout[-7000:],flush=True)
        raise SystemExit(proc.returncode)
    print('Completed: '+logname,flush=True)

command([sys.executable,'code/assemble.py'],'assemble_output.json')
command(['lualatex','-interaction=nonstopmode','-halt-on-error','STRATA_paper.tex'],
        'build_lualatex_1.txt')
command(['bibtex','STRATA_paper'],'build_bibtex.txt')
command(['lualatex','-interaction=nonstopmode','-halt-on-error','STRATA_paper.tex'],
        'build_lualatex_2.txt')
command(['lualatex','-interaction=nonstopmode','-halt-on-error','STRATA_paper.tex'],
        'build_lualatex_final.txt')
command([sys.executable,'code/assemble.py'],'assemble_output.json')
log=(ROOT/'STRATA_paper.log').read_text()
checks={
    'engine':'LuaLaTeX (LuaHBTeX)',
    'errors':re.findall(r'^!.*$',log,re.M),
    'undefined_citations_or_references':re.findall(r'^.*(?:undefined|multiply defined).*$' ,log,re.M),
    'missing_characters':re.findall(r'^Missing character:.*$',log,re.M),
    'overfull_boxes':re.findall(r'^Overfull .*$',log,re.M),
    'underfull_boxes':re.findall(r'^Underfull .*$',log,re.M),
    'output':re.findall(r'Output written on .*',log),
}
(ROOT/'code'/'build_quality.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2),flush=True)
if checks['errors'] or checks['undefined_citations_or_references'] or checks['missing_characters']:
    raise SystemExit('The final log contains an unresolved error.')
