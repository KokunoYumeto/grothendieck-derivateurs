"""Finite-stage verification of the full symmetric-group telescope in E.4.

T_n has objects 0,...,n and Hom(i,j)=S_{j+1} for i<=j.
Composition is multiplication after extending the earlier permutation.
All finite data through n=3 are verified; the infinite statement is proved.
"""
from itertools import permutations
import json

def identity(n): return tuple(range(n+1))
def extend(p,n): return p+tuple(range(len(p),n+1))
def mul(p,q): return tuple(p[q[i]] for i in range(len(p)))
def shift(p): return (0,)+tuple(x+1 for x in p)
def arrows(n):
    return [(i,j,p) for j in range(n+1) for i in range(j+1)
            for p in permutations(range(j+1))]
def comp(b,a):
    i,j,p=a; jj,k,q=b
    assert j==jj
    return (i,k,mul(q,extend(p,k)))
def collapse(a,m,shifted=False):
    i,j,p=a
    return (m,m,extend(shift(p) if shifted else p,m))
def S(a):
    i,j,p=a
    return (i+1,j+1,shift(p))

out=[]
for n in range(4):
    aa=arrows(n); aset=set(aa)
    outgoing={i:[a for a in aa if a[0]==i] for i in range(n+1)}
    triples=0; pairs=0
    for a in aa:
        i,j,p=a
        assert comp((j,j,identity(j)),a)==a
        assert comp(a,(i,i,identity(i)))==a
        for b in outgoing[j]:
            assert comp(b,a) in aset
            assert S(comp(b,a))==comp(S(b),S(a))
            pairs+=1
            for c in outgoing[b[1]]:
                assert comp(c,comp(b,a))==comp(comp(c,b),a)
                triples+=1
    m=n+1
    larger=set(arrows(m))
    assert {a for a in larger if a[0]<=n and a[1]<=n}==aset
    cycle=tuple(list(range(1,m+1))+[0])
    nat_eq=0
    for a in aa:
        i,j,p=a
        eta_i=(i,m,identity(m)); eta_j=(j,m,identity(m))
        assert comp(collapse(a,m),eta_i)==comp(eta_j,a)
        e_i=(i+1,m,identity(m)); e_j=(j+1,m,identity(m))
        assert comp(collapse(a,m,True),e_i)==comp(e_j,S(a))
        tau=(m,m,cycle)
        assert comp(tau,collapse(a,m))==comp(collapse(a,m,True),tau)
        nat_eq+=3
    out.append(dict(n=n,objects=n+1,arrows=len(aa),composable_pairs=pairs,
                    associativity_triples=triples,naturality_equations=nat_eq,
                    full_inclusion=True,shift_functor=True,
                    id_and_shift_connected_by_three_transformations=True))
print(json.dumps({'finite_stages':out,'status':'PASS',
                  'infinite_conclusion':'proved in E.4, not inferred from finite checks'},indent=2))
