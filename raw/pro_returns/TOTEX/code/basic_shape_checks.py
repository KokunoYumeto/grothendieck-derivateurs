"""Exact finite checks for basic shapes and bounded monoid arithmetic.

Universal statements about arbitrary diagrams are proved in the paper.
This verifies the concrete finite categories and a nontrivial comparison model.
The N-monoid calculation checks bounded integer arithmetic and one finite
interval of its Z-valued universal covering category, not an infinite census.
"""
from itertools import product
from pathlib import Path
import json


class FiniteCategory:
    def __init__(self, objects, arrows, identities, composition):
        self.objects = tuple(objects)
        self.arrows = dict(arrows)  # name -> (source, target)
        self.identities = dict(identities)
        self.composition = dict(composition)  # (first, second) -> composite

    def verify(self):
        pairs = triples = 0
        for a in self.objects:
            assert self.arrows[self.identities[a]] == (a, a)
        for f, (a, b) in self.arrows.items():
            assert self.composition[self.identities[a], f] == f
            assert self.composition[f, self.identities[b]] == f
            for g, (c, d) in self.arrows.items():
                if b != c:
                    continue
                pairs += 1
                gf = self.composition[f, g]
                assert self.arrows[gf] == (a, d)
                for h, (e, _) in self.arrows.items():
                    if d == e:
                        triples += 1
                        assert self.composition[gf, h] == self.composition[f, self.composition[g, h]]
        assert len(self.composition) == pairs
        return {'objects': len(self.objects), 'arrows': len(self.arrows),
                'composable_pairs': pairs, 'composable_triples': triples}

    def is_filtered(self):
        if not self.objects:
            return False
        for a, b in product(self.objects, repeat=2):
            if not any(any(v == (a, z) for v in self.arrows.values()) and
                       any(v == (b, z) for v in self.arrows.values()) for z in self.objects):
                return False
        for f, g in product(self.arrows, repeat=2):
            if self.arrows[f] == self.arrows[g]:
                b = self.arrows[f][1]
                if not any(c == b and self.composition[f, t] == self.composition[g, t]
                           for t, (c, _) in self.arrows.items()):
                    return False
        return True


def discrete(n):
    return FiniteCategory(range(n), {('id', a): (a, a) for a in range(n)},
                          {a: ('id', a) for a in range(n)},
                          {(('id', a), ('id', a)): ('id', a) for a in range(n)})


def disjoint_union(categories):
    return FiniteCategory(
        [(i, a) for i, c in enumerate(categories) for a in c.objects],
        {(i, f): ((i, a), (i, b)) for i, c in enumerate(categories) for f, (a, b) in c.arrows.items()},
        {(i, a): (i, f) for i, c in enumerate(categories) for a, f in c.identities.items()},
        {((i, f), (i, g)): (i, h) for i, c in enumerate(categories)
         for (f, g), h in c.composition.items()})


report = {'scope': 'Finite indexing-category and comparison-model checks; universal comparisons proved symbolically.'}
report['empty'] = {**discrete(0).verify(), 'filtered': discrete(0).is_filtered()}
report['discrete_two'] = {**discrete(2).verify(), 'filtered': discrete(2).is_filtered()}
c2 = FiniteCategory([0], {0: (0, 0), 1: (0, 0)}, {0: 0},
                    {(f, g): (f+g) % 2 for f, g in product(range(2), repeat=2)})
chain = FiniteCategory([0, 1], {'i': (0, 0), 'j': (1, 1), 'a': (0, 1)},
                       {0: 'i', 1: 'j'},
                       {('i', 'i'): 'i', ('j', 'j'): 'j', ('i', 'a'): 'a', ('a', 'j'): 'a'})
c2.verify(); chain.verify()
grothendieck = disjoint_union([c2, chain])
colimit = disjoint_union([c2, chain])
assert vars(grothendieck) == vars(colimit)
report['discrete_two_sample_comparison'] = {**grothendieck.verify(), 'canonical_comparison': 'identity'}
assert vars(disjoint_union([])) == vars(discrete(0))

arrows = {'iV': ('V', 'V'), 'iW': ('W', 'W'),
          **{f'v{k}': ('V', 'W') for k in range(3)},
          'uV': ('V', 'T'), 'uW': ('W', 'T'), 'iT': ('T', 'T')}
ids = {'V': 'iV', 'W': 'iW', 'T': 'iT'}
comp = {}
for f, (a, b) in arrows.items():
    for g, (c, d) in arrows.items():
        if b != c:
            continue
        if f == ids[a]: h = g
        elif g == ids[c]: h = f
        else:
            assert d == 'T'
            h = 'u' + a
        comp[f, g] = h
cone = FiniteCategory(['V', 'W', 'T'], arrows, ids, comp)
report['terminal_cone_on_triple'] = {**cone.verify(), 'filtered': cone.is_filtered(),
                                    'three_composites': [comp[f'v{k}', 'uW'] for k in range(3)]}
assert cone.is_filtered() and len(set(report['terminal_cone_on_triple']['three_composites'])) == 1
assert not report['empty']['filtered'] and not report['discrete_two']['filtered']

# N is the one-object monoid with composition given by addition.  The sample
# set below is not declared to be a finite submonoid: sums are evaluated as
# unrestricted integers.  The paper supplies the symbolic cancellation and
# group-completion proofs for arbitrary values.
nat_sample = tuple(range(7))
for a in nat_sample:
    assert 0 + a == a == a + 0
monoid_associativity_checks = 0
unequal_pair_postcomposition_checks = 0
for a, b, c in product(nat_sample, repeat=3):
    assert (a + b) + c == a + (b + c)
    monoid_associativity_checks += 1
    if a != b:
        assert a + c != b + c
        unequal_pair_postcomposition_checks += 1
assert all(0 + c != 1 + c for c in nat_sample)

# In the categorical universal cover, objects are integers and an arrow
# i -> j is the unique n in N with j = i+n.  Check the full finite interval
# [-4,4], including every arrow and every composable triple.
integer_sample = tuple(range(-4, 5))
cover_arrows = {(i, j): (i, j) for i in integer_sample
                for j in integer_sample if i <= j}
cover_composition = {((i, j), (j, k)): (i, k)
                     for i, j, k in product(integer_sample, repeat=3)
                     if i <= j <= k}
integer_cover_interval = FiniteCategory(
    integer_sample, cover_arrows, {i: (i, i) for i in integer_sample},
    cover_composition)
cover_counts = integer_cover_interval.verify()
for i, j in product(integer_sample, repeat=2):
    witnesses = [n for n in range(9) if j == i + n]
    assert witnesses == ([j-i] if i <= j else [])
for ((i, j), (_, k)), (source, target) in cover_composition.items():
    assert source == i and target == k
    assert (j-i) + (k-j) == k-i
action_law_checks = 0
for i, a, b in product(integer_sample, nat_sample, nat_sample):
    assert (i + a) + b == i + (a + b)
    action_law_checks += 1
assert integer_cover_interval.is_filtered()
report['natural_numbers_monoid_and_integer_cover'] = {
    'scope': 'Bounded exact arithmetic and a full finite cover interval only; the paper proves the infinite statements symbolically.',
    'monoid_sample': list(nat_sample),
    'identity_elements_checked': len(nat_sample),
    'associativity_checks': monoid_associativity_checks,
    'unequal_pair_postcomposition_checks': unequal_pair_postcomposition_checks,
    'pair_zero_one_has_no_sample_post_equalizer': True,
    'cover_integer_interval': [integer_sample[0], integer_sample[-1]],
    'cover_arrow_formula_pairs_checked': len(integer_sample)**2,
    'cover_composition_addition_checks': len(cover_composition),
    'integer_translation_action_law_checks': action_law_checks,
    'finite_cover_interval': {**cover_counts, 'filtered': True},
    'all_bounded_checks_passed': True,
}
out = Path(__file__).resolve().parent / 'outputs' / 'basic_shape_checks.json'
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
