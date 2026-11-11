"""Finite categorical checks for the two printed XII 273--274 errors.

The noncontractibility and acyclicity of A are certified by finite_examples.py
and the written proof.  Here we verify the precise cube and pullback hypotheses.
"""
import json
from pathlib import Path
from finite_examples import FiniteCategory, acyclic_category, add_terminal_cones
from ag_audit_examples import full_subcategory

OUT = Path(__file__).resolve().parent

def inclusion(A, B):
    assert set(A.objects) <= set(B.objects)
    assert set(A.arrows) <= set(B.arrows)
    for k, v in A.comp.items():
        assert B.comp[k] == v
    return {'objects': {x: x for x in A.objects},
            'arrows': {a[0]: a[0] for a in A.arrows}}

def mv(square):
    zero, one, two, three = square
    assert set(zero.objects) == set(one.objects) & set(two.objects)
    assert set(three.objects) == set(one.objects) | set(two.objects)
    assert set(three.arrows) == set(one.arrows) | set(two.arrows)
    assert three.is_sieve(one.objects) and three.is_sieve(two.objects)
    return [inclusion(zero, one), inclusion(zero, two),
            inclusion(one, three), inclusion(two, three)]

def main():
    A = acyclic_category()
    suspension = add_terminal_cones(A, ('plus', 'minus'))
    Cplus = full_subcategory(suspension, A.objects + ('plus',))
    Cminus = full_subcategory(suspension, A.objects + ('minus',))
    X = [A, A, Cminus, Cminus]
    Y = [A, Cplus, Cminus, suspension]
    source_edges, target_edges = mv(X), mv(Y)
    vertical = [inclusion(x, y) for x, y in zip(X, Y)]
    # All functors are literal inclusions, so all six faces strictly commute.
    assert all(v == k for f in vertical for k, v in f['objects'].items())
    assert all(v == k for f in vertical for k, v in f['arrows'].items())
    I = FiniteCategory(('0', '1'),
                       [('id:0', '0', '0'), ('id:1', '1', '1'), ('a', '0', '1')],
                       {('id:0', 'id:0'): 'id:0', ('id:1', 'id:1'): 'id:1',
                        ('id:1', 'a'): 'a', ('a', 'id:0'): 'a'})
    E0 = full_subcategory(I, ('0',))
    E1 = full_subcategory(I, ('1',))
    empty = full_subcategory(I, ())
    parallel = FiniteCategory(('a','t'),
                              [('id:a','a','a'),('id:t','t','t'),
                               ('alpha','a','t'),('beta','a','t')],
                              {('id:a','id:a'):'id:a',('id:t','id:t'):'id:t',
                               ('alpha','id:a'):'alpha',('id:t','alpha'):'alpha',
                               ('beta','id:a'):'beta',('id:t','beta'):'beta'})
    assert not set(E0.objects) & set(E1.objects)
    result = {
        'cube_6c': {'categories': {name: c.verify() for name, c in
                                  [('A', A), ('CA_plus', Cplus),
                                   ('CA_minus', Cminus), ('SigmaA', suspension)]},
                    'source_vertices': ['A', 'A', 'CA_minus', 'CA_minus'],
                    'target_vertices': ['A', 'CA_plus', 'CA_minus', 'SigmaA'],
                    'both_squares_MV': True, 'all_faces_strictly_commute': True,
                    'weak_equivalence_status_from_written_proof':
                    {'f0': True, 'f1': False, 'f2': True, 'f3': True}},
        'cofibration_recognition': {'parallel_arrow_category':parallel.verify(),
                                   'homology':parallel.homology(),
                                   'source_is_sieve':parallel.is_sieve(('a',)),
                                   'boundary_weight_cardinality':2,
                                   'universal_cofibrancy':'Proved for every complement change in G.10'},
        'literal_Cons2': {'categories': {name: c.verify() for name, c in
                                       [('empty', empty), ('point0', E0),
                                        ('point1', E1), ('interval', I)]},
                         'pullback_objects': [],
                         'pullback_arrows': [],
                         'other_three_vertices_have_terminal_objects': True,
                         'initial_legs_are_W_cofibrations':
                         'Written coproduct-stability argument for every modern fundamental localizer',
                         'failure_for_nonzero_ring_R': 'H0(empty;R)=0, H0(point;R)=R'}
    }
    data = {'cube_vertical_maps': vertical, 'source_edges': source_edges,
            'target_edges': target_edges,
            'cofibration_recognition_category':parallel.export(),
            'Cons2_categories': {name: c.export() for name, c in
                                [('empty', empty), ('point0', E0),
                                 ('point1', E1), ('interval', I)]}}
    (OUT/'ag_small_checks_data.json').write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
