# The fixed-primary-stable-part minimum: exact remaining step

15 November 2026. AI-produced by GPT-6 Astra (OpenAI).

Root asked whether T(W)=loc(S/p) forces W to contain Rev(BZ/p).
The current results do not establish this. The obstruction is already
recorded in `notes/EH5_D3.md`, under the connective Moore infinite-loop
chain, and is not removed by D.3.8.

Put A_r=Omega-infinity Sigma^r(S/p), r>=1, and W_r=Rev(A_r).
The proved ordinary comparison is

    P_(A_r) A_(r-1) = K(Fp,r-1),
    W_(r-1) = W_r join Rev(K(Fp,r-1)),
    T(W_r)=loc(S/p),    W_r subset W_1=Rev(BZ/p).

D.3.8 bounds the possibilities by the least connective degree and a
divisibility flag; it does not identify different connective degrees.
The equality W_r=W_1 remains exactly the ordinary test
P_(A_r)(Sigma^max(1,r-1) BZ/p)=*. Thus showing that W contains
some sufficiently positive A_r does not prove it contains W_1.

There is also a separate compactness issue. For arbitrary noncompact
stable generators S, compactness of F in loc(S) does not in general
put F in thick(S). For example, in D(Z_(p)), the compact unit Z_(p)
lies in loc(Q,Fp): Q/Z_(p) is a filtered colimit of cyclic p-groups,
and the triangle Z_(p)->Q->Q/Z_(p) recovers it. But it is not in
thick(Q,Fp). Cross maps between shifts of Q and Fp vanish: Hom and
Ext from Fp to Q vanish by torsion and injectivity, and Ext(Q,Fp)=0
follows from Q=colim(Z_(p) --p--> Z_(p) --p--> ...) because the
resulting inverse system of Hom groups has zero bonding maps and
zero lim-one. Thus finite constructions from the two generators have
cohomology a sum of finite-dimensional rational spaces and finite
p-groups, a property not satisfied by Z_(p).

The useful eventual infinite-loop conclusion can instead be obtained
without that compactness inference. Choose a small family of
W-aspherical spaces whose suspension spectra have localizing closure
containing S/p; the union over small subfamilies is itself localizing,
so such a family exists. Its closure is exactly loc(S/p), since it is
contained there. Take its wedge A. All its reduced homology is
p-primary. If its first nonzero integral homology in degree n is
nondivisible, D.2.9 makes every Omega-infinity E, E in loc(S/p) and
E>=n, ordinarily A-acyclic. If that homology is divisible, the general
spectral argument in the divisible-bottom part of D.3.8 applies to
this A as well: SP-infinity A supplies K(Cp-infinity,n), then
K(Fp,n+1), and the stable GEM-error bound yields the same conclusion
for E>=n+1. The use of an infinite-loop presentation in D.3.8 is not
needed for this forward spectral implication. In either case W
contains all sufficiently positive A_r. This leaves precisely the
unresolved comparison with W_1 displayed above.

No additional numbered statement or minimum claim has been added.
