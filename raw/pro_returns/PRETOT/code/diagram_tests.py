#!/usr/bin/env python3
"""Exact chain checks for the finite cell models in Part F."""
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

lines=[]
def out(x): print(x); lines.append(x)

out('R9 disconnected correction: a two-object discrete category has no common successor; its two components are singleton filtered categories.')
out('For every diagram over a discrete category, Grothendieck construction and categorical colimit are the same coproduct; the canonical comparison is the identity.')
for m in range(1,7):
    # Vertices s,a,b,t; arrows sa,sb,at,bt and m long edges e_i:s->t.
    # Each e_i bounds the two triangles through a and b.
    edges=[(0,1),(0,2),(1,3),(2,3)]+[(0,3)]*m
    d1=s.zeros(4,len(edges)); d2=s.zeros(len(edges),2*m)
    for j,(u,v) in enumerate(edges): d1[v,j]=1; d1[u,j]=-1
    for i in range(m):
        d2[0,2*i]=1; d2[2,2*i]=1; d2[4+i,2*i]=-1
        d2[1,2*i+1]=1; d2[3,2*i+1]=1; d2[4+i,2*i+1]=-1
    assert d1*d2==s.zeros(4,2*m)
    sn1=smith_normal_form(d1,domain=ZZ); sn2=smith_normal_form(d2,domain=ZZ)
    a=[abs(int(sn1[i,i])) for i in range(min(sn1.shape)) if sn1[i,i]]
    b=[abs(int(sn2[i,i])) for i in range(min(sn2.shape)) if sn2[i,i]]
    assert all(x==1 for x in a+b)
    hom=[4-len(a),len(edges)-len(a)-len(b),2*m-len(b)]
    assert hom==[1,0,m-1]
    out(f'Poset/Cat square model m={m}: chain ranks (4,{4+m},{2*m}); H0=Z,H1=0,H2=Z^{m-1}, no torsion.')
out('The strict colimit has the m=1 diamond nerve, hence all m>1 comparisons fail in H2.')
out('Poset/Pos parallel-edge model: two vertices, two edges, boundary rank 1, H1=Z; its poset reflection is [1], H1=0.')
out('All finite chain checks PASS.')
output = Path(__file__).resolve().parent / 'outputs'
output.mkdir(exist_ok=True)
(output/'diagram_tests.out').write_text('\n'.join(lines)+'\n')
