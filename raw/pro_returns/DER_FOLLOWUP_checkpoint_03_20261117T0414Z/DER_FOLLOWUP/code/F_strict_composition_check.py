#!/usr/bin/env python3
"""Independent reconstruction of the finite PRETOT strict-sieve example.

Input is the stated two-relator presentation, not the earlier act certificate.
We rebuild the coned polygon semisimplicial set, its free degeneracy completion,
the right M_2-act, and both collage sieves. Universal totality is proved in the
paper; enumeration checks the complete finite algebra and a nontrivial quotient.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.
"""
from itertools import combinations_with_replacement,product
from pathlib import Path
import json
WORDS=('aaaaaBBB','bbbBABA')
vertices=('v','c0','c1')
edges=('a','b')+tuple(f'r{k}:{i}' for k,w in enumerate(WORDS) for i in range(len(w)))
faces={e:('v','v') if e in ('a','b') else ('v','c'+e[1]) for e in edges}
triangles=tuple(f't{k}:{i}' for k,w in enumerate(WORDS) for i in range(len(w)))
for k,w in enumerate(WORDS):
    for i,letter in enumerate(w):
        r=f'r{k}:{i}';s=f'r{k}:{(i+1)%len(w)}'
        faces[f't{k}:{i}']=(letter.lower(),s,r) if letter.islower() else (letter.lower(),r,s)
nd=(vertices,edges,triangles)
def face_of(dim,name,index):return faces[name][index]
for t in triangles:
    for i in range(3):
        for j in range(i+1,3):
            assert face_of(1,face_of(2,t,j),i)==face_of(1,face_of(2,t,i),j-1)
def mono(m,n):return tuple(combinations_with_replacement(range(n+1),m+1))
def compose(g,f):return tuple(g[x] for x in f)
def restrict_simplex(dim,name,subset):
    # Delete omitted vertices in descending order; all simplicial identities
    # were independently checked above, so the result is independent of order.
    for i in sorted(set(range(dim+1))-set(subset),reverse=True):
        name=face_of(dim,name,i);dim-=1
    return name
def pull(x,a):
    dim,name,surj=x
    values=compose(surj,a);image=tuple(sorted(set(values)))
    return (len(image)-1,restrict_simplex(dim,name,image),tuple(image.index(v) for v in values))
K=tuple((d,x,s) for d in range(3) for x in nd[d] for s in mono(2,d) if len(set(s))==d+1)
M=mono(2,2);mi={a:i for i,a in enumerate(M)};ki={x:i for i,x in enumerate(K)}
unit=mi[(0,1,2)]
mul=[[mi[compose(a,b)] for b in M] for a in M]
action=[[ki[pull(x,a)] for a in M] for x in K]
assert len(M)==10 and len(K)==52
for a,b,c in product(range(10),repeat=3):assert mul[a][mul[b][c]]==mul[mul[a][b]][c]
for x,a,b in product(range(52),range(10),range(10)):
    assert action[action[x][a]][b]==action[x][mul[a][b]]
# Presentation-cell boundary is unimodular; the two-complex is acyclic.
exp=[[sum((1 if c.islower() else -1) for c in w if c.lower()==g) for w in WORDS] for g in 'ab']
det=exp[0][0]*exp[1][1]-exp[0][1]*exp[1][0]
assert abs(det)==1
def cycle(c):
    p=list(range(5))
    for x,y in zip(c,c[1:]+c[:1]):p[x-1]=y-1
    return tuple(p)
perms={'a':cycle([1,4,3,2,5]),'b':cycle([1,2,3])}
perms.update({k.upper():tuple(p.index(i) for i in range(5)) for k,p in list(perms.items())})
identity=tuple(range(5))
for w in WORDS:
    p=identity
    for c in w:p=compose(p,perms[c])
    assert p==identity
assert perms['a']!=identity
group={identity};todo=[identity]
while todo:
    p=todo.pop()
    for q in perms.values():
        z=compose(p,q)
        if z not in group:group.add(z);todo.append(z)
assert len(group)==60
# Objects L (lower U), I (new initial), U (old U), T (new target).
arrows={}
for s,t in [('L','L'),('U','U'),('L','U')]:
    for a in range(10):arrows[s,t,a]=(s,t)
for s,t in [('I','I'),('T','T'),('I','U'),('I','T')]:arrows[s,t,0]=(s,t)
for s in ['L','U']:
    for x in range(52):arrows[s,'T',x]=(s,'T')
ids={s:(s,s,unit if s in ['L','U'] else 0) for s in ['L','I','U','T']}
def comp(g,f):
    s,m,a=f;mm,t,b=g;assert m==mm
    if f==ids[s]:return g
    if g==ids[t]:return f
    if s in ['L','U'] and t in ['L','U']:return(s,t,mul[b][a])
    if s=='I':return(s,t,0)
    assert t=='T' and m in ['L','U']
    return(s,t,action[b][a])
pairs=triples=0
for f,(s,t) in arrows.items():
    assert comp(f,ids[s])==f==comp(ids[t],f)
    for g,(u,v) in arrows.items():
        if t!=u:continue
        h=comp(g,f);assert h in arrows and arrows[h]==(s,v);pairs+=1
        for k,(w,z) in arrows.items():
            if v==w:
                assert comp(k,h)==comp(comp(k,g),f);triples+=1
for subset in [{'L'},{'L','I','U'}]:
    assert all(s in subset for s,t in arrows.values() if t in subset)
for t in ['L','U']:
    counit=('L',t,unit)
    assert {comp(counit,('L','L',a)) for a in range(10)}=={f for f,st in arrows.items() if st==('L',t)}
for x,a in product(range(52),range(10)):
    assert comp(('L','T',x),('L','L',a))==('L','T',action[x][a])
report={'nondegenerate_simplex_counts':[len(s) for s in nd],
        'presentation_exponent_matrix':exp,'determinant':det,
        'nontrivial_permutation_quotient_order':len(group),
        'monoid_size':len(M),'act_size':len(K),'monoid_triples':1000,'act_laws':5200,
        'X_objects':3,'X_arrows':sum(s!='T' and t!='T' for s,t in arrows.values()),
        'Y_objects':4,'Y_arrows':len(arrows),'composable_pairs':pairs,
        'associativity_triples':triples,'both_sieves':True,
        'first_sieve_right_adjoint_hom_bijections':True,
        'composite_crossing_act_is_K2':True,
        'interpretation':'Finite algebra checked exhaustively; universal totality uses the proof in F.3 and E.4.'}
out=Path(__file__).resolve().parent/'outputs'/'F_strict_composition_check.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
