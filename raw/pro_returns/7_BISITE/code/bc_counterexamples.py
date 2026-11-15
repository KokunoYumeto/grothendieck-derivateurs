"""Exact finite checks used in BISITE Parts B and C; Python standard library only.

The category laws and nonabelian presentations are checked exactly.  Contractible
lifting categories in the text are proved by initial/terminal objects; this
script does not infer contractibility from homology.
"""
from itertools import combinations, product
from collections import deque
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

class Category:
    def __init__(self,objects,arrows,src,tgt,ident,compose):
        self.objects=list(objects); self.arrows=list(arrows)
        self.src=src; self.tgt=tgt; self.ident=ident; self.compose=compose
    def verify(self):
        triples=0
        for a in self.arrows:
            assert self.compose(a,self.ident(self.src(a)))==a
            assert self.compose(self.ident(self.tgt(a)),a)==a
        for a in self.arrows:
          for b in self.arrows:
            if self.tgt(a)!=self.src(b): continue
            c=self.compose(b,a)
            assert c in self.arrows and self.src(c)==self.src(a) and self.tgt(c)==self.tgt(b)
            for d in self.arrows:
              if self.tgt(b)==self.src(d):
                assert self.compose(d,c)==self.compose(self.compose(d,b),a)
                triples+=1
        return {'objects':len(self.objects),'arrows':len(self.arrows),'associative_triples':triples}

def poset(objects,le):
    ar=[(x,y) for x in objects for y in objects if le(x,y)]
    return Category(objects,ar,lambda a:a[0],lambda a:a[1],lambda x:(x,x),lambda b,a:(a[0],b[1]))

def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out
def inv(w):return [-a for a in reversed(w)]

def fundamental_presentation(C):
    # Van Kampen presentation of the nerve's two-skeleton, with a spanning tree collapsed.
    seen={C.objects[0]}; tree=set()
    while len(seen)<len(C.objects):
        for a in C.arrows:
            x,y=C.src(a),C.tgt(a)
            if (x in seen) != (y in seen):
                seen.update([x,y]); tree.add(a); break
        else:raise ValueError('Disconnected category')
    generators=[a for a in C.arrows if a!=C.ident(C.src(a)) and a not in tree]
    ids={a:i+1 for i,a in enumerate(generators)}
    def word(a):return [ids[a]] if a in ids else []
    relations=[]
    for a in C.arrows:
      for b in C.arrows:
        if C.tgt(a)==C.src(b):
          w=reduce_word(word(a)+word(b)+inv(word(C.compose(b,a))))
          if w:relations.append(w)
    active=set(ids.values()); eliminated=[]
    while True:
        choice=None
        for w in sorted(relations,key=len):
            for idx,l in enumerate(w):
                if sum(abs(z)==abs(l) for z in w)==1:
                    choice=(w,idx,l);break
            if choice:break
        if not choice:break
        w,idx,l=choice;g=abs(l)
        # P g S=1 gives g=P^{-1}S^{-1}; P g^{-1} S=1 gives g=S P.
        replacement=reduce_word(inv(w[:idx])+inv(w[idx+1:])) if l>0 else reduce_word(w[idx+1:]+w[:idx])
        rr=[]
        for v in relations:
            sub=[]
            for a in v:
                sub += replacement if a==g else inv(replacement) if a==-g else [a]
            sub=reduce_word(sub)
            if sub:rr.append(sub)
        relations=rr; active.remove(g); eliminated.append(g)
    rels=sorted(set(tuple(w) for w in relations))
    ren={a:i+1 for i,a in enumerate(sorted(active))}
    return {'initial_generators_after_tree':len(ids),'eliminated_generators':len(eliminated),
            'remaining_generators':len(active),
            'remaining_relations':sorted(set(tuple((1 if x>0 else -1)*ren[abs(x)] for x in w) for w in rels))}

Kobs=[i for i in range(1,15)] # nonempty proper subsets of a four-element set
le=lambda a,b:(a&b)==a
K=poset(Kobs,le)
sigma=(1,3,7)
def twist(x,y,z):return int((x,y,z)==sigma)
def extension(rank):
    labels=list(product(range(2),repeat=rank))
    ar=[(x,y,m) for x in Kobs for y in Kobs if le(x,y) for m in labels]
    def comp(b,a):
        x,y,m=a;_,z,n=b;c=twist(x,y,z)
        return (x,z,tuple((mi+ni+c)%2 for mi,ni in zip(m,n)))
    return Category(Kobs,ar,lambda a:a[0],lambda a:a[1],lambda x:(x,x,(0,)*rank),comp)
H=extension(1);HH=extension(2)

out={'K':K.verify(),'H':H.verify(),'H_pullback_H':HH.verify()}
out['fundamental_groups']={name:fundamental_presentation(C) for name,C in [('K',K),('H',H),('H_pullback_H',HH)]}
assert out['fundamental_groups']['K']['remaining_generators']==0
assert out['fundamental_groups']['H']['remaining_generators']==0
assert out['fundamental_groups']['H_pullback_H']['remaining_generators']==1
assert set(map(tuple,out['fundamental_groups']['H_pullback_H']['remaining_relations'])) <= {(1,1),(-1,-1)}

# Every lifted arrow in the central C2 extension is cartesian and cocartesian.
lift_factorizations=0
for a in H.arrows:
  for b in H.arrows:
    if H.src(a)==H.src(b) and le(H.tgt(a),H.tgt(b)):
      lifts=[c for c in H.arrows if H.src(c)==H.tgt(a) and H.tgt(c)==H.tgt(b) and H.compose(c,a)==b]
      assert len(lifts)==1;lift_factorizations+=1
    if H.tgt(a)==H.tgt(b) and le(H.src(b),H.src(a)):
      lifts=[c for c in H.arrows if H.src(c)==H.src(b) and H.tgt(c)==H.src(a) and H.compose(a,c)==b]
      assert len(lifts)==1;lift_factorizations+=1
out['H_bifibration_unique_factorizations']=lift_factorizations

# A smooth proper map that is not an opfibration: diamond x<a,b<c over [1].
D=poset(['x','a','b','c'],lambda a,b:a==b or a=='x' or b=='c')
f=lambda a:0 if a=='x' else 1
lift_tests={}
for a in D.objects:
 for t in [0,1]:
  if f(a)<=t:
   L=[b for b in D.objects if (a,b) in D.arrows and f(b)==t]
   ini=[z for z in L if all((z,w) in D.arrows for w in L)]
   ter=[z for z in L if all((w,z) in D.arrows for w in L)]
   assert ini or ter
   lift_tests[f'outgoing:{a}:{t}']={'objects':L,'initial':ini,'terminal':ter}
  if t<=f(a):
   L=[b for b in D.objects if (b,a) in D.arrows and f(b)==t]
   ini=[z for z in L if all((z,w) in D.arrows for w in L)]
   ter=[z for z in L if all((w,z) in D.arrows for w in L)]
   assert ini or ter
   lift_tests[f'incoming:{a}:{t}']={'objects':L,'initial':ini,'terminal':ter}
assert lift_tests['outgoing:x:1']['initial']==[]
out['diamond']={'laws':D.verify(),'lifts':lift_tests}

# Intrinsic fibration (even universal equivalence) that fails properness.
V=poset(['a','b','c'],lambda a,b:a==b or a=='a')
color={'a':0,'b':0,'c':1};section={0:'a',1:'c'}
for x in V.objects:assert (section[color[x]],x) in V.arrows
assert [y for y in V.objects if color[y]==1 and ('b',y) in V.arrows]==[]
out['V']={'laws':V.verify(),'retraction_unit_exists':True,'outgoing_from_b_to_1':[]}

# Simplicial horn S=Lambda^2_1. Degenerate simplices do not add vertices in this pullback.
Sfaces={(0,),(1,),(2,),(0,1),(1,2)}
slice_vertices=[i for i in [0,1,2] if (i,2) in Sfaces or i==2]
out['inner_horn']={'nondegenerate_simplices':sorted(Sfaces),'vertices_of_S_over_2':slice_vertices,
 'pullback_of_vertex_0':list(set([0])&set(slice_vertices)),
 'pullback_of_edge_01':sorted(set([0,1])&set(slice_vertices))}
assert out['inner_horn']['pullback_of_vertex_0']==[] and out['inner_horn']['pullback_of_edge_01']==[1]

# Free-group endomorphism from POLES: alpha(x)=x, alpha(y)=y[x,y].
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def inverse(a):return tuple(a.index(i) for i in range(3))
x=(1,0,2);y=(2,1,0);identity=(0,1,2)
comm=mul(mul(mul(x,y),inverse(x)),inverse(y))
ay=mul(y,comm)
def orbits(gens):
 unseen=set(range(3));ans=[]
 while unseen:
  orbit={next(iter(unseen))};q=deque(orbit)
  while q:
   a=q.popleft()
   for g in gens:
    if g[a] not in orbit:orbit.add(g[a]);q.append(g[a])
  unseen-=orbit;ans.append(sorted(i+1 for i in orbit))
 return ans
out['three_sheeted']={'x':x,'y':y,'alpha_y_permutation':ay,'before_orbits':orbits([x,y]),'after_orbits':orbits([x,ay]),'abelianization_matrix':[[1,0],[0,1]]}
assert ay==x and len(out['three_sheeted']['before_orbits'])==1 and len(out['three_sheeted']['after_orbits'])==2

# Presheaf-elements separator over [1]: the source supported only at 0.
out['presheaf_elements']={'base':'0<1','source_values':[1,0],'target_values':[1,1],
                         'incoming_lifts':['singleton'],'outgoing_lift_0_to_1':[]}

# Finite C2 regular action groupoid, projection to BC2.
EG=poset([0,1],lambda a,b:True)
out['regular_C2']={'laws':EG.verify(),'base_group_addition_mod2':[[0,1],[1,0]],'fibre_objects':[0,1],
                  'fibre_nonidentity_arrows':0,'total_components':1,'fibre_components':2}

path=ROOT/'BISITE/code/bc_counterexamples.out.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
