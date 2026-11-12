"""Auxiliary finite check; no assertion about the infinite AKR union."""
from akr_stages import Cat, quotient_H
import json
C=Cat(); V=C.obj('V',1); W=C.obj('W',3)
for i in range(3): C.hom[V,W].add((i,))
original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
for (x,y),fs in sorted(original.items()):
    for i,f in enumerate(fs):
        for j,g in enumerate(fs): C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
for x in (V,W):
    for y in (V,W): C.sum(f'S_{x}_{y}',x,y)
vals,labs=quotient_H(C)
fail=[]; cycles=[]; arrow_count=pair_count=0
for (x,y),fs in C.hom.items():
    for f in fs:
        arrow_count+=1
        hf=tuple(labs[y][f[h]] for h in vals[x])
        if len(set(hf))!=len(hf):fail.append((x,y,f))
    for f in fs:
        for g in fs:
            pair_count+=1
            edges={labs[y][f[h]]:labs[y][g[h]] for h in vals[x] if labs[y][f[h]]!=labs[y][g[h]]}
            for v in edges:
                seen=set();w=v
                while w in edges and w not in seen:seen.add(w);w=edges[w]
                if w in seen:cycles.append((x,y,f,g));break
print(json.dumps({'objects':len(C.size),'arrows_checked':arrow_count,
                  'ordered_parallel_pairs_checked':pair_count,
                  'H_transition_injection_failures':len(fail),
                  'pairs_inducing_nontrivial_cycles_on_H_components':len(cycles),
                  'scope':'finite repaired K1 only'},indent=2))
assert not fail and not cycles
