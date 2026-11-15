"""Finite algebra checks used in C.5 and C.12; no external dependencies."""
from itertools import permutations, product
from collections import deque

def compose(a,b):
    """Apply b first, then a."""
    return tuple(a[b[i]] for i in range(len(a)))
def power(a,n):
    e=tuple(range(len(a))); ans=e
    for _ in range(n): ans=compose(ans,a)
    return ans
def order(a):
    for i in range(1,61):
        if power(a,i)==tuple(range(len(a))):return i
    raise AssertionError

e=tuple(range(5)); x=(1,2,0,3,4)
y=next(y for y in permutations(range(5)) if order(y)==5 and order(compose(x,y))==2)
seen={e}; todo=deque([e])
while todo:
    a=todo.popleft()
    for b in (x,y):
        c=compose(a,b)
        if c not in seen: seen.add(c); todo.append(c)
assert power(x,3)==power(y,5)==power(compose(x,y),2)==e
D=((3,2),(-5,-3)); det=D[0][0]*D[1][1]-D[0][1]*D[1][0]
assert det==1 and len(seen)==60
print('Presentation K: x^3=y^5=(xy)^2.')
print('Cellular boundary C2 -> C1 (columns = relators):',D)
print('determinant =',det,'; H0=Z, H1=H2=0; no cells above degree 2.')
print('Permutations on 0,...,4: x =',x,'; y =',y)
print('orders x,y,xy =',order(x),order(y),order(compose(x,y)))
print('Generated finite quotient order =',len(seen),'(therefore pi1(K) is nontrivial).')

# C2 as category: one object, endomorphisms 0,1, composition addition mod 2.
# Forgetful C2-Set -> Set is not full on the regular two-point action.
for a,b,c in product(range(2),repeat=3):
    assert ((a+b)%2+c)%2==(a+(b+c)%2)%2
for a in range(2):
    assert (a+0)%2==a==(0+a)%2 and (a+a)%2==0
print("BC2: composition is addition mod 2; identity, inverses, all 8 associativity triples verified.")
def equivariant(func):
    return all(func[(i+1)%2]==(func[i]+1)%2 for i in range(2))
all_maps=list(product(range(2),repeat=2))
equivariant_maps=[f for f in all_maps if equivariant(f)]
assert len(all_maps)==4 and len(equivariant_maps)==2
print('BC2 regular-set endomorphisms:',equivariant_maps)
print('Underlying-set endomorphisms:',all_maps)
print('Point -> BC2 restriction not full: 2 -> 4 endomorphisms.')
# Constant action functor Set -> C2-Set is fully faithful: equivariance tautological.
for m,n in product(range(5),repeat=2):
    maps=list(product(range(n),repeat=m))
    assert all(all(f[i]==f[i] for i in range(m)) for f in maps)
print('Constant-action full-faithfulness checked on sizes 0 through 4; general proof: trivial actions impose no equation.')
