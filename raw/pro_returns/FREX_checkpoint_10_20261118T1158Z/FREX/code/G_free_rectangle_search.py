#!/usr/bin/env python3
"""Exact fixed-length unification of unrestricted four-factor rectangles.

For each edge (a,b,c), impose u_a=pq, u_b=rq, v_c=ps, v_a=rs.
The lengths and cut positions are sampled, while all resulting equalities and
ranks are checked exactly. Finite failures are not nonexistence proofs.
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import random
import sympy as sp
from G_cross_lift_rank_search import UF, EDGES as THETA_EDGES, N as THETA_N


def unify(n, edges, lengths, cuts):
    offsets = [0]
    for length in lengths:
        offsets.append(offsets[-1] + length)
    uf = UF(offsets[-1])
    blocks = []
    for (a,b,c), p in zip(edges,cuts):
        q = lengths[a]-p
        r = lengths[b]-q
        s = lengths[n+c]-p
        assert min(p,q,r,s)>0
        assert r+s == lengths[n+a]
        # Pair the two occurrences of each of p,q,r,s.
        pairs = [(a,0,n+c,0,p),
                 (a,p,b,r,q),
                 (b,0,n+a,0,r),
                 (n+c,p,n+a,r,s)]
        for i,ii,j,jj,size in pairs:
            for k in range(size):
                uf.union(offsets[i]+ii+k, offsets[j]+jj+k)
        blocks.append(dict(p=p,q=q,r=r,s=s))
    words = [[uf.find(j) for j in range(offsets[i],offsets[i+1])]
             for i in range(2*n)]
    columns = defaultdict(lambda:[0]*(2*n))
    for i,word in enumerate(words):
        for letter in word:
            columns[letter][i] += 1
    patterns = sorted(set(map(tuple,columns.values())))
    mat=sp.Matrix(2*n,len(patterns),lambda i,j:patterns[j][i])
    rank=mat.rank()
    prefix_pairs=[]
    suffix_pairs=[]
    for i in range(2*n):
        for j in range(i+1,2*n):
            x,y=words[i],words[j]
            if x==y[:len(x)] or y==x[:len(y)]:
                prefix_pairs.append([i,j])
            if x==y[-len(x):] or y==x[-len(y):]:
                suffix_pairs.append([i,j])
    return dict(rank=rank, alphabet_size=len(columns), count_patterns=patterns,
                point_words=words, rectangle_lengths=blocks,
                prefix_pairs=prefix_pairs, suffix_pairs=suffix_pairs)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--shape',choices=['fan','theta'],default='theta')
    ap.add_argument('--trials',type=int,default=200)
    ap.add_argument('--seed',type=int,default=20261118)
    ap.add_argument('--scale',type=int,default=30)
    args=ap.parse_args()
    n,edges=(5,[(0,1,2),(0,3,4)]) if args.shape=='fan' else (THETA_N,THETA_EDGES)
    d=sp.zeros(len(edges),2*n)
    for j,(a,b,c) in enumerate(edges):
        d[j,b]+=1;d[j,a]-=1;d[j,n+c]+=1;d[j,n+a]-=1
    basis=d.nullspace()
    expected=2*n-d.rank()
    rng=random.Random(args.seed)
    histogram=Counter()
    best=None
    for trial in range(args.trials):
        perturb=sp.zeros(2*n,1)
        for v in basis:
            perturb+=rng.randint(-args.scale,args.scale)*v
        perturb=list(map(int,perturb))
        margin=2*max(map(abs,perturb))+5
        lengths=[margin+x for x in perturb]
        cuts=[]
        for a,b,c in edges:
            lo=max(1,lengths[a]-lengths[b]+1)
            hi=min(lengths[a]-1,lengths[n+c]-1)
            assert lo<=hi
            cuts.append(rng.randint(lo,hi))
        assert d*sp.Matrix(lengths)==sp.zeros(len(edges),1)
        result=unify(n,edges,lengths,cuts)
        histogram[result['rank']]+=1
        score=(result['rank'],-len(result['prefix_pairs'])-len(result['suffix_pairs']))
        if best is None or score>best['score']:
            best=dict(result,trial=trial,lengths=lengths,cuts=cuts,score=score)
            print(f'trial={trial} rank={result["rank"]}/{expected} '
                  f'alphabet={result["alphabet_size"]} '
                  f'prefix={len(result["prefix_pairs"])} suffix={len(result["suffix_pairs"])}',flush=True)
        if result['rank']==expected and not result['prefix_pairs'] and not result['suffix_pairs']:
            print('Full incidence rank with pairwise bifix point words found.',flush=True)
            break
    report=dict(parameters=vars(args),n=n,edges=edges,expected_rank=expected,
                trials=trial+1,rank_histogram=dict(sorted(histogram.items())),best=best,
                finite_search_only=True)
    path=Path(__file__).with_name(f'G_free_rectangle_{args.shape}.json')
    path.write_text(json.dumps(report,indent=2)+'\n')
    print('Exact rank histogram:',dict(sorted(histogram.items())),flush=True)
    print('Finite search only; no global extension or nonexistence claim.',flush=True)


if __name__=='__main__':
    main()
