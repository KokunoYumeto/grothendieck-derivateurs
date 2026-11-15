"""Independent exact verification of the reported ordered-graph witnesses.

This file rebuilds all maps directly from edge sets (without importing the
search program), checks coefficients and marginals, and uses SymPy's
DomainMatrix over QQ, GF(2), and GF(3) for a second rank calculation.
"""
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from sympy import Matrix, QQ, GF
from sympy.polys.matrices import DomainMatrix


ROOT=Path(__file__).resolve().parent


def audit(record):
    n=record['n']; edges={tuple(e) for e in record['edges']}
    paths=[t for t in combinations(range(n),3)
           if (t[0],t[1]) in edges and (t[1],t[2]) in edges
           and (t[0],t[2]) not in edges]
    kind=record['kind']; field=record['field']
    prime=None if field=='Q' else int(field.split('_')[1])
    coefficients={tuple(item['path']):Fraction(item['coefficient'])
                  for item in record['support']}
    assert set(coefficients)<=set(paths)
    assert sum(coefficients.values())==1 if prime is None else sum(coefficients.values())%prime==1
    images=(list(range(n)) if kind=='triple_vertices' else sorted(edges))
    image_index={x:i for i,x in enumerate(images)}
    marginals=[[Fraction(0) for _ in images]
               for _ in range(3 if kind=='triple_vertices' else 2)]
    columns=[]
    for path in paths:
        maps=list(path) if kind=='triple_vertices' else [path[:2],path[1:]]
        for i,img in enumerate(maps):
            marginals[i][image_index[img]]+=coefficients.get(path,0)
        column=[]
        for i in range(1,len(maps)):
            column.extend(int(x==maps[i])-int(x==maps[0]) for x in images)
        columns.append(column)
    for marginal in marginals[1:]:
        diff=[x-y for x,y in zip(marginal,marginals[0])]
        assert all(x==0 for x in diff) if prime is None else all(x%prime==0 for x in diff)
    D=Matrix.hstack(*[Matrix(c) for c in columns])
    augmented=D.col_join(Matrix([[1]*len(paths)]))
    ranks={}
    for label,domain in [('Q',QQ),('F_2',GF(2)),('F_3',GF(3))]:
        ranks[label]=[DomainMatrix.from_Matrix(m).convert_to(domain).rank()
                      for m in [D,augmented]]
    if 'rank_D' in record:
        assert ranks[field]==[record['rank_D'],record['rank_D_augmented']]
    print(json.dumps({'kind':kind,'field':field,'n':n,'edges':sorted(edges),
        'all_paths':paths,'nonzero_coefficients':record['support'],
        'marginals':[[str(x) for x in row] for row in marginals],
        'ranks_D_Daug':ranks,'certificate_verified':True}))


for filename in ['finite_ordered_graphs_results.json','finite_ordered_graphs_random7.json']:
    for record in json.loads((ROOT/filename).read_text())['first_certificates'].values():
        audit(record)

# Hand-constructed theta: two paths in the graph of edges with lengths 4,3.
theta={'n':7,'edges':[(0,1),(1,2),(2,3),(3,5),(5,6),(1,4),(4,5)],
    'kind':'pair_edges','field':'Q','support':[
        {'path':p,'coefficient':str(c)} for p,c in [
            ((0,1,2),1),((1,2,3),1),((2,3,5),1),((3,5,6),1),
            ((0,1,4),-1),((1,4,5),-1),((4,5,6),-1)]]}
audit(theta)
theta['kind']='triple_vertices'
audit(theta)
print('All independent coefficient, image, and exact rank checks passed.')
