#!/usr/bin/env python3
"""Independent full-basis checks for the once-suspended eleven-cell table.

The existing free Dyer--Lashof/Serre enumerator computes all operations;
the hand table is then compared with it. This certifies the mod-two
bases, first Bockstein ranks, seven cycle Sq2 values, and the
quadratic-summand ranks and Sq4 values used in D.2.33. Integral
cell slides, geometric attaching maps, Toda compositions and ordinary
realization are proved in the manuscript, not inferred by this script.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json

with redirect_stdout(StringIO()):
    import D2_Qsource_primary as q

def mon(*letters):
    return tuple(sorted(letters))

def unit(u=0, v=0, w=0, t=0):
    return q.units[(u,v,w,t)]

A,B,C,D,E,F,X,G,H = (unit(1),unit(v=1),unit(2),unit(w=1),
                       unit(1,1),unit(3),unit(v=2),unit(2,1),unit(1,w=1))
I,J,L = unit(4),unit(1,2),unit(v=1,w=1)
m,n,o,t = unit(3,1),unit(2,w=1),unit(v=3),unit(t=1)
R = f'Q4[{A}]'
Q = lambda s,x: f'Q{s}[{x}]'

b10 = {
    'AR':mon(A,R), 'Q6B':mon(Q(6,B)), 'Q7A':mon(Q(7,A)),
    'A2B':mon(A,A,B), 'AF':mon(A,F), 'AX':mon(A,X),
    'BD':mon(B,D), 'BE':mon(B,E), 'C2':mon(C,C),
    'm':mon(m), 'n':mon(n), 'o':mon(o), 't':mon(t),
}
b11 = {
    'BR':mon(B,R), 'AQ5A':mon(A,Q(5,A)), 'Q6C':mon(Q(6,C)),
    'Q7B':mon(Q(7,B)), 'Q8A':mon(Q(8,A)), 'A2C':mon(A,A,C),
    'AG':mon(A,G), 'AH':mon(A,H), 'AB2':mon(A,B,B),
    'CD':mon(C,D), 'CE':mon(C,E), 'BF':mon(B,F), 'BX':mon(B,X),
    'u5':mon(unit(5)), 'u2v2':mon(unit(2,2)),
    'uvw':mon(unit(1,1,1)), 'w2':mon(unit(w=2)),
}
assert set(b10.values()) == set(q.basis(10))
assert set(b11.values()) == set(q.basis(11))

cycles = {
    'K1':{b10['AR'],b10['A2B']}, 'K2':{b10['C2']},
    'K3':{b10['Q7A']}, 'K4':{b10['AF']},
    'K5':{b10['m'],b10['n']}, 'K6':{b10['t']},
    'K7':{b10['AX'],b10['BD'],b10['BE']},
}
expected10 = {
    'AR':{mon(A,A,A)}, 'A2B':{mon(A,A,A)},
    'Q6B':{mon(Q(5,B))}, 'AX':{mon(A,D),mon(A,E)},
    'BD':{mon(A,D)}, 'BE':{mon(A,E)}, 'o':{mon(J),mon(L)},
}
expected11 = {'BR':'K1','Q6C':'K2','Q8A':'K3','AG':'K4',
              'BF':'K4','BX':'K7','u2v2':'K5','w2':'K6'}
for name,z in b10.items():
    assert set(q.sq(1,z)) == expected10.get(name,set()), ('beta10',name)
for name,z in b11.items():
    expected = cycles[expected11[name]] if name in expected11 else set()
    assert set(q.sq(1,z)) == expected, ('beta11',name)

def apply(operation, poly):
    return q.xor(*(q.sq(operation,z) for z in poly))

sq2 = {}
for name,cycle in cycles.items():
    assert not apply(1,cycle), ('not beta cycle',name)
    sq2[name] = apply(2,cycle)
    expected = ({mon(G),mon(H)} if name=='K5' else
                {mon(A,C),mon(B,B)} if name=='K7' else set())
    assert sq2[name] == expected, ('cycle Sq2',name,sq2[name],expected)

rank10 = len(q.span_basis(q.encode(q.sq(1,z),q.basis(9)) for z in b10.values()))
rank11 = len(q.span_basis(q.encode(q.sq(1,z),q.basis(10)) for z in b11.values()))
cycle_rank = len(q.span_basis(q.encode(z,q.basis(10)) for z in cycles.values()))
assert (rank10,rank11,cycle_rank)==(5,7,7)

# The Snaith weight-two summand relevant to D.2.33. Through these
# degrees every non-unit Dyer generator is a single operation, so
# it has weight two; a product has the sum of its factor weights.
def weight(z):
    return sum(2 if 'q' in q.gens[g] else 1 for g in z)

quadratic_bases = {
    degree:tuple(z for z in q.basis(degree) if weight(z)==2)
    for degree in range(8,12)
}
quadratic_dims = {degree:len(ba) for degree,ba in quadratic_bases.items()}
assert quadratic_dims == {8:3,9:5,10:7,11:9}
quadratic_ranks = {}
for degree in (9,10,11):
    quadratic_ranks[degree] = len(q.span_basis(
        q.encode(q.sq(1,z),quadratic_bases[degree-1])
        for z in quadratic_bases[degree]))
assert quadratic_ranks == {9:2,10:3,11:4}
quadratic_cycles = [cycles[name] for name in ('K2','K3','K4','K7')]
assert len(q.span_basis(q.encode(z,quadratic_bases[10])
                       for z in quadratic_cycles)) == 4
assert apply(4,cycles['K2']) == {mon(A,A)}
assert not apply(4,cycles['K7'])

def readable(poly):
    return [list(z) for z in sorted(poly)]

result = {
    'status':'PASS', 'scope':__doc__.strip(),
    'basis_dimensions':{'degree10':len(b10),'degree11':len(b11)},
    'Bockstein_ranks':{'degree10_to9':rank10,'degree11_to10':rank11},
    'cycle_rank':cycle_rank,
    'quadratic_dimensions':quadratic_dims,
    'quadratic_Bockstein_ranks':quadratic_ranks,
    'D33_fourth_square_checks':{'Sq4_C2':'A2','Sq4_K7':'0'},
    'beta10':{k:readable(q.sq(1,z)) for k,z in b10.items()},
    'beta11':{k:readable(q.sq(1,z)) for k,z in b11.items()},
    'cycles':{k:readable(z) for k,z in cycles.items()},
    'cycle_Sq2':{k:readable(z) for k,z in sq2.items()},
}
dest=Path(__file__).parent/'outputs'/'D2_once_eleven_certificate.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','basis_dimensions':result['basis_dimensions'],
                  'Bockstein_ranks':result['Bockstein_ranks'],
                  'cycle_rank':cycle_rank,'output':str(dest)}))
