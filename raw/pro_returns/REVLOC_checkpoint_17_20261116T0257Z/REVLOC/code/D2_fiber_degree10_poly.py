#!/usr/bin/env python3
"""Independent polynomial part of the proposed degree-ten fibre table.

No Browder, top-operation, integral exponent, or homotopy assertion is
certified here. The Serre algebra and Cartan implementation are reused
from the separately audited degree-at-most-nine calculation.
"""
import json
from pathlib import Path
import D2_fiber_poly_check as a

a.LABEL.update({(5,0,0,0):'p', (2,2,0,0):'q',
                (1,1,1,0):'r', (0,0,2,0):'s'})
a.EXP.update({v:k for k,v in a.LABEL.items()})
a.GEN_SQ[3][1] = {(0,0,2,0)}
p=a.pol
A=a.CLASSES['A4']; z=a.CLASSES['z5']; f=a.CLASSES['p3']
W=a.CLASSES['W8']; C=a.CLASSES['C8']; M=a.CLASSES['M8']
Z0=a.xor(a.CLASSES['Pm9'], a.CLASSES['ZA9'], a.CLASSES['Pn9'])
classes={
 'DA':p('aabb'),
 'FA':a.mul(A,f),
 'Z2':a.mul(z,z),
 'D2':p('dd'),
 'Q10':p('q','cx','aj','aax','abe','aabb','bg','bbc'),
 'Pp':p('p','ai','cf','aaf','acc','aaac','aaaaa'),
 'Pr':p('r','al','bh','ed'),
}
expected={
 'DA':(set(),W,set()), 'FA':(set(),W,set()),
 'Z2':(set(),W,set()), 'D2':(set(),set(),p('bb')),
 'Q10':(Z0,a.xor(M,C,W),f),
 'Pp':(set(),W,f), 'Pr':(set(),set(),set()),
}
def tensor(x,y):
 return {(l,r) for l in x for r in y}
coproduct={
 'DA':a.xor(tensor(A,p('bb')),tensor(p('bb'),A)),
 'FA':a.xor(tensor(A,f),tensor(f,A)),
 'Q10':tensor(z,z),
}
rows=[]
for name,poly in classes.items():
 rd=a.reduced_delta(poly)
 assert rd==coproduct.get(name,set()),(name,'diagonal',rd)
 ops=tuple(a.sq(k,poly) for k in (1,2,4))
 assert ops==expected[name],(name,ops,expected[name])
 rows.append({'class':name,'polynomial':a.show(poly),
              'reduced_coproduct':a.show_tensor(rd),
              'Sq1':a.show(ops[0]),'Sq2':a.show(ops[1]),
              'Sq4':a.show(ops[2])})
dest=Path(__file__).parent/'outputs'/'D2_fiber_degree10_poly.json'
result={'status':'PASS','degree':10,'classes':rows,
 'scope':'Seven polynomial classes, full coproducts and 21 primary operation values only.'}
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','classes':len(rows),'operation_values':21,
                  'output':str(dest)}))
