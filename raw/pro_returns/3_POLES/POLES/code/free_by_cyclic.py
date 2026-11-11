#!/usr/bin/env python3
"""Exact algebraic certificates for the free-by-cyclic homology-circle example."""
import json
from pathlib import Path
import sympy as s

def reduce(word):
    ans=[]
    for x in word:
        if ans and ans[-1] == -x:
            ans.pop()
        else:
            ans.append(x)
    return tuple(ans)

def inverse(word):
    return tuple(-x for x in reversed(word))

def substitute(word, mapping):
    ans=[]
    for x in word:
        ans.extend(mapping[x] if x > 0 else inverse(mapping[-x]))
    return reduce(ans)

phi={1:(2,),2:(-1,2)}
psi={1:(1,-2),2:(1,)}
for generator in [(1,),(2,)]:
    assert substitute(substitute(generator,phi),psi)==generator
    assert substitute(substitute(generator,psi),phi)==generator
M=s.Matrix([[0,-1],[1,1]])
assert (M-s.eye(2)).det()==1
assert reduce((1,2,-1,-2)) != ()
result={'phi':phi,'inverse_psi':psi,'both_composites_identity':True,
        'abelianization_matrix':[[int(x) for x in row] for row in M.tolist()],
        'det_M_minus_I':1, 'free_commutator_nontrivial':True,
        'proof_obligations_in_paper':'Graph mapping torus is K(G,1); Wang sequence computes homology; Nielsen-Schreier controls subgroups.'}
out=Path(__file__).with_name('free_by_cyclic_output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('PASS: automorphism, inverse, determinant, and noncommutativity certificates.')
