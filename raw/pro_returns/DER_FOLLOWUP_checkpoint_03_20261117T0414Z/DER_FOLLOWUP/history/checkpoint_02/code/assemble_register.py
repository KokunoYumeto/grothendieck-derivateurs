#!/usr/bin/env python3
"""Merge the audited section registers and bibliography; preserve source notes."""
from pathlib import Path
import csv,re,json
root=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
rows={}
for name in ['A_results.csv','CD_results.csv','G_results.csv','BEF_results.csv']:
    for row in csv.DictReader((root/'notes'/name).open()):
        rows[row['id']]=row
locations={'B':'VII ms.99–115','E':'XII ms.93–97; PRETOT A.5',
           'F':'II ms.36ter; XII ms.93–114; VII ms.99–115; XV ms.128–137; XVI ms.7–16,99–113'}
deps={'B.1':'R12; INDLOCAL C.21,C.23; PATHS A.2 audited',
 'B.2':'Explicit moment-body and relative simplex-category proofs; Hirschhorn 15.10.4,19.9.1',
 'B.3':'B.2; PATHS C.P1–C.P2 audited; explicit strictification',
 'B.4':'B.1; finite presentability of finite signed orders; two explicit comma contractions',
 'B.5':'B.1; sequential homotopy-colimit comparison',
 'B.6':'B.3; B.5; explicit set diagram',
 'B.7':'Explicit finite presentation; two amalgam contractions',
 'B.8':'B.3–B.7', 'B.9':'B.1; B.3; Cegarra–Heredia Theorem5.1; 317 dimension-two convention audited',
 'B.10':'B.1–B.9', 'E.1':'Explicit idempotent completion and extension',
 'E.2':'E.1; simplex bar and cell attachment induction',
 'E.3':'Explicit Delta[2]/boundary counterexample; E.2',
 'E.4':'E.1–E.2; truncated Dold–Kan; two-sided Tor bar; final comparison',
 'E.5':'E.1–E.4; Hopf sequence; dimension-preserving mapping cylinder',
 'F.1':'A.8–A.9; A.15; D.2,D.4,D.7; R1,R6,R17 audited',
 'F.2':'E.2; E.4; explicit five-element act and double-cosieve action',
 'F.3':'A–G and audited PRETOT B.4/TOTASPH F.9'}
for path in sorted((root/'sections').glob('*.tex')):
    txt=path.read_text()
    for m in re.finditer(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+?)\}\s*(?:\\label\{([^}]+)\})?',txt):
        ident,status,title,label=m.groups()
        if ident not in rows:
            rows[ident]={'id':ident,'statement':title,'status':status,
             'where_proved':f'sections/{path.name}'+(f' label {label}' if label else ''),
             'depends_on':deps.get(ident,''),
             'manuscript_pages_settled':locations.get(ident[0],''),
             'notes':'Complete quantified statement and proof in the named section; independent verification recorded in code/outputs and notes.'}
        assert rows[ident]['status']==status,(ident,status,rows[ident]['status'])
        rows[ident]['where_proved']=f'sections/{path.name}'+(f' label {label}' if label else '')
order=lambda k:(k.split('.')[0],int(k.split('.')[1]))
with (root/'DER_FOLLOWUP_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for k in sorted(rows,key=order):w.writerow(rows[k])
bibs=['A_refs.bib','CD_references.bib','G_references.bib','BE_references.bib','B_interval_references.bib','F_A_refs.bib','F_references.bib','F_R19_refs.bib','D_attempt_refs.bib','D_root_attempt_refs.bib']
parts=[];keys=set()
for name in bibs:
    p=root/'notes'/name
    if not p.exists():continue
    txt=p.read_text()
    if name=='G_references.bib':
        # Same book as Cisinski2006; both sets of inspected passages are in
        # A_refs.bib. Preserve the old fragment for the standalone audit.
        txt=re.sub(r'(?ms)^@book\{GCisinski2006,.*?^\}\s*','',txt)
    for k in re.findall(r'@\w+\{\s*([^,]+),',txt):
        assert k not in keys,('duplicate bibliography key',k)
        keys.add(k)
    parts.append('% Source: notes/'+name+'\n'+txt)
(root/'DER_FOLLOWUP_references.bib').write_text('\n\n'.join(parts))
summary={'claims':len(rows),'bibliography_entries':len(keys),
 'status_counts':{s:sum(r['status']==s for r in rows.values()) for s in sorted({r['status'] for r in rows.values()})}}
(root/'code'/'outputs'/'assemble_register.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
