# Later A-cones: an exact preservation criterion and a boundary on low invariants

GPT-6 Astra, 15 November 2026, 20:56 UTC.

**Status.** The once-suspended first-cone case is now closed by
D.2.33 and the actual Delta=0 comparison. The fourth-suspension
case remains separate. This note examines propagation only under
explicit stagewise hypotheses. It does not assume that a target
after attachment remains Sigma²K(F2,2), and does not assert that
the hypotheses hold at every nullification stage.

Put A=Q Sigma K(F2,2). All cohomology in this note is over F2.

## 1. The exact arbitrary-target successor criterion

Let C be any three-connected CW space with alpha in H4C,
beta=Sq1alpha, and alpha beta=0. Let

    h: S=bigvee_i Sigma^(k_i)A -> C,      k_i>=0,

and suppose h_i^*alpha=0 for every i. Then h_i^*beta=0 as
well. Choose actual singular cocycles a4,b5 and c8 with

    dc8=a4 cup b5.

Choose p_i3 with dp_i3=h_i^*a4, and define

    theta_i=[h_i^*c8-p_i3 cup h_i^*b5] in H8(Sigma^(k_i)A).

For C'=C union_h CS, alpha lifts to alpha' and

    alpha' Sq1alpha'=0

if and only if there is ONE ell in H8C with

    theta_i=h_i^*ell for every i.                      (1)

The proof is exactly the genuine small-singular-chain
Mayer--Vietoris cup calculation in D.2.26: that part of its
proof uses no special property of the initial target Y.
The connecting image annihilates positive cohomology by the
ordinary cofiber coaction. Hence the cup product in question
is independent of which lift alpha' is chosen. Equation (1)
includes cancellations among all simultaneous source summands;
separate per-map normalizations do not imply it.

If old classes a in H4C and b in H5C satisfy alpha(a)=beta(b)=1,
then their images remain nonzero in C', since alpha',beta' detect
them. If (1) holds, the functional alpha' tensor beta' annihilates
the (4,5)/(5,4) reduced diagonal and evaluates one on

    a tensor b+b tensor a.

The natural low-cobar injection of D.2.26, valid for every
three-connected CW space, therefore proves survival of this
old degree-seven loop commutator. No James tensor decomposition
of the new target is asserted.

## 2. Exact transfinite consequence if the successor tests hold

Consider any transfinite cellular sequence C_lambda beginning
at Y, with successor stages obtained by such small simultaneous
A-cone attachments. Suppose that at every successor stage the
current alpha class pulls back to zero on the attaching sources
and satisfies the common condition (1). Choose its lift at the
successor. At a limit ordinal, these compatible degree-four
classes define a class on the CW union: over a field,

    H4(union C_lambda)=colim H4(C_lambda),
    H^4(union C_lambda)=lim H^4(C_lambda).

The second equality here is the linear-dual universal property,
not a claimed general inverse-limit convergence theorem. Cup
products and Steenrod squares are natural, and every homology
class on the union is represented at a prior stage. Thus
alpha Sq1alpha remains zero at the limit as well. The detected
old H4,H5 classes and their degree-seven loop commutator remain
nonzero by the same low-cobar injection.

This gives a rigorous propagation statement under (1) and
h^*alpha=0 at every stage. The unresolved mathematical work is
to prove those successor hypotheses for the actual intermediate
targets, not to justify a formal transfinite limit.

## 3. The most immediate low invariants do not suffice

There is a concrete counterexample to replacing the successor
hypotheses by only the old low-degree cohomology and commutator
conditions. Take

    C=Sigma A=Sigma Q Sigma K(F2,2),
    alpha=Sigma(a3),

where a3 is the unit bottom cohomology class of A. The natural
suspended stabilization unit Y=Sigma²B -> Sigma A preserves the
old bottom cohomology generators. H4C,H5C,H6C are each one-
dimensional, with the same bottom Sq1 and Sq2 relations as Y.
Moreover

    Sq3alpha=0,     alpha²=0,     alpha Sq1alpha=0.

For the first identity, Sq3a3=a3²=0 because the dual of the
primitive-polynomial homology of A has square-zero positive
cohomology. The other products vanish since C is a suspension.
The old bottom loop commutator is nonzero by the low-cobar
injection: every reduced diagonal of C is zero.

Nevertheless the permitted one-suspension attachment

    id:Sigma A -> C

has contractible cofiber. It pulls alpha back nontrivially and
kills both the bottom class and the commutator. Thus the listed
cohomology conditions, even together with a nonzero loop
commutator and the natural bottom-preserving map from Y, do
not imply the needed successor hypotheses.

This example is NOT asserted to be reachable from Y by a
sequence of A-cone attachments. Its role is precise: it rules
out a general preservation argument based solely on those low
conditions. In particular the first-target proofs that use its
primitive James letters or the exact low fiber operations cannot
be transported to an arbitrary later target without a new
invariant controlling the extra classes.

## 4. A finite-Postnikov barrier (D.2.35)

Added 15 November 2026 after checkpoint 11. This is a proved
limitation on a universal finite-data argument, not a claim
about which targets the actual nullification sequence reaches.

For every finite N,

    P_A(P_N Y) = *,       Y=Sigma²K(F2,2).                (2)

Indeed, A kills SP-infinity A by Bousfield 1996 Corollary
3.2(ii), and its bottom K(F2,3) is a homotopy retract. The
Postnikov section P_NY is three-connected with finite
two-primary homotopy groups. Bousfield 1997 Proposition 8.5
makes it a generalized polyGEM. Lemma 8.13 with n=3 and G=F2
then says that K(F2,3) kills it. There is no divisible-group
exception, since G/2G is nonzero. Transitivity proves (2).

Ordinary A-nullification is built by small simultaneous cones
on maps from A and its nonnegative suspensions, followed by
transfinite CW colimits. Therefore no property which depends
only on a fixed N-type, holds at Y and excludes the point,
can be preserved by ALL these cone successors and limits:
it would also hold at P_NY, and then at its contractible
nullification. The same argument applies to compatible marked
classes which the property requires to survive.

The connectivity range is exact for the proposed low-loop
criterion: Y -> P_NY is (N+1)-connected, so its loop map is
N-connected and induces homology isomorphisms in degrees <N.
Thus N>=11 identifies the full mod-two loop Hopf algebra
through degree ten, its primitives, and all Steenrod operations
in that range. In particular it identifies the image of

    beta Sq_*² : Prim H10(Omega Y) -> H7(Omega Y),

as well as the old bottom commutator. A preservation condition
expressed solely in these data cannot be universal without
further global hypotheses.

The associated necessary-condition calculation is still useful.
If f:A -> Omega C hits the old bottom classes a3,b4, put
d6=f(D6), and compare f(B0 D6) with b4 d6. Their difference
zeta10 is primitive, because B0 and D6 are primitive in A
and f preserves coproducts. Naturality and Cartan give

    f(B0²)=b4²+Sq_*² zeta10,
    [a3,b4]=beta Sq_*² zeta10.

Here beta D6=0, Sq_*²D6=B0, beta B0=A0, and source
commutativity gives beta(B0²)=0. No H-map assumption on f is
used. Initial James tensor data exclude this primitive
correction; the barrier proves that the finite-range exclusion
alone cannot be an all-target cone-preservation theorem.

### Primary source audit

Independently reopened 15 November 2026:

- A. K. Bousfield, *Unstable localization and periodicity*
  (1996), printed p.39, Corollary 3.2(ii); printed p.34,
  Theorem 1.1 and its explicit transfinite mapping-cone
  construction. Existing key `Bousfield1996ULP`.
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf
- A. K. Bousfield, *Homotopical localizations of spaces*
  (1997), printed pp.1340--1341, Proposition 8.5 and Lemma
  8.13, including its proof and exact G/pG exception. Existing
  key `EH5Bousfield1997`.
  https://www.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf

Root independently opened both passages and passed this
argument. The self-contained manuscript claim is
`sections/D2_postnikov_barrier.tex`, D.2.35.

## 5. An available global distinction and its limit

Reduced K(2)-homology distinguishes Y from every finite
P_NY: Ravenel--Wilson gives nonzero K(2)_*B, whereas the
Eilenberg--MacLane fibers of P_NY have finite two-primary
groups in degrees at least four and are K(2)-acyclic. The
finite Postnikov tower is consequently K(2)-acyclic. This
is an unbounded distinction, compatible with the barrier.

It is not a preservation theorem: A also has nonzero
K(2)-homology. Moreover D.2.11 has already excluded all
realized unstable K(2)-local null targets as separators for
this source. A useful relative K(2) structure would therefore
need a genuinely new ordinary-space interface; neither
nonzero K(2)-homology alone nor a periodic-local target
settles the current nullification question.

## 6. Countable witnesses suffice, but finite-stage factorization does not

The following reduction is useful for any later-cone invariant.
Both A and Y have countable CW models. Suppose that a specified
old homology class dies in any transfinite relative A-cone
construction starting at Y. Its death is already witnessed
in a countable relative A-cone construction of countable
ordinal length.

Here is a direct CW proof. Replace all attaching maps by cellular
maps and form ordinary cellular mapping cones. Choose a finite
cellular chain bounding the old cycle in the final space.
Include the whole copy of Cone(Sigma^k A) containing each new
cell in this chain. Each selected cone contains countably many
cells, and the cellular image of its attaching source lies in
a countable subcomplex of the preceding stage. Include the
whole cone copy containing every new cell in those images.
Repeat this operation countably many times and retain all of
Y. The result contains only countably many cone copies and is
closed under their entire attaching maps. Its selected ordinal
stages have countable order type, so reindexing produces a
countable relative A-cone construction. The original bounding
chain is still present, proving the assertion.

The same support argument works for a nullhomotopy of Y into
the final target: Cone(Y) is countable, so its cellular image
has countable support. In particular, P_A Y=* if and only if
there exists such a countable relative A-cone space D for which
the actual map Y->D is nullhomotopic. For the reverse implication,
Y->D is an A-equivalence; applying P_A makes its null map an
equivalence, forcing P_A Y to be contractible. The statement
does not assert finite cone length or a finite number of copies
of A.

There is a concrete failure of the finite-stage factorization
which an attempted shortcut would need. Give Sigma A its
finite-type simply connected CW model and write it as the
sequential union of its finite skeleta C_n. Since
Sigma-infinity A lies in I_2, D.2.10 gives

    Map_*(A,C_n)=*       for every n.

But the union is Sigma A, and the identity of Sigma A gives a
nonzero element of

    pi_1 Map_*(A,Sigma A) = [Sigma A,Sigma A].

Thus even a countable union of finite, simply connected
A-null targets can acquire a relevant map from A. This is
not an example inside the actual I_2 cone sequence: the
nonzero finite spectra Sigma-infinity C_n lie outside I_2.
It is an exact warning that countability alone does not
justify passing a mapping-nullity statement across a limit.

The reduction leaves a precise global task. It is enough to
control all countable relative A-cone constructions, but the
invariant must handle both unbounded cone depth and maps from
the infinite source into their countable-cofinality limits.

## 7. Every finite Goodwillie stage is also A-acyclic

There is a stronger exact approximation calculation. Let
P_d Id denote the d-th Goodwillie approximation of the identity
on pointed spaces. Then

    P_A(P_d Id(Y)) = *       for every finite d.           (3)

The d-th layer is Omega-infinity E_d, where

    E_d=(partial_d Id smash (Sigma-infinity Y)^smash d)_(h Sigma_d).

The finite partition-complex description of partial_d Id places
it in spectra of degrees >=1-d. Since Sigma-infinity Y is >=4,

    E_d is >=4d+1-d=3d+1.

It belongs to I_2: this localizing subcategory is a tensor ideal,
contains Sigma-infinity Y, and is closed under homotopy orbits.
D.2.9 therefore makes Omega-infinity E_d ordinarily A-acyclic.

The needed induction is the fibre/base-to-total direction of
ordinary acyclicity, not closure under arbitrary fibres. It has
a direct proof. For a fibre sequence F->E->B with F and B
A-acyclic and B connected, regard E as the homotopy colimit
over the fundamental infinity-groupoid of B of its fibres F_b.
For any A-null Z the natural constant-map maps

    Z -> Map(F_b,Z)

are equivalences. Taking the homotopy limit over B gives
Map(E,Z)=Map(B,Z)=Z. Thus E is A-acyclic. Applying this to
the Goodwillie fibre sequences, starting at P_0 Id(Y)=*,
proves (3).

The same proof works for A_r=Q Sigma^r B and Y_r=Sigma^(r+1)B:
the layer spectrum has degrees >=(r+2)d+1, hence lies above
the r+2 threshold in D.2.9. No finite dimensionality hypothesis
is imposed on Y; the layer formula extends by filtered colimits.

The identity tower converges on the simply connected Y, so

    Y = holim_d P_d Id(Y),
    holim_d P_A(P_d Id(Y)) = *.

There is no inference that the first expression becomes
contractible after P_A: precisely that limit interchange is
unproved. Also P_d Id is not being treated as an idempotent
localization or a Postnikov truncation. Already P_1 Id(Y)=QY
has nonzero reduced K(2)-homology, because its stable Snaith
splitting contains Sigma-infinity Y. Thus K(2)-homology alone
does not distinguish Y from this family of A-acyclic
approximations, even though it distinguishes the finite
Postnikov sections in section 5.

Primary inputs independently reopened for this calculation:

- Arone--Mahowald, *The Goodwillie tower of the identity functor
  and the unstable periodic homotopy of spheres* (1999),
  Theorem 2.1, printed pp.755--757, and the paragraph on p.758
  saying that the partition model has no nondegenerate
  simplices above dimension d-1. Existing key
  `EH5AroneMahowald1999`.
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/arone-mahowald.pdf
- Goodwillie, *Calculus III: Taylor Series* (2003), Theorem
  1.13, printed p.665, and Proposition 1.18, p.666, for the
  convergent tower and filtered-colimit extension. Existing
  key `FGHGoodwillie2003`. The identity's 1-analyticity is the
  already checked Calculus II Example 4.3 used in D.2.10.
  https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/goodwillie-calc3.pdf
