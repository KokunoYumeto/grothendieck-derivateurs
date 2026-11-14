#!/usr/bin/env python3
"""Exhaustive finite checks of C.15, G=BC2, for all words of length <=4.
The checks include the literal functors and both natural transformations,
not only the connected-component counts. No third-party package is needed.
"""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json
# Objects a,b,g. Six arrows: three identities, one extra g-automorphism,
# and the two cone arrows. Label is relevant only in Hom(g,g).
a,b,g=0,1,2
ARROWS=((a,a,0),(b,b,0),(g,g,0),(g,g,1),(a,g,0),(b,g,0))
def hom(x,y):return tuple(z for z in ARROWS if z[:2]==(x,y))
def ident(x):return(x,x,0)
def comp(v,u):
 assert u[1]==v[0]
 return(u[0],v[1],(u[2]^v[2]) if u[0]==g else 0)
def marked(u):return u[0]!=a or u==ident(a)
for u,v,w in product(ARROWS,repeat=3):
 if u[1]==v[0] and v[1]==w[0]:assert comp(w,comp(v,u))==comp(comp(w,v),u)
def paths(word):
 n=len(word)
 for mid in product(range(3),repeat=n-1):
  ob=(a,)+mid+(b,)
  hs=[]
  for i,sgn in enumerate(word):
   hh=hom(ob[i],ob[i+1]) if sgn=='+' else tuple(u for u in hom(ob[i+1],ob[i]) if marked(u))
   hs.append(hh)
  for ar in product(*hs):yield(ob,ar)
def is_nat(word,c,d,alpha):
 if alpha[0]!=ident(a) or alpha[-1]!=ident(b):return False
 if any(x not in hom(u,v) for x,u,v in zip(alpha,c[0],d[0])):return False
 for i,sgn in enumerate(word):
  lo,hi=(i,i+1) if sgn=='+' else (i+1,i)
  if comp(alpha[hi],c[1][i])!=comp(d[1][i],alpha[lo]):return False
 return True
def nats(word,c,d):
 hs=[hom(x,y) for x,y in zip(c[0],d[0])]
 for alpha in product(*hs):
  if is_nat(word,c,d,alpha):yield alpha
def kl(c):return c[0].index(g),c[0].index(b)
def transport(c,i,j):
 assert all(x==g for x in c[0][min(i,j):max(i,j)+1])
 ans=0
 for u in c[1][min(i,j):max(i,j)]:ans^=u[2]
 return ans
# E(alpha) is its component at k(c), transported in d back to k(d).
def E(c,d,alpha):
 kc,lc=kl(c);kd,ld=kl(d)
 assert kd<=kc and ld>=lc
 return alpha[kc][2]^transport(d,kc,kd)
def U(word,c):
 k,l=kl(c);ob=c[0][:l]+(b,)*(len(c[0])-l)
 ar=tuple(c[1][i] if i<l else ident(b) for i in range(len(word)))
 return ob,ar
def Umap(word,c,d,alpha):
 l=kl(c)[1];ud=U(word,d)
 return tuple(alpha[i] if i<l else hom(b,ud[0][i])[0] for i in range(len(alpha)))
def section(word):
 k0=word.index('+')+1;l0=len(word)-word[::-1].index('-')
 assert k0<l0
 ob=(a,)*k0+(g,)*(l0-k0)+(b,)*(len(word)+1-l0)
 ar=[]
 for i,sgn in enumerate(word):
  x,y=(ob[i],ob[i+1]) if sgn=='+' else (ob[i+1],ob[i])
  ar.append(hom(x,y)[0])
 return tuple(ob),tuple(ar)
def smap(s,bit):return tuple((x,x,bit if x==g else 0) for x in s[0])
def eps(c):
 l=kl(c)[1]
 return tuple(ident(x) if i<l else hom(b,x)[0] for i,x in enumerate(c[0]))
def theta(word,c,s):
 uc=U(word,c);k,l=kl(c);out=[]
 for i,(x,y) in enumerate(zip(uc[0],s[0])):
  out.append((g,g,transport(c,i,k)) if x==g else hom(x,y)[0])
 return tuple(out)
def compose_nt(v,u):return tuple(comp(y,x) for x,y in zip(u,v))
counts=defaultdict(int);records=[]
for n in range(1,5):
 for letters in product('+-',repeat=n):
  word=''.join(letters);ps=list(paths(word))
  if not ps:counts['empty_types']+=1;continue
  s=section(word);assert s in ps
  assert E(s,s,smap(s,0))==0 and E(s,s,smap(s,1))==1
  ats=[];outgoing=defaultdict(list)
  for ci,c in enumerate(ps):
   uc=U(word,c);assert uc in ps
   assert is_nat(word,uc,c,eps(c))
   assert is_nat(word,uc,s,theta(word,c,s))
   counts['object_retraction_checks']+=1
   for di,d in enumerate(ps):
    for alpha in nats(word,c,d):
     ualpha=Umap(word,c,d,alpha);ed=E(c,d,alpha)
     assert is_nat(word,uc,U(word,d),ualpha)
     assert is_nat(word,s,s,smap(s,ed))
     # Naturality of U=>id and U=>sE.
     assert compose_nt(alpha,eps(c))==compose_nt(eps(d),ualpha)
     assert compose_nt(smap(s,ed),theta(word,c,s))==compose_nt(theta(word,d,s),ualpha)
     ats.append((ci,di,alpha));outgoing[ci].append((di,alpha))
  for ci,di,alpha in ats:
   c,d=ps[ci],ps[di]
   for ei,beta in outgoing[di]:
    e=ps[ei];gamma=compose_nt(beta,alpha)
    assert is_nat(word,c,e,gamma)
    assert E(c,e,gamma)==(E(c,d,alpha)^E(d,e,beta))
    assert Umap(word,c,e,gamma)==compose_nt(Umap(word,d,e,beta),Umap(word,c,d,alpha))
    counts['composite_checks']+=1
  counts['nonempty_types']+=1;counts['path_objects']+=len(ps);counts['path_arrows']+=len(ats)
  records.append({'word':word,'objects':len(ps),'arrows':len(ats)})
result={'status':'PASS','category_objects':3,'category_arrows':6,'counts':dict(counts),'types':records}
text=json.dumps(result,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(text)
print(text,end='')
