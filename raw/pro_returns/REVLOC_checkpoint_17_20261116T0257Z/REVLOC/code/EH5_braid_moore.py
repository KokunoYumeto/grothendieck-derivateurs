#!/usr/bin/env python3
"""Integral Salvetti/Moore tensor model: research certificate, not yet a theorem.

Model for D_n^{(2)} M(Z/2,2): the Salvetti complex of the braid
group B_n with its signed permutation action on the tensor Moore
chain complex.  The exact applicability is separately audited.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p))) % 2


def subgroup(n, subset):
    blocks=[]; start=0
    for i in range(n-1):
        if i not in subset:
            blocks.append(tuple(range(start,i+1))); start=i+1
    blocks.append(tuple(range(start,n)))
    out=[]
    for pieces in product(*(list(permutations(b)) for b in blocks)):
        out.append(tuple(x for p in pieces for x in p))
    return out


def act(p, word, inverse=False):
    if inverse:
        p=tuple(p.index(i) for i in range(len(p)))
    out=[0]*len(p)
    for i,x in enumerate(word): out[p[i]]=x
    sign=(-1)**sum(word[i]*word[j] for i in range(len(p))
                  for j in range(i+1,len(p)) if p[i]>p[j])
    return tuple(out),sign


def complex_model(n, inverse=False):
    cells=defaultdict(list)
    for r in range(n):
        for subset in combinations(range(n-1),r):
            for word in product((0,1),repeat=n):
                cells[2*n+sum(word)+r].append((subset,word))
    indices={d:{v:i for i,v in enumerate(vs)} for d,vs in cells.items()}
    matrices={}
    for d,vs in cells.items():
        mat=sp.zeros(len(cells.get(d-1,[])),len(vs))
        for col,(subset,word) in enumerate(vs):
            r=len(subset)
            for jpos,j in enumerate(subset):
                smaller=tuple(k for k in subset if k!=j)
                reps=[p for p in subgroup(n,subset)
                      if all(p[k]<p[k+1] for k in smaller)]
                for p in reps:
                    target,sign=act(p,word,inverse)
                    mat[indices[d-1][(smaller,target)],col]+=(-1)**(jpos+parity(p))*sign
            # Tensor Moore differential, with the total-complex sign.
            for i,x in enumerate(word):
                if x:
                    target=word[:i]+(0,)+word[i+1:]
                    mat[indices[d-1][(subset,target)],col]+=2*(-1)**(r+sum(word[:i]))
        matrices[d]=mat
    return cells,matrices


def gf2_basis(columns):
    piv={}
    for v in columns:
        while v:
            k=v.bit_length()-1
            if k in piv: v^=piv[k]
            else: piv[k]=v;break
    return piv


def mod2_columns(mat):
    return [sum((int(mat[i,j])%2)<<i for i in range(mat.rows)) for j in range(mat.cols)]


def gf2_kernel(mat):
    piv={}; out=[]
    for j,v in enumerate(mod2_columns(mat)):
        w=1<<j
        while v:
            k=v.bit_length()-1
            if k in piv: v^=piv[k][0];w^=piv[k][1]
            else: piv[k]=(v,w);break
        if not v: out.append(w)
    return out


def gf2_reduce(v,piv):
    for k in sorted(piv,reverse=True):
        if (v>>k)&1: v^=piv[k]
    return v


def homology_mod2(cells,ds):
    result={}; reps={}; boundaries={}
    for d in sorted(cells):
        b=gf2_basis(mod2_columns(ds.get(d+1,sp.zeros(len(cells[d]),0))))
        base=dict(b); hs=[]
        for x in gf2_kernel(ds[d]):
            y=gf2_reduce(x,base)
            if y:
                base[y.bit_length()-1]=y;hs.append(x)
        result[d]=len(hs);reps[d]=hs;boundaries[d]=b
    return result,reps,boundaries


def integer_homology(cells,ds):
    out={}
    for d in sorted(cells):
        mat=ds[d]
        if mat.rows and mat.cols:
            diag,left,right=smith_normal_decomp(DomainMatrix.from_Matrix(mat).convert_to(sp.ZZ))
            diag=diag.to_Matrix();right=right.to_Matrix()
            rank=sum(diag[i,i]!=0 for i in range(min(diag.shape)))
        else:
            rank=0;right=sp.eye(mat.cols)
        boundary=right.inv()*ds.get(d+1,sp.zeros(len(cells[d]),0))
        assert boundary[:rank,:]==sp.zeros(rank,boundary.cols)
        boundary=boundary[rank:,:]
        if boundary.rows and boundary.cols:
            diag,_,_=smith_normal_decomp(DomainMatrix.from_Matrix(boundary).convert_to(sp.ZZ))
            diag=diag.to_Matrix()
            invariants=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]]
        else: invariants=[]
        out[d]={"free_rank":boundary.rows-len(invariants),
                "torsion":[x for x in invariants if x>1]}
    return out


def main():
    output={"scope":__doc__,"models":[]}
    for n in (2,4):
        for inv in (False,True):
            cells,ds=complex_model(n,inv)
            failures=[d for d in ds if d-1 in ds and ds[d-1]*ds[d]!=sp.zeros(ds[d-1].rows,ds[d].cols)]
            row={"arity":n,"inverse_action":inv,"d_squared_failures":failures,
                 "chain_ranks":{d:len(vs) for d,vs in sorted(cells.items())}}
            if not failures:
                dims,hs,bds=homology_mod2(cells,ds)
                row["mod2_homology_ranks"]=dims
                row["integral_homology"]=integer_homology(cells,ds)
                row["beta1_ranks"]={}
                for d,reps in hs.items():
                    images=[]
                    for rep in reps:
                        x=sp.Matrix([int((rep>>i)&1) for i in range(len(cells[d]))])
                        y=ds[d]*x
                        assert all(int(z)%2==0 for z in y)
                        v=sum((int(z)//2%2)<<i for i,z in enumerate(y))
                        images.append(gf2_reduce(v,bds.get(d-1,{})))
                    row["beta1_ranks"][d]=len(gf2_basis(images))
            output["models"].append(row)
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
