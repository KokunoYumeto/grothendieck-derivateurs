"""Finite-category checks used in RESIDUE Part D. Standard library only.
Arrows are immutable labels; comp(g,f) means g after f.
"""
from itertools import product
from collections import defaultdict, deque
class Category:
 def __init__(self,objects,arrows,src,dst,ident,comp,name=''):
  self.objects=tuple(objects); self.arrows=tuple(arrows); self.src=src; self.dst=dst
  self.ident=ident; self.comp=comp; self.name=name
  self.hom=defaultdict(list)
  for a in self.arrows:self.hom[src[a],dst[a]].append(a)
 def check(self):
  for a in self.arrows:
   assert self.comp(self.ident[self.dst[a]],a)==a
   assert self.comp(a,self.ident[self.src[a]])==a
  n=0
  for f in self.arrows:
   for g in self.arrows:
    if self.dst[f]!=self.src[g]:continue
    gf=self.comp(g,f)
    assert gf in self.arrows and self.src[gf]==self.src[f] and self.dst[gf]==self.dst[g]
    for h in self.arrows:
     if self.dst[g]!=self.src[h]:continue
     assert self.comp(h,gf)==self.comp(self.comp(h,g),f)
     n+=1
  return {'objects':len(self.objects),'arrows':len(self.arrows),'associative_triples':n}
 def sub(self,objects,arrows=None):
  o=set(objects); a=[f for f in self.arrows if self.src[f] in o and self.dst[f] in o and (arrows is None or f in arrows)]
  return Category(o,a,{f:self.src[f] for f in a},{f:self.dst[f] for f in a},{x:self.ident[x] for x in o},self.comp)
 def components(self):
  ds={x:x for x in self.objects}
  def root(x):
   while ds[x]!=x:x=ds[x]
   return x
  for f in self.arrows:ds[root(self.src[f])]=root(self.dst[f])
  parts=defaultdict(list)
  for x in self.objects:parts[root(x)].append(x)
  return list(parts.values())
 def terminal_objects(self):return [x for x in self.objects if all(len(self.hom[y,x])==1 for y in self.objects)]
 def initial_objects(self):return [x for x in self.objects if all(len(self.hom[x,y])==1 for y in self.objects)]

def poset(n,leq,name=''):
 obs=range(n); ar=[(i,j) for i in obs for j in obs if leq(i,j)]
 return Category(obs,ar,{a:a[0] for a in ar},{a:a[1] for a in ar},{i:(i,i) for i in obs},lambda g,f:(f[0],g[1]),name)

def group_cat(p):
 a=list(range(p));return Category([0],a,{x:0 for x in a},{x:0 for x in a},{0:0},lambda g,f:(f+g)%p,'BC'+str(p))

def twisted(K,dim=1):
 V=list(product(range(2),repeat=dim));zero=(0,)*dim
 A=[(f,v) for f in K.arrows for v in V]
 def coc(f,g):return int(f[0]==1 and f[1]==3 and g[1]==7 and f[0]!=f[1] and g[0]!=g[1])
 def compose(g,f):
  c=coc(f[0],g[0]);return (K.comp(g[0],f[0]),tuple((x+y+c)%2 for x,y in zip(f[1],g[1])))
 return Category(K.objects,A,{a:K.src[a[0]] for a in A},{a:K.dst[a[0]] for a in A},{x:(K.ident[x],zero) for x in K.objects},compose,'twist'+str(dim))

def cat_pullback(E,B,X,eo,ea,xo,xa):
 ob=[(e,x) for e in E.objects for x in X.objects if eo(e)==xo(x)]
 ar=[(f,g) for f in E.arrows for g in X.arrows if ea(f)==xa(g)]
 return Category(ob,ar,{a:(E.src[a[0]],X.src[a[1]]) for a in ar},{a:(E.dst[a[0]],X.dst[a[1]]) for a in ar},{x:(E.ident[x[0]],X.ident[x[1]]) for x in ob},lambda h,g:(E.comp(h[0],g[0]),X.comp(h[1],g[1])))

def lift_category(E,B,po,pa,e,beta,incoming):
 # Objects are lifts with prescribed target (incoming) or source (outgoing).
 ob=[f for f in E.arrows if pa(f)==beta and (E.dst[f]==e if incoming else E.src[f]==e)]
 arr=[]
 for f,g in product(ob,repeat=2):
  if incoming:
   for h in E.hom[E.src[f],E.src[g]]:
    if pa(h)==B.ident[B.src[beta]] and E.comp(g,h)==f:arr.append((f,g,h))
  else:
   for h in E.hom[E.dst[f],E.dst[g]]:
    if pa(h)==B.ident[B.dst[beta]] and E.comp(h,f)==g:arr.append((f,g,h))
 return Category(ob,arr,{a:a[0] for a in arr},{a:a[1] for a in arr},{f:(f,f,E.ident[E.src[f] if incoming else E.dst[f]]) for f in ob},lambda b,a:(a[0],b[1],E.comp(b[2],a[2])))

def free_reduce(w):
 a=[]
 for s in w:
  if a and a[-1]==-s:a.pop()
  else:a.append(s)
 return a

def inverse(w):return [-x for x in w[::-1]]

def pi1_presentation(C):
 if len(C.components())!=1:return {'components':len(C.components())}
 if not C.objects:return {'components':0}
 # Choose an undirected maximal tree in the non-loop arrow graph.
 seen={C.objects[0]}; tree=set()
 while len(seen)<len(C.objects):
  for f in C.arrows:
   s,t=C.src[f],C.dst[f]
   if (s in seen)!=(t in seen):tree.add(f);seen|={s,t};break
  else:raise AssertionError('disconnected')
 nonids=[f for f in C.arrows if f!=C.ident[C.src[f]] and f not in tree]
 gens={f:i+1 for i,f in enumerate(nonids)}
 def word(f):return [] if f not in gens else [gens[f]]
 rel=[]
 for f,g in product(C.arrows,repeat=2):
  if C.dst[f]==C.src[g]:
   w=free_reduce(word(f)+word(g)+inverse(word(C.comp(g,f))))
   if w:rel.append(w)
 original=(len(gens),len(rel))
 remaining=set(gens.values())
 while True:
  chosen=None
  for w in sorted(rel,key=len):
   counts={abs(x):sum(abs(y)==abs(x) for y in w) for x in w}
   once=next((x for x in w if counts[abs(x)]==1),None)
   if once is not None:chosen=(w,once);break
  if chosen is None:break
  w,g=chosen;i=w.index(g);left=w[:i];right=w[i+1:]
  repl=inverse(left)+inverse(right)
  if g<0:repl=inverse(repl)
  k=abs(g);new=[]
  for r in rel:
   a=[]
   for x in r:a.extend(repl if x==k else inverse(repl) if x==-k else [x])
   a=free_reduce(a)
   if a:new.append(a)
  rel=new;remaining.discard(k)
 rel=sorted(set(tuple(r) for r in rel))
 if not remaining:kind='trivial'
 elif len(remaining)==1:
  g=next(iter(remaining));from math import gcd
  d=0
  for r in rel:d=gcd(d,abs(sum(1 if x==g else -1 for x in r)))
  kind='Z' if d==0 else 'C'+str(d)
 else:kind='presentation'
 return {'initial_generators':original[0],'initial_relations':original[1],'remaining_generators':sorted(remaining),'remaining_relations':rel,'identified_group':kind}
