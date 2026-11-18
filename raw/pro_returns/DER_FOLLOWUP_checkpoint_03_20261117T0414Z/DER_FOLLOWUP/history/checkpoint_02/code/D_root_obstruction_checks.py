#!/usr/bin/env python3
"""Check the finite graph behind the failed first-return-loop replacement.

The proof that there are infinitely many free generators is the exact normal
form a c^n b in the attempt note. This bounded enumeration only checks the given
finite graph and every word in the stated range; it is not an infinite proof.
"""
from pathlib import Path
import json
edges={'a':('x','v'),'b':('v','x'),'c':('v','v')}
paths=[('x','')];loops=[];first=[]
for length in range(1,15):
    paths=[(t,w+a) for s,w in paths for a,(u,t) in edges.items() if s==u]
    for t,w in paths:
        if t!='x':continue
        loops.append(w)
        pieces=[];start=0;vertex='x'
        for i,a in enumerate(w):
            assert edges[a][0]==vertex;vertex=edges[a][1]
            if vertex=='x':pieces.append(w[start:i+1]);start=i+1
        assert start==len(w)
        assert all(p[0]=='a' and p[-1]=='b' and set(p[1:-1])<=set('c') for p in pieces)
        if len(pieces)==1:first.append(w)
assert first==['a'+'c'*n+'b' for n in range(13)]
rank=len(edges)-2+1
assert rank==2
out={'graph_vertices':['x','v'],'graph_edges':edges,
 'underlying_graph_first_betti_number':rank,'maximum_path_length':14,
 'loops_checked':len(loops),'first_return_generators_checked':len(first),
 'exact_first_return_normal_form':'a c^n b, n >= 0',
 'unique_loop_factorization_at_visits_to_x':True,
 'scope':'The loop monoid has infinitely many free generators; its inclusion does not recover the rank-two graph fundamental group.'}
(Path(__file__).resolve().parent/'outputs'/'D_root_obstruction_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
