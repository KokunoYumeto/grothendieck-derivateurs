"""Independent exhaustive verification of the six-object B062 counterexample.

This program does not import the search or its rewriting engine. Axiom (a) is
certified by explicit relative functors and natural weak zigzags, not inferred
from a finite path-length calculation.
"""
from itertools import product
from pathlib import Path

log=[]
def say(x):log.append(str(x))
O=tuple(range(6))
covers={(0,1),(0,2),(1,3),(2,3),(1,4),(3,5),(4,5)}
rel=covers|{(x,x) for x in O}
while True:
    more={(a,c) for a,b in rel for bb,c in rel if bb==b}
    if more<=rel:break
    rel|=more
W={(x,x) for x in O}|{(1,3),(1,4),(2,3)}
say('Objects: '+repr(O))
say('Hasse covers: '+repr(sorted(covers)))
say('All arrows: '+repr(sorted(rel)))
say('W: '+repr(sorted(W)))
for a,b in sorted(rel):
    for bb,c in sorted(rel):
        if b==bb:say(f'Composition ({b},{c}) o ({a},{b}) = ({a},{c})')
for a,b in rel:
    for bb,c in rel:
        if b!=bb:continue
        assert (a,c) in rel
        assert sum(x in W for x in ((a,b),(b,c),(a,c)))!=2
        for cc,d in rel:
            if c==cc:assert (a,d) in rel
say('PASS: all identities, composition, associative triples, and two-out-of-three')

meet={}
for a,b in product(O,repeat=2):
    lows=[x for x in O if (x,a) in rel and (x,b) in rel]
    best=[x for x in lows if all((y,x) in rel for y in lows)]
    assert len(best)==1
    meet[a,b]=best[0]
say('Meet matrix, row and column order 0..5:')
for a in O:say([meet[a,b] for b in O])
say('PASS: every pair has its specified meet, hence all pullbacks exist')
assert all((0,x) in rel and (x,5) in rel for x in O)

expected={0:{0},1:{0,1},2:{0,2},3:{0,3},4:{0,1,4},5:{0,3,5}}
F={};slices={};universals={}
for s in O:
    S={x for x in O if (x,s) in rel};slices[s]=S
    Ws={u for u in W if u[1] in S}
    F[s]={x for x in S if all((meet[a,x],meet[b,x]) in W for a,b in Ws)}
    assert F[s]==expected[s]
    restricted={u for u in Ws if u[0] in F[s] and u[1] in F[s]}
    universals[s]={u for u in restricted if all((meet[u[0],t],meet[u[1],t]) in W for t in S)}
    assert universals[s]==restricted
    say(f'Base {s}: slice={sorted(S)}, intrinsic objects={sorted(F[s])}, W on them={sorted(restricted)}')
say('PASS: (b) at all six bases, by every possible strict pullback')

def functor(domain,target,assignment):
    assert set(assignment)==set(domain)
    assert set(assignment.values())<=set(target)
    assert all((assignment[a],assignment[b]) in rel for a,b in rel if a in domain and b in domain)
    assert all((assignment[a],assignment[b]) in W for a,b in W if a in domain and b in domain)
def natural_weak(domain,A,B):
    assert all((A[x],B[x]) in W for x in domain)
    # Naturality is equality of the unique arrows, and existence is checked.
    for a,b in rel:
        if a in domain and b in domain:
            assert (A[a],A[b]) in rel and (B[a],B[b]) in rel
            assert (A[a],B[b]) in rel

# For s=0,1,2,4 the full fibrant subcategory is the whole slice.
for s in (0,1,2,4):assert F[s]==slices[s]

# Base 3: a coaugmentation from the identity to the reflection.
S=slices[3];Id={x:x for x in S};R3={0:0,1:3,2:3,3:3}
functor(S,F[3],R3);natural_weak(S,Id,R3)
assert all(R3[x]==x for x in F[3])
say('Base 3 R='+repr(R3)+'; Id -> inclusion R has weak components')

# Base 5: weak natural zigzag Id <- T -> inclusion R.
Id={x:x for x in O};R={0:0,1:3,2:3,3:3,4:3,5:5}
T={0:0,1:1,2:2,3:3,4:1,5:5}
functor(O,F[5],R);functor(O,O,T)
natural_weak(O,T,Id);natural_weak(O,T,R)
assert all(R[x]==x and T[x]==x for x in F[5])
say('Base 5 R='+repr(R))
say('Base 5 T='+repr(T))
say('PASS: Id <- T -> inclusion R consists of natural weak transformations, and R inclusion = Id')
say('PASS: explicit relative inverse certificates prove (a) at every base')

# Strong saturation: W is the inverse image of identities under R.
assert all(((a,b) in W)==(R[a]==R[b]) for a,b in rel)
say('PASS: W = R^{-1}(identities); hence W is strongly saturated')

H={0,3,4,5}
assert F[5]<=H<=set(O)
WH={u for u in W if u[0] in H and u[1] in H}
assert WH=={(x,x) for x in H}
assert (3,4) not in rel and (4,3) not in rel
assert (1,3) in W and (1,4) in W and 1 not in H
say('Intermediate H objects='+repr(sorted(H)))
say('Intermediate H arrows='+repr(sorted(u for u in rel if u[0] in H and u[1] in H)))
say('Intermediate H W='+repr(sorted(WH)))
say('PASS: H localizes to itself and 4 is not isomorphic to any object of F[5]')
say('PASS: in the whole localization, 3 and 4 are isomorphic via 3 <- 1 -> 4')
say('CONCLUSION: a and b hold for every base; c fails at base 5')
out=Path(__file__).with_suffix('.out.txt')
out.write_text('\n'.join(log)+'\n')
print('\n'.join(x for x in log if x.startswith('PASS') or x.startswith('CONCLUSION')))
print('Complete certificate:',out)
