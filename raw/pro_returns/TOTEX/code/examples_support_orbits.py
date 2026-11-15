#!/usr/bin/env python3
"""Check finite support orbit counts for the final-image obstruction.

For two increasing finite subsets of sizes k,l in Q, an orbit is an
interleaving with possible matches, counted by the Delannoy recurrence.
For r independent ordered-atom sorts the counts multiply. This is an exact
finite check of the one-or-at-least-three obstruction, not a substitute for
the universal least-support argument in the paper.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from functools import lru_cache
from itertools import product
from math import prod
from pathlib import Path
import json

@lru_cache(None)
def orbit_count(k, l):
    if not k or not l:
        return 1
    return orbit_count(k - 1, l) + orbit_count(k, l - 1) + orbit_count(k - 1, l - 1)


def main():
    rows = []
    for r in (1, 2, 3):
        profiles = [p for p in product(range(5), repeat=r) if any(p)]
        disjoint = overlapping = 0
        for p in profiles:
            for q in profiles:
                n = prod(orbit_count(a, b) for a, b in zip(p, q))
                overlap = any(a and b for a, b in zip(p, q))
                assert (n >= 3) if overlap else (n == 1)
                assert n != 2
                if overlap:
                    overlapping += 1
                else:
                    disjoint += 1
        rows.append({'factors': r, 'nonzero_profiles': len(profiles),
                     'profile_pairs': len(profiles)**2,
                     'one_orbit_cases': disjoint,
                     'at_least_three_orbit_cases': overlapping,
                     'two_orbit_cases': 0})
    report = {'support_sizes': list(range(5)), 'cases': rows,
              'single_factor_counts': [[orbit_count(k, l) for l in range(5)] for k in range(5)],
              'all_checks_passed': True}
    out = json.dumps(report, indent=2) + '\n'
    Path(__file__).with_suffix('.out').write_text(out)
    print(out, end='')

if __name__ == '__main__':
    main()
