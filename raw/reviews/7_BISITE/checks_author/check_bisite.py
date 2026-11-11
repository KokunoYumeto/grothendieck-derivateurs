# Own checks for the review of BISITE (Claude, Fable 5.2, 11 Nov 2026).
# Written from the statements; no code of the return was opened or run.
from itertools import product, combinations


def section(s):
    print("\n== " + s + " ==")


# ---------- finite posets ----------
def closure(n, covers):
    le = [[i == j for j in range(n)] for i in range(n)]
    for a, b in covers:
        le[a][b] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if le[i][k] and le[k][j]:
                    le[i][j] = True
    return le


def meet(le, n, a, b):
    lows = [x for x in range(n) if le[x][a] and le[x][b]]
    tops = [x for x in lows if all(le[y][x] for y in lows)]
    return tops[0] if len(tops) == 1 else None


# ---------- E.12 / A.13 : six-element lattice, XIIc B062 ----------
section("E.12 (XIIc B062): six-element lattice")
n = 6
le = closure(n, [(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (3, 5), (4, 5)])
M = [[meet(le, n, a, b) for b in range(n)] for a in range(n)]
print("all meets exist:", all(M[a][b] is not None for a in range(n) for b in range(n)))
print("meets 1^2, 2^4, 3^4 =", M[1][2], M[2][4], M[3][4])
W = {(x, x) for x in range(n)} | {(1, 3), (1, 4), (2, 3)}
arr = [(a, b) for a in range(n) for b in range(n) if le[a][b]]


def two_of_three(W, arr, le):
    for (a, b) in arr:
        for c in range(len(le)):
            if le[b][c]:
                t = [(a, b) in W, (b, c) in W, (a, c) in W]
                if sum(t) == 2:
                    return False
    return True


print("W has two-out-of-three:", two_of_three(W, arr, le))


def fib(x, s):
    # x <= s is intrinsic over s: pullback along x -> s keeps W on arrows a -> b with b <= s
    return all((M[a][x], M[b][x]) in W for (a, b) in W if le[b][s])


F = {s: [x for x in range(n) if le[x][s] and fib(x, s)] for s in range(n)}
print("F_s:", F)
print("as stated:", F == {0: [0], 1: [0, 1], 2: [0, 2], 3: [0, 3], 4: [0, 1, 4], 5: [0, 3, 5]})
okb = True
for s in range(n):
    for x in F[s]:
        for y in F[s]:
            if (x, y) in W:
                for t in range(n):
                    if le[t][s] and (M[x][t], M[y][t]) not in W:
                        okb = False
print("(b) at every base:", okb)
R = [0, 3, 3, 3, 3, 5]
T = [0, 1, 2, 3, 1, 5]
mono = lambda f: all(le[f[a]][f[b]] for (a, b) in arr)
presW = lambda f: all((f[a], f[b]) in W for (a, b) in W)
print("R, T monotone:", mono(R), mono(T), " preserve W:", presW(R), presW(T))
print("T(x)->x in W:", all((T[x], x) in W for x in range(n)),
      "  T(x)->R(x) in W:", all((T[x], R[x]) in W for x in range(n)))
print("R and T are the identity on F_5:", all(R[x] == x and T[x] == x for x in F[5]))
print("W = {a<=b : R(a)=R(b)}:", W == {(a, b) for (a, b) in arr if R[a] == R[b]})
R3 = [0, 3, 3, 3]
print("base 3: x->R3(x) in W:", all((x, R3[x]) in W for x in range(4)))
H = [0, 3, 4, 5]
print("non-identity W-arrows inside H={0,3,4,5}:", [(a, b) for (a, b) in W if a in H and b in H and a != b],
      "; 3 and 4 comparable:", le[3][4] or le[4][3])
print("4->5 factors as a W-arrow followed by an intrinsic fibration over 5:",
      any((4, z) in W and z in F[5] for z in range(n)))

# ---------- A.8 ----------
section("A.8: transporter on the chain 0<1<2<3")
arr4 = [(a, b) for a in range(4) for b in range(4) if a <= b]
W4 = {(x, x) for x in range(4)} | {(0, 2), (0, 3)}
A4 = {(x, x) for x in range(4)} | {(0, 3)}


def TW(A, W):
    # p = (e -> b): every arrow (x -> y) of A with y <= b, pulled back along e -> b, lies in W
    return {(e, b) for (e, b) in arr4 if all((min(x, e), min(y, e)) in W for (x, y) in A if y <= b)}


def KW(L, W):
    return {(x, y) for (x, y) in W if all((min(x, e), min(y, e)) in W for (e, b) in L if b == y)}


Tr = TW(A4, W4)
print("T_W(A) = all arrows minus", set(arr4) - Tr, "; (1,2),(2,3) in T:", (1, 2) in Tr, (2, 3) in Tr,
      "; K_W T_W(A) == A:", KW(Tr, W4) == A4)


# ---------- finite categories ----------
class Cat:
    def __init__(s, objs, arrows, src, tgt, comp, ident):
        s.objs = objs
        s.arrows = arrows
        s.src = src
        s.tgt = tgt
        s.comp = comp
        s.ident = ident
        s.by_src = {}
        for f in arrows:
            s.by_src.setdefault(src[f], []).append(f)

    def check(s):
        for f in s.arrows:
            assert s.comp(f, s.ident(s.src[f])) == f and s.comp(s.ident(s.tgt[f]), f) == f
        cnt = 0
        for f in s.arrows:
            for g in s.by_src.get(s.tgt[f], []):
                gf = s.comp(g, f)
                assert gf in s.src and s.src[gf] == s.src[f] and s.tgt[gf] == s.tgt[g]
                for h in s.by_src.get(s.tgt[g], []):
                    assert s.comp(h, gf) == s.comp(s.comp(h, g), f)
                    cnt += 1
        return cnt

    def components(s):
        par = {o: o for o in s.objs}

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        for f in s.arrows:
            par[find(s.src[f])] = find(s.tgt[f])
        return len({find(o) for o in s.objs})

    def h1_f2(s):
        # dim H^1(B;F_2) = dim{phi on arrows : phi(gf)=phi(g)+phi(f)} - (#objects - #components)
        idx = {f: i for i, f in enumerate(s.arrows)}
        piv = {}
        for f in s.arrows:
            for g in s.by_src.get(s.tgt[f], []):
                r = 0
                for a in (f, g, s.comp(g, f)):
                    r ^= (1 << idx[a])
                while r:
                    h = r.bit_length() - 1
                    if h in piv:
                        r ^= piv[h]
                    else:
                        piv[h] = r
                        break
        return len(s.arrows) - len(piv) - (len(s.objs) - s.components())


# ---------- B.12 ----------
section("B.12: H -> K, central C_2-extension of the face poset of the boundary of the tetrahedron")
subs = [frozenset(c) for k in (1, 2, 3) for c in combinations(range(4), k)]
incl = [(x, y) for x in subs for y in subs if x <= y]
special = (frozenset({0}), frozenset({0, 1}), frozenset({0, 1, 2}))


def coc(u, v):
    return 1 if (u[0], u[1], v[1]) == special else 0


def mkH(k):
    labels = list(product((0, 1), repeat=k))
    arrows = [(u, m) for u in incl for m in labels]
    src = {a: a[0][0] for a in arrows}
    tgt = {a: a[0][1] for a in arrows}

    def comp(g, f):
        (v, nn), (u, mm) = g, f
        cc = coc(u, v)
        return ((u[0], v[1]), tuple((a + b + cc) % 2 for a, b in zip(mm, nn)))
    ident = lambda x: ((x, x), tuple([0] * k))
    return Cat(subs, arrows, src, tgt, comp, ident), labels


Kc, _ = mkH(0)
H1, L1 = mkH(1)
H2, L2 = mkH(2)
print("K: objects, arrows, composable triples:", len(Kc.objs), len(Kc.arrows), Kc.check())
print("H: objects, arrows, composable triples (all associative):", len(H1.objs), len(H1.arrows), H1.check())
print("H x_K H: arrows, composable triples (all associative):", len(H2.arrows), H2.check())
tri = [(x, y, z) for x in subs for y in subs for z in subs if x < y < z]
print("triangles of BK:", len(tri), "; the cochain is non-zero on", sum(coc((x, y), (y, z)) for (x, y, z) in tri))
edges = [(x, y) for x in subs for y in subs if x < y]
print("each edge in exactly two triangles:",
      all(sum(1 for t in tri if e in ((t[0], t[1]), (t[1], t[2]), (t[0], t[2]))) == 2 for e in edges))
print("Euler characteristic of BK:", len(subs) - len(edges) + len(tri))
print("dim H^1(-;F_2) of K, H, H x_K H:", Kc.h1_f2(), H1.h1_f2(), H2.h1_f2(), "(stated: 0, 0, 1)")


def bif(Hc, labels):
    for u in incl:
        for v in incl:
            if v[0] == u[1]:
                for m in labels:
                    for t in labels:
                        if sum(1 for nn in labels if Hc.comp((v, nn), (u, m))[1] == t) != 1:
                            return False
                        if sum(1 for mm in labels if Hc.comp((v, m), (u, mm))[1] == t) != 1:
                            return False
    return True


print("unique factorization through every arrow (so every arrow is cartesian and cocartesian):", bif(H1, L1))

# ---------- B.10 (n = 0) and A.32 ----------
section("B.10 (n=0) and A.32")
E_objs = [0, 1]
E_arr = [(i, j) for i in E_objs for j in E_objs]
objs = [(x, t) for x in (0, 1) for t in (0, 1)]
arrs = [(a, b) for a in objs for b in objs if a[1] == (b[1] + b[0] - a[0]) % 2]
cc = Cat(objs, arrs, {a: a[0] for a in arrs}, {a: a[1] for a in arrs}, lambda g, f: (f[0], g[1]), lambda x: (x, x))
cc.check()
print("E/c: objects", len(objs), "arrows", len(arrs), "components", cc.components(),
      "(two chaotic categories on two objects:", len(arrs) == 8, ")")
ExB_arr = [(a, g) for a in E_arr for g in (0, 1)]
ExB = Cat(E_objs, ExB_arr, {a: a[0][0] for a in ExB_arr}, {a: a[0][1] for a in ExB_arr},
          lambda g, f: ((f[0][0], g[0][1]), (f[1] + g[1]) % 2), lambda x: ((x, x), 0))
Ec = Cat(E_objs, E_arr, {a: a[0] for a in E_arr}, {a: a[1] for a in E_arr}, lambda g, f: (f[0], g[1]), lambda x: (x, x))
ExB.check()
Ec.check()
print("E x BC_2: components", ExB.components(), "dim H^1(F_2)", ExB.h1_f2(),
      "; E: components", Ec.components(), "dim H^1(F_2)", Ec.h1_f2())
print("arrows of E over the identity of BC_2 (the strict fibre is discrete on two objects):",
      [a for a in E_arr if (a[1] - a[0]) % 2 == 0])

# ---------- B.11 ----------
section("B.11: the three-sheeted covering")


def mul(p, q):
    return tuple(p[q[i]] for i in range(3))


def inv(p):
    r = [0] * 3
    for i, v in enumerate(p):
        r[v] = i
    return tuple(r)


x = (1, 0, 2)
y = (2, 1, 0)
ay = mul(y, mul(x, mul(y, mul(inv(x), inv(y)))))
print("x ->", x, "; alpha(y) = y x y x^-1 y^-1 ->", ay, "; equal:", ay == x)


def orbits(gens):
    seen = set()
    out = []
    for i in range(3):
        if i in seen:
            continue
        o = {i}
        ch = True
        while ch:
            ch = False
            for g in gens:
                for j in list(o):
                    if g[j] not in o:
                        o.add(g[j])
                        ch = True
        seen |= o
        out.append(sorted(o))
    return out


print("orbits of the action:", orbits([x, y]), " of the pulled-back action:", orbits([x, ay]))

# ---------- B.7 ----------
section("B.7: the two posets over [1]")
names = ['x', 'a', 'b', 'c']
leP = closure(4, [(0, 1), (1, 3), (0, 2), (2, 3)])
pP = [0, 1, 1, 1]


def out_lifts(le, p, a, b):
    return [z for z in range(len(p)) if le[a][z] and p[z] == b]


def in_lifts(le, p, a, b):
    return [z for z in range(len(p)) if le[z][a] and p[z] == b]


def has_min(le, S):
    return any(all(le[m][z] for z in S) for m in S)


def has_max(le, S):
    return any(all(le[z][m] for z in S) for m in S)


for a in range(4):
    for b in (0, 1):
        if pP[a] <= b:
            S = out_lifts(leP, pP, a, b)
            print("P outgoing", names[a], "over ->", b, [names[z] for z in S],
                  "has least" if has_min(leP, S) else "no least", "/", "has greatest" if has_max(leP, S) else "no greatest")
        if b <= pP[a]:
            S = in_lifts(leP, pP, a, b)
            print("P incoming", names[a], "over <-", b, [names[z] for z in S],
                  "has least" if has_min(leP, S) else "no least", "/", "has greatest" if has_max(leP, S) else "no greatest")
leV = closure(3, [(0, 1), (0, 2)])
pV = [0, 0, 1]
s = [0, 2]
print("V: outgoing lifts of b over 0->1:", out_lifts(leV, pV, 1, 1), "; p s = id:",
      [pV[s[t]] for t in (0, 1)] == [0, 1], "; s p(v) <= v for all v:", all(leV[s[pV[v]]][v] for v in range(3)))
