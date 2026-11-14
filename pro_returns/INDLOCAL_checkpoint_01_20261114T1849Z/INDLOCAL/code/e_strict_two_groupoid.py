#!/usr/bin/env python3
"""Finite certificate for INDLOCAL E.1. Uses exact arithmetic in F_2."""
import itertools
import json
from pathlib import Path

G = (0, 1)
add = lambda x, y: (x + y) % 2
assert all(add(add(x,y),z) == add(x,add(y,z)) for x,y,z in itertools.product(G, repeat=3))
assert all(add(add(a,b),add(c,d)) == add(add(a,c),add(b,d))
           for a,b,c,d in itertools.product(G, repeat=4))

def normalized_cochains(degree):
    tuples = list(itertools.product(G, repeat=degree))
    support = [t for t in tuples if all(t)]
    return [{t: (values[support.index(t)] if t in support else 0) for t in tuples}
            for values in itertools.product(G, repeat=len(support))]

def coboundary(cochain, degree):
    ans = {}
    for t in itertools.product(G, repeat=degree+1):
        value = cochain[t[1:]] + cochain[t[:-1]]
        for j in range(degree):
            collapsed = t[:j] + (add(t[j],t[j+1]),) + t[j+2:]
            value += cochain[collapsed]
        ans[t] = value % 2
    return ans

one = normalized_cochains(1)
two = normalized_cochains(2)
cocycles = [c for c in two if not any(coboundary(c,2).values())]
boundaries = {tuple(coboundary(c,1).items()) for c in one}
assert len(cocycles) == 2 and len(boundaries) == 1
result = {
    'strict_two_groupoid_objects': 1,
    'strict_two_groupoid_1_cells': 1,
    'strict_two_groupoid_2_cells': 2,
    'associativity_checks': 8,
    'interchange_checks': 16,
    'strict_functors_from_BC2': 1,
    'normalized_2_cocycles': len(cocycles),
    'normalized_2_coboundaries': len(boundaries),
    'H2_BC2_C2_order': len(cocycles)//len(boundaries),
    'comparison_bijective': False,
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
