#!/usr/bin/env python3
"""Find and exactly certify a small positive-measure obstruction."""
from ordered_poset_signed import posets, extensions, restrict_rows
from scipy.sparse import load_npz
from scipy.optimize import linprog
from fractions import Fraction
from pathlib import Path
import json
a=load_npz('FREX/verification/ordered_poset_n4.npz')
keys=[('normalization',)];variables=[];groups={}
for n in range(5):
    for rows in posets(n):
        for perm in extensions(rows):variables.append((n,rows,perm))
        if not n:continue
        start=len(keys)
        for omit in range(n):
            keep=[i for i in range(n) if i!=omit]
            small=restrict_rows(rows,keep)
            for p in extensions(small):keys.append((n,rows,omit,p))
        groups[(n,rows)]=list(range(start,len(keys)))
base=[i for i,k in enumerate(keys) if i==0 or k[0]<=3]
good=[]
for key,indices in groups.items():
    if key[0]!=4:continue
    selected=base+indices
    sub=a[selected]
    result=linprog([0]*a.shape[1],A_eq=sub,b_eq=[1]+[0]*(len(selected)-1),bounds=(0,None),method='highs')
    if result.status==2:
        good.append(key)
        print('single 4-point obstruction',key,flush=True)
        break
if not good:
    selected=list(range(a.shape[0]))
    for key,indices in groups.items():
        if key[0]!=4:continue
        remove=set(indices)
        trial=[i for i in selected if i not in remove]
        result=linprog([0]*a.shape[1],A_eq=a[trial],b_eq=[1]+[0]*(len(trial)-1),bounds=(0,None),method='highs')
        if result.status==2:selected=trial
else:selected=base+groups[good[0]]
sub=a[selected]
dual=linprog([0]*len(selected),A_ub=-sub.T,b_ub=[0]*a.shape[1],bounds=[(-1,-1)]+[(None,None)]*(len(selected)-1),method='highs')
v=[Fraction(float(x)).limit_denominator(1000000) for x in dual.x]
res=[Fraction(0)]*a.shape[1]
for i,c in enumerate(v):
    if not c:continue
    for j in range(sub.indptr[i],sub.indptr[i+1]):res[int(sub.indices[j])]+=c*int(sub.data[j])
assert v[0]==-1 and min(res)>=0
report={'equations':[{'key':keys[selected[i]],'coefficient':str(c)} for i,c in enumerate(v) if c],
        'positive_variables':[{'variable':variables[i],'coefficient':str(c)} for i,c in enumerate(res) if c],
        'exact_check':True}
Path('FREX/verification/ordered_poset_small_positive_certificate.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))

