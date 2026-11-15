"""Exact set-coequalizer diagnostics for a component-transition path.

The input path size here is deliberately not assumed bounded by the
point-level n. This investigates the separate component-injectivity
obligation; it does not assert that these long paths occur in C.1.
"""

import json


def necklace(k, length):
    s = 4 * k + 1
    parent = list(range(s * length))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def join(x, y):
        x, y = root(x), root(y)
        if x != y:
            parent[y] = x
    for i in range(s):
        left, right = ((1, 0) if i < 2 * k else
                       ((1, 1) if i == 2 * k else
                        ((0, 1) if i < 4 * k else (0, 0))))
        for t in range(length - 1):
            join(i * length + t + left,
                 ((i + 1) % s) * length + t + right)
    classes = [root(x) for x in range(s * length)]
    maps = [classes[i * length:(i + 1) * length] for i in range(s)]
    injective = [len(set(f)) == len(f) for f in maps]
    return {'k': k, 's': s, 'path_vertices': length,
            'quotient_points': len(set(classes)),
            'all_copies_injective': all(injective),
            'injective_copies': sum(injective),
            'copy_zero_fiber_sizes': sorted([maps[0].count(v) for v in set(maps[0])])}


def main():
    data = []
    for k in (1, 2, 3, 5, 11):
        rows = [necklace(k, length) for length in range(2, 4 * k + 5)]
        first_failure = next((row['path_vertices'] for row in rows
                              if not row['all_copies_injective']), None)
        data.append({'k': k, 's': 4 * k + 1,
                     'first_noninjective_path_size': first_failure,
                     'rows': rows})
    print(json.dumps({'scope': 'Finite exact set-colimit diagnostics only; occurrence among generated component maps is not asserted.',
                      'calculations': data}, indent=2))


if __name__ == '__main__':
    main()
