"""Exact finite-poset search for XIIc B062, with certified rewriting completions.

We enumerate naturally labelled finite posets (so every isomorphism class occurs),
require every pair with a common upper bound to have a meet, enumerate all W,
and enforce identities and two-out-of-three. Intrinsic fibres and axiom (b) are
tested by all strict pullbacks. Ordinary localizations are computed by terminating
Knuth--Bendix rewriting on the path category. A successful completion checks ALL
overlap and inclusion critical pairs. A finite set of normal forms then gives
the exact localization, with no path-length approximation. Noncompleted or
infinite normal-form presentations are reported as skipped, never certified.
"""
from itertools import combinations,product
from pathlib import Path
from collections import Counter
import json,sys,time

ROOT=Path(__file__).resolve().parents[1]
MAXN=int(sys.argv[1]) if len(sys.argv)>1 else 5
STATS=Counter(); SKIPS=[]; LOG=[]; CACHE={}

class CompletionLimit(Exception):pass

class Localization:
    def __init__(self,objects,rel,W):
        self.objects=tuple(sorted(objects))
        orig=sorted((a,b) for a,b in rel if a!=b and a in objects and b in objects)
        self.edges=[(a,b,1) for a,b in orig]+[(b,a,-1) for a,b in orig if (a,b) in W]
        self.orig={(a,b):i for i,(a,b,sgn) in enumerate(self.edges) if sgn==1}
        self.inv={(b,a):i for i,(a,b,sgn) in enumerate(self.edges) if sgn==-1}
        self.rules={}
        for (a,b),f in self.orig.items():
            for (c,d),g in self.orig.items():
                if b==c:self.add((f,g),(self.orig[a,d],))
            if (a,b) in W:
                inv=self.inv[a,b]
                self.add((f,inv),());self.add((inv,f),())
        self.complete()
        self.forms={(a,b):[] for a in self.objects for b in self.objects}
        self.form_source={}
        queue=[(a,(),a) for a in self.objects]
        seen=set(queue)
        while queue:
            a,w,b=queue.pop()
            self.forms[a,b].append(w)
            for k,(src,tgt,_) in enumerate(self.edges):
                if src!=b:continue
                v=w+(k,)
                if self.reduce(v)!=v:continue
                if len(v)>30 or len(seen)>5000:raise CompletionLimit('infinite or large normal forms')
                item=(a,v,tgt)
                if item not in seen:seen.add(item);queue.append(item)
        self.iso_objects=set()
        for a,b in product(self.objects,repeat=2):
            if any(self.reduce(f+g)==() and self.reduce(g+f)==()
                   for f in self.forms[a,b] for g in self.forms[b,a]):
                self.iso_objects.add((a,b))

    def reduce(self,w):
        w=tuple(w)
        for _ in range(20000):
            changed=False
            for lhs,rhs in self.rules.items():
                for i in range(len(w)-len(lhs)+1):
                    if w[i:i+len(lhs)]==lhs:
                        w=w[:i]+rhs+w[i+len(lhs):];changed=True;break
                if changed:break
            if not changed:return w
        raise CompletionLimit('reduction budget')

    def add(self,a,b):
        a=self.reduce(a);b=self.reduce(b)
        if a==b:return False
        if (len(a),a)<(len(b),b):a,b=b,a
        self.rules[a]=b
        if len(self.rules)>400 or len(a)>15:raise CompletionLimit('completion budget')
        return True

    def complete(self):
        for roundnum in range(300):
            old=list(self.rules.items()); added=False
            for a,ar in old:
                for b,br in old:
                    # Overlap a suffix with b prefix, including full matches.
                    for k in range(1,min(len(a),len(b))+1):
                        if a[-k:]==b[:k]:
                            if self.add(ar+b[k:],a[:-k]+br):added=True
                    # Inclusion ambiguity: b inside a.
                    for i in range(len(a)-len(b)+1):
                        if a[i:i+len(b)]==b:
                            if self.add(ar,a[:i]+br+a[i+len(b):]):added=True
            if not added:
                STATS['completed_presentations']+=1
                return
        raise CompletionLimit('completion rounds')

    def image_word(self,source,w):
        out=[]
        for i in w:
            a,b,sgn=source.edges[i]
            out.append(self.orig[a,b] if sgn==1 else self.inv[b,a])
        return self.reduce(tuple(out))

def localize(objects,rel,W):
    key=(tuple(sorted(objects)),tuple(sorted((a,b) for a,b in rel if a in objects and b in objects)),tuple(sorted((a,b) for a,b in W if a in objects and b in objects)))
    if key not in CACHE:
        try:CACHE[key]=Localization(objects,rel,W)
        except CompletionLimit as ex:CACHE[key]=str(ex)
    val=CACHE[key]
    if isinstance(val,str):raise CompletionLimit(val)
    return val

def is_equivalence(source,target):
    for a,b in product(source.objects,repeat=2):
        images=[target.image_word(source,w) for w in source.forms[a,b]]
        if len(images)!=len(set(images)) or set(images)!=set(target.forms[a,b]):return False
    return all(any((a,b) in target.iso_objects for a in source.objects) for b in target.objects)

def enumerate_posets(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        rel={(i,i) for i in range(n)}|{p for k,p in enumerate(pairs) if mask>>k&1}
        if any((a,c) not in rel for a,b in rel for bb,c in rel if b==bb):continue
        meet={};valid=True
        for a,b in product(range(n),repeat=2):
            if not any((a,t) in rel and (b,t) in rel for t in range(n)):continue
            lows=[x for x in range(n) if (x,a) in rel and (x,b) in rel]
            best=[x for x in lows if all((y,x) in rel for y in lows)]
            if len(best)!=1:valid=False;break
            meet[a,b]=best[0]
        if valid:yield rel,meet

def check(n,rel,meet,W):
    fibres={}; slices={}
    for s in range(n):
        objs={x for x in range(n) if (x,s) in rel};slices[s]=objs
        F={x for x in objs if all((meet[a,x],meet[b,x]) in W for a,b in W if b in objs)}
        fibres[s]=F
        for a,b in W:
            if a in F and b in F and any((meet[a,t],meet[b,t]) not in W for t in objs):
                STATS['b_fails']+=1;return None
    STATS['b_holds']+=1
    # With at most one omitted object, every intermediate is an endpoint.
    if all(len(slices[s]-fibres[s])<=1 for s in range(n)):
        STATS['no_proper_intermediate']+=1;return None
    STATS['nontrivial_intermediate_candidates']+=1
    localdata={}
    try:
        for s in range(n):
            F=localize(fibres[s],rel,W);M=localize(slices[s],rel,W)
            if not is_equivalence(F,M):STATS['a_fails']+=1;return None
            localdata[s]=(F,M)
        STATS['a_and_b_hold']+=1
        for s,(F,M) in localdata.items():
            missing=sorted(slices[s]-fibres[s])
            for bits in range(1,(1<<len(missing))-1):
                objects=fibres[s]|{x for i,x in enumerate(missing) if bits>>i&1}
                H=localize(objects,rel,W)
                if not is_equivalence(F,H) or not is_equivalence(H,M):
                    return dict(n=n,rel=sorted(rel),W=sorted(W),base=s,
                                fibres={str(k):sorted(v) for k,v in fibres.items()},H=sorted(objects),
                                normal_forms={str(k):[list(x) for x in v] for k,v in H.forms.items()})
        STATS['c_holds']+=1
    except CompletionLimit as exc:
        STATS['skipped']+=1
        SKIPS.append(dict(n=n,rel=sorted(rel),W=sorted(W),reason=str(exc)))
    return None

start=time.time()
found=None
for n in range(1,MAXN+1):
    before=STATS.copy()
    for rel,meet in enumerate_posets(n):
        STATS['posets_with_pullbacks']+=1
        nonid=sorted((a,b) for a,b in rel if a!=b)
        identities={(x,x) for x in range(n)}
        triples=[((a,b),(b,c),(a,c)) for a,b in rel for bb,c in rel if bb==b]
        for mask in range(1<<len(nonid)):
            W=identities|{p for i,p in enumerate(nonid) if mask>>i&1}
            if any(sum(x in W for x in t)==2 for t in triples):continue
            STATS['two_out_of_three_classes']+=1
            found=check(n,rel,meet,W)
            if found:break
        if found:break
    item={k:STATS[k]-before[k] for k in STATS}
    line=f'n={n}: {item}; elapsed={time.time()-start:.2f}s'
    LOG.append(line);print(line,flush=True)
    if found:break
result={'max_n':MAXN,'found':found,'statistics':dict(STATS),'skips':SKIPS,'log':LOG}
target=ROOT/'code'/f'a_b062_search_n{MAXN}.out.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print('FOUND' if found else 'NO COUNTEREXAMPLE in completely certified cases',flush=True)
print('output',target,flush=True)
