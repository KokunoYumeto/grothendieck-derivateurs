#!/usr/bin/env python3
"""Exhaust all complete antisymmetric sign rules through four coordinates.

Test transitivity on every strict three-alternative coordinate profile.
The surviving rules must be exactly the signed coordinate projections.
The manuscript gives the general finite-ultrafilter proof separately.
"""
from itertools import permutations, product


def profiles(n):
    result=set()
    for ranks in product(tuple(permutations(range(3))),repeat=n):
        masks=[]
        for a,b in ((0,1),(1,2),(0,2)):
            masks.append(sum((1<<i) for i,r in enumerate(ranks) if r[a]<r[b]))
        result.add(tuple(masks))
    return result


for n in range(1,5):
    full=(1<<n)-1
    representatives=[a for a in range(1<<n) if a<(a^full)]
    tested=0
    valid=[]
    tests=profiles(n)
    for choices in product((False,True),repeat=len(representatives)):
        rule=[False]*(1<<n)
        for a,wins in zip(representatives,choices):
            rule[a]=wins
            rule[a^full]=not wins
        tested+=1
        # Every ordered triple is represented among the profiles; checking
        # x<y and y<z => x<z consequently checks every orientation.
        if all(not (rule[a] and rule[b]) or rule[c] for a,b,c in tests):
            valid.append(tuple(rule))
    expected={tuple(bool(a&(1<<i))^negative for a in range(1<<n))
              for i in range(n) for negative in (False,True)}
    assert set(valid)==expected
    print(f'n={n}: rules={tested}, strict-three-alternative profiles={len(tests)}, '
          f'transitive={len(valid)}=2*n; PASS')
print('General theorem uses the written ultrafilter argument, not extrapolation.')
