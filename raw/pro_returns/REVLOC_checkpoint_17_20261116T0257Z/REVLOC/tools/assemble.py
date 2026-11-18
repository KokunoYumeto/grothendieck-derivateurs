#!/usr/bin/env python3
"""Assemble the bibliography and numbered-statement register from owned sections."""
from pathlib import Path
import re,csv
p=Path(__file__).resolve().parents[1]
(p/'REVLOC_references.bib').write_text('% AI-produced bibliography; opening status is recorded in each entry.\n\n'+'\n'.join(x.read_text() for x in sorted((p/'references').glob('*.bib'))))
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
owned={}
for src in sorted((p/'records').glob('*.csv')):
    with src.open(newline='') as f:
        for row in csv.DictReader(f):
            if row.get('id'): owned[row['id']]=row
rows=[]
for src in sorted((p/'sections').glob('*.tex')):
    content=src.read_text()
    pat=re.compile(r'\\begin\{claim\}\{([^{}]*)\}\{([^{}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}')
    for m in pat.finditer(content):
        ident,status,title=m.groups()
        row=owned.pop(ident,{})
        rows.append({**dict.fromkeys(fields,''),**row,'id':ident,'statement':title,'status':status,'where_proved':str(src.relative_to(p))})
rows.extend(owned.values())
with (p/'REVLOC_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
print(f'Assembled {len(rows)} statement rows and {len(list((p/"references").glob("*.bib")))} bibliography fragments.')
