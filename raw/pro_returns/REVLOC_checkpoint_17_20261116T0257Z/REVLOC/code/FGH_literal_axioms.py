"""Finite certificate for the failure of absolute => relative Theorem A.
No topology is inferred solely from ranks: the paper identifies each complex
as the suspension of a polygon and supplies its integral orientation chain.
"""
from itertools import combinations
from fractions import Fraction
import json
from pathlib import Path

def parity(xs):
    return -1 if sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))%2 else 1

def simplicial_suspension(n):
    facets=[(a,i,(i+1)%n) for a in (n,n+1) for i in range(n)]
    faces=set()
    for t in facets:
        for r in range(1,4):
            faces.update(tuple(sorted(s)) for s in combinations(t,r))
    return sorted(faces,key=lambda s:(len(s),s))

def chain_add(out,t,c):
    key=tuple(sorted(t)); out[key]=out.get(key,0)+parity(t)*c
    if out[key]==0: del out[key]

def orientation(n):
    out={}
    for i in range(n):
        chain_add(out,(n,i,(i+1)%n),1)
        chain_add(out,(n+1,i,(i+1)%n),-1)
    return out

def boundary(c):
    out={}
    for t,k in c.items():
        for i in range(len(t)):
            chain_add(out,t[:i]+t[i+1:],k*((-1)**i))
    return out

def poset(faces):
    return [[set(x)<=set(y) for y in faces] for x in faces]

def check_poset(r):
    n=len(r)
    assert all(r[i][i] for i in range(n))
    assert all(not(r[i][j] and r[j][i]) for i in range(n) for j in range(i))
    assert all(not(r[i][j] and r[j][k]) or r[i][k] for i in range(n) for j in range(n) for k in range(n))

def monotone(r,s,f):
    assert all(not r[i][j] or s[f[i]][f[j]] for i in range(len(r)) for j in range(len(r)))

def collage(p,q,f):
    # objects: P root layer, Q left layer, one right-layer cone point.
    a=len(p); b=len(q); n=a+b+1
    r=[[False]*n for _ in range(n)]
    for i in range(a):
        for j in range(a):r[i][j]=p[i][j]
        for j in range(b):r[i][a+j]=q[f[i]][j]
        r[i][-1]=True
    for i in range(b):
        for j in range(b):r[a+i][a+j]=q[i][j]
    r[-1][-1]=True
    check_poset(r)
    return r,[0]*a+[1]*b+[2]

p_faces=simplicial_suspension(8); q_faces=simplicial_suspension(4)
p=poset(p_faces);q=poset(q_faces)
check_poset(p);check_poset(q)
vmap={i:i%4 for i in range(8)}|{8:4,9:5}
f=[q_faces.index(tuple(sorted(vmap[v] for v in face))) for face in p_faces]
monotone(p,q,f)
z8=orientation(8);z4=orientation(4)
assert not boundary(z8) and not boundary(z4)
image={}
for face,c in z8.items():chain_add(image,tuple(vmap[v] for v in face),c)
assert image=={face:2*c for face,c in z4.items()}
kf,tagf=collage(p,q,f);ki,tagi=collage(q,q,list(range(len(q))))
u=f+[len(q)+j for j in range(len(q))]+[2*len(q)]
monotone(kf,ki,u)
assert all(tagf[i]==tagi[u[i]] for i in range(len(kf)))
# J = (0 -> 1, 0 -> 2). Slices over j are full subposets
# on layers which have an arrow to j, since J is a poset.
jrel=[[True,True,True],[False,True,False],[False,False,True]]
check_poset(jrel)
slice_data=[]
for j in range(3):
    sx=[i for i,t in enumerate(tagf) if jrel[t][j]]
    sy=[i for i,t in enumerate(tagi) if jrel[t][j]]
    assert all(u[i] in sy for i in sx)
    # evaluation and inclusion are an adjunction E left adjoint I.
    if j==0:
        ex={i:i for i in sx};ix=list(range(len(p))); rr=p
        ey={i:i for i in sy};iy=list(range(len(q))); ss=q
        component=f
    elif j==1:
        ex={i:(f[i] if i<len(p) else i-len(p)) for i in sx};ix=[len(p)+i for i in range(len(q))];rr=q
        ey={i:(i if i<len(q) else i-len(q)) for i in sy};iy=[len(q)+i for i in range(len(q))];ss=q
        component=list(range(len(q)))
    else:
        ex={i:0 for i in sx};ix=[len(kf)-1];rr=[[True]]
        ey={i:0 for i in sy};iy=[len(ki)-1];ss=[[True]]
        component=[0]
    assert all(kf[a][ix[b]]==rr[ex[a]][b] for a in sx for b in range(len(rr)))
    assert all(ki[a][iy[b]]==ss[ey[a]][b] for a in sy for b in range(len(ss)))
    assert all(ey[u[a]]==component[ex[a]] for a in sx)
    slice_data.append({'base_object':j,'source_objects':len(sx),'target_objects':len(sy),'evaluation_adjunctions':'verified','naturality':'verified'})
# The two sieve pieces M_f and cone(P) of K(f).
a=len(p);b=len(q)
M=set(range(a+b)); CP=set(range(a))|{a+b}
for subset in (M,CP):
    assert all(not kf[x][y] or x in subset for y in subset for x in range(len(kf)))
assert M|CP==set(range(len(kf))) and M&CP==set(range(a))
result={'P_faces_by_dimension':[sum(len(x)==d+1 for x in p_faces) for d in range(3)],'Q_faces_by_dimension':[sum(len(x)==d+1 for x in q_faces) for d in range(3)],'P_objects':len(p),'Q_objects':len(q),'Kf_objects':len(kf),'Kid_objects':len(ki),'Kf_arrows':sum(map(sum,kf)),'Kid_arrows':sum(map(sum,ki)),'degree_on_integral_orientation':2,'cofiber_reduced_cellular_complex':{'C3':'Z','C2':'Z','boundary3':2,'H2':'Z/2','other_reduced_homology':0},'slice_checks':slice_data,'all_poset_and_functor_axioms':'verified','sieve_cover':'verified'}
root=Path(__file__).resolve().parent/'outputs'
root.mkdir(exist_ok=True)
(root/'FGH_literal_axioms.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
