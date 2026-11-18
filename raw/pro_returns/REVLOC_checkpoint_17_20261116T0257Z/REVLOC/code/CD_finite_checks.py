#!/usr/bin/env python3
"""Exact finite checks for C.7 and D.0. AI-produced; no priority claimed.

Builds the semisimplicial presentation complexes directly, their finite
face-occurrence categories, and all composition tables. The group-order
calculation uses Todd--Coxeter enumeration; its complete coset table is saved.
"""
from itertools import combinations, product, permutations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r

OUT = Path(__file__).resolve().parent / 'outputs'
OUT.mkdir(exist_ok=True)

def presentation_complex(words):
    vertices = ('v',) + tuple(f'c{k}' for k in range(len(words)))
    edges = ('a', 'b') + tuple(f'r{k}_{i}' for k,w in enumerate(words) for i in range(len(w)))
    faces = {}
    for e in edges:
        faces[e] = ('v','v') if e in ('a','b') else ('v',f'c{e[1]}')
    triangles = []
    for k,w in enumerate(words):
        for i,letter in enumerate(w):
            t = f't{k}_{i}'
            triangles.append(t)
            r0, r1 = f'r{k}_{i}', f'r{k}_{(i+1)%len(w)}'
            faces[t] = (letter.lower(),r1,r0) if letter.islower() else (letter.lower(),r0,r1)
    simplices = (vertices, edges, tuple(triangles))
    def pull(dim,name,inj):
        if len(inj) == dim+1:
            assert inj == tuple(range(dim+1))
            return name
        if dim == 1:
            return faces[name][1-inj[0]]
        if dim == 2 and len(inj) == 2:
            return faces[name][next(i for i in range(3) if i not in inj)]
        if dim == 2 and len(inj) == 1:
            return f'c{name[1]}' if inj[0] == 0 else 'v'
        raise ValueError((dim,name,inj))
    objects = [(dim,name) for dim,ss in enumerate(simplices) for name in ss]
    oi = {o:i for i,o in enumerate(objects)}
    arrows = []
    for target,(dim,name) in enumerate(objects):
        for mdim in range(dim+1):
            for inj in combinations(range(dim+1),mdim+1):
                source = oi[(mdim,pull(dim,name,inj))]
                arrows.append((source,target,inj))
    ai = {a:i for i,a in enumerate(arrows)}
    identities = [ai[(i,i,tuple(range(d+1)))] for i,(d,_) in enumerate(objects)]
    comp = {}
    for g,(s2,t2,j) in enumerate(arrows):
        for f,(s1,t1,i) in enumerate(arrows):
            if t1 == s2:
                comp[g,f] = ai[(s1,t2,tuple(j[k] for k in i))]
    triples = 0
    for (g,f),gf in comp.items():
        for h,(s,t,_) in enumerate(arrows):
            if s == arrows[g][1]:
                assert comp[h,gf] == comp[comp[h,g],f]
                triples += 1
    for f,(s,t,_) in enumerate(arrows):
        assert comp[f,identities[s]] == f == comp[identities[t],f]
    d1 = sp.zeros(len(vertices),len(edges))
    for j,e in enumerate(edges):
        d1[vertices.index(faces[e][0]),j] += 1
        d1[vertices.index(faces[e][1]),j] -= 1
    d2 = sp.zeros(len(edges),len(triangles))
    for j,t in enumerate(triangles):
        for i,e in enumerate(faces[t]):
            d2[edges.index(e),j] += (-1)**i
    assert d1*d2 == sp.zeros(len(vertices),len(triangles))
    s2 = smith_normal_form(d2,domain=ZZ)
    inv = [abs(int(s2[i,i])) for i in range(min(s2.shape)) if s2[i,i]]
    assert all(x == 1 for x in inv), 'Image of d2 must be primitive for this quick homology check'
    betti = [len(vertices)-d1.rank(),len(edges)-d1.rank()-d2.rank(),len(triangles)-d2.rank()]
    return {'words':words,'f_vector':list(map(len,simplices)), 'homology_free_ranks':betti,
            'd2_smith_nonzero':inv,'objects':objects,'arrows':arrows,
            'composition':[[g,f,gf] for (g,f),gf in sorted(comp.items())],
            'associativity_triples_checked':triples}

P = presentation_complex(('aaaaaBBB','bbbBABA'))
assert P['homology_free_ranks'] == [1,0,0]
assert (len(P['objects']),len(P['arrows'])) == (35,159)
T = presentation_complex(('abaBAB',))
assert T['homology_free_ranks'] == [1,1,0]

def perm_mul(x,y): return tuple(x[y[i]] for i in range(len(x)))
a3,b3 = (1,0,2),(0,2,1)
assert perm_mul(perm_mul(a3,b3),a3) == perm_mul(perm_mul(b3,a3),b3)
assert perm_mul(a3,b3) != perm_mul(b3,a3)
S3 = set(permutations(range(3)))
assert len(S3) == 6

F,a,b = free_group('a,b')
G = FpGroup(F,[a**5*b**-3, b**3*(a*b)**-2])
ct = coset_enumeration_r(G,[])
ct.compress(); ct.standardize()
assert ct.n == 120
assert all(v is not None for row in ct.table for v in row)
coset_table = ct.table

def mm(x,y):
    a,b,c,d=x; e,f,g,h=y
    return ((a*e+b*g)%5,(a*f+b*h)%5,(c*e+d*g)%5,(c*f+d*h)%5)
I=(1,0,0,1); minusI=(4,0,0,4)
def power(x,n):
    z=I
    for _ in range(n): z=mm(z,x)
    return z
SL2=[x for x in product(range(5),repeat=4) if (x[0]*x[3]-x[1]*x[2])%5==1]
assert len(SL2)==120
chosen=None
for aa in SL2:
    if power(aa,5)!=minusI: continue
    for bb in SL2:
        if power(bb,3)!=minusI or power(mm(aa,bb),2)!=minusI: continue
        subgroup={I}; frontier=[I]
        while frontier:
            z=frontier.pop()
            for g in (aa,bb):
                t=mm(z,g)
                if t not in subgroup: subgroup.add(t);frontier.append(t)
        if len(subgroup)==120:
            chosen=(aa,bb);break
    if chosen:break
assert chosen is not None

data={'poincare':P,'trefoil':T,'trefoil_S3_images':[a3,b3],
      'presentation_boundary':[[5,-2],[-3,1]],'presentation_boundary_determinant':-1,
      'poincare_group_order':120,'poincare_coset_generators':['a','a^-1','b','b^-1'],
      'poincare_coset_table':coset_table,'SL2_F5_generators':chosen,
      'SL2_F5_order':len(SL2),'all_checks_passed':True}
(OUT/'CD_finite_checks.json').write_text(json.dumps(data,indent=2)+'\n')
summary={'P_category':[len(P['objects']),len(P['arrows'])], 'P_homology':P['homology_free_ranks'],
         'P_group_order':120,'T_category':[len(T['objects']),len(T['arrows'])],
         'T_homology':T['homology_free_ranks'],'nonabelian_S3_representation':True,
         'all_checks_passed':True}
print(json.dumps(summary,indent=2))
(OUT/'CD_finite_checks.out').write_text(json.dumps(summary,indent=2)+'\n')
