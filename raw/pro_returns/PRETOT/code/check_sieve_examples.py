"""Exact checks for PRETOT C/D. Python 3 + sympy; no randomized tests."""
from itertools import combinations, product
from pathlib import Path
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
import json


def category(objects, arrows, composition):
    """arrows maps name to (source,target); composition(g,f)=g after f."""
    ids = {o: 'id_' + o for o in objects}
    for f, (s,t) in arrows.items():
        assert composition(f, ids[s]) == f
        assert composition(ids[t], f) == f
    for h,g,f in product(arrows, repeat=3):
        if arrows[f][1] == arrows[g][0] and arrows[g][1] == arrows[h][0]:
            assert composition(h,composition(g,f)) == composition(composition(h,g),f)
    return objects, arrows, composition


def idempotent_retract():
    Aob=['a']; Aarr={'id_a':('a','a'),'e':('a','a')}
    def common_comp(g,f):
        if f.startswith('id_'): return g
        if g.startswith('id_'): return f
        if f=='e' and g=='e': return 'e'
        if f=='e' and g in ('beta','gamma'): return 'beta'
        raise AssertionError((g,f))
    A=category(Aob,Aarr,common_comp)
    C=category(['a','b'],dict(Aarr,id_b=('b','b'),beta=('a','b'),gamma=('a','b')),common_comp)
    B=category(['a','b'],dict(Aarr,id_b=('b','b'),beta=('a','b')),common_comp)
    retract={f:('beta' if f=='gamma' else f) for f in C[1]}
    for g,f in product(C[1],repeat=2):
        if C[1][f][1]==C[1][g][0]:
            assert retract[C[2](g,f)] == B[2](retract[g],retract[f])
    assert all(retract[f]==f for f in B[1])
    # right adjoint r:C->A: r(beta)=e, r(gamma)=id_a, r(e)=e.
    r={'id_a':'id_a','id_b':'id_a','e':'e','beta':'e','gamma':'id_a'}
    for g,f in product(C[1],repeat=2):
        if C[1][f][1]==C[1][g][0]:
            assert r[C[2](g,f)]==A[2](r[g],r[f])
    counit={'a':'id_a','b':'gamma'}
    for x in C[0]:
        homA=[f for f in A[1]]
        homC=[f for f,(s,t) in C[1].items() if s=='a' and t==x]
        images=[C[2](counit[x],f) for f in homA]
        assert sorted(images)==sorted(homC)
    for f,(s,t) in C[1].items():
        assert C[2](f,counit[s])==C[2](counit[t],r[f])
    # In B the generated cosieve is B but Hom(a,b) has one element;
    # no object of A can represent it, since End_A(a) has two elements.
    assert len([f for f,(s,t) in B[1].items() if s=='a' and t=='b'])==1
    return {'A_objects':1,'A_arrows':2,'B_objects':2,'B_arrows':4,
            'C_objects':2,'C_arrows':5,'all_category_axioms':True,
            'B_retract_of_C_under_A':True,'A_to_C_right_adjoint_checked':True,
            'A_to_B_not_Dwyer_hom_cardinalities':[2,1]}


def poset_homology(objects, lt):
    levels=[[ (x,) for x in objects ]]
    while levels[-1]:
        nxt=[s+(y,) for s in levels[-1] for y in objects if lt(s[-1],y)]
        levels.append(nxt)
    boundaries={}; smith={}; ranks={0:0}
    for n in range(1,len(levels)):
        rows={s:i for i,s in enumerate(levels[n-1])}
        d=Matrix.zeros(len(rows),len(levels[n]))
        for j,s in enumerate(levels[n]):
            for k in range(n+1): d[rows[s[:k]+s[k+1:]],j]+=(-1)**k
        boundaries[n]=d
        if n>1: assert boundaries[n-1]*d == Matrix.zeros(len(levels[n-2]),len(levels[n]))
        sn=smith_normal_form(d,domain=ZZ)
        diag=[abs(int(sn[k,k])) for k in range(min(sn.rows,sn.cols)) if sn[k,k]]
        smith[n]=diag; ranks[n]=len(diag)
    H=[]
    for n in range(len(levels)-1):
        H.append({'degree':n,'free_rank':len(levels[n])-ranks.get(n,0)-ranks.get(n+1,0),
                  'torsion':[d for d in smith.get(n+1,[]) if d>1]})
    return {'simplex_counts':[len(l) for l in levels[:-1]],'integral_homology':H,
            'all_nonzero_smith_invariants_one':all(d==1 for l in smith.values() for d in l)}


def cone_sphere_failure():
    A=[frozenset(s) for k in range(4) for s in combinations(range(4),k)]
    V=[s for s in A if s]
    ends=[frozenset((0,1,2)),frozenset((0,1,3))]
    E=[(s,k) for s in A for k in ([0] if s in ends else [0,1])]
    def elt(a,b):
        s,k=a; t,l=b
        return s<t and (t in ends or k==l)
    aH=poset_homology(A,lambda x,y:x<y)
    vH=poset_homology(V,lambda x,y:x<y)
    eH=poset_homology(E,elt)
    assert [h['free_rank'] for h in aH['integral_homology']]==[1,0,0,0]
    assert [h['free_rank'] for h in vH['integral_homology']]==[1,0,1]
    assert [h['free_rank'] for h in eH['integral_homology']]==[1,1,0,0]
    return {'cone_A':aH,'sphere_cosieve_V':vH,'detecting_action_elements':eH,
            'conclusion':'The initial cone over this S^2 poset is not totally W_2-aspherical.'}


if __name__=='__main__':
    result={'cisinski_retract':idempotent_retract(), 'failed_total_cone_candidate':cone_sphere_failure()}
    report=json.dumps(result,indent=2)
    output_dir=Path(__file__).resolve().parent/'outputs'
    output_dir.mkdir(parents=True,exist_ok=True)
    (output_dir/'check_sieve_examples.out').write_text(report+'\n',encoding='utf-8')
    print(report)
