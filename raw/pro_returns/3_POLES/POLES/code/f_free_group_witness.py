"""Finite quotient certificate for the free-group endomorphism in POLES F.8.

F=<x,y>; alpha(x)=x; alpha(y)=y*x*y*x^-1*y^-1.
Permutation multiplication p*q means p after q.  The infinite free-group
argument is supplied in the paper; this checks the entire six-arrow target
category and the two different homomorphisms which agree after alpha.
"""
from itertools import permutations, product
import json

S3 = tuple(permutations(range(3)))
identity = (0, 1, 2)

def mul(p, q):
    return tuple(p[q[i]] for i in range(3))

def inv(p):
    return tuple(p.index(i) for i in range(3))

assert all(mul(p, q) in S3 for p, q in product(S3, repeat=2))
assert all(mul(mul(p,q),r) == mul(p,mul(q,r))
           for p,q,r in product(S3, repeat=3))
assert all(mul(identity,p)==p==mul(p,identity) for p in S3)
assert all(mul(p,inv(p))==identity==mul(inv(p),p) for p in S3)

x12 = (1, 0, 2)
y13 = (2, 1, 0)
alpha = {'x': ('x',), 'y': ('y','x','y','X','Y')}
h0 = {'x': x12, 'y': x12}
h1 = {'x': x12, 'y': y13}

def evaluate(word, assignment):
    ans = identity
    for letter in word:
        value = assignment[letter.lower()]
        if letter.isupper():
            value = inv(value)
        ans = mul(ans, value)
    return ans

composites = [{g:evaluate(alpha[g],h) for g in ('x','y')}
              for h in (h0,h1)]
assert h0 != h1
assert composites[0] == composites[1]
exponent_columns = [[sum(1 if z==g else -1 if z==g.upper() else 0
                         for z in alpha[source])
                     for g in ('x','y')]
                    for source in ('x','y')]
assert exponent_columns == [[1,0],[0,1]]

def orbits(generators):
    remaining = set(range(3))
    answer = []
    moves = tuple(generators) + tuple(inv(g) for g in generators)
    while remaining:
        orbit = {min(remaining)}
        while True:
            enlarged = orbit | {p[i] for p in moves for i in orbit}
            if enlarged == orbit:
                break
            orbit = enlarged
        answer.append(sorted(i+1 for i in orbit))
        remaining -= orbit
    return answer

original_orbits = orbits(tuple(h1.values()))
pullback_orbits = orbits(tuple(composites[1].values()))
assert original_orbits == [[1,2,3]]
assert pullback_orbits == [[1,2],[3]]
print(json.dumps({
    'category_BS3': {'objects':1,'arrows':len(S3),
                    'associativity_triples_checked':len(S3)**3,
                    'identity_and_inverses':'verified'},
    'permutation_convention':'zero-indexed tuples; p*q = p after q',
    'alpha_words':alpha,
    'abelianization_columns':exponent_columns,
    'h0':h0,'h1':h1,
    'h0_after_alpha':composites[0],
    'h1_after_alpha':composites[1],
    'different_homomorphisms_with_equal_restrictions':True,
    'action_groupoid_original_orbits':original_orbits,
    'action_groupoid_pullback_along_alpha_orbits':pullback_orbits,
    'conclusion':'alpha is not surjective; its abelianization is the identity'
}, indent=2))
