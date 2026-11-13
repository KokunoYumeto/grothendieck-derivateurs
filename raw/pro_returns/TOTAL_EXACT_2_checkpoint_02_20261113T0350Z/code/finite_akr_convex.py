"""Exact finite check of componentwise geodesic convexity of AKR images.

No all-stage claim is made. For every distinct incoming arrow image whose
source has >=4 points, test every connected component of its induced graph.
Singletons and edge components are tautologically convex in a simple graph.
Ambient BFS tracks whether any shortest path has left the specified image.
"""
import argparse,json,time
from collections import defaultdict,deque
from finite_akr_intersections import build


def restricted_distances(graph,source,image):
    distances={source:0};queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if v in image and v not in distances:
                distances[v]=distances[u]+1;queue.append(v)
    return distances


def outside_path(graph,source,target,image,max_distance):
    initial=(source,False);parent={initial:None};distance={initial:0};queue=deque([initial])
    while queue:
        state=queue.popleft();u,out=state
        if u==target and out:
            path=[]
            while state is not None:path.append(state[0]);state=parent[state]
            return path[::-1]
        if distance[state]==max_distance:continue
        for v in graph[u]:
            nxt=(v,out or v not in image)
            if nxt not in parent:
                parent[nxt]=state;distance[nxt]=distance[state]+1;queue.append(nxt)
    raise AssertionError('reported violation has no independently reconstructed path')


def check(C):
    result={'objects':len(C.size),'minimum_source_size':4,'targets':[],'failures':[]}
    for z in range(len(C.size)):
        graph=defaultdict(set)
        for f in C.hom.get((1,z),()):
            graph[f[0]].add(f[1]);graph[f[1]].add(f[0])
        incoming={}
        for x in range(z):
            if C.size[x]<4:continue
            for f in C.hom.get((x,z),()):incoming.setdefault(frozenset(f),(x,f))
        stats={'target':C.names[z],'incoming_distinct_images':len(incoming),
               'images_checked':0,'source_BFS_checks':0,'ambient_vertices_visited':0}
        for image,(x,f) in incoming.items():
            stats['images_checked']+=1
            for source in sorted(image):
                intrinsic=restricted_distances(graph,source,image)
                if len(intrinsic)<=2 or source==max(intrinsic):continue
                radius=max(intrinsic.values());distances={source:0};outside={source:False};queue=deque([source])
                while queue:
                    u=queue.popleft()
                    if distances[u]>=radius:continue
                    for v in graph[u]:
                        length=distances[u]+1;left=outside[u] or v not in image
                        if v not in distances:
                            distances[v]=length;outside[v]=left;queue.append(v)
                        elif distances[v]==length and left:
                            outside[v]=True
                stats['source_BFS_checks']+=1;stats['ambient_vertices_visited']+=len(distances)
                for v,d in intrinsic.items():
                    if v<=source:continue
                    if distances[v]<d or outside[v]:
                        path=outside_path(graph,source,v,image,d)
                        assert len(path)-1<=d and any(w not in image for w in path)
                        result['failures'].append({'target':C.names[z],
                            'source_object':C.names[x],'map':f,'image':sorted(image),
                            'vertices':[source,v],'intrinsic_distance':d,
                            'ambient_distance':distances[v],
                            'shortest_or_shorter_path_leaving_image':path})
                        break
                if result['failures']:break
            if result['failures']:break
        result['targets'].append(stats);print(json.dumps(stats),flush=True)
        if result['failures']:break
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--stage',choices=['k1','selected_k2','critical_k3'],default='k1')
    args=ap.parse_args();start=time.time();result=check(build(args.stage));result['stage']=args.stage
    result['elapsed_seconds']=time.time()-start
    print(json.dumps(result,indent=2),flush=True)
