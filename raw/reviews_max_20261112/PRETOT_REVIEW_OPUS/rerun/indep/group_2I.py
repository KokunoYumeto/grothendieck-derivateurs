"""The group of the PRETOT presentation complex: G = <a,b | a^5 b^-3, b^3 (ab)^-2>.

Independent computation (Claude Opus 5.5, 12 Nov 2026), pure Python:
  1. Todd-Coxeter coset enumeration over the trivial subgroup (HLT with
     coincidence processing): |G|.
  2. The regular permutation representation: orders of a, b, ab, z = a^5;
     centre; derived subgroup (perfectness); abelianization from the relation matrix.
  3. The map a -> (1 4 3 2 5), b -> (1 2 3) to A_5 (right-to-left composition):
     a homomorphism onto A_5 with kernel exactly the centre {1, z}.
  4. An explicit isomorphism G -> SL(2,5): matrices A, B in SL(2,F_5) with
     A^5 = B^-3... relators satisfied, generating all of SL(2,5); z -> -I.
Usage: python -I group_2I.py <output_dir>
"""
import sys
import json
from pathlib import Path
from itertools import product

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
LOG = []


def say(s):
    print(s)
    LOG.append(s)


# generators: 0=a, 1=a^-1, 2=b, 3=b^-1
INV = [1, 0, 3, 2]


def word(s):
    m = {'a': 0, 'A': 1, 'b': 2, 'B': 3}
    return [m[c] for c in s]


RELATORS = [word('aaaaaBBB'), word('bbbBABA')]   # a^5 b^-3 ; b^3 (ab)^-2 = b^3 B A B A


def todd_coxeter(relators, ngens=4, max_cosets=200000):
    table = [[None] * ngens]
    parent = [0]           # union-find for coincidences; parent[c]==c means alive
    queue = []

    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c

    def define(c, g):
        if len(table) >= max_cosets:
            raise RuntimeError('coset limit')
        d = len(table)
        table.append([None] * ngens)
        parent.append(d)
        table[c][g] = d
        table[d][INV[g]] = c
        return d

    def coincidence(a, b):
        a, b = find(a), find(b)
        if a == b:
            return
        if a > b:
            a, b = b, a
        parent[b] = a
        queue.append(b)
        while queue:
            e = queue.pop()
            for g in range(ngens):
                f = table[e][g]
                if f is None:
                    continue
                table[f][INV[g]] = None
                e1, f1 = find(e), find(f)
                if table[e1][g] is not None:
                    x, y = find(table[e1][g]), f1
                    if x != y:
                        x, y = min(x, y), max(x, y)
                        parent[y] = x
                        queue.append(y)
                elif table[f1][INV[g]] is not None:
                    x, y = find(table[f1][INV[g]]), e1
                    if x != y:
                        x, y = min(x, y), max(x, y)
                        parent[y] = x
                        queue.append(y)
                else:
                    table[e1][g] = f1
                    table[f1][INV[g]] = e1

    def scan_and_fill(c, w):
        f = c
        bk = c
        i = 0
        j = len(w) - 1
        while True:
            while i <= j and table[f][w[i]] is not None:
                f = table[f][w[i]]
                i += 1
            if i > j:
                if f != bk:
                    coincidence(f, bk)
                return
            while j >= i and table[bk][INV[w[j]]] is not None:
                bk = table[bk][INV[w[j]]]
                j -= 1
            if j < i:
                coincidence(f, bk)
                return
            if i == j:
                table[f][w[i]] = bk
                table[bk][INV[w[i]]] = f
                return
            define(f, w[i])

    c = 0
    while c < len(table):
        if find(c) == c:
            for w in relators:
                if find(c) != c:
                    break
                scan_and_fill(c, w)
            if find(c) == c:
                for g in range(ngens):
                    if table[c][g] is None:
                        define(c, g)
        c += 1
    alive = [x for x in range(len(table)) if find(x) == x]
    idx = {x: i for i, x in enumerate(alive)}
    perms = []
    for g in range(ngens):
        perms.append(tuple(idx[find(table[x][g])] for x in alive))
    return len(alive), perms


def pmul(p, q):          # p after q, as maps on points (right-to-left)
    return tuple(p[x] for x in q)


def pinv(p):
    r = [0] * len(p)
    for i, x in enumerate(p):
        r[x] = i
    return tuple(r)


def porder(p):
    e = tuple(range(len(p)))
    k, q = 1, p
    while q != e:
        q = pmul(p, q)
        k += 1
    return k


def closure(gens, ident):
    seen = {ident}
    todo = [ident]
    while todo:
        x = todo.pop()
        for g in gens:
            y = pmul(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def main():
    n, perms = todd_coxeter(RELATORS)
    say(f'Todd-Coxeter over the trivial subgroup: |G| = {n}')
    assert n == 120
    # The coset action is a right action: coset.x ; as permutations, word w acts by composing left to right.
    a, A, b, B = perms
    e = tuple(range(n))
    # right-action convention: the permutation of a word x1 x2 ... is x_k o ... o x1 as maps (apply x1 first)
    def wperm(s):
        p = e
        for ch in s:
            g = {'a': a, 'A': A, 'b': b, 'B': B}[ch]
            p = pmul(g, p)
        return p
    for rel in ('aaaaaBBB', 'bbbBABA'):
        assert wperm(rel) == e
    z = wperm('aaaaa')
    assert z != e and pmul(z, z) == e
    assert wperm('bbb') == z and wperm('abab') == z
    say(f'orders: a -> {porder(a)}, b -> {porder(b)}, ab -> {porder(wperm("ab"))}, z = a^5 = b^3 = (ab)^2 -> {porder(z)}')
    G = closure([a, b], e)
    assert len(G) == 120   # regular representation is faithful of degree 120
    centre = [g for g in G if pmul(g, a) == pmul(a, g) and pmul(g, b) == pmul(b, g)]
    assert sorted(centre) == sorted([e, z])
    say('centre Z(G) = {1, z}, z = a^5 of order 2')
    # derived subgroup: normal closure of [a,b]
    comm = pmul(pmul(pinv(a), pinv(b)), pmul(a, b))
    conj = {pmul(pmul(g, comm), pinv(g)) for g in G}
    D = closure(list(conj), e)
    say(f'derived subgroup order {len(D)} (perfect: {len(D) == 120})')
    assert len(D) == 120
    say('abelianization: relation matrix [[5,-3],[-2,1]] (exponent sums of a, b), determinant -1, so G^ab = 0')
    assert 5 * 1 - (-3) * (-2) == -1
    # element orders census
    census = {}
    for g in G:
        census[porder(g)] = census.get(porder(g), 0) + 1
    say(f'element-order census: {dict(sorted(census.items()))}')
    # 2I has orders 1:1, 2:1, 3:20, 4:30, 5:24, 6:20, 10:24
    assert census == {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}

    # ---- the map to A_5 ----
    def perm5(cycle):
        p = list(range(5))
        for i, x in enumerate(cycle):
            p[x - 1] = cycle[(i + 1) % len(cycle)] - 1
        return tuple(p)
    pa, pb = perm5((1, 4, 3, 2, 5)), perm5((1, 2, 3))
    e5 = tuple(range(5))
    img = {'a': pa, 'A': pinv(pa), 'b': pb, 'B': pinv(pb)}
    # A word x1 x2 ... xk is sent to the product phi(x1) phi(x2) ... phi(xk) with
    # right-to-left composition of permutations (the return's convention).
    def w5(s):
        p = e5
        for ch in s:
            p = pmul(p, img[ch])
        return p
    assert w5('aaaaaBBB') == e5 and w5('bbbBABA') == e5
    # BFS over the Cayley graph: element of G (regular perm) -> image in S_5
    # In the regular perm convention above, wperm(s + ch) = gen(ch) o wperm(s).
    gens = {'a': a, 'A': A, 'b': b, 'B': B}
    phi = {e: e5}
    todo = [e]
    while todo:
        x = todo.pop()
        for ch, g in gens.items():
            y = pmul(g, x)
            val = pmul(phi[x], img[ch])
            if y in phi:
                assert phi[y] == val, 'map to A_5 not well defined'
            else:
                phi[y] = val
                todo.append(y)
    image = set(phi.values())
    assert len(phi) == 120 and len(image) == 60
    assert all(sum(1 for i in range(5) for j in range(i + 1, 5) if p[i] > p[j]) % 2 == 0 for p in image)
    kernel = sorted(g for g in G if phi[g] == e5)
    assert kernel == sorted([e, z])
    say('a -> (1 4 3 2 5), b -> (1 2 3): well-defined homomorphism G -> A_5, onto (60 even permutations), kernel = {1, z} = Z(G)')

    # ---- explicit isomorphism with SL(2,5) ----
    p = 5
    def mm(X, Y):
        return ((X[0] * Y[0] + X[1] * Y[2]) % p, (X[0] * Y[1] + X[1] * Y[3]) % p,
                (X[2] * Y[0] + X[3] * Y[2]) % p, (X[2] * Y[1] + X[3] * Y[3]) % p)
    I2 = (1, 0, 0, 1)
    SL = [X for X in product(range(p), repeat=4) if (X[0] * X[3] - X[1] * X[2]) % p == 1]
    assert len(SL) == 120
    def mpow(X, k):
        Y = I2
        for _ in range(k):
            Y = mm(Y, X)
        return Y
    def minv(X):
        return (X[3], (-X[1]) % p, (-X[2]) % p, X[0])
    def mclosure(gs):
        seen = {I2}
        todo = [I2]
        while todo:
            x = todo.pop()
            for g in gs:
                y = mm(x, g)
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        return seen
    found = None
    for X in SL:
        X5 = mpow(X, 5)
        if X5 == I2:
            continue
        for Y in SL:
            if mpow(Y, 3) == X5 and mpow(mm(X, Y), 2) == X5 and len(mclosure([X, Y])) == 120:
                found = (X, Y)
                break
        if found:
            break
    assert found
    MA, MB = found
    minus = ((-1) % p, 0, 0, (-1) % p)
    assert mpow(MA, 5) == minus
    mimg = {'a': MA, 'A': minv(MA), 'b': MB, 'B': minv(MB)}
    psi = {e: I2}
    todo = [e]
    while todo:
        x = todo.pop()
        for ch, g in gens.items():
            y = pmul(g, x)
            val = mm(psi[x], mimg[ch])
            if y in psi:
                assert psi[y] == val
            else:
                psi[y] = val
                todo.append(y)
    assert len(psi) == 120 and len(set(psi.values())) == 120   # bijective onto SL(2,5)
    assert psi[z] == minus
    say(f'isomorphism G -> SL(2,5): a -> {MA}, b -> {MB} (entries a11,a12,a21,a22 mod 5); bijective; z -> -I')
    say('Hence G = <a,b | a^5 = b^3 = (ab)^2> is the binary icosahedral group 2I = SL(2,5), order 120, perfect,')
    say('centre {1,z} = {+-1}, and the A_5 map of the return is the quotient by the centre, G/Z(G) = PSL(2,5) = A_5.')
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'group_2I.out').write_text('\n'.join(LOG) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
