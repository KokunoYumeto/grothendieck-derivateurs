#!/usr/bin/env python3
"""Verify the saved finite twisted four-factor charts without resampling."""
from collections import Counter
import json
from pathlib import Path
import sympy as sp

for shape in ('lex_chains',):
    path=Path(__file__).with_name('G_twisted_lex_chains.json')
    report=json.loads(path.read_text())
    n=report['n']; words=report['best']['point_words']
    ranks=[]
    for (a,b,c),lens in zip(report['edges'],report['best']['rectangle_lengths']):
        p=words[a][:lens['p']]
        q=words[a][lens['p']:]
        r=words[b][:lens['r']]
        s=words[n+c][:lens['s']]
        assert p+q==words[a] and r+q==words[b]
        assert s+p==words[n+c] and s+r==words[n+a]
        images=[p,q,r,s,words[c],words[n+b]]
        counts=[Counter(w) for w in images]
        alphabet=sorted(set().union(*(set(w) for w in images)))
        matrix=sp.Matrix(6,len(alphabet),lambda i,j:counts[i][alphabet[j]])
        ranks.append(matrix.rank())
    assert all(rank==6 for rank in ranks)
    matrix=sp.Matrix(2*n,len(report['best']['count_patterns']),
                     lambda i,j:report['best']['count_patterns'][j][i])
    assert matrix.rank()==report['expected_rank']
    for a,b,c in report['edges']:
        assert matrix.row(b)-matrix.row(a)+matrix.row(n+c)-matrix.row(n+a)==sp.zeros(1,matrix.cols)
    assert not report['best']['prefix_pairs'] and not report['best']['suffix_pairs']
    qs=[];ss=[]
    for (a,b,c),z in zip(report['edges'],report['best']['rectangle_lengths']):
        qs.append(words[a][z['p']:]);ss.append(words[n+c][:z['s']])
    from itertools import combinations
    for x,y in combinations(qs,2): assert x==y[-len(x):] or y==x[-len(y):]
    for x,y in combinations(ss,2): assert x==y[:len(x)] or y==x[:len(y)]
    flag=report['best'];f,k=flag['first'],flag['second'];e1,e2=flag['signs']
    order=sorted(range(len(report['edges'])),key=lambda j:(e1*report['edges'][j][f],e2*report['edges'][j][k]))
    assert [len(qs[j]) for j in order]==sorted(map(len,qs))
    assert [len(ss[j]) for j in order]==sorted(map(len,ss))
    print('Exact global suffix q-chain and prefix s-chain verified with signed lex flag',f,k,(e1,e2))
    print(f'{shape}: every rectangle composition exact; edge chart ranks={ranks}; '
          f'point incidence rank={matrix.rank()}; all point words bifix; PASS')
print('Only the indicated finite V,W,X diagrams are certified; global extension remains unproved.')
from G_rectangle_basis_search import fold
from G_rectangle_local import reduce_group
core=['pq','rq','sp','sr']
vertices,rank,_=fold(core)
assert rank==4
# u_b u_a^{-1} v_c v_a^{-1}; uppercase denotes inverse.
relator=reduce_group('rqQPspRS')
assert relator
print('Twisted local core group rank:',rank,'(four independent words).')
print('Original DF relator is nontrivial:',relator)
