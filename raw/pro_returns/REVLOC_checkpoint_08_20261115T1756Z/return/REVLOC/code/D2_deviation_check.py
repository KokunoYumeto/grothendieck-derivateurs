#!/usr/bin/env python3
"""Exact F_2 source calculation for the binary-deviation obstruction.

This checks the nine-dimensional source calculation, not the topological
existence of a deviation or the target identities. Those are proved in the
paper. H^*(K(F_2,2);F_2)=F_2[u_2,v_3,w_5,t_9,...]; only these four
generators occur in the degrees used. Steenrod squares below follow from
Sq^1 u=v, Sq^2 v=w, Sq^4 w=t, instability, Adem, and Cartan.
"""
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path

DEGREES = (2, 3, 5, 9)
NAMES = ("u", "v", "w", "t")
ZERO = (0, 0, 0, 0)

def mon(*powers):
    return tuple(powers)

GEN_SQ = (
    {0: mon(1,0,0,0), 1: mon(0,1,0,0), 2: mon(2,0,0,0)},
    {0: mon(0,1,0,0), 2: mon(0,0,1,0), 3: mon(0,2,0,0)},
    {0: mon(0,0,1,0), 1: mon(0,2,0,0), 4: mon(0,0,0,1),
     5: mon(0,0,2,0)},
    {0: mon(0,0,0,1), 1: mon(0,0,2,0)},
)

def parity(items):
    return frozenset(k for k, n in Counter(items).items() if n % 2)

def multiply_monomials(a, b):
    return tuple(x + y for x, y in zip(a, b))

@lru_cache(None)
def square_monomial(a, degree):
    if degree < 0:
        return frozenset()
    if degree == 0:
        return frozenset((a,))
    if a == ZERO:
        return frozenset()
    index = next(i for i, n in enumerate(a) if n)
    if index == 3 and degree > 2:
        raise ValueError("Only Sq^1 and Sq^2 on t are specified or needed")
    rest = list(a)
    rest[index] -= 1
    return parity(
        multiply_monomials(value, other)
        for k, value in GEN_SQ[index].items() if k <= degree
        for other in square_monomial(tuple(rest), degree - k)
    )

def square_tensor(poly, degree):
    return parity(
        (left, right)
        for a, b in poly for k in range(degree + 1)
        for left in square_monomial(a, k)
        for right in square_monomial(b, degree - k)
    )

def basis(n):
    result = []
    def rec(index, remain, powers):
        if index == len(DEGREES):
            if remain == 0:
                result.append(tuple(powers))
            return
        for e in range(remain // DEGREES[index] + 1):
            rec(index + 1, remain - e * DEGREES[index], powers + [e])
    rec(0, n, [])
    return result

def fmt_mon(a):
    return " ".join(name if e == 1 else f"{name}^{e}"
                    for name, e in zip(NAMES, a) if e) or "1"

def fmt(poly):
    return sorted(f"{fmt_mon(a)} tensor {fmt_mon(b)}" for a, b in poly)

def main():
    source = [(a,b) for d in range(1,8)
              for a in basis(d) for b in basis(8-d)]
    assert len(source) == 9
    middle = (mon(2,0,0,0), mon(2,0,0,0))
    survivors = []
    for mask in range(1 << len(source)):
        z = frozenset(a for i,a in enumerate(source) if mask & (1 << i))
        if middle not in z:
            continue
        if square_tensor(z,2):
            continue
        if square_tensor(square_tensor(z,1),2):
            continue
        survivors.append(z)
    assert len(survivors) == 1
    z, = survivors
    assert not square_tensor(z,1)
    third = square_tensor(square_tensor(z,4),2)
    sixth = square_tensor(z,6)
    assert third == sixth
    detecting = (mon(0,0,1,0), mon(0,0,0,1))
    assert detecting in third
    result = {
        "field": "F_2",
        "source_basis_degree_8": fmt(source),
        "all_vectors_checked": 1 << len(source),
        "vectors_with_middle_coefficient_1": 1 << (len(source)-1),
        "survivors_of_Sq2_and_Sq2Sq1": len(survivors),
        "unique_survivor": fmt(z),
        "Sq1_survivor": fmt(square_tensor(z,1)),
        "Sq2Sq4_survivor_equals_Sq6": third == sixth,
        "Sq2Sq4_survivor": fmt(third),
        "coefficient_w_tensor_t": int(detecting in third),
        "survivors_of_all_three_constraints": 0,
        "scope": "Source Steenrod algebra only; topological hypotheses proved separately."
    }
    destination = Path(__file__).parent / "outputs" / "D2_deviation_check.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
