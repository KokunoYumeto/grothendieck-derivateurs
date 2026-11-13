"""A generic graph-gluing warning; this is NOT an AKR category example.

Two convex, component-injective embeddings can have bounded point orbits
but cyclic component orbits. The repaired beta gluing can then merge
different components of an old copy. All data are explicit.
"""
import json
from collections import defaultdict,deque


def repaired_maps(points,f,g,k):
    s=4*k+1;fixed={a for a,b in zip(f,g) if a==b}
    transition={a:b for a,b in zip(f,g) if a!=b};paths=[]
    for start in sorted(set(transition)-set(transition.values())):
        path=[start]
        while path[-1] in transition:path.append(transition[path[-1]])
        paths.append(path)
    assert sum(len(p)-1 for p in paths)==len(transition)
    assert k>=max(map(len,paths),default=1)
    coords={v:(j,t) for j,path in enumerate(paths) for t,v in enumerate(path)}
    def beta(i,t,n):
        if i<=2*k:
            z=t+i;return z if z<=2*k else z+2*k-n+1
        z=t-i+6*k-n+2
        return z if z>2*k else t-i+4*k
    maps=[]
    for i in range(s):
        out=[]
        for v in range(points):
            if v in fixed:out.append(('fixed',v))
            elif v in coords:
                j,t=coords[v];out.append(('path',j,beta(i,t,len(paths[j]))))
            else:out.append(('private',v,i))
        assert len(set(out))==points;maps.append(out)
    values=sorted({x for m in maps for x in m});index={x:i for i,x in enumerate(values)}
    return [[index[v] for v in m] for m in maps],values


def shortest_path(graph,start,end):
    parent={start:None};queue=deque([start])
    while queue:
        u=queue.popleft()
        if u==end:
            path=[]
            while u is not None:path.append(u);u=parent[u]
            return path[::-1]
        for v in graph[u]:
            if v not in parent:parent[v]=u;queue.append(v)
    return None


if __name__=='__main__':
    # S has two isolated vertices. T consists of edges 0--1 and 2--3.
    edges=[(0,1),(2,3)];f=(0,2);g=(3,1);k=3
    maps,values=repaired_maps(4,f,g,k);graph=defaultdict(set)
    for m in maps:
        for a,b in edges:graph[m[a]].add(m[b]);graph[m[b]].add(m[a])
    path=shortest_path(graph,maps[0][0],maps[0][2])
    assert path is not None
    assert len(graph)==26 and sum(map(len,graph.values()))==52
    assert all(len(neighbors)==2 for neighbors in graph.values())
    reached={maps[0][0]};queue=deque(reached)
    while queue:
        u=queue.popleft()
        for v in graph[u]-reached:reached.add(v);queue.append(v)
    assert len(reached)==26
    assert len(path)-1==13
    print(json.dumps({'scope':'generic graph gluing, not asserted to occur in C.1',
        'source_S_edges':[],'target_T_edges':edges,'f':f,'g':g,'k':k,'s':4*k+1,
        'point_transition_paths':[[0,3],[2,1]],
        'old_T_components':[[0,1],[2,3]],
        'f_component_images':[0,1],'g_component_images':[1,0],
        'new_graph_vertices':len(graph),'new_graph_edges':sum(map(len,graph.values()))//2,
        'new_graph_is_a_26_cycle':True,'alpha_0':maps[0],
        'path_between_old_distinct_components':path,
        'path_in_coordinate_labels':[values[v] for v in path],
        'path_length':len(path)-1},indent=2))
