#!/usr/bin/env python3
"""Fundamental groups by spanning-tree presentations and certified Tietze eliminations."""
from pathlib import Path
from itertools import combinations
import json
P=Path(__file__).parent

def reduce_word(w):
 st=[]
 for x in w:
  if st and st[-1]==-x:st.pop()
  else:st.append(x)
 return st

def inverse(w):return [-x for x in reversed(w)]

def fundamental_group(points,R):
 n=len(points);less=lambda i,j:i!=j and all((x,y) in R for x,y in zip(points[i],points[j]))
 edges=[(i,j) for i in range(n) for j in range(n) if less(i,j)]
 parent=list(range(n))
 def find(i):
  while parent[i]!=i:i=parent[i]
  return i
 tree=set()
 for i,j in edges:
  a,b=find(i),find(j)
  if a!=b:parent[a]=b;tree.add((i,j))
 gens={edge:k+1 for k,edge in enumerate(e for e in edges if e not in tree)}
 rels=[]
 for i,j in edges:
  for k in range(n):
   if less(j,k):rels.append(reduce_word([x for x in [gens.get((i,j),0),gens.get((j,k),0),-gens.get((i,k),0)] if x]))
 initial=[w[:] for w in rels if w];active=set(gens.values());steps=[]
 while True:
  rels=[reduce_word(w) for w in rels];rels=[w for w in rels if w]
  found=None
  for ri,w in enumerate(rels):
   for pos,x in enumerate(w):
    g=abs(x)
    if sum(abs(y)==g for y in w)==1:
     u=w[pos+1:]+w[:pos];replacement=inverse(u) if x>0 else u
     found=(ri,g,replacement);break
   if found:break
  if not found:break
  ri,g,replacement=found;steps.append({'generator':g,'relation':rels[ri],'replacement':replacement});active.remove(g)
  def sub(w):
   out=[]
   for x in w:out.extend(replacement if x==g else inverse(replacement) if x==-g else [x])
   return reduce_word(out)
  rels=[sub(w) for k,w in enumerate(rels) if k!=ri]
 return {'initial_generators':len(gens),'initial_relations':initial,'tietze_steps':steps,
 'remaining_generators':sorted(active),'remaining_relations':rels,
 'conclusion':f'free group of rank {len(active)}' if not rels else 'presentation retained'}

catalogue={x['id']:x for x in json.loads((P/'relative_posets_catalogue.json').read_text())};out=[]
for c in json.loads((P/'relative_posets_certificates.json').read_text()):
 if any(len(comp)>1 for comp in c['core_paths']):
  R=set(map(tuple,catalogue[c['id']]['order']));points=[tuple(p) for comp in c['core_paths'] for p in comp]
  out.append({'id':c['id'],'length':c['L'],'a':c['a'],'b':c['b'],**fundamental_group(points,R)})
(P/'core_fundamental_groups_output.json').write_text(json.dumps(out,indent=2));print(json.dumps([{k:v for k,v in r.items() if k not in ['initial_relations','tietze_steps']} for r in out],indent=2))
