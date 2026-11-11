#!/usr/bin/env python3
"""Finite checks supporting Part F; infinite arguments are proved in F.tex.
No finite check below purports to decide an infinite homotopy claim.
"""
from itertools import permutations, product
from pathlib import Path

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)
def pad(p,n): return tuple(p)+tuple(range(len(p),n))

def main():
    lines=[]
    total=0
    for m in range(0,7):
        # sigma supported on {0,...,m}; c=(0 1 ... m+1).
        n=m+2
        c=tuple(range(1,n))+(0,)
        for sigma0 in permutations(range(m+1)):
            sigma=pad(sigma0,n)
            shifted=(0,)+tuple(sigma0[i]+1 for i in range(m+1))
            assert compose(compose(c,sigma),inv(c))==shifted
            total+=1
    lines.append(f'Shift-conjugacy formula: {total} permutations checked, support sizes 1..7; PASS.')
    # The one-object category BC2: arrows 0=e,1=g, composition addition mod2.
    for a,b,c in product(range(2),repeat=3):
        assert ((a+b)%2+c)%2==(a+(b+c)%2)%2
    for a in range(2): assert (a+0)%2==a and (0+a)%2==a
    lines.append('BC2: one object, two arrows, composition (a+b) mod 2; identities and all 8 associativity triples PASS.')
    # Every normalized nondegenerate n-simplex is (g,...,g).
    for n in range(1,10):
        simplex=(1,)*n
        faces=[simplex[1:]]+[simplex[:i]+((simplex[i]+simplex[i+1])%2,)+simplex[i+2:] for i in range(n-1)]+[simplex[:-1]]
        surviving=[f for f in faces if 0 not in f]
        coeff=len(surviving)%2
        assert coeff==0
        lines.append(f'BC2 normalized F2 boundary in degree {n}: 0 (chain rank 1).')
    lines.append('Symbolic proof applies in every degree: internal faces contain e; the two endpoint faces cancel mod2.')
    lines.append('Telescope alternating cocycle congruences b0 = sum_{j=0}^{N} 2^j a_j modulo 2^(N+1):')
    for N in [1,3,5,7,11,15]:
        modulus=2**(N+1)
        residue=sum(2**j for j in range(N+1) if j%2==0)
        assert (3*residue+1)%modulus==0
        lines.append(f'N={N}: b0 = {residue} (mod {modulus}); 3*b0+1 = 0 modulo {modulus}.')
    lines.append('These finite congruences individually have solutions. The infinite incompatibility with an integer b0 is proved in F.tex.')
    output='\n'.join(lines)+'\n'
    print(output,end='')
    Path(__file__).with_suffix('.out').write_text(output)
if __name__=='__main__': main()
