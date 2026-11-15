"""Finite category checks used in Part D. Python 3, no external packages.
All group-presentation eliminations below are explicit Tietze moves.
"""
from itertools import combinations
from collections import Counter
import json

class Category:
    def __init__(self, objects, arrows, src, tgt, identity, composition, name):
        self.objects=list(objects); self.arrows=list(arrows)
        self.src=src;self.tgt=tgt;self.identity=identity
        self.composition=composition;self.name=name
    def comp(self,g,f):
        assert self.tgt[f]==self.src[g]
        return self.composition[(g,f)]
    def verify(self):
        for x in self.objects:
            a=self.identity[x]
            assert self.src[a]==self.tgt[a]==x
        composable=0; triples=0
        for f in self.arrows:
            assert self.comp(f,self.identity[self.src[f]])==f
            assert self.comp(self.identity[self.tgt[f]],f)==f
            for g in self.arrows:
                if self.tgt[f]!=self.src[g]:continue
                composable+=1
                gf=self.comp(g,f)
                assert self.src[gf]==self.src[f] and self.tgt[gf]==self.tgt[g]
                for h in self.arrows:
                    if self.tgt[g]!=self.src[h]:continue
                    triples+=1
                    assert self.comp(h,gf)==self.comp(self.comp(h,g),f)
        return dict(name=self.name,objects=len(self.objects),arrows=len(self.arrows),composable_pairs=composable,associative_triples=triples)
    def restrict(self,objects,name):
        obj=set(objects);ars=[a for a in self.arrows if self.src[a] in obj and self.tgt[a] in obj]
        return Category(objects,ars,{a:self.src[a] for a in ars},{a:self.tgt[a] for a in ars},{x:self.identity[x] for x in obj},{(g,f):h for (g,f),h in self.composition.items() if g in ars and f in ars},name)
    def components(self):
        par={x:x for x in self.objects}
        def root(x):
            while par[x]!=x:x=par[x]
            return x
        for a in self.arrows:
            u,v=root(self.src[a]),root(self.tgt[a]);par[u]=v
        return len({root(x) for x in self.objects})

def cat(objects, arrows,src,tgt,ident,compose,name):
    composition={(g,f):compose(g,f) for g in arrows for f in arrows if tgt[f]==src[g]}
    return Category(objects,arrows,src,tgt,ident,composition,name)

def reduce_word(w):
    r=[]
    for t in w:
        if r and r[-1]==-t:r.pop()
        else:r.append(t)
    while len(r)>1 and r[0]==-r[-1]:r=r[1:-1]
    return tuple(r)

def inverse(w):return tuple(-t for t in reversed(w))

def fundamental_presentation(C):
    # Collapse a spanning forest of the unoriented 1-skeleton.
    par={x:x for x in C.objects}
    def root(x):
        while par[x]!=x:x=par[x]
        return x
    tree=set()
    for a in C.arrows:
        u,v=root(C.src[a]),root(C.tgt[a])
        if u!=v:tree.add(a);par[u]=v
    ids=set(C.identity.values());generators={a:i+1 for i,a in enumerate(a for a in C.arrows if a not in tree|ids)}
    def word(a):return () if a not in generators else (generators[a],)
    relations=set()
    for (g,f),h in C.composition.items():
        r=reduce_word(word(f)+word(g)+inverse(word(h)))
        if r:relations.add(r)
    initial_gens=len(generators); initial_rels=len(relations); eliminated=[]
    while True:
        choice=None
        for r in sorted(relations,key=lambda r:(len(r),r)):
            counts=Counter(abs(t) for t in r)
            for j,t in enumerate(r):
                if counts[abs(t)]==1:
                    # cyclic rotate to t w=1; solve t=w^{-1}.
                    w=r[j+1:]+r[:j]
                    value=inverse(w) if t>0 else w
                    choice=abs(t),value,r;break
            if choice:break
        if not choice:break
        g,val,r0=choice
        new=set()
        for r in relations:
            rr=[]
            for t in r:
                rr.extend(val if t==g else inverse(val) if t==-g else (t,))
            rr=reduce_word(rr)
            if rr:new.add(rr)
        relations=new;eliminated.append(g)
    surviving=set(generators.values())-set(eliminated)
    return dict(initial_generators=initial_gens,initial_relations=initial_rels,Tietze_eliminations=len(eliminated),remaining_generators=sorted(surviving),remaining_relations=sorted(relations))

# Sphere poset and nonzero normalized cocycle.
V=range(4)
Bobj=[frozenset(s) for k in (1,2,3) for s in combinations(V,k)]
Bars=[(x,y) for x in Bobj for y in Bobj if x<=y]
B=cat(Bobj,Bars,{a:a[0] for a in Bars},{a:a[1] for a in Bars},{x:(x,x) for x in Bobj},lambda g,f:(f[0],g[1]),'B = nonempty proper subsets of {0,1,2,3}')
sigma=(frozenset([0]),frozenset([0,1]),frozenset([0,1,2]))
def cocycle(x,y,z):return int((x,y,z)==sigma)
cochain_checks=0
for x in Bobj:
 for y in Bobj:
  for z in Bobj:
   for w in Bobj:
    if x<=y<=z<=w:
     cochain_checks+=1
     assert (cocycle(y,z,w)-cocycle(x,z,w)+cocycle(x,y,w)-cocycle(x,y,z))%2==0
Ears=[(x,y,n) for x,y in Bars for n in (0,1)]
E=cat(Bobj,Ears,{a:a[0] for a in Ears},{a:a[1] for a in Ears},{x:(x,x,0) for x in Bobj},lambda g,f:(f[0],g[1],(f[2]+g[2]+cocycle(f[0],f[1],g[1]))%2),'E_c')
# Add object a below b0 and its upper cone.
a='a'; b0=frozenset([0]);Yobj=[a]+Bobj
Yars=Bars+[(a,a)]+[(a,b) for b in Bobj if b0<=b]
Y=cat(Yobj,Yars,{u:u[0] for u in Yars},{u:u[1] for u in Yars},{x:(x,x) for x in Yobj},lambda g,f:(f[0],g[1]),'Y')
def r(x):return b0 if x==a else x
Xars=[(x,y,n) for x,y in Yars for n in (0,1)]
X=cat(Yobj,Xars,{u:u[0] for u in Xars},{u:u[1] for u in Xars},{x:(x,x,0) for x in Yobj},lambda g,f:(f[0],g[1],(f[2]+g[2]+cocycle(r(f[0]),r(f[1]),r(g[1])))%2),'X = Y x_B E_c')
# Check each p:X->Y arrow has a unique lift with each prescribed source,
# followed by each prescribed factorization: opcartesian / cartesian labels.
for base in Yars:
 for lift in [t for t in Xars if t[:2]==base]:
  for v in Xars:
   if X.src[v]==X.src[lift] and (X.tgt[lift],X.tgt[v]) in Yars:
    matches=[h for h in Xars if X.src[h]==X.tgt[lift] and X.tgt[h]==X.tgt[v] and X.comp(h,lift)==v]
    assert len(matches)==1

# Rational ms118 example.
O=['a','b']; A=[('a','a',0)]+[(x,'b',n) for x in O for n in (0,1)]
R=cat(O,A,{u:u[0] for u in A},{u:u[1] for u in A},{x:(x,x,0) for x in O},lambda g,f:(f[0],g[1],(f[2]+g[2])%2),'rational Y')
RO=[(x,z) for x in O for z in (0,1)]
RA=[(u,z) for u in A for z in (0,1)]
RX=cat(RO,RA,{v:(v[0][0],v[1]) for v in RA},{v:(v[0][1],(v[1]+v[0][2])%2) for v in RA},{x:((x[0],x[0],0),x[1]) for x in RO},lambda g,f:(R.comp(g[0],f[0]),f[1]),'rational X')
R0=RX.restrict([('a',0),('a',1)],'rational fibre 0')
R1=RX.restrict([('b',0),('b',1)],'rational fibre 1')

out={'categories':[C.verify() for C in [B,E,Y,X,R,RX,R0,R1]],'normalized_cocycle_quadruples_checked':cochain_checks,'sphere_f_vector':[14,36,24],'cocycle_evaluation_on_mod2_fundamental_cycle':1,'fundamental_presentations':{C.name:fundamental_presentation(C) for C in [B,E,Y,X,X.restrict(['a'],'X_0 = BC2')]},'rational_fibre_components':[R0.components(),R1.components()]}
assert not out['fundamental_presentations']['E_c']['remaining_generators']
assert not out['fundamental_presentations']['X = Y x_B E_c']['remaining_generators']
assert out['rational_fibre_components']==[2,1]
if __name__ == "__main__":
 print(json.dumps(out,indent=2))
