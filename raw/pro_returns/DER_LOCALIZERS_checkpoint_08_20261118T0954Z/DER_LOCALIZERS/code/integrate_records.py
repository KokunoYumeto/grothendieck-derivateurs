#!/usr/bin/env python3
"""Merge independently maintained claim, check-event and citation records."""
from pathlib import Path
import csv,re
root=Path(__file__).resolve().parents[1]
header=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
rows=[]
for p in sorted((root/'notes').glob('*_results.csv')):
 with p.open(newline='') as f:
  for r in csv.DictReader(f):
   if set(r)!=set(header): raise ValueError((p,r))
   rows.append(r)
ids=[r['id'] for r in rows]
if len(ids)!=len(set(ids)):raise ValueError('Duplicate claim identifier')
with (root/'DER_LOCALIZERS_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=header);w.writeheader();w.writerows(rows)
checks=[]
ch=['statement_id','date','who','type','outcome']
for p in sorted((root/'notes').glob('*_checks.tsv')):
 with p.open(newline='') as f:
  rd=csv.DictReader(f,delimiter='\t')
  if rd.fieldnames!=ch: raise ValueError((p,rd.fieldnames))
  checks.extend(rd)
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=ch,delimiter='\t');w.writeheader();w.writerows(checks)
texts=[];keys=[]
for p in sorted((root/'notes').glob('*_references.bib')):
 s=p.read_text();texts.append('% Source record: '+p.name+'\n'+s)
 keys+=re.findall(r'@\w+\s*\{\s*([^,]+),',s)
if len(keys)!=len(set(keys)):raise ValueError('Duplicate bibliography key')
(root/'DER_LOCALIZERS_references.bib').write_text('\n\n'.join(texts))
claims=[];cites=[]
for p in sorted((root/'sections').glob('*.tex')):
 s=p.read_text();claims+=re.findall(r'\\begin\{claim\}\{([^}]+)\}',s)
 for c in re.findall(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}',s):cites+=c.split(',')
missing=set(claims)-set(ids)
missing_cites=set(cites)-set(keys)
print(f'{len(rows)} results; {len(checks)} check events; {len(keys)} bibliography entries')
print('Claims missing metadata:',sorted(missing));print('Citations missing records:',sorted(missing_cites))
if missing or missing_cites:raise SystemExit(1)
