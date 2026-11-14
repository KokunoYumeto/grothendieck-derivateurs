#!/usr/bin/env python3
"""Aggregate stable statement IDs, metadata, and the verified bibliography."""
import csv,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
metadata={}
for path in sorted((ROOT/'research').glob('*_results.json')):
    raw=json.loads(path.read_text())
    rows=raw if isinstance(raw,list) else raw.get('results',[])
    for row in rows:
        if row.get('id') in metadata: raise ValueError('duplicate metadata '+row['id'])
        metadata[row['id']]=row
rows=[]
pattern=re.compile(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{')
for path in sorted((ROOT/'sections').glob('*.tex')):
    text=path.read_text()
    for m in pattern.finditer(text):
        pos=m.end(); depth=1; end=pos
        while depth:
            c=text[end]; end+=1
            if c=='{': depth+=1
            elif c=='}': depth-=1
        title=text[pos:end-1]
        finish=text.index('\\end{claim}',end)
        statement=text[end:finish].strip()
        row={k:'' for k in fields}
        row.update(id=m.group(1),statement=title+' — '+statement,status=m.group(2),
                   where_proved=str(path.relative_to(ROOT))+'; '+m.group(1))
        row.update({k:v for k,v in metadata.get(row['id'],{}).items() if k in fields})
        rows.append(row)
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids)), 'duplicate statement IDs'
def order(row):
    return tuple(int(x) if x.isdigit() else x for x in re.split(r'(\d+)',row['id']))
rows.sort(key=order)
with (ROOT/'INDLOCAL_results.csv').open('w',newline='') as out:
    writer=csv.DictWriter(out,fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)
bibs=sorted((ROOT/'research').glob('*_references.bib'))
entries='\n\n'.join(p.read_text() for p in bibs)
(ROOT/'INDLOCAL_references.bib').write_text(entries+'\n')
print(json.dumps({'statements':len(rows),'metadata_rows':len(metadata),'bibliography_parts':[p.name for p in bibs]},indent=2))
