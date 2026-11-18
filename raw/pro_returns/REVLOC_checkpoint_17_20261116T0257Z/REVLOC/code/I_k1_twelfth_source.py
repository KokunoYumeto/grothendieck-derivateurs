#!/usr/bin/env python3
"""Quadratic source data for the conditional k=1 twelve-cell test.

This checks primary operations in H_*(D2 Sigma K(F2,2);F2) through
13 and the integral H8--H12 groups from the signed arity-two chain
model. It does not compute unstable attachments, target homotopy,
or assert a mapping nonextension beyond D.2.33.
"""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
from math import gcd
import json
import sys

root=Path(__file__).parent
sys.path.insert(0,str(root))
s={}
helper=(root/'D2_Qsource_primary.py').read_text().split('rows=[]')[0]
helper=helper.replace('MAX = 12','MAX = 13')
exec(compile(helper,'quadratic_source_helpers','exec'),s)
gens,basis,sq=s['gens'],s['basis'],s['sq']

def weight(m):
    return sum(2 if 'q' in gens[x] else 1 for x in m)

def qb(n):
    return tuple(m for m in basis(n) if weight(m)==2)

aliases={
    (1,0,0,0):'A',(0,1,0,0):'B',(2,0,0,0):'C',
    (0,0,1,0):'D',(1,1,0,0):'E',(3,0,0,0):'F',
    (0,2,0,0):'X',(2,1,0,0):'G',(1,0,1,0):'H',
    (4,0,0,0):'I',(1,2,0,0):'J',(0,1,1,0):'L',
    (3,1,0,0):'m',(2,0,1,0):'n',(0,3,0,0):'o',(0,0,0,1):'t'
}

def label(g):
    d=gens[g]
    if 'ex' in d:return aliases.get(d['ex'],g)
    return f'Q{d["q"]}{label(d["unit"])}'

def show(m):
    return '*'.join(label(g) for g in m)

def poly(p):
    return ' + '.join(show(m) for m in sorted(p)) or '0'

def rank(columns, target):
    pos={m:i for i,m in enumerate(target)}
    piv={}
    for col in columns:
        v=sum(1<<pos[m] for m in col)
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return len(piv)

rows=[]
for n in range(9,14):
    current=[]
    for m in qb(n):
        current.append({'class':show(m), **{
            f'Sq{k}':poly(sq(k,m)) for k in (1,2,4,6)}})
    rows.append({'degree':n,'dimension':len(current),
                 'beta_rank':rank([sq(1,m) for m in qb(n)],qb(n-1)),
                 'classes':current})

# The ordinary integral homology of X=Sigma B through degree9.
# It is only used to compute D2X through degree12; higher summands
# first contribute in degree13. The two degree9 summands are distinct.
blocks=[(3,2,'a'),(5,4,'c'),(6,2,'e'),(7,2,'f'),
        (8,2,'h'),(9,8,'i'),(9,2,'j')]
from I_k1_extended_power import homology
integral=defaultdict(list)
contributions=[]
for d,m,name in blocks:
    if 2*d>12:continue
    result=homology(d,m,12)
    for entry in result:
        integral[entry['degree']].extend(entry['torsion'])
        assert entry['free_rank']==0
        contributions.append({'degree':entry['degree'],'summand':'D2 '+name,
                              'torsion':entry['torsion']})
for (d,m,name),(e,n,other) in combinations(blocks,2):
    for degree in (d+e,d+e+1):
        if degree>12:continue
        group=gcd(m,n)
        if group>1:
            integral[degree].append(group)
            contributions.append({'degree':degree,'summand':name+' tensor '+other,
                                  'torsion':[group]})
for degree in integral:integral[degree].sort()
for n in range(9,13):
    assert len(qb(n))==len(integral[n])+len(integral[n-1])
assert integral[11]==[2,2,2,2,8]
assert integral[12]==[2]*8
assert rows[-1]['beta_rank']==8
assert rows[-2]['beta_rank']==4
out={'status':'PASS','scope':__doc__.strip(),'primary_tables':rows,
     'integral_groups':{str(n):integral[n] for n in range(8,13)},
     'integral_summands':contributions,
     'chain_input':'X homology through9, split over Z; D2 of each Moore block plus ordinary pairwise derived tensors. No attaching-map conclusion.'}
p=root/'outputs'/'I_k1_twelfth_source.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','dimensions':{r['degree']:r['dimension'] for r in rows},
                  'beta_ranks':{r['degree']:r['beta_rank'] for r in rows},
                  'H11':integral[11],'H12':integral[12],'output':str(p)}))
