"""Exact finite verification of XIIapp ms. 15's S^2 and S^3 categories.

Run with Python 3 and SymPy from any directory.  The full finite nerves are
computed, not a fixed truncation of an infinite nerve.  Category and chain
utilities are imported from the supplied independent path checker.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
import json
from path_checks import Category, sphere_category, nerve_matrices


def main():
    base = sphere_category()
    base.check()
    objects = base.objects + ('e', 't')
    arrows = dict(base.arrows)
    for z in ('e', 't'):
        arrows['id_' + z] = (z, z)
        for x in base.objects:
            arrows[x + '_to_' + z] = (x, z)
    identities = {x: 'id_' + x for x in objects}

    def compose(g, f):
        if f.startswith('id_'):
            return g
        if g.startswith('id_'):
            return f
        if g in base.arrows:
            return base.compose(g, f)
        return arrows[f][0] + '_to_' + arrows[g][1]

    double = Category(objects, arrows, identities, compose)
    double.check()
    hb, hd = nerve_matrices(base), nerve_matrices(double)
    assert hb['simplex_counts'] == [4, 6, 4, 0]
    assert hd['simplex_counts'] == [6, 14, 16, 8, 0]
    assert [v['rank'] for v in hb['homology']] == [1, 0, 1]
    assert [v['rank'] for v in hd['homology']] == [1, 0, 0, 1]
    assert all(not v['torsion'] for h in (hb, hd) for v in h['homology'])
    # With spanning tree {r,A,B}, the remaining generators are s,c,d.
    # All four triangles give c=1, s=c, d=1, s=d, so pi_1 is trivial.
    relations = [('r','A','c'), ('s','A','c'),
                 ('r','B','d'), ('s','B','d')]
    assert all(base.compose(g, f) == h for f,g,h in relations)
    report = {'sphere': {'objects': len(base.objects), 'arrows': len(base.arrows),
                          'full_nerve': hb,
                          'pi1_tree': ['r','A','B'],
                          'pi1_relations_after_tree': ['c=1','s=c','d=1','s=d'],
                          'pi1_trivial': True},
              'double_cone': {'objects': len(double.objects), 'arrows': len(double.arrows),
                              'full_nerve': hd},
              'all_category_axioms': 'PASS',
              'all_chain_identities': 'PASS',
              'integral_smith_forms': 'PASS'}
    result = json.dumps(report, indent=2) + '\n'
    output = Path(__file__).resolve().parent / 'outputs'
    output.mkdir(exist_ok=True)
    (output / 'appendix_gluing_check.out').write_text(result, encoding='utf-8')
    print(result, end='')


if __name__ == '__main__':
    main()
