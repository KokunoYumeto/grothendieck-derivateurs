"""Author's independent check (Claude, Fable 5.2), 10-11 Nov 2026.
Mod-p Betti numbers of the nerve of a small finite category, from the normalized chain complex
(strings of composable non-identity arrows; a face that composes to an identity is dropped).
Used for: P_2 (5-element monoid, claim G.9), P_3 (7-element monoid, G.10), R_2 (3 objects, 9 arrows, G.11).
"""
import itertools, sys
import numpy as np

def rank_mod(M, p):
    M = M.copy() % p
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        if r == rows:
            break
        piv = np.nonzero(M[r:, c])[0]
        if piv.size == 0:
            continue
        i = r + piv[0]
        if i != r:
            M[[r, i]] = M[[i, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        if nz.size:
            M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
    return r

def betti(arrows, src, tgt, comp, ident, top, primes):
    """arrows: list of non-identity arrow names; comp(a,b)= b after a (a first), may return an identity."""
    chains = [None, [(a,) for a in arrows]]
    for k in range(2, top + 2):
        chains.append([s + (a,) for s in chains[k - 1] for a in arrows if tgt[s[-1]] == src[a]])
    nobj = len(set(src.values()) | set(tgt.values()))
    objs = sorted(set(src.values()) | set(tgt.values()))
    out = {}
    for p in primes:
        ranks = {}
        # d1: arrows -> objects
        D = np.zeros((len(objs), len(chains[1])), dtype=np.int64)
        for j, (a,) in enumerate(chains[1]):
            D[objs.index(tgt[a]), j] += 1
            D[objs.index(src[a]), j] -= 1
        ranks[1] = rank_mod(D, p)
        for k in range(2, top + 2):
            idx = {s: i for i, s in enumerate(chains[k - 1])}
            D = np.zeros((len(chains[k - 1]), len(chains[k])), dtype=np.int64)
            for j, s in enumerate(chains[k]):
                faces = [(s[1:], 1), (s[:-1], (-1) ** k)]
                for i in range(1, k):
                    c = comp(s[i - 1], s[i])
                    if c in ident:
                        continue
                    faces.append((s[:i - 1] + (c,) + s[i + 1:], (-1) ** i))
                for f, sg in faces:
                    D[idx[f], j] += sg
            ranks[k] = rank_mod(D, p)
        dims = {0: nobj}
        dims.update({k: len(chains[k]) for k in range(1, top + 2)})
        b = {0: dims[0] - ranks[1]}
        for k in range(1, top + 1):
            b[k] = dims[k] - ranks[k] - ranks[k + 1]
        out[p] = b
    return out

def monoid(elems, mult, one, top, primes):
    arrows = [e for e in elems if e != one]
    src = {a: 0 for a in arrows}; tgt = {a: 0 for a in arrows}
    return betti(arrows, src, tgt, lambda a, b: mult(b, a), {one}, top, primes)

# P_2: 1 and x_ij (i,j in {0,1}), x_ij x_kl = x_il
P2 = ['1'] + [('x', i, j) for i in (0, 1) for j in (0, 1)]
def m2(a, b):
    if a == '1': return b
    if b == '1': return a
    return ('x', a[1], b[2])
# check associativity
assert all(m2(m2(a, b), c) == m2(a, m2(b, c)) for a in P2 for b in P2 for c in P2)
print('P_2 (5 elements): mod-p Betti numbers of BP_2, degrees 0..4:', monoid(P2, m2, '1', 4, [2, 3, 1000003]))

# P_3 = P_2 + {q, r}: x q = x r = x_{i0}, q x = r x = x, q^2 = q r = q, r^2 = r q = r
P3 = P2 + ['q', 'r']
def m3(a, b):
    if a == '1': return b
    if b == '1': return a
    ax = isinstance(a, tuple); bx = isinstance(b, tuple)
    if ax and bx: return ('x', a[1], b[2])
    if ax and not bx: return ('x', a[1], 0)
    if not ax and bx: return b
    return a   # q q = q, q r = q, r r = r, r q = r
assert all(m3(m3(a, b), c) == m3(a, m3(b, c)) for a in P3 for b in P3 for c in P3), 'P_3 not associative'
print('P_3 (7 elements): mod-p Betti numbers of BP_3, degrees 0..4:', monoid(P3, m3, '1', 4, [2, 3]))

# R_2: objects 0,1,2; Hom(i,j) = Z/2 for i<j, composition by addition mod 2; only identities as endomorphisms
arr = [(i, j, e) for i in range(3) for j in range(3) if i < j for e in (0, 1)]
src = {a: a[0] for a in arr}; tgt = {a: a[1] for a in arr}
print('R_2 (3 objects, 9 arrows): mod-p Betti numbers, degrees 0..3:',
      betti(arr, src, tgt, lambda a, b: (a[0], b[1], (a[2] + b[2]) % 2), set(), 3, [2, 3, 1000003]))
