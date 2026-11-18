#!/usr/bin/env python3
"""Finite nonnegative invariant-measure feasibility, independently exact-checked."""
from scipy.sparse import load_npz
from scipy.optimize import linprog
from fractions import Fraction
from pathlib import Path
import json, time
out={}
for n in (4,5):
    a=load_npz(f'FREX/verification/ordered_poset_n{n}.npz')
    b=[1]+[0]*(a.shape[0]-1)
    t=time.time()
    sol=linprog([0]*a.shape[1],A_eq=a,b_eq=b,bounds=(0,None),method='highs')
    report={'n':n,'status':int(sol.status),'message':sol.message,
            'elapsed_seconds':time.time()-t}
    if sol.success:
        v=[Fraction(float(x)).limit_denominator(1000000) for x in sol.x]
        ok=all(sum((int(a.data[j])*v[int(a.indices[j])] for j in range(a.indptr[i],a.indptr[i+1])),Fraction(0))==b[i] for i in range(a.shape[0]))
        report['exact_check']=ok
    else:
        # y b < 0 and A^T y >= 0 forbids A x=b, x>=0.
        norm=[(-1,-1)]+[(None,None)]*(a.shape[0]-1)
        dual=linprog([0]*a.shape[0],A_ub=-a.T,b_ub=[0]*a.shape[1],bounds=norm,method='highs')
        report['dual_status']=int(dual.status)
        if dual.success:
            v=[Fraction(float(x)).limit_denominator(1000000) for x in dual.x]
            residual=[Fraction(0)]*a.shape[1]
            for i,c in enumerate(v):
                if not c:continue
                for j in range(a.indptr[i],a.indptr[i+1]):
                    residual[int(a.indices[j])]+=c*int(a.data[j])
            ok=v[0]==-1 and min(residual)>=0
            report['exact_farkas']=ok
            report['support_size']=sum(bool(c) for c in v)
            Path(f'FREX/verification/ordered_poset_positive_n{n}_certificate.json').write_text(json.dumps({str(i):str(c) for i,c in enumerate(v) if c},indent=2))
    print(report,flush=True);out[n]=report
    if sol.status==2 and report.get('exact_farkas'):break
Path('FREX/verification/ordered_poset_positive_report.json').write_text(json.dumps(out,indent=2))

