#!/usr/bin/env python3
"""Check the saved finite twisted factors against necessary G.19 orbit orders.

An admissible order for a full-support edge orbit is either equality,
a signed order on one coordinate inside a fixed singleton-coordinate
fiber, or a signed two-coordinate global lex order. This finite checker
only tests compatibility on the six saved edges; it is not a proof of
any global realization.
"""
import json
from itertools import permutations,product
from pathlib import Path
r=json.loads(Path(__file__).with_name('G_twisted_lex_chains.json').read_text())
w=r['best']['point_words'];n=r['n'];edges=r['edges'];factors={k:[] for k in 'pqrs'}
for (a,b,c),z in zip(edges,r['best']['rectangle_lengths']):
 factors['p'].append(w[a][:z['p']]);factors['q'].append(w[a][z['p']:])
 factors['r'].append(w[b][:z['r']]);factors['s'].append(w[n+c][:z['s']])

def cmp_words(x,y,side):
 if x==y:return 0
 if side=='prefix':
  if x==y[:len(x)]:return -1
  if y==x[:len(y)]:return 1
 else:
  if x==y[-len(x):]:return -1
  if y==x[-len(y):]:return 1
 return None

def model(e,f,kind,base=None,pivots=(),signs=()):
 if e==f:return 0
 if kind=='equality':return None
 if kind=='fiber' and e[base]!=f[base]:return None
 a=tuple(s*e[i] for i,s in zip(pivots,signs));b=tuple(s*f[i] for i,s in zip(pivots,signs))
 return (a>b)-(a<b)
models=[dict(kind='equality')]
for base in range(3):
 for pivot in range(3):
  if pivot!=base:
   for sign in (-1,1):models.append(dict(kind='fiber',base=base,pivots=[pivot],signs=[sign]))
for pivots in permutations(range(3),2):
 for signs in product((-1,1),repeat=2):models.append(dict(kind='global',pivots=pivots,signs=signs))
answer={}
for k in 'pqrs':
 for side in ('prefix','suffix'):
  actual=[[cmp_words(x,y,side) for y in factors[k]] for x in factors[k]]
  compatible=[m for m in models if all(actual[i][j]==model(e,f,**m) for i,e in enumerate(edges) for j,f in enumerate(edges))]
  answer[k+'_'+side]=dict(actual=actual,compatible=compatible)
  print(k,side,'compatible order models:',len(compatible),compatible,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(answer,indent=2)+'\n')
print('Finite compatibility only. Empty lists refute this saved model as a global factor-orbit pattern, not all same-flag models.')
