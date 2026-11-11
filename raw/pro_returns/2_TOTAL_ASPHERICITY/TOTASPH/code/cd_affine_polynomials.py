"""Construct and verify integral affine equalizers for Delta_inj.

The algorithm implements polynomial interpolation on the coordinate
hyperplanes x_i=z_i-z_{i+1}=0. All arithmetic is exact in Z.
"""
from itertools import combinations
from functools import lru_cache
import sympy as s

@lru_cache(None)
def cone(n,k):
    z=s.symbols('z:'+str(n+2))
    if n==0:return s.Integer(1)
    y=s.symbols('y:'+str(n+1))
    old=s.symbols('z:'+str(n+1))
    Q=cone(n-1,2*k).subs(dict(zip(old,y)),simultaneous=True)
    F=[s.expand(Q*s.prod(y[l]**k for l in range(n+1) if l!=i)) for i in range(n+1)]
    x=s.symbols('x:'+str(n+1));u=s.Symbol('u')
    lifts=[]
    for i in range(n+1):
        lift=F[i].subs({y[l]:z[l] if l<=i else z[l+1] for l in range(n+1)},simultaneous=True)
        lifts.append(s.expand(lift.subs({z[l]:u+sum(x[j] for j in range(l,n+1)) for l in range(n+2)},simultaneous=True)))
    C=0
    for r in range(1,n+2):
        for S in combinations(range(n+1),r):
            C+=(-1)**(r+1)*lifts[S[0]].subs({x[j]:0 for j in S})
    return s.expand(C.subs({**{x[j]:z[j]-z[j+1] for j in range(n+1)},u:z[-1]},simultaneous=True))

for n in range(4):
    z=s.symbols('z:'+str(n+2));y=s.symbols('y:'+str(n+1))
    C=cone(n,1);poly=s.Poly(C,*z)
    faces=[s.expand(y[i]*C.subs({z[l]:y[l] if l<=i else y[l-1] for l in range(n+2)},simultaneous=True)) for i in range(n+1)]
    assert all(v==faces[0] for v in faces)
    assert C.subs({v:1 for v in z})==1
    degrees={sum(m) for m,c in poly.terms()}
    assert len(degrees)==1
    degree=next(iter(degrees))
    assert degree==2**(n+1)-n-2
    # Recover the actual injections and verify face equality as dictionaries.
    M=n+degree
    terms=[]
    for gaps,c in poly.terms():
        injection=tuple(sum(gaps[:l+1])+l for l in range(n+1))
        assert 0<=injection[0] and injection[-1]<=M
        assert all(injection[j]<injection[j+1] for j in range(n))
        terms.append((injection,int(c)))
    face_dicts=[]
    for i in range(n+1):
        d={}
        for inj,c in terms:
            f=inj[:i]+inj[i+1:];d[f]=d.get(f,0)+c
        face_dicts.append({f:c for f,c in d.items() if c})
    assert all(d==face_dicts[0] for d in face_dicts)
    print({'source_ordinal':n,'target_ordinal':M,'degree':degree,'nonzero_terms':len(terms),'augmentation':sum(c for inj,c in terms),'equal_faces':True})
    if n<=2:print('terms =',sorted(terms))
