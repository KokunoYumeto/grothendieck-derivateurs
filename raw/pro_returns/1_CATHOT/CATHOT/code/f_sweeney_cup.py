#!/usr/bin/env python3
"""Exact small rational bar-cochain calculation for Sweeney Example 5.2.
The five listed elements are nonidentity arrows of the six-element monoid.
This is a diagnostic, not a homotopy-type classification.
"""
from itertools import product
from pathlib import Path
import sympy as sp
T=[[0,1,0,1,0],[0,1,0,1,0],[2,3,2,3,2],[2,3,2,3,2],[0,1,0,1,0]]

def d(n):
    src=list(product(range(5),repeat=n)); tar=list(product(range(5),repeat=n+1))
    ix={w:i for i,w in enumerate(src)}
    mat=sp.zeros(len(tar),len(src))
    for i,w in enumerate(tar):
        mat[i,ix[w[1:]]]+=1
        for j in range(n):
            v=w[:j]+(T[w[j]][w[j+1]],)+w[j+2:]
            mat[i,ix[v]]+=(-1)**(j+1)
        mat[i,ix[w[:-1]]]+=(-1)**(n+1)
    return mat,src,tar

def main():
    assert all(T[T[a][b]][c]==T[a][T[b][c]] for a,b,c in product(range(5),repeat=3))
    d1,_,_=d(1); d2,words2,_=d(2); d3,_,words4=d(3)
    assert d2*d1==sp.zeros(125,5)
    assert d3*d2==sp.zeros(625,25)
    basis=d1.columnspace(); rank=len(basis)
    phi=None
    for v in d2.nullspace():
        if sp.Matrix.hstack(*basis,v).rank()>rank:
            phi=v;break
    assert phi is not None
    q={w:phi[i] for i,w in enumerate(words2)}
    cup=sp.Matrix([q[w[:2]]*q[w[2:]] for w in words4])
    rank3=d3.rank(); rankaug=d3.row_join(cup).rank()
    lines=[f'Sweeney Example 5.2 semigroup associativity: 125 triples PASS.',f'd1 rank={d1.rank()}, d2 rank={d2.rank()}, dim H2={25-d2.rank()-d1.rank()}.',f'Chosen rational H2 cocycle (word:value nonzero): {[(w,str(q[w])) for w in words2 if q[w]]}',f'd3 rank={rank3}; augmented d3|phi^2 rank={rankaug}.',f'Rational H2 cup square is {"zero" if rankaug==rank3 else "nonzero"}.','No conclusion about homotopy type or cardinality of [BM,S2] follows from this computation alone.']
    out='\n'.join(lines)+'\n';print(out,end='');Path(__file__).with_suffix('.out').write_text(out)
if __name__=='__main__':main()
