from pathlib import Path
import sys,json
from akr_stage_model import Cat
C=Cat();V=C.obj('V',1);W=C.obj('W',3)
for i in range(3):C.hom[V,W].add((i,))
original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
for (x,y),fs in sorted(original.items()):
    for i,f in enumerate(fs):
        for j,g in enumerate(fs):C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
for x in (V,W):
    for y in (V,W):C.sum(f'S_{x}_{y}',x,y)

def check(C,label):
    fails=[];tested=0
    for z in range(len(C.size)):
        incoming=[(x,f,set(f)) for x in range(z+1) for f in C.hom.get((x,z),())]
        for x,f,sf in incoming:
            if x not in (0,1):continue
            for y,g,sg in incoming:
                if len(f)>len(g) or not sf<=sg:continue
                tested+=1
                inv={p:i for i,p in enumerate(g)}
                h=tuple(inv[p] for p in f)
                if h not in C.hom.get((x,y),()):
                    fails.append({'source':C.names[x],'through':C.names[y],'target':C.names[z],'left':f,'right':g,'missing':h})
                    if len(fails)==20:break
            if len(fails)==20:break
        if len(fails)==20:break
    print(json.dumps({'stage':label,'objects':len(C.size),'tested_inclusions':tested,'first_failures':fails},indent=2),flush=True)
check(C,'K1')
left=C.names.index('Q_0_1_0_1');right=C.names.index('Q_0_1_1_0')
t=C.sum('S_K2_two_cycle_targets',left,right)
lf=next(iter(C.hom[left,t]));rg=next(iter(C.hom[right,t]))
f=tuple(lf[j] for j in sorted(C.hom[W,left])[0]);g=tuple(rg[j] for j in sorted(C.hom[W,right])[0])
C.qfilter('Q_K3_selected_cross_sum',W,t,f,g,297,3)
check(C,'selected_critical_K3')
