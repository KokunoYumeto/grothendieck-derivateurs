#!/usr/bin/env python3
"""Exact finite positive-saturation and basis certificates.
These examples concern restricted amalgamation proposals, not the main derived-colimit question.
"""
from pathlib import Path
from collections import defaultdict,deque
import json
def check(words,limit=200000):
 es=[];nv=1
 for word in words:
  s=0
  for k,a in enumerate(word):
   t=0 if k==len(word)-1 else nv
   if t:nv+=1
   es.extend(((s,a,t),(t,-a,s)));s=t
 par=list(range(nv))
 def find(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 changed=True
 while changed:
  changed=False;out={}
  for s,a,t in es:
   s,t=find(s),find(t)
   if (s,a) in out:
    u=find(out[s,a])
    if t!=u:par[t]=u;changed=True
   else:out[s,a]=t
 folded={(find(s),a,find(t))for s,a,t in es}
 dag=defaultdict(dict);nfa=defaultdict(lambda:defaultdict(set))
 for s,a,t in folded:
  if a>0:dag[s][a]=t
 for s,a,t in es:
  if a>0:nfa[s][a].add(t)
 root=find(0);start=(root,frozenset([0]));queue=deque([start]);prev={start:None}
 found=None
 while queue:
  state=queue.popleft();v,ns=state
  if v==root and 0 not in ns:found=state;break
  for a,t in sorted(dag[v].items()):
   nts=frozenset(z for q in ns for z in nfa[q].get(a,()))
   nxt=(t,nts)
   if nxt not in prev:
    prev[nxt]=(state,a);queue.append(nxt)
  if len(prev)>limit:
   return {'status':'bounded-search-inconclusive','product_states':len(prev)}
 if found is not None:
  w=[];at=found
  while prev[at] is not None:
   at,a=prev[at];w.append(a)
  w.reverse()
  return {'status':'not-saturated','product_states':len(prev),
          'shortest_witness_length':len(w),'witness':w,
          'source_word_lengths':[len(w)for w in words]}
 return {'status':'saturated','product_states':len(prev),
         'source_word_lengths':[len(w)for w in words]}

def red(w):
 r=[]
 for x in w:
  if r and r[-1]==-x:r.pop()
  else:r.append(x)
 return r

def inv(w):return [-x for x in reversed(w)]
def subst(w,images):
 return red([z for x in w for z in (images[abs(x)-1] if x>0 else inv(images[-x-1]))])
def basis(images,inverses):
 n=len(images)
 assert n==len(inverses)
 for i in range(n):
  assert subst(images[i],inverses)==[i+1],(i,'source')
  assert subst(inverses[i],images)==[i+1],(i,'target')
 return 2*n

def bifix(words):
 for i,x in enumerate(words):
  for j,y in enumerate(words):
   if i!=j:
    assert y[:len(x)]!=x and y[-len(x):]!=x

def unique_code(words):
 """Exact Sardinas--Patterson exhaustion for a finite positive code."""
 words=[tuple(w)for w in words]
 assert len(set(words))==len(words) and all(words)
 def quot(x,y):return y[len(x):] if y[:len(x)]==x else None
 current=frozenset(q for x in words for y in words if x!=y
                   for q in [quot(x,y)] if q is not None)
 seen=set();rounds=0
 while current and current not in seen:
  assert () not in current
  seen.add(current);rounds+=1
  current=frozenset(q for x in words for y in current
                    for q in [quot(x,y),quot(y,x)] if q is not None)
 return rounds

cases={
 'cone_conflict_left':([[1,2],[1,3],[2,4]],[ [1,2],[1,3],[2,4],[2] ],[[1,-4],[4],[4,-1,2],[-4,3]]),
 'cone_conflict_right':([[1,3,2,4,5],[1,2],[3,4]],[[1,3,2,4,5],[1,2],[3,4],[1],[3]],[[4],[-4,2],[5],[-5,3],[-3,5,-2,4,-5,-4,1]]),
 'saturated_output_left':([[1,2],[1,3],[4]],[[1,2],[1,3],[4],[1]],[[4],[-4,1],[-4,2],[3]]),
 'saturated_output_right':([[2],[1,3],[1,4]],[[2],[1,3],[1,4],[1]],[[4],[1],[-4,2],[-4,3]])
}
out={};checks=0
for name,(words,images,inverses) in cases.items():
 bifix(words);r=check(words);assert r['status']=='saturated',r
 count=basis(images,inverses);checks+=count
 r['group_inverse_identities']=count
 out[name]=r
 print(name,'saturated',r['product_states'],'states;',count,'inverse identities; bifix PASS')
# Ordinary positive amalgam for the second span, target alphabet a,b,e,C,D.
left=[[1],[2],[3,4],[1,3,5]]
right=[[1,3],[1,2],[4],[5]]
source_left=cases['saturated_output_left'][0]
source_right=cases['saturated_output_right'][0]
for x,y in zip(source_left,source_right):assert subst(x,left)==subst(y,right)
# Verify injectivity directly by finite residual-word exhaustion, and also
# retain full abelian rank certificates as a separate finite check.
code_rounds={'left':unique_code(left),'right':unique_code(right)}
import sympy as sp
from itertools import combinations
minors={}
for name,words in [('left',left),('right',right)]:
 mat=sp.Matrix([[w.count(j) for w in words]for j in range(1,6)])
 found=None
 for rs in combinations(range(5),4):
  det=int(mat[list(rs),:].det())
  if abs(det)==1:found=(list(rs),det);break
 assert found is not None
 minors[name]=found
out['ordinary_amalgam']={'source_equations':3,'unit_minors':minors,'residual_code_rounds':code_rounds,'scope':'injective ordinary monoid maps; output saturation is not claimed'}
out['scope']='Four finite input saturation tests and group-basis certificates; no universal comparison conclusion.'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Total exact group inverse identities:',checks)
print('Ordinary amalgam:3 equations,2 residual-code checks and2 unit-minor certificates PASS')
