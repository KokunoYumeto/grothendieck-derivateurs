#!/usr/bin/env python3
"""All quotients of the left regular act of the ten-element example.

The R1 vanishing is certified for ALL left modules by the saved right-
module splitting. Here every quotient-representable set action is also
enumerated, and its induced tensor splitting is checked independently.
This is not offered as a substitute for the universal proof.
"""
from pathlib import Path
from collections import defaultdict, Counter
import json
OUT=Path(__file__).resolve().parent/'outputs'
D=json.loads((OUT/'main_counterexample_data.json').read_text())
C=json.loads((OUT/'projectivity_certificate.json').read_text())
T=D['multiplication']; ACT=D['right_action']; ID=D['identity_index']
Scol=defaultdict(list); Runit=defaultdict(list)
for r,c,v in C['inclusion_S']['entries']:Scol[c].append((r//10,r%10,v))
for r,c,v in C['retraction_R']['entries']:
    if c%10==ID:Runit[c//10].append((r,v))

def partitions(n):
    def rec(a,m):
        if len(a)==n:yield tuple(a);return
        for x in range(m+2):yield from rec(a+[x],max(m,x))
    yield from rec([0],0)

rows=[]; examined=0
for p in partitions(10):
    examined+=1
    blocks=[[] for _ in range(max(p)+1)]
    for i,b in enumerate(p):blocks[b].append(i)
    if any(len({p[T[g][x]] for x in block})!=1 for g in range(10) for block in blocks):continue
    q=len(blocks);la=[[p[T[g][block[0]]] for block in blocks] for g in range(10)]
    parent=list(range(52*q))
    def root(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(a,b):
        a,b=root(a),root(b)
        if a!=b:parent[a]=b
    for h in range(52):
        for m in range(10):
            for l in range(q):union(ACT[h][m]*q+l,h*q+la[m][l])
    representatives={}
    for z in range(52*q):representatives.setdefault(root(z),z)
    keys=list(representatives);ci={x:i for i,x in enumerate(keys)}
    component=[ci[root(z)] for z in range(52*q)]
    ns=len(keys)
    sb=[]
    for key in keys:
        h,l=divmod(representatives[key],q);col=defaultdict(int)
        for c,m,v in Scol[h]:col[c*q+la[m][l]]+=v
        sb.append({r:v for r,v in col.items() if v})
    # Check well-definedness on every element of each tensor component.
    for h in range(52):
        for l in range(q):
            col=defaultdict(int)
            for c,m,v in Scol[h]:col[c*q+la[m][l]]+=v
            assert {r:v for r,v in col.items() if v}==sb[component[h*q+l]]
    rb=[]
    for c in range(18):
        for l in range(q):
            col=defaultdict(int)
            for h,v in Runit[c]:col[component[h*q+l]]+=v
            rb.append({r:v for r,v in col.items() if v})
    for j,col in enumerate(sb):
        result=defaultdict(int)
        for r,v in col.items():
            for k,w in rb[r].items():result[k]+=v*w
        assert {k:v for k,v in result.items() if v}=={j:1}
    rows.append({'partition':list(p),'quotient_size':q,'tensor_components':ns,'tensor_RS_identity':True,
                 'positive_bar_homology':'zero in every degree, by verified projectivity'})
result={'partitions_examined':examined,'left_regular_quotients':len(rows),'by_quotient_size':dict(sorted(Counter(x['quotient_size'] for x in rows).items())),
        'tests':rows}
(OUT/'quotient_action_tests.json').write_text(json.dumps(result,indent=2))
msg=f"All {examined} set partitions examined.\nLeft regular quotient actions: {len(rows)}.\nCounts by quotient size: {result['by_quotient_size']}.\nAll induced tensor splittings well-defined and RS=I: PASS.\nPositive homology of every tested restricted action is zero in every degree by the verified projective module certificate; the theorem proves this for arbitrary actions as well.\n"
print(msg,end='');(OUT/'quotient_action_tests.out').write_text(msg)
