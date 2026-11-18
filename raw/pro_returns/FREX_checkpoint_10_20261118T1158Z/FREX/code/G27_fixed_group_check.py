"""Exact finite checks for G.27; normal-form proof handles all sizes."""
from itertools import combinations

def reduce_group(word):
    out=[]
    for a in word:
        if out and out[-1]==-a: out.pop()
        else: out.append(a)
    return out

def inv(word): return [-x for x in word[::-1]]

w00=[1,3]; w10=[2,3]; w11=[2,4]; w01=[1,4]
rel=w00+inv(w10)+w11+inv(w01)
assert reduce_group(rel)==[]
assert reduce_group([1,-3,4,-2])==[1,-3,4,-2]
print('Four boundary letters: nontrivial reduced relation in Free4, trivial after wij=ai bj.')

def edge_image(n,m,embedding,edge,two_sided):
    # Edges: L0,L1; gap_i (i=0,...,n-2); optional R0,R1.
    if edge[0]=='L': return [('L',edge[1])]+[('g',i) for i in range(embedding[0])]
    if edge[0]=='g': return [('g',i) for i in range(embedding[edge[1]],embedding[edge[1]+1])]
    return [('g',i) for i in range(embedding[-1],m-1)]+[('R',edge[1])]

def edges(n,two): return [('L',0),('L',1)]+[('g',i) for i in range(n-1)]+([('R',0),('R',1)] if two else [])
checks=0
for two in [False,True]:
    for n in range(1,5):
        assert len(edges(n,two))==n+(3 if two else 1)
        for m in range(n,5):
            for e in combinations(range(m),n):
                for k in range(m,6):
                    for f in combinations(range(k),m):
                        comp=tuple(f[i] for i in e)
                        for a in edges(n,two):
                            direct=edge_image(n,k,comp,a,two)
                            twice=sum((edge_image(m,k,f,b,two) for b in edge_image(n,m,e,a,two)),[])
                            assert direct==twice
                            checks+=1
print('Exact subdivision functoriality checks:',checks)
# One-sided group invariant between two chart points:
a0x=[1];a1x=[2];t=[3]
a0y=a0x+t;a1y=a1x+t
assert reduce_group(a0x+inv(a1x))==reduce_group(a0y+inv(a1y))
assert reduce_group(a0x+inv(a1x))==[1,-2]
print('One-sided k is unchanged by a common appended interval and has nonzero left-edge exponent.')
print('PASS')
