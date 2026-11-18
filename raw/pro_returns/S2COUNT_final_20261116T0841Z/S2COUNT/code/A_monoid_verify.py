#!/usr/bin/env python3
"""Independent finite checks for the rectangular-band inflation monoids M_r.

No third-party dependencies.  The all-degree proof is in sections/A_agent.tex.
This script checks the finite multiplication law, its integral algebra model,
the split kernel used in the projective resolution, the spherical bar cycles,
and every face identification in the explicit sphere maps through degree 8.
"""
from collections import defaultdict
from itertools import product
import json
from pathlib import Path


def monoid(r):
    names = ['1', 'e', 'x01', 'x10', 'x11'] + [f'y{i+1}' for i in range(r)]
    rc = {1:(0,0), 2:(0,1), 3:(1,0), 4:(1,1)}
    rc.update({5+i:(0,0) for i in range(r)})
    idx = {(0,0):1, (0,1):2, (1,0):3, (1,1):4}
    n = len(names)
    table = [[(j if i == 0 else i if j == 0 else idx[rc[i][0],rc[j][1]])
              for j in range(n)] for i in range(n)]
    return names, table


def add(*xs):
    return tuple(map(sum, zip(*xs)))


def neg(x):
    return tuple(-a for a in x)


def basis(n, i):
    return tuple(int(j == i) for j in range(n))


def mul(table, x, y):
    z = [0]*len(table)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[table[i][j]] += a*b
    return tuple(z)


def boundary(table, chain):
    out = defaultdict(int)
    for word, c in chain.items():
        out[word[1:]] += c
        for i in range(1,len(word)):
            w = word[:i-1]+(table[word[i-1]][word[i]],)+word[i+1:]
            if 0 not in w:  # normalized degeneracies
                out[w] += (-1)**i*c
        out[word[:-1]] += (-1)**len(word)*c
    return {w:c for w,c in out.items() if c}


def face(table, word, i):
    if i == 0:
        return word[1:]
    if i == len(word):
        return word[:-1]
    return word[:i-1]+(table[word[i-1]][word[i]],)+word[i+1:]


def cochain(w, simplex):
    """Primitive integral cocycle dual to b tensor t_w tensor a."""
    return int(simplex[0] in (2,4) and simplex[-1] in (3,4)
               and simplex[1:-1] == tuple(5+j for j in w))


def primitive(left, right, simplex):
    p = len(left)+2
    return int(simplex[0] in (2,4) and simplex[-1] in (3,4)
               and simplex[1:p-1] == tuple(5+j for j in left)
               and simplex[p-1] == 4
               and simplex[p:-1] == tuple(5+j for j in right))


def main():
    records = []
    for r in (0,1,2):
        names, table = monoid(r)
        n = len(names)
        assert all(table[0][a] == a == table[a][0] for a in range(n))
        triples = 0
        for a,b,c in product(range(n),repeat=3):
            assert table[table[a][b]][c] == table[a][table[b][c]]
            triples += 1
        retraction = list(range(5))+[1]*r
        assert all(retraction[table[i][j]] == table[retraction[i]][retraction[j]]
                   for i,j in product(range(n),repeat=2))
        assert all(table[table[i][i]][i] == table[i][i] for i in range(1,n))
        one,e = basis(n,0),basis(n,1)
        u = add(one,neg(e))
        a = add(basis(n,3),neg(e))
        b = add(basis(n,2),neg(e))
        c = add(basis(n,4),neg(basis(n,3)),neg(basis(n,2)),e)
        ts = [add(basis(n,5+j),neg(e)) for j in range(r)]
        B = dict(e=e,u=u,a=a,b=b,c=c,**{f't{i+1}':t for i,t in enumerate(ts)})
        zero = (0,)*n
        expected = {
            ('e','e'):'e',('u','u'):'u',('u','a'):'a',('a','e'):'a',
            ('e','b'):'b',('b','u'):'b',('u','c'):'c',('c','u'):'c',
            ('a','b'):'c'
        }
        for j in range(r):
            t = f't{j+1}'
            expected['u',t] = t
            expected[t,'u'] = t
        for p,q in product(B,repeat=2):
            assert mul(table,B[p],B[q]) == B[expected[p,q]] if (p,q) in expected else mul(table,B[p],B[q]) == zero
        # Explicit integral inverse to the displayed basis: proves unimodularity.
        assert add(e,u) == one
        assert add(e,b) == basis(n,2)
        assert add(e,a) == basis(n,3)
        assert add(e,a,b,c) == basis(n,4)
        for j,t in enumerate(ts):
            assert add(e,t) == basis(n,5+j)
        # Rb is isomorphic to Re by multiplication by b; a and t_j
        # carry the one-dimensional u-simple action.  These certify the kernels.
        for x in B.values():
            assert mul(table,mul(table,x,e),b) == mul(table,x,b)
            for t in ts:
                xu = mul(table,x,u)
                assert mul(table,x,t) == tuple(z*xu[0] for z in t)
            xu = mul(table,x,u)
            assert mul(table,x,a) == tuple(z*xu[0] for z in a)
        sphere_count = 0
        face_count = 0
        cup_count = 0
        cocycle_count = 0
        primitive_count = 0
        degree_counts = {}
        for deg in range(2,9):
            count = 0
            for w in product(range(r),repeat=deg-2):
                choices = [(2,1)] + [(5+j,1) for j in w] + [(3,1)]
                chain = {}
                for bits in product((0,1),repeat=deg):
                    word = tuple(choices[j][bits[j]] for j in range(deg))
                    chain[word] = (-1)**sum(bits)
                    for i in range(deg+1):
                        # In S^1*(S^0)^{*(deg-1)}, faces 0,1 flip bit 0;
                        # face i>=2 flips bit i-1.
                        bit = 0 if i <= 1 else i-1
                        flip = list(bits)
                        flip[bit] ^= 1
                        other = tuple(choices[j][flip[j]] for j in range(deg))
                        assert face(table,word,i) == face(table,other,i)
                        face_count += 1
                assert boundary(table,chain) == {}
                assert sum(cochain(w,s)*coef for s,coef in chain.items()) == 1
                for cut in range(2,deg-1):
                    for left in product(range(r),repeat=cut-2):
                        for right in product(range(r),repeat=deg-cut-2):
                            pairing = sum(cochain(left,s[:cut])*cochain(right,s[cut:])*coef
                                          for s,coef in chain.items())
                            assert pairing == 0
                            cup_count += 1
                # In the relative E-normalized bar, every difference in
                # this chain is exactly b, t_j, or a; its surviving word
                # has coefficient 1.  Distinct w are distinct basis words.
                assert choices[0] == (2,1) and choices[-1] == (3,1)
                count += 1
            degree_counts[deg] = count
            assert count == r**(deg-2)
            sphere_count += count
        for deg in range(2,5):
            for w in product(range(r),repeat=deg-2):
                for simplex in product(range(1,n),repeat=deg+1):
                    val = sum((-1)**i*cochain(w,face(table,simplex,i))
                              for i in range(deg+2))
                    assert val == 0
                    cocycle_count += 1
        for p,q in ((2,2),(2,3),(3,2)):
            for left in product(range(r),repeat=p-2):
                for right in product(range(r),repeat=q-2):
                    for simplex in product(range(1,n),repeat=p+q):
                        value = sum((-1)**i*primitive(left,right,face(table,simplex,i))
                                    for i in range(p+q+1))
                        cup = cochain(left,simplex[:p])*cochain(right,simplex[p:])
                        assert value == (-1)**p*cup
                        primitive_count += 1
        rec = dict(r=r,order=n,names=names,table=table,
                   associativity_triples_checked=triples,
                   integral_ring_basis_and_kernel_checks='PASS',
                   retraction='PASS',sphere_cycles_checked=sphere_count,
                   sphere_face_equalities_checked=face_count,
                   cocycle_coboundaries_checked=cocycle_count,
                   cup_product_pairings_checked=cup_count,
                   explicit_integral_cup_primitives_checked=primitive_count,
                   spherical_generators_by_degree=degree_counts,
                   homology='H0=Z, H1=0, Hn=Z^(r^(n-2)) for n>=2; all-degree proof in paper')
        records.append(rec)
        print(f'M_{r}: {n} elements; {triples} associativity triples; integral ring and resolution kernels PASS')
        print(f'  Retraction PASS; {sphere_count} sphere cycles and {face_count} face equalities PASS')
        print(f'  {cocycle_count} integral cocycle coboundaries and {cup_count} cup pairings PASS')
        print(f'  {primitive_count} explicit integral cup-primitive equations PASS')
        print(f'  Sphere ranks in degrees 2..8: {list(degree_counts.values())}')
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(records,indent=2)+'\n')
    print('All independent checks passed.')


if __name__ == '__main__':
    main()
