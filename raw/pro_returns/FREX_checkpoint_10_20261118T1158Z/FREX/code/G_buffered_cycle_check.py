#!/usr/bin/env python3
"""Exact finite buffered-DF cycle; no global lift is asserted.
Eight two-letter words telescope in the ambient free group. Four
independent letters complete the three four-generator point maps.
"""
import json
from pathlib import Path
from sympy import Matrix

names = ['p','q','r','s','t','u','v','w','a_c','b_c','c_b','d_b']
letters = {name:i+1 for i,name in enumerate(names)}
def word(*ns): return tuple(letters[n] for n in ns)
def inv(w): return tuple(-a for a in reversed(w))
def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a: out.pop()
        else: out.append(a)
    return tuple(out)
def mul(*ws): return red(sum(ws,()))
W={
'a_b':word('p','q'),'b_b':word('r','q'),
'b_a':word('r','s'),'a_a':word('t','s'),
'c_c':word('t','u'),'d_c':word('v','u'),
'd_a':word('v','w'),'c_a':word('p','w'),
'a_c':word('a_c'),'b_c':word('b_c'),
'c_b':word('c_b'),'d_b':word('d_b')}
u={x:mul(W['a_'+x],inv(W['b_'+x])) for x in 'abc'}
v={x:mul(W['c_'+x],inv(W['d_'+x])) for x in 'abc'}
assert mul(u['b'],inv(u['a']),v['c'],inv(v['a']))==()
assert u['b']==word('p')+inv(word('r'))
assert u['a']==word('t')+inv(word('r'))
assert v['c']==word('t')+inv(word('v'))
assert v['a']==word('p')+inv(word('v'))
# Explicit basis reconstruction of the core subgroup from seven words.
A=W['a_b']; B=W['b_b']; E=mul(inv(B),W['b_a'])
C=mul(W['a_a'],inv(E)); F=mul(inv(C),W['c_c'])
D=mul(W['d_c'],inv(F)); J=mul(inv(D),W['d_a'])
assert [A,B,C,D,E,F,J]==[
word('p','q'),word('r','q'),word('t','q'),word('v','q'),
mul(inv(word('q')),word('s')),mul(inv(word('q')),word('u')),
mul(inv(word('q')),word('w'))]
assert mul(A,J)==W['c_a']
# These seven basis elements together with q give an explicit basis of F8.
q=word('q')
recovered=[mul(A,inv(q)),q,mul(B,inv(q)),mul(q,E),
           mul(C,inv(q)),mul(q,F),mul(D,inv(q)),mul(q,J)]
assert recovered==[word(n) for n in names[:8]]
ws=list(W.values()); keys=list(W)
for i,a in enumerate(ws):
 for j,b in enumerate(ws):
  if i!=j:
   assert not (len(a)<=len(b) and b[:len(a)]==a)
   assert not (len(a)<=len(b) and b[-len(a):]==a)
M=Matrix([[w.count(i+1) for w in ws] for i in range(len(names))])
cols=list(M.rref()[1]); rows=list(M[:,cols].T.rref()[1])
minor=M.extract(rows,cols).det()
assert len(cols)==11 and abs(minor)==1
kernel=M.nullspace();assert len(kernel)==1
expected={k:0 for k in keys}
for k,c in [('a_b',1),('b_b',-1),('b_a',1),('a_a',-1),
            ('c_c',1),('d_c',-1),('d_a',1),('c_a',-1)]:expected[k]=c
kv=Matrix([expected[k] for k in keys]);assert M*kv==Matrix.zeros(12,1)
# Every point image is a four-word code: in fact all twelve words are bifix.
for x in 'abc':assert M[:,[keys.index(k+'_'+x) for k in 'abcd']].rank()==4
out={'scope':'finite V,W buffered cycle only; global template excluded in accompanying note',
     'word_order':keys,'words':{k:[names[a-1] for a in w] for k,w in W.items()},
     'DF_group_relator_reduces_to_identity':True,'all_twelve_words_bifix':True,
     'point_map_ranks':[4,4,4],'point_count_rank':M.rank(),
     'primitive_relation':expected,'unit_minor_rows':rows,'unit_minor_columns':cols,
     'unit_minor_determinant':int(minor),'core_subgroup_rank':7,
     'core_basis_plus_q_reconstructs_ambient_F8':True,
     'global_realization_asserted':False}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
