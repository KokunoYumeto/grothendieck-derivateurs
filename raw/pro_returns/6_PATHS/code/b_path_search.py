"""Finite truncations of Grothendieck path categories for finite posets.
All homology is over F_2. Truncations are diagnostic, never evidence about an
unbounded colimit without a persistence proof. Category arrows retain their
type maps (parallel maps are NOT merged).
"""
from itertools import product, combinations_with_replacement, combinations
import argparse,json,time

def closure(n,edges):
 r={(i,i) for i in range(n)}|set(edges)
 for k in range(n):
  for i in range(n):
   for j in range(n):
    if (i,k) in r and (k,j) in r:r.add((i,j))
 return r

def type_maps(s,t):
 m,n=len(s),len(t)
 if m==0:return [tuple([0])] if n==0 else []
 out=[]
 for mid in combinations_with_replacement(range(n+1),m-1):
  f=(0,)+mid+(n,)
  if all(all(t[k]==s[i] for k in range(f[i],f[i+1])) for i in range(m)):
   out.append(f)
 return out

def path_category(n,rel,W,a,b,L,restricted):
 objects=[]
 for l in range(L+1):
  for s in product((1,-1),repeat=l):
   if l==0:
    if a==b:objects.append((s,(a,)))
    continue
   for mid in product(range(n),repeat=l-1):
    p=(a,)+mid+(b,)
    if all(((p[i],p[i+1]) in rel if s[i]==1 else (p[i+1],p[i]) in W) for i in range(l)):
     objects.append((s,p))
 cache={}; arrows=[]; outgoing=[[] for o in objects];incoming=[[] for o in objects]
 lookup={};allowed=W if restricted else rel
 for i,(s,p) in enumerate(objects):
  for j,(t,q) in enumerate(objects):
   fs=cache.setdefault((s,t),type_maps(s,t))
   for f in fs:
    if all((p[k],q[f[k]]) in allowed for k in range(len(p))):
     ix=len(arrows);arrows.append((i,j,f));lookup[i,j,f]=ix
     outgoing[i].append(ix);incoming[j].append(ix)
 return objects,arrows,outgoing,incoming,lookup

def h01(cat):
 objs,arr,outs,ins,lookup=cat
 parents=list(range(len(objs)))
 def root(i):
  while parents[i]!=i:
   parents[i]=parents[parents[i]];i=parents[i]
  return i
 idset=set();basis={};rank=0
 for e,(i,j,f) in enumerate(arr):
  if i==j and f==tuple(range(len(f))):idset.add(e);continue
  u,v=root(i),root(j)
  if u!=v:parents[u]=v
  else:basis[e]=len(basis)
 pivots={};two=0
 for mid in range(len(objs)):
  for e in ins[mid]:
   if e in idset:continue
   i,j,f=arr[e]
   for d in outs[mid]:
    if d in idset:continue
    j,k,g=arr[d]
    c=lookup[i,k,tuple(g[x] for x in f)]
    row=0
    for z in (e,d,c):
     if z in basis:row^=1<<basis[z]
    two+=1
    while row:
     p=row.bit_length()-1
     if p in pivots:row^=pivots[p]
     else:pivots[p]=row;break
 h0=len({root(i) for i in range(len(objs))})
 return {'objects':len(objs),'nonidentity_arrows':len(arr)-len(idset),'nondegenerate_2simplices':two,'h0_F2':h0,'h1_F2':len(basis)-len(pivots)}

def w_subcategories(n,rel):
 nonid=sorted((i,j) for i,j in rel if i!=j)
 for bits in product((False,True),repeat=len(nonid)):
  W={(i,i) for i in range(n)}|{x for x,b in zip(nonid,bits) if b}
  if closure(n,W)!=W:continue
  two3=all(sum([(i,j) in W,(j,k) in W,(i,k) in W])!=2 for i,j in rel for jj,k in rel if j==jj)
  yield W,two3

def run(L=3):
 models=[('chain2',2,[(0,1)]),('chain3',3,[(0,1),(1,2)]),('span',3,[(0,1),(0,2)]),('cospan',3,[(1,0),(2,0)]),('crown4',4,[(0,1),(0,3),(2,1),(2,3)])]
 count=0
 for name,n,edges in models:
  rel=closure(n,edges)
  for W,two3 in w_subcategories(n,rel):
   # Extremes and self-maps suffice as a bounded diagnostic, not exhaustive categories.
   for a,b in [(0,0),(0,n-1)]:
    z={'model':name,'W_nonid':sorted([e for e in W if e[0]!=e[1]]),'two_out_of_three':two3,'a':a,'b':b,'max_word_length':L}
    for restricted,key in [(True,'restricted'),(False,'full')]:
     z[key]=h01(path_category(n,rel,W,a,b,L,restricted))
    z['same_h0_h1']=all(z['restricted'][key]==z['full'][key] for key in ['h0_F2','h1_F2'])
    print(json.dumps(z),flush=True);count+=1
 print(json.dumps({'cases':count,'conclusion':'Finite truncations only. No assertion about unbounded nerves follows.'}),flush=True)
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--length',type=int,default=3)
 run(parser.parse_args().length)
