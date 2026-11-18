#!/usr/bin/env python3
"""Exact primary-annihilator basis; no higher/integral lift is inferred."""
from pathlib import Path
import json
import I_E2_primary_15 as a

pivots={};kernel=[]
for j,v in enumerate(a.LBAS[13]):
    x=a.poly(v,13);out=0;offset=0
    for k in (1,2,4,8):
        sp,nk=a.LSPACE[13-k]
        value=sp.coords(a.vector(a.sq(k,x),13-k))>>nk
        out^=value<<offset
        offset+=len(a.LBAS[13-k])
    coefficient=1<<j
    while out:
        i=out.bit_length()-1
        if i not in pivots:break
        v0,c0=pivots[i];out^=v0;coefficient^=c0
    if out:pivots[out.bit_length()-1]=(out,coefficient)
    else:kernel.append(coefficient)

assert len(pivots)==26 and len(kernel)==7
rows=[]
for j,c in enumerate(kernel):
    value=a.EMPTY;names=[]
    for i,v in enumerate(a.LBAS[13]):
        if c>>i&1:
            value=a.xor(value,a.poly(v,13));names.append(a.LIDS[13][i])
    beta=a.sq(1,value)
    expected=[a.bracket(a.u,a.D),a.bracket(a.u,a.E6)]+[a.EMPTY]*5
    assert beta==expected[j]
    rows.append({'id':f'K{j+1}','coordinates':names,
                 'E_representative':a.show(value),
                 'beta_in_E':a.show(beta),'all_positive_Sq_in_L':[]})

report={'status':'PASS','scope':__doc__,'dimension_H15_L':33,
        'rank_positive_operations':26,'dimension_primary_annihilator':7,
        'cycles':rows,'integral_lifts':'unresolved; beta1 alone does not decide'}
dest=Path(__file__).parent/'outputs'/'I_L15_primary_cycles.json'
dest.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','cycles':7,'output':str(dest)}))
