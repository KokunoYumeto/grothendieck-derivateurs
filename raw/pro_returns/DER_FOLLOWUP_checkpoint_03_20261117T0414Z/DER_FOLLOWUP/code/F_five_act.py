#!/usr/bin/env python3
"""Complete finite category and exact integral H1 check for Claim F.2."""
from itertools import product, combinations_with_replacement
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

M=list(combinations_with_replacement(range(2),2))
identity=(0,1)
mul=lambda g,f:tuple(g[i] for i in f)
H=[(0,0),(1,1),(2,2),(0,1),(1,2)]
act=lambda h,m:tuple(h[i] for i in m)
for f,g,h in product(M,repeat=3):
    assert mul(h,mul(g,f))==mul(mul(h,g),f)
for h,f,g in product(H,M,M):
    assert act(act(h,g),f)==act(h,mul(g,f))
E=[(act(k,m),k,m) for k in H for m in M]
edges={(0,1),(1,2)}
assert not any(a[0] in edges and a[2]!=identity for a in E)
assert all(any(a[0]==(1,1) and a[1]==e for a in E) for e in edges)
assert not any(all(any(a[0]==e and a[1]==z for a in E) for e in edges) for z in H)

def fibre(h):
    return [0] if h in edges else [0,1]
DH=[(h,i) for h in H for i in fibre(h)]
DE=[]
for h,k,m in E:
    for i in fibre(h):
        j=0 if k in edges else i
        DE.append(((h,i),(k,j),m))

def homology1(objects,arrows):
    nonid=[a for a in arrows if a[2]!=identity]
    parent={v:v for v in objects}
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    tree=set()
    for a in nonid:
        x,y=root(a[0]),root(a[1])
        if x!=y:
            parent[y]=x
            tree.add(a)
    components=len({root(v) for v in objects})
    basis=[a for a in nonid if a not in tree]
    bi={a:i for i,a in enumerate(basis)}
    cols=[]
    pairs=0
    for f in nonid:
        for g in nonid:
            if f[1]!=g[0]:
                continue
            comp=(f[0],g[1],mul(g[2],f[2]))
            assert comp in arrows
            col=[0]*len(basis)
            for a,sign in [(g,1),(comp,-1),(f,1)]:
                if a in bi:
                    col[bi[a]]+=sign
            cols.append(col); pairs+=1
    mat=s.Matrix(len(basis),len(cols),lambda i,j:cols[j][i])
    snf=smith_normal_form(mat,domain=ZZ)
    pivots=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
    return {'objects':len(objects),'arrows':len(arrows),
            'nonidentity_arrows':len(nonid),'composable_nonidentity_pairs':pairs,
            'H0_rank':components,'cycle_basis_size':len(basis),
            'relation_Smith_nonzero_diagonal':pivots,
            'H1_rank':len(basis)-len(pivots),
            'H1_torsion':[d for d in pivots if d>1]}
e=homology1(H,E); d=homology1(DH,DE)
assert (e['H0_rank'],e['H1_rank'],e['H1_torsion'])==(1,0,[])
assert (d['H0_rank'],d['H1_rank'],d['H1_torsion'])==(1,1,[])
print(json.dumps({'status':'passed','monoid':M,'act':H,
 'monoid_associativity_triples':len(M)**3,'act_laws':len(H)*len(M)**2,
 'element_category':e,'doubled_category':d,
 'exact_obstruction':'H1 of doubled action component = Z'},indent=2))
