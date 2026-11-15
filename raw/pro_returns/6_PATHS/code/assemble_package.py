#!/usr/bin/env python3
"""Assemble and cross-check the result register and verified bibliography."""
from pathlib import Path
import csv
import json
import re
from collections import Counter

root=Path(__file__).resolve().parents[1]
aliases={
 'DwyerKanCalculatingPATHS':'DwyerKan1980Calculating',
 'DwyerKanFunctionPATHS':'DwyerKan1980Function',
 'KerodonPATHS':'ALurie2026',
 'DKerodon':'ALurie2026',
}
def normalize_citation(match):
    keys=[aliases.get(k.strip(),k.strip()) for k in match.group(2).split(',')]
    return match.group(1)+','.join(keys)+match.group(3)

citerx=re.compile(r'(\\(?:cite\w*|nocite)\*?(?:\[[^\]]*\])*\{)([^}]+)(\})')
for p in (root/'sections').glob('*.tex'):
    original=p.read_text()
    new=citerx.sub(normalize_citation,original)
    if new!=original:p.write_text(new)

entries={}
for name in ['A','B','CE','D']:
    text=(root/f'research/{name}_references.bib').read_text()
    chunks=re.split(r'(?m)(?=^@\w+\{)',text)
    for chunk in chunks:
        match=re.match(r'@\w+\{([^,]+),',chunk)
        if not match:continue
        key=match.group(1)
        assert key not in entries,key
        assert re.search(r'\b(?:unverified|verified)\b',chunk,re.I),key
        entries[key]=chunk.strip()
for old,new in aliases.items():
    assert old in entries and new in entries,(old,new)
    old_entry=entries.pop(old)
    # Keep the verification scope of aliases in machine-readable BibTeX
    # comments without printing duplicate bibliography entries.
    comment='\n'.join('% alias '+old+': '+line.replace('@','(at)') for line in old_entry.splitlines())
    entries[new]+='\n'+comment

bib='% Every entry is marked verified or unverified; alias notes retain provenance.\n\n'
bib+='\n\n'.join(entries[k] for k in sorted(entries))+'\n'
(root/'PATHS_references.bib').write_text(bib)

rows=[]
for name in ['A','B','CE','D']:
    rows+=json.loads((root/f'research/{name}_results.json').read_text())
by_id={r['id']:r for r in rows}
assert len(by_id)==len(rows),'duplicate result id'
stated=[]
sections=['A_definitions','A_colimits','B','C_paths','C','D','D_kt','E']
for name in sections:
    source=(root/f'sections/{name}.tex').read_text()
    for ident,status,title in re.findall(r'\\begin\{result\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)',source):
        assert ident in by_id,('missing metadata',ident)
        assert by_id[ident]['status']==status,(ident,status,by_id[ident]['status'])
        stated.append(ident)
assert set(stated)==set(by_id),('extra metadata',set(by_id)-set(stated))
assert len(stated)==len(set(stated)),'duplicate result environment'
fields=['id','statement','status','where_proved','depends_on','manuscript_rows_or_pages_settled','notes']
with (root/'PATHS_results.csv').open('w',newline='') as out:
    writer=csv.DictWriter(out,fieldnames=fields)
    writer.writeheader()
    for ident in stated:
        row=by_id[ident]
        writer.writerow({k:'; '.join(map(str,row[k])) if isinstance(row.get(k),list)
                          else row.get(k,'') for k in fields})

tex='\n'.join(p.read_text() for p in (root/'sections').glob('*.tex'))
cited={k.strip() for m in citerx.finditer(tex) for k in m.group(2).split(',')}
assert cited <= entries.keys(),('undefined bibliography keys',cited-entries.keys())
refs=set(re.findall(r'\\(?:ref|pageref|hyperref)\{res:([^}]+)\}',tex))
# Hyperref's bracket form is checked separately.
refs|=set(re.findall(r'\\hyperref\[res:([^\]]+)\]',tex))
refs={r for r in refs if '#' not in r}
refs|=set(re.findall(r'\\(?:pathres|auditref)\{([^}]+)\}',tex))
assert refs<=set(stated),('undefined statement labels',refs-set(stated))
summary={'numbered_statements':len(stated),'status_counts':dict(Counter(r['status'] for r in rows)),
         'bibliography_entries':len(entries),'cited_entries':len(cited),
         'statement_cross_references':len(refs),'all_statuses_match':True,
         'no_undefined_citations_or_statement_labels':True,
         'open_statements':[r['id'] for r in rows if r['status']=='Open']}
(root/'audit/assembly_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
