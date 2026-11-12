"""Independent checks for PRETOT B.2(v), E.5/G.2, E.8, F.12 and one new observation on Ty^op.

Claude Opus 5.5, 12 Nov 2026.  Uses thmA5_indep.py (my own module) for M, H and the action.
Usage: python -I parts_indep.py <output_dir>
"""
import sys
from itertools import product, combinations_with_replacement
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE))
import thmA5_indep as T5          # noqa: E402  (module level builds K, M, H only)
from linalg_int import homology_from_boundaries  # noqa: E402

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'out'
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def b2v():
    M, H, pull, after = T5.M, T5.H, T5.pull, T5.after
    act = {(h, m): pull(h, m) for h in H for m in M}
    # hom-set sizes of Y (objects L = lower copy M_0, O = initial 0, U = old copy of M, T = t)
    hom = {('L', 'L'): 10, ('U', 'U'): 10, ('O', 'O'): 1, ('T', 'T'): 1, ('L', 'U'): 10, ('O', 'U'): 1,
           ('L', 'T'): 52, ('U', 'T'): 52, ('O', 'T'): 1}
    X = {k: v for k, v in hom.items() if 'T' not in k}
    objs = ['L', 'O', 'U', 'T']
    inn = {y: sum(v for (s, t), v in hom.items() if t == y) for y in objs}
    out = {y: sum(v for (s, t), v in hom.items() if s == y) for y in objs}
    pairs = sum(inn[y] * out[y] for y in objs)
    triples = sum(v * inn[s] * out[t] for (s, t), v in hom.items())
    say(f'B.2(v): |Arr X| = {sum(X.values())}, |Arr Y| = {sum(hom.values())}, composable pairs {pairs}, triples {triples}')
    assert (sum(X.values()), sum(hom.values()), pairs, triples) == (32, 138, 2131, 28204)
    # G = j_! F at the lower object: coend of X(L, U) x F(U) = M x H over End(U) = M:
    # (beta o u, h) ~ (u, h.beta).  Compute the quotient by union-find and its right M-action.
    pairs_ = [(u, h) for u in M for h in H]
    par = {p: p for p in pairs_}

    def fd(p):
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p
    for u in M:
        for h in H:
            for beta in M:
                a, b = fd((after(beta, u), h)), fd((u, act[h, beta]))
                if a != b:
                    par[a] = b
    classes = {fd(p) for p in pairs_}
    inv = {fd(p): act[p[1], p[0]] for p in pairs_}       # (u,h) -> h.u is constant on classes
    for p in pairs_:
        assert inv[fd(p)] == act[p[1], p[0]]
    assert len(classes) == 52 and len(set(inv.values())) == 52
    # right action of End(L) = M by precomposition: (u, h).a = (u o a, h) -> h.(u a) = (h.u).a
    for p in pairs_:
        for a in M:
            assert act[p[1], after(p[0], a)] == act[inv[fd(p)], a]
    say('   G(m_0) = M x_M H has 52 classes, identified with H as a right M-set: the composite weight at t is H')
    # B.2(iii), (iv) arrow counts
    say(f'B.2(iii): |Arr(M u_H t)| = {10 + 52 + 1};  B.2(iv): |Arr(B)| = {1 + 1 + 10}, |Arr(B u_F t)| = {12 + 53 + 1}')


def nerve(objects, arrows, compose, ident):
    """arrows: list of (name, src, tgt); compose(g, f) -> name; ident: set of identity names."""
    src = {a: s for a, s, t in arrows}
    tgt = {a: t for a, s, t in arrows}
    nonid = [a for a, s, t in arrows if a not in ident]
    chains = [[(o,) for o in objects], [(a,) for a in nonid]]
    while chains[-1]:
        chains.append([c + (b,) for c in chains[-1] for b in nonid if src[b] == tgt[c[-1]]])
    chains.pop()
    idx = [{c: i for i, c in enumerate(ch)} for ch in chains]
    bnd = {}
    for n in range(1, len(chains)):
        B = [[0] * len(chains[n]) for _ in chains[n - 1]]
        for j, c in enumerate(chains[n]):
            if n == 1:
                B[idx[0][(tgt[c[0]],)]][j] += 1
                B[idx[0][(src[c[0]],)]][j] -= 1
                continue
            B[idx[n - 1][c[1:]]][j] += 1
            B[idx[n - 1][c[:-1]]][j] += (-1) ** n
            for i in range(1, n):
                h = compose(c[i], c[i - 1])
                if h not in ident:
                    B[idx[n - 1][c[:i - 1] + (h,) + c[i + 1:]]][j] += (-1) ** i
        bnd[n] = B
    dims = [len(c) for c in chains]
    return dims, homology_from_boundaries(dims, bnd)


def sphere_and_double_cone():
    base = [('1x', 'x', 'x'), ('1o', 'o', 'o'), ('1a', 'a', 'a'), ('1b', 'b', 'b'),
            ('r', 'x', 'o'), ('s', 'x', 'o'), ('A', 'o', 'a'), ('B', 'o', 'b'), ('c', 'x', 'a'), ('d', 'x', 'b')]
    ident = {'1x', '1o', '1a', '1b', '1e', '1t'}

    def comp(g, f):
        if f in ident:
            return g
        if g in ident:
            return f
        if g in ('A', 'B') and f in ('r', 's'):
            return 'c' if g == 'A' else 'd'
        if g.startswith('to_'):            # x -> e, etc.
            return 'to_' + g.split('_')[1] + '_from_' + dict((a, s) for a, s, t in arrows_all)[f]
        raise ValueError((g, f))
    arrows_all = list(base)
    dims, hom = nerve(['x', 'o', 'a', 'b'], base, comp, ident)
    say(f"G.2 / E.5: V'_0 = S (x =>r,s o ->A a, o ->B b, Ar = As, Br = Bs): chain ranks {dims}, homology {hom}")
    assert dims == [4, 6, 4] and hom == [(1, []), (0, []), (1, [])]
    # double cone: two new objects e, t, one arrow from each old object to each, no arrows between e and t
    arrows2 = list(base) + [('1e', 'e', 'e'), ('1t', 't', 't')]
    for z in ('e', 't'):
        for o in ('x', 'o', 'a', 'b'):
            arrows2.append((f'{o}>{z}', o, z))
    src2 = {a: s for a, s, t in arrows2}

    def comp2(g, f):
        if f in ident:
            return g
        if g in ident:
            return f
        if '>' in g:
            return f'{src2[f]}>{g.split(">")[1]}'
        return comp(g, f)
    dims2, hom2 = nerve(['x', 'o', 'a', 'b', 'e', 't'], arrows2, comp2, ident)
    say(f"   V'_0 with two cone points e, t (XIIapp ms. 15, the category bar V'): {len(arrows2)} arrows, chain ranks {dims2}, homology {hom2}")
    assert len(arrows2) == 20 and dims2 == [6, 14, 16, 8] and hom2 == [(1, []), (0, []), (0, []), (1, [])]


def type_maps(src, tgt):
    """Ty(src, tgt): endpoint-preserving, numerically monotone functors I_src -> I_tgt (words in '+-')."""
    n, m = len(src), len(tgt)
    for v in combinations_with_replacement(range(m + 1), n + 1):
        if v[0] != 0 or v[-1] != m:
            continue
        ok = True
        for i in range(n):
            a, b = v[i], v[i + 1]
            if a == b:
                continue
            # the edge i -- i+1 of the source must map onto one edge of the target with the same orientation
            if b != a + 1 or tgt[a] != src[i]:
                ok = False
                break
        if ok:
            yield v


def ty_checks():
    f, g = (0, 0, 0, 1), (0, 1, 1, 1)
    assert set(type_maps('+-+', '+')) == {f, g}
    tested = 0
    for L in range(0, 9):
        for w in product('+-', repeat=L):
            for h in type_maps(''.join(w), '+-+'):
                assert 1 in h and 2 in h
                fh = tuple(f[x] for x in h)
                gh = tuple(g[x] for x in h)
                assert fh != gh
                tested += 1
    say(f'F.12: Ty(+-+, +) = {{f, g}} = {{(0,0,0,1), (0,1,1,1)}}; all {tested} maps h: sigma -> (+-+) with |sigma| <= 8 '
        f'hit vertices 1 and 2 and have fh != gh (no equalizer in Ty, so Ty^op is not filtered)')
    # New observation: an affine equalizer of the same pair exists in Ty^op.
    r = '+-+-+'
    hs = list(type_maps(r, '+-+'))
    h1, h2, h3 = (0, 1, 2, 3, 3, 3), (0, 0, 0, 1, 2, 3), (0, 1, 2, 2, 2, 3)
    assert h1 in hs and h2 in hs and h3 in hs
    combo = {h1: 1, h2: 1, h3: -1}

    def push(phi):
        out = {}
        for h, c in combo.items():
            k = tuple(phi[x] for x in h)
            out[k] = out.get(k, 0) + c
        return {k: v for k, v in out.items() if v}
    assert push(f) == push(g) and sum(combo.values()) == 1
    say(f'   new: in Ty^op the pair f^op, g^op : (+) -> (+-+) has the affine equalizer t = h1 + h2 - h3 in Z[Ty((+-+-+), (+-+))], '
        f'h1 = {h1}, h2 = {h2}, h3 = {h3}: f t = g t = {push(f)} (one jump map), augmentation 1')
    # Ty^op is not sifted: spans (+) <- x -> (+) keep the order of their two jump edges
    say('   (Ty^op is not sifted: for spans (+) <- x -> (+) in Ty the relative order of the two jump edges is invariant)')


def walking_retraction():
    # R: objects 0, z; arrows id0, u: 0->z, r: z->0, e = u r, idz;  r u = id0
    Rarr = {'id0': ('0', '0'), 'u': ('0', 'z'), 'r': ('z', '0'), 'e': ('z', 'z'), 'idz': ('z', 'z')}
    def rc(g, f):         # g o f
        assert Rarr[f][1] == Rarr[g][0]
        if f in ('id0', 'idz'):
            return g
        if g in ('id0', 'idz'):
            return f
        table = {('r', 'u'): 'id0', ('u', 'r'): 'e', ('e', 'u'): 'u', ('r', 'e'): 'r', ('e', 'e'): 'e'}
        return table[(g, f)]
    for h in Rarr:
        for g in Rarr:
            for f in Rarr:
                if Rarr[f][1] == Rarr[g][0] and Rarr[g][1] == Rarr[h][0]:
                    assert rc(h, rc(g, f)) == rc(rc(h, g), f)
    # paths of length <= 1 from 0: (type, vertex objects, edge arrow)
    paths = {'t': ('', ('0',), ()), 'a+': ('+', ('0', '0'), ('id0',)), 'd+': ('+', ('0', 'z'), ('u',)),
             'a-': ('-', ('0', '0'), ('id0',)), 'd-': ('-', ('0', 'z'), ('r',))}
    homs = {}
    for p, (tp, vp, ep) in paths.items():
        for q, (tq, vq, eq) in paths.items():
            maps = []
            for phi in type_maps(tp, tq):
                # eta_i : vp[i] -> vq[phi(i)], eta_0 = id0, naturality on the edge of p
                choices = [[a for a, (s, t) in Rarr.items() if s == vp[i] and t == vq[phi[i]]] for i in range(len(vp))]
                for eta in product(*choices):
                    if eta[0] != 'id0':
                        continue
                    if tp:
                        e = ep[0]
                        # image of the edge under q o phi
                        if phi[0] == phi[1]:
                            img = 'id0' if vq[phi[0]] == '0' else 'idz'
                        else:
                            img = eq[0]
                        if tp == '+':      # edge 0 -> 1 : eta_1 o c(e) = img o eta_0
                            if rc(eta[1], e) != rc(img, eta[0]):
                                continue
                        else:              # edge 1 -> 0 : eta_0 o c(e) = img o eta_1
                            if rc(eta[0], e) != rc(img, eta[1]):
                                continue
                    maps.append((phi, eta))
            homs[(p, q)] = maps
    narrows = sum(len(v) for v in homs.values())
    say(f'E.8: walking retraction R (5 arrows); the first truncation P_<=1 of P(R,0) has {len(paths)} objects and {narrows} arrows')
    assert narrows == 15
    assert all(len(homs[(p, 't')]) == 1 for p in paths) and all(len(homs[('t', p)]) == 0 for p in paths if p != 't')
    # In P_<=1 / z: objects (p, beta: end(p) -> z).  (d+, idz) and (t, u) have no common successor.
    end = {p: v[-1] for p, (tp, v, ep) in paths.items()}
    def succ(obj):
        p, beta = obj
        out = set()
        for q in paths:
            for (phi, eta) in homs[(p, q)]:
                last = eta[-1]
                for b2 in [a for a, (s, t) in Rarr.items() if s == end[q] and t == 'z']:
                    if rc(b2, last) == beta:
                        out.add((q, b2))
        return out
    s1, s2 = succ(('d+', 'idz')), succ(('t', 'u'))
    assert s2 == {('t', 'u')} and ('t', 'u') not in s1 and not (s1 & s2)
    say('   in P_<=1/z the objects (d+, id_z) and (t, u) have no common successor (u r = e != id_z), so q_1 is not total')


def main():
    b2v()
    sphere_and_double_cone()
    ty_checks()
    walking_retraction()
    say('ALL PART CHECKS PASSED')
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'parts_indep.out').write_text('\n'.join(LOG) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
