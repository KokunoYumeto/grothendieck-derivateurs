"""Independent enumeration of small finite categories (review of CATHOT, Part G).

Written by the reviewer (Claude); shares no code with the answer's code/ folder.
Usage:  python -I enum_small_categories.py N_OBJECTS N_ARROWS TARGET
  TARGET = 2 or 3: look for tables whose normalized nerve has the F_2-homology of S^TARGET
  in degrees 0..TARGET+1; survivors are re-tested modulo 3 and modulo a large prime.
Arrows 0..n-1 are the identities.  Every assignment of (source,target) to the other arrows
(as a multiset of pairs) and every associative composition table is visited; no reduction
by isomorphism.  Only connected categories are kept.
"""
import sys, itertools, time


def enumerate_tables(n, m):
    """yield (src, tgt, comp) with comp[(g,f)] = g after f, for all categories with n objects, m arrows."""
    pairs = [(s, t) for s in range(n) for t in range(n)]
    for choice in itertools.combinations_with_replacement(pairs, m - n):
        src = list(range(n)) + [p[0] for p in choice]
        tgt = list(range(n)) + [p[1] for p in choice]
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a in range(n, m):
            parent[find(src[a])] = find(tgt[a])
        if len({find(x) for x in range(n)}) != 1:
            continue
        non = list(range(n, m))
        cells = [(g, f) for g in non for f in non if tgt[f] == src[g]]
        cand = {}
        ok = True
        for (g, f) in cells:
            c = [h for h in range(m) if src[h] == src[f] and tgt[h] == tgt[g]]
            if not c:
                ok = False
                break
            cand[(g, f)] = c
        if not ok:
            continue
        comp = {}
        for a in range(m):          # products with identities
            comp[(a, src[a])] = a
            comp[(tgt[a], a)] = a

        def assoc_ok(h, g, f):
            # (h g) f == h (g f), only when everything is defined and known
            if tgt[f] != src[g] or tgt[g] != src[h]:
                return True
            hg = comp.get((h, g))
            gf = comp.get((g, f))
            if hg is None or gf is None:
                return True
            l = comp.get((hg, f))
            r = comp.get((h, gf))
            if l is None or r is None:
                return True
            return l == r

        def rec(i):
            if i == len(cells):
                for h in range(m):      # full check, for safety
                    for g in range(m):
                        if tgt[g] != src[h]:
                            continue
                        for f in range(m):
                            if tgt[f] != src[g]:
                                continue
                            if comp[(comp[(h, g)], f)] != comp[(h, comp[(g, f)])]:
                                return
                yield dict(comp)
                return
            (g, f) = cells[i]
            for v in cand[(g, f)]:
                comp[(g, f)] = v
                good = True
                for z in range(m):
                    if not (assoc_ok(g, f, z) and assoc_ok(z, g, f)):
                        good = False
                        break
                if good:
                    for (a, b), ab in list(comp.items()):
                        if ab == g and not assoc_ok(a, b, f):
                            good = False
                            break
                        if ab == f and not assoc_ok(g, a, b):
                            good = False
                            break
                if good:
                    yield from rec(i + 1)
                del comp[(g, f)]
        for table in rec(0):
            yield src, tgt, table


def chains(n, m, src, tgt, kmax):
    non = list(range(n, m))
    C = [[(x,) for x in range(n)]]            # degree 0: objects
    C.append([(a,) for a in non])
    for k in range(2, kmax + 1):
        C.append([c + (a,) for c in C[-1] for a in non if src[a] == tgt[c[-1]]])
    return C


def boundary_rows(n, m, src, tgt, comp, C, k):
    """rows of d_k: C_k -> C_{k-1} as dict col->coeff; strings are (f1,...,fk), f1 applied first."""
    index = {c: i for i, c in enumerate(C[k - 1])}
    rows = []
    for c in C[k]:
        row = {}

        def add(face, sign):
            if face is None:
                return
            j = index[face]
            row[j] = row.get(j, 0) + sign
        if k == 1:
            a = c[0]
            add((tgt[a],), 1)
            add((src[a],), -1)
        else:
            add(c[1:], 1)
            for i in range(k - 1):
                p = comp[(c[i + 1], c[i])]
                add(None if p < n else c[:i] + (p,) + c[i + 2:], (-1) ** (i + 1))
            add(c[:-1], (-1) ** k)
        rows.append(row)
    return rows


def rank_mod(rows, p):
    if p == 2:
        basis = {}
        r = 0
        for row in rows:
            v = 0
            for j, c in row.items():
                if c & 1:
                    v |= 1 << j
            while v:
                hb = v.bit_length() - 1
                if hb in basis:
                    v ^= basis[hb]
                else:
                    basis[hb] = v
                    r += 1
                    break
        return r
    piv = {}
    r = 0
    for row in rows:
        v = {j: c % p for j, c in row.items() if c % p}
        while v:
            j = max(v)
            if j in piv:
                b = piv[j]
                fac = v[j]
                for jj, cc in b.items():
                    nv = (v.get(jj, 0) - fac * cc) % p
                    if nv:
                        v[jj] = nv
                    else:
                        v.pop(jj, None)
            else:
                inv = pow(v[j], p - 2, p)
                piv[j] = {jj: cc * inv % p for jj, cc in v.items()}
                r += 1
                break
    return r


def betti(n, m, src, tgt, comp, kmax, p, want=None):
    """Betti numbers b_0..b_kmax over F_p; returns None early if they deviate from `want`."""
    C = chains(n, m, src, tgt, kmax + 1)
    ranks = {0: 0}
    out = []
    for k in range(0, kmax + 1):
        if k + 1 not in ranks:
            ranks[k + 1] = rank_mod(boundary_rows(n, m, src, tgt, comp, C, k + 1), p)
        if k not in ranks:
            ranks[k] = rank_mod(boundary_rows(n, m, src, tgt, comp, C, k), p)
        b = len(C[k]) - ranks[k] - ranks[k + 1]
        out.append(b)
        if want is not None and b != want[k]:
            return None
    return out


def main():
    n, m, target = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    want = [1] + [0] * (target - 1) + [1, 0]
    t0 = time.time()
    count = 0
    zero = 0
    surv2 = []
    for src, tgt, comp in enumerate_tables(n, m):
        count += 1
        if n == 1:
            # a one-sided zero z (z.x = z for all x, or x.z = z for all x) gives a natural
            # transformation between the identity functor and a constant one: contractible nerve
            if any(all(comp[(z, x)] == z for x in range(m)) or all(comp[(x, z)] == z for x in range(m))
                   for z in range(1, m)):
                zero += 1
                continue
        if betti(n, m, src, tgt, comp, target + 1, 2, want) is not None:
            surv2.append((list(src), list(tgt), comp))
    print(f"objects={n} arrows={m} target=S^{target}: tables={count}, with one-sided zero "
          f"(skipped, contractible)={zero}, F_2-survivors={len(surv2)}, time={time.time()-t0:.1f}s")
    P = 1000003
    final = 0
    for src, tgt, comp in surv2:
        b3 = betti(n, m, src, tgt, comp, target + 1, 3)
        bP = betti(n, m, src, tgt, comp, target + 1, P)
        tab = [[comp.get((g, f), '.') for f in range(m)] for g in range(m)]
        cand = (b3 == want and bP == want)
        if cand:
            final += 1
        print(f"  survivor src={src} tgt={tgt} table[g][f]=g after f: {tab} betti mod3={b3} mod{P}={bP} -> "
              + ("HOMOLOGY OF THE SPHERE mod 2,3,P" if cand else "excluded"))
    print(f"  tables with the homology of S^{target} through degree {target+1} (mod 2, 3, {P}): {final}")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
