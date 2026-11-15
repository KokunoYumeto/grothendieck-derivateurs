#!/usr/bin/env python3
"""Finite verification of B035/Lead 5 counterexample and its final S2 image."""
from itertools import product
from pathlib import Path
import json
from ag_finite_examples import named_category, integral_homology
from root_monoid_checks import homology, export


def check_functor(A,B,objects,arrows):
    bnames={a['name']:i for i,a in enumerate(B.arrows)}
    f={i:bnames[arrows[a['name']]] for i,a in enumerate(A.arrows)}
    for i,a in enumerate(A.arrows):
        b=B.arrows[f[i]]
        assert b['source']==objects[a['source']]
        assert b['target']==objects[a['target']]
        if a['identity']: assert b['identity']
    for (g,h),c in A.composites.items():
        assert B.composites[f[g],f[h]]==f[c]
    comma=[]
    for b in B.objects:
        nodes=[(a,i) for a in A.objects for i,v in enumerate(B.arrows)
               if v['source']==b and v['target']==objects[a]]
        edges=[]
        for a,v in nodes:
            for h,arrow in enumerate(A.arrows):
                if arrow['source']==a:
                    w=B.composites[f[h],v]
                    target=(arrow['target'],w)
                    assert target in nodes
                    edges.append(((a,v),target))
        seen={nodes[0]} if nodes else set()
        while True:
            enlarged=set(seen)
            for x,y in edges:
                if x in seen or y in seen: enlarged.update((x,y))
            if enlarged==seen: break
            seen=enlarged
        comma.append(dict(target=b,objects=len(nodes),arrows=len(edges),
                          nonempty_connected=bool(nodes) and seen==set(nodes)))
    assert all(c['nonempty_connected'] for c in comma)
    return dict(functor_laws=True,final=True,comma_categories=comma)


def main():
    E=named_category(['i','h1','h2'],[('e','i','i'),('u1','i','h1'),('u2','i','h2')],
                     {('e','e'):'e',('u1','e'):'u1',('u2','e'):'u2'})
    P=named_category(['0','1','2'],[('a','0','1'),('b','0','2')],{})
    C=named_category(['x','0','1','2'],
                     [('r','x','0'),('s','x','0'),('a','0','1'),('b','0','2'),
                      ('v','x','1'),('w','x','2')],
                     {('a','r'):'v',('a','s'):'v',('b','r'):'w',('b','s'):'w'})
    X=named_category(['u','t'],[('e','u','u'),('hi','u','t'),('h1','u','t'),('h2','u','t')],
                     {('e','e'):'e',('hi','e'):'hi',('h1','e'):'hi',('h2','e'):'hi'})
    fobj={'i':'0','h1':'1','h2':'2'}
    far={'id_i':'id_0','id_h1':'id_1','id_h2':'id_2','e':'id_0','u1':'a','u2':'b'}
    inclusion_objects={o:o for o in P.objects}
    inclusion_arrows={a['name']:a['name'] for a in P.arrows}
    result={}
    for name,cat in [('E',E),('Psi',P),('sphere_C',C),('sieve_target_X',X)]:
        result[name]=dict(validation=cat.validate(),homology=homology(cat))
    result['E_to_Psi']=check_functor(E,P,fobj,far)
    result['Psi_to_C']=check_functor(P,C,inclusion_objects,inclusion_arrows)
    result['E_to_C']=check_functor(E,C,fobj,far)
    successors=lambda o:{a['target'] for a in E.arrows if a['source']==o}
    assert not successors('h1') & successors('h2')
    result['nonfiltered_witness']={'first':'h1','second':'h2','common_successors':[]}
    # R has 1,e; two copies identify e.  The right action of e is constant.
    H=['i','h1','h2']
    act={'1':{h:h for h in H},'e':{h:'i' for h in H}}
    mult=lambda g,f: 'e' if 'e' in (g,f) else '1'
    for g,f,h in product(['1','e'],['1','e'],H):
        assert act[mult(g,f)][h]==act[f][act[g][h]]
    result['presheaf_action']={'values':H,'action':act,'laws':True,
                              'pushout_of_two_representables_along_fixed_element':True}
    assert [z['free_rank'] for z in result['E']['homology']['homology']]==[1,0,0,0,0]
    assert [z['free_rank'] for z in result['sphere_C']['homology']['homology']]==[1,0,1,0,0]
    for r in [result['E'],result['sphere_C']]:
        assert all(not z['torsion'] for z in r['homology']['homology'])
    directory=Path(__file__).resolve().parent
    (directory/'root_presheaf_data.json').write_text(json.dumps({n:export(c) for n,c in [('E',E),('Psi',P),('C',C),('X',X)]},indent=2))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
