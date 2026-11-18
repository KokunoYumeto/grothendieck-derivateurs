#!/usr/bin/env python3
"""Test the remaining cross-family Levi branch on the eleven-vertex example.

For e=(a,b,c), impose v_c=u_a t_e and v_a=u_b t_e. For each sampled
integral length vector in the incidence kernel, identify corresponding
letter positions. The resulting words are the most general solution for
those fixed lengths. Compute the exact rank of their abelianized images.
This is a finite exploratory test, never a nonexistence proof.
"""
import argparse, json, random
from collections import Counter, defaultdict
from pathlib import Path
import sympy as sp

EDGES=[(0,1,8),(1,2,9),(2,3,10),(0,3,4),(4,5,6),(6,7,8)]
N=11

class UF:
    def __init__(self,n): self.p=list(range(n)); self.sz=[1]*n
    def find(self,a):
        while self.p[a]!=a:
            self.p[a]=self.p[self.p[a]]; a=self.p[a]
        return a
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b:return
        if self.sz[a]<self.sz[b]:a,b=b,a
        self.p[b]=a; self.sz[a]+=self.sz[b]

def solution(lengths):
    offset=[0]
    for length in lengths: offset.append(offset[-1]+length)
    uf=UF(offset[-1])
    for a,b,c in EDGES:
        t=lengths[N+c]-lengths[a]
        assert t==lengths[N+a]-lengths[b] and t>0
        for j in range(lengths[a]):uf.union(offset[a]+j,offset[N+c]+j)
        for j in range(lengths[b]):uf.union(offset[b]+j,offset[N+a]+j)
        for j in range(t):
            uf.union(offset[N+c]+lengths[a]+j,offset[N+a]+lengths[b]+j)
    columns=defaultdict(lambda:[0]*(2*N))
    for i in range(2*N):
        for j in range(offset[i],offset[i+1]):columns[uf.find(j)][i]+=1
    patterns=list(set(map(tuple,columns.values())))
    matrix=sp.Matrix(2*N,len(patterns),lambda i,j:patterns[j][i])
    return matrix.rank(), len(columns), patterns

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--trials',type=int,default=50)
    ap.add_argument('--seed',type=int,default=20261118); args=ap.parse_args()
    rng=random.Random(args.seed)
    d=sp.zeros(len(EDGES),2*N)
    for j,(a,b,c) in enumerate(EDGES):
        d[j,b]+=1;d[j,a]-=1;d[j,N+c]+=1;d[j,N+a]-=1
    kernel=d.nullspace(); expected=2*N-len(EDGES)
    assert len(kernel)==expected
    hist=Counter(); best=None
    for k in range(args.trials):
        perturb=sp.zeros(2*N,1)
        for vec in kernel: perturb+=rng.randrange(-9,10)*vec
        perturb=list(map(int,perturb))
        scale=2*max(map(abs,perturb))+2
        lengths=[scale*(1 if i<N else 2)+perturb[i] for i in range(2*N)]
        rank,alphabet,patterns=solution(lengths)
        hist[rank]+=1
        if best is None or rank>best['rank']:
            assert d*sp.Matrix(2*N,len(patterns),lambda i,j:patterns[j][i])==sp.zeros(len(EDGES),len(patterns))
            best={'rank':rank,'expected_rank':expected,'lengths':lengths,
                  'alphabet_size':alphabet,'count_patterns':patterns,'trial':k}
            print(f'trial={k}, rank={rank}/{expected}, alphabet={alphabet}',flush=True)
    out={'seed':args.seed,'trials':args.trials,'rank_histogram':dict(sorted(hist.items())), 'best':best}
    Path(__file__).with_name('G_cross_lift_rank_search.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Exact rank histogram:',dict(sorted(hist.items())),flush=True)
    print('No inference of nonexistence is made from this finite search.',flush=True)

if __name__=='__main__':main()
