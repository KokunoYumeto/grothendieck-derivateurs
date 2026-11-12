"""Independent monoid census for PRETOT Proposition A.14 (Claude Opus 5.5, 12 Nov 2026).

All labelled monoids on {0,...,n-1} with identity 0, n <= 4; all right acts on {0,...,q-1}, q <= 3.
For each connected category of elements: H_1 by my own Smith form, and, when H_1 = 0, pi_1 = 1
certified by my own Todd-Coxeter enumeration over the trivial subgroup (index 1).
Usage: python -I census_indep.py <output_dir>
"""
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE))
from linalg_int import smith_diagonal  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'out'


def monoids(n):
    cells = [(g, f) for g in range(1, n) for f in range(1, n)]
    for vals in product(range(n), repeat=len(cells)):
        T = [[0] * n for _ in range(n)]
        for a in range(n):
            T[0][a] = a
            T[a][0] = a
        for (g, f), v in zip(cells, vals):
            T[g][f] = v
        if all(T[T[a][b]][c] == T[a][T[b][c]] for a in range(1, n) for b in range(1, n) for c in range(1, n)):
            yield T


def coset_enum_trivial(ngen, relators, limit=3000):
    """Todd-Coxeter (HLT) over the trivial subgroup; generators 0..ngen-1, letter x>0 means gen x-1,
    x<0 its inverse.  Returns the index, or None if the limit is reached."""
    cols = 2 * ngen
    col = lambda x: 2 * (x - 1) if x > 0 else 2 * (-x - 1) + 1
    inv = lambda c: c ^ 1
    rels = [[col(x) for x in r] for r in relators if r]
    table = [[None] * cols]
    parent = [0]

    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c

    def merge(a, b, queue):
        a, b = find(a), find(b)
        if a != b:
            a, b = min(a, b), max(a, b)
            parent[b] = a
            queue.append(b)

    def coincidence(a, b):
        queue = []
        merge(a, b, queue)
        while queue:
            e = queue.pop()
            for g in range(cols):
                f = table[e][g]
                if f is None:
                    continue
                table[f][inv(g)] = None
                e1, f1 = find(e), find(f)
                if table[e1][g] is not None:
                    merge(table[e1][g], f1, queue)
                elif table[f1][inv(g)] is not None:
                    merge(table[f1][inv(g)], e1, queue)
                else:
                    table[e1][g] = f1
                    table[f1][inv(g)] = e1

    def define(c, g):
        d = len(table)
        table.append([None] * cols)
        parent.append(d)
        table[c][g] = d
        table[d][inv(g)] = c

    def scan(c, w):
        f, b, i, j = c, c, 0, len(w) - 1
        while True:
            while i <= j and table[f][w[i]] is not None:
                f = table[f][w[i]]
                i += 1
            if i > j:
                if f != b:
                    coincidence(f, b)
                return
            while j >= i and table[b][inv(w[j])] is not None:
                b = table[b][inv(w[j])]
                j -= 1
            if j < i:
                coincidence(f, b)
                return
            if i == j:
                table[f][w[i]] = b
                table[b][inv(w[i])] = f
                return
            define(f, w[i])
    c = 0
    while c < len(table):
        if len(table) > limit:
            return None
        if find(c) == c:
            for w in rels:
                if find(c) != c:
                    break
                scan(c, w)
            if find(c) == c:
                for g in range(cols):
                    if table[c][g] is None:
                        define(c, g)
        c += 1
    return sum(1 for x in range(len(table)) if find(x) == x)


def analyse(T, q, act):
    """act[g] is a tuple: x.g ; arrows (x,g): x.g -> x for g != 0."""
    n = len(T)
    # connectedness
    par = list(range(q))

    def fd(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    arrows = [(x, g) for x in range(q) for g in range(1, n)]
    tree = set()
    for (x, g) in arrows:
        a, b = fd(act[g][x]), fd(x)
        if a != b:
            par[a] = b
            tree.add((x, g))
    if len({fd(x) for x in range(q)}) != 1:
        return None
    gen = {a: i + 1 for i, a in enumerate(a for a in arrows if a not in tree)}
    rel = []
    for (x, g) in arrows:
        for f in range(1, n):
            y = act[g][x]                    # source of (x,g); arrow (y,f): y.f -> y composes before (x,g)
            comp = T[g][f]                   # composite (x, g f)
            word = []
            if (y, f) in gen:
                word.append(gen[(y, f)])
            if (x, g) in gen:
                word.append(gen[(x, g)])
            if comp != 0 and (x, comp) in gen:
                word.append(-gen[(x, comp)])
            rel.append(word)
    ng = len(gen)
    if ng == 0:
        return (True, True)
    M = [[0] * ng for _ in rel]
    for i, w in enumerate(rel):
        for x in w:
            M[i][abs(x) - 1] += 1 if x > 0 else -1
    d = smith_diagonal(M, ng)
    h1_zero = len(d) == ng and all(v == 1 for v in d)
    if not h1_zero:
        return (False, False)
    idx = coset_enum_trivial(ng, rel)
    return (True, idx == 1)


def main():
    lines = []
    total = {}
    for n in range(1, 5):
        row = {'labelled_monoids': 0, 'right_acts': 0, 'connected': 0, 'H1_zero': 0, 'pi1_trivial_certified': 0}
        for T in monoids(n):
            row['labelled_monoids'] += 1
            for q in range(1, 4):
                funcs = list(product(range(q), repeat=q))
                for choice in product(range(len(funcs)), repeat=n - 1):
                    act = [tuple(range(q))] + [funcs[c] for c in choice]
                    # right action: x.(g f) = (x.g).f
                    if not all(act[T[g][f]][x] == act[f][act[g][x]] for g in range(1, n) for f in range(1, n) for x in range(q)):
                        continue
                    row['right_acts'] += 1
                    r = analyse(T, q, act)
                    if r is None:
                        continue
                    row['connected'] += 1
                    if r[0]:
                        row['H1_zero'] += 1
                        if r[1]:
                            row['pi1_trivial_certified'] += 1
        lines.append(f'order {n}: {row}')
        print(lines[-1], flush=True)
        total[n] = row
    expected = {1: (1, 3, 1, 1), 2: (2, 21, 8, 7), 3: (11, 249, 143, 125), 4: (156, 5872, 3856, 3148)}
    for n, (lm, ra, co, h1) in expected.items():
        r = total[n]
        assert (r['labelled_monoids'], r['right_acts'], r['connected'], r['H1_zero']) == (lm, ra, co, h1), n
        assert r['pi1_trivial_certified'] == r['H1_zero'], n
    lines.append('Agrees with the return\'s table (labelled monoids, acts, connected, H1 = 0); every H1 = 0 case has pi_1 = 1 '
                 'certified by coset enumeration of index 1: no acyclic non-simply-connected element category within these bounds.')
    print(lines[-1])
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'census_indep.out').write_text('\n'.join(lines) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
