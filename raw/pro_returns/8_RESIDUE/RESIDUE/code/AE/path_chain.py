#!/usr/bin/env python3
"""Exact full fixed-shape path posets for [2], W={identities,0->2}.
No finite truncation is claimed to calculate the all-type limit.
Beat-point removal provides certificates of contractible components.
"""
from itertools import product
import json, pathlib

def paths(n,a,b):
    out=[]
    def go(prefix):
        k=len(prefix)-1
        if k==2*n:
            if prefix[-1]==b:out.append(tuple(prefix))
            return
        for x in range(3):
            prev=prefix[-1]
            ok=(x==prev or (x,prev)==(0,2)) if k%2==0 else prev<=x
            if ok:go(prefix+[x])
    go([a]);return out

def audit(n,a,b):
    p=paths(n,a,b);N=len(p)
    lower=[set() for _ in p];upper=[set() for _ in p]
    for i,u in enumerate(p):
        for j,v in enumerate(p):
            if i!=j and all(x<=y for x,y in zip(u,v)):
                upper[i].add(j);lower[j].add(i)
    active=set(range(N));cert=[]
    while True:
        found=False
        for i in sorted(active):
            lo=lower[i]&active;up=upper[i]&active
            maxlo=[j for j in lo if lo <= lower[j]|{j}]
            minup=[j for j in up if up <= upper[j]|{j}]
            if maxlo or minup:
                tgt=(maxlo or minup)[0]
                cert.append([i,tgt,'down' if maxlo else 'up'])
                active.remove(i);found=True;break
        if not found:break
    core_comps=[];unseen=set(active)
    while unseen:
        seed=next(iter(unseen));st=[seed];unseen.remove(seed);comp=[]
        while st:
            i=st.pop();comp.append(i)
            for j in (lower[i]|upper[i])&unseen:
                unseen.remove(j);st.append(j)
        core_comps.append(sorted(comp))
    return {'n':n,'length':2*n,'a':a,'b':b,'objects':N,'nonidentity_arrows':sum(map(len,upper)),
       'beat_removals':len(cert),'core_components':list(map(len,core_comps)),
       'contractible_components_certified':all(len(c)==1 for c in core_comps),
       'core_paths':[[p[i] for i in c] for c in core_comps], 'certificate':cert}

if __name__=='__main__':
    data=[audit(n,a,b) for n in range(1,7) for a in range(3) for b in range(3)]
    path=pathlib.Path(__file__).with_name('path_chain_output.json');path.write_text(json.dumps(data,indent=2))
    for r in data:
        print(r['length'],r['a'],r['b'],r['objects'],r['nonidentity_arrows'],r['core_components'])
