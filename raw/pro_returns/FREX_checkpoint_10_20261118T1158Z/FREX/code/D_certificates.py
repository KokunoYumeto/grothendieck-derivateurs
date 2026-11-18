"""Finite certificates for the predimension classification (standard library only)."""
from itertools import combinations
from fractions import Fraction
from pathlib import Path


def hypergraph_data(k,a,b,n,edges):
    masks=[sum(1<<v for v in e) for e in edges]
    delta=lambda s:a*s.bit_count()-b*sum((e&s)==e for e in masks)
    whole=(1<<n)-1
    d=delta(whole)
    bad=[]
    for s in range(1,whole):
        if s.bit_count()>=2 and delta(s)<d:
            bad.append((s,delta(s)))
    assert a<d<=Fraction(a*n,2),(k,a,b,n,d)
    assert not bad,(k,a,b,n,d,bad[:2])
    return d,len(edges)


def atom(k,a,b):
    assert b<(k-1)*a
    if k==2 and 2*b>=a:
        d=a-b
        n=a//d+1
        edges={tuple(sorted((i,(i+1)%n))) for i in range(n)}
        return n,sorted(edges),'cycle'
    if b<=a:
        bound=2*a-b if k==2 else 2*a
        n=4
        from math import comb
        while a*n-b*comb(n,k)>bound:
            n+=1
        e=(a*n-bound+b-1)//b
        return n,list(combinations(range(n),k))[:e],'truncated clique'
    q=(b+a-1)//a-1
    d=b-q*a
    c=k-q
    r=((c-1)*a-1)//d
    n=c+r*q
    edges=[tuple(range(c))+tuple(range(c+j*q,c+(j+1)*q)) for j in range(r)]
    return n,edges,'petals'


def graph_automorphisms(n,adj):
    # Grow a connected assignment order. At each step, exact adjacency to
    # every previously assigned vertex is required. This enumerates all.
    order=[0]
    while len(order)<n:
        unused=set(range(n))-set(order)
        v=max(unused,key=lambda u:(len(adj[u]&set(order)),-u))
        order.append(v)
    result=[]
    def visit(mp,used):
        if len(mp)==n:
            result.append(tuple(mp[v] for v in range(n)));return
        u=order[len(mp)]
        for v in range(n):
            if v in used:continue
            if all(((x in adj[u])==(y in adj[v])) for x,y in mp.items()):
                mp[u]=v;used.add(v);visit(mp,used);used.remove(v);del mp[u]
    visit({},set())
    return result


def frucht_certificate():
    n=12
    jumps=[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
    edges={tuple(sorted((v,(v+1)%n))) for v in range(n)}
    edges|={tuple(sorted((v,(v+jumps[v])%n))) for v in range(n)}
    edges=sorted(edges)
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    assert all(len(a)==3 for a in adj)
    cuts=[sum(((s>>u)&1)!=((s>>v)&1) for u,v in edges) for s in range(1,(1<<n)-1)]
    autos=graph_automorphisms(n,adj)
    assert min(cuts)==3
    assert autos==[tuple(range(n))]
    removed=0
    hyp=[tuple(i for i,e in enumerate(edges) if v in e) for v in range(n) if v!=removed]
    d,e=hypergraph_data(3,2,3,len(edges),hyp)
    print('Cubic graph:',edges)
    print('All degrees = 3; minimum nontrivial edge cut =',min(cuts))
    print('Automorphisms:',autos)
    print('Removed graph vertex:',removed)
    print('Hyperedges on edge-token vertices 0..17:',hyp)
    print('Hypergraph n =',len(edges),'e =',e,'delta =',d)
    print('Exhaustive nonempty subsets checked:',(1<<len(edges))-1)
    print('Every subset of size >=2 has delta >=3; singleton delta =2.')
    return hyp


def five_edge_example():
    es=[(0,1,2),(1,2,3),(2,3,4),(0,1,3),(1,3,4)]
    coeff=[1,1,1,-1,-1]
    marginals=[]
    for j in range(3):
        m=[sum(c for c,e in zip(coeff,es) if e[j]==v) for v in range(5)]
        marginals.append(m)
    assert marginals==[[0,0,1,0,0]]*3
    print('Lead 8(e): coefficient augmentation =',sum(coeff),'; marginals =',marginals)
    for a,b in [(3,1),(2,1),(1,1),(5,2)]:
        masks=[sum(1<<v for v in e) for e in es]
        de=lambda s:a*s.bit_count()-b*sum((e&s)==e for e in masks)
        positive=all(de(s)>0 for s in range(1,32))
        closed=all(all(de(u)>de(e) for u in range(32) if u!=e and (u&e)==e) for e in masks)
        print('  a,b=',a,b,'positive=',positive,'all five edges closed=',closed)


if __name__=='__main__':
    print('Universal atom finite checks (all constructed examples <=18 vertices):')
    count=0;large=0
    for k in range(2,8):
        for a in range(1,7):
            for b in range(1,(k-1)*a):
                n,es,kind=atom(k,a,b)
                if n>18:large+=1;continue
                d,e=hypergraph_data(k,a,b,n,es)
                count+=1
    print('Validated parameter triples:',count,'; skipped for exponential size:',large)
    for k,a,b in [(2,2,1),(3,3,1),(3,2,3),(4,3,4),(5,3,7)]:
        n,es,kind=atom(k,a,b)
        d,e=hypergraph_data(k,a,b,n,es)
        print('Atom',k,a,b,':',kind,'n=',n,'e=',e,'delta=',d,'edges=',es)
    five_edge_example()
    # Every tuple has its own private vertex, certifying 1-sparsity.
    tuples=[(i,j,8+t) for t,(i,j) in enumerate(combinations(range(8),2))]
    assert len({z for i,j,z in tuples})==len(tuples)==28
    assert len(tuples)>3*8
    print('Shadow-remark counterexample: 28 private ternary tuples, K8 shadow, 28 > 24.')
    frucht_certificate()
