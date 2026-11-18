"""Finite exact certificates for the modular primitive-weight construction.
The theorem is proved algebraically in C4_addendum.tex; these are examples,
not a search-based assertion of exactness for all module diagrams.
"""
from fractions import Fraction as Q
from collections import defaultdict

def clean(d,p=None):
 return {str(k):(v if p is None else v%p) for k,v in sorted(d.items()) if (v if p is None else v%p)}
for p in [2,3,5,7,11,13,17,19]:
 weights=[]
 for j in range(p): weights.append((1,(Q(1,p),Q(j,p),Q(j+1-p,p))))
 for j in range(1,p): weights.append((-1,(Q(0),Q(j,p),Q(j-p,p))))
 assert sum(w for w,b in weights)==1
 assert all(x+y-z==1 for w,(x,y,z) in weights)
 marginals=[]
 for i in range(3):
  m=defaultdict(int)
  for w,b in weights:m[b[i]]+=w
  assert clean(m,p)=={'0':1}
  marginals.append(clean(m))
 print(f'p={p}, support={len(weights)}, augmentation=1, all delta(b)=1, all three marginals=delta_0 mod p')
 print(' integral marginals:',marginals)
 if p==2: print(' explicit signed atoms (weight,b01,b12,b02):',[(w,*map(str,b)) for w,b in weights])
print('PASS: exact rational arithmetic and every modular marginal checked')
