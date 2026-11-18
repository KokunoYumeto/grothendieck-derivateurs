#!/usr/bin/env python3
"""Exact positive-language saturation checks on the finite G22 charts.
For each given positive code X, compare X* with <X>_group intersect A*.
A found witness refutes saturation; a completed finite automaton search proves it.
No assertion about global diagrams is made.
"""
from pathlib import Path
from collections import defaultdict,deque
import json
R=json.loads(Path(__file__).with_name('G_twisted_lex_chains.json').read_text())
ws=R['best']['point_words'];n=R['n'];edges=R['edges'];rects=R['best']['rectangle_lengths']
alphabet=sorted(set(sum(ws,[])));code={a:i+1 for i,a in enumerate(alphabet)}
ws=[[code[c] for c in w]for w in ws]

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

out={}
for x in range(n):out['point_'+str(x+1)]=check([ws[x],ws[n+x]])
for e,((a,b,c),z) in enumerate(zip(edges,rects)):
 factors=[ws[a][:z['p']],ws[a][z['p']:],ws[b][:z['r']],ws[n+c][:z['s']],ws[c],ws[n+b]]
 out['edge_'+str(e+1)]=check(factors)
for name,r in out.items():
 print(name,r['status'],'states',r['product_states'],
       'witness_length',r.get('shortest_witness_length'))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Finite G22 positive-language tests only; no amalgamation or global-extension conclusion.')
