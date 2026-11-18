"""Search ordered loose-cycle suffix systems; finite experiment only."""

import json
import random
from pathlib import Path

from CD_suffix_length_search import (
    kernel, length_vector, subgroup_rank, universal_words, validate,
)

rng = random.Random(2026111702)
abstract = [(0, 1, 2), (2, 3, 4), (4, 5, 6), (0, 6, 7)]
seen = set()
failures = []
attempted = 0
rank_histogram = {}
while len(seen) < 600:
    permutation = list(range(8))
    rng.shuffle(permutation)
    edges = tuple(sorted(tuple(sorted(permutation[x] for x in e)) for e in abstract))
    if edges in seen:
        continue
    seen.add(edges)
    assert len(validate(8, edges)) == 4
    kbasis = kernel(8, edges)
    best, attempts = -1, []
    for trial in range(8):
        lengths = length_vector(8, edges, kbasis, rng, 20)
        u, v, t, size = universal_words(lengths, edges)
        rank = subgroup_rank(u + v)
        assert rank <= 12
        rank_histogram[rank] = rank_histogram.get(rank, 0) + 1
        attempts.append(dict(rank=rank, lengths=lengths))
        best = max(best, rank)
        if rank == 12:
            break
    if best < 12:
        failures.append(dict(edges=edges, best_rank=best, attempts=attempts))
    if len(seen) % 100 == 0:
        print(f"{len(seen)} distinct ordered loose four-cycles; "
              f"{len(failures)} without full-rank solution so far", flush=True)

result = dict(objects=len(seen), failures=failures, trial_rank_histogram=rank_histogram)
Path("DER_FOLLOWUP_work/code/outputs/CD_suffix_order_search.json").write_text(
    json.dumps(result, indent=2) + "\n")
print("trial rank histogram:", rank_histogram)
print("No finite search result is a proof of existence for all objects or of functorial compatibility.")
