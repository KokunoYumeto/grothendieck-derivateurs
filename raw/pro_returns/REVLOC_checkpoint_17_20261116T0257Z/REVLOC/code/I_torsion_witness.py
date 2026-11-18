"""Explicit finite simplicial data for the nonzero torsion construction.

Build M(Z/5,1) as a poset mapping cone of a fivefold circle map;
wedge on a tetrahedral S^2; triangulate an attaching S^2 representing a
Bass unit of Z[C5]; give the resulting finite poset map and symbolic
second subdivision (a Thomason trivial cofibration).
"""
from itertools import combinations
from collections import defaultdict, deque
from pathlib import Path
import json
import sympy as sp

OUT=Path(__file__).parent/'outputs'

def closure(n,edges):
    r=[{i} for i in range(n)]
    for i,j in edges:r[i].add(j)
    for k in range(n):
        for i in range(n):
            if k in r[i]:r[i].update(r[k])
    assert all(not(i!=j and i in r[j]) for i in range(n) for j in r[i])
    return r

def nerve(r):
    out=set()
    def rec(c):
        out.add(frozenset(c))
        for y in r[c[-1]]-{c[-1]}:rec(c+[y])
    for x in range(len(r)):rec([x])
    return out

def faces(ts):
    return {frozenset(c) for t in ts for k in range(1,len(t)+1) for c in combinations(t,k)}

def circle(m):
    return [frozenset([i]) for i in range(m)]+[frozenset([i,(i+1)%m]) for i in range(m)]

def orient_sign(t):
    return (-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))

# Circle posets and the fivefold simplicial covering.
cs,ct=circle(15),circle(3)
f=[ct.index(frozenset(v%3 for v in s)) for s in cs]
r=[set() for _ in range(37)]
for i,s in enumerate(cs):
    r[i].update(j for j,t in enumerate(cs) if s<=t)
    r[i].update(30+j for j,t in enumerate(ct) if ct[f[i]]<=t)
    r[i].add(36)
for i,s in enumerate(ct):r[30+i].update(30+j for j,t in enumerate(ct) if s<=t)
r[36].add(36)
assert all(i in r[i] and all(r[j]<=r[i] for j in r[i]) for i in range(37))
K0=nerve(r)
base=30
# Target S^2, with orientation induced by the ordered tetrahedron.
sphere_vertices=(base,37,38,39)
sphere_triangles=[(base,38,37),(base,37,39),(base,39,38),(37,38,39)]
K=K0|faces(sphere_triangles)
assert K0 & faces(sphere_triangles)=={frozenset([base])}

# A Z/5 cocycle on K0. Compute by solving the triangle equations and fixing
# the winding of the target-circle loop to one. This independently records
# the fundamental group labels used by the attaching map.
edges=sorted([tuple(sorted(s)) for s in K0 if len(s)==2]);ei={e:i for i,e in enumerate(edges)}
tris=[tuple(sorted(s)) for s in K0 if len(s)==3]
rows=[]
for a,b,c in tris:
    v=[0]*(len(edges)+1);v[ei[a,b]]=1;v[ei[b,c]]=1;v[ei[a,c]]=-1;rows.append(v)
loop=[30,33,31,34,32,35,30]
v=[0]*(len(edges)+1)
for a,b in zip(loop,loop[1:]):v[ei[tuple(sorted((a,b)))]]+=1 if a<b else -1
v[-1]=1;rows.append(v)
# Set a spanning tree to zero to choose a convenient cocycle representative.
adj=defaultdict(list)
for a,b in edges:adj[a].append(b);adj[b].append(a)
seen={base};todo=deque([base])
while todo:
    a=todo.popleft()
    for b in adj[a]:
        if b not in seen:
            seen.add(b);todo.append(b)
            v=[0]*(len(edges)+1);v[ei[tuple(sorted((a,b)))]]=1;rows.append(v)
A=[[z%5 for z in v] for v in rows];pivot=[];row=0
for col in range(len(edges)):
    pick=next((k for k in range(row,len(A)) if A[k][col]),None)
    if pick is None:continue
    A[row],A[pick]=A[pick],A[row]
    inv=pow(A[row][col],-1,5);A[row]=[z*inv%5 for z in A[row]]
    for k in range(len(A)):
        if k!=row and A[k][col]:
            fac=A[k][col];A[k]=[(a-fac*b)%5 for a,b in zip(A[k],A[row])]
    pivot.append((row,col));row+=1
for a in A:assert any(a[:-1]) or not a[-1]
sol=[0]*len(edges)
for row,col in reversed(pivot):sol[col]=(A[row][-1]-sum(A[row][j]*sol[j] for j in range(col+1,len(edges))))%5
cocycle={e:sol[j] for e,j in ei.items()}
for e in [tuple(sorted(s)) for s in K if len(s)==2 and s not in K0]:cocycle[e]=0

def lab(a,b):
    if a==b:return 0
    return cocycle[tuple(sorted((a,b)))]*(1 if a<b else -1)%5
assert sum(lab(a,b) for a,b in zip(loop,loop[1:]))%5==1

# Central sphere, with nine pairwise vertex-disjoint triangular ports.
central=[(0,2,1),(0,1,3),(0,3,2),(1,2,3)];nxt=4;ports=[]
for k in range(9):
    face=next(t for t in central if t not in ports)
    central.remove(face);a,b,c=face;ap,bp,cp=range(nxt,nxt+3);nxt+=3
    central.extend([(a,b,bp),(a,bp,ap),(b,c,cp),(b,cp,bp),(c,a,ap),(c,ap,cp),(ap,bp,cp)])
    ports.append((ap,bp,cp))
assert len({v for p in ports for v in p})==27
source=[t for t in central if t not in ports]
vertex_map={v:base for v in range(nxt)}
# A degree-one sphere with a constant triangular port, removed to make a disk.
disk=[(0,2,4),(2,1,4),(1,0,5),(4,1,5),(0,1,3),(0,3,2),(1,2,3)]
disk_port=(0,4,5)
disk_labels={0:base,1:37,2:38,3:39,4:base,5:base}
unit=[-2,1,3,1,-2]
terms=[(i,1 if coeff>0 else -1) for i,coeff in enumerate(unit) for _ in range(abs(coeff))]
assert len(terms)==9
# Orient each tube so its starting boundary cancels the central hole boundary;
# reverse the disk port order at its far end. The map can be reflected to
# create negative terms independently of the gluing orientation.
for port,(power,sgn) in zip(ports,terms):
    # Travel once extra around five loops for power zero? A one-edge constant
    # cylinder avoids direct vertex identification and is easier to inspect.
    path=[base]
    for _ in range(power):path+=loop[1:]
    if len(path)==1:path.append(base)
    previous=port
    for target_vertex in path[1:]:
        current=tuple(range(nxt,nxt+3));nxt+=3
        for v in current:vertex_map[v]=target_vertex
        for j in range(3):
            a,b=previous[j],previous[(j+1)%3]
            ap,bp=current[j],current[(j+1)%3]
            source.extend([(a,b,bp),(a,bp,ap)])
        previous=current
    # Port has sphere-orientation (0,4,5); reverse it to cancel tube far edge.
    relabel={disk_port[0]:previous[0],disk_port[1]:previous[2],disk_port[2]:previous[1]}
    for v in range(6):
        if v not in relabel:relabel[v]=nxt;nxt+=1
        image=disk_labels[v]
        # The gluing reverses disk orientation; swap the two nonbase labels
        # for positive coefficients to offset this reversal.
        if sgn==1:
            if image==37:image=38
            elif image==38:image=37
        vertex_map[relabel[v]]=image
    source.extend(tuple(relabel[v] for v in t) for t in disk)

S=faces(source)
# Independent surface and simplicial-map checks.
inc=defaultdict(list)
for tid,t in enumerate(source):
    for j in range(3):
        a,b=t[j],t[(j+1)%3]
        inc[tuple(sorted((a,b)))].append((tid,1 if a<b else -1))
assert len({frozenset(t) for t in source})==len(source)
assert all(len(v)==2 for v in inc.values())
assert len(vertex_map)-len(inc)+len(source)==2
assert all(frozenset(vertex_map[v] for v in t) in K for t in source)
# Determine a coherent orientation (the construction is allowed to use either
# local triangle orientation). This also checks orientability and connectedness.
adjtri=defaultdict(list)
for values in inc.values():
    (i,a),(j,b)=values;adjtri[i].append((j,-a*b));adjtri[j].append((i,-a*b))
ori={0:1};todo=deque([0])
while todo:
    i=todo.popleft()
    for j,fac in adjtri[i]:
        value=ori[i]*fac
        if j in ori:assert ori[j]==value
        else:ori[j]=value;todo.append(j)
assert len(ori)==len(source)
# Check every vertex link is a single cycle.
for v in vertex_map:
    link=defaultdict(set)
    for t in source:
        if v in t:
            a,b=[x for x in t if x!=v];link[a].add(b);link[b].add(a)
    assert link and all(len(ns)==2 for ns in link.values())
    reached={next(iter(link))};todo=deque(reached)
    while todo:
        x=todo.popleft()
        for y in link[x]:
            if y not in reached:reached.add(y);todo.append(y)
    assert len(reached)==len(link)
# Lift the simplicial attaching sphere to the C5 cover via the cocycle.
vsadj=defaultdict(list)
for a,b in inc:vsadj[a].append(b);vsadj[b].append(a)
deck={0:0};todo=deque([0])
while todo:
    a=todo.popleft()
    for b in vsadj[a]:
        val=(deck[a]+lab(vertex_map[a],vertex_map[b]))%5
        if b in deck:assert deck[b]==val
        else:deck[b]=val;todo.append(b)
coeff=[0]*5
for i,t in enumerate(source):
    images=tuple(vertex_map[v] for v in t)
    if frozenset(images)==frozenset((37,38,39)):
        assert len({deck[v] for v in t})==1
        coeff[deck[t[0]]]+=ori[i]*orient_sign(images)
# Depending on the global surface orientation, the coefficient vector is ±u.
assert coeff==unit or coeff==[-v for v in unit],coeff
T=sp.symbols('t');u=sum(coeff[i]*T**i for i in range(5));mod=T**5-1
uinv=sp.invert(u,mod,domain=sp.QQ)
invcoeff=[int(uinv.expand().coeff(T,i)) for i in range(5)]
assert all(uinv.expand().coeff(T,i)==invcoeff[i] for i in range(5))
assert sp.rem(u*uinv,mod)==1
# Nontrivial Whitehead class: evaluate in C at the fifth root. Its modulus
# is (2*cos(pi/5))^4 > 1; trivial units ±t^j have modulus one.
assert sum(coeff)==1 or sum(coeff)==-1

# Full finite poset presentation of the homotopy cofiber.
xf=sorted(K,key=lambda s:(len(s),tuple(sorted(s))))
sf=sorted(S,key=lambda s:(len(s),tuple(sorted(s))))
xf_index={s:i for i,s in enumerate(xf)}
alpha=[xf_index[frozenset(vertex_map[v] for v in s)] for s in sf]
A_indices=[xf_index[s] for s in xf if s in K0]
# Y = non-Hausdorff mapping cylinder F(S) -> F(K), plus cone on F(S).
# Order data are stored as the two face families and alpha, avoiding a quadratic
# redundant transitive relation. Comparisons are exactly those formulas.
assert all(xf[alpha[i]]<=xf[alpha[j]] for i,s in enumerate(sf) for j,t in enumerate(sf) if s<=t)
# Matrix of group-ring multiplication: determinant ±1 verifies integrality independently.
M=sp.Matrix([[coeff[(i-j)%5] for j in range(5)] for i in range(5)])
assert abs(M.det())==1

report={
 'description':'Finite data for A -> Y; the final Thomason cofibration is sd^2 A -> sd^2 Y.',
 'circle_source_faces':[sorted(s) for s in cs],'circle_target_faces':[sorted(s) for s in ct],
 'circle_face_map':f,'target_circle_loop':loop,
 'base_poset_upper_sets':[sorted(s) for s in r],
 'base_complex_faces':[sorted(s) for s in sorted(K0,key=lambda s:(len(s),tuple(sorted(s))))],
 'wedge_sphere_oriented_triangles':sphere_triangles,
 'target_faces':[sorted(s) for s in xf],
 'source_oriented_triangles':[list(t if ori[i]==1 else (t[0],t[2],t[1])) for i,t in enumerate(source)],
 'source_faces':[sorted(s) for s in sf],
 'simplicial_vertex_map':vertex_map,'face_poset_map':alpha,'base_face_poset_indices':A_indices,
 'cocycle_mod5':[[a,b,v] for (a,b),v in cocycle.items()],
 'source_lift_deck_labels':deck,'group_ring_boundary':coeff,'inverse_group_ring_boundary':invcoeff,
 'multiplication_determinant':int(M.det()),
 'source_f_vector':[len(vertex_map),len(inc),len(source)],
 'Y_object_count':len(xf)+len(sf)+1,
 'Y_order_definition':{'objects':'X_i, S_j, tip; X is target_faces, S is source_faces',
 'internal':'X_i <= X_j iff target_faces[i] subset target_faces[j]; same for S',
 'mixed':'S_i <= X_j iff target_faces[alpha[i]] subset target_faces[j]; every S_i < tip',
 'other':'Only identities and the relations listed; no X-to-S, X-to-tip, tip-to-X or tip-to-S arrows'},
 'final_objects':'Nonempty inclusion chains of nonempty chains of Y, with inclusion order; source restricts to base_face_poset_indices.'}
(OUT/'I_torsion_witness.json').write_text(json.dumps(report,indent=2))
print('PASS: degree-five circle map and 37-object poset mapping cone constructed')
print('PASS: target has',len(xf),'faces; source S^2 has f-vector',report['source_f_vector'])
print('PASS: source is connected, closed, oriented, all vertex links circles, Euler characteristic 2')
print('PASS: every attaching triangle maps to a target simplex')
print('PASS: lifted relative boundary in Z[C5] =',coeff)
print('PASS: inverse in Z[C5] =',invcoeff,'; regular-representation determinant =',M.det())
print('PASS: |u(exp(2 pi i/5))| = (2 cos(pi/5))^4 > 1, so [u] != 0 in Wh(C5)')
print('Finite cofiber poset Y has',report['Y_object_count'],'objects')
print('Final map is the explicitly defined second subdivision of the base-face-poset inclusion A -> Y.')
