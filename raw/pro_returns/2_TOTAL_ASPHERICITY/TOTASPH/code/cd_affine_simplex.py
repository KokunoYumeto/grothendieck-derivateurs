"""Search integer affine cones in the free linearization of Delta_inj."""
from itertools import combinations
import sympy as s
from math import gcd,lcm
from functools import reduce
for k in range(2,5):
  for N in range(k+1,2*k+5):
    cols=list(combinations(range(N),k)); faces=list(combinations(range(N),k-1)); fi={f:i for i,f in enumerate(faces)}
    M=s.zeros((k-1)*len(faces),len(cols))
    for j,c in enumerate(cols):
      for i in range(1,k):
        M[(i-1)*len(faces)+fi[c[:i]+c[i+1:]],j]+=1
        M[(i-1)*len(faces)+fi[c[1:]],j]-=1
    basis=M.nullspace(); gi=0; witness=None
    for v in basis:
      den=reduce(lcm,(x.q for x in v),1); vi=v*den; weight=int(sum(vi));gi=gcd(gi,weight)
      if abs(weight)==1:witness=[(c,int(x/weight)) for c,x in zip(cols,vi) if x]
    print({'cardinality':k,'target_cardinality':N,'kernel_dim':len(basis),'basis_weight_gcd':gi,'witness':witness})
    if witness:break
