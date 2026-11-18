#!/usr/bin/env python3
"""Finite free-E2 Hopf/Steenrod calculation for Omega^2 Sigma^2 K(F2,2).

The algebra is CLM's free restricted Poisson algebra.  Ordinary Lyndon
brackets and their restricted squares are represented in the free tensor
algebra; the external Pontryagin polynomial algebra is kept separate.
All arithmetic is exact over F2.  This is an authored computation, not
a replacement for the geometric edge/bar arguments in D.2.56.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import D2_fiber_poly_check as bpoly

MAX = 12
WEIGHT = MAX + 1
ZERO = (0, 0, 0, 0)
bpoly.LABEL.clear()
for e in product(range(7), range(5), range(3), range(2)):
    if 0 < bpoly.deg(e) <= MAX:
        bpoly.LABEL[e] = ''.join(g + (str(n) if n > 1 else '')
                                for g,n in zip(('u','v','w','t'),e) if n)
bpoly.EXP.clear()
bpoly.EXP.update({v:k for k,v in bpoly.LABEL.items()})
bpoly.GEN_SQ[3][1] = {(0,0,2,0)}
LABELS = sorted(bpoly.LABEL, key=lambda e:(bpoly.deg(e),e))
LID = {e:i for i,e in enumerate(LABELS)}
LD = [bpoly.deg(e) for e in LABELS]
LW = [d+1 for d in LD]

def xor(*args):
    ans=set()
    for x in args: ans.symmetric_difference_update(x)
    return frozenset(ans)

def aconcat(x,y):
    ans=set()
    for a in x:
        for b in y: ans.symmetric_difference_update({a+b})
    return frozenset(ans)

def alyndon(w):
    return bool(w) and all(w < w[i:] for i in range(1,len(w)))

def words(maxw, prefix=(), wt=0):
    for i,w in enumerate(LW):
        if wt+w > maxw: continue
        p=prefix+(i,)
        yield p
        yield from words(maxw,p,wt+w)

LYNDON = [w for w in words(WEIGHT) if alyndon(w)]

@lru_cache(None)
def split(w):
    assert len(w)>1
    for i in range(1,len(w)):
        if alyndon(w[i:]): return w[:i],w[i:]
    raise AssertionError(w)

@lru_cache(None)
def lexpand(w):
    if len(w)==1:return frozenset({w})
    a,b=split(w)
    x,y=lexpand(a),lexpand(b)
    return xor(aconcat(x,y),aconcat(y,x))

GENS=[]
for w in LYNDON:
    wt=sum(LW[i] for i in w)
    r=0
    while wt*2**r<=WEIGHT:
        GENS.append((w,r))
        r+=1
GENS.sort(key=lambda g:(sum(LW[i] for i in g[0])*2**g[1]-1,g))
GID={g:i for i,g in enumerate(GENS)}
GD=[sum(LW[i] for i in w)*2**r-1 for w,r in GENS]
LABELGEN={e:GID[((LID[e],),0)] for e in LABELS}

@lru_cache(None)
def gexpand(g):
    w,r=GENS[g]
    ans=lexpand(w)
    for _ in range(r):ans=aconcat(ans,ans)
    return ans

LEADING={}
for g in range(len(GENS)):
    ex=gexpand(g)
    lead=min(ex)
    assert lead not in LEADING
    LEADING[lead]=g

@lru_cache(None)
def lie_reduce(ex):
    work=set(ex);out=set()
    while work:
        lead=min(work)
        assert lead in LEADING, ('not a restricted Lie element',lead,work)
        g=LEADING[lead]
        out.symmetric_difference_update({g})
        work.symmetric_difference_update(gexpand(g))
    return frozenset(out)

ONE=frozenset({()})
EMPTY=frozenset()

def mono(*gs):return frozenset({tuple(sorted(gs))})

@lru_cache(None)
def mul(x,y):
    out=set()
    for a in x:
        for b in y:out.symmetric_difference_update({tuple(sorted(a+b))})
    return frozenset(out)

def power(x,n):
    ans=ONE
    for _ in range(n):ans=mul(ans,x)
    return ans

def pdegree(x):
    if not x:return None
    ds={sum(GD[g] for g in m) for m in x}
    assert len(ds)==1,ds
    return next(iter(ds))

@lru_cache(None)
def gbracket(g,h):
    if g==h:return EMPTY
    ex=xor(aconcat(gexpand(g),gexpand(h)),aconcat(gexpand(h),gexpand(g)))
    return frozenset((k,) for k in lie_reduce(ex))

@lru_cache(None)
def bracket(x,y):
    out=EMPTY
    for a in x:
        for b in y:
            for i,g in enumerate(a):
                for j,h in enumerate(b):
                    rest=mono(*(a[:i]+a[i+1:]+b[:j]+b[j+1:]))
                    out=xor(out,mul(rest,gbracket(g,h)))
    return out

@lru_cache(None)
def xi_monomial(m):
    if not m:return EMPTY
    if len(m)==1:
        w,r=GENS[m[0]]
        return mono(GID[(w,r+1)])
    x,y=mono(m[0]),mono(*m[1:])
    return xor(mul(xi(x),power(y,2)),mul(power(x,2),xi(y)),
               mul(mul(x,y),bracket(x,y)))

@lru_cache(None)
def xi(x):
    out=EMPTY;previous=EMPTY
    for m in sorted(x):
        one=frozenset({m})
        out=xor(out,xi_monomial(m),bracket(previous,one))
        previous=xor(previous,one)
    return out

def label(e):return mono(LABELGEN[e])

def named(name):return label(bpoly.EXP[name])

@lru_cache(None)
def sq_gen(k,g):
    if k==0:return mono(g)
    if k>GD[g]:return EMPTY
    w,r=GENS[g]
    if r:
        z=mono(GID[(w,r-1)]);d=pdegree(z)
        out=xi(sq(k//2,z)) if k%2==0 else (power(sq(k//2,z),2) if d%2 else EMPTY)
        for i in range((k+1)//2):
            out=xor(out,bracket(sq(i,z),sq(k-i,z)))
        return out
    if len(w)==1:
        old=LABELS[w[0]]
        return frozenset((LABELGEN[e],) for e in LABELS
                         if bpoly.deg(e)==LD[w[0]]-k and old in bpoly.csq(k,e))
    left,right=split(w)
    x,y=mono(GID[(left,0)]),mono(GID[(right,0)])
    return xor(*(bracket(sq(i,x),sq(k-i,y)) for i in range(k+1)))

@lru_cache(None)
def sq(k,x):
    if k==0:return x
    out=EMPTY
    for m in x:
        total={0:ONE}
        for g in m:
            nxt={}
            for i,value in total.items():
                for j in range(k-i+1):
                    z=mul(value,sq_gen(j,g))
                    if z:nxt[i+j]=xor(nxt.get(i+j,EMPTY),z)
            total=nxt
        out=xor(out,total.get(k,EMPTY))
    return out

def tmul(x,y):
    ans=set()
    for a,b in x:
        for c,d in y:
            ans.symmetric_difference_update({(tuple(sorted(a+c)),tuple(sorted(b+d)))})
    return frozenset(ans)

def tbracket(x,y):
    out=set()
    for a,b in x:
        for c,d in y:
            for left in bracket(frozenset({a}),frozenset({c})):
                out.symmetric_difference_update({(left,tuple(sorted(b+d)))})
            for right in bracket(frozenset({b}),frozenset({d})):
                out.symmetric_difference_update({(tuple(sorted(a+c)),right)})
    return frozenset(out)

def txi(x):
    out=set();previous=frozenset()
    for a,b in sorted(x):
        ap,bp=frozenset({a}),frozenset({b})
        term=frozenset({(a,b)})
        for u in xi(ap):
            for v in power(bp,2):out.symmetric_difference_update({(u,v)})
        for u in power(ap,2):
            for v in xi(bp):out.symmetric_difference_update({(u,v)})
        out.symmetric_difference_update(tbracket(previous,term))
        previous=xor(previous,term)
    return frozenset(out)

@lru_cache(None)
def delta_gen(g):
    w,r=GENS[g]
    if r:return txi(delta_gen(GID[(w,r-1)]))
    if len(w)>1:
        a,b=split(w)
        return tbracket(delta_gen(GID[(a,0)]),delta_gen(GID[(b,0)]))
    e=LABELS[w[0]];ans=set()
    for left in product(*(range(n+1) for n in e)):
        right=tuple(n-m for n,m in zip(e,left))
        a=() if left==ZERO else (LABELGEN[left],)
        b=() if right==ZERO else (LABELGEN[right],)
        ans.add((a,b))
    return frozenset(ans)

@lru_cache(None)
def delta(x):
    ans=frozenset()
    for m in x:
        term=frozenset({((),())})
        for g in m:term=tmul(term,delta_gen(g))
        ans=xor(ans,term)
    return ans

@lru_cache(None)
def antipode_label(e):
    if e==ZERO:return ONE
    ans=label(e)
    for l in product(*(range(n+1) for n in e)):
        r=tuple(n-m for n,m in zip(e,l))
        if l==ZERO or r==ZERO:continue
        ans=xor(ans,mul(label(l),antipode_label(r)))
    return ans

@lru_cache(None)
def q_monomial(m):
    total=ZERO
    for g in m:
        w,r=GENS[g]
        if r or len(w)!=1:return None
        e=LABELS[w[0]]
        if any(a&b for a,b in zip(total,e)):return None
        total=tuple(a+b for a,b in zip(total,e))
    return total

@lru_cache(None)
def retract(x):
    ans=EMPTY
    for a,b in delta(x):
        qb=q_monomial(b)
        if qb is not None:ans=xor(ans,mul(frozenset({a}),antipode_label(qb)))
    return ans

def monomials(n,start=0):
    if n==0:
        yield ()
        return
    for g in range(start,len(GENS)):
        if GD[g]>n:break
        for rest in monomials(n-GD[g],g):yield (g,)+rest

TBAS={n:list(monomials(n)) for n in range(MAX+1)}
TINDEX={n:{m:i for i,m in enumerate(v)} for n,v in TBAS.items()}

def vector(x,n):
    ans=0
    for m in x:ans^=1<<TINDEX[n][m]
    return ans

def poly(v,n):
    return frozenset(TBAS[n][i] for i in range(len(TBAS[n])) if v>>i&1)

class Span:
    def __init__(self):self.pivots={};self.vectors=[]
    def reduce(self,v):
        c=0
        while v:
            k=v.bit_length()-1
            if k not in self.pivots:return v,c
            w,d=self.pivots[k];v^=w;c^=d
        return 0,c
    def add(self,v):
        r,c=self.reduce(v)
        if not r:return False
        idx=len(self.vectors);self.vectors.append(v)
        self.pivots[r.bit_length()-1]=(r,c^(1<<idx))
        return True
    def coords(self,v):
        r,c=self.reduce(v)
        assert not r,('outside span',r)
        return c

FSPACE={}
for n in range(MAX+1):
    sp=Span()
    for m in TBAS[n]:sp.add(vector(retract(frozenset({m})),n))
    FSPACE[n]=sp

BASEOPS=[(),(1,),(2,),(3,),(2,1),(3,1),(4,1),(4,2),
         (5,2),(4,2,1),(5,2,1)]

a=named('u');b=named('v');c=named('u2');d=named('w');e=named('uv')
u=xi(a);k=bracket(a,b);R=bracket(a,c)
A=power(a,2)
p3=xor(named('u3'),mul(a,c),power(a,3))
P=xor(named('u2v'),mul(a,e),mul(b,c),mul(power(a,2),b))
Q=xor(named('uw'),mul(a,d))
D=k;E6=xor(power(b,2),p3);S=xor(xi(b),P,Q)

@lru_cache(None)
def base_function(I,m):
    x=frozenset({m})
    for j in I:x=sq(j,x)
    x=retract(x)
    return int(next(iter(A)) in x)

ESPACE={}
for n in range(MAX+1):
    basis=FSPACE[n].vectors
    relation_span=Span();kernel=[]
    # The output blocks are contractions by each polynomial base generator.
    offsets=[];total=0
    for I in BASEOPS:
        deg=4+sum(I)
        if deg<=n:
            offsets.append((I,n-deg,total))
            total+=len(TBAS[n-deg])
    for j,v in enumerate(basis):
        out=0
        diagonal=delta(poly(v,n))
        for I,rd,off in offsets:
            leftdeg=n-rd
            contracted=EMPTY
            for l,r in diagonal:
                if sum(GD[g] for g in l)==leftdeg and base_function(I,l):
                    contracted=xor(contracted,frozenset({r}))
            out^=vector(contracted,rd)<<off
        rem,comb=relation_span.reduce(out)
        if rem:
            # Span's generator index must remain the original column index.
            relation_span.pivots[rem.bit_length()-1]=(rem,comb^(1<<j))
        else:
            kernel.append(comb^(1<<j))
    sp=Span()
    for v in kernel:
        ambient=0
        for j,w in enumerate(basis):
            if v>>j&1:ambient^=w
        sp.add(ambient)
    ESPACE[n]=sp

KERNEL={10:[power(u,2)],11:[mul(u,D),mul(u,E6),xi(u)],
        12:[mul(u,S),mul(u,R),power(D,2),mul(D,E6),power(E6,2),
            bracket(u,D),bracket(u,E6)]}

LSPACE={};LIDS={};LBAS={}
for n in range(5,MAX+1):
    combined=Span()
    for x in KERNEL.get(n,[]):
        v=vector(x,n);ESPACE[n].coords(v)
        assert combined.add(v)
    nk=len(combined.vectors)
    selected=[]
    for v in ESPACE[n].vectors:
        if combined.add(v):selected.append(v)
    LSPACE[n]=(combined,nk)
    LBAS[n]=selected
    LIDS[n]=[('a7' if n==5 else f'L{n+2}_{i+1:02d}') for i in range(len(selected))]

def gname(g):
    w,r=GENS[g]
    if len(w)==1:s='['+bpoly.LABEL[LABELS[w[0]]]+']'
    else:
        l,v=split(w)
        s='{'+gname(GID[(l,0)])+','+gname(GID[(v,0)])+'}'
    for _ in range(r):s='xi('+s+')'
    return s

def show(x):
    return ' + '.join('*'.join(gname(g) for g in m) or '1' for m in sorted(x)) or '0'

def binom2(n,k):
    return int(n>=0 and k>=0 and (k&~n)==0)

def verify():
    # Independent prior dimension counts, including all actual cover images.
    assert [len(TBAS[n]) for n in range(13)]==[1,0,1,1,2,4,6,9,16,26,42,69,112]
    assert [len(FSPACE[n].vectors) for n in range(13)]==[1,0,0,0,1,2,3,4,7,11,18,30,49]
    assert [len(ESPACE[n].vectors) for n in range(13)]==[1,0,0,0,0,1,2,2,5,8,12,20,32]
    assert [len(LBAS[n]) for n in range(5,13)]==[1,2,2,5,8,11,17,25]
    checks=0
    for n in range(1,MAX+1):
        for m in TBAS[n]:
            x=frozenset({m})
            diagonal=delta(x)
            lco=set();rco=set()
            for left,right in diagonal:
                for aa,bb in delta(frozenset({left})):
                    lco.symmetric_difference_update({(aa,bb,right)})
                for aa,bb in delta(frozenset({right})):
                    rco.symmetric_difference_update({(left,aa,bb)})
            assert lco==rco,('coproduct not coassociative',n,show(x))
            assert retract(retract(x))==retract(x)
            for i in range(1,min(8,n)+1):
                assert sq(i,retract(x))==retract(sq(i,x))
                rhs=set()
                for left,right in diagonal:
                    for j in range(i+1):
                        for aa in sq(j,frozenset({left})):
                            for bb in sq(i-j,frozenset({right})):
                                rhs.symmetric_difference_update({(aa,bb)})
                assert delta(sq(i,x))==rhs,('Sq coproduct incompatibility',n,i,show(x))
            for i in range(1,min(8,n)+1):
                for j in range(1,min(8,n-i)+1):
                    if i>=2*j:continue
                    lhs=sq(j,sq(i,x))
                    rhs=xor(*(sq(t,sq(i+j-t,x)) for t in range(i//2+1)
                              if binom2(j-t-1,i-2*t)))
                    assert lhs==rhs,('Adem',n,show(x),i,j,show(lhs),show(rhs))
                    checks+=1
    # The seven geometric bar-kernel generators form an A-submodule in range.
    for n,vs in KERNEL.items():
        for x in vs:
            for i in range(1,n-4):
                z=sq(i,x)
                if not z:continue
                sp,nk=LSPACE[n-i]
                cc=sp.coords(vector(z,n-i))
                assert cc>>nk==0,('bar kernel not stable',n,i,show(x),show(z))
    return checks

def main():
    checks=verify()
    classes=[];operations={str(i):{} for i in (1,2,4)}
    for n in range(5,13):
        for id,v in zip(LIDS[n],LBAS[n]):
            x=poly(v,n)
            classes.append({'id':id,'degree':n+2,'E_representative':show(x)})
            for i in (1,2,4):
                if n-i<5:continue
                y=sq(i,x)
                ESPACE[n-i].coords(vector(y,n-i))
                sp,nk=LSPACE[n-i]
                cc=sp.coords(vector(y,n-i))>>nk
                out=[w for j,w in enumerate(LIDS[n-i]) if cc>>j&1]
                if out:operations[str(i)][id]=out
    report={'status':'PASS','bottom':'a7','internal_degree':16,
            'classes':classes,'operations':operations,'Adem_checks':checks,
            'dimensions':{str(n+2):len(LBAS[n]) for n in range(5,13)},
            'scope':'Actual homology Sq_* matrices on L through14 via D56 edge and two bar quotients; no Adams result inferred.'}
    dest=Path(__file__).parent/'outputs'/'I_L14_primary.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'PASS','classes':len(classes),'Adem_checks':checks,'output':str(dest)}))

if __name__=='__main__':main()
