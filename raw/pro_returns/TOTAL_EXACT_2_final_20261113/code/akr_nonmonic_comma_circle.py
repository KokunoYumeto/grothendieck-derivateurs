"""Exact finite counterexample to the unqualified 'the component is a circle'."""
from collections import defaultdict
import json,itertools
objects=('x','T','S')
arrows={f'id_{x}':(x,x) for x in objects}
arrows.update(c=('x','T'),d=('x','T'),f=('T','S'),g=('T','S'),h=('x','S'))
def compose(a,b):
    # a after b
    assert arrows[b][1]==arrows[a][0]
    if a.startswith('id_'):return b
    if b.startswith('id_'):return a
    assert a in ('f','g') and b in ('c','d')
    return 'h'
composable=0;triples=0
for a,b in itertools.product(arrows,repeat=2):
    if arrows[b][1]==arrows[a][0]:
        c=compose(a,b);assert arrows[c]==(arrows[b][0],arrows[a][1]);composable+=1
for a,b,c in itertools.product(arrows,repeat=3):
    if arrows[c][1]==arrows[b][0] and arrows[b][1]==arrows[a][0]:
        assert compose(a,compose(b,c))==compose(compose(a,b),c);triples+=1
s=5;k=1
vertices=[('S',i,'h') for i in range(s)]+[('T',i,c) for i in range(s) for c in ('c','d')]
edges=[]
for i in range(s):
    maps=('g','f') if i<2*k else (('g','g') if i==2*k else (('f','g') if i<4*k else ('f','f')))
    for c in ('c','d'):
        for j,a in ((i,maps[0]),((i+1)%s,maps[1])):
            assert compose(a,c)=='h'
            edges.append((('T',i,c),('S',j,'h')))
parent={v:v for v in vertices}
def find(v):
    while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
    return v
for u,v in edges:
    a,b=find(u),find(v)
    if a!=b:parent[a]=b
components=len({find(v) for v in vertices})
deg=defaultdict(int)
for u,v in edges:deg[u]+=1;deg[v]+=1
out={'category_objects':list(objects),'arrows':arrows,'arrows_count':len(arrows),'composable_pairs_checked':composable,'associative_triples_checked':triples,'index_cycle_length':s,'comma_vertices':len(vertices),'comma_edges':len(edges),'comma_components':components,'comma_H1_free_rank':len(edges)-len(vertices)+components,'S_vertex_valences':sorted({deg[v] for v in vertices if v[0]=='S'}),'T_vertex_valences':sorted({deg[v] for v in vertices if v[0]=='T'}),'conclusion':'connected comma graph has H1=Z^6 and is not a circle; equalizing precomposition still forces noncontractibility'}
assert components==1 and out['comma_H1_free_rank']==6
print(json.dumps(out,indent=2))
