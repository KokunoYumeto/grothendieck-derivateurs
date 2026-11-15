#!/usr/bin/env python3
"""Enumerate all monotone maps from the triangle face poset to its subdivision."""
import itertools
import json
from pathlib import Path

vertices=['v0','v1','v2']
edges=['e0','e1','e2']
objects=vertices+edges
incidences=[('v0','e0'),('v1','e0'),('v1','e1'),('v2','e1'),('v2','e2'),('v0','e2')]
chains=[(x,) for x in objects]+[(v,e) for v,e in incidences]
leq=lambda a,b: set(a)<=set(b)
cycleP=['v0','e0','v1','e1','v2','e2']
cycleQ=[]
for a,b in zip(cycleP,cycleP[1:]+cycleP[:1]):
    cycleQ.extend([(a,), next(ch for ch in chains if set(ch)=={a,b})])
pos={x:i for i,x in enumerate(cycleQ)}
counts={}
maps=0
for low in itertools.product(chains,repeat=3):
    choices=[]
    for edge in edges:
        below=[low[vertices.index(v)] for v,e in incidences if e==edge]
        choices.append([q for q in chains if all(leq(p,q) for p in below)])
    for high in itertools.product(*choices):
        f=dict(zip(objects,low+high))
        assert all(leq(f[v],f[e]) for v,e in incidences)
        total=0
        for a,b in zip(cycleP,cycleP[1:]+cycleP[:1]):
            delta=(pos[f[b]]-pos[f[a]])%12
            assert delta in [0,1,11]
            total+=-1 if delta==11 else delta
        assert total%12==0
        degree=total//12
        counts[degree]=counts.get(degree,0)+1
        maps+=1
assert set(counts)=={0}
# Last-element subdivision map: each incidence pair is sent to its edge.
last={ch:(ch[-1] if len(ch)==2 else ch[0]) for ch in chains}
assert all(last[ch] in ch for ch in chains)
result={'source_objects':objects,'source_strict_order':incidences,
        'target_objects_nonempty_chains':chains,'source_oriented_cycle':cycleP,
        'target_oriented_cycle':cycleQ,'monotone_maps_enumerated':maps,
        'degree_distribution':counts,'last_element_map':[(list(k),v) for k,v in last.items()]}
Path(__file__).with_name('poset_subdivision_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('PASS: every reverse monotone map has degree zero.')
