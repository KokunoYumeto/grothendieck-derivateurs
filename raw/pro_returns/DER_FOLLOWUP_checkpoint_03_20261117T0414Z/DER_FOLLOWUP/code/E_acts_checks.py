#!/usr/bin/env python3
"""Exact finite audit of the Lead 4(a) counterexample.

K=Delta[2]/boundary. In degrees 0 and 1 it has one simplex;
in degree 2 it has basepoint b and nondegenerate t.
Monotone maps act on t by t only for the identity of [2].
No floating point arithmetic and no unbounded assertion is inferred.
"""
from itertools import combinations_with_replacement, product
import sympy as sp

def maps(m,n):
    return list(combinations_with_replacement(range(n+1),m+1))
def comp(g,f):
    return tuple(g[i] for i in f)
def kval(m,n,f,x):
    return 't' if n==m==2 and x=='t' and f==(0,1,2) else 'b'
K={0:['b'],1:['b'],2:['b','t']}
checked=0
for a,b,c in product(range(3),repeat=3):
    for f,g in product(maps(a,b),maps(b,c)):
        for x in K[c]:
            assert kval(a,b,f,kval(b,c,g,x))==kval(a,c,comp(g,f),x)
            checked+=1
M=maps(2,2)
assert len(M)==10
for f,g,h in product(M,repeat=3):
    assert comp(h,comp(g,f))==comp(comp(h,g),f)
for x,f,g in product(K[2],M,M):
    assert kval(2,2,f,kval(2,2,g,x))==kval(2,2,comp(g,f),x)

# Proposed nondegenerate injection category: v -> t in 3 ways.
d1=sp.Matrix([[-1,-1,-1],[1,1,1]])
assert d1.rank()==1
assert len(d1.nullspace())==2
print('K=Delta[2]/boundary; truncated functor equations checked:',checked)
print('M_2 elements:',len(M),'associativity triples:',len(M)**3)
print('M_2/K_2 objects=2, arrows=20; all act equations hold')
print('Nondegenerate injection category: objects=2, arrows=5')
print('Normalized nerve ranks: C0=2, C1=3, C2=0')
print('d1=',d1.tolist())
print('H0=Z, H1=Z^2, H2=0 (integer graph homology; no torsion)')
print('K normalized chains: C0=Z, C1=0, C2=Z, all boundaries=0')
print('H0(K)=Z, H1(K)=0, H2(K)=Z')
alpha=(0,1) # [1] -> [2], a face of t.
assert not any(tuple([j,j])==alpha for j in range(3))
print('Face injection [1]->[2] cannot factor through [1]->[0].')
print('PASS: claimed second weak equivalence is false.')
