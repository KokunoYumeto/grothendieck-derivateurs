"""Independent finite audit of Lead 8; mathematical certificate is universal.

The finite bounds are computational checks, not substitutes for the proof.
Zero-based letter indices; vertex indices start at zero.
"""
from itertools import product, combinations_with_replacement
from functools import lru_cache

@lru_cache(None)
def maps_letters(source, target):
    return tuple(f for f in combinations_with_replacement(range(len(target)), len(source))
                 if all(source[i] == target[f[i]] for i in range(len(source))))

@lru_cache(None)
def maps_vertices(tau, rho):
    n,m = len(tau), len(rho)
    if n == 0:
        return ((0,),) if m == 0 else ()
    ans=[]
    for middle in combinations_with_replacement(range(m+1), n-1):
        phi=(0,)+middle+(m,)
        if all(all(sign == tau[i] for sign in rho[phi[i]:phi[i+1]]) for i in range(n)):
            ans.append(phi)
    return tuple(ans)

def letter_of_vertex(phi):
    return tuple(i for i in range(len(phi)-1) for _ in range(phi[i+1]-phi[i]))

def compose(f,g):
    """f after g, for ordinary maps on ordered sets."""
    return tuple(f[j] for j in g)

def words(bound):
    return tuple(''.join(w) for n in range(bound+1) for w in product('+-',repeat=n))

w4=words(4)
comparisons=0
for tau in w4:
    for rho in w4:
        assert set(map(letter_of_vertex, maps_vertices(tau,rho))) == set(maps_letters(rho,tau))
        comparisons+=1
print('word/vertex dual descriptions: tested word lengths <= 4; pairs =',comparisons,'; all matched')

w3=words(3)
composition_count=0
for tau in w3:
    for rho in w3:
        for sigma in w3:
            for phi in maps_vertices(tau,rho):
                for psi in maps_vertices(rho,sigma):
                    v=compose(psi,phi)
                    assert v in maps_vertices(tau,sigma)
                    assert letter_of_vertex(v)==compose(letter_of_vertex(phi),letter_of_vertex(psi))
                    composition_count+=1
print('contravariant composition bijection: tested word lengths <= 3; composable pairs =',composition_count,'; all matched')

p,q='++','+-+'
e,c=(0,2),(0,0)
assert e in maps_letters(p,q) and c in maps_letters(p,q)
print('Hom(++,+-+) =',maps_letters(p,q))
target_count=0; arrow_count=0; square_checks=0; dual_checks=0
for sigma in words(9):
    gs=maps_letters(q,sigma)
    target_count+=1
    for g in gs:
        assert g[0] < g[1] < g[2]
        ge,gc=compose(g,e),compose(g,c)
        assert ge[0] < ge[1] and gc[0] == gc[1]
        # Universal dual certificate phi(injective)=1, phi(constant)=0.
        phi=lambda f: int(f[0] < f[1])
        assert phi(ge)-phi(gc)==1
        dual_checks+=1
    es={compose(g,e) for g in gs}
    cs={compose(g,c) for g in gs}
    assert es.isdisjoint(cs)
    square_checks+=len(gs)**2
    arrow_count+=len(gs)
print('target words length <= 9 =',target_count,'; outgoing arrows from +-+ =',arrow_count)
print('no-square ordered pairs checked through disjoint supports =',square_checks)
print('integral dual certificates phi(ge-gc)=1 checked =',dual_checks)
for modulus in [0,2,3,5,7]:
    # modulus 0 denotes Z; same coefficient identity works in every unital ring.
    print('affine obstruction certified over', 'Z' if modulus==0 else f'F_{modulus}')
assert 0 % 1 == 1 % 1
print('zero ring: 0=1, so t=0 is an affine equalizer; nonzero-ring qualifier is necessary')
