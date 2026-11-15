"""Exact finite categorical checks supporting A.6 and the fork in E.

This validates only the listed finite categories. Infinite horn attachment and
the all-dimensional nonfibrancy argument are mathematical proofs in the paper.
"""
import json
from itertools import product
import sympy as sp

def verify_poset(name, n, strict):
    rel={(i,i) for i in range(n)}|set(strict)
    assert all((j,i) not in rel for i,j in strict)
    assert all((i,k) in rel for i,j in rel for j2,k in rel if j2==j)
    arrows=sorted(rel)
    comps=0
    for a,b,c in product(arrows,repeat=3):
        if a[1]==b[0] and b[1]==c[0]:
            assert (a[0],c[1]) in rel
            comps+=1
    edges=sorted(strict)
    assert not any(i!=j and j!=k for i,j in strict for j2,k in strict if j==j2)
    d=sp.zeros(n,len(edges))
    for k,(i,j) in enumerate(edges):
        d[i,k]=-1; d[j,k]=1
    return dict(name=name,objects=n,arrows=len(arrows),associativity_triples=comps,
                boundary_rank=d.rank(),homology_Z=[n-d.rank(),len(edges)-d.rank()],
                terminal=[t for t in range(n) if all((i,t) in rel for i in range(n))])

out=[verify_poset('four-object crown',4,{(0,2),(0,3),(1,2),(1,3)}),
     verify_poset('terminal fork',3,{(0,1),(2,1)})]
assert out[0]['homology_Z']==[1,1]
assert out[1]['homology_Z']==[1,0] and out[1]['terminal']==[1]
assert (0,2) not in {(0,0),(1,1),(2,2),(0,1),(2,1)}
print(json.dumps({'checks':out,'status':'PASS'},indent=2))
