"""Finite combinatorial certificates for Part H.5.

The graph category is the category of simplices of a directed graph,
with two distinct face arrows for a loop. Its nerve is its subdivision.
"""
from itertools import permutations, product
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).parent
OUT=ROOT/'outputs'/'EH5_group_witnesses.json'

def mul(p,q): return tuple(p[q[i]] for i in range(3))
def inv(p): return tuple(p.index(i) for i in range(3))
identity=(0,1,2)
perms=list(permutations(range(3)))
x=(1,0,2); y=(2,1,0)
word=[('y',1),('x',-1),('y',-1),('x',1),('y',1)]
def evaluate(w, vals):
    z=identity
    for letter,sgn in w:
        a=vals[letter]
        z=mul(z,a if sgn==1 else inv(a))
    return z
alpha_y=evaluate(word,{'x':x,'y':y})
assert alpha_y==x
def generated(gens):
    S={identity}
    while True:
        T=S|{mul(a,b) for a in S for b in gens}
        if T==S:return S
        S=T
before=generated([x,y]);after=generated([x,alpha_y])
assert len(before)==6 and len(after)==2
def centralizer(S):return [g for g in perms if all(mul(g,h)==mul(h,g) for h in S)]
assert len(centralizer(before))==1
assert len(centralizer(after))==2

# Abelianized Fox derivatives; each prefix is a Laurent monomial.
X,Y=sp.symbols('X Y')
def fox(w,letter):
    prefix=sp.Integer(1);ans=sp.Integer(0)
    for a,sgn in w:
        v=X if a=='x' else Y
        if a==letter:
            ans += prefix if sgn==1 else -prefix/v
        prefix *= v**sgn
    return sp.expand(ans)
J=sp.Matrix([[1,fox(word,'x')],[0,fox(word,'y')]])
assert sp.expand(J.det()-(2-X**-1))==0
assert sum(s for a,s in word if a=='x')==0
assert sum(s for a,s in word if a=='y')==1

# Source graph has the x-loop and the 5-edge y-cycle at vertex 0.
vertices=[f'v{i}' for i in range(5)]
edges=['x0']+[f'e{i}' for i in range(5)]
face={'x0':('v0','v0')}
for i,(a,sgn) in enumerate(word):
    start=f'v{i}';end=f'v{(i+1)%5}'
    face[f'e{i}']=(start,end) if sgn==1 else (end,start)
target_vertices=['v'];target_edges=['x','y']
object_map={v:'v' for v in vertices}|{'x0':'x'}|{f'e{i}':a for i,(a,s) in enumerate(word)}
# Face arrows go vertex->edge, and their distinct labels are kept.
source_arrows=[(f'id_{o}',o,o) for o in vertices+edges]
for e,(s,t) in face.items():
    source_arrows += [(f'{e}_0',s,e),(f'{e}_1',t,e)]
target_arrows=[(f'id_{o}',o,o) for o in target_vertices+target_edges]
for e in target_edges: target_arrows += [(f'{e}_0','v',e),(f'{e}_1','v',e)]
arrow_map={f'id_{o}':f'id_{object_map[o]}' for o in vertices+edges}
arrow_map.update({f'{e}_{j}':f'{object_map[e]}_{j}' for e in edges for j in (0,1)})
lookup={a:(s,t) for a,s,t in target_arrows}
for a,s,t in source_arrows:
    assert lookup[arrow_map[a]]==(object_map[s],object_map[t])
def compose(a,b,arr):
    d={x:(s,t) for x,s,t in arr}
    assert d[a][1]==d[b][0]
    if a.startswith('id_'):return b
    if b.startswith('id_'):return a
    raise AssertionError('No two nonidentity face arrows are composable')
for a,s,t in source_arrows:
    for b,s2,t2 in source_arrows:
        if t==s2:
            assert arrow_map[compose(a,b,source_arrows)]==compose(arrow_map[a],arrow_map[b],target_arrows)
assert len(source_arrows)==23 and len(target_arrows)==7

# Finite S^1 poset and its double cone, for failure of reverse excision.
P=['a','b','c','d'];relations={(u,v) for u in ('a','b') for v in ('c','d')}
def nerve_betti(objects, strict):
    chains=[]
    for n in range(len(objects)):
        chains.append([t for t in product(objects,repeat=n+1)
                       if len(set(t))==n+1 and all((t[i],t[i+1]) in strict for i in range(n))])
    Ds=[sp.zeros(0,len(chains[0]))]
    for n in range(1,len(chains)):
        ix={c:i for i,c in enumerate(chains[n-1])};D=sp.zeros(len(ix),len(chains[n]))
        for j,c in enumerate(chains[n]):
            for i in range(n+1):D[ix[c[:i]+c[i+1:]],j]+=(-1)**i
        Ds.append(D)
    from sympy.matrices.normalforms import smith_normal_form
    smith=[]
    for D in Ds:
        S=smith_normal_form(D,domain=sp.ZZ)
        ds=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
        assert all(d==1 for d in ds);smith.append(ds)
    betti=[len(chains[n])-Ds[n].rank()-(Ds[n+1].rank() if n+1<len(Ds) else 0) for n in range(len(chains))]
    return {'chains':[len(c) for c in chains], 'betti':list(map(int,betti)), 'smith':smith}
cone=P+['u'];cone_rel=relations|{(x,'u') for x in P}
double=P+['u','v'];double_rel=cone_rel|{(x,'v') for x in P}
hP=nerve_betti(P,relations);hU=nerve_betti(cone,cone_rel);hX=nerve_betti(double,double_rel)
assert hP['betti'][:2]==[1,1]
assert hU['betti']==[1,0,0,0,0]
assert hX['betti']==[1,0,1,0,0,0]
result={
 'source_graph_category':{'objects':vertices+edges,'arrows':source_arrows,'object_map':object_map,'arrow_map':arrow_map},
 'target_graph_category':{'objects':target_vertices+target_edges,'arrows':target_arrows},
 'alpha_words':{'x':[['x',1]],'y':word},'H1_matrix':[[1,0],[0,1]],
 'abelianized_Fox_Jacobian':str(J),'determinant':str(sp.expand(J.det())),
 'S3_images':{'x':x,'y':y,'alpha_y':alpha_y,'image_order_before':len(before),'image_order_after':len(after),
              'centralizer_order_before':len(centralizer(before)),'centralizer_order_after':len(centralizer(after))},
 'double_cone':{'S1_poset':hP,'cone':hU,'double_cone':hX,'objects':double,'strict_relations':sorted(double_rel)},
 'all_tests_passed':True}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
