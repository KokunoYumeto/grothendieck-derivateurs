"""Finite free-chart certificates supporting the G29 affine cut proof."""
from itertools import combinations

def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a: out.pop()
        else: out.append(a)
    return out

def inv(w):return [-a for a in w[::-1]]

def join(u,v):
    path=red(inv(u)+v)
    i=0
    while i<len(path) and path[i]>0:i+=1
    assert all(a<0 for a in path[i:]), 'no common positive upper bound'
    return red(u+path[:i])

count=0
for m in range(2,7):
    for n in range(1,7):
        spine=list(range(m+1,m+n))
        jL={i:inv([i+1]+spine) for i in range(m)}
        jO={q:inv(spine[q:]) for q in range(n)}
        assert jO[n-1]==[]
        for a,b in combinations(range(m),2):
            assert join(jL[a],jL[b])==jO[0]
            count+=1
        for i in range(m):
            for q in range(n):
                assert red(inv(jL[i])+jO[q])==[i+1]+spine[:q]
                count+=1
        for p in range(n):
            for q in range(p+1,n):
                assert red(inv(jO[p])+jO[q])==spine[p:q]
                count+=1
print('Exact finite oriented-tree join and interval checks:',count)
print('Every distinct pair of left leaves has join the first chain vertex in all tested charts.')
print('The finite proof uses arbitrary m,n; no assertion of an original limit join.')
print('PASS')
