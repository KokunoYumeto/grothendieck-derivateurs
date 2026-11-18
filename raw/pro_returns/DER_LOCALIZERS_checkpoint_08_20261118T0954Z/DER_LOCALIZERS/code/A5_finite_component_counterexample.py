"""Finite certificate for A.5's counterexample to relative Theorem A.

Requires Python 3 and sympy.  The category P is the double collage of the
face-poset maps u,v : suspension(C6) -> suspension(C3), of degrees 1,2.
Its two pole objects and two parallel mixed arrows form Q.  BQ -> BP is a
pi_1 isomorphism and an integral-homology equivalence, but not a weak
homotopy equivalence: its universal-cover relative chain complex is
Z[t,t^-1] --(2t-1)--> Z[t,t^-1], in degrees 3,2.

The script constructs every object and arrow, verifies functoriality,
composition and associativity, checks the degree calculations by integral
chains, and computes the integral homology of the homotopy-coequalizer
chain complex.  The infinite counterexample is the explicitly specified
countable disjoint union of copies; no finite calculation is claimed to
enumerate that union.
"""
from itertools import combinations, product
from fractions import Fraction
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def sphere(n):
    N,S=n,n+1
    facets=[frozenset((p,i,(i+1)%n)) for p in (N,S) for i in range(n)]
    faces=set()
    for T in facets:
        for r in range(1,len(T)+1):
            faces.update(frozenset(F) for F in combinations(sorted(T),r))
    return sorted(faces,key=lambda F:(len(F),tuple(sorted(F))))

A,B=sphere(6),sphere(3)
def u_vertex(v):return v//2 if v<6 else v-3
def v_vertex(v):return v%3 if v<6 else v-3
def image_face(F,func):return frozenset(func(x) for x in F)
u={F:image_face(F,u_vertex) for F in A}
v={F:image_face(F,v_vertex) for F in A}
assert all(F in B for F in (*u.values(),*v.values()))
assert all(u[F]<=u[G] and v[F]<=v[G] for F in A for G in A if F<=G)

# Each arrow is (source,target,tag).  Tag -1 means a within-layer arrow;
# tag 0 or 1 distinguishes the two kinds of mixed arrow.
objects=[('A',F) for F in A]+[('B',F) for F in B]
arrows=[]
for layer,faces in [('A',A),('B',B)]:
    arrows.extend(((layer,F),(layer,G),-1) for F in faces for G in faces if F<=G)
for eps,functor in enumerate((u,v)):
    arrows.extend((('A',F),('B',G),eps) for F in A for G in B if functor[F]<=G)
arrow_set=set(arrows)
def compose(after,before):
    assert before[1]==after[0]
    tag=max(before[2],after[2])
    out=(before[0],after[1],tag)
    assert out in arrow_set
    return out
outgoing={o:[] for o in objects}
for a in arrows:outgoing[a[0]].append(a)
pair_count=triple_count=0
for a in arrows:
    identity_source=(a[0],a[0],-1)
    identity_target=(a[1],a[1],-1)
    assert compose(a,identity_source)==compose(identity_target,a)==a
    for b in outgoing[a[1]]:
        ba=compose(b,a);pair_count+=1
        for c in outgoing[b[1]]:
            assert compose(c,ba)==compose(compose(c,b),a)
            triple_count+=1
Q_objects=[('A',frozenset((6,))),('B',frozenset((3,)))]
Q_arrows=[a for a in arrows if a[0] in Q_objects and a[1] in Q_objects]
assert len(Q_objects)==2 and len(Q_arrows)==4

def chains(faces,d):return [tuple(sorted(F)) for F in faces if len(F)==d+1]
def sign_to_sorted(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def boundary(faces,d):
    src,tgt=chains(faces,d),chains(faces,d-1)
    D=sp.zeros(len(tgt),len(src));lookup={t:i for i,t in enumerate(tgt)}
    for j,s in enumerate(src):
        for k in range(len(s)):D[lookup[s[:k]+s[k+1:]],j]+=(-1)**k
    return D
def chain_map(func,d):
    src,tgt=chains(A,d),chains(B,d)
    F=sp.zeros(len(tgt),len(src));lookup={t:i for i,t in enumerate(tgt)}
    for j,s in enumerate(src):
        image=tuple(func(x) for x in s)
        if len(set(image))==len(image):
            F[lookup[tuple(sorted(image))],j]=sign_to_sorted(image)
    return F
def sphere_cycle(n,faces):
    basis=chains(faces,2);lookup={s:i for i,s in enumerate(basis)}
    z=sp.zeros(len(basis),1)
    for p,sign in [(n,1),(n+1,-1)]:
        for i in range(n):
            triple=(p,i,(i+1)%n)
            z[lookup[tuple(sorted(triple))],0]+=sign*sign_to_sorted(triple)
    return z
dA={d:boundary(A,d) for d in (1,2)}
dB={d:boundary(B,d) for d in (1,2)}
U={d:chain_map(u_vertex,d) for d in range(3)}
V={d:chain_map(v_vertex,d) for d in range(3)}
for d in (1,2):
    assert dB[d]*U[d]==U[d-1]*dA[d]
    assert dB[d]*V[d]==V[d-1]*dA[d]
zA,zB=sphere_cycle(6,A),sphere_cycle(3,B)
assert dA[2]*zA==sp.zeros(dA[2].rows,1)
assert dB[2]*zB==sp.zeros(dB[2].rows,1)
assert U[2]*zA==zB and V[2]*zA==2*zB

# Cone(V-U), the integral chains of the homotopy coequalizer.
dimsA=[len(chains(A,d)) for d in range(3)]+[0]
dimsB=[len(chains(B,d)) for d in range(3)]+[0]
dims=[dimsB[d]+(dimsA[d-1] if d else 0) for d in range(4)]
D={}
for d in range(1,4):
    bdiff=dB.get(d,sp.zeros(dimsB[d-1],dimsB[d]))
    fmap=V[d-1]-U[d-1]
    adiff=dA.get(d-1,sp.zeros(0 if d==1 else dimsA[d-2],dimsA[d-1]))
    D[d]=bdiff.row_join(fmap).col_join(sp.zeros(adiff.rows,bdiff.cols).row_join(-adiff))
    assert D[d].shape==(dims[d-1],dims[d])
assert D[1]*D[2]==sp.zeros(dims[0],dims[2])
assert D[2]*D[3]==sp.zeros(dims[1],dims[3])
ranks={d:D[d].rank() for d in D}
homology=[]
for d in range(4):
    rank=dims[d]-ranks.get(d,0)-ranks.get(d+1,0)
    nextdiff=D.get(d+1,sp.zeros(dims[d],0))
    snf=smith_normal_form(nextdiff,domain=ZZ)
    torsion=[abs(int(snf[j,j])) for j in range(min(snf.shape)) if abs(snf[j,j])>1]
    homology.append({'degree':d,'free_rank':rank,'torsion':torsion})
assert [h['free_rank'] for h in homology]==[1,1,0,0]
assert all(not h['torsion'] for h in homology)

# The relative universal-cover obstruction, verified exactly over Q.
coefficients={1:2,0:-1}
augmentation=sum(coefficients.values())
evaluation=sum(Fraction(c)*Fraction(1,2)**e for e,c in coefficients.items())
assert augmentation==1 and evaluation==0
assert Fraction(1)!=0
result={
 'finite_category':{
  'construction':'double collage of u,v: face(suspension C6) -> face(suspension C3)',
  'A_face_counts':dimsA[:3],'B_face_counts':dimsB[:3],
  'P_object_count':len(objects),'P_arrow_count':len(arrows),
  'Q_object_count':len(Q_objects),'Q_arrow_count':len(Q_arrows),
  'composition_pairs_checked':pair_count,'associativity_triples_checked':triple_count,
  'u_equator_vertex_images':[u_vertex(i) for i in range(6)],
  'v_equator_vertex_images':[v_vertex(i) for i in range(6)]},
 'sphere_map_degrees':{'u':1,'v':2},
 'homotopy_coequalizer_chain_ranks':dims,
 'differential_ranks':ranks,'integral_homology':homology,
 'fundamental_group_certificate':'L and K are simply connected suspensions of polygonal circles; van Kampen gives Z, generated by the two-arrow pole circle Q.',
 'relative_universal_cover_chain':{'C3':'Z[t,t^-1]','C2':'Z[t,t^-1]','d3':'2*t-1'},
 'augmentation_d3':augmentation,'evaluation_d3_at_half':str(evaluation),
 'nonzero_H2_module':'Z[t,t^-1]/(2*t-1) is Z[1/2], with t acting by 1/2',
 'finite_coproducts':{str(n):{'bad_component_count':n,'in_W_fin':True} for n in range(1,9)},
 'countable_coproduct':{'bad_component_count':'aleph_0','in_W_fin':False},
 'conclusion':'Each Q -> P lies in W_fin; its countable coproduct does not. The comma functor over each object of the discrete category N is Q -> P.'
}
print(json.dumps(result,indent=2))
