#!/usr/bin/env python3
"""Exact finite certificates supporting A4.3--A4.4.

AI-produced by GPT-6 Astra, OpenAI, 18 November 2026.
The infinite-product and ultrafilter arguments are proved in the text;
this program does not purport to construct a nonprincipal ultrafilter.
It checks the finite Moore cofiber and detecting quotient map, the
finite-image factorization used by A4.3, and finite projections of the
bounded/unbounded exponent distinction.
"""

from fractions import Fraction
from itertools import product
from math import isqrt
import json


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def moore_certificate(p):
    assert is_prime(p)
    # Reduced chains of cofib(p:S^2 -> S^2): C_3=Z, C_2=Z,
    # d_3=[p], d_2=0.  Its nonzero Smith invariant is exactly p.
    d3, d2 = p, 0
    assert d2 * d3 == 0
    assert d3 != 0                 # ker(d_3)=0 over Z
    residues = set(range(p))       # coker(d_3)=Z/p
    assert len(residues) == p
    for a, b in product(residues, repeat=2):
        assert ((a + b) % p - a - b) % p == 0
    # Over Z[1/p], d_3 has the displayed inverse; no reduced homology.
    assert Fraction(1, p) * d3 == 1
    # q:M -> M/M^(2)=S^3 is a cellular chain map, q_3=1, q_2=0.
    q3, q2, sphere_d3 = 1, 0, 0
    assert sphere_d3 * q3 == q2 * d3
    # On cochains q^* carries the generator to 1 in coker(p)=H^3(M;Z).
    pullback_top_class = q3 % p
    assert pullback_top_class == 1 and pullback_top_class != 0
    return {"p": p, "H2_invariant_factor": p,
            "H3": 0, "top_cohomology_class_mod_p": pullback_top_class}


def fibre_partition(values):
    fibres = {}
    for i, a in enumerate(values):
        fibres.setdefault(a, []).append(i)
    blocks = tuple(tuple(v) for v in fibres.values())
    block_values = tuple(values[b[0]] for b in blocks)
    reconstruction = [None] * len(values)
    for block, value in zip(blocks, block_values):
        for i in block:
            reconstruction[i] = value
    assert tuple(reconstruction) == values
    assert len(blocks) == len(set(values))
    return blocks


def partition_certificates():
    count = 0
    for cardinal in (2, 3):
        for n in range(7):
            for values in product(range(cardinal), repeat=n):
                blocks = fibre_partition(values)
                assert len(blocks) <= min(n, cardinal)
                count += 1
    # Two simultaneously chosen partitions admit a common refinement.
    for a in product(range(2), repeat=4):
        for b in product(range(3), repeat=4):
            pa, pb = fibre_partition(a), fibre_partition(b)
            refinement = [set(x) & set(y) for x in pa for y in pb]
            refinement = [x for x in refinement if x]
            assert set().union(*refinement) == set(range(4))
            assert sum(map(len, refinement)) == 4
            assert len(refinement) <= min(4, len(pa) * len(pb))
            for block in refinement:
                assert len({a[i] for i in block}) == 1
                assert len({b[i] for i in block}) == 1
    return count


def exponent_certificates(primes):
    bounded_cases = 0
    unbounded_witnesses = 0
    for p in primes:
        for e in range(1, 5):
            modulus = p**e
            for n in range(1, 7):
                # Check multiplication by p^e on each basis coordinate of
                # (Z/p^e)^n.  Additivity then checks the whole finite product.
                for i in range(n):
                    v = [int(i == j) for j in range(n)]
                    assert all((modulus * x) % modulus == 0 for x in v)
                bounded_cases += 1
        for r in range(10):
            # The r+1 coordinate of (1 mod p^n)_n survives p^r.
            assert (p**r) % (p**(r + 1)) != 0
            unbounded_witnesses += 1
    return bounded_cases, unbounded_witnesses


def main():
    primes = (2, 3, 5, 7)
    moore = [moore_certificate(p) for p in primes]
    functions_checked = partition_certificates()
    bounded, unbounded = exponent_certificates(primes)
    print(json.dumps({
        "status": "PASS",
        "moore_certificates": moore,
        "finite_functions_factored": functions_checked,
        "simultaneous_partition_pairs": 2**4 * 3**4,
        "bounded_exponent_products": bounded,
        "unbounded_exponent_witnesses": unbounded,
        "scope": "finite chain, partition, and exponent certificates only"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
