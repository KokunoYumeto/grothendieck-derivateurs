"""Exact finite audit of the conditional mean in A:ordered-vector-amenability.

The general proof is symbolic.  This exhausts the smallest nontrivial
case P=F2, Q=F2^2, V=F2^3, with three independent colours and a point
mass on the increasing three-colour pattern. No floating point is used.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product

points=tuple(range(1,8))
embeddings=tuple((x,y,x^y) for x in points for y in points if y!=x)
assert len(embeddings)==42
extensions={(i,u):tuple(g for g in embeddings if g[i]==u)
            for i in range(3) for u in points}
assert {len(v) for v in extensions.values()}=={6}
sums=defaultdict(int)
squares=defaultdict(int)
counts=defaultdict(int)
total_weight=0
for colouring in product(range(3),repeat=7):
    weights={g:int(tuple(colouring[x-1] for x in g)==(0,1,2))
             for g in embeddings}
    total_weight+=sum(weights.values())
    for i in range(3):
        for u in points:
            value=sum(weights[g] for g in extensions[i,u])
            key=(i,u,colouring[u-1])
            sums[key]+=value
            squares[key]+=value*value
            counts[key]+=1
for (i,u,colour),count in counts.items():
    mean=Fraction(sums[i,u,colour],count)
    expected=Fraction(6,3**2)*int(colour==i)
    assert mean==expected
    variance=Fraction(squares[i,u,colour],count)-mean*mean
    assert variance<=6**2*Fraction((4-2)**2,8-2)
assert Fraction(total_weight,3**7)==Fraction(42,3**3)
for i in range(3):
    for u in points:
        for g in extensions[i,u]:
            bad=sum(set(g).intersection(h)!={u} for h in extensions[i,u])
            assert Fraction(bad,6)<=Fraction((4-2)**2,8-2)
print('PASS: all 2,187 colourings; 63 conditional means and variances')
print('PASS: all 126 fixed-extension collision bounds')
print('E(total weight) =',Fraction(total_weight,3**7))
print('The general n-dimensional Reiter conclusion is proved in A.17.')
