#!/usr/bin/env python3
"""Verify enumerated multiplication tables and record idempotent-corner reductions.
The proof in A.5 identifies each reduction as a nerve weak equivalence.
The reduced monoids of order <=5 are groups or the rectangular-band monoid.
"""
from pathlib import Path
from itertools import product,permutations
import json,collections
P=Path(__file__).parent

def canonical(n,t):
 out=[]
 for tail in permutations(range(1,n)):
  p=(0,)+tail;iv={x:i for i,x in enumerate(p)}
  out.append(tuple(iv[t[p[i]*n+p[j]]] for i in range(n) for j in range(n)))
 return min(out)

def corner(n,t,e):
 mul=lambda a,b:t[a*n+b]
 elements={mul(mul(e,x),e) for x in range(n)}
 elems=[e]+sorted(elements-{e});iv={x:i for i,x in enumerate(elems)}
 return len(elems),canonical(len(elems),[iv[mul(x,y)] for x in elems for y in elems])

def options(n,t):
 mul=lambda a,b:t[a*n+b]
 for e in range(1,n):
  if mul(e,e)!=e:continue
  eM={mul(e,x) for x in range(n)};Me={mul(x,e) for x in range(n)}
  eMe={mul(mul(e,x),e) for x in range(n)}
  if eMe==eM or eMe==Me:
   yield e,('eM' if eMe==eM else 'Me'),corner(n,t,e)

def group(n,t):return all(any(t[x*n+y]==t[y*n+x]==0 for y in range(n)) for x in range(n))

M=json.loads((P/'monoids_tables.json').read_text());lookup={(m['n'],tuple(m['table'])):i for i,m in enumerate(M)}
rows=[];terminal_counts=collections.Counter()
for i,m in enumerate(M):
 n=m['n'];t=m['table']
 assert all(t[j]==t[j*n]==j for j in range(n))
 assert all(t[t[a*n+b]*n+c]==t[a*n+t[b*n+c]] for a,b,c in product(range(n),repeat=3))
 assert tuple(t)==canonical(n,t)
 chain=[];nn,tt=n,tuple(t)
 while True:
  opts=list(options(nn,tt))
  if not opts:break
  e,side,(nn2,tt2)=min(opts,key=lambda x:x[2][0]);assert nn2<nn
  chain.append({'source':lookup[(nn,tt)],'idempotent':e,'side':side,'target':lookup[(nn2,tt2)]})
  nn,tt=nn2,tt2
 target=lookup[(nn,tt)];terminal_counts[target]+=1
 kind='group' if group(nn,tt) else 'rectangular-band-with-unit'
 if kind!='group':
  assert nn==5 and all(tt[x*nn+x]==x for x in range(1,nn))
  assert all(tt[tt[x*nn+y]*nn+z]==tt[x*nn+z] for x,y,z in product(range(1,nn),repeat=3))
 rows.append({'id':i,'n':n,'reduction_chain':chain,'terminal_id':target,'type':kind,'is_1_type':kind=='group'})
summary={'monoid_isomorphism_classes':len(rows),'counts_by_order':dict(collections.Counter(r['n'] for r in rows)),
 'non_1_types':[r['id'] for r in rows if not r['is_1_type']], 'terminal_counts':dict(terminal_counts)}
(P/'monoids_classification.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2));print(json.dumps(summary,indent=2))
