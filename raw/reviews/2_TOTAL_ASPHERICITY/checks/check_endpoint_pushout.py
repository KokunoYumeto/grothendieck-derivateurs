"""TOTASPH F.23: the pushout-product alpha of {0} -> [1] with the endpoints {0,2n} -> Phi_n is not a
W_infty-cofibration. Own construction of the ordinary pushouts P +_A D and P +_A C (Claude, Fable 5.2)
with fincat.pushout_sieve; the answer's code was neither run nor imported.
"""
from fincat import Cat, betti, poset_cat, add_terminal, full_sub, pushout_sieve, check_functor, is_final


def sphere_C():
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
    return Cat(objs, arr, ident, comp)


def run(n):
    # Phi_n: 0 -> 1 <- 2 -> ... <- 2n ; k <= k' iff k = k' or (k even, k' odd, |k - k'| = 1)
    def leqI(k, k2):
        return k == k2 or (k % 2 == 0 and abs(k - k2) == 1)
    Pobj = [(e, k) for e in (0, 1) for k in range(2 * n + 1)]
    P = poset_cat(Pobj, lambda s, t: s[0] <= t[0] and leqI(s[1], t[1]))
    P.check()
    Aobj = [(0, k) for k in range(2 * n + 1)] + [(1, 0), (1, 2 * n)]
    A = full_sub(P, Aobj)
    C = sphere_C()
    C.check()
    D = add_terminal(C, 's')
    D.check()
    bettiP = betti(P, 4, 2)[1]
    bettiA = betti(A, 4, 2)[1]

    def pmap(target):
        p_obj = {}
        for o in Aobj:
            if o == (0, 0):
                p_obj[o] = 'z'
            elif o == (1, 0):
                p_obj[o] = 'b'
            else:
                p_obj[o] = 'a'
        p_arr = {}
        for f, (s, t) in A.arrows.items():
            S, T = p_obj[s], p_obj[t]
            hs = target.hom(S, T)
            assert len(hs) == 1
            p_arr[f] = hs[0]
        check_functor(p_obj, p_arr, A, target)
        return p_obj, p_arr

    print(f'n = {n}: P = [1] x Phi_n has {len(P.objects)} objects, {len(P.arrows)} arrows, Betti mod 2 {bettiP}; '
          f'A has {len(A.objects)} objects, {len(A.arrows)} arrows, Betti mod 2 {bettiA}')
    for name, target in (('D = C with a terminal object (contractible)', D), ('C (type S^2)', C)):
        p_obj, p_arr = pmap(target)
        Q, cls = pushout_sieve(P, Aobj, target, p_obj, p_arr)
        ntr = Q.check()
        res = {}
        for p in (2, 3, 5, 1000003):
            counts, b = betti(Q, 7, p)
            res[p] = b
        print(f'   pushout along p: A -> {name}: {len(Q.objects)} objects, {len(Q.arrows)} arrows, '
              f'{ntr} composable triples associative; simplices {counts}')
        for p, b in res.items():
            print(f'      Betti mod {p}: {b}')
        print(f'      target: Betti mod 2 {betti(target, 5, 2)[1]}')
        # crossing weights as described in the proof
        u1 = ('T', (1, 1))
        w1 = {c: len(Q.hom(('C', c), u1)) for c in target.objects}
        print(f'      |Hom(c, u_1)| = {w1}')
        if n >= 2:
            u2 = ('T', (1, 2))
            w2 = {c: len(Q.hom(('C', c), u2)) for c in target.objects}
            rep = {c: len(target.hom(c, 'a')) for c in target.objects}
            print(f'      |Hom(c, u_2)| = {w2}; |Hom(c, a)| = {rep}')
            assert w2 == rep


run(2)
run(3)
print('ALL ASSERTIONS PASSED')
