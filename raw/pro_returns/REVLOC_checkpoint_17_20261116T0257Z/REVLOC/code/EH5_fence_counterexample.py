"""Exact finite certificate refuting the proposed criterion in Part E.1.

All categories here are posets, with at most one arrow between two objects.
We check every composition, every comma category, all homology groups via
integer Smith normal form, and the offending strict base change.
"""
import json
from itertools import combinations, product
from pathlib import Path
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

OUT = Path(__file__).parent / "outputs" / "EH5_fence_counterexample.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

def category(objects, nonidentity):
    relation = {(x,x) for x in objects} | set(nonidentity)
    assert all((a,c) in relation for a,b in relation for b2,c in relation if b == b2)
    assert all(a == b or (b,a) not in relation for a,b in relation)
    return (tuple(objects), relation)

def subcategory(C, objects):
    O = set(objects)
    return category(tuple(x for x in C[0] if x in O), {(a,b) for a,b in C[1] if a in O and b in O and a!=b})

def homology(C):
    O, R = C
    chains = []
    for k in range(len(O)):
        level = [t for t in product(O, repeat=k+1)
                 if len(set(t))==k+1 and all((t[i],t[i+1]) in R for i in range(k))]
        chains.append(level)
    matrices = [Matrix.zeros(0,len(chains[0]))]
    for n in range(1,len(chains)):
        idx = {t:i for i,t in enumerate(chains[n-1])}
        D = Matrix.zeros(len(chains[n-1]),len(chains[n]))
        for j,t in enumerate(chains[n]):
            for i in range(n+1):
                D[idx[t[:i]+t[i+1:]],j] += (-1)**i
        matrices.append(D)
    for n in range(2,len(matrices)):
        assert matrices[n-1]*matrices[n] == Matrix.zeros(matrices[n-1].rows,matrices[n].cols)
    # Every boundary matrix here has primitive image in its whole chain group,
    # which proves torsion-freeness of the corresponding homology quotient.
    smith = []
    for D in matrices:
        S = smith_normal_form(D,domain=ZZ)
        ds = [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
        assert all(d==1 for d in ds)
        smith.append(ds)
    betti = [len(chains[n])-matrices[n].rank()-(matrices[n+1].rank() if n+1<len(matrices) else 0)
             for n in range(len(chains))]
    return {"chain_ranks":[len(x) for x in chains],"boundary_smith":smith,"integral_betti":list(map(int,betti))}

E = category(("a","b","d","c"), {("a","b"),("d","b"),("d","c")})
B = category((0,1,2), {(0,1),(1,2),(0,2)})
p = {"a":0,"b":1,"d":1,"c":2}
assert all((p[x],p[y]) in B[1] for x,y in E[1])
result = {"E_objects":E[0],"E_arrows":sorted(E[1]),"B_objects":B[0],"B_arrows":sorted(B[1]),"p":p}
result["fibers"] = {str(i):homology(subcategory(E,[x for x in E[0] if p[x]==i])) for i in B[0]}
result["commas"] = {str(i):homology(subcategory(E,[x for x in E[0] if p[x]<=i])) for i in B[0]}
for name in ("fibers","commas"):
    assert all(v["integral_betti"]==[1]+[0]*(len(v["integral_betti"])-1) for v in result[name].values())
edge_pullback = subcategory(E,("a","c"))
endpoint_pullback = subcategory(E,("a",))
result["edge_0_to_2_pullback"] = homology(edge_pullback)
result["endpoint_0_pullback"] = homology(endpoint_pullback)
assert result["edge_0_to_2_pullback"]["integral_betti"][0]==2
assert result["endpoint_0_pullback"]["integral_betti"][0]==1
result["all_tests_passed"] = True
OUT.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
