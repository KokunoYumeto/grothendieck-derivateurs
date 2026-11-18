"""Exact finite audit of G.26's three-interval cancellation identities.
No finite experiment is used as a substitute for the arbitrary-tree proof.
"""
from itertools import product
from collections import deque


def trees(n):
    if n == 2:
        yield [(0, 1)]
        return
    for seq in product(range(n), repeat=n-2):
        deg=[1]*n
        for v in seq: deg[v]+=1
        edges=[]
        for v in seq:
            leaf=next(i for i,d in enumerate(deg) if d==1)
            edges.append((leaf,v));deg[leaf]-=1;deg[v]-=1
        a,b=[i for i,d in enumerate(deg) if d==1]
        edges.append((a,b))
        yield edges


def order(n,edges,bits):
    reach=[[i==j for j in range(n)] for i in range(n)]
    for (a,b),bit in zip(edges,bits):
        if bit: a,b=b,a
        reach[a][b]=True
    for k in range(n):
        for i in range(n):
            for j in range(n): reach[i][j] |= reach[i][k] and reach[k][j]
    return reach


def bound(n,le,a,b,upper):
    c=[x for x in range(n) if (le[a][x] and le[b][x] if upper else le[x][a] and le[x][b])]
    best=[x for x in c if all(le[x][y] if upper else le[y][x] for y in c)]
    assert len(best)==1,(a,b,upper,c,best)
    return best[0]

count=0;extensions=0;orientations=0
for n in range(2,6):
    for edges in trees(n):
        for bits in product((0,1), repeat=n-1):
            le=order(n,edges,bits);orientations+=1
            for a,b,c,d in product(range(n),repeat=4):
                if le[a][b] and le[c][b] and le[c][d]:
                    e=bound(n,le,a,c,True);f=bound(n,le,b,d,False)
                    assert le[e][f] or le[f][e]
                    if le[e][f]:
                        assert bound(n,le,e,d,False)==e
                        assert bound(n,le,a,f,True)==f
                        assert le[a][d]
                    else:
                        assert bound(n,le,e,d,False)==f
                        assert bound(n,le,a,f,True)==e
                    count+=1
                if a!=b and le[a][b] and le[b][d] and le[a][c]:
                    if bound(n,le,c,b,False)==a:
                        assert bound(n,le,c,d,False)==a
                        extensions+=1
print('Finite oriented trees checked:',orientations)
print('Three-interval identities checked:',count)
print('Preceding-turn extension identities checked:',extensions)
print('All exact checks passed. Scope: finite audit only; proof is in G.26.')
