"""Exact finite witness to failure of two-out-of-three, A.5."""
from itertools import product

G = (0, 1)
mul = lambda a, b: (a + b) % 2
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(G, repeat=3))
assert all(mul(0,a)==a==mul(a,0) for a in G)
functions = list(product(G, repeat=2))
equivariant = [f for f in functions if all(f[mul(g,x)] == mul(g,f[x]) for g,x in product(G,repeat=2))]
fixed = [x for x in G if all(mul(g,x)==x for g in G)]
print('C2 associativity and identity: verified')
print('Functions on the regular two-element set:', functions)
print('Equivariant functions:', equivariant)
print('Hom cardinalities: underlying =', len(functions), '; equivariant =', len(equivariant))
print('Fixed points:', fixed, '; underlying points:', list(G))
print('Orbit count: 1; underlying point count: 2')
assert len(equivariant)==2 and len(functions)==4 and fixed==[]
print('The witness is finite; full faithfulness of trivial actions for arbitrary sets is proved in A.5.')
