"""Exploratory repaired B.9 stages with small s, NOT admissible C.1 bounds."""
from akr_stage_model import Cat,quotient_H
from collections import defaultdict
from pathlib import Path
import random,json,copy
rng=random.Random(20261113)
C=Cat();V=C.obj('V',1);W=C.obj('W',3)
for i in range(3):C.hom[V,W].add((i,))
L,_=C.qfilter('L',V,W,(0,),(1,),13,3)
R,_=C.qfilter('R',V,W,(1,),(0,),13,3)
S=C.sum('sumLR',L,R)
a=next(iter(C.hom[L,S]));b=next(iter(C.hom[R,S]))
f=tuple(a[t] for t in sorted(C.hom[W,L])[0]);g=tuple(b[t] for t in sorted(C.hom[W,R])[0])
T,_=C.qfilter('cross',W,S,f,g,13,3)
def check(C,target,cap=30000):
    vals,labs=quotient_H(C);graph=defaultdict(set)
    for b in C.hom.get((W,target),()):graph[b[0]].add(b[1]);graph[b[1]].add(b[0])
    count=0
    for x in range(target):
        if C.size[x]<=3:continue
        fs=sorted(C.hom.get((x,target),()))
        pairs=[(i,j) for i in range(len(fs)) for j in range(i)]
        if len(pairs)>cap:pairs=rng.sample(pairs,cap)
        for i,j in pairs:
            f,g=fs[i],fs[j];count+=1
            fixed={f[v] for v in range(C.size[x]) if f[v]==g[v]}
            ed={f[v]:g[v] for v in range(C.size[x]) if f[v]!=g[v]}
            paths=[]
            for v in ed.keys()-set(ed.values()):
                p=[v]
                while p[-1] in ed:p.append(ed[p[-1]])
                paths.append(p)
            assert sum(len(p)-1 for p in paths)==len(ed)
            ss=[('fixed',fixed)]
            for d in range(1,max([len(p) for p in paths]+[1])):
                ss += [('prefix'+str(d),fixed|{v for p in paths for v in p[:-d]}),('suffix'+str(d),fixed|{v for p in paths for v in p[d:]})]
            for lab,subset in ss:
                grouped=defaultdict(set)
                for v in subset:grouped[labs[target][v]].add(v)
                for component,vs in grouped.items():
                    unseen=set(vs);comps=[]
                    while unseen:
                        todo=[unseen.pop()];reach=set(todo)
                        while todo:
                            for w in graph[todo.pop()] & unseen:
                                unseen.remove(w);reach.add(w);todo.append(w)
                        comps.append(sorted(reach))
                    if len(comps)>1:return {'pairs':count,'failure':{'source':C.names[x],'target':C.names[target],'pair':[i,j],'f':f,'g':g,'kind':lab,'components':comps}}
    return {'pairs':count,'failure':None}
print(json.dumps({'scope':'repaired B.9 small parameters; not C.1','base_sizes':C.size,'base_test':check(C,T)}),flush=True)
for trial in range(32):
    D=copy.deepcopy(C);x=rng.choice([L,R,S]);fs=sorted(D.hom[x,T]);i,j=rng.sample(range(len(fs)),2);f,g=fs[i],fs[j]
    edges={f[v]:g[v] for v in range(D.size[x]) if f[v]!=g[v]};paths=[]
    for v in edges.keys()-set(edges.values()):
        p=[v]
        while p[-1] in edges:p.append(edges[p[-1]])
        paths.append(p)
    n=max([len(p) for p in paths]+[3]);n+=1-n%2;s=4*n+1
    z,_=D.qfilter('next',x,T,f,g,s,n)
    out={'trial':trial,'source':D.names[x],'pair':[i,j],'n':n,'s':s,'new_size':D.size[z],**check(D,z)}
    print(json.dumps(out),flush=True)
    if out['failure']:
        Path(__file__).with_name('akr_small_repaired_failure.json').write_text(json.dumps(out,indent=2));break
