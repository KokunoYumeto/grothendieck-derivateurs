"""Monoids of a given order with identity 0: all associative tables (no reduction by isomorphism),
split by the value of the first free cell so that several processes can share the work.

Usage: python -I enum_monoids.py ORDER TARGET [FIRST_VALUE]
Looks for tables whose normalized bar complex has the F_2-homology of S^TARGET in degrees
0..TARGET+1; survivors are re-tested modulo 3 and modulo 1000003.  Reviewer's code.
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enum_small_categories import betti


def tables(m, first=None):
    T = [[-1] * m for _ in range(m)]
    for a in range(m):
        T[0][a] = a
        T[a][0] = a
    cells = [(x, y) for x in range(1, m) for y in range(1, m)]
    R = range(m)

    def ok(x, y, v):
        # triples (x,y,z) and (z,x,y)
        for z in R:
            yz = T[y][z]
            if yz >= 0:
                l = T[v][z]
                r = T[x][yz]
                if l >= 0 and r >= 0 and l != r:
                    return False
            zx = T[z][x]
            if zx >= 0:
                l = T[zx][y]
                r = T[z][v]
                if l >= 0 and r >= 0 and l != r:
                    return False
        # triples (a,b,y) with ab = x, and (x,b,c) with bc = y
        for a in R:
            Ta = T[a]
            for b in R:
                if Ta[b] == x:
                    by = T[b][y]
                    if by >= 0:
                        r = Ta[by]
                        if r >= 0 and r != v:
                            return False
                if Ta[b] == y:          # here (a,b) plays the role of (b,c)
                    xb = T[x][a]
                    if xb >= 0:
                        l = T[xb][b]
                        if l >= 0 and l != v:
                            return False
        return True

    def rec(i):
        if i == len(cells):
            for a in R:
                for b in R:
                    ab = T[a][b]
                    for c in R:
                        if T[ab][c] != T[a][T[b][c]]:
                            return
            yield [row[:] for row in T]
            return
        x, y = cells[i]
        values = R if (i > 0 or first is None) else [first]
        for v in values:
            T[x][y] = v
            if ok(x, y, v):
                yield from rec(i + 1)
            T[x][y] = -1
    yield from rec(0)


def main():
    m, target = int(sys.argv[1]), int(sys.argv[2])
    first = int(sys.argv[3]) if len(sys.argv) > 3 else None
    want = [1] + [0] * (target - 1) + [1, 0]
    t0 = time.time()
    count = zero = 0
    surv = []
    src = [0] * m
    tgt = [0] * m
    for T in tables(m, first):
        count += 1
        if any(all(T[z][x] == z for x in range(m)) or all(T[x][z] == z for x in range(m)) for z in range(1, m)):
            zero += 1
            continue
        comp = {(g, f): T[g][f] for g in range(m) for f in range(m)}
        if betti(1, m, src, tgt, comp, target + 1, 2, want) is not None:
            surv.append((T, comp))
    print(f"order={m} first={first} target=S^{target}: tables={count}, with a one-sided zero={zero}, "
          f"F_2-survivors={len(surv)}, time={time.time()-t0:.1f}s")
    final = 0
    for T, comp in surv:
        b3 = betti(1, m, src, tgt, comp, target + 1, 3)
        bP = betti(1, m, src, tgt, comp, target + 1, 1000003)
        cand = (b3 == want and bP == want)
        final += cand
        print(f"  survivor {T} betti mod3={b3} mod1000003={bP} -> " + ("HOMOLOGY OF THE SPHERE" if cand else "excluded"))
    print(f"  tables with the homology of S^{target} through degree {target+1}: {final}")


if __name__ == "__main__":
    main()
