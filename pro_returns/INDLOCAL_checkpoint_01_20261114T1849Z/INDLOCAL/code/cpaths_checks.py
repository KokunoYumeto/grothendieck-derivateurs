"""Independent finite audits for INDLOCAL Part C.

The proofs quantify over arbitrary categories and word lengths.  These finite
calculations check their formulas and the finite crown counterexample.
Run with Python 3; no third-party dependencies are required.
"""
from itertools import product, combinations_with_replacement
from collections import Counter
import json


def words(bound):
    return ["".join(w) for n in range(bound + 1) for w in product("+-", repeat=n)]


def arrow(word, a, b):
    if a <= b:
        return all(s == "+" for s in word[a:b])
    return all(s == "-" for s in word[b:a])


def type_maps(source, target):
    n, m = len(source), len(target)
    if n == 0:
        return [(0,)] if m == 0 else []
    result = []
    for middle in combinations_with_replacement(range(m + 1), n - 1):
        f = (0,) + middle + (m,)
        if all(arrow(target, f[i], f[i+1]) if s == "+" else
               arrow(target, f[i+1], f[i]) for i, s in enumerate(source)):
            result.append(f)
    return result


def letter_maps(source, target):
    """Arrows source -> target in Ty^op, represented on letter positions."""
    return [f for f in combinations_with_replacement(range(len(target)), len(source))
            if all(source[i] == target[f[i]] for i in range(len(source)))]


def to_letters(f, target_length):
    return tuple(next(i for i in range(len(f)-1) if f[i] <= j < f[i+1])
                 for j in range(target_length))


def first_run(word):
    return next((i for i in range(1, len(word)) if word[i] != word[0]), len(word))


def check_clamping(source, target):
    fs = type_maps(source, target)
    if not fs or not target:
        return len(fs)
    a, b = first_run(source), first_run(target)
    if source[0] != target[0]:
        assert all(all(f[i] == 0 for i in range(a+1)) for f in fs)
        assert {f[a:] for f in fs} == set(type_maps(source[a:], target))
    else:
        image = set()
        for f in fs:
            r = (0,) + tuple(max(x, b) for x in f[1:])
            assert r in fs
            assert r[:a+1] == (0,) + (b,)*a
            assert (0,) + tuple(max(x, b) for x in r[1:]) == r
            if source[0] == "+":
                assert all(arrow(target, x, y) for x, y in zip(f, r))
            else:
                assert all(arrow(target, y, x) for x, y in zip(f, r))
            image.add(r)
        suffixes = {tuple(x-b for x in r[a:]) for r in image}
        assert suffixes == set(type_maps(source[a:], target[b:]))
        # On comparable maps, applying the clamp gives comparable maps.
        for f, g in product(fs, repeat=2):
            if all(arrow(target, x, y) for x, y in zip(f, g)):
                rf, rg = (0,)+tuple(max(x,b) for x in f[1:]), (0,)+tuple(max(x,b) for x in g[1:])
                assert all(arrow(target, x, y) for x, y in zip(rf, rg))
    return len(fs)


def main():
    output = {}
    ws = words(4)
    for s, t in product(ws, repeat=2):
        assert set(to_letters(f, len(t)) for f in type_maps(s, t)) == set(letter_maps(t, s))
    output["vertex_letter_bijection_pairs"] = len(ws)**2

    count = 0
    short = words(3)
    for s, t, u in product(short, repeat=3):
        for f, g in product(type_maps(s,t), type_maps(t,u)):
            composite = tuple(g[x] for x in f)
            ff, gg = to_letters(f,len(t)), to_letters(g,len(u))
            assert to_letters(composite,len(u)) == tuple(ff[x] for x in gg)
            count += 1
    output["contravariant_compositions"] = count

    counts = Counter()
    for s,t in product(words(5),words(4)):
        number = check_clamping(s,t)
        counts["pairs"] += 1
        counts["nonempty_pairs"] += bool(number)
        counts["maps"] += number
    output["cp1_clamping"] = dict(counts)

    e,c=(0,2),(0,0)
    count=0
    for t in words(9):
        gs=letter_maps("+-+",t)
        left=set()
        right=set()
        for g in gs:
            assert g[0] < g[1] < g[2]
            ge,gc=tuple(g[i] for i in e),tuple(g[i] for i in c)
            assert ge[0] < ge[1] and gc[0] == gc[1]
            left.add(ge);right.add(gc)
            assert int(ge[0] != ge[1]) - int(gc[0] != gc[1]) == 1
            count+=1
        assert not left.intersection(right)
    output["r8_dual_certificate_arrows"] = count
    output["r8_target_words"] = len(words(9))

    base=set((i,i) for i in range(4)) | {(0,1),(0,3),(2,1),(2,3)}
    edges=sorted(base-set((i,i) for i in range(4)))
    crown_checks=0
    for bits in product((0,1),repeat=4):
        marked=set((i,i) for i in range(4)) | {x for x,b in zip(edges,bits) if b}
        for n in range(1,8):
            for sign in "+-":
                paths=[]
                for mid in product(range(4),repeat=n-1):
                    p=(0,)+mid+(0,)
                    if all(((p[i],p[i+1]) in base) if sign=="+" else
                           ((p[i+1],p[i]) in marked) for i in range(n)):
                        paths.append(p)
                assert paths == [(0,)*(n+1)]
                crown_checks+=1
    output["crown_onesign_marking_length_checks"] = crown_checks
    # Nerve of the crown is a connected graph with four edges and vertices.
    assert len(edges)-4+1 == 1
    for k in range(-12,13):
        for j in (k-1,k+1):
            directed=(k,j) if k%2==0 else (j,k)
            assert tuple(x%4 for x in directed) in base
    output["crown_nerve_betti"] = [1,1]

    # Check the ACTUAL left, right and symmetric padding maps for (+,-,+).
    d=3
    count=0
    for n,p in product(range(1,5),repeat=2):
        word="+-+"
        left=lambda i:max(0,i-p*d)
        right=lambda i:min(i,n*d)
        sym=lambda i:min(max(0,i-p*d),2*n*d)
        ql_big=lambda i:min(i,(n+p)*d)
        qr_big=lambda i:max(0,i-(n+p)*d)
        ql=lambda i:min(i,n*d)
        qr=lambda i:max(0,i-n*d)
        for i in range(2*(n+p)*d+1):
            assert left(ql_big(i)) == ql(sym(i))
            assert right(qr_big(i)) == qr(sym(i))
        for source,target,f in [
            (word*(n+p),word*n,tuple(left(i) for i in range((n+p)*d+1))),
            (word*(n+p),word*n,tuple(right(i) for i in range((n+p)*d+1))),
            (word*(2*(n+p)),word*(2*n),tuple(sym(i) for i in range(2*(n+p)*d+1)))]:
            assert all(arrow(target,f[i],f[i+1]) if s=="+" else
                       arrow(target,f[i+1],f[i]) for i,s in enumerate(source))
        count+=1
    output["plus_minus_plus_padding_squares"] = count
    print(json.dumps(output,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
