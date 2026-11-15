#!/usr/bin/env python3
"""Preserve finished readers and every current source/record in a checkpoint."""
import argparse,json,re,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'output';DEST=ROOT/'deliverables'
TEXT={'.tex','.bib','.sty','.py','.tsv','.md','.json','.jsonl','.lua','.csv','.log','.txt'}
def sanitized(b):
 s=b.decode('utf-8',errors='replace')
 s=re.sub(r'(?:[A-Za-z]:[\\/](?:Users|home)[\\/][^\s\n"<>]+|/(?:Users|home|root|workspace|tmp)/[^\s\n"<>]+)','[local path removed]',s)
 s=re.sub(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}','[e-mail address removed]',s)
 return s.encode()
def checkpoint(n,complete):
 DEST.mkdir(exist_ok=True)
 target=DEST/f'DER_READERS_checkpoint_{n}.zip'
 states={}
 for name in complete:
  p=OUT/'records/build'/f'{name}.json';d=json.loads(p.read_text());assert d['compiled_without_errors'];states[name]={'pages':d['pages'],'errors':0,'missing_glyphs':len(d['passes'][-1]['missing_glyphs'])}
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(OUT.rglob('*')):
   if not p.is_file() or '__pycache__' in p.parts:continue
   rel=p.relative_to(OUT)
   if p.suffix=='.pdf':
    companion_ok=False
    if p.stem=='LesDerivateurs_companion':
     status=OUT/'records/APPENDIX_COMPILE_STATUS.json'
     companion_ok=status.exists() and json.loads(status.read_text()).get('latex_errors')==0
    if p.stem not in complete and not companion_ok:continue
   elif p.suffix not in TEXT:continue
   # Only explicitly sanitized build logs are deliverable records.
   if p.suffix=='.log' and 'records' not in rel.parts:continue
   b=p.read_bytes();z.writestr(rel.as_posix(),sanitized(b) if p.suffix in TEXT else b)
  for p in sorted((ROOT/'work/corrections_fr').glob('manual*.json')):
   z.writestr('records/decisions/'+p.name,sanitized(p.read_bytes()))
  status='# Checkpoint '+str(n)+'\n\nCompleted readers (LuaLaTeX, zero errors):\n\n'+''.join('- '+k+': '+str(v['pages'])+' pages; '+str(v['missing_glyphs'])+' missing glyphs.\n' for k,v in states.items())+'\nOther sources, decisions and plans in this checkpoint remain work in progress. Their presence does not certify completion. The final correction coverage, appendix validation, apparatus counts and final archives will supersede this checkpoint.\n'
  z.writestr('CHECKPOINT_STATUS.md',status)
 print(json.dumps({'checkpoint':target.name,'bytes':target.stat().st_size,'completed':states}))
 return target
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('number',type=int);ap.add_argument('complete',nargs='+');a=ap.parse_args();checkpoint(a.number,a.complete)
