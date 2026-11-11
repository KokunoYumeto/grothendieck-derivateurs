"""Finite counterexample checks for Part D; exact arithmetic only."""
from itertools import product
import json
# The discrete category on two objects.
objects=(0,1)
arrows=[(x,x) for x in objects]
assert len(arrows)==2
assert all(s==t for s,t in arrows)
assert not any(s==0 and t==1 for s,t in arrows)
print(json.dumps({'example':'discrete_two_objects','objects':objects,'arrows':arrows,'components':2,'H0_rank_Z':2,'colimit_formula':'M0 direct_sum M1','exact':'direct sums preserve short exact sequences of modules'}))
# C_2, with 0 the identity, composition x*y=(x+y) mod 2.
from fractions import Fraction
M=range(2)
mul=lambda x,y:(x+y)%2
assert all(mul(0,x)==x==mul(x,0) for x in M)
assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(M,repeat=3))
assert not any(mul(c,0)==mul(c,1) for c in M)
e=[Fraction(1,2),Fraction(1,2)]
assert sum(e)==1
for g in M:
    eg=[sum(e[x] for x in M if mul(x,g)==y) for y in M]
    assert eg==e
diffs=[0,2,0,2,0,2]
assert all(diffs[i]*diffs[i+1]==0 for i in range(len(diffs)-1))
print(json.dumps({'example':'C2','table':[[mul(x,y) for y in M] for x in M],'associative':True,'filtered':False,'periodic_trivial_coefficient_differentials_degrees_1_through_6':[0,2,0,2,0,2],'H1_Z':'Z/2','positive_homology_Q':'zero, since multiplication by 2 is invertible','Q_augmentation_splitting_coefficients':['1/2','1/2']}))
# Comparison strata for the two-point cospans in Delta_inj, checked on
# every map with source and target ordinals of cardinality <= 5.
from itertools import combinations
checked=0
for n in range(1,6):
  for N in range(n,6):
    for f in combinations(range(N),n):
      for a,b in product(range(n),repeat=2):
        cmp=lambda x,y:(x>y)-(x<y)
        assert cmp(a,b)==cmp(f[a],f[b]);checked+=1
print(json.dumps({'example':'Delta_inj_cospan_strata','comparisons':['less','equal','greater'],'invariance_checks':checked,'passed':True,'scope':'bounded computational verification; general proof in paper'}))
