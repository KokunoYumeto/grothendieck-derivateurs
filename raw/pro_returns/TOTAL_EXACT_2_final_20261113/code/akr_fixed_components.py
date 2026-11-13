from pathlib import Path
import sys,json
from collections import defaultdict
from akr_stage_model import Cat,quotient_H
C=Cat();V=C.obj('V',1);W=C.obj('W',3)
for i in range(3):C.hom[V,W].add((i,))
original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
for (x,y),fs in sorted(original.items()):
    for i,f in enumerate(fs):
        for j,g in enumerate(fs):C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
for x in (V,W):
    for y in (V,W):C.sum(f'S_{x}_{y}',x,y)
if '--k2' in sys.argv:
    t=C.names.index('Q_0_1_0_1');fs=sorted(C.hom[W,t]);f,g=fs[:2]
    C.qfilter('Q_K2_selected',W,t,f,g,153,3)
if '--critical' in sys.argv:
    left=C.names.index('Q_0_1_0_1');right=C.names.index('Q_0_1_1_0')
    t=C.sum('S_K2_two_cycle_targets',left,right)
    lf=next(iter(C.hom[left,t]));rg=next(iter(C.hom[right,t]))
    f=tuple(lf[j] for j in sorted(C.hom[W,left])[0]);g=tuple(rg[j] for j in sorted(C.hom[W,right])[0])
    C.qfilter('Q_K3_selected_cross_sum',W,t,f,g,297,3)
vals,labs=quotient_H(C)
fail=[]; count=0
for (x,y),fs in list(C.hom.items()):
    if x==y or x in (0,1):continue
    graph=defaultdict(set)
    for b in C.hom.get((W,x),()):
        graph[b[0]].add(b[1]);graph[b[1]].add(b[0])
    fs=sorted(fs)
    for i,f in enumerate(fs):
        for g in fs[:i]:
            count+=1
            fixed={v for v in range(C.size[x]) if f[v]==g[v]}
            bycomp=defaultdict(set)
            for v in fixed:bycomp[labs[x][v]].add(v)
            for component,subset in bycomp.items():
                unseen=set(subset); comps=[]
                while unseen:
                    todo=[unseen.pop()]; reached=set(todo)
                    while todo:
                        for w in graph[todo.pop()] & unseen:
                            unseen.remove(w);reached.add(w);todo.append(w)
                    comps.append(sorted(reached))
                if len(comps)>1:
                    fail.append({'source':C.names[x],'target':C.names[y],'f':f,'g':g,'fixed_components_same_H_class':comps})
                    if len(fail)>=5:break
            if len(fail)>=5:break
        if len(fail)>=5:break
    if len(fail)>=5:break
print(json.dumps({'objects':len(C.size),'pairs_checked':count,'fixed_component_failures':fail},indent=2))
