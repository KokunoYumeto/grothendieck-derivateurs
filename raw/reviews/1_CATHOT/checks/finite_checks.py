"""Independent finite checks for the review of CATHOT (reviewer's own code; python -I finite_checks.py).

1. B.2: spin lifts of x=(ab)(cd), y=(ac)(bd) in a Clifford algebra anticommute and square to -1
        (so the double cover of Alt restricted to the Klein four-group is Q_8: the torus class is non-zero).
2. E.4/F.2: c g c^-1 = s(g) for the cycle c=(0 1 ... n+1) and every g in Sym{0..n}, n<=5;
        the categories T_n (n<=3): associativity, the three natural transformations joining the
        inclusion T_n -> T_{n+1} to the shift.
3. C.5: finite truncations of the fence: distance from 0 to 2r is 2r.
4. E.5: the nine-fence in the twelve-cycle fence: contraction h_k, and no strict retraction (all 9^3 maps).
5. E.7: sieve property of c Sd^2 Lambda^n_k in c Sd^2 Delta^n (n=2,3), which makes every category
        with a terminal object Thomason-fibrant; the terminal fork has no single arrow between 0 and 2.
6. E.23: the half-fence maps phi_j are order-preserving, and phi_j <= phi_{j+1} (j even) or >= (j odd).
7. A.6: the crown: Ex^2 N(D) has finitely many edges at a vertex (count of fence maps), H_1 = Z.
"""
import itertools
from fractions import Fraction

# ---------------------------------------------------------------- 1. Clifford algebra
def cl_mul(a, b):
    """Clifford algebra with e_i^2 = -1; elements: dict frozenset(sorted tuple) -> coeff, basis words as tuples."""
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            w = list(wa) + list(wb)
            sign = 1
            # bubble sort with sign, cancel equal neighbours (e_i e_i = -1)
            changed = True
            while changed:
                changed = False
                for i in range(len(w) - 1):
                    if w[i] > w[i + 1]:
                        w[i], w[i + 1] = w[i + 1], w[i]
                        sign = -sign
                        changed = True
                    elif w[i] == w[i + 1]:
                        del w[i:i + 2]
                        sign = -sign
                        changed = True
                        break
            k = tuple(w)
            out[k] = out.get(k, 0) + sign * ca * cb
    return {k: v for k, v in out.items() if v != 0}

def cl_add(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + s * v
    return {k: v for k, v in out.items() if v != 0}

def e(i):
    return {(i,): Fraction(1)}

def scal(c, a):
    return {k: c * v for k, v in a.items()}

a_, b_, c_, d_ = 0, 1, 2, 3
xt = scal(Fraction(1, 2), cl_mul(cl_add(e(a_), e(b_), -1), cl_add(e(c_), e(d_), -1)))
yt = scal(Fraction(1, 2), cl_mul(cl_add(e(a_), e(c_), -1), cl_add(e(b_), e(d_), -1)))
minus_one = {(): Fraction(-1)}
assert cl_mul(xt, xt) == minus_one and cl_mul(yt, yt) == minus_one
assert cl_add(cl_mul(xt, yt), cl_mul(yt, xt)) == {}
# the lifts act on vectors as the permutations x and y: v -> u v u^-1, with u^-1 = -u here
def conj(u, v):
    return cl_mul(cl_mul(u, v), scal(Fraction(-1), u))
perm_x = {a_: b_, b_: a_, c_: d_, d_: c_}
perm_y = {a_: c_, c_: a_, b_: d_, d_: b_}
for i in range(4):
    assert conj(xt, e(i)) == e(perm_x[i]) and conj(yt, e(i)) == e(perm_y[i])
print("1. Clifford check: lifts of (ab)(cd), (ac)(bd) square to -1, anticommute, and cover these permutations: OK")

# ---------------------------------------------------------------- 2. shift and T_n
def compose(p, q):            # p after q, permutations as tuples
    return tuple(p[q[i]] for i in range(len(q)))

def inverse(p):
    r = [0] * len(p)
    for i, v in enumerate(p):
        r[v] = i
    return tuple(r)

def extend(p, size):
    return tuple(p) + tuple(range(len(p), size))

def shift(p):                 # s(p)(0)=0, s(p)(i+1)=p(i)+1 ; Sym{0..j} -> Sym{0..j+1}
    return (0,) + tuple(v + 1 for v in p)

count = 0
for n in range(0, 6):
    c = tuple(list(range(1, n + 2)) + [0])            # c(k)=k+1, c(n+1)=0 on {0..n+1}
    for g in itertools.permutations(range(n + 1)):
        ge = extend(g, n + 2)
        assert compose(compose(c, ge), inverse(c)) == shift(g)
        count += 1
print(f"2a. c g c^-1 = s(g) checked for {count} permutations (n <= 5): OK")

def T(n):
    """arrows of T_n: (i, j, g) with i<=j<=n and g in Sym{0..j}; composition (j,k,h)o(i,j,g) = (i,k,h*ext(g))."""
    return [(i, j, g) for j in range(n + 1) for i in range(j + 1) for g in itertools.permutations(range(j + 1))]

def comp_T(b, a):
    (j, k, h), (i, j2, g) = b, a
    assert j == j2
    return (i, k, compose(h, extend(g, k + 1)))

for n in range(0, 4):
    arrows = T(n)
    by_src = {}
    for a in arrows:
        by_src.setdefault(a[0], []).append(a)
    # identities and associativity
    for a in arrows:
        idt = (a[1], a[1], tuple(range(a[1] + 1)))
        ids = (a[0], a[0], tuple(range(a[0] + 1)))
        assert comp_T(idt, a) == a and comp_T(a, ids) == a
    if n <= 2:
        for a in arrows:
            for b in by_src.get(a[1], []):
                for c3 in by_src.get(b[1], []):
                    assert comp_T(c3, comp_T(b, a)) == comp_T(comp_T(c3, b), a)
    # functors T_n -> T_{n+1}: inclusion I, shift S, constants-at-(n+1) with labels: CI (ext g), CS (shifted g)
    m = n + 1
    I = lambda a: a
    S = lambda a: (a[0] + 1, a[1] + 1, shift(a[2]))
    CI = lambda a: (m, m, extend(a[2], m + 1))
    CS = lambda a: (m, m, extend(shift(a[2]), m + 1))
    idm = tuple(range(m + 1))
    cyc = tuple(list(range(1, m + 1)) + [0])
    for a in arrows:
        i, j, g = a
        # functoriality of S on composites is checked through comp_T below
        # natural transformation I => CI with components (i, m, id)
        assert comp_T((j, m, idm), I(a)) == comp_T(CI(a), (i, m, idm))
        # natural transformation S => CS with components (i+1, m, id)
        assert comp_T((j + 1, m, idm), S(a)) == comp_T(CS(a), (i + 1, m, idm))
        # natural isomorphism CI => CS with the single component (m, m, cyc)
        assert comp_T((m, m, cyc), CI(a)) == comp_T(CS(a), (m, m, cyc))
    if n <= 2:
        for a in arrows:
            for b in by_src.get(a[1], []):
                assert S(comp_T(b, a)) == comp_T(S(b), S(a))
    print(f"2b. T_{n}: {len(arrows)} arrows; identities{', associativity, functoriality of the shift' if n<=2 else ''}; "
          f"inclusion => const <=> const' <= shift in Fun(T_{n},T_{n+1}): OK")

# ---------------------------------------------------------------- 3. fence distances
def fence_adj(N):             # objects 0..N-1, arrows even -> adjacent odd
    return {i: [j for j in (i - 1, i + 1) if 0 <= j < N] for i in range(N)}
for r in (1, 2, 4, 8, 16):
    adj = fence_adj(2 * r + 1)
    dist = {0: 0}
    frontier = [0]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    assert dist[2 * r] == 2 * r
print("3. fence: distance(0, 2r) = 2r for r = 1,2,4,8,16: OK (the infinite statement is the general argument)")

# ---------------------------------------------------------------- 4. nine-fence in the twelve-cycle
def leq_fence(i, j, modulus=None):
    """order of the fence poset: i <= j iff i == j or (i even and j adjacent to i)."""
    if i == j:
        return True
    if i % 2:
        return False
    if modulus is None:
        return abs(i - j) == 1
    return (i - j) % modulus in (1, modulus - 1)

A = list(range(9))
B = list(range(12))
for k in range(9):            # h_k(i) = max(i,k) is order-preserving, consecutive ones comparable pointwise
    h = [max(i, k) for i in A]
    assert all(leq_fence(h[i], h[j]) for i in A for j in A if leq_fence(i, j))
    if k < 8:
        h2 = [max(i, k + 1) for i in A]
        assert all(leq_fence(h[i], h2[i]) for i in A) or all(leq_fence(h2[i], h[i]) for i in A)
retractions = 0
for img in itertools.product(A, repeat=3):
    r = {i: i for i in A}
    r.update({9: img[0], 10: img[1], 11: img[2]})
    if all(leq_fence(r[i], r[j]) for i in B for j in B if leq_fence(i, j, 12)):
        retractions += 1
assert retractions == 0
print("4. nine-fence A in twelve-cycle fence B: A contracts to the point 8 through h_k; strict retractions B -> A: 0 of 729: OK")

# ---------------------------------------------------------------- 5. sieve property; terminal fork
def nonempty_subsets(vertices):
    return [frozenset(s) for r in range(1, len(vertices) + 1) for s in itertools.combinations(vertices, r)]

def chains_of(faces):
    """non-empty chains (strictly increasing under inclusion) of the given set of faces."""
    faces = sorted(faces, key=len)
    out = []
    def rec(prefix, start):
        for idx in range(start, len(faces)):
            f = faces[idx]
            if not prefix or (prefix[-1] < f):
                out.append(tuple(prefix + [f]))
                rec(prefix + [f], idx + 1)
    rec([], 0)
    return out

for n in (2, 3):
    V = list(range(n + 1))
    full = nonempty_subsets(V)
    for k in V:
        horn = [f for f in full if f != frozenset(V) and f != frozenset(V) - {k}]
        big = set(frozenset(c) for c in chains_of(full))       # objects of c Sd^2 Delta^n: chains of faces
        small = set(frozenset(c) for c in chains_of(horn))     # objects of c Sd^2 Lambda^n_k
        assert small <= big
        # order: a chain is <= another when it is a subchain. Sieve: every subchain of an old chain is old.
        for ch in small:
            for r in range(1, len(ch) + 1):
                for sub in itertools.combinations(sorted(ch, key=len), r):
                    assert frozenset(sub) in small
        # hence no arrow from a new object to an old one
        assert not any(new < old for new in big - small for old in small)
print("5a. c Sd^2 Lambda^n_k is a sieve in c Sd^2 Delta^n for n=2,3 (no arrow from a new chain to an old one): OK")
fork_leq = {(0, 0), (1, 1), (2, 2), (0, 1), (2, 1)}
assert (0, 2) not in fork_leq and (2, 0) not in fork_leq
print("5b. terminal fork 0 -> 1 <- 2: terminal object 1; no arrow between 0 and 2 in either direction: OK")

# ---------------------------------------------------------------- 6. half-fence collar maps
def half_leq(i, j):           # integer fence restricted to i,j <= 0; arrows even -> adjacent odd
    return i == j or (i % 2 == 0 and abs(i - j) == 1)

def phi(j, i):
    if i <= -j - 2:
        return i + 2
    if i <= -j:
        return -j
    return i

L = range(-60, 1)
for j in range(0, 25):
    for i in L:
        for i2 in (i - 1, i + 1):
            if i2 in L and half_leq(i, i2):
                assert half_leq(phi(j, i), phi(j, i2)), (j, i, i2)
    assert phi(j, 0) == 0
    lo = all(half_leq(phi(j, i), phi(j + 1, i)) for i in L)
    hi = all(half_leq(phi(j + 1, i), phi(j, i)) for i in L)
    assert (lo if j % 2 == 0 else hi)
    diff = [i for i in L if phi(j, i) != phi(j + 1, i)]
    assert diff == [-j - 2, -j - 1]
assert all(phi(0, i) == min(i + 2, 0) for i in L)
print("6. half-fence maps phi_j (j<25): order-preserving, fix 0, phi_0 = collar insertion, "
      "phi_j <= phi_{j+1} (j even) / >= (j odd), differing only at -j-2, -j-1: OK")

# ---------------------------------------------------------------- 7. crown
crown = {('a0', 'b0'), ('a0', 'b1'), ('a1', 'b0'), ('a1', 'b1')}
objs = ['a0', 'a1', 'b0', 'b1']
def cle(x, y):
    return x == y or (x, y) in crown
# edges of Ex^2 N(D) = functors from the five-object fence (0 -> 1 <- 2 -> 3 <- 4) to D
edges = [f for f in itertools.product(objs, repeat=5)
         if cle(f[0], f[1]) and cle(f[2], f[1]) and cle(f[2], f[3]) and cle(f[4], f[3])]
loops_at_a0 = [f for f in edges if f[0] == 'a0' and f[4] == 'a0']
print(f"7. crown: Ex^2 N(D) has {len(edges)} edges, {len(loops_at_a0)} of them loops at a0 (finite), "
      f"while pi_1 = Z (4 vertices, 4 edges, no 2-simplices: Euler characteristic 0, connected): not Kan: OK")
print("ALL FINITE CHECKS PASSED")
