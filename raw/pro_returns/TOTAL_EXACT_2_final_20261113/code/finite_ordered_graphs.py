"""Exact finite search for affine equalizers in ordered induced graph embeddings.

Targets are all labelled graphs on [n], with the labels fixing the linear
order. Source p is either one vertex (all three maps to the increasing
induced path q) or one edge (the two edge maps to q). Gaussian elimination
is exact over Q, F2, F3. Finite results are NOT totality claims.
"""
import argparse, json, math, random, time
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def matrix_audit(columns, dimension, prime=None, certificate=False):
    """Return ranks and one affine kernel vector if it exists.

    Eliminate columns of D, retaining the augmentation as a last coordinate.
    In coefficient-tracking mode preserve an exact expression in originals.
    """
    basis={}; witness=None
    count=len(columns)
    for j,column in enumerate(columns):
        if prime is None:
            v=list(map(Fraction,column)); w=Fraction(1)
            comb=[Fraction(int(j==k)) for k in range(count)] if certificate else None
        else:
            v=[x%prime for x in column]; w=1
            comb=[int(j==k) for k in range(count)] if certificate else None
        for pivot,(b,bw,bc) in basis.items():
            factor=v[pivot]
            if not factor: continue
            if prime is None:
                v=[x-factor*y for x,y in zip(v,b)]; w-=factor*bw
                if certificate: comb=[x-factor*y for x,y in zip(comb,bc)]
            else:
                v=[(x-factor*y)%prime for x,y in zip(v,b)]; w=(w-factor*bw)%prime
                if certificate: comb=[(x-factor*y)%prime for x,y in zip(comb,bc)]
        pivot=next((i for i,x in enumerate(v) if x),None)
        if pivot is None:
            if w and witness is None:
                if certificate:
                    inv=1/w if prime is None else pow(w,-1,prime)
                    witness=[x*inv for x in comb] if prime is None else [(x*inv)%prime for x in comb]
                else: witness=True
            continue
        factor=v[pivot]
        inv=1/factor if prime is None else pow(factor,-1,prime)
        if prime is None:
            v=[x*inv for x in v]; w*=inv
            if certificate: comb=[x*inv for x in comb]
        else:
            v=[(x*inv)%prime for x in v]; w=w*inv%prime
            if certificate: comb=[x*inv%prime for x in comb]
        basis[pivot]=(v,w,comb)
        # insertion order need not be sorted: each stored column has zero in
        # every earlier pivot, which suffices for this elimination order.
    rank=len(basis)
    if certificate and witness is not None:
        sums=[sum(c*x for c,x in zip(witness,row)) for row in zip(*columns)]
        if prime is None:
            assert all(x==0 for x in sums) and sum(witness)==1
        else:
            assert all(x%prime==0 for x in sums) and sum(witness)%prime==1
    return rank,rank+int(witness is not None),witness


def data_for_n(n):
    edges=tuple(combinations(range(n),2)); index={e:i for i,e in enumerate(edges)}
    triples=[]
    for a,b,c in combinations(range(n),3):
        req=(1<<index[a,b]) | (1<<index[b,c]); no=1<<index[a,c]
        v=[0]*(2*n);v[a]-=1;v[b]+=1;v[n+a]-=1;v[n+c]+=1
        e=[0]*len(edges);e[index[a,b]]-=1;e[index[b,c]]+=1
        triples.append(((a,b,c),req,no,v,e))
    return edges,triples


def certificate_record(n,mask,edges,paths,kind,prime):
    cols=[x[3] if kind=='triple_vertices' else x[4] for x in paths]
    dimension=2*n if kind=='triple_vertices' else len(edges)
    r,ra,w=matrix_audit(cols,dimension,prime,True)
    assert w is not None
    rec={'n':n,'mask':mask,'edges':[list(e) for i,e in enumerate(edges) if mask>>i&1],
         'kind':kind,'field':'Q' if prime is None else f'F_{prime}',
         'rank_D':r,'rank_D_augmented':ra,
         'support':[{'path':list(p[0]),'coefficient':str(c)} for p,c in zip(paths,w) if c]}
    if prime is None:
        denominator=math.lcm(*(x.denominator for x in w))
        ints=[int(x*denominator) for x in w]
        rec['integral_annihilator_augmentation']=denominator
        rec['integral_coefficients']=ints
    return rec


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-n',type=int,default=6)
    ap.add_argument('--random-n',type=int,default=0);ap.add_argument('--samples',type=int,default=0)
    ap.add_argument('--output',default='finite_ordered_graphs_results.json')
    args=ap.parse_args(); start=time.time(); results=[]; first={}; totals={}
    rng=random.Random(20261113)
    ns=list(range(1,args.max_n+1))
    if args.random_n: ns.append(args.random_n)
    for n in ns:
        edges,templates=data_for_n(n)
        exhaustive=(not args.random_n or n!=args.random_n)
        masks=range(1<<len(edges)) if exhaustive else [rng.getrandbits(len(edges)) for _ in range(args.samples)]
        stats={'n':n,'exhaustive':exhaustive,'graphs':len(masks),'graphs_with_path':0,
               'path_embeddings':0,'max_paths':0,'affine_equalizer_counts':{},'rank_pairs':{}}
        for kind in ['triple_vertices','pair_edges']:
            for field in ['Q','F_2','F_3']:
                stats['affine_equalizer_counts'][kind+':'+field]=0
                stats['rank_pairs'][kind+':'+field]={}
        for mask in masks:
            paths=[p for p in templates if mask&p[1]==p[1] and not mask&p[2]]
            if paths: stats['graphs_with_path']+=1
            stats['path_embeddings']+=len(paths);stats['max_paths']=max(stats['max_paths'],len(paths))
            for kind in ['triple_vertices','pair_edges']:
                cols=[p[3] if kind=='triple_vertices' else p[4] for p in paths]
                dimension=2*n if kind=='triple_vertices' else len(edges)
                for prime in [None,2,3]:
                    key=kind+':'+('Q' if prime is None else f'F_{prime}')
                    r,ra,w=matrix_audit(cols,dimension,prime)
                    rankkey=f'{r}/{ra}'
                    stats['rank_pairs'][key][rankkey]=stats['rank_pairs'][key].get(rankkey,0)+1
                    if w is not None:
                        stats['affine_equalizer_counts'][key]+=1
                        if key not in first:
                            first[key]=certificate_record(n,mask,edges,paths,kind,prime)
                            print('FIRST',json.dumps(first[key]),flush=True)
        results.append(stats)
        print('STAGE',json.dumps(stats),flush=True)
        Path(args.output).write_text(json.dumps({'results':results,'first_certificates':first,'elapsed_seconds':time.time()-start},indent=2))
    print('ELAPSED_SECONDS',round(time.time()-start,3),flush=True)

if __name__=='__main__': main()
