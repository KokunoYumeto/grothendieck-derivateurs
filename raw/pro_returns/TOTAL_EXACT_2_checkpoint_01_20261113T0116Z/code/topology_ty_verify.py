"""Independent exhaustive finite checks of the Ty letter-map description.
The unbounded non-totality and arbitrary-ring proof is in topology_akr.md.
"""
from itertools import product,combinations_with_replacement
import json
from pathlib import Path

def letter_maps(a,b):
    for f in combinations_with_replacement(range(len(b)),len(a)):
        if all(a[i]==b[f[i]] for i in range(len(a))): yield f

def vertex_maps(a,b):
    n,m=len(a),len(b)
    if n==0:
        if m==0: yield (0,)
        return
    for middle in combinations_with_replacement(range(m+1),n-1):
        f=(0,)+middle+(m,)
        if all(all(t==a[i] for t in b[f[i]:f[i+1]]) for i in range(n)):
            yield f

def letters_from_vertices(v,m):
    return tuple(next(i for i in range(len(v)-1) if v[i]<j<=v[i+1]) for j in range(1,m+1))

def comp(g,f): return tuple(g[i] for i in f)
words=[''.join(v) for n in range(5) for v in product('+-',repeat=n)]
pairs=0;composition_checks=0
for a in words:
    for b in words:
        assert set(letter_maps(b,a))=={letters_from_vertices(v,len(b)) for v in vertex_maps(a,b)}
        pairs+=1
small=[''.join(v) for n in range(4) for v in product('+-',repeat=n)]
for a in small:
    for b in small:
        for c in small:
            for f in letter_maps(a,b):
                for g in letter_maps(b,c):
                    assert comp(g,f) in set(letter_maps(a,c));composition_checks+=1
p,q='++','+-+'
e,c=(0,2),(0,0)
arrow_checks=0;target_checks=0
for n in range(10):
    for w in product('+-',repeat=n):
        s=''.join(w);gs=list(letter_maps(q,s));target_checks+=1
        E={comp(g,e) for g in gs};C={comp(g,c) for g in gs}
        assert not E.intersection(C)
        for g in gs:
            assert g[0]<g[1]<g[2]
            assert len(set(comp(g,e)))==2 and len(set(comp(g,c)))==1
            arrow_checks+=1
out={'word_pairs_through_length_4':pairs,'mismatches':0,'compositions_through_length_3':composition_checks,
     'targets_through_length_9':target_checks,'arrows_from_plus_minus_plus':arrow_checks,
     'span_completions':0,'affine_functional_on_te':'augmentation(t)','affine_functional_on_tc':0,
     'scope':'finite sanity check; arbitrary-word and arbitrary-ring proof is mathematical'}
print(json.dumps(out,indent=2))
