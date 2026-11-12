"""Independent check of the TOTEX Part C computations (review of TOTEX, Claude Opus 5.5, 12 Nov 2026).

Written from the formulas of TOTEX_paper.tex Part C (Proposition C.1 repair, section "Exact integral
computations") without importing the return's code.  Builds the concrete categories of finite sets and
injections, the quotient functors H = h_V/(c v_a ~ c v_b) (pair) and h_V/(c v_0 ~ c v_1 ~ c v_2) (triple), the
nerves of their categories of elements, and the Betti numbers over F_p for several primes p (equal Betti numbers
for p = 2, 3, 5 and a large prime exclude 2-, 3- and 5-torsion; the return's own unit-elimination certificate is
what proves torsion-freeness).  Also re-verifies the quasi-filter neighbour identities and AKR property (11)
for every quasi-filter built here.

Usage: python -I akr_indep.py [--literal-common-n] [--k2] [--k3crit]
"""
import sys, time
from collections import defaultdict

LITERAL = '--literal-common-n' in sys.argv

class Cat:
    def __init__(self):
        self.size = []; self.name = []; self.hom = defaultdict(set)
    def add(self, name, n):
        x = len(self.size); self.size.append(n); self.name.append(name)
        self.hom[(x, x)].add(tuple(range(n))); return x
    def add_target(self, name, gens, points):
        """gens: list of (source object y, map as tuple of point labels in the new target)."""
        order = sorted(set(points), key=repr)          # same naming rule as the paper's tagged sets
        ix = {p: i for i, p in enumerate(order)}
        z = self.add(name, len(order))
        for y, f in gens:
            fi = tuple(ix[v] for v in f)
            for x in range(z):
                for g in list(self.hom.get((x, y), ())):
                    self.hom[(x, z)].add(tuple(fi[t] for t in g))
        return z, [tuple(ix[v] for v in f) for _, f in gens]

def beta(i, x, m, k):
    """The displayed formula of TOTEX Prop. C.1 / AKR B.5 with s = 4k+1, path of m vertices."""
    if i <= 2 * k:
        return x + i if x + i <= 2 * k else x + i + 2 * k - m + 1
    z = x - i + 6 * k - m + 2
    return z if z > 2 * k else x - i + 4 * k

def quasi_filter(C, name, X, Y, f, g, s, nmin=3):
    k = (s - 1) // 4; assert s == 4 * k + 1
    fixed = {f[a] for a in range(C.size[X]) if f[a] == g[a]}
    edge = {f[a]: g[a] for a in range(C.size[X]) if f[a] != g[a]}
    heads = set(edge.values()); active = set(edge) | heads
    paths = []
    for v in sorted(set(edge) - heads):
        p = [v]
        while p[-1] in edge: p.append(edge[p[-1]])
        paths.append(p)
    assert {v for p in paths for v in p} == active          # no directed cycles
    n = max([nmin] + [len(p) for p in paths])
    if n % 2 == 0: n += 1
    assert k >= n
    coord = {v: (j, t) for j, p in enumerate(paths) for t, v in enumerate(p)}
    gens = []
    for i in range(s):
        img = []
        for v in range(C.size[Y]):
            if v in fixed: img.append(('fixed', v))
            elif v in active:
                j, t = coord[v]; m = n if LITERAL else len(paths[j])
                img.append(('path', j, beta(i, t, m, k)))
            else: img.append(('private', v, i))
        assert len(set(img)) == len(img), 'not injective'
        gens.append((Y, tuple(img)))
    pts = [('fixed', v) for v in fixed] + [('private', v, i) for v in range(C.size[Y]) if v not in fixed | active
                                           for i in range(s)] + [('path', j, t) for j in range(len(paths)) for t in range(s)]
    z, alph = C.add_target(name, gens, pts)
    # neighbour identities: alpha_i g = alpha_{i+1} f (i<2k); alpha_2k g = alpha_2k+1 g; alpha_i f = alpha_{i+1} g (2k<i<4k);
    # alpha_4k f = alpha_0 f; and AKR (11): consecutive images meet exactly in the identified composite image.
    comp = lambda a, h: tuple(a[t] for t in h)
    fail11 = 0
    for i in range(s):
        a, b = alph[i], alph[(i + 1) % s]
        if i < 2 * k: ok = comp(a, g) == comp(b, f); shared = comp(a, g)
        elif i == 2 * k: ok = comp(a, g) == comp(b, g); shared = comp(a, g)
        elif i < 4 * k: ok = comp(a, f) == comp(b, g); shared = comp(a, f)
        else: ok = comp(a, f) == comp(b, f); shared = comp(a, f)
        assert ok, ('neighbour identity fails', name, i)
        if set(a) & set(b) != set(shared): fail11 += 1
    signed = 2 * k - (2 * k - 1)
    return z, alph, fail11, signed

def stage_K1(C):
    V = C.add('V', 1); W = C.add('W', 3)
    for i in range(3): C.hom[(V, W)].add((i,))
    K0 = {(x, y): sorted(fs) for (x, y), fs in C.hom.items()}
    fails = 0
    for (x, y), fs in sorted(K0.items()):
        for i, f in enumerate(fs):
            for j, g in enumerate(fs):
                _, _, fl, sg = quasi_filter(C, f'Q_{x}_{y}_{i}_{j}', x, y, f, g, 45)
                fails += fl; assert sg == 1
    for x in (V, W):
        for y in (V, W):
            C.add_target(f'S_{x}_{y}', [(x, tuple(('L', i) for i in range(C.size[x]))),
                                        (y, tuple(('R', i) for i in range(C.size[y])))],
                         [('L', i) for i in range(C.size[x])] + [('R', i) for i in range(C.size[y])])
    return fails

def check_category(C):
    for (x, y), fs in C.hom.items():
        if x == y: assert fs == {tuple(range(C.size[x]))}, 'non-identity endomorphism'
        for f in fs: assert len(set(f)) == len(f) and all(0 <= v < C.size[y] for v in f)
    for (x, y), fs in list(C.hom.items()):
        for z in range(len(C.size)):
            for g in C.hom.get((y, z), ()):
                for f in fs: assert tuple(g[t] for t in f) in C.hom[(x, z)], 'not closed'

def element_nerve(C, pairs):
    """H = h_V / relation generated by (c v_a, c v_b) for (a,b) in pairs, c in hom(W,x).  V = object 0, W = 1."""
    cls = []
    for x in range(len(C.size)):
        pts = sorted(f[0] for f in C.hom.get((0, x), ()))
        par = {p: p for p in pts}
        def r(p):
            while par[p] != p: par[p] = par[par[p]]; p = par[p]
            return p
        for c in C.hom.get((1, x), ()):
            for a, b in pairs: par[r(c[a])] = r(c[b])
        cls.append({p: r(p) for p in pts})
    verts = [(x, h) for x in range(len(C.size)) for h in sorted(set(cls[x].values()))]
    vid = {v: i for i, v in enumerate(verts)}
    arrows = []; out = defaultdict(list)
    for (x, y), fs in C.hom.items():
        if x == y: continue
        for f in fs:
            for h in sorted(set(cls[x].values())):
                arrows.append((vid[(x, h)], vid[(y, cls[y][f[h]])], x, y, f, h))
                out[vid[(x, h)]].append(len(arrows) - 1)
    aid = {(a[2], a[3], a[4], a[5]): i for i, a in enumerate(arrows)}
    simp = [[(i,) for i in range(len(verts))], [(i,) for i in range(len(arrows))]]
    while True:
        nxt = [c + (j,) for c in simp[-1] for j in out[arrows[c[-1]][1]]]
        if not nxt: break
        simp.append(nxt)
    def compose(i, j):
        _, _, x, y, f, h = arrows[i]; _, _, y2, z, g, _ = arrows[j]; assert y == y2
        return aid[(x, z, tuple(g[t] for t in f), h)]
    index = [{c: n for n, c in enumerate(cs)} for cs in simp]
    bds = [None, {n: {arrows[c[0]][1]: 1, arrows[c[0]][0]: -1} if arrows[c[0]][1] != arrows[c[0]][0] else {}
                  for n, c in enumerate(simp[1])}]
    for d in range(2, len(simp)):
        bd = {}
        for n, c in enumerate(simp[d]):
            col = defaultdict(int)
            col[index[d - 1][c[1:]]] += 1                      # face 0: drop first arrow
            col[index[d - 1][c[:-1]]] += (-1) ** d              # face d: drop last arrow
            for i in range(1, d):                               # inner faces: compose arrows i-1, i
                col[index[d - 1][c[:i - 1] + (compose(c[i - 1], c[i]),) + c[i + 1:]]] += (-1) ** i
            bd[n] = {r: v for r, v in col.items() if v}
        bds.append(bd)
    return [len(s) for s in simp], bds

def rank_mod(bd, p):
    piv = {}; rank = 0
    for col in bd.values():
        v = {r: a % p for r, a in col.items() if a % p}
        while v:
            r = max(v)
            if r in piv:
                a = v[r]; pv = piv[r]
                for t, b in pv.items():
                    nb = (v.get(t, 0) - a * b) % p
                    if nb: v[t] = nb
                    else: v.pop(t, None)
            else:
                inv = pow(v[r], -1, p); piv[r] = {t: (b * inv) % p for t, b in v.items()}; rank += 1; break
    return rank

def betti(counts, bds, p):
    rk = [0] + [rank_mod(bds[d], p) for d in range(1, len(counts))] + [0]
    return [counts[d] - rk[d] - rk[d + 1] for d in range(len(counts))]

def report(C, label, pairs, primes=(2, 3, 5, 1000003)):
    t0 = time.time(); counts, bds = element_nerve(C, pairs)
    for d in range(2, len(bds)):                                # d^2 = 0
        for col in bds[d].values():
            acc = defaultdict(int)
            for r, a in col.items():
                for r2, b in bds[d - 1][r].items(): acc[r2] += a * b
            assert not any(acc.values()), 'd^2 != 0'
    res = {p: betti(counts, bds, p) for p in primes}
    narr = sum(len(v) for v in C.hom.values())
    print(f"{label}: objects {len(C.size)}, arrows {narr}, nerve {counts}, Betti " +
          ", ".join(f"F_{p}: {res[p]}" for p in primes) + f"  [{time.time()-t0:.1f}s]", flush=True)
    return res

if __name__ == '__main__':
    PAIR, TRIPLE = [(0, 1)], [(0, 1), (0, 2)]
    C = Cat(); f11 = stage_K1(C); check_category(C)
    print(('LITERAL common-n' if LITERAL else 'REPAIRED') + f" K1 built: {len(C.size)} objects; quasi-filters failing (11): {f11}")
    report(C, 'K1 pair', PAIR); report(C, 'K1 triple', TRIPLE)
    if '--k2' in sys.argv:
        t = C.name.index('Q_0_1_0_1'); fs = sorted(C.hom[(1, t)]); f, g = fs[:2]
        _, _, fl, _ = quasi_filter(C, 'Q_K2', 1, t, f, g, 153); check_category(C)
        print(f"K2 substage quasi-filter on the first two tuples W -> Q_0_1_0_1 (s=153); fails (11): {fl}")
        report(C, 'K1 + one K2 quasi-filter, pair', PAIR)
    if '--k3crit' in sys.argv:
        left = C.name.index('Q_0_1_0_1'); right = C.name.index('Q_0_1_1_0')
        t, _ = C.add_target('S_K2', [(left, tuple(('L', i) for i in range(C.size[left]))),
                                      (right, tuple(('R', i) for i in range(C.size[right])))],
                            [('L', i) for i in range(C.size[left])] + [('R', i) for i in range(C.size[right])])
        report(C, 'K1 + K2 sum of the two circle targets, pair', PAIR)
        lf = next(iter(C.hom[(left, t)])); rg = next(iter(C.hom[(right, t)]))
        f = tuple(lf[j] for j in sorted(C.hom[(1, left)])[0]); g = tuple(rg[j] for j in sorted(C.hom[(1, right)])[0])
        _, _, fl, _ = quasi_filter(C, 'Q_K3', 1, t, f, g, 297); check_category(C)
        print(f"K3 cross-sum quasi-filter (s=297); fails (11): {fl}")
        report(C, 'K1 + K2 sum + K3 quasi-filter, pair', PAIR, primes=(2, 1000003))
