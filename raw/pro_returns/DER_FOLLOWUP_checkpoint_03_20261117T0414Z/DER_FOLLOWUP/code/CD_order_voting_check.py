"""Finite audit of the elementary decisive-set step in the order lemma.

Enumerates odd Boolean rules for m<=3, normalizes unanimity, and checks
all independent coordinate orders on three alternatives. Only the m
coordinate projections survive. Also checks the four-region table.
AI-produced, GPT-6 Astra, ChatGPT Pro, 17 November 2026.
"""

from itertools import permutations, product

orders = tuple(permutations(range(3)))


def before(order, a, b):
    return order.index(a) < order.index(b)


table = {(1, 1): (0, 1, 2), (1, 0): (2, 0, 1),
         (0, 1): (1, 2, 0), (0, 0): (2, 1, 0)}
for (a, d), order in table.items():
    assert before(order, 0, 1) == bool(a)
    assert before(order, 1, 2) == bool(d)
    assert before(order, 0, 2) == bool(a and d)
print("all four membership regions of the decisive-intersection table checked")

for m in range(1, 4):
    full = (1 << m) - 1
    pairs = [(mask, full ^ mask) for mask in range(1 << m)
             if mask < (full ^ mask)]
    survivors = []
    tested = 0
    for bits in product((False, True), repeat=len(pairs)):
        rule = {}
        for (mask, complement), value in zip(pairs, bits):
            rule[mask] = value
            rule[complement] = not value
        if not rule[full]:
            continue
        tested += 1
        good = True
        for profile in product(orders, repeat=m):
            relation = {}
            for a, b in permutations(range(3), 2):
                mask = sum((1 << i) for i, order in enumerate(profile)
                           if before(order, a, b))
                relation[a, b] = rule[mask]
            if any(relation[a, b] and relation[b, c] and not relation[a, c]
                   for a, b, c in permutations(range(3))):
                good = False
                break
        if good:
            matching = [i for i in range(m)
                        if all(rule[mask] == bool(mask & (1 << i))
                               for mask in range(1 << m))]
            assert len(matching) == 1
            survivors.append(matching[0])
    assert sorted(survivors) == list(range(m))
    print(f"m={m}: {tested} normalized odd rules; all {6**m} coordinate "
          f"order profiles tested for survivors; exactly {m} coordinate projections")
print("Finite certificate supplements the general ultrafilter proof.")
