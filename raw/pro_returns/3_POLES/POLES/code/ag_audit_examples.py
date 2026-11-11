"""Exact checks for the manuscript-audit counterexamples in Part G.

Uses the fully specified 35-object category and integer chain checker from
finite_examples.py.  The categorical smoothness criterion and van Kampen
arguments are written in the paper; this program verifies all finite data.
"""
import json
from pathlib import Path
from finite_examples import FiniteCategory, acyclic_category, add_terminal_cones

OUT=Path(__file__).resolve().parent

def generated_four_object_category():
    obs=('x','z','a','b')
    nonid=[('alpha','x','z'),('beta','x','z'),('r','z','a'),
           ('s','z','b'),('ra','x','a'),('sa','x','b')]
    arrows=[(f'id:{x}',x,x) for x in obs]+nonid
    comp={}
    for f,x,y in arrows:
        comp[f,f'id:{x}']=f
        comp[f'id:{y}',f]=f
    for t,composite in [('r','ra'),('s','sa')]:
        for source in ('alpha','beta'):comp[t,source]=composite
    return FiniteCategory(obs,arrows,comp)

def full_subcategory(cat,objects):
    objects=set(objects)
    arrows=[a for a in cat.arrows if a[1] in objects and a[2] in objects]
    ids={a[0] for a in arrows}
    return FiniteCategory(sorted(objects),arrows,
                          {k:v for k,v in cat.comp.items() if k[0] in ids and k[1] in ids})

def smooth_integral(cats):
    # cats[0] includes literally into cats[1], cats[2].  The base has 1->0<-2.
    obs=[f'{i}|{o}' for i,c in cats.items() for o in c.objects]
    meta={}; arrows=[]; ids={}
    for i,c in cats.items():
        for a,s,t in c.arrows:
            aid=f'id:{i}|{s}' if a==c.identities[s] else f'{i}|{a}'
            arrows.append((aid,f'{i}|{s}',f'{i}|{t}'))
            meta[aid]=(i,i,a);ids[i,i,a]=aid
    for j in (1,2):
        for a,s,t in cats[j].arrows:
            if t not in cats[0].objects:continue
            aid=f'{j}>0|{a}'
            arrows.append((aid,f'{j}|{s}',f'0|{t}'))
            meta[aid]=(j,0,a);ids[j,0,a]=aid
    comp={}
    for f,s,t in arrows:
        for g,tt,u in arrows:
            if t!=tt:continue
            i,j,uf=meta[f];jj,k,ug=meta[g]
            assert j==jj
            # Internal arrows of cats[0] have the same names under either inclusion.
            underlying=cats[i].comp[ug,uf]
            comp[g,f]=ids[i,k,underlying]
    return FiniteCategory(obs,arrows,comp)

def connected_components(objects,edges):
    parent={o:o for o in objects}
    def root(o):
        while parent[o]!=o:
            parent[o]=parent[parent[o]];o=parent[o]
        return o
    for x,y in edges:parent[root(x)]=root(y)
    return len({root(o) for o in objects})

def main():
    C=generated_four_object_category()
    Psi=full_subcategory(C,('z','a','b'))
    commas={}
    for c in C.objects:
        objects=[a for a in C.arrows if a[1]==c and a[2] in Psi.objects]
        edges=[]
        for a,_,s in objects:
            for b,_,t in objects:
                for h,ss,tt in Psi.arrows:
                    if ss==s and tt==t and C.comp[h,a]==b:edges.append((a,b))
        components=connected_components([a[0] for a in objects],edges)
        assert objects and components==1
        commas[c]={'objects':len(objects),'arrows':len(edges),'components':components}
    sphere3=add_terminal_cones(C,('plus','minus'))
    A=acyclic_category()
    P={0:A,1:add_terminal_cones(A,('cone_plus',)),2:add_terminal_cones(A,('cone_minus',))}
    T={i:add_terminal_cones(p,('upper_t',)) for i,p in P.items()}
    I=smooth_integral(T)
    K=smooth_integral(P)
    p0={f'{i}|{o}' for i,p in P.items() for o in p.objects}
    lift_reports={}
    for i in (0,1,2):
        target=f'{i}|upper_t'
        lift_arrows=[a for a in I.arrows if a[2]==target and a[1] in p0]
        domain_objects=[a[1] for a in lift_arrows]
        assert len(domain_objects)==len(set(domain_objects))
        expected=set(K.objects) if i==0 else {f'{i}|{o}' for o in P[i].objects}
        assert set(domain_objects)==expected, (i,sorted(set(domain_objects)-expected),sorted(expected-set(domain_objects)))
        # Uniqueness of arrows into the target makes the lift category the full subcategory.
        L=full_subcategory(I,expected)
        if i==0:
            assert set(L.arrows)==set(K.arrows) and L.comp==K.comp
        lift_reports[str(i)]={'category_axioms':L.verify(),
                              'identified_with': 'smooth integral of CA <- A -> CA' if i==0 else f'cone {i}'}
    result={'fork':{'category_axioms':Psi.verify(),'homology':Psi.homology()},
            'target_S2':{'category_axioms':C.verify(),'homology':C.homology(),
                         'outgoing_comma_categories':commas,'inclusion_final':True},
            'pushout_S3':{'category_axioms':sphere3.verify(),'homology':sphere3.homology()},
            'smoothness_counterexample':{'integral_category_axioms':I.verify(),
                                        'exceptional_lift_categories':lift_reports,
                                        'central_lift_homology':K.homology(),
                                        'central_bad_source_lift':'A: the acyclic non-simply-connected 35-object category'},
            'limitations':'Homotopy types S2, S3 and simple connectivity of the central lift follow from the written cone/van Kampen proofs; the program verifies finite categorical and chain data.'}
    (OUT/'ag_audit_examples_data.json').write_text(json.dumps({'C':C.export(),'Psi':Psi.export(),
                                                            'smooth_integral':I.export()},indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
