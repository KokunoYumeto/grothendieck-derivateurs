#!/usr/bin/env python3
"""Search for a finite obstruction to the direct positive-prefix lift of DF D.4.

For each ordered triple (a,b,c), the proposed lift asks for nonempty t_e
with u_b=t_e u_a and v_a=t_e v_c. Word lengths would give positive t in
the intersection of the cut spaces of the (a,b) and (a,c) graphs.

Farkas duality: this is impossible iff a nonzero nonnegative vector is a
sum of a circulation on each graph. A MILP searches for such circulations
whose supporting 3-hypergraph has every edge d-closed for delta=2v-3e.
No MILP status is treated as an exact mathematical certificate. Any
candidate is rechecked with exact rational arithmetic below.
"""
from itertools import combinations
from pathlib import Path
import argparse
import json
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp, linprog
from scipy.sparse import coo_matrix
from fractions import Fraction


def build(n):
    edges=list(combinations(range(n),3))
    m=len(edges)
    rr=[]; cc=[]; dd=[]; lo=[]; hi=[]
    def row(terms, lower=-np.inf, upper=np.inf):
        i=len(lo)
        for j,x in terms:
            if x: rr.append(i); cc.append(j); dd.append(float(x))
        lo.append(lower); hi.append(upper)
    # lambda is a circulation on first--third; mu on first--second.
    for graph in (0,1):
        for x in range(n):
            terms=[]
            for j,(a,b,c) in enumerate(edges):
                end=c if graph==0 else b
                coeff=(int(x==end)-int(x==a))
                if coeff: terms.append((graph*m+j, coeff))
            row(terms,0,0)
    for j in range(m):
        row([(j,1),(m+j,1)],0,np.inf)
        for off in (0,m):
            row([(off+j,1),(2*m+j,-1)],-np.inf,0)
            row([(off+j,-1),(2*m+j,-1)],-np.inf,0)
    row([(j,1) for j in range(2*m)],1,np.inf)
    masks=[sum(1<<x for x in e) for e in edges]
    for size in range(4,n+1):
        for subset in combinations(range(n),size):
            mask=sum(1<<x for x in subset)
            terms=[(2*m+j,3) for j,em in enumerate(masks) if em&mask==em]
            if terms: row(terms,-np.inf,2*size-4)
    mat=coo_matrix((dd,(rr,cc)),shape=(len(lo),3*m)).tocsr()
    objective=np.r_[np.zeros(2*m),np.ones(m)]
    integrality=np.r_[np.zeros(2*m,dtype=int),np.ones(m,dtype=int)]
    bounds=Bounds(np.r_[-np.ones(2*m),np.zeros(m)],np.ones(3*m))
    return edges, objective, integrality, bounds, LinearConstraint(mat,lo,hi)


def exact_check(n, edges, lam, mu):
    # Only the displayed rational values are used in the certificate check.
    L=[Fraction(float(x)).limit_denominator(100000) for x in lam]
    U=[Fraction(float(x)).limit_denominator(100000) for x in mu]
    def circulation(vec,which):
        out=[Fraction(0) for _ in range(n)]
        for (a,b,c),w in zip(edges,vec):
            out[a]-=w; out[(c if which==0 else b)]+=w
        return all(x==0 for x in out)
    c=[x+y for x,y in zip(L,U)]
    assert circulation(L,0) and circulation(U,1)
    assert min(c)>=0 and sum(c)>0
    used=[e for e,x,y in zip(edges,L,U) if x or y]
    for size in range(1,n+1):
        for subset in combinations(range(n),size):
            st=set(subset)
            r=sum(set(e)<=st for e in used)
            assert 2*size-3*r>0
            if size>3 and r: assert 2*size-3*r>3
    # An independent primal LP must report infeasibility.
    m=len(used)
    eq=np.zeros((2*m,2*n+m))
    for j,(a,b,c0) in enumerate(used):
        eq[2*j,b]=1; eq[2*j,a]=-1; eq[2*j,2*n+j]=-1
        eq[2*j+1,n+a]=1; eq[2*j+1,n+c0]=-1; eq[2*j+1,2*n+j]=-1
    primal=linprog(np.zeros(2*n+m),A_eq=eq,b_eq=np.zeros(2*m),
        bounds=[(None,None)]*(2*n)+[(1,None)]*m,method='highs')
    assert primal.status==2, primal.message
    return {'n':n,'edges':[[x+1 for x in e] for e in used],
            'lambda':[str(x) for x,y in zip(L,U) if x or y],
            'mu':[str(y) for x,y in zip(L,U) if x or y],
            'sum':[str(x+y) for x,y in zip(L,U) if x or y],
            'exact_check':'PASS', 'primal_status':'infeasible'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--n',type=int,nargs='+',default=[8,9,10])
    ap.add_argument('--seconds',type=float,default=20)
    ap.add_argument('--explicit',action='store_true',help='Check the hand-constructed eleven-vertex certificate only')
    args=ap.parse_args()
    if args.explicit:
        edges=[(0,1,8),(1,2,9),(2,3,10),(0,3,4),(4,5,6),(6,7,8)]
        lam=[-1,0,0,1,1,1]
        mu=[1,1,1,-1,0,0]
        cert=exact_check(11,edges,lam,mu)
        print(json.dumps(cert,indent=2),flush=True)
        print('All 2047 nonempty vertex subsets have positive predimension.',flush=True)
        print('All six hyperedges are d-closed: every strict superset has predimension > 3.',flush=True)
        print('Exact dual identity: t_1 + t_2 + t_4 + t_5 = 0 (edge indices start at zero).',flush=True)
        print('Hence every nonnegative length solution kills those four edge parameters.',flush=True)
        Path(__file__).with_name('G_positive_lift_n11.json').write_text(json.dumps(cert,indent=2)+'\n')
        return
    for n in args.n:
        edges,obj,integ,bnd,cons=build(n)
        print(f'n={n}, triples={len(edges)}, constraints={cons.A.shape[0]}',flush=True)
        ans=milp(obj,integrality=integ,bounds=bnd,constraints=cons,
                 options={'time_limit':args.seconds,'mip_rel_gap':0})
        print(f'MILP status {ans.status}: {ans.message}',flush=True)
        if ans.x is not None:
            m=len(edges)
            cert=exact_check(n,edges,ans.x[:m],ans.x[m:2*m])
            print(json.dumps(cert,indent=2),flush=True)
            out=Path(__file__).with_name(f'G_positive_lift_n{n}.json')
            out.write_text(json.dumps(cert,indent=2)+'\n')

if __name__=='__main__': main()
