#!/usr/bin/env python3
"""Finite polynomial tests for the E=F<5> edge through degree twelve.

Certifies the displayed Newton primitive/Sq tests and Hilbert-series counts.
The Hopf-freeness, minimal-resolution bound and EMSS interfaces are proved
in the accompanying note, not inferred from this computation.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import D2_fiber_poly_check as a

MAX = 13
a.LABEL.clear()
for e in product(range(7), range(5), range(3), range(2)):
    if 0 < a.deg(e) <= MAX:
        a.LABEL[e] = ''.join(g+(str(n) if n > 1 else '')
                            for g,n in zip(('u','v','w','t'),e) if n)
a.EXP.clear()
a.EXP.update({name:e for e,name in a.LABEL.items()})
a.GEN_SQ[3][1] = {(0,0,2,0)}

def label(e): return a.term(a.LABEL[e])

@lru_cache(None)
def inverse_u(k):
    if k == 0: return {()}
    return a.xor(*(a.mul(label((j,0,0,0)), inverse_u(k-j))
                   for j in range(1,k+1)))

def newton_u(k, generator):
    i = ('u','v','w','t').index(generator)
    terms=[]
    for j in range(k+1):
        e=[j,0,0,0]
        e[i]+=1
        terms.append(a.mul(label(tuple(e)),inverse_u(k-j)))
    return a.xor(*terms)

P = newton_u(2,'v')
Q = newton_u(1,'w')
Z11 = newton_u(1,'t')
T12 = a.xor(label((0,1,0,1)), a.term('v','t'))
T13a = newton_u(4,'w')
T13b = newton_u(2,'t')
tests = {'Z11':Z11, 'T12':T12, 'T13a':T13a, 'T13b':T13b}
for name, value in tests.items():
    assert not a.reduced_delta(value), (name,a.show_tensor(a.reduced_delta(value)))
assert a.sq(1,T12) == Z11
assert a.sq(6,T13a) == P
assert a.sq(6,T13b) == Q

# Power detector for the only extra primitive in base degree twelve.
x2=a.term('v2','v2')
assert a.reduced_delta(x2) == {(('v','v'),('v','v'))}

def series_mul(x,y,n=MAX):
    return [sum(x[i]*y[k-i] for i in range(k+1)) for k in range(n+1)]
def series_div(x,y,n=MAX):
    assert y[0] == 1
    out=[]
    for k in range(n+1):out.append(x[k]-sum(y[j]*out[k-j] for j in range(1,k+1)))
    return out
def poly_series(gens,n=MAX):
    out=[1]+[0]*n
    for d,multiplicity in sorted(gens.items()):
        for _ in range(multiplicity):
            for k in range(d,n+1):out[k]+=out[k-d]
    return out

HB=poly_series({2:1,3:1,5:1,9:1})
# Lyndon basis of the ordinary alternating Lie algebra on s H~B.
# Weighted PBW: prod(1-t^w)^(-l_w)=1/(1-V(t)).
W=MAX+1
V=[0]*(W+1)
for d in range(1,MAX+1):V[d+1]=HB[d]
tensor=[1]+[0]*W
for k in range(1,W+1):tensor[k]=sum(V[j]*tensor[k-j] for j in range(1,k+1))
lie={}
current=[1]+[0]*W
for w in range(1,W+1):
    m=tensor[w]-current[w]
    assert m>=0
    lie[w]=m
    for _ in range(m):
        for k in range(w,W+1):current[k]+=current[k-w]
assert current == tensor
restricted={}
for w,m in lie.items():
    if not m:continue
    q=w
    while q<=W:
        restricted[q-1]=restricted.get(q-1,0)+m
        q*=2
HT=poly_series(restricted)
HF=series_div(HT,HB)
basegens={4:1,5:1,6:1,7:2,8:1,9:1,10:1,11:2,12:1,13:2}
HK4=poly_series(basegens)
HE=series_div(HF,HK4)
assert HE[1:11] == [0,0,0,0,1,2,2,5,8,12], HE

def show(poly):
    return ' + '.join('*'.join('['+x+']' for x in word) or '1'
                      for word in sorted(poly)) or '0'

rows=[]
for name,value in tests.items():
    rows.append({'class':name,'polynomial':show(value),
                 'Sq1':show(a.sq(1,value)),
                 'Sq6':show(a.sq(6,value)),
                 'reduced_coproduct':[]})
report={'status':'PASS','scope':__doc__.strip(),'tests':rows,
        'power_detector_reduced_coproduct':
            [[show({l}),show({r})] for l,r in sorted(a.reduced_delta(x2))],
        'dimensions':{'B':HB,'T':HT,'F':HF,'K4':HK4,'edge_quotient':HE},
        'ordinary_Lie_generators_by_shifted_degree':lie,
        'E2_polynomial_generators_by_degree':restricted,
        'L_bar_quotient_dimensions':{'H13':HE[11]-3,'H14':HE[12]-7},
        'proven_edge_range':12,
        'warning':'Degree13 edge quotient is only a formal Hilbert coefficient here; no claim of edge validity in degree13.'}
dest=Path(__file__).parent/'outputs'/'I_cover_extension.json'
dest.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','E11':HE[11],'E12':HE[12],
                  'F11':HF[11],'F12':HF[12],'output':str(dest)}))
