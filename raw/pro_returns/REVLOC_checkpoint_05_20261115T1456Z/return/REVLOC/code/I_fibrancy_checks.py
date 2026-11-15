"""Finite witness-tree certificate for the proof of I.9a.

This verifies a particular finite lifting obstruction into the beat-free
22-point poset of I.1a. The proof for all finite targets is in I.tex.
The simplex used for the lifting problem is specified by its vertex set;
its complete double-flag poset is not materialized.
"""
from pathlib import Path
from collections import deque
import json

OUT=Path(__file__).parent/'outputs'
data=json.loads((OUT/'I_finite_checks.json').read_text())['octahedron_minus_facet']
oldfaces=[frozenset(x) for x in data['faces']]
faces=[oldfaces[i] for i in data['face_poset_core']]
n=len(faces)
upper=[{j for j in range(n) if faces[i]<=faces[j]} for i in range(n)]
strict=[r-{i} for i,r in enumerate(upper)]
assert all(not any(all(z in upper[y] for z in strict[x]) for y in strict[x]) for x in range(n))

# A spanning tree of the comparability graph, with the inherited orientations.
edges=[];seen={0};todo=deque([0])
while todo:
    x=todo.popleft()
    for y in range(n):
        if y not in seen and (y in upper[x] or x in upper[y]):
            edges.append((x,y) if y in upper[x] else (y,x))
            seen.add(y);todo.append(y)
assert len(seen)==n and len(edges)==n-1
labels=list(range(n));witness={}
def attach(t):
    x=labels[t]
    for z in sorted(strict[x]):
        u=len(labels);labels.append(z);edges.append((t,u));witness[t,z]=u
        attach(u)
for t in range(n):attach(t)
nt=len(labels)
assert len(edges)==nt-1
adj=[set() for _ in labels]
for a,b in edges:
    assert labels[b] in strict[labels[a]]
    adj[a].add(b);adj[b].add(a)
reached={0};todo=deque([0])
while todo:
    x=todo.popleft()
    for y in adj[x]:
        if y not in reached:reached.add(y);todo.append(y)
assert len(reached)==nt
# Check an explicit leaf deletion contracts the underlying tree.
active=set(range(nt));leaf_certificate=[]
while len(active)>1:
    v=next(v for v in sorted(active) if len(adj[v]&active)==1)
    w=next(iter(adj[v]&active));leaf_certificate.append([v,w]);active.remove(v)

upT=[{i} for i in range(nt)]
for x,y in edges:upT[x].add(y)
for k in range(nt):
    for x in range(nt):
        if k in upT[x]:upT[x].update(upT[k])
assert all(not(i!=j and i in upT[j]) for i in range(nt) for j in upT[i])
assert all(labels[j] in upper[labels[i]] for i in range(nt) for j in upT[i])
assert all((t,z) in witness and witness[t,z] in upT[t] for t,x in enumerate(labels) for z in strict[x])

def chains(up):
    result=[]
    def visit(c):
        result.append(tuple(c))
        for y in sorted(up[c[-1]]-{c[-1]}):visit(c+[y])
    for x in range(len(up)):visit([x])
    return result
C=chains(upT);Csets=[frozenset(c) for c in C];ci={s:i for i,s in enumerate(Csets)}
upC=[{j for j,t in enumerate(Csets) if s<=t} for s in Csets]
D=chains(upC);Dsets=[frozenset(d) for d in D];di={s:i for i,s in enumerate(Dsets)}
lastT=[C[d[-1]][-1] for d in D]
h=[labels[t] for t in lastT]
assert set(h)==set(range(n))

# Force any g>=h to equal h by a finite descending-domain certificate.
forced={};certificate=[]
for x in sorted(range(n),key=lambda x:len(strict[x])):
    for i,t in enumerate(lastT):
        if h[i]!=x:continue
        allowed=set(upper[x]);constraints=[]
        for z in sorted(strict[x]):
            tz=witness[t,z]
            largest=Csets[D[i][-1]]
            newchain=ci[largest|{tz}]
            extended=di[Dsets[i]|{newchain}]
            assert h[extended]==z and extended in forced
            assert Dsets[i]<Dsets[extended]
            allowed={y for y in allowed if z in upper[y]}
            constraints.append([z,extended])
        assert allowed=={x}
        forced[i]=x;certificate.append({'flag':i,'value':x,'upper_witness_flags':constraints})
assert len(forced)==len(D)
commonlower=[x for x in range(n) if all(y in upper[x] for y in range(n))]
assert not commonlower
out={
 'target_faces':[sorted(s) for s in faces],
 'T_labels':labels,'T_directed_edges':edges,'T_leaf_deletion_certificate':leaf_certificate,
 'T_upper_witnesses':[[t,z,u] for (t,z),u in sorted(witness.items())],
 'T_chains':[list(c) for c in C],'D_flags':[list(d) for d in D],
 'h_values':h,'forcing_certificate':certificate,
 'simplex_vertex_count':nt+1,
 'simplex_definition':'All nonempty subsets of T vertices plus one extra vertex; Q is the inclusion-poset of nonempty flags of these subsets.',
 'extension_obstruction':'Old flags sigma, upper flags sigma union {full vertex set}, and singleton full vertex set form K(D). Any extension forces a common lower bound of all target elements; none exists.'}
(OUT/'I_fibrancy_checks.json').write_text(json.dumps(out,indent=2))
print('PASS: target has',n,'elements and no upbeat points')
print('PASS: witness T has',nt,'vertices and',len(edges),'tree edges; explicit leaf collapse certified')
print('PASS: label map T -> P is onto, monotone, and has every required upper witness')
print('PASS: sd^2 T has',len(D),'objects; every pointwise enlargement of h is forced to equal h')
print('PASS: target has no common lower bound, obstructing the specified finite trivial-cofibration lift')
print('The ambient simplex has',nt+1,'vertices; its full double-flag poset is specified symbolically')
