"""Does the triple v_0, v_1, v_2 : V -> W acquire a (rational / F_p) simultaneous affine equalizer at some object
of the computed AKR stages?  For each object r: T_r : Z[A(W,r)] -> Z[A(V,r)]^2, t |-> (t(v_1 - v_0), t(v_2 - v_0)).
A rational simultaneous affine equalizer at r exists iff the augmentation functional is NOT in the row space of
T_r, i.e. iff rank [T_r ; aug] > rank T_r.  Ranks are computed modulo a large prime (and mod 2, 3).  Same for the
pairs (v_0, v_1) and (v_0, v_2).  Own code (akr_indep.py); review of TOTEX, 12 Nov 2026.
Usage: python -I akr_triple_equalizers.py [--literal-common-n] [--k2] [--k3crit]"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import akr_indep as A

def rank_rows(rows, p):
    """rank of a list of sparse row vectors {col: value} modulo p (Gaussian elimination)."""
    return A.rank_mod({i: r for i, r in enumerate(rows)}, p)

def test(C, label, primes=(1000003, 2, 3)):
    out = []
    for r in range(len(C.size)):
        Wr = sorted(C.hom.get((1, r), ())); Vr = sorted(C.hom.get((0, r), ()))
        if not Wr: continue
        vidx = {f[0]: i for i, f in enumerate(Vr)}        # an arrow V -> r is its image point
        cols = {}
        for j, c in enumerate(Wr):                          # column of the basis element c : W -> r
            col = {}
            for blk, (a, b) in enumerate(((1, 0), (2, 0))):
                for pt, sgn in ((c[a], 1), (c[b], -1)):
                    key = blk * len(Vr) + vidx[pt]; col[key] = col.get(key, 0) + sgn
            cols[j] = {k: v for k, v in col.items() if v}
        res = {}
        for name, blocks in (('triple', (0, 1)), ('pair01', (0,)), ('pair02', (1,))):
            # rows of T restricted to the chosen blocks, as functionals on t (indexed by j)
            rows = {}
            for j, col in cols.items():
                for k, v in col.items():
                    if k // len(Vr) in blocks: rows.setdefault(k, {})[j] = v
            R = list(rows.values()); aug = {j: 1 for j in cols}
            res[name] = {p: rank_rows(R + [aug], p) > rank_rows(R, p) for p in primes}
        out.append((C.name[r], len(Wr), res))
    print(label)
    for name, n, res in out:
        print(f"  {name:>14} |A(W,r)|={n:>6}  " + "  ".join(
            f"{k}: " + "".join('Y' if res[k][p] else '-' for p in primes) for k in ('triple', 'pair01', 'pair02')))
    print("  (Y/- per prime 1000003, 2, 3: an affine equalizer at r exists over that field / does not)", flush=True)

if __name__ == '__main__':
    C = A.Cat(); A.stage_K1(C)
    test(C, ('LITERAL' if A.LITERAL else 'REPAIRED') + ' K1')
    if '--k2' in sys.argv:
        t = C.name.index('Q_0_1_0_1'); fs = sorted(C.hom[(1, t)]); f, g = fs[:2]
        A.quasi_filter(C, 'Q_K2', 1, t, f, g, 153)
        test(C, 'K1 + one K2 quasi-filter')
    if '--k3crit' in sys.argv:
        left = C.name.index('Q_0_1_0_1'); right = C.name.index('Q_0_1_1_0')
        t, _ = C.add_target('S_K2', [(left, tuple(('L', i) for i in range(C.size[left]))),
                                      (right, tuple(('R', i) for i in range(C.size[right])))],
                            [('L', i) for i in range(C.size[left])] + [('R', i) for i in range(C.size[right])])
        lf = next(iter(C.hom[(left, t)])); rg = next(iter(C.hom[(right, t)]))
        f = tuple(lf[j] for j in sorted(C.hom[(1, left)])[0]); g = tuple(rg[j] for j in sorted(C.hom[(1, right)])[0])
        A.quasi_filter(C, 'Q_K3', 1, t, f, g, 297)
        test(C, 'K1 + K2 sum + K3 quasi-filter')
