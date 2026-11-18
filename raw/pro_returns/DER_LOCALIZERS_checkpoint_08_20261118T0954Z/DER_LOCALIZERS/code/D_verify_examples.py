#!/usr/bin/env python3
"""Finite certificates for Part D. All arithmetic is exact.

The homology table checks degrees 0--4 only. The proof in D.tex uses
averaging and Mayer--Vietoris to establish all degrees. No bounded
calculation is presented as a proof of an unbounded statement.
"""
from fractions import Fraction
from itertools import product
import json


def rank(a, p=0):
    if not a:
        return 0
    a = [[Fraction(x) if not p else int(x) % p for x in row] for row in a]
    m, n, r = len(a), len(a[0]), 0
    for j in range(n):
        q = next((i for i in range(r, m) if a[i][j]), None)
        if q is None:
            continue
        a[r], a[q] = a[q], a[r]
        inv = 1/a[r][j] if not p else pow(a[r][j], -1, p)
        a[r] = [x*inv if not p else x*inv % p for x in a[r]]
        for i in range(m):
            if i == r or not a[i][j]:
                continue
            factor = a[i][j]
            a[i] = [x-factor*y if not p else (x-factor*y) % p
                    for x,y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


class ConeCategory:
    def __init__(self, ell, cone_points):
        self.ell = ell
        self.objects = tuple(range(cone_points+1))
        self.arrows = [('g', i) for i in range(ell)]
        self.arrows += [('id', i) for i in range(1, cone_points+1)]
        self.arrows += [('c', i) for i in range(1, cone_points+1)]

    def src(self, f):
        return f[1] if f[0] == 'id' else 0

    def tgt(self, f):
        return f[1] if f[0] in ('id', 'c') else 0

    def identity(self, x):
        return ('g', 0) if x == 0 else ('id', x)

    def compose(self, f, g):
        """Return g after f."""
        assert self.tgt(f) == self.src(g)
        if f[0] == g[0] == 'g':
            return ('g', (f[1]+g[1]) % self.ell)
        if g[0] == 'id':
            return f
        if f[0] == 'id':
            return g
        assert f[0] == 'g' and g[0] == 'c'
        return g

    def check(self):
        for f in self.arrows:
            assert self.compose(self.identity(self.src(f)), f) == f
            assert self.compose(f, self.identity(self.tgt(f))) == f
        count = 0
        for f,g,h in product(self.arrows, repeat=3):
            if self.tgt(f) == self.src(g) and self.tgt(g) == self.src(h):
                assert self.compose(self.compose(f,g),h) == self.compose(f,self.compose(g,h))
                count += 1
        return count

    def chains(self, n):
        if n == 0:
            return list(self.objects)
        nonid = [f for f in self.arrows if f != self.identity(self.src(f))]
        if n == 1:
            return [(f,) for f in nonid]
        return [s+(f,) for s in self.chains(n-1) for f in nonid
                if self.tgt(s[-1]) == self.src(f)]

    def boundary(self, n, source, target):
        rows = {s:i for i,s in enumerate(target)}
        a = [[0]*len(source) for _ in target]
        for j,s in enumerate(source):
            if n == 1:
                a[rows[self.tgt(s[0])]][j] += 1
                a[rows[self.src(s[0])]][j] -= 1
                continue
            faces = [s[1:]]
            faces += [s[:i-1]+(self.compose(s[i-1],s[i]),)+s[i+1:] for i in range(1,n)]
            faces += [s[:-1]]
            for i,t in enumerate(faces):
                if all(f != self.identity(self.src(f)) for f in t):
                    a[rows[t]][j] += (-1)**i
        return a

    def homology(self, p):
        chains = [self.chains(n) for n in range(6)]
        matrices = [None]+[self.boundary(n,chains[n],chains[n-1]) for n in range(1,6)]
        for n in range(2,6):
            a,b = matrices[n-1],matrices[n]
            assert all(sum(a[i][k]*b[k][j] for k in range(len(b))) == 0
                       for i in range(len(a)) for j in range(len(chains[n])))
        ranks = [0]+[rank(matrices[n],p) for n in range(1,6)]
        return [len(chains[n])-ranks[n]-ranks[n+1] for n in range(5)]


def matrix_product(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def run():
    print('FINITE CATEGORY AND COCHAIN CERTIFICATES; all calculations exact')
    for ell,p in [(2,0),(2,3),(3,2),(3,5)]:
        assert not p or ell % p
        for cones in [0,1,2]:
            c = ConeCategory(ell,cones)
            triples = c.check()
            h = c.homology(p)
            assert h == [1,0,0,0,0]
            if cones == 2:
                for u in [{0,1},{0,2}]:
                    assert all(c.src(f) in u for f in c.arrows if c.tgt(f) in u)
            print(json.dumps(dict(ell=ell,field='Q' if p==0 else 'F'+str(p),
                                  cone_points=cones,objects=len(c.objects),arrows=len(c.arrows),
                                  associativity_triples=triples,H0_through_H4=h)))
        t = [[int(i == (j+1)%ell) for j in range(ell)] for i in range(ell)]
        diff = [[t[i][j]-int(i==j) for j in range(ell)] for i in range(ell)]
        inv_dim = ell-rank(diff,p)
        assert inv_dim == 1 < ell
        print(f'C_{ell} regular representation: invariant dimension {inv_dim}; fibre dimension {ell}')
    # Authoritative words: x_i^{-1} x_{i+1} x_i x_{i+1}^{-2}.
    relators = ['AbaBB','BcbCC','CdcDD','DadAA']
    letters='abcd'
    matrix=[[sum((1 if x==g else -1 if x==g.upper() else 0) for x in r)
             for r in relators] for g in letters]
    expected=[[0,0,0,-1],[-1,0,0,0],[0,-1,0,0],[0,0,-1,0]]
    assert matrix == expected
    assert rank(matrix)==4
    # Signed permutation determinant.
    import itertools
    det=0
    for perm in itertools.permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term=(-1)**inversions
        for i,j in enumerate(perm): term*=matrix[i][j]
        det+=term
    assert det == -1
    print('Higman presentation boundary C2→C1 =',matrix,'; determinant =',det)
    # In BS(1,2), a(t)=t/2 and b(t)=t+1 satisfy a^-1 b a=b^2.
    a=[[Fraction(1,2),0],[0,1]]; ai=[[2,0],[0,1]]; b=[[1,1],[0,1]]
    assert matrix_product(matrix_product(ai,b),a)==matrix_product(b,b)
    print('BS(1,2) affine normal-form input: a^-1 b a=b^2 verified; b is translation by 1.')
    print('S2 cellular complex: C0=Z, C1=0, C2=Z; H2 over every nonzero field has dimension 1.')
    print('All checks passed. Infinite-order, absence of finite quotients, all-degree acyclicity,')
    print('and absence of finite-dimensional representations are proved symbolically in D.1/D.5/D.7.')


if __name__ == '__main__':
    run()
