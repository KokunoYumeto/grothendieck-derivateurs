#!/usr/bin/env python3
"""Necessary primary-module test for A -> W=Omega(Y<5>) through degree 11.

This is NOT a realization test. The target is the suspended Pontryagin
indecomposable quotient of H(F), F=Omega W. The low bar calculation
identifies its primitive-cohomology dual; degree-eleven product terms
have zero Sq1/2/4 and are omitted. No arbitrary map is assumed to
preserve products or Dyer--Lashof operations.
"""
from pathlib import Path
import json
import sys

root=Path(__file__).parent
sys.path.insert(0,str(root))
s={}
exec(compile((root/'D2_Qsource_primary.py').read_text().split('rows=[]')[0],
             'D2_Qsource_primary_helpers','exec'),s)
basis,sq=s['basis'],s['sq']

# Degrees in F; all are shifted upward by one for W.
F={4:['A'],5:['z','u'],6:['d','e','f'],7:['V','R','P','Q'],
   8:['C','L','M','J1','J2','J3'],
   9:['N','K1','K2','K3','K4','K5','Pm','Pn','Po'],
   10:['D2','Q10','Pp','Pr','B1','B2','B3','B4','B5','B6','B7','B8']}
ops={}
def row(x,b='',s2='',s4=''):
    for k,v in zip((1,2,4),(b,s2,s4)):ops[(k,x)]=set(v.split())
row('A');row('z','A');row('u')
for x in ('d','e','f'):row(x,'','A')
row('V','e','u');row('R');row('P','f','z');row('Q','','z')
row('C','','','A');row('L','Q','d');row('M','Q','f')
row('J1','','d e');row('J2');row('J3','R','d e')
row('N','','R','u');row('K1');row('K2','J1 J2','R')
row('K3','J1');row('K4','J2');row('K5');row('Pm')
row('Pn','','P Q','z');row('Po','L M','P Q','z')
row('D2','','','d');row('Q10','Pm Pn','M C','f')
row('Pp','','','f');row('Pr')
row('B1','K1','J2');row('B2','','J2');row('B3','K1')
row('B4','K2 K3 K4','J1 J2 J3','d e')
row('B5','','J1 J3','d e');row('B6','','J2')
row('B7','K5');row('B8')

T={d+1:xs for d,xs in F.items()}
variables=[]
for d in range(5,12):
    for m in basis(d):
        for x in T[d]:variables.append((d,m,x))
vid={v:i for i,v in enumerate(variables)}
equations=[]
equation_labels=[]
for d in range(5,12):
    for k in (1,2,4):
        if d-k<5:continue
        for m in basis(d):
            for y in T[d-k]:
                v=0
                for n in sq(k,m):v^=1<<vid[(d-k,n,y)]
                for x in T[d]:
                    if y in ops[k,x]:v^=1<<vid[(d,m,x)]
                if v:
                    equations.append(v)
                    equation_labels.append({'degree':d,'square':k,'source':list(m),'target':y})

def reduce_rows(rows):
    piv={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:piv[p]=v;break
    return piv
piv=reduce_rows(equations)
traced={}
for j,v in enumerate(equations):
    trace=1<<j
    while v:
        p=v.bit_length()-1
        if p in traced:
            v^=traced[p][0];trace^=traced[p][1]
        else:
            traced[p]=(v,trace);break
def remainder(v):
    for p in sorted(piv,reverse=True):
        if (v>>p)&1:v^=piv[p]
    return v

# Homology images paired with theta7=e7*.
tests=[]
certificates=[]
for m in basis(7):
    v=1<<vid[(7,m,'e')]
    tests.append({'source':list(m),'forced_zero_by_primary_module':remainder(v)==0})
    trace=0
    for p in sorted(traced,reverse=True):
        if (v>>p)&1:v^=traced[p][0];trace^=traced[p][1]
    if v==0:
        used=[]
        for j,label in enumerate(equation_labels):
            if (trace>>j)&1:
                terms=[{'degree':d,'source':list(n),'target':x}
                       for i,(d,n,x) in enumerate(variables) if (equations[j]>>i)&1]
                used.append({**label,'terms':terms})
        certificates.append({'source':list(m),'equations':used})

# Relations in the quotient target remain genuine Steenrod relations.
def op(k,p):
    out=set()
    for x in p:out.symmetric_difference_update(ops.get((k,x),set()))
    return out
for d,xs in F.items():
    for x in xs:
        assert not op(1,op(1,{x})),('beta2',x)
        assert op(2,op(2,{x}))==op(1,op(2,op(1,{x}))),('Adem',x)

out={'status':'PASS','scope':__doc__.strip(),'variables':len(variables),
     'equations':len(equations),'rank':len(piv),'theta_degree7_tests':tests,
     'certificates':certificates,
     'conclusion':'Only a necessary primary-module test; surviving coefficients are not realized maps.'}
dest=root/'outputs'/'FGH_k1_primary_module.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
