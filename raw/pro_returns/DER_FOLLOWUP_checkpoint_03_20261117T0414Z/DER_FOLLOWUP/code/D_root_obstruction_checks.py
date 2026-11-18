#!/usr/bin/env python3
"""Check the finite graph behind the failed first-return-loop replacement.

The proof that there are infinitely many free generators is the exact normal
form a c^n b in the attempt note. This bounded enumeration only checks the given
finite graph and every word in the stated range; it is not an infinite proof.
"""
from pathlib import Path
from itertools import product
import json
edges={'a':('x','v'),'b':('v','x'),'c':('v','v')}
paths=[('x','')];loops=[];first=[]
for length in range(1,15):
    paths=[(t,w+a) for s,w in paths for a,(u,t) in edges.items() if s==u]
    for t,w in paths:
        if t!='x':continue
        loops.append(w)
        pieces=[];start=0;vertex='x'
        for i,a in enumerate(w):
            assert edges[a][0]==vertex;vertex=edges[a][1]
            if vertex=='x':pieces.append(w[start:i+1]);start=i+1
        assert start==len(w)
        assert all(p[0]=='a' and p[-1]=='b' and set(p[1:-1])<=set('c') for p in pieces)
        if len(pieces)==1:first.append(w)
assert first==['a'+'c'*n+'b' for n in range(13)]
rank=len(edges)-2+1
assert rank==2
def reduce_word(w):
    stack=[]
    for c in w:
        if stack and stack[-1]==c.swapcase():stack.pop()
        else:stack.append(c)
    return ''.join(stack)
def inv(w):return ''.join(c.swapcase() for c in w[::-1])
positive=[''.join(w) for n in range(1,6) for w in product('ab',repeat=n)]
conjugate_checks=0;positive_conjugates=0
for a,b in product(positive,repeat=2):
    c=reduce_word(a+b+a+inv(b)+inv(a))
    is_positive=c.islower()
    commute=a+b==b+a
    assert is_positive==commute
    if is_positive:assert c==a;positive_conjugates+=1
    conjugate_checks+=1
assert reduce_word('abaBA')=='abaBA'
assert reduce_word('abAB')!=''
code_words={'x':'aa','y':'ab','z':'ba','w':'bb'}
code_kernel='xZ wY'.replace(' ','')
assert reduce_word(code_kernel)==code_kernel
code_kernel_image=''.join(code_words[c] if c.islower() else inv(code_words[c.lower()]) for c in code_kernel)
assert reduce_word(code_kernel_image)==''
# A fixed block length gives unique parsing, independently of the group check.
code_products={}
for n in range(5):
    for word in product(code_words,repeat=n):
        image=''.join(code_words[c] for c in word)
        assert image not in code_products
        code_products[image]=word
out={'graph_vertices':['x','v'],'graph_edges':edges,
 'underlying_graph_first_betti_number':rank,'maximum_path_length':14,
 'loops_checked':len(loops),'first_return_generators_checked':len(first),
 'exact_first_return_normal_form':'a c^n b, n >= 0',
 'unique_loop_factorization_at_visits_to_x':True,
 'scope':'The loop monoid has infinitely many free generators; its inclusion does not recover the rank-two graph fundamental group.',
 'injective_monoid_noninjective_group_example':{
 'generator_images':code_words,'nontrivial_reduced_kernel_word':code_kernel,
 'image_before_reduction':code_kernel_image,'image_after_reduction':'',
 'distinct_positive_code_products_checked':len(code_products),
 'general_injectivity_proof':'Every image word has a unique parsing into consecutive length-two blocks.'},
 'positive_conjugation_obstruction':{'a_b_lengths_at_most':5,
 'pairs_checked':conjugate_checks,'positive_conjugates':positive_conjugates,
 'all_positive_conjugates_force_commutation':True,
 'free_group_marked_words':['a','b','abaBA'],
 'general_proof':'For c=(ab)a(ab)^-1, positive words have |c|=|a|. In (ab)a=c(ab), initial prefixes give c=a, hence ba=ab. The finite enumeration is not used as the proof.'}}
(Path(__file__).resolve().parent/'outputs'/'D_root_obstruction_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
