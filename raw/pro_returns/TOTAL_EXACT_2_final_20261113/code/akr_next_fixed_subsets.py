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
if '--critical' in sys.argv:
    left=C.names.index('Q_0_1_0_1');right=C.names.index('Q_0_1_1_0')
    t=C.sum('S_K2_two_cycle_targets',left,right)
    lf=next(iter(C.hom[left,t]));rg=next(iter(C.hom[right,t]))
    f=tuple(lf[j] for j in sorted(C.hom[W,left])[0]);g=tuple(rg[j] for j in sorted(C.hom[W,right])[0])
    C.qfilter('Q_K3_selected_cross_sum',W,t,f,g,297,3)
else:
    t=C.names.index('Q_0_1_0_1');fs=sorted(C.hom[W,t]);pick=[int(x) for x in sys.argv[sys.argv.index('--pair')+1].split(',')] if '--pair' in sys.argv else [0,1];f,g=[fs[i] for i in pick]
    C.qfilter('Q_K2_selected',W,t,f,g,153,3)
vals,labs=quotient_H(C)
graphs=[]
for y in range(len(C.size)):
    graph=defaultdict(set)
    for b in C.hom.get((W,y),()):
        graph[b[0]].add(b[1]);graph[b[1]].add(b[0])
    graphs.append(graph)
fails=[];count=0;tests=0
for (x,y),fs in list(C.hom.items()):
    if x==y or x in (0,1):continue
    graph=graphs[y];fs=sorted(fs)
    for i,f in enumerate(fs):
        for g in fs[:i]:
            count+=1
            fixed={f[v] for v in range(C.size[x]) if f[v]==g[v]}
            edges={f[v]:g[v] for v in range(C.size[x]) if f[v]!=g[v]}
            paths=[]
            for v in edges.keys()-set(edges.values()):
                path=[v]
                while path[-1] in edges:path.append(edges[path[-1]])
                paths.append(path)
            assert sum(len(p)-1 for p in paths)==len(edges)
            subsets=[('fixed',fixed)]
            for cut in range(1,max([len(p) for p in paths]+[1])):
                subsets.append((f'prefix_cut_{cut}',fixed|{v for p in paths for v in p[:-cut]}))
                subsets.append((f'suffix_cut_{cut}',fixed|{v for p in paths for v in p[cut:]}))
            for label,subset in subsets:
                tests+=1;bycomp=defaultdict(set)
                for v in subset:bycomp[labs[y][v]].add(v)
                for component,vertices in bycomp.items():
                    unseen=set(vertices);comps=[]
                    while unseen:
                        todo=[unseen.pop()];reached=set(todo)
                        while todo:
                            for w in graph[todo.pop()] & unseen:
                                unseen.remove(w);reached.add(w);todo.append(w)
                        comps.append(sorted(reached))
                    if len(comps)>1:
                        fails.append({'source':C.names[x],'target':C.names[y],'pair_indices':[i,fs.index(g)],'f':f,'g':g,'subset_kind':label,'subset':sorted(subset),'disconnected_in_H_component':comps})
                        if len(fails)>=3:break
                if len(fails)>=3:break
            if len(fails)>=3:break
        if len(fails)>=3:break
    if len(fails)>=3:break
print(json.dumps({'objects':len(C.size),'arrow_pairs_checked':count,'subsets_checked':tests,'failures':fails},indent=2))
