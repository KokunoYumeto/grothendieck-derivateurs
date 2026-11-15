#!/usr/bin/env python3
"""Check completed English mapping against every unchanged source unit and French variant."""
from pathlib import Path
import collections,hashlib,json,re
from transfer_english import editorial_spans,ANCHOR,blank_comments

OUT=Path('output/records');ROOT=Path('work/en/translation')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def lexical_balance(s):
    braces=dollars=0;i=0
    while i<len(s):
        c=s[i]
        if c=='%':
            k=s.find('\n',i);i=len(s) if k<0 else k+1;continue
        if c=='\\':
            m=re.match(r'\\(?:[A-Za-z@]+|.)',s[i:]);i+=len(m[0]) if m else 1;continue
        if c=='{':braces+=1
        elif c=='}':braces-=1
        elif c=='$':dollars+=1
        i+=1
    return [braces,dollars%2]
def notes(s):return [s[a:b] for a,b in editorial_spans(s)]
def anchors(s):return [(m[1],m[2]) for m in ANCHOR.finditer(blank_comments(s))]
def main():
    p=json.loads((OUT/'EN_CHANGE_PLAN.json').read_text());fr=json.loads((OUT/'FR_CORRECTION_PLAN.json').read_text());audit=json.loads((OUT/'EN_TRANSFER_AUDIT.json').read_text())
    assert p['input_sha256']['FR_CORRECTION_PLAN.json']==sha(OUT/'FR_CORRECTION_PLAN.json'),'French plan changed after English mapping'
    assert p['input_sha256']['EN_TRANSFER_DECISIONS.json']==sha(OUT/'EN_TRANSFER_DECISIONS.json'),'Manual decisions changed after English mapping'
    assert len(p['rows'])==1879 and len({r['id'] for r in p['rows']})==1879
    assert {r['status'] for r in p['rows']}<={'applied','no_english_effect'},'English source rows remain unfinished'
    assert {r['status'] for r in audit['rows']}<={'applied','already_incorporated','no_english_effect'},'French variant transfer remains unfinished'
    fids={e['id'] for e in fr['edits']};eids={e['id'] for e in p['edits']}
    assert len(eids)==len(p['edits'])
    assert collections.Counter(r['fr_edit_id'] for r in audit['rows'])==collections.Counter(fids)
    for r in audit['rows']:
        ids=set(filter(None,r['english_edit_ids'].split(';')))
        assert ids<=eids
        if r['status']=='applied':assert ids,('Applied French variant has no English counterpart',r['fr_edit_id'])
    by=collections.defaultdict(list)
    for e in p['edits']:
        assert set(e.get('fr_edit_ids',[]))<=fids
        assert e['sources'] and e['reason'] and e['before']!=e['after']
        assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',e['after'])
        by[e['unit']].append(e)
    records=[]
    for path in sorted(ROOT.rglob('*_p*.tex')):
        u=str(path.relative_to(ROOT));s=path.read_text();es=by[u];t=s
        for a,b in zip(es,es[1:]):assert a['end']<=b['start'],('Overlapping English intervals',u,a['id'],b['id'])
        for e in reversed(es):
            assert s[e['start']:e['end']]==e['before'],('Original interval mismatch',e['id'])
            t=t[:e['start']]+e['after']+t[e['end']:]
        assert notes(s)==notes(t),('Editorial note text changed',u)
        assert anchors(s)==anchors(t),('Page/manuscript anchor changed',u)
        assert lexical_balance(s)==lexical_balance(t),('Brace/dollar parity changed',u)
        records.append({'unit':u,'source_sha256':sha(path),'variants':len(es),'original_offsets_exact':True,'editors_notes_exact':True,'anchors_exact':True,'brace_balance_and_dollar_parity_preserved':True})
    assert len(records)==243
    result={'counts':p['counts'],'units_checked':len(records),'fr_plan_sha256':sha(OUT/'FR_CORRECTION_PLAN.json'),'en_plan_sha256':sha(OUT/'EN_CHANGE_PLAN.json'),'every_french_variant_accounted_for':True,'every_source_row_accounted_for':True,'all_original_offsets_and_protected_text_verified':True,'checks':records,'scope':'Textual and structural validation. Mathematical changes remain justified by the cited supplied correction records; book compilation is recorded separately.'}
    (OUT/'EN_PLAN_VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
