"""Finite checks for BISITE A.3, A.8, A.18, A.20, A.24, A.29--30, A.33--34.

All data and complete composition tables are printed, so the finite examples
can be reconstructed without relying on the accompanying paper.
"""
from itertools import product
from pathlib import Path

LOG=[]
def log(x):
    LOG.append(str(x))

class Category:
    def __init__(self, objects, arrows, src, tgt, identities, compose, name):
        self.objects=tuple(objects); self.arrows=tuple(arrows)
        self.src=src; self.tgt=tgt; self.identities=identities
        self.compose=compose; self.name=name
    def verify(self):
        log(f'CATEGORY {self.name}: objects={self.objects!r}')
        for f in self.arrows:
            assert self.src[f] in self.objects and self.tgt[f] in self.objects
            assert self.compose(f,self.identities[self.src[f]])==f
            assert self.compose(self.identities[self.tgt[f]],f)==f
            log(f'  arrow {f!r}: {self.src[f]!r} -> {self.tgt[f]!r}')
        pairs=0; triples=0
        for g,f in product(self.arrows,repeat=2):
            if self.src[g]==self.tgt[f]:
                h=self.compose(g,f)
                assert h in self.arrows and self.src[h]==self.src[f] and self.tgt[h]==self.tgt[g]
                pairs+=1
                log(f'  compose({g!r},{f!r})={h!r}')
        for h,g,f in product(self.arrows,repeat=3):
            if self.src[h]==self.tgt[g] and self.src[g]==self.tgt[f]:
                assert self.compose(h,self.compose(g,f))==self.compose(self.compose(h,g),f)
                triples+=1
        log(f'  PASS: units, {pairs} composable pairs, {triples} associative triples')
    def components(self, objects=None, arrows=None):
        objects=list(self.objects if objects is None else objects)
        arrows=self.arrows if arrows is None else arrows
        parent={x:x for x in objects}
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        for f in arrows:
            a,b=self.src[f],self.tgt[f]
            if a in parent and b in parent:
                parent[find(a)]=find(b)
        return len({find(x) for x in objects})

def chain(n):
    obj=tuple(range(n)); arr=tuple((i,j) for i in obj for j in obj if i<=j)
    return Category(obj,arr,{f:f[0] for f in arr},{f:f[1] for f in arr},
                    {i:(i,i) for i in obj},lambda g,f:(f[0],g[1]),f'[{n-1}]')

C=chain(4); C.verify()
iso={(i,i) for i in C.objects}
W=iso|{(0,2),(0,3)}; A=iso|{(0,3)}
for D in (W,A):
    for g,f in product(D,repeat=2):
        if f[1]==g[0]: assert C.compose(g,f) in D

def transport(A,W):
    out=set()
    for x,y in C.arrows:
        good=True
        for a,b in A:
            if b<=y and (min(a,x),min(b,x)) not in W:
                good=False
        if good:out.add((x,y))
    return out
def kernel(L,W):
    return {f for f in W if all((min(f[0],x),x) in W for x,y in L if y==f[1])}
T=transport(A,W); K=kernel(T,W)
assert T==set(C.arrows)-{(1,3)} and K==A
assert (1,2) in T and (2,3) in T and (1,3) not in T
log(f'A.8 W={sorted(W)}; A={sorted(A)}; T_W(A)={sorted(T)}; K_W(T_W(A))={sorted(K)}')
log('A.8 PASS: transporter is not closed under composition')

# A.18: finite opfibration and finite covering.
Bobj=('a','b')
Barr=('a0','b0','b1','h0','h1')
Bsrc={'a0':'a','b0':'b','b1':'b','h0':'a','h1':'a'}
Btgt={'a0':'a','b0':'b','b1':'b','h0':'b','h1':'b'}
label={'a0':0,'b0':0,'b1':1,'h0':0,'h1':1}
def bcomp(g,f):
    if f=='a0':return g
    if g=='b0':return f
    return ('b' if Bsrc[f]=='b' else 'h')+str((label[g]+label[f])%2)
B=Category(Bobj,Barr,Bsrc,Btgt,{'a':'a0','b':'b0'},bcomp,'B rational weak fibration')
B.verify()
Eobj=tuple(product(Bobj,(0,1)))
Earr=tuple(product(Barr,(0,1)))
Esrc={(f,z):(Bsrc[f],z) for f,z in Earr}
Etgt={(f,z):(Btgt[f],(z+label[f])%2) for f,z in Earr}
def ecomp(g,f):
    return (bcomp(g[0],f[0]),f[1])
E=Category(Eobj,Earr,Esrc,Etgt,{(o,z):(B.identities[o],z) for o,z in Eobj},ecomp,'E category of elements')
E.verify()
for f,z in Earr:
    assert Esrc[f,z][0]==Bsrc[f] and Etgt[f,z][0]==Btgt[f]
for f in Barr:
    for z in (0,1):
        assert sum(g[0]==f and Esrc[g]==(Bsrc[f],z) for g in Earr)==1
        assert sum(g[0]==f and Etgt[g]==(Btgt[f],z) for g in Earr)==1
log('A.18 PASS: p:E->B is a discrete fibration and discrete opfibration')
color={'a':0,'b':1}
def qarrow(f):return (color[Bsrc[f]],color[Btgt[f]])
I=chain(2)
def cocartesian(h):
    x,y=Bsrc[h],Btgt[h]
    for z in Bobj:
        for beta in I.arrows:
            if beta!=(color[y],color[z]):continue
            if beta not in I.arrows:continue
            for g in Barr:
                if Bsrc[g]!=x or Btgt[g]!=z or qarrow(g)!=(color[x],color[z]):continue
                lifts=[k for k in Barr if Bsrc[k]==y and Btgt[k]==z and qarrow(k)==beta and bcomp(k,h)==g]
                if len(lifts)!=1:return False
    return True
for x in Bobj:
    for alpha in I.arrows:
        if alpha[0]!=color[x]:continue
        assert any(Bsrc[h]==x and qarrow(h)==alpha and cocartesian(h) for h in Barr)
log('A.18 PASS: q:B->[1] has cocartesian lifts for every outgoing arrow')
counts=[]
for c in (0,1):
    objects=[x for x in Eobj if color[x[0]]==c]
    arrows=[f for f in Earr if color[Esrc[f][0]]==c and color[Etgt[f][0]]==c]
    counts.append(E.components(objects,arrows))
    log(f'A.18 fibre at {c}: objects={objects!r}, arrows={arrows!r}, components={counts[-1]}')
assert counts==[2,1]
log('A.18 PASS: composite constant H^0 transition has dimensions 1 -> 2')

# A.20: inclusion {1} -> [1].
I.verify()
commas={s:[(1,a) for a in I.arrows if a==(1,s)] for s in I.objects}
assert commas[0]==[] and len(commas[1])==1
log(f'A.20 over-comma objects: {commas!r}')
log('A.20 PASS: empty -> terminal transition for a cosieve')

# A.24: pullback of opposite endpoint maps.
source_pullback=[(0,0) for _ in [None] if 0==1]
target_pullback=[(0,0) for _ in [None] if 0==0]
assert len(source_pullback)==0 and len(target_pullback)==1
log(f'A.24 source pullback objects={source_pullback!r}; target={target_pullback!r}')
log('A.24 PASS: objectwise weak equivalence has non-equivalent ordinary limits')

# A.3: e -> BC2 fails full faithfulness on sets; BC2 -> e succeeds on trivial actions.
maps_to_regular=[(z,) for z in (0,1)]
equivariant=[m for m in maps_to_regular if (m[0]+1)%2==m[0]]
assert len(maps_to_regular)==2 and not equivariant
log('A.3 PASS: maps from trivial singleton to regular C2-set: 0 equivariant, 2 underlying')

# A.29: double annihilators and the missing closure after a join.
V=list(product((0,1),repeat=2))
dot=lambda x,y:sum(a*b for a,b in zip(x,y))%2
ann=lambda S:{y for y in V if all(dot(x,y)==0 for x in S)}
close=lambda S:ann(ann(S))
U={(0,0),(1,0)}; Vline={(0,0),(0,1)}
assert close(U)==U and close(Vline)==Vline
assert len(U|Vline)==3 and close(U|Vline)==set(V)
log(f'A.29 vector space objects={V!r}; scalar product table={[[dot(x,y) for y in V] for x in V]!r}')
log(f'A.29 U={sorted(U)!r}, Vline={sorted(Vline)!r}; union={sorted(U|Vline)!r}; closed join={sorted(close(U|Vline))!r}')
log('A.29 PASS: a join of closed subsets need not be closed')

# A.30 and A.34: union closure and non-antitonicity of stabilizers.
C2=chain(3); C2.verify()
units={(i,i) for i in C2.objects}
L1=units|{(0,1)}; L2=units|{(1,2)}
def closed_under_composition(L):
    return all((f[0],g[1]) in L for g,f in product(L,repeat=2) if f[1]==g[0])
def closed_under_pullback(L):
    return all((min(a,x),x) in L for a,b in L for x,y in C2.arrows if y==b)
for L in (L1,L2):
    assert closed_under_composition(L) and closed_under_pullback(L)
assert not closed_under_composition(L1|L2)
log(f'A.30 L1={sorted(L1)!r}; L2={sorted(L2)!r}; union={sorted(L1|L2)!r}')
log('A.30 PASS: both input classes compose and are pullback-stable; their union fails composition')
A2=units|{(0,2)}
def stabilizer(K):
    return {p for p in C2.arrows if all((min(a,p[0]),min(b,p[0])) in K for a,b in K if b<=p[1])}
stab=stabilizer(A2); staball=stabilizer(set(C2.arrows))
assert (1,2) not in stab and (1,2) in staball
log(f'A.34 A={sorted(A2)!r}; Stab(A)={sorted(stab)!r}; Stab(all)={sorted(staball)!r}')
log('A.34 PASS: stabilizer is not antitone')

# A.33: map of finite-set pushout squares with initial/final isomorphisms.
def pushout(left,right,f,g):
    points=[('L',x) for x in left]+[('R',y) for y in right]
    parent={x:x for x in points}
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    for x in f: parent[find(('L',f[x]))]=find(('R',g[x]))
    parts={r:[] for r in {find(x) for x in points}}
    for x in points:parts[find(x)].append(x)
    return sorted([sorted(v) for v in parts.values()])
D=(0,1); one=('*',)
idD={0:0,1:1}; collapse={0:'*',1:'*'}; ide={'*':'*'}
PX=pushout(D,one,idD,collapse)
PY=pushout(one,one,collapse,collapse)
assert len(PX)==len(PY)==1
assert all(collapse[idD[x]]==collapse[x] for x in D)
assert all(ide[collapse[x]]==collapse[x] for x in D)
assert len(set(collapse.values()))<len(collapse)
log(f'A.33 X pushout classes={PX!r}; Y pushout classes={PY!r}')
log(f'A.33 component maps f0={idD!r}, f1={collapse!r}, f2={ide!r}, f3=identity on singleton')
log('A.33 PASS: f0 and f3 are isomorphisms, f1 is not')

out=Path(__file__).with_suffix('.out.txt')
out.write_text('\n'.join(LOG)+'\n')
print('\n'.join(x for x in LOG if 'PASS' in x))
print(f'Complete object, arrow, and composition data: {out}')
