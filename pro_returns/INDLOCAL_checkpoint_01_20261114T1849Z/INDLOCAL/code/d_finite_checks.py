#!/usr/bin/env python3
"""Exact finite certificates for Part D. Uses only the Python standard library.

The rank calculation uses Fraction, never floating point. Categories are
explicitly enumerated by source, target, and paths; every associativity
instance is checked. The fibrant replacements in the prose are infinite
and are not represented as finite computational certificates.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

def rank(rows):
    if not rows: return 0
    a=[[Fraction(x) for x in row] for row in rows]
    h=w=0
    nr,nc=len(a),len(a[0])
    for c in range(nc):
        k=next((k for k in range(h,nr) if a[k][c]),None)
        if k is None: continue
        a[h],a[k]=a[k],a[h]
        t=a[h][c]; a[h]=[v/t for v in a[h]]
        for k in range(nr):
            if k!=h and a[k][c]:
                t=a[k][c]; a[k]=[v-t*u for v,u in zip(a[k],a[h])]
        h+=1
        if h==nr:break
    return h

# Six-point poset P = S^0 * S^0 * S^0.
vertices=tuple(range(6))
level=lambda x:x//2
le=lambda x,y:x==y or level(x)<level(y)
P1=[(x,y) for x in vertices for y in vertices if x!=y and le(x,y)]
P2=[(x,y,z) for x,y,z in product(vertices,repeat=3) if level(x)<level(y)<level(z)]
assert len(P1)==12 and len(P2)==8
# Free category X on the eight adjacent-level Hasse arrows.
X1=[(x,y) for x in vertices for y in vertices if level(y)==level(x)+1]
X1 += P2
# Nonidentity morphism represented by its full directed path.
def src(a):return a[0]
def tgt(a):return a[-1]
def comp(a,b):
    assert tgt(a)==src(b)
    return a+b[1:]
Xall=[(v,) for v in vertices]+X1
assert len(Xall)==22
for a,b,c in product(Xall,repeat=3):
    if tgt(a)==src(b) and tgt(b)==src(c):
        assert comp(comp(a,b),c)==comp(a,comp(b,c))
X2=[(a,b) for a,b in product(X1,repeat=2) if tgt(a)==src(b)]
assert len(X2)==8

def betti(vs,edges,triangles,faces):
    d1=[[0]*len(edges) for v in vs]
    vi={v:i for i,v in enumerate(vs)};ei={e:i for i,e in enumerate(edges)}
    for k,e in enumerate(edges):
        d1[vi[src(e)]][k]-=1;d1[vi[tgt(e)]][k]+=1
    d2=[[0]*len(triangles) for e in edges]
    for k,t in enumerate(triangles):
        for sign,e in faces(t):d2[ei[e]][k]+=sign
    assert all(sum(d1[i][j]*d2[j][k] for j in range(len(edges)))==0
               for i in range(len(vs)) for k in range(len(triangles)))
    r1,r2=rank(d1),rank(d2)
    return [len(vs)-r1,len(edges)-r1-r2,len(triangles)-r2]
PX_betti=betti(vertices,P1,P2,lambda t:[(1,(t[1],t[2])),(-1,(t[0],t[2])),(1,(t[0],t[1]))])
XX_betti=betti(vertices,X1,X2,lambda t:[(1,t[1]),(-1,comp(*t)),(1,t[0])])
assert PX_betti==[1,0,1] and XX_betti==[1,3,0]
# Each 2-simplex of N X contains its own unique composite edge, allowing
# an elementary collapse onto the Hasse graph. Verify uniqueness directly.
composites=[comp(*t) for t in X2]
assert len(set(composites))==len(X2)
assert set(composites)==set(a for a in X1 if len(a)==3)

# D.5: the initial fork has no common upper bound of u and v.
F=(0,1,2) # 0=o, 1=u, 2=v
fle=lambda x,y:x==y or x==0
square_extensions=[w for w in F if fle(1,w) and fle(2,w)]
assert square_extensions==[]
# Successive maps [1]→F for the padded fence 0 ← 0' → 1.
padded=((0,1),(0,0),(2,2))
assert all(fle(a,b) for a,b in padded)
assert all(fle(padded[1][i],padded[0][i]) for i in range(2))
assert all(fle(padded[1][i],padded[2][i]) for i in range(2))
# Exact retraction witness proving [0]→[1] is a retract of cSd² endpoint.
zle=lambda x,y:x==y or (x%2==0 and abs(x-y)==1)
section=(0,1)
retract=(0,1,1,1,1)
assert all((not zle(x,y)) or retract[x]<=retract[y] for x,y in product(range(5),repeat=2))
assert tuple(retract[i] for i in section)==(0,1)

result={
 'D5':{'fixed_square_extensions':0,'padded_fence_maps':padded,'padded_maps_and_transformations_checked':True,
       'cofibration_retract_section':section,'cofibration_retract_projection':retract},
 'D6':{'P_objects':6,'P_morphisms':18,'P_nondegenerate_2simplices':8,'P_betti_over_Q':PX_betti,
       'X_objects':6,'X_morphisms':22,'X_nondegenerate_2simplices':8,'X_betti_over_Q':XX_betti,
       'X_associativity_checked':True,'X_collapses_to_hasse_graph':True,'graph_rank':3},
 'scope':'Finite certificates only; fibrancy of the infinite replacement follows from the cited model structure, not finite testing.'
}
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.out').write_text(json.dumps(result,indent=2)+'\n')
