"""Exact beat-point audit of the corrected relative simplex cylinder.

Construct the categorical Dwyer pushout as a poset, then record every
deleted point and its unique comparison witness.  The proof of each
deletion is checked as an actual monotone retraction.
"""
from itertools import combinations
from pathlib import Path
import json


def flags(vertices):
    faces = [frozenset(a) for size in range(1, len(vertices) + 1)
             for a in combinations(vertices, size)]
    result = []

    def visit(chain):
        result.append(frozenset(chain))
        for face in faces:
            if chain[-1] < face:
                visit(chain + [face])

    for face in faces:
        visit([face])
    return result


def encode(flag):
    return sorted([sorted(face) for face in flag], key=lambda a: (len(a), a))


def quotient(n):
    all_flags = flags(tuple(range(n + 2)))
    top = frozenset(range(n + 1))

    def projection(flag):
        return frozenset(frozenset(n if v == n + 1 else v for v in face)
                         for face in flag)

    def image(flag):
        projected = projection(flag)
        return ('b', projected) if max(projected, key=len) != top else ('i', flag)

    objects = list(dict.fromkeys(image(c) for c in all_flags))
    ids = {c: i for i, c in enumerate(objects)}
    count = len(objects)
    le = [[i == j for j in range(count)] for i in range(count)]
    for c in all_flags:
        for d in all_flags:
            if c <= d:
                le[ids[image(c)]][ids[image(d)]] = True
    for k in range(count):
        for i in range(count):
            if le[i][k]:
                for j in range(count):
                    le[i][j] = le[i][j] or le[k][j]
    assert all(not (le[i][j] and le[j][i]) for i in range(count)
               for j in range(i))
    return objects, le


def dismantle(n):
    objects, le = quotient(n)
    current = list(range(len(objects)))
    certificate = []
    while True:
        chosen = None
        for x in current:
            below = [y for y in current if y != x and le[y][x]]
            above = [y for y in current if y != x and le[x][y]]
            for direction, candidates in [('down', below), ('up', above)]:
                for y in candidates:
                    condition = (all(le[z][y] for z in below) if direction == 'down'
                                 else all(le[y][z] for z in above))
                    if condition:
                        chosen = x, y, direction
                        break
                if chosen:
                    break
            if chosen:
                break
        if chosen is None:
            break
        x, y, direction = chosen
        retract = {z: y if z == x else z for z in current}
        # Verify the exact retraction and its pointwise natural transformation.
        assert all(le[retract[a]][retract[b]] for a in current for b in current
                   if le[a][b])
        assert all(retract[retract[a]] == retract[a] for a in current)
        assert all(le[retract[a]][a] if direction == 'down' else le[a][retract[a]]
                   for a in current)
        certificate.append({'point': x, 'image': y, 'direction': direction})
        current.remove(x)
    # Exhaustively verify there is no remaining beat point.
    for x in current:
        below = [y for y in current if y != x and le[y][x]]
        above = [y for y in current if y != x and le[x][y]]
        assert not any(all(le[z][y] for z in below) for y in below)
        assert not any(all(le[y][z] for z in above) for y in above)
    return {
        'dimension': n,
        'initial_objects': len(objects),
        'deletions': len(certificate),
        'core_objects': len(current),
        'strongly_contractible': len(current) == 1,
        'core': [[i, objects[i][0], encode(objects[i][1])] for i in current],
        'certificate': certificate,
    }


def flag_sweep(n):
    """Verify the dimension-uniform formula, for this finite dimension."""
    objects, le = quotient(n)
    ids = {c: i for i, c in enumerate(objects)}
    all_flags = flags(tuple(range(n + 2)))
    faces = sorted(set().union(*all_flags), key=lambda a: (len(a), tuple(sorted(a))))
    top = frozenset(range(n + 1))

    def project(flag):
        return frozenset(frozenset(n if v == n + 1 else v for v in face)
                         for face in flag)

    def image(flag):
        projected = project(flag)
        key = ('b', projected) if max(projected, key=len) != top else ('i', flag)
        return ids[key]

    current = {s: s for s in faces}

    def stage(changes=None):
        result = {}
        for c in all_flags:
            out = frozenset(t for s in c
                            for t in ((current[s], changes[s]) if changes and s in changes
                                      else (current[s],)))
            assert all(a <= b or b <= a for a in out for b in out)
            assert project(out) == project(c)
            key, value = image(c), image(out)
            assert key not in result or result[key] == value
            result[key] = value
        values = [result[i] for i in range(len(objects))]
        assert all(le[values[a]][values[b]] for a in range(len(objects))
                   for b in range(len(objects)) if le[a][b])
        assert all(values[a] == a for a, (tag, _) in enumerate(objects) if tag == 'b')
        return values

    stages = [stage()]
    for inserting, sizes in [(True, range(n + 2, 0, -1)), (False, range(1, n + 3))]:
        for size in sizes:
            changes = {s: (current[s] | {n} if inserting else current[s] - {n + 1})
                       for s in faces if len(s) == size and n + 1 in s}
            stages.append(stage(changes))
            current.update(changes)
            stages.append(stage())
    assert stages[0] == list(range(len(objects)))
    assert all(le[stages[t][a]][stages[t + 1][a]] if t % 2 == 0
               else le[stages[t + 1][a]][stages[t][a]]
               for t in range(len(stages) - 1) for a in range(len(objects)))
    factor = []
    contraction = []
    for tag, flag in objects:
        rf = flag if tag == 'b' else project(flag)
        factor.append(image(rf))
        contraction.append(image(rf | {top}))
    assert stages[-1] == factor
    point = image(frozenset([top]))
    assert all(le[factor[a]][contraction[a]] and le[point][contraction[a]]
               for a in range(len(objects)))
    return {'relative_sweep_steps': len(stages) - 1,
            'full_contraction_steps': len(stages) + 1,
            'contraction_point': point}


if __name__ == '__main__':
    data = [dismantle(n) for n in (1, 2)]
    for row in data:
        row.update(flag_sweep(row['dimension']))
    Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps([{key: value for key, value in row.items()
                       if key not in ('certificate', 'core')} for row in data], indent=2))
