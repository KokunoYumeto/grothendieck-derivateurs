# The restricted-square target and the actual mixed-fiber cancellation

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Research note following D.2.29.

**Status.** The canonical nonextension is proved in D.2.29. The
incoming Bockstein calculation below is a direct integral E2-chain
calculation. The mixed-fiber comparison in Sections 3--4 was
independently audited and passed by root and the axioms agent.
These calculations do not establish or exclude an arbitrary
fourth-suspension extension agreeing only on the unit.

## 1. The ambient outgoing second Bockstein cancels

Continue the notation

    T=Omega²Sigma²B, B=K(F2,2), k={a,b}, u5=xi1(a),
    E=T<5>=Omega²Z', U=Omega²E=Omega⁴Z'.

Here beta b=a, beta k=0, and beta2[k]=[u5], the last equality
being the previously proved Moore-four block in D.2.18.
CLM Chapter III Lemma 3.10, printed p.232, gives

    beta2[xi1(k)]=[{k,u5}].

This is ZERO on the second Bockstein page, because

    beta {b,{a,k}}={a,{a,k}}={xi1(a),k}={u5,k}.

The second equality is the restricted-Lie identity from CLM
Chapter III Theorem 1.3. The right side is a first-Bockstein
boundary, not a surviving secondary obstruction. There is no
contradiction with D.2.29: xi1(k) itself is not a *first*
Bockstein boundary.

## 2. An incoming second Bockstein and an integral order-four lift

In fact xi1(k) is an incoming second-Bockstein target. Put

    y=xi1(b), degree7;    e=beta y=b²+k, degree6.

Choose integral chains y,e with dy=2e. This is always possible:
take an integral lift of the mod-two cycle y and define e=dy/2.
Then de=0 and its reduction represents beta[y].

Let h(x,z) be the degree-one operation obtained from the ordered
little-two-cubes path joining the two multiplication orders. With
a consistent orientation its chain equation, for the present
even e and odd y, is

    d h(e,y)=ye-ey-2h(e,e),       d(y²)=2ey-2ye.

The signs are just the tensor differential and the endpoint
identity for the commutativity path. Therefore

    d(y²+2h(e,y))=-4h(e,e).

The chain h(e,e) is an integral cycle. Its mod-two class is the
top operation xi1(e), since the two endpoints agree on e tensor e.
Top additivity and Cartan give

    xi1(e)=xi1(b²+k)=xi1(k),

because xi1(b²)=0 and {b²,k}=0. Thus

    beta2[(xi1 b)²]=[xi1 k] !=0.

Equivalently h(e,e) is an integral lift of xi1(k) of order
dividing four. It cannot have order at most two: a chain bounding
twice that cycle would make xi1(k) a first-Bockstein boundary,
contrary to the complete Hall-basis argument of D.2.29. Hence
the integral lift has exact order four.

This argument uses only the one-dimensional ordered little-cubes
chain and its symmetry action. It does not import an E-infinity
square-Bockstein formula into an E2 target. The primary chain
convention and top-operation construction are the ones used in
the proof of CLM Chapter III Lemma 3.10, and the top additivity,
Cartan, and restricted identities are Chapter III Theorems 1.2--1.4.

For a separate numerical check, `code/EH5_braid_moore.py` constructs
the integral braid Salvetti complex with the signed tensor Moore
module. With the inverse-action convention its differential
squares to zero. It reproduces H5=Z/4 for the arity-two bottom
Moore block and gives H13=Z/4, H12=(Z/2)^4 for the arity-four
block. Its direct-model applicability is not needed for the
proof above; the output is retained as a research certificate,
not as a substitute for the explicit chain argument.

## 3. The exact internal cancellation in the connected cover

Vanishing of the ambient bracket in Bockstein homology does not
by itself imply vanishing in E, because H12E->H12T has not been
shown injective. The following universal construction resolves
that issue without a higher-degree Tor computation.

Let

    M=M(Z/2,2),       N=M(Z/4,5),
    V=Omega²Sigma²(M wedge N),
    P=fib(Sigma²(M wedge N) -> Sigma²M times Sigma²N),
    K=Omega²P=fib(V -> C2M times C2N).

The bottom cells of Sigma²M and Sigma²N have dimensions four
and seven. The product relative to the wedge therefore has no
relative cell below dimension eleven. Its homotopy fiber P is
nine-connected, and K is seven-connected.

The map V->C2M times C2N has a space section obtained by
multiplying the two looped wedge inclusions. Since this is a
map of group-like loop spaces, multiplication with the section
gives a homotopy equivalence

    K times C2M times C2N -> V.

One can check this directly on homotopy groups using the split
fiber exact sequence; all spaces are connected. In particular
H*K->H*V is injective, compatibly with the coalgebra and all
Bocksteins. Primitives in a tensor product of connected
coalgebras are the sums of primitives of its factors.

Use a,b for the two M labels, and x5,d6 for the N bottom and top
labels. All four labels are primitive; beta b=a and beta d6=0.
Inside H13V set

    z={b,{a,d6}}.

It is primitive and maps to zero in both pure factors. Hence it
is the image of a unique primitive z_K in H13K. The same applies
to {xi1(a),d6} in degree twelve. The exact free-E2 identities give

    beta z={a,{a,d6}}={xi1(a),d6},

and injectivity of H*K->H*V proves this identity already in K.

Now use the actual maps

    m:M->B->T,       mu:N->T

from the bottom Moore inclusion and D.2.17. The latter has
bottom alphaBar and top homology k. By the free double-loop
adjunction they induce an E2 map V->T, the double loop of a map
Sigma²(M wedge N)->Y. Its restriction to P lifts to Z', because
P is nine-connected and Z' is the six-connected cover of Y.
Consequently K->T lifts to E by an actual DOUBLE-LOOP map,
denoted ell:K->E.

It remains to identify the right-hand side internally, rather
than only after mapping into T. The bottom Hopf-invariant-one
map nu4:S7->S4, followed by the bottom inclusion into Sigma²M,
has a double adjunct S5->C2M whose Hurewicz image is xi1(a).
Under V->T this is precisely the chosen alphaBar of D.2.17.
Its mixed E2 Browder construction with N gives an actual map

    Sigma(S5 smash N) -> K.

Both projections to the pure factors are canonically null,
so it indeed factors through the homotopy fiber. After ell,
it agrees with the internal Browder map of the lifted sphere
u5:S5->E and the lifted Moore map mu:N->E. This follows either
from the double-loop construction just given or from uniqueness
of lifts from the ten-connected source Sigma(S5 smash N).
Thus ell_* sends {xi1(a),d6} EXACTLY to {u5,D6} in H12E,
where D6=k is the cover's Moore-top class. We have proved

    beta ell_*(z_K)={u5,D6} in H12E.

No injectivity statement about H12E->H12T has been used.

## 4. The cancellation also holds before two homology suspensions

The same universal fiber controls the possible suspension-kernel
term in U. Since K is seven-connected, Omega²K is five-connected.
Homology suspension is an isomorphism below the first product
degree, so

    sigma²:H_i(Omega²K;F2)->H_(i+2)(K;F2)

is an isomorphism for i<=11. More explicitly, the first products
in Omega²K have degree twelve and those in Omega K have degree
fourteen. Thus z_K and its degree-twelve Bockstein have unique
desuspensions z'_11 and b'_10, satisfying beta z'=b'.

Write N=Sigma²N0 with N0=M(Z/4,3). The double adjunct of the
mixed Browder map of Section 3 has domain

    Sigma^(-2) Sigma(S5 smash N)
       =Sigma³(S3 smash N0).

After composition with Omega²ell:Omega²K->U, it is precisely
the generalized E4 Browder map of the adjoint bottom sphere
u3:S3->U and adjoint Moore map N0->U. Both fourfold deloops
are the same generalized Whitehead product in Z'; this checks
the maps, not merely their homology suspensions. Therefore

    (Omega²ell)_*(b'_10)=lambda3(u3,q4),

where q4 is the top H4U class with double suspension D6. We
obtain the exact internal identity

    beta (Omega²ell)_*(z'_11)=lambda3(u3,q4) in H10U.

Consequently the suggested second Bockstein
beta2[xi3(q4)]=[lambda3(q4,u3)] also vanishes on its page.
There is no omitted suspension-kernel qualification in this
conclusion; the high connectivity of K and the actual
double-adjunction comparison supply it.

## 5. Remaining scope

The actual Hopf-invariant-one composite through rho gives a
spherical target class xi1(r), whose outer-square coefficients
on (xi1(k),xi1(f)) are (1,1). This can change the individually
tested xi1(k) coefficient in a relative top-cell choice. The
canonical value has coefficients (1,0); a full extension must
have both zero because neither outer generator is a first
Bockstein boundary. Whether the sum of these coefficients is
rigid under all allowed relative changes has not been proved.
The cancellations above show that the proposed outgoing
second-Bockstein detector does not establish that rigidity,
either in T, in E, or in U.

Primary sources used here are already in the manuscript:
CLM1976 Chapter III Theorems1.2--1.4 and Lemma3.10; Arkowitz1962
Definitions2.2--2.3 and Theorem2.4 for the generalized
Whitehead/Browder adjunction. No new numerical homotopy-group
claim is imported from the exploratory Moore-space searches.
