# Own checks for the TOTASPH review (Claude Fable 5.2, 12 Nov 2026).
# (1) the n = 2 affine cone in Delta_inj printed in the return's output: augmentation 1, all three cofaces equal,
#     hence (by the argument of C.9) all parallel pairs into [2] are equalized; also equalizes all maps [0] -> [2].
# (2) the 4-object category Z = (x => z -> a, z -> b), ra = rb etc.: integral homology of its nerve.
from itertools import product
from fractions import Fraction

terms = [((0, 1, 3), 1), ((0, 1, 4), -2), ((0, 1, 5), 1), ((0, 2, 3), -1), ((0, 2, 4), 5), ((0, 2, 5), -4),
 ((0, 3, 4), -3), ((0, 3, 5), 2), ((0, 3, 6), 1), ((0, 4, 5), 1), ((0, 4, 6), -1), ((1, 2, 3), 1), ((1, 2, 4), -3),
 ((1, 2, 5), 2), ((1, 3, 4), 1), ((1, 3, 5), 2), ((1, 3, 6), -2), ((1, 4, 5), -3), ((1, 4, 6), 1), ((1, 5, 6), 1),
 ((2, 3, 4), 2), ((2, 3, 5), -3), ((2, 3, 6), 1), ((2, 4, 5), 1), ((2, 4, 6), 1), ((2, 5, 6), -2), ((3, 4, 5), 1),
 ((3, 4, 6), -1), ((3, 5, 6), 1)]
assert sum(c for _, c in terms) == 1
def compose(t, h):          # h: tuple, an injection [m] -> [2]; t: combination of injections [2] -> [6]
    d = {}
    for inj, c in t:
        f = tuple(inj[i] for i in h)
        d[f] = d.get(f, 0) + c
    return {f: c for f, c in d.items() if c}
cofaces = [(1, 2), (0, 2), (0, 1)]
vals = [compose(terms, h) for h in cofaces]
assert vals[0] == vals[1] == vals[2], "cofaces not equalized"
pts = [compose(terms, (i,)) for i in range(3)]
assert pts[0] == pts[1] == pts[2], "vertices not equalized"
print("n=2 affine cone: augmentation 1; t d^0 = t d^1 = t d^2 with", len(vals[0]), "terms; all maps [0]->[2] equalized")

# (2) homology of the nerve of Z by normalized chains over Q (ranks) - enough to see H_2 = Z, H_1 = 0
objs = ['x', 'z', 'a', 'b']
arrows = {('x','z'): ['al','be'], ('z','a'): ['r'], ('z','b'): ['s'], ('x','a'): ['ga'], ('x','b'): ['de']}
comp = {('r','al'):'ga', ('r','be'):'ga', ('s','al'):'de', ('s','be'):'de'}
nonid = [(n, s_, t_) for (s_, t_), ns in arrows.items() for n in ns]
# nondegenerate simplices: chains of composable non-identity arrows
chains1 = nonid
chains2 = [(f, g) for f in nonid for g in nonid if f[2] == g[1]]          # f then g
assert all((g[0], f[0]) in comp for f, g in chains2)
chains3 = [(f, g, h) for (f, g) in chains2 for h in nonid if g[2] == h[1]]
print("simplex counts", len(objs), len(chains1), len(chains2), len(chains3))
import sympy as sp
d1 = sp.zeros(len(objs), len(chains1))
for j, (n, s_, t_) in enumerate(chains1):
    d1[objs.index(t_), j] += 1; d1[objs.index(s_), j] -= 1
idx1 = {c[0]: i for i, c in enumerate(chains1)}
d2 = sp.zeros(len(chains1), len(chains2))
for j, (f, g) in enumerate(chains2):
    d2[idx1[g[0]], j] += 1; d2[idx1[comp[(g[0], f[0])]], j] -= 1; d2[idx1[f[0]], j] += 1
assert (d1 * d2).is_zero_matrix
r1, r2 = d1.rank(), d2.rank()
print("ranks: H0 =", len(objs) - r1, " H1 =", len(chains1) - r1 - r2, " H2 =", len(chains2) - r2)
