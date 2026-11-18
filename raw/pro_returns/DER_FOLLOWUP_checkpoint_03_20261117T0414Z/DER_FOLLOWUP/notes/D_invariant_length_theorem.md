# Invariant positive lengths and the C_delta monoid comparison

GPT-6 Astra, 17 November 2026. The full proof was independently
audited by root, paths_monoids, and localization. The last audit
requested the explicit universal-abelian-group terminology in
Step 7, now incorporated. This is a conditional theorem, not a settlement of the
unrestricted C_delta question. Its hypotheses include a strictly
positive invariant real length; such a length does not always exist.

## Statement

Let A=C_delta, U its rich limit, G=Aut(U), and I the directed poset
of actual nonempty finite closed substructures of U. Let M:A→FreeMon
be any diagram and S=colim_I M. Suppose that S admits a homomorphism

    ℓ:S→(R_{≥0},+)

such that ℓ(s)=0 iff s=1, and ℓ(gs)=ℓ(s) for every g∈G.

Then q_M is a weak equivalence. Moreover

    T_i^A(M_ab)=0  for every i>0.

The second assertion is a separate consequence of the proof; it
does not follow merely from passage of q_M.

## Inputs already proved and audited

1. D.8 (`D:free-limit-criterion`): product-compatible saturation
   M→T_S, with T_S(F)=S^{G_F}, preserves B int_A M and ordinary
   monoid colimits. The proof applies to arbitrary monoid diagrams.
2. D.9 (`D:finite-free-injective-reduction`): a filtered colimit of
   free monoids is cancellative, conical, equidivisible, and every
   finite subset lies in a finite-rank free submonoid. The finite
   free hull is canonical; in particular finite free submonoids
   form a directed poset under inclusion.
3. R17: for finite closed E,F (also allowing the empty structure),

       <G_E,G_F> = G_{E∩F}.

   Finite closed substructures are rigid because their order is
   linear. G is strongly homogeneous, and all finite intersections
   of closed substructures are closed. A is total, and BA is
   contractible. The group G_empty is G itself.
4. D.6: for a diagram of categories with a fixed object set C and
   identity object maps, the groupoid completion of its Grothendieck
   construction agrees with that of its categorical colimit when
   BA is simply connected. The proof contracts the A-transports at
   each c. It uses no freeness of the category values.

## Step 1: product stabilizers fix all factors

If g(ab)=ab, compare the factorizations (ga)(gb)=ab in the
equidivisible monoid S. Either ga=a t or a=(ga)t for some t∈S.
Length invariance gives ℓ(t)=0, so t=1 and ga=a. Cancellation
then gives gb=b. Therefore

    G_{ab}=G_a∩G_b.

In particular every fixed monoid S_F=S^{G_F} is factor-closed in S:
ab∈S_F implies a,b∈S_F. This is the only use of the real length.
The same conclusion would suffice as a hypothesis on its own.

## Step 2: finite charts and their fixed submonoids

Let J be the directed poset of finite-rank free submonoids H⊂S.
For each finite closed F, put H_F=H∩S_F. Since S_F is factor-closed,
H_F is the free submonoid on the subset

    atoms(H)_F = atoms(H)∩S_F.

Indeed, every letter of any H-factorization of an S_F-word also
lies in S_F. Conversely any word on the displayed subset belongs
to S_F. The union of the H_F over J is all S_F. Thus S_F is a
filtered colimit of free monoids, though it need not itself be free.

If H⊂H′, a generator of H_F decomposes in H′ using only generators
of H′_F, again by factor-closedness. All constructions below are
therefore natural on J. No claim that H→H′ induces an injection on
free-group completions or on graph-chain modules is made.

## Step 3: an intrinsic graph-chain module

Fix any monoid C and a G-invariant monoid map ρ:S→C. G acts trivially
on C. For a submonoid L⊂S let D(L) be the left translation category
with objects C and arrows

    (m,c):c→ρ(m)c,       m∈L.

If L is free, D(L) is the free category on edges indexed by
C×atoms(L). Its graph chain complex is

    Z[C×atoms(L)] --∂--> Z[C],
    ∂(c,b)=[ρ(b)c]−[c].

A positive substitution L→L′ sends an edge to the corresponding
oriented path. On chains this is the sum of that path's edges.
These chain maps compose exactly; uniqueness of word substitution
proves this, independently of any choice of metric parametrization.

Define

    E = colim_{H∈J} Z[C×atoms(H)],
    E_F = colim_{H∈J} Z[C×atoms(H_F)].

There is a compatible boundary E_F→Z[C]. At each chart the map
Z[C×atoms(H_F)]→Z[C×atoms(H)] is an inclusion on a subset of a
basis. Filtered colimits of abelian groups preserve monomorphisms,
so E_F→E is injective. This remains true even though individual
transition maps E_H→E_H′ can have kernels.

These modules are intrinsic: the generator associated with a word
s and an object c can be denoted D(s,c); after passing to a common
chart it is the sum of the edges along s. It satisfies

    D(st,c)=D(t,c)+D(s,ρ(t)c).

G acts by D(s,c)↦D(gs,c), and each such generator has open
stabilizer. Elements of G_F fix E_F pointwise. Strong homogeneity
therefore defines a strict A-diagram F↦E_F by extending embeddings
to G, independently of the extensions.

## Step 4: distributivity of finite supports

For any finite closed F,E_1,...,E_r, including empty ones,

    E_F ∩ (E_{E_1}+...+E_{E_r})
      = E_{F∩E_1}+...+E_{F∩E_r}.                 (1)

At a single chart H, the relevant modules are generated by subsets
of the same edge basis. An atom belongs both to S_F and to S_E iff
it is fixed by <G_F,G_E>=G_{F∩E}, hence iff it belongs to S_{F∩E}.
The elementary intersection/distributivity identity for basis
submodules proves (1) at H. Filtered exactness transports finite
sums and intersections to the colimit: equivalently take kernels
of the maps defining intersections inside the common ambient E.
The monomorphisms established above identify these with genuine
subgroups of E. This proves (1).

For n≥0, filter the A-diagram E_F by

    E_F^{≤n}= sum_{closed B⊂F, |B|≤n} E_B.

There are only finitely many B in each F. The filtration exhausts
E_F, since it equals E_F for n≥|F|. Put

    V_B=E_B / sum_{closed D⊊B} E_D.

Formula (1) gives a natural isomorphism

    E_F^{≤n}/E_F^{≤n−1}
      ≅ ⊕_{closed B⊂F, |B|=n} V_B.              (2)

Indeed the intersection of the contribution from B with all the
other contributions is generated by proper closed intersections
B∩B′, and is therefore exactly its lower-support part after
quotienting. This is also valid for n=0, where the only support is
the empty structure and the preceding term is zero.

The G action identifies V_B along isomorphisms of supports. Its
pointwise stabilizer G_B acts trivially. There is no additional
finite automorphism action, since every finite ordered support is
rigid. Thus for n>0, (2), as an A-module, is a direct sum over
isomorphism types of n-point closed structures B of

    Z[A(B,−)] ⊗_Z V_B.

For n=0 it is the constant module V_empty.

All these modules have vanishing higher derived colimits. For a
representable summand, the bar complex is the chain complex of
the element category of A(B,−), with coefficients V_B. That
category has the initial object id_B, providing a chain contraction
for arbitrary abelian V_B, not merely for free coefficients. The
constant summand is acyclic because BA is contractible. Induction
on n through the short exact sequences of the filtration, followed
by its filtered union, therefore gives

    T_i^A(E_−)=0  for all i>0.                   (3)

The final passage is valid because the bar complex computing
derived colimits consists of direct sums and filtered colimits of
abelian groups are exact.

## Step 5: translation-category homology

Since D(S_F)=colim_H D(H_F), its nerve is the filtered colimit of
their nerves. The graph models of D(H_F) show

    H_q(BD(S_F);Z)=0  for q≥2,

and give the natural exact sequence

    0→H_1(BD(S_F))→E_F→Z[C]→Z[π_0D(S_F)]→0.   (4)

Both the constant module Z[C] and the final free Set-action module
in (4) have vanishing higher derived colimits, by contractibility
of BA and totality of A. Split (4) into two short exact sequences
at the image of its boundary. Using (3) and the two long exact
derived-colimit sequences gives

    T_i^A(H_1(BD(S_−)))=0  for i>0.              (5)

The Grothendieck homology spectral sequence for the A-diagram
D(S_F) therefore has no surviving terms of total degree ≥2:
its q≥2 rows vanish, its q=0 row is acyclic in positive degrees,
and its q=1 row is acyclic in positive degrees by (5). Consequently

    H_j(B int_A D(S_F);Z)=0  for j≥2.           (6)

## Step 6: contractible comparison commas

Take C=colim_A^Mon T_S and let ρ:S→C be its invariant universal
map. The ordinary categorical colimit of D(S_F) is C//C, the
regular translation category. A presentation verifies this:
generators are pairs (c,s) with s a stage element; transition and
multiplication relations are exactly the presentation of the
monoid colimit, in every context c. The resulting arrows are
precisely c→mc for m∈C. This category has initial object 1.

The fixed-object transport argument of D.6, using simply connected
BA, makes B int_A D(S_F) simply connected and connected. Together
with (6), Hurewicz and Whitehead imply that it is contractible.
This Grothendieck construction is the sole comma of

    int_A T_S → B C.

Theorem A proves q_{T_S} is a weak equivalence. D.8 transports the
result back to q_M.

## Step 7: higher derived colimits of the abelianizations

Repeat the edge-module construction with C the one-element monoid.
Then E_F=(S_F^gp)_ab, the universal abelian GROUP of S_F, since
the boundary is zero and group completion followed by abelianization
commutes with this colimit of free charts. Equation
(3) gives T_i^A((S_−^gp)_ab)=0 for i>0. Each BS_F has no homology
above degree one, as shown in Step 5. Its homotopy-colimit spectral
sequence therefore has H_j=0 for j≥2. D.8 identifies this homotopy
colimit with B int_A M. Finally D.1 gives

    T_i^A(M_ab)=H_{i+1}(B int_A M;Z)=0,  i>0.

This completes both assertions of the conditional theorem.

## Consequence for the based positive-matrix stabilization

The based diagram H in `D_positive_stabilization.md` has the
natural strictly positive real functional

    L_X = λ^(−N_X) ell B_X.

Indeed L_Y H(f)=L_X, and every basis value is strictly positive.
If those specified positive integer matrices admitted strict word
substitutions in their specified bases, the resulting free-monoid
diagram would have a natural positive length, hence an invariant
positive length on its filtered limit S. Step 7 would force
T_1(H)=0, contradicting the proved T_1(H)=Z.

Therefore that particular based positive-matrix diagram has no
strict FreeMon lift. This does not rule out a free-monoid diagram
whose abstract abelianization is isomorphic to H after basis changes
on which this functional ceases to be positive. It also does not
settle arbitrary FreeMon diagrams over C_delta.

## Additional corollary: a positive length on the colimit is enough

**Proved and independently audited by root and paths_monoids.** The
monoid colimit C is the coinvariant monoid S_G. A compatible cocone
on the stage monoids is the same as a homomorphism on their filtered
limit S that is invariant under G: each closed embedding extends to
G, and each restricted automorphism is an arrow of A. This verifies
the coinvariant universal property.

The map S→S_G has trivial identity fibre. Indeed S is conical.
The coinvariant congruence is generated by pairs g(s)=s, and a
single contextual relation has the form

    x g(s) y  ↔  x s y.

One side equals 1 if and only if x=s=y=1, by conicality, and then
the other side equals 1 as well. Every chain of these elementary
relations therefore preserves the singleton class {1}. It also
follows that C is conical: if [s][t]=1, then st=1 in S, forcing
s=t=1.

Consequently any strictly positive additive real length on C pulls
back to a G-invariant strictly positive length on S. All conclusions
of the theorem then apply. In particular:

> Every FreeMon diagram over C_delta whose monoid colimit is a free
> monoid passes its comparison, and has T_i(M_ab)=0 for all i>0.

More generally the same holds whenever the monoid colimit has a
strictly positive additive grading into the nonnegative reals.

This rules out the suggested suffix-chart counterexample route
with abelianization Q and free monoid colimit FreeMon(u,t). No
coherent global diagram having all those properties can exist,
even though numerous finite charts exist. It does not rule out
a failing comparison whose colimit has no strictly positive
additive real length. Root requested this corollary be added to
the paper after the current checkpoint/QA, rather than editing
the source during compilation.

## Search and provenance record

The proof above was derived in this research session from the
already audited R17 stabilizer/all-action reduction and D.8–D.9.
No external theorem asserting this conditional comparison was
found or imported, and no priority claim is made. Exact searches
performed after deriving the proof, to check nearby literature:

- `"free monoids" "invariant length"`
- `"equidivisible" "length function" automorphism`
- `"free monoid" "derived colimits" length`

These searches returned related length-function/freeness and
homotopy-of-monoids material, but no matching C_delta statement.
No new search hit was used as a proof dependency. The previously
opened Lawson–Wallis paper is already recorded separately with
its integer-length limitation. The free-hull inputs and exact
primary theorem numbers are in `D_free_hull_independent_audit.md`.
The paper version is `sections/D_invariant_length.tex`, claim D.10.
