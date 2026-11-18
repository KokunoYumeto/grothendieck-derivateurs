#!/usr/bin/env python3
"""Exact combinatorial data; numerical feasibility, followed by rational check.

Finite truncation of invariant signed measures on linear extensions of the
generic independently ordered poset. Ground order is the vertex order.
No finite truncation certifies the infinite assertion.
"""
from itertools import product, permutations
from fractions import Fraction
from pathlib import Path
import argparse, json, time
import numpy as np
from scipy.sparse import coo_matrix, save_npz
from scipy.optimize import linprog


def posets(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for signs in product(range(3),repeat=len(pairs)):
        rows=[0]*n
        for (i,j),s in zip(pairs,signs):
            if s==1: rows[i]|=1<<j
            elif s==2: rows[j]|=1<<i
        good=True
        for i in range(n):
            out=rows[i]
            for j in range(n):
                if out>>j&1 and (rows[j]&~out):
                    good=False;break
            if not good:break
        if good:yield tuple(rows)


def restrict_rows(rows,keep):
    return tuple(sum(((rows[i]>>j)&1)<<jj for jj,j in enumerate(keep)) for i in keep)


def extensions(rows):
    n=len(rows)
    for perm in permutations(range(n)):
        done=0;good=True
        for i in perm:
            if rows[i]&done:good=False;break
            done|=1<<i
        if good:yield perm


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=4)
    ap.add_argument('--out',default='ordered_poset_signed');args=ap.parse_args()
    start=time.time();indices={};by_n=[];exts={};count=0
    for n in range(args.n+1):
        ps=list(posets(n));by_n.append(ps)
        for rows in ps:
            ee=list(extensions(rows));exts[(n,rows)]=ee
            for perm in ee:indices[(n,rows,perm)]=count;count+=1
        print(f'n={n}: posets={len(ps)} cumulative variables={count}',flush=True)
    rr=[0];cc=[indices[(0,(),())]];dd=[1];rhs=[1];equation_keys=[('normalization',)]
    for n in range(1,args.n+1):
        for rows in by_n[n]:
            for omit in range(n):
                keep=[i for i in range(n) if i!=omit]
                small=restrict_rows(rows,keep)
                grouped={p:[] for p in exts[(n-1,small)]}
                for perm in exts[(n,rows)]:
                    p=tuple(i-(i>omit) for i in perm if i!=omit)
                    grouped[p].append(indices[(n,rows,perm)])
                for p,large_indices in grouped.items():
                    eq=len(rhs);rhs.append(0);equation_keys.append((n,rows,omit,p))
                    rr.append(eq);cc.append(indices[(n-1,small,p)]);dd.append(-1)
                    for j in large_indices:rr.append(eq);cc.append(j);dd.append(1)
    mat=coo_matrix((dd,(rr,cc)),shape=(len(rhs),count)).tocsr()
    print(f'equations={len(rhs)} nonzeros={mat.nnz}',flush=True)
    result=linprog(np.zeros(count),A_eq=mat,b_eq=np.array(rhs,dtype=float),bounds=(None,None),method='highs')
    report={'n':args.n,'posets':[len(x) for x in by_n],'variables':count,
            'equations':len(rhs),'nonzeros':int(mat.nnz),'status':int(result.status),
            'message':result.message,'elapsed_seconds':time.time()-start}
    out=Path(args.out);out.parent.mkdir(parents=True,exist_ok=True)
    save_npz(str(out)+'.npz',mat)
    if result.success:
        rational=[Fraction(float(x)).limit_denominator(1000000) for x in result.x]
        residual=[]
        for eq in range(mat.shape[0]):
            total=sum((int(mat.data[j])*rational[int(mat.indices[j])] for j in range(mat.indptr[eq],mat.indptr[eq+1])),Fraction(0))
            if total!=rhs[eq]:residual.append((eq,str(total-rhs[eq])))
        report['rational_residual_count']=len(residual)
        report['rational_residual_examples']=residual[:10]
        report['nonzero_weights']=sum(bool(x) for x in rational)
        report['max_abs_weight']=str(max(map(abs,rational)))
        report['denominators']=sorted({x.denominator for x in rational})
        samples=[]
        for key,i in indices.items():
            if key[0]<=3:samples.append({'n':key[0],'rows':key[1],'extension':key[2],'weight':str(rational[i])})
        report['small_weights']=samples
        with open(str(out)+'_weights.json','w') as f:json.dump([str(x) for x in rational],f)
    else:
        # A Farkas multiplier y has A^T y=0 and y_0=1. The primal
        # normalization b=e_0 then makes y^T b=1, certifying inconsistency.
        dual_rhs=np.zeros(count+1);dual_rhs[-1]=1
        from scipy.sparse import vstack
        norm=coo_matrix(([1],([0],[0])),shape=(1,len(rhs))).tocsr()
        dual=vstack([mat.T,norm]).tocsr()
        cert=linprog(np.zeros(len(rhs)),A_eq=dual,b_eq=dual_rhs,bounds=(None,None),method='highs')
        report['dual_status']=int(cert.status)
        if cert.success:
            rat=[Fraction(float(x)).limit_denominator(1000000) for x in cert.x]
            res=[Fraction(0) for _ in range(count)]
            for eq,v in enumerate(rat):
                if not v:continue
                for j in range(mat.indptr[eq],mat.indptr[eq+1]):res[int(mat.indices[j])]+=int(mat.data[j])*v
            ok=all(x==0 for x in res) and rat[0]==1
            report['exact_farkas_certificate']=ok
            support=[{'equation':i,'key':equation_keys[i],'multiplier':str(v)} for i,v in enumerate(rat) if v]
            report['certificate_support_size']=len(support)
            with open(str(out)+'_certificate.json','w') as f:json.dump(support,f,indent=2)
    with open(str(out)+'_report.json','w') as f:json.dump(report,f,indent=2)
    print(json.dumps({k:v for k,v in report.items() if k!='small_weights'},indent=2))


if __name__=='__main__':main()
