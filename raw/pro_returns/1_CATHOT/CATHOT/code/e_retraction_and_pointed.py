"""Exhaustive finite certificates for E.5 and E.14."""
from itertools import product
import json

def fence_rel(vertices,cycle=False):
    n=len(vertices); rel={(i,i) for i in vertices}
    for i in vertices:
        if i%2==0:
            for j in (i-1,i+1):
                if cycle: j%=n
                if j in vertices: rel.add((i,j))
    return rel
A=fence_rel(list(range(9)))
B=fence_rel(list(range(12)),True)
assert {p for p in B if p[0]<9 and p[1]<9}==A
retractions=[]
for images in product(range(9),repeat=3):
    f=tuple(range(9))+images
    if all((f[i],f[j]) in A for i,j in B): retractions.append(f)
assert not retractions
contractions=[]
for k in range(9):
    f=tuple(max(k,i) for i in range(9))
    assert all((f[i],f[j]) in A for i,j in A)
    contractions.append(f)
for f,g in zip(contractions,contractions[1:]):
    assert all((f[i],g[i]) in A for i in range(9)) or all((g[i],f[i]) in A for i in range(9))

# E: full subcategory of pointed sets on singleton and {0,1}.
sizes={0:1,1:2}
arrows=[]
for src,tgt in product(range(2),repeat=2):
    for tail in product(range(sizes[tgt]),repeat=sizes[src]-1):
        arrows.append((src,tgt,(0,)+tail))
def compose(b,a):
    assert a[1]==b[0]
    return (a[0],b[1],tuple(b[2][x] for x in a[2]))
triples=0
for a,b,c in product(arrows,repeat=3):
    if a[1]==b[0] and b[1]==c[0]:
        assert compose(c,compose(b,a))==compose(compose(c,b),a)
        triples+=1
assert len(arrows)==5
assert sum(a[0]==a[1]==1 for a in arrows)==2
print(json.dumps({
 'strict_retraction':{'A_objects':9,'A_arrows':len(A),'B_objects':12,'B_arrows':len(B),
                      'candidate_maps_fixing_A':9**3,'retractions':len(retractions),
                      'identity_to_constant_zigzag_length':8,
                      'cofibration_reason':'c Sd^2 of simplicial path inclusion into triangle boundary'},
 'finite_pointed_category':{'objects':2,'arrows':arrows,'associativity_triples':triples},
 'status':'PASS'},indent=2))
