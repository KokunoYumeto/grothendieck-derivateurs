#!/usr/bin/env python3
"""Vary positive local free-group bases, then test their X11 extensions.

Finite randomized experiment.  Failed samples do not prove nonexistence.
"""
import argparse, json, random
from collections import Counter
from pathlib import Path
import sympy as sp
from G_rectangle_local import bifix, determinant
from G_rectangle_basis_search import fold
from G_rectangle_extension_search import solution, EDGES, N


def main():
    global N, EDGES
    ap=argparse.ArgumentParser()
    ap.add_argument('--templates',type=int,default=12)
    ap.add_argument('--trials',type=int,default=3)
    ap.add_argument('--seed',type=int,default=20261118)
    ap.add_argument('--max-length',type=int,default=6)
    ap.add_argument('--configuration',choices=['theta','fan'],default='theta')
    args=ap.parse_args()
    if args.configuration=='fan':
        import G_rectangle_extension_search as extension
        N=extension.N=5
        EDGES=extension.EDGES=[(0,1,2),(0,3,4)]
    expected=2*N-len(EDGES)
    rng=random.Random(args.seed)
    incidence=sp.zeros(len(EDGES),2*N)
    for i,(a,b,c) in enumerate(EDGES):
        incidence[i,b]+=1;incidence[i,a]-=1
        incidence[i,N+c]+=1;incidence[i,N+a]-=1
    kernel=incidence.nullspace()
    report=[]
    attempts=0
    best_rank=0
    best=None
    for template_no in range(args.templates):
        while True:
            attempts+=1
            p,r,q,s=[''.join(rng.choice('abc') for _ in range(
                rng.randint(1,args.max_length))) for _ in range(4)]
            words=[p+q,r+q,p+s,r+s]
            difference=[r.count(a)-p.count(a) for a in 'abc']
            if not min(difference)<0<max(difference):continue
            if not bifix(words):continue
            counts=[[word.count(a) for a in 'abc'] for word in words[:3]]
            if abs(determinant(counts))!=1:continue
            vertices,rank,_=fold(words)
            if vertices==1 and rank==3:break
        inverse=sp.Matrix(counts).inv()
        pos=sum(max(0,x) for x in difference)
        neg=sum(max(0,-x) for x in difference)
        weights=[neg if d>0 else pos if d<0 else 1 for d in difference]
        U=sum(weights[i]*words[0].count(a) for i,a in enumerate('abc'))
        V=sum(weights[i]*words[2].count(a) for i,a in enumerate('abc'))
        assert U==sum(weights[i]*words[1].count(a) for i,a in enumerate('abc'))
        templates=dict(ua=words[0],ub=words[1],vc=words[2],va=words[3])
        hist=Counter()
        min_edge=[]
        for trial in range(args.trials):
            perturb=sp.zeros(2*N,1)
            for vec in kernel:perturb+=rng.randint(-2,2)*vec
            perturb=list(map(int,perturb))
            scale=1
            for a,b,c in EDGES:
                block=list(map(int,inverse*sp.Matrix(
                    [perturb[a],perturb[b],perturb[N+c]])))
                scale=max(scale,1+max(abs(x)//w for x,w in zip(block,weights)))
            lengths=[scale*(U if i<N else V)+perturb[i] for i in range(2*N)]
            rank,alphabet,patterns,edge_ranks,point_words,edge_maps=solution(
                lengths,templates,inverse)
            hist[rank]+=1;min_edge.append(min(edge_ranks))
            if rank>best_rank:
                best_rank=rank
                best=dict(template=templates,rank=rank,alphabet=alphabet,
                          edge_ranks=edge_ranks,lengths=lengths,
                          point_words=point_words,edge_maps=edge_maps)
                print(f'new rank {rank}/{expected} at template {template_no}, edge ranks {edge_ranks}',flush=True)
        row=dict(template_number=template_no,p=p,r=r,q=q,s=s,words=words,
                 base_weights=weights,base_U=U,base_V=V,
                 rank_histogram=dict(sorted(hist.items())),min_edge_ranks=min_edge)
        report.append(row)
        print(f'template={template_no} ranks={dict(sorted(hist.items()))} min_edges={min_edge}',flush=True)
        Path(__file__).with_name('G_rectangle_vary_'+args.configuration+'.json').write_text(json.dumps(
            dict(parameters=vars(args),candidates_tried=attempts,templates=report,
                 best=best,negative_results_are_only_exploratory=True),indent=2)+'\n')
        if best_rank==expected and min(best['edge_ranks'])==5:break
    print('Finite experiment only; no global existence or nonexistence conclusion.',flush=True)


if __name__=='__main__':main()
