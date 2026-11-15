#!/usr/bin/env python3
"""Check orderability of the repaired AKR beta necklace for monotone pairs.

Each pair is a pair of increasing injections from a finite linear order.
The target has exactly the prescribed repaired points.  Its precedence
graph contains every comparison of adjacent source points in every copy.
Acyclicity is exactly existence of an order making all copies increasing.
"""

from collections import defaultdict, deque
from itertools import combinations
import argparse
import json


def repaired_pair(f, g, target_size, k):
    fixed = {x for x, y in zip(f, g) if x == y}
    successor = {x: y for x, y in zip(f, g) if x != y}
    active = set(successor) | set(successor.values())
    paths = []
    for initial in sorted(set(successor) - set(successor.values())):
        path = [initial]
        while path[-1] in successor:
            path.append(successor[path[-1]])
        paths.append(path)
    assert set(x for path in paths for x in path) == active
    coordinates = {x: (j, t) for j, path in enumerate(paths)
                   for t, x in enumerate(path)}
    max_path = max([len(path) for path in paths] + [1])
    assert k >= max_path
    s = 4 * k + 1

    def beta(i, t, length):
        if i <= 2 * k:
            value = t + i
            return value if value <= 2 * k else value + 2 * k - length + 1
        value = t - i + 6 * k - length + 2
        return value if value > 2 * k else t - i + 4 * k

    copies = []
    vertices = {("fixed", x) for x in fixed}
    for j in range(len(paths)):
        vertices.update(("path", j, t) for t in range(s))
    for i in range(s):
        copy = []
        for x in range(target_size):
            if x in fixed:
                point = ("fixed", x)
            elif x in active:
                j, t = coordinates[x]
                point = ("path", j, beta(i, t, len(paths[j])))
            else:
                point = ("private", x, i)
                vertices.add(point)
            copy.append(point)
        assert len(set(copy)) == target_size
        copies.append(copy)

    witnesses = {}
    outgoing = defaultdict(set)
    indegree = {v: 0 for v in vertices}
    for i, copy in enumerate(copies):
        for x, (left, right) in enumerate(zip(copy, copy[1:])):
            assert left != right
            witnesses.setdefault((left, right), (i, x, x + 1))
            if right not in outgoing[left]:
                outgoing[left].add(right)
                indegree[right] += 1
    queue = deque(v for v, degree in indegree.items() if degree == 0)
    ordering = []
    while queue:
        v = queue.popleft()
        ordering.append(v)
        for w in outgoing[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    if len(ordering) == len(vertices):
        position = {v: i for i, v in enumerate(ordering)}
        assert all(all(position[x] < position[y] for x, y in zip(copy, copy[1:]))
                   for copy in copies)
        return {"orderable": True, "max_path": max_path,
                "paths": paths, "vertices": len(vertices)}

    remaining = {v for v, degree in indegree.items() if degree > 0}
    # Every remaining vertex has a remaining predecessor.  Following one
    # backwards finds a directed cycle, subsequently returned forwards.
    incoming = defaultdict(list)
    for v in remaining:
        for w in outgoing[v] & remaining:
            incoming[w].append(v)
    history, location = [], {}
    v = min(remaining)
    while v not in location:
        location[v] = len(history)
        history.append(v)
        v = min(incoming[v])
    cycle = list(reversed(history[location[v]:]))
    cycle.append(cycle[0])
    comparisons = []
    for left, right in zip(cycle, cycle[1:]):
        assert right in outgoing[left]
        comparisons.append({"from": left, "to": right,
                            "copy_and_source_pair": witnesses[left, right]})
    return {"orderable": False, "max_path": max_path,
            "paths": paths, "vertices": len(vertices),
            "cycle": comparisons}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-target", type=int, default=8)
    parser.add_argument("--all-failures", action="store_true")
    args = parser.parse_args()
    tested = 0
    for target_size in range(1, args.max_target + 1):
        local = 0
        for source_size in range(1, target_size + 1):
            injections = list(combinations(range(target_size), source_size))
            for fi, f in enumerate(injections):
                for g in injections[fi:]:
                    successor = {x: y for x, y in zip(f, g) if x != y}
                    maximum = 1
                    for initial in set(successor) - set(successor.values()):
                        length, current = 1, initial
                        while current in successor:
                            length += 1
                            current = successor[current]
                        maximum = max(maximum, length)
                    n = maximum if maximum % 2 else maximum + 1
                    record = repaired_pair(f, g, target_size, n)
                    tested += 1
                    local += 1
                    if not record["orderable"]:
                        print(json.dumps({"target_size": target_size,
                                          "source_size": source_size,
                                          "f": f, "g": g, "n": n, "k": n,
                                          "record": record}, sort_keys=True), flush=True)
                        for multiplier in (2, 4):
                            larger = repaired_pair(f, g, target_size, multiplier * n)
                            print(json.dumps({"larger_k": multiplier * n,
                                              "record": larger}, sort_keys=True), flush=True)
                        if not args.all_failures:
                            print(f"Stopped after first obstruction; pairs tested={tested}", flush=True)
                            return
        print(f"target size {target_size}: tested {local} unordered monotone pairs; "
              f"cumulative {tested}", flush=True)
    print(f"No obstruction in {tested} unordered monotone pairs.", flush=True)


if __name__ == "__main__":
    main()
