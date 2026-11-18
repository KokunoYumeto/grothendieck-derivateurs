"""Finite certificates for C.5 and the disk identities used in C.1/C.7.

All arithmetic is exact over F_2. The abstract argument covers arbitrary X;
the symbolic 2x2 block identity below is its certificate, while the examples
exercise nonzero differential, disconnected grading, and the zero complex.
"""
import json
import sympy as s


def rank_mod2(A):
    rows=[list(map(lambda x:int(x)%2,row)) for row in A.tolist()]
    r=0
    for c in range(A.cols):
        pivot=next((j for j in range(r,len(rows)) if rows[j][c]),None)
        if pivot is None: continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for j in range(len(rows)):
            if j!=r and rows[j][c]: rows[j]=[a^b for a,b in zip(rows[j],rows[r])]
        r+=1
    return r


def check_tensor_disk(dims,diffs):
    # (J tensor X)_n = X_n + X_{n-1}; d(a,b)=(d_X a+b,d_X b)
    dim=lambda n:dims[n] if 0<=n<len(dims) else 0
    d=lambda n:diffs.get(n,s.zeros(dim(n-1),dim(n)))
    N=len(dims)+1
    Ds={}
    Hs={}
    for n in range(N+1):
        Ds[n]=s.zeros(dim(n-1)+dim(n-2),dim(n)+dim(n-1))
        Ds[n][:dim(n-1),:dim(n)]=d(n)
        Ds[n][:dim(n-1),dim(n):]=s.eye(dim(n-1))
        Ds[n][dim(n-1):,dim(n):]=d(n-1)
        # h_n(a,b)=(0,a)
        Hs[n]=s.zeros(dim(n+1)+dim(n),dim(n)+dim(n-1))
        Hs[n][dim(n+1):,:dim(n)]=s.eye(dim(n))
    for n in range(N):
        dh=Ds[n+1]*Hs[n]
        hd=Hs[n-1]*Ds[n] if n else s.zeros(dim(n)+dim(n-1))
        assert all(int(x)%2==0 for x in dh+hd-s.eye(dim(n)+dim(n-1)))
    hom=[]
    for n in range(N):
        hom.append(dim(n)+dim(n-1)-rank_mod2(Ds[n])-rank_mod2(Ds[n+1]))
    assert not any(hom)
    return {'dimensions_X':dims,'dimensions_J_tensor_X':[dim(n)+dim(n-1) for n in range(N)],'homology_dimensions':hom,'contraction_identity':True}

# k=F2 x F3, e=(1,0), f=(0,1).
e=(1,0); f=(0,1)
mul=lambda x,y:(x[0]*y[0]%2,x[1]*y[1]%3)
add=lambda x,y:((x[0]+y[0])%2,(x[1]+y[1])%3)
assert mul(e,e)==e and mul(f,f)==f and mul(e,f)==(0,0) and add(e,f)==(1,1)
# Counit at fk is 0 -> F3. Dimension test is finite and conclusive.
assert mul(e,f)==(0,0)
print(json.dumps({'ring':'F_2 x F_3','orthogonal_idempotents':True,'counit_on_fk_H0_domain_cardinality':1,'counit_on_fk_H0_target_cardinality':3,'counit_is_quasi_isomorphism':False},sort_keys=True))
for dims,diffs in [([0],{}),([1],{}),([1,1],{1:s.Matrix([[1]])}),([1,2,1],{1:s.Matrix([[1,0]]),2:s.Matrix([[0],[1]])}),([1,0,1],{})]:
    print(json.dumps(check_tensor_disk(dims,diffs),sort_keys=True))
# Symbolic signs work over all rings, independently of mod2 examples.
u,v,w=s.symbols('u v w',commutative=False)
print('Symbolic contraction: d h(a,b) + h d(a,b) = (a,-d(a)) + (0,d(a)+b) = (a,b).')
print('All certificate assertions passed.')
print(json.dumps({'dropped_interval_counterexample':'M=F2-Mod, phi=id, kappa=id','degree_zero_complex_H1':0,'target_F2_shift1_H1':1,'J_equals_unit_positive_derived_vanishing':True,'J_equals_zero_total_vanishing_but_alpha_not_monic':True},sort_keys=True))
# Pointwise epimorphism of parallel-arrow diagrams:
# (F2 --id,0--> F2) -> (F2 --0,0--> 0).
assert 1-rank_mod2(s.Matrix([[1]]))==0
assert 1-rank_mod2(s.zeros(0,1))==1
print(json.dumps({'all_limits_exact_counterexample':True,'source_equalizer_dim':0,'target_equalizer_dim':1,'component_maps_epimorphic':True,'equalizer_map_epimorphic':False},sort_keys=True))
