"""Exact finite checks for STRATA Part F.

The finite posets here are posets of stratum TYPES, not the infinite
Charney--Lee categories. They verify enumeration and forgetting of labels.
The exit mapping-space counterexample S^2={p} union R^2 has link S^1;
we compute this link's integral cellular homology from a 3-edge circle.
The nonsmooth forgetful counterexample has infinite category BZ;
only its exact exponent kernel, not the whole category, is checked here.
"""
from itertools import combinations
from collections import Counter
import sympy as sp


def canonical_split(part, labels):
    left = frozenset(part)
    right = frozenset(labels) - left
    return tuple(sorted((tuple(sorted(left)), tuple(sorted(right)))))


def stable_splits(labels):
    labels = frozenset(labels)
    return sorted({canonical_split(s, labels)
                   for r in range(2, len(labels)-1)
                   for s in combinations(sorted(labels), r)})


def compatible(a, b):
    return any(not (frozenset(x) & frozenset(y)) for x in a for y in b)


def tree_types(labels):
    splits = stable_splits(labels)
    types = []
    for r in range(len(labels)-2):
        for chosen in combinations(splits, r):
            if all(compatible(a, b) for a, b in combinations(chosen, 2)):
                types.append(frozenset(chosen))
    return types


def forget(tree, label, labels):
    target = frozenset(labels) - {label}
    result = set()
    for split in tree:
        retained = frozenset(split[0]) - {label}
        if len(retained) >= 2 and len(target-retained) >= 2:
            result.add(canonical_split(retained, target))
    return frozenset(result)


def main():
    labels4, labels5 = frozenset(range(1,5)), frozenset(range(1,6))
    t4, t5 = tree_types(labels4), tree_types(labels5)
    assert Counter(map(len,t4)) == Counter({0:1,1:3})
    assert Counter(map(len,t5)) == Counter({0:1,1:10,2:15})
    print('X4 stratum counts by number of nodes:', dict(sorted(Counter(map(len,t4)).items())))
    print('X5 stratum counts by number of nodes:', dict(sorted(Counter(map(len,t5)).items())))
    print('X5 number of strata:', len(t5))
    relations = [(a,b) for a in t5 for b in t5 if a >= b]
    print('X5 EXIT STRATUM POSET comparable ordered pairs including identities:', len(relations))
    assert len(relations) == 81
    assert all(forget(a,5,labels5) >= forget(b,5,labels5) for a,b in relations)
    print('Forgetting 5 preserves all stratum-poset relations: True')
    for target in sorted(t4, key=lambda t:(len(t),str(sorted(t)))):
        fibre = [s for s in t5 if forget(s,5,labels5)==target]
        counts = dict(sorted(Counter(map(len,fibre)).items()))
        print('Stratum fibre over', 'open' if not target else str(sorted(target)), ':', counts)
        assert counts == ({0:1,1:4} if not target else {1:2,2:5})
    circle_d1 = sp.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
    assert circle_d1.rank()==2
    print('Link circle chain groups: C1=Z^3, C0=Z^3; rank(d1)=2')
    print('Link homology: H0=Z, H1=Z, Hk=0 for k>1')
    exponent_map=sp.Matrix([[1,1]])
    ker=exponent_map.nullspace()
    assert ker == [sp.Matrix([-1,1])]
    print('Exact kernel of exponent map Z^2 -> Z, (r,s) -> r+s: Z*(-1,1)')
    print('Thus the outgoing EXIT lifting groupoid in F.11 has stabilizer Z.')
    print('All finite checks passed; no computation substitutes for the tree proof in F.10.')


if __name__ == '__main__':
    main()
