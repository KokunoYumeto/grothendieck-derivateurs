#!/usr/bin/env python3
"""Independent finite checks for B.1, B.6 and the presentation in B.7.

No finite truncation is used to prove an infinite cofinality claim.
All maps are monotone sign-preserving maps of letter positions.
"""
from itertools import product, combinations_with_replacement
from collections import Counter
import json

def words(n):
    return [tuple(w) for k in range(n+1) for w in product('+-', repeat=k)]

def maps(a,b,injective=False):
    for f in combinations_with_replacement(range(len(b)),len(a)):
        if all(a[i]==b[f[i]] for i in range(len(a))):
            if not injective or len(set(f))==len(f):
                yield f

def compose(g,f):
    return tuple(g[i] for i in f)

def runs(w):
    return sum(i==0 or s!=w[i-1] for i,s in enumerate(w))

def pairs(w):
    return {(p,q) for p in range(len(w)) for q in range(p+1,len(w))
            if w[p]=='+' and w[q]=='-'}

def marked(w,pq):
    p,q=pq
    return any(w[x]=='-' and w[y]=='+' for x in range(p+1,q)
               for y in range(x+1,q))

BASE=None
def S(w):
    return {BASE}|{pq for pq in pairs(w) if not marked(w,pq)}

def action(w,v,f,x):
    if x is BASE:
        return BASE
    y=tuple(f[i] for i in x)
    return BASE if marked(v,y) else y

def amalgam_over_target(v,w,pv,pw,g):
    """B.7 comma contraction, with tagged points and two glued anchors."""
    anchors={pv[0]:pw[0],pv[1]:pw[1]}
    def vi(i):
        return ('a',anchors[i]) if i in anchors else ('v',i)
    def wi(j):
        return ('a',j) if j in pw else ('w',j)
    out=[]
    for j in range(len(w)):
        var=[i for i,x in enumerate(g) if x==j]
        if j in pw:
            pa=pv[pw.index(j)]
            out += [vi(i) for i in var if i<pa]
            out += [wi(j)]
            out += [vi(i) for i in var if i>pa]
        else:
            out += [vi(i) for i in var]+[wi(j)]
    idx={p:i for i,p in enumerate(out)}
    sign=tuple(w[p[1]] if p[0] in ('a','w') else v[p[1]] for p in out)
    fvi=tuple(idx[vi(i)] for i in range(len(v)))
    fwi=tuple(idx[wi(j)] for j in range(len(w)))
    h=tuple(g[p[1]] if p[0]=='v' else p[1] for p in out)
    assert fvi in list(maps(v,sign,True))
    assert fwi in list(maps(w,sign,True))
    assert h in list(maps(sign,w))
    assert compose(h,fvi)==g
    assert compose(h,fwi)==tuple(range(len(w)))
    assert tuple(fvi[x] for x in pv)==tuple(fwi[x] for x in pw)
    assert marked(sign,tuple(fwi[x] for x in pw))
    return out,sign,vi,wi

def fixed_amalgam(v,pv):
    """B.7 injection-only contraction with fixed b=+-+- at anchors 0,3."""
    w=tuple('+-+-'); pw=(0,3)
    p,q=pv
    points=[('v',i) for i in range(p)]+[('a',0)]
    points += [('v',i) for i in range(p+1,q)]
    points += [('w',1),('w',2),('a',3)]
    points += [('v',i) for i in range(q+1,len(v))]
    idx={x:i for i,x in enumerate(points)}
    vi=lambda i: ('a',0) if i==p else (('a',3) if i==q else ('v',i))
    wi=lambda j: ('a',j) if j in pw else ('w',j)
    sign=tuple(v[i] if tag=='v' else w[i] for tag,i in points)
    assert tuple(idx[vi(i)] for i in range(len(v))) in list(maps(v,sign,True))
    assert tuple(idx[wi(j)] for j in range(4)) in list(maps(w,sign,True))
    return points,sign,vi,wi

counts=Counter()
W=words(4)
hom={(a,b):list(maps(a,b)) for a in W for b in W}
for w in W:
    represented={tuple(f[i] for i in (0,3)) for f in maps(tuple('+-+-'),w)}
    assert represented=={pq for pq in pairs(w) if marked(w,pq)}
    counts['presentation_objects']+=1
    for x in S(w):
        assert action(w,w,tuple(range(len(w))),x)==x
        counts['identities']+=1
for a in W:
    for b in W:
        for f in hom[a,b]:
            for x in S(a):
                assert action(a,b,f,x) in S(b)
                counts['well_defined_images']+=1
            for c in W:
                for g in hom[b,c]:
                    gf=compose(g,f)
                    for x in S(a):
                        assert action(a,c,gf,x)==action(b,c,g,action(a,b,f,x))
                        counts['functor_laws']+=1

# R12's two image sets, tested in all targets of length <=8.
a=tuple('++'); b=tuple('+-+')
for w in words(8):
    left={compose(g,(0,2)) for g in maps(b,w)}
    right={compose(g,(0,0)) for g in maps(b,w)}
    assert left.isdisjoint(right)
    for g in maps(b,w):
        assert len(set(g))==3
        counts['R12_injective_maps']+=1
    counts['R12_targets']+=1

# B.6: exact three-point local fibre, and all map/composition cases on the
# length-four truncation. Upper-region values are represented by None.
def B6(w):
    return {BASE} if runs(w)>1 else set(maps(tuple('++'),w))
def B6map(a,b,f,x):
    return BASE if runs(b)>1 else compose(f,x)
assert len(B6(tuple('++')))==3
for a in W:
    for b in W:
        for f in hom[a,b]:
            assert runs(a)<=runs(b)
            for x in B6(a):
                assert B6map(a,b,f,x) in B6(b)
            for c in W:
                for g in hom[b,c]:
                    for x in B6(a):
                        assert B6map(a,c,compose(g,f),x)==B6map(b,c,g,B6map(a,b,f,x))
                        counts['B6_functor_laws']+=1

# Every marked object up to length five, with all maps to marked targets
# up to length five, for the explicit comma amalgam.
MW=[(w,p) for w in words(5) for p in pairs(w) if marked(w,p)]
for v,pv in MW:
    fixed_amalgam(v,pv)
    counts['fixed_amalgams']+=1
    for w,pw in MW:
        for g in maps(v,w):
            if tuple(g[i] for i in pv)!=pw:
                continue
            amalgam_over_target(v,w,pv,pw,g)
            counts['comma_amalgams']+=1

# Naturality on all injective marked embeddings among the same objects.
for v,pv in MW:
    old,os,ovi,owi=fixed_amalgam(v,pv)
    for vp,pvp in MW:
        new,ns,nvi,nwi=fixed_amalgam(vp,pvp)
        ni={p:i for i,p in enumerate(new)}
        for h in maps(v,vp,True):
            if tuple(h[i] for i in pv)!=pvp:
                continue
            induced=tuple(ni[nvi(h[i])] if tag=='v' else ni[nwi(i)]
                          for tag,i in old)
            assert induced in list(maps(os,ns,True))
            counts['fixed_amalgam_naturality']+=1

for n in range(1,61):
    j=tuple('+' if i%2==0 else '-' for i in range(n))
    survivors=S(j)-{BASE}
    assert survivors=={(i,i+1) for i in range(0,n-1,2)}
    counts['alternating_stages']+=1

print(json.dumps({'status':'passed','bounds':{'functor_word_length':4,
    'R12_target_length':8,'amalgam_word_length':5,'alternating_length':60},
    'checks':dict(sorted(counts.items()))},indent=2))
