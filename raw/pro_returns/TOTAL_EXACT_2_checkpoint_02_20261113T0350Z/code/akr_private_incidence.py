"""Finite private-incidence certificates; no assertion of totality."""
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
certificates=[]
for x in range(len(C.size)):
    edges=sorted(C.hom.get((W,x),()))
    incidence=defaultdict(set)
    for i,e in enumerate(edges):
        for p in e:incidence[p].add(i)
    queue=deque(p for p,es in incidence.items() if len(es)==1)
    alive=set(range(len(edges)));peeling=[]
    while queue:
        p=queue.popleft()
        if len(incidence[p])!=1:continue
        i=next(iter(incidence[p]));assert i in alive
        peeling.append([i,p,edges[i].index(p)])
        alive.remove(i)
        for v in edges[i]:
            incidence[v].remove(i)
            if len(incidence[v])==1:queue.append(v)
    assert not alive,(C.names[x],len(alive))
    # Independent certificate replay using the incidence counts only.
    degrees=defaultdict(int)
    for e in edges:
        for p in e:degrees[p]+=1
    removed=set()
    for i,p,slot in peeling:
        assert i not in removed and edges[i][slot]==p and degrees[p]==1
        removed.add(i)
        for v in edges[i]:degrees[v]-=1
    assert len(removed)==len(edges)
    certificates.append({'object':C.names[x],'edges':edges,'peeling':peeling})
    print(json.dumps({'object':C.names[x],'W_arrows':len(edges),'peeling_steps':len(peeling),'remaining_core':len(alive)}))
suffix='critical' if '--critical' in sys.argv else 'k2'
path=Path(__file__).with_name(f'akr_private_incidence_{suffix}_certificate.json')
path.write_text(json.dumps(certificates,separators=(',',':')))
print(json.dumps({'certificate':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'listed finite stages only; every coefficient ring'}))
