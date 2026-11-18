#!/usr/bin/env python3
"""Search positive word lifts of the incidence relation only in abelianization.

The four core words are group-independent (Stallings rank four), so they
never satisfy the original DF group relator.  Tests concern only the named
finite configuration.  No failed sample is a nonexistence theorem.
"""
import argparse
import json
import random
from collections import Counter
from pathlib import Path
from math import lcm
import sympy as sp
import G_rectangle_extension_search as extension
from G_rectangle_basis_search import fold


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--templates',type=int,default=50)
    ap.add_argument('--trials',type=int,default=4)
    ap.add_argument('--seed',type=int,default=202611180640)
    ap.add_argument('--max-length',type=int,default=8)
    ap.add_argument('--configuration',choices=['theta','fan'],default='fan')
    args=ap.parse_args()
    if args.configuration=='fan':
        extension.N=5
        extension.EDGES=[(0,1,2),(0,3,4)]
    n,edges=extension.N,extension.EDGES
    expected=2*n-len(edges)
    rng=random.Random(args.seed)
    incidence=sp.zeros(len(edges),2*n)
    for i,(a,b,c) in enumerate(edges):
        incidence[i,b]+=1; incidence[i,a]-=1
        incidence[i,n+c]+=1; incidence[i,n+a]-=1
    kernel=incidence.nullspace()
    attempts=0; rows=[]; best=None
    dest=Path(__file__).with_name('G_abelian_only_'+args.configuration+'.json')
    for template_no in range(args.templates):
        while True:
            attempts+=1
            length=rng.randint(3,args.max_length)
            ua,ub,vc=[''.join(rng.choice('abc') for _ in range(length))
                      for _ in range(3)]
            va_counts=[ub.count(a)+vc.count(a)-ua.count(a) for a in 'abc']
            if min(va_counts)<0: continue
            va_letters=[a for a,count in zip('abc',va_counts) for _ in range(count)]
            rng.shuffle(va_letters); va=''.join(va_letters)
            words=[ua,ub,vc,va]
            if len(set(words))<4: continue
            counts=sp.Matrix([[w.count(a) for a in 'abc'] for w in words[:3]])
            determinant=counts.det()
            if not determinant: continue
            vertices,group_rank,_=fold(words)
            if group_rank!=4: continue
            break
        inverse=counts.inv()
        denominator=lcm(*(int(x.q) for x in inverse))
        templates=dict(ua=ua,ub=ub,vc=vc,va=va)
        histogram=Counter(); minimum_edge_ranks=[]
        for trial in range(args.trials):
            perturb=sp.zeros(2*n,1)
            for vec in kernel:
                perturb+=rng.randint(-3,3)*vec
            perturb=[int(x) for x in perturb]
            scale=1
            for a,b,c in edges:
                block=inverse*sp.Matrix([perturb[a],perturb[b],perturb[n+c]])
                scale=max(scale,1+max(abs(x).__ceil__() for x in block))
            lengths=[int(denominator*(scale*length+x)) for x in perturb]
            assert min(lengths)>0
            rank,alphabet,patterns,edge_ranks,point_words,edge_maps=extension.solution(
                lengths,templates,inverse)
            histogram[rank]+=1; minimum_edge_ranks.append(min(edge_ranks))
            key=(rank,min(edge_ranks))
            if best is None or key>(best['rank'],min(best['edge_ranks'])):
                best=dict(template=templates,template_group_rank=group_rank,
                          determinant=int(determinant),rank=rank,expected_rank=expected,
                          alphabet_size=alphabet,edge_ranks=edge_ranks,lengths=lengths,
                          count_patterns=patterns,point_words=point_words,edge_maps=edge_maps)
                print(f'new best rank={rank}/{expected} edge_ranks={edge_ranks} '
                      f'template={templates}',flush=True)
        rows.append(dict(template_number=template_no,template=templates,
                         core_group_rank=group_rank,core_abelian_rank=3,
                         determinant=int(determinant),length=length,
                         rank_histogram=dict(sorted(histogram.items())),
                         minimum_edge_ranks=minimum_edge_ranks))
        print(f'template={template_no} ranks={dict(sorted(histogram.items()))} '
              f'min_edges={minimum_edge_ranks}',flush=True)
        dest.write_text(json.dumps(dict(parameters=vars(args),candidates_tried=attempts,
            configuration=dict(n=n,edges=edges),templates=rows,best=best,
            negative_results_are_only_exploratory=True),indent=2)+'\n')
        if best['rank']==expected and min(best['edge_ranks'])==5:
            print('Finite full-rank lift found, with no original DF group relator.',flush=True)
            break
    print('Finite test only; no claim of extension to all C_delta.',flush=True)


if __name__=='__main__':
    main()
