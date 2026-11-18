#!/usr/bin/env python3
"""Finite twisted incidence tests imposing admissible lex orders on q/s.

The global suffix q-chain and prefix s-chain have the same chosen signed
lex order on the strong-edge orbit.  This is a necessary structural regime,
not a construction on the full category.  All word equalities/ranks are exact.
"""
import argparse
import itertools
import json
from pathlib import Path
import random
from collections import Counter
import sympy as sp
from G_twisted_chains_search import unify
from G_cross_lift_rank_search import EDGES,N

ap=argparse.ArgumentParser()
ap.add_argument('--trials',type=int,default=3)
ap.add_argument('--seed',type=int,default=202611180723)
args=ap.parse_args()
rng=random.Random(args.seed)
d=sp.zeros(len(EDGES),2*N)
for i,(a,b,c) in enumerate(EDGES):
 d[i,b]+=1;d[i,a]-=1;d[i,N+c]+=1;d[i,N+a]-=1
kernel=d.nullspace()
expected=2*N-d.rank()
rows=[];best=None
for first,second in itertools.permutations(range(3),2):
 for signs in itertools.product((-1,1),repeat=2):
  order=sorted(range(len(EDGES)),key=lambda j:(signs[0]*EDGES[j][first],signs[1]*EDGES[j][second]))
  ranks={edge:i for i,edge in enumerate(order)}
  histogram=Counter()
  for trial in range(args.trials):
   perturb=sp.zeros(2*N,1)
   for v in kernel:perturb+=rng.randint(-4,4)*v
   perturb=list(map(int,perturb))
   differences=[perturb[N+c]-perturb[a] for a,b,c in EDGES]
   step=2*max([abs(x) for x in differences]+[1])+3
   base=max([abs(x) for x in differences]+[1])+3
   q=[base+step*ranks[j] for j in range(len(EDGES))]
   shift=max(q)+2*max(map(abs,perturb))+7
   lengths=[shift+x for x in perturb]
   cuts=[lengths[a]-qj for (a,b,c),qj in zip(EDGES,q)]
   result=unify(N,EDGES,lengths,cuts)
   assert [result['rectangle_lengths'][j]['q'] for j in order]==sorted(q)
   assert [result['rectangle_lengths'][j]['s'] for j in order]==sorted(z['s'] for z in result['rectangle_lengths'])
   histogram[result['rank']]+=1
   score=(result['rank'],-len(result['prefix_pairs'])-len(result['suffix_pairs']))
   if best is None or score>tuple(best['score']):
    best=dict(result,first=first,second=second,signs=signs,trial=trial,
              lengths=lengths,cuts=cuts,score=score)
  rows.append(dict(first=first,second=second,signs=signs,edge_order=order,
                   rank_histogram=dict(sorted(histogram.items()))))
  print('flag',first,second,signs,'ranks',dict(sorted(histogram.items())),flush=True)
report=dict(parameters=vars(args),n=N,edges=EDGES,expected_rank=expected,
            regimes=rows,best=best,finite_only=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('Best point rank:',best['rank'],'/',expected,'prefix/suffix comparabilities:',len(best['prefix_pairs']),len(best['suffix_pairs']))
print('Finite regimes only. No universal construction or nonexistence conclusion.')
