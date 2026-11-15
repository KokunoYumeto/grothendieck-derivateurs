"""Private marked-vertex checks for the two protected first-stage cycles."""
from pathlib import Path
from collections import defaultdict,deque
import json,hashlib,sys
from akr_stage_model import Cat
C=Cat();V=C.obj('V',1);W=C.obj('W',3)
for i in range(3):C.hom[V,W].add((i,))
original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
for (x,y),fs in sorted(original.items()):
    for i,f in enumerate(fs):
        for j,g in enumerate(fs):C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
for x in (V,W):
    for y in (V,W):C.sum(f'S_{x}_{y}',x,y)
if '--critical' in sys.argv:
    left=C.names.index('Q_0_1_0_1');right=C.names.index('Q_0_1_1_0')
    t=C.sum('S_K2_two_cycle_targets',left,right)
    lf=next(iter(C.hom[left,t]));rg=next(iter(C.hom[right,t]))
    f=tuple(lf[j] for j in sorted(C.hom[W,left])[0]);g=tuple(rg[j] for j in sorted(C.hom[W,right])[0])
    C.qfilter('Q_K3_selected_cross_sum',W,t,f,g,297,3)
else:
    t=C.names.index('Q_0_1_0_1');fs=sorted(C.hom[W,t]);f,g=fs[:2]
    C.qfilter('Q_K2_selected',W,t,f,g,153,3)

protected=[C.names.index('Q_0_1_0_1'),C.names.index('Q_0_1_1_0')]
marked={p:{v for e in C.hom[W,p] for v in e[:2]} for p in protected}
assert all(len(s)==45 for s in marked.values())
all_cells={}
for x in range(len(C.size)):
    cells=[(p,h,frozenset(h[v] for v in marked[p])) for p in protected for h in sorted(C.hom.get((p,x),()))]
    all_cells[x]=cells
    incidence=defaultdict(set)
    for i,(_,_,vs) in enumerate(cells):
        for v in vs:incidence[v].add(i)
    queue=deque(v for v,ii in incidence.items() if len(ii)==1)
    alive=set(range(len(cells)));steps=0
    while queue:
        v=queue.popleft()
        if len(incidence[v])!=1:continue
        i=next(iter(incidence[v]));alive.remove(i);steps+=1
        for w in cells[i][2]:
            incidence[w].remove(i)
            if len(incidence[w])==1:queue.append(w)
    assert not alive,(C.names[x],len(alive))
    print(json.dumps({'object':C.names[x],'protected_cells':len(cells),'private_marked_vertex_steps':steps,'remaining':len(alive)}),flush=True)
# Relative test at top object for all incoming arrows with domain size >3.
z=len(C.size)-1;cells=all_cells[z];relative_arrows=0;relative_cells=0
for y in range(z):
    if C.size[y]<=3:continue
    for g in C.hom.get((y,z),()):
        relative_arrows+=1;image=set(g)
        factoring={(p,tuple(g[v] for v in b)) for p in protected for b in C.hom.get((p,y),())}
        fresh=[i for i,(p,h,vs) in enumerate(cells) if (p,h) not in factoring]
        for i in fresh:assert len(cells[i][2]&image)<=2
        incidence=defaultdict(set)
        for i in fresh:
            for v in cells[i][2]-image:incidence[v].add(i)
        queue=deque(v for v,ii in incidence.items() if len(ii)==1)
        alive=set(fresh)
        while queue:
            v=queue.popleft()
            if len(incidence[v])!=1:continue
            i=next(iter(incidence[v]));alive.remove(i)
            for w in cells[i][2]-image:
                incidence[w].remove(i)
                if len(incidence[w])==1:queue.append(w)
        assert not alive,(y,len(alive));relative_cells+=len(fresh)
print(json.dumps({'relative_top':C.names[z],'incoming_arrows_checked':relative_arrows,'new_protected_cells_peeled_cumulative':relative_cells,'scope':'finite critical or selected substage only; all-stage theorem proved separately'}),flush=True)
