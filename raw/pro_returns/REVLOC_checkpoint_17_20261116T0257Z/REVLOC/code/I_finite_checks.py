"""Finite certificates for REVLOC Part I. Pure Python, exhaustive order checks."""
from itertools import combinations, product
from pathlib import Path
import json

def tc(n,edges):
    r=[[i==j for j in range(n)] for i in range(n)]
    for x,y in edges:r[x][y]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):r[i][j]|=r[k][j]
    assert all(not (i!=j and r[i][j] and r[j][i]) for i in range(n) for j in range(n))
    return r

def beats(r,V):
    out=[]
    for x in V:
        lo=[y for y in V if y!=x and r[y][x]]
        hi=[y for y in V if y!=x and r[x][y]]
        for y in lo:
            if all(r[z][y] for z in lo):out.append((x,'down',y));break
        for y in hi:
            if all(r[y][z] for z in hi):out.append((x,'up',y));break
    return out

def core(r):
    V=list(range(len(r)));deletions=[]
    while beats(r,V):
        x,d,y=beats(r,V)[0];deletions.append([x,d,y]);V.remove(x)
    return V,deletions

def chains(r,V=None):
    V=list(range(len(r))) if V is None else list(V)
    out=set()
    def rec(seq):
        out.add(frozenset(seq))
        for y in V:
            if y!=seq[-1] and r[seq[-1]][y]: rec(seq+[y])
    for x in V: rec([x])
    return out

def complex_faces(facets):
    return {frozenset(s) for f in facets for k in range(1,len(f)+1) for s in combinations(f,k)}

def collapse(K):
    K=set(K);cert=[]
    while len(K)>1:
        facets=[s for s in K if not any(s<t for t in K)]
        found=False
        for t in sorted(facets,key=lambda x:(-len(x),sorted(x))):
            if len(t)==1:continue
            for v in sorted(t):
                s=t-{v}
                if sum(s<=u for u in facets)==1:
                    assert len(t)==len(s)+1 and s in K
                    cert.append([sorted(s),sorted(t)])
                    K.remove(s);K.remove(t);found=True;break
            if found:break
        if not found:break
    return cert, [sorted(s) for s in sorted(K,key=lambda x:(len(x),sorted(x)))]

def covers(r,V=None):
    V=list(range(len(r))) if V is None else list(V)
    return [(x,y) for x in V for y in V if x!=y and r[x][y]
            and not any(z not in (x,y) and r[x][z] and r[z][y] for z in V)]

def components(n,es):
    seen=set();count=0
    for x in range(n):
        if x in seen:continue
        count+=1;todo=[x];seen.add(x)
        while todo:
            v=todo.pop()
            for a,b in es:
                w=b if a==v else a if b==v else None
                if w is not None and w not in seen:seen.add(w);todo.append(w)
    return count

# The octahedral sphere with the open triangle (a,b,c) removed.
pairs=[(0,1),(2,3),(4,5)]
facets=[tuple(x) for x in product(*pairs) if x!=(0,2,4)]
K=complex_faces(facets)
faces=sorted(K,key=lambda s:(len(s),sorted(s)))
r=[[s<=t for t in faces] for s in faces]
C,beat_certificate=core(r)
assert not beats(r,C) and len(C)>1
coll_K,rem_K=collapse(K)
assert len(rem_K)==1
# Enumerate nerve via strict chains recursively (rank <= 2 here).
KP=chains(r)
coll_KP,rem_KP=collapse(KP)
assert len(rem_KP)==1
core_nerve=chains(r,C)
coll_core,rem_core=collapse(core_nerve)
assert len(rem_core)==1
# All comparable-to-identity self-maps of the core can be checked by backtracking.
def comparable_selfmaps(r,V,up):
    choices={x:[y for y in V if r[x][y] if up] if up else [y for y in V if r[y][x]] for x in V}
    out=[];f={}
    def rec(k):
        if k==len(V):out.append(dict(f));return
        x=V[k]
        for y in choices[x]:
            if all((not r[x][z] or r[y][f[z]]) and (not r[z][x] or r[f[z]][y]) for z in f):
                f[x]=y;rec(k+1);del f[x]
    rec(0);return out
up=comparable_selfmaps(r,C,True);down=comparable_selfmaps(r,C,False)
assert len(up)==len(down)==1
# Four-point diamond: 0<1,2<3, but 1 and 2 incomparable.
dia=tc(4,[(0,1),(0,2),(1,3),(2,3)])
dia_core,dia_beats=core(dia)
assert len(dia_core)==1
es=covers(dia)
cycle_rank=len(es)-4+components(4,es)
assert cycle_rank==1
# The six-point noncofibrant order A2 + A2 + A2 used in the cell peeling proof.
six=tc(6,[(a,b) for a in [0,1] for b in [2,3]]+[(b,c) for b in [2,3] for c in [4,5]])
assert len(covers(six))==8 and not beats(six,list(range(6)))
assert not [x for x in range(6) if all(six[b][x] for b in [2,3]) and all(six[x][c] for c in [4,5])]
for b in [2,3]:
    assert [x for x in range(6) if six[x][b] and all(six[a][x] for a in [0,1])]==[b]
for c in [4,5]:
    assert [x for x in range(6) if six[x][c] and all(six[b][x] for b in [2,3])]==[c]
data={
 'octahedron_minus_facet':{'vertices':['a','ap','b','bp','c','cp'],'facets':facets,'face_count':len(faces),
  'faces':[sorted(s) for s in faces],'simplicial_collapse':coll_K,'simplicial_remainder':rem_K,
  'face_poset_core':C,'beat_deletions':beat_certificate,'core_cover_edges':covers(r,C),
  'nerve_simplex_count':len(KP),'nerve_collapse':coll_KP,'nerve_remainder':rem_KP,
  'core_nerve_simplex_count':len(core_nerve),'core_nerve_collapse':coll_core,'core_nerve_remainder':rem_core,
  'core_comparable_endomorphisms':{'up':len(up),'down':len(down)}},
 'diamond':{'covers':es,'beat_deletions':dia_beats,'core':dia_core,'undirected_hasse_cycle_rank':cycle_rank},
 'noncofibrant_six_point':{'labels':['a1','a2','b1','b2','c1','c2'],'covers':covers(six),
 'upper_sets':[[j for j in range(6) if six[i][j]] for i in range(6)],
 'no_interpolant_between_both_middle_and_both_top':True,
 'cell_peeling_fixed_point_conditions':True}}
p=Path(__file__).parent/'outputs'/'I_finite_checks.json';p.write_text(json.dumps(data,indent=2))
print('PASS: octahedron-minus-facet has',len(K),'nonempty simplices and collapses to',rem_K)
print('PASS: its face poset has',len(faces),'objects; beat-point core has',len(C),'objects')
print('Core labels:',[(i,sorted(faces[i])) for i in C])
print('Core cover edges:',covers(r,C))
print('PASS: both the face-poset nerve and core nerve have certified simplicial collapses to points')
print('PASS: the core has exactly one endomorphism above identity and one below identity')
print('PASS: diamond has point core and Hasse-graph cycle rank 1')
print('PASS: six-point noncofibrant order and all cell-peeling interval obstructions verified')
print('Output:',p)
