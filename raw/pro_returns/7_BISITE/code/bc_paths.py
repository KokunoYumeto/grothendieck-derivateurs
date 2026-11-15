"""Exact monoid and endpoint-naturality checks for BISITE B.21."""
from itertools import product
from pathlib import Path
import json
R=['1']+[(i,j) for i in [0,1] for j in [0,1]]
def mul(a,b):
    if a=='1':return b
    if b=='1':return a
    return (a[0],b[1])
triples=0
for a,b,c in product(R,repeat=3):
    assert mul(mul(a,b),c)==mul(a,mul(b,c));triples+=1
e=(0,0)
assert all(mul(e,r)!='1' and mul(r,e)!='1' for r in R)
checks=0
for incoming in [False,True]:
    for m in range(-5,6):
        if m%2 != int(incoming):continue
        def component(i):return '1' if i<=m else e
        for i in range(-8,9,2):
            for j in [i-1,i+1]:
                edge=e if set([i,j])==set([m,m+1]) else '1'
                if incoming:assert component(i)==mul(component(j),edge)
                else:assert mul(edge,component(i))==component(j)
                checks+=1
out={'monoid_elements':R,'associativity_equations':triples,
     'nonunit_left_right_ideal_verified':True,'delayed_lift_naturality_equations':checks}
Path(__file__).with_suffix('.out.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
