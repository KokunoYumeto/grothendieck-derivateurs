#!/usr/bin/env python3
"""Locate TeX faults in independent chapter projections before final builds.

Temporary chapter PDFs are diagnostics only; the delivered readers are always
the complete projections emitted from their annotated master.
"""
import argparse, concurrent.futures, json, subprocess
from pathlib import Path
import build_readers as B
import compile_books as C

def run_one(p):
    dest=p.with_suffix('.stdout')
    with dest.open('w') as f:
        proc=subprocess.run(['lualatex','--no-shell-escape','-interaction=nonstopmode','-file-line-error','-halt-on-error',p.name],cwd=p.parent,env=C.environment(),stdout=f,stderr=subprocess.STDOUT)
    log=p.with_suffix('.log').read_text(errors='replace')
    d=C.diagnostics(C.sanitize(log));d['returncode']=proc.returncode;d['file']=p.name
    print(json.dumps({'file':p.name,'returncode':proc.returncode,'errors':d['errors'],'missing_glyphs':d['missing_glyphs']},ensure_ascii=False),flush=True)
    return d

def main():
    ap=argparse.ArgumentParser();ap.add_argument('language',choices=['FR','EN']);ap.add_argument('--workers',type=int,default=4);ap.add_argument('--only',nargs='*');a=ap.parse_args()
    data=B.read_master(B.OUT/a.language/f'DER_{a.language}_annotated_master.tex')
    dest=B.ROOT/'work/chapter_checks'/a.language;dest.mkdir(parents=True,exist_ok=True)
    chapters={}
    for u in data['units']:chapters.setdefault(Path(u['unit']).parts[0],[]).append(u)
    paths=[]
    for chapter,units in chapters.items():
        if a.only and chapter not in a.only:continue
        for form_i,form in [(1,'apparatus'),(2,'reading')]:
            p=dest/f'{chapter}_{form}.tex'
            s=B.preamble(a.language)+'\n'+r'\tracinglostchars=3'+'\n'+r'\begin{document}'+'\n'+''.join(u['forms'][form_i] for u in units)+r'\end{document}'+'\n'
            p.write_text(s);paths.append(p)
    if not a.only or 'register' in a.only:
        p=dest/'register.tex';p.write_text(B.preamble(a.language)+'\n'+r'\tracinglostchars=3'+'\n'+r'\begin{document}'+'\n'+B.apparatus(a.language,data['units'])+r'\end{document}'+'\n');paths.append(p)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:results=list(pool.map(run_one,paths))
    (dest/'RESULTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'chapters_checked':len(paths),'failures':sum(r['returncode']!=0 for r in results),'language':a.language}),flush=True)

if __name__=='__main__':main()
