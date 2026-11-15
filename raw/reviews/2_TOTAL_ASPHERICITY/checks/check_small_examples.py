"""Own enumeration of the small examples of TOTASPH (B.5, B.6, E.3, A.16/G.5, F.10, F.18, F.19).
Claude (Fable 5.2), review of 10-11 November 2026. Uses only fincat.py of this folder."""
import itertools
from fincat import (Cat, betti, monoid_cat, collage_cov, elements_cov, elements_contra, is_final,
                    check_functor, add_terminal, add_initial, full_sub, pushout_sieve, components)

PRIMES = (2, 3, 5, 1000003)


def show(name, cat, maxdim):
    n = cat.check()
    out = []
    for p in PRIMES:
        counts, b = betti(cat, maxdim, p)
        out.append((p, b))
    print(f'{name}: {len(cat.objects)} objects, {len(cat.arrows)} arrows, {n} composable triples associative')
    print(f'   nondegenerate simplices by dimension (to {maxdim}): {counts}')
    for p, b in out:
        print(f'   Betti mod {p}: {b}')
    return out


def filtered(cat):
    """Direct test of the two filteredness conditions (nonempty assumed)."""
    for a in cat.objects:
        for b in cat.objects:
            if not any(cat.hom(a, c) and cat.hom(b, c) for c in cat.objects):
                return False
    for f, (a, b) in cat.arrows.items():
        for g, (a2, b2) in cat.arrows.items():
            if (a, b) == (a2, b2) and f != g:
                if not any(cat.comp[(h, f)] == cat.comp[(h, g)] for h, (s, t) in cat.arrows.items() if s == b):
                    return False
    return True


def opposite(cat):
    return Cat(cat.objects, {f: (t, s) for f, (s, t) in cat.arrows.items()}, cat.ident,
               {(f, g): v for (g, f), v in cat.comp.items()})


print('=== B.5: the monoid {1,e,f}, uv = v for u,v in {e,f}')
E3 = ['1', 'e', 'f']
mul = {}
for g in E3:
    for f in E3:
        mul[(g, f)] = f if g == '1' else (g if f == '1' else f)
M = monoid_cat(E3, '1', mul)
M.check()
print('   filtered:', filtered(M), ' cofiltered:', filtered(opposite(M)))
K_obj = {'*': ['h', 'i']}
K_arr = {'1': {'h': 'h', 'i': 'i'}, 'e': {'h': 'i', 'i': 'i'}, 'f': {'h': 'i', 'i': 'i'}}
# functoriality of K
for g in E3:
    for f in E3:
        for x in K_obj['*']:
            assert K_arr[mul[(g, f)]][x] == K_arr[g][K_arr[f][x]]
show('   M (truncated nerve, top entry is only a bound)', M, 5)
El = elements_cov(M, K_obj, K_arr)
show('   El_M(K) (expect S^1 in degrees 0..4)', El, 5)
MK = collage_cov(M, K_obj, K_arr)
show('   M_K (expect S^2 in degrees 0..4)', MK, 5)
inc_obj = {'*': '*'}
inc_arr = {m: m for m in E3}
print('   M -> M_K final:', is_final(inc_obj, inc_arr, M, MK))

print('=== B.6: rectangular bands (I x J)^1, |I|,|J| <= 3: filtered iff |J| = 1; cofiltered iff |I| = 1')
for ni in (1, 2, 3):
    for nj in (1, 2, 3):
        el = ['1'] + [(i, j) for i in range(ni) for j in range(nj)]
        mu = {}
        for g in el:
            for f in el:
                mu[(g, f)] = f if g == '1' else (g if f == '1' else (g[0], f[1]))
        B = monoid_cat(el, '1', mu)
        B.check()
        fl, cf = filtered(B), filtered(opposite(B))
        assert fl == (nj == 1) and cf == (ni == 1)
        print(f'   |I|={ni} |J|={nj}: filtered {fl}, cofiltered {cf}')
        if nj >= 2:
            # the homomorphism to {1,e,f} forgetting I and sending j=0 to e, j>0 to f
            hom = {x: ('1' if x == '1' else ('e' if x[1] == 0 else 'f')) for x in el}
            for g in el:
                for f in el:
                    assert hom[mu[(g, f)]] == mul[(hom[g], hom[f])]
            assert set(hom.values()) == set(E3)
print('   surjective homomorphisms onto {1,e,f} verified for |J| >= 2')

print('=== The fork Psi and the sphere category C (A.16, E.3, G.5)')
# C: x => z (la, mu), r: z->a, v: z->b, r la = r mu =: ga, v la = v mu =: de
objs = ['x', 'z', 'a', 'b']
arr = {'1x': ('x', 'x'), '1z': ('z', 'z'), '1a': ('a', 'a'), '1b': ('b', 'b'),
       'la': ('x', 'z'), 'mu': ('x', 'z'), 'r': ('z', 'a'), 'v': ('z', 'b'), 'ga': ('x', 'a'), 'de': ('x', 'b')}
ident = {'x': '1x', 'z': '1z', 'a': '1a', 'b': '1b'}
comp = {}
for f, (s, t) in arr.items():
    comp[(f, ident[s])] = f
    comp[(ident[t], f)] = f
comp[('r', 'la')] = comp[('r', 'mu')] = 'ga'
comp[('v', 'la')] = comp[('v', 'mu')] = 'de'
C = Cat(objs, arr, ident, comp)
show('   C (expect S^2: 1,0,1)', C, 4)
Psi = full_sub(C, ['z', 'a', 'b'])
Psi.check()
print('   Psi:', len(Psi.objects), 'objects,', len(Psi.arrows), 'arrows')
fin, detail = is_final({o: o for o in Psi.objects}, {f: f for f in Psi.arrows}, Psi, C)
print('   Psi -> C final:', fin, detail)
objs_x, edges_x = __import__('fincat').comma_under({o: o for o in Psi.objects}, {f: f for f in Psi.arrows}, Psi, C, 'x')
print('   x\\Psi has', len(objs_x), 'objects and', len([e for e in edges_x if e[0] != e[1]]), 'non-identity arrows (a 4-cycle)')
for S in (['z', 'a'], ['z', 'b'], ['z']):
    sub = full_sub(Psi, S)
    print('   sieve', S, 'has terminal object:', any(all(len(sub.hom(o, t)) == 1 for o in S) for t in S))

print('=== E.3: U = {1,e}, H = {i,h1,h2}, H(e) constant i')
U = monoid_cat(['1', 'e'], '1', {('1', '1'): '1', ('1', 'e'): 'e', ('e', '1'): 'e', ('e', 'e'): 'e'})
U.check()
H_obj = {'*': ['i', 'h1', 'h2']}
H_arr = {'1': {x: x for x in H_obj['*']}, 'e': {x: 'i' for x in H_obj['*']}}
E = elements_contra(U, H_obj, H_arr)
show('   E = U/H', E, 4)
print('   arrows of E:', sorted((str(s[1]), str(t[1]), str(f[0])) for f, (s, t) in E.arrows.items()))
print('   h1, h2 have a common successor:', any(E.hom(('*', 'h1'), c) and E.hom(('*', 'h2'), c) for c in E.objects))
q_obj = {('*', 'i'): 'z', ('*', 'h1'): 'a', ('*', 'h2'): 'b'}
q_arr = {}
for f, (s, t) in E.arrows.items():
    S, T = q_obj[s], q_obj[t]
    q_arr[f] = [g for g in C.hom(S, T)][0]
    assert len(C.hom(S, T)) == 1
check_functor(q_obj, q_arr, E, C)
print('   E -> Psi -> C is a functor; final:', is_final(q_obj, q_arr, E, C))

# sample tests of totality of H: p: U -> D, d = p(e) idempotent; element category of p_!H by the coend
def kan_test(D, c, d, name):
    assert D.comp[(d, d)] == d and D.arrows[d] == (c, c)
    # p_! H (v) = (D(v,c) x H) / ((al.d, h) ~ (al, H(e) h)) ; restriction along D-arrows by precomposition
    val = {}
    for v in D.objects:
        pairs = [(al, h) for al in D.hom(v, c) for h in H_obj['*']]
        par = {x: x for x in pairs}

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x
        for al in D.hom(v, c):
            for h in H_obj['*']:
                par[find((D.comp[(d, al)], h))] = find((al, 'i'))
        val[v] = {x: find(x) for x in pairs}
    F_obj = {v: sorted(set(val[v].values()), key=str) for v in D.objects}
    F_arr = {}
    for g, (v, w) in D.arrows.items():
        F_arr[g] = {}
        for (al, h), cl in val[w].items():
            img = val[v][(D.comp[(al, g)], h)]
            assert F_arr[g].get(cl, img) == img
            F_arr[g][cl] = img
    El = elements_contra(D, F_obj, F_arr)
    El.check()
    res = [betti(El, 4, p)[1] for p in (2, 3, 1000003)]
    print(f'   p_!H on {name}: element category has {len(El.objects)} objects, {len(El.arrows)} arrows; Betti (mod 2, 3, 1000003): {res}')

kan_test(U, '*', 'e', 'U itself (identity functor)')
kan_test(U, '*', '1', 'U, e -> 1')
kan_test(C, 'z', '1z', 'the sphere category C at z, e -> 1')
kan_test(M, '*', 'e', 'the monoid {1,e,f}, e -> e')
kan_test(M, '*', '1', 'the monoid {1,e,f}, e -> 1')
MKc = collage_cov(M, K_obj, K_arr)
kan_test(MKc, '*', 'f', 'M_K (type S^2), e -> f')

print('=== F.18: X = (a => t -> s), ga al = ga be = de; U = {a}')
objs = ['a', 't', 's']
arr = {'1a': ('a', 'a'), '1t': ('t', 't'), '1s': ('s', 's'), 'al': ('a', 't'), 'be': ('a', 't'), 'ga': ('t', 's'), 'de': ('a', 's')}
ident = {'a': '1a', 't': '1t', 's': '1s'}
comp = {}
for f, (s, t) in arr.items():
    comp[(f, ident[s])] = f
    comp[(ident[t], f)] = f
comp[('ga', 'al')] = comp[('ga', 'be')] = 'de'
X = Cat(objs, arr, ident, comp)
show('   X', X, 3)
print('   U/t has', len(X.hom('a', 't')), 'objects and only identities (U = {a} is discrete): not connected')
# pushouts along p: {a} -> D for several D: the inclusion D -> X +_U D must be a homology isomorphism
def test_pushout(D, c, name):
    P, cls = pushout_sieve(X, ['a'], D, {'a': c}, {'1a': D.ident[c]})
    P.check()
    pad = lambda b: (b + [0, 0, 0, 0])[:4]   # degrees 0..3 (the nerves here have dimension <= 4)
    bD = [pad(betti(D, 5, p)[1]) for p in (2, 3)]
    bP = [pad(betti(P, 5, p)[1]) for p in (2, 3)]
    print(f'   pushout along a -> {name}: {len(P.objects)} objects, {len(P.arrows)} arrows; Betti of D {bD}, of pushout {bP}')
    assert bD == bP

test_pushout(C, 'z', 'C (S^2) at z')
test_pushout(C, 'x', 'C (S^2) at x')
test_pushout(C, 'a', 'C (S^2) at a')
par2 = Cat(['p', 'q'], {'1p': ('p', 'p'), '1q': ('q', 'q'), 'f': ('p', 'q'), 'g': ('p', 'q')}, {'p': '1p', 'q': '1q'},
           {('1p', '1p'): '1p', ('1q', '1q'): '1q', ('f', '1p'): 'f', ('g', '1p'): 'g', ('1q', 'f'): 'f', ('1q', 'g'): 'g'})
test_pushout(par2, 'q', 'the parallel pair (S^1) at its target')
test_pushout(par2, 'p', 'the parallel pair (S^1) at its source')

print('=== F.19: {a} in (a => t): the source is discrete, the crossing presheaf has two elements')
show('   parallel pair', par2, 2)

print('=== F.10: lower-copy construction for V = discrete {a,b} (W_0) and V = parallel pair (W_1)')
def lower_copy(V, tag):
    B = add_initial(V, 'o')
    B.check()
    # X: B plus lower copy V0 of V, X(v0, b') = B(v, b')
    objects = [('B', o) for o in B.objects] + [('L', v) for v in V.objects]
    arrows, ident, comp = {}, {}, {}
    for f, (s, t) in B.arrows.items():
        arrows[('B', f)] = (('B', s), ('B', t))
    for f, (s, t) in V.arrows.items():
        arrows[('L', f)] = (('L', s), ('L', t))
        arrows[('X', f)] = (('L', s), ('B', t))      # crossing arrow v0 -> b' for f: v -> b' in V
    # crossing arrows into o: none, since B(v, o) is empty
    for o in B.objects:
        ident[('B', o)] = ('B', B.ident[o])
    for v in V.objects:
        ident[('L', v)] = ('L', V.ident[v])
    for (g, f), w in B.comp.items():
        comp[(('B', g), ('B', f))] = ('B', w)
        if f in V.arrows:  # f: v -> b' crossing, g in B out of b' (stays in V since V is a cosieve of B)
            comp[(('B', g), ('X', f))] = ('X', w)
    for (g, f), w in V.comp.items():
        comp[(('L', g), ('L', f))] = ('L', w)
        comp[(('X', g), ('L', f))] = ('X', w)
    Xc = Cat(objects, arrows, ident, comp)
    Xc.check()
    Y = add_terminal(Xc, 't')
    out = show(f'   Y for {tag}', Y, 5)
    lower = [('L', v) for v in V.objects]
    # V0 is a sieve in Y; X is a sieve in Y
    for f, (s, t) in Y.arrows.items():
        assert not (t in lower and s not in lower)
        assert not (t != 't' and s == 't')
    # right adjoint of V0 -> generated cosieve (two copies of V): old v |-> lower v
    for v in V.objects:
        for w in V.objects:
            assert len(Xc.hom(('L', w), ('B', v))) == len(Xc.hom(('L', w), ('L', v)))
    # boundary category V0/t: one arrow from each lower object to t, so it is V0 itself
    assert all(len(Y.hom(l, 't')) == 1 for l in lower)
    V0 = full_sub(Xc, lower)
    print(f'   boundary category V0/t = V0: {len(V0.objects)} objects, {len(V0.arrows)} arrows; Betti mod 2:',
          betti(V0, 3, 2)[1], '; components:', components(V0.objects, list(V0.arrows.values())))
    print('   X (the intermediate category): Betti mod 2', betti(Xc, 4, 2)[1])

disc = Cat(['a', 'b'], {'1a': ('a', 'a'), '1b': ('b', 'b')}, {'a': '1a', 'b': '1b'}, {('1a', '1a'): '1a', ('1b', '1b'): '1b'})
lower_copy(disc, 'W_0 (expect 6 objects, 15 arrows)')
lower_copy(par2, 'W_1 (expect 6 objects, 21 arrows)')
print('ALL ASSERTIONS PASSED')
