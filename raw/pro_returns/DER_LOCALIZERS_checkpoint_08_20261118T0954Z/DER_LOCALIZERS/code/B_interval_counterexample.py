"""Finite certificates for the all-interval integral-homology counterexample.
The graph map f sends a to a and b to b*a*b*a^-1*b^-1.
We verify its cellular homology map, and non-extension to the finite solvable
one-object groupoid S3, including the freedom of simultaneous conjugation.
Only Python's standard library is used.
"""
from itertools import permutations, product
from json import dumps
G = list(permutations(range(3)))
one = tuple(range(3))
def mul(g,h): return tuple(g[h[i]] for i in range(3))
def inv(g): return tuple(g.index(i) for i in range(3))
def comm(g,h): return mul(mul(mul(g,h),inv(g)),inv(h))
def conj(g,h): return mul(mul(g,h),inv(g))
def closure(gens):
    s={one,*gens}
    while True:
        t=s|{inv(x) for x in s}|{mul(x,y) for x in s for y in s}
        if t==s:return s
        s=t
def derived(s):return closure({comm(x,y) for x in s for y in s})
assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(G,repeat=3))
D1=derived(set(G));D2=derived(D1)
assert len(D1)==3 and D2=={one}
# Word convention: 1=a, 2=b, negative integers are inverses.
f_a=[1]
f_b=[2,1,2,-1,-2]
def exponent_vector(w):return [sum((1 if a>0 else -1) for a in w if abs(a)==i) for i in (1,2)]
cols=[exponent_vector(w) for w in (f_a,f_b)]
assert cols==[[1,0],[0,1]]
def eval_word(w,a,b):
    value=one
    for letter in w:
        v={1:a,2:b}[abs(letter)]
        value=mul(value,v if letter>0 else inv(v))
    return value
images={(eval_word(f_a,a,b),eval_word(f_b,a,b)) for a,b in product(G,repeat=2)}
label_target=((0,2,1),(1,0,2))
assert label_target not in images
assert all((conj(s,label_target[0]),conj(s,label_target[1])) not in images for s in G)
# Explicit finite simplicial graphs: two triangular target circles.
Y_edges=[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]
Y_cycles={1:[(0,0,1),(1,1,2),(2,2,0)],
          2:[(3,0,3),(4,3,4),(5,4,0)]}
X_edges=[]; X_edge_map=[]; X_vertex_map={0:0}; next_vertex=1
for word in (f_a,f_b):
    path=[]
    for letter in word:
        segment=Y_cycles[abs(letter)]
        if letter<0:segment=[(e,t,s) for e,s,t in reversed(segment)]
        path.extend((e,s,t,letter>0) for e,s,t in segment)
    current=0
    for ix,(e,s,t,positive) in enumerate(path):
        assert X_vertex_map[current]==s
        target=0 if ix==len(path)-1 else next_vertex
        if target:
            next_vertex+=1;X_vertex_map[target]=t
        else:assert t==0
        X_edges.append((current,target) if positive else (target,current))
        X_edge_map.append(e)
        current=target
assert len(X_vertex_map)==17 and len(X_edges)==18
assert all((X_vertex_map[s],X_vertex_map[t])==Y_edges[e]
           for (s,t),e in zip(X_edges,X_edge_map))
def components(vertices,edges):
    sets=[{v} for v in vertices]
    for s,t in edges:
        touching=[q for q in sets if s in q or t in q]
        merged=set().union(*touching)
        sets=[q for q in sets if q not in touching]+[merged]
    return len(sets)
assert components(X_vertex_map,X_edges)==components(range(5),Y_edges)==1
assert len(X_edges)-len(X_vertex_map)+1==len(Y_edges)-5+1==2
result={
 'finite_simplicial_graphs':{'Y_edges':Y_edges,'X_edges':X_edges,'vertex_map':X_vertex_map,'edge_map':X_edge_map,'X_counts':[17,18],'Y_counts':[5,6]},
 'group':'S3, permutations of {0,1,2}, multiplication composition',
 'group_order':len(G), 'derived_subgroup_orders':[len(G),len(D1),len(D2)],
 'f_on_words':{'a':f_a,'b':f_b},
 'H0_map':[[1]],'H1_matrix_columns':cols,'higher_homology':'zero for both rank-two graphs',
 'Hom(F2,S3)_size':len(G)**2,'precomposition_image_size':len(images),
 'unextendible_labels':label_target,
 'unextendible_even_up_to_simultaneous_conjugacy':True,
 'conclusion':'The mapping-cylinder inclusion is an integral homology equivalence but is not left orthogonal to NS3 -> *.'
}
print(dumps(result,indent=2))
