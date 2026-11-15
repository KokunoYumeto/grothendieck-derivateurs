# Primary Miller sources and ordinary nullification

Research note, 2026-11-15. This note records exact restrictions on the current
strict-interval search. It does not claim a separator.

Write A=B(Z/p). A primary space below means a connected space whose reduced
integral homology is p-primary torsion. For such a space X, the previously
proved finite-suspension criterion for the reversible minimum is

    X belongs to minRev(A)  if and only if  P_A(Sigma X) is contractible.

Ordinary A-nullity of X does not replace this criterion.

## The H-space strengthening

**Claim.** If X is a connected primary H-space, then

    P_A(Sigma X)=*  if and only if  P_A X=*.

Consequently a noncontractible primary H-space which is both A-null and
Miller (maps trivially to the finite sphere targets) would lie outside the
reversible minimum. The H-space hypothesis is essential to the proof; no
general-space assertion is made.

**Proof.** The reverse implication follows because the ordinary A-acyclic
class is closed under suspension. For the forward implication put Z=P_A X.
Nullification preserves finite products, so Z is a connected H-space and the
unit X -> Z is an H-map up to homotopy. Since Sigma X is A-acyclic and Z is
A-null, Map_*(X,Omega Z)=Map_*(Sigma X,Z) is contractible.

Bousfield1997 Lemma5.5 now says that Map_*(X,Z) is homotopically discrete
and that pi_1 Z acts trivially on [X,Z]. His Key Lemma5.3 therefore gives

    Map_*(SP^infinity X,Z) ~= Map_*(X,Z).

By Dold--Thom, SP^infinity X is a connected GEM with homotopy groups
Htilde_n(X;Z), all p-primary. Every K(G,n) for a p-primary abelian group G
and n>=1 is A-acyclic. The product of these Eilenberg--Mac Lane factors is
weakly equivalent to their weak product, because their connectivities tend
to infinity; the weak product is a filtered homotopy colimit of finite
products. Thus the whole GEM is A-acyclic. Since Z is A-null, the left
mapping space is contractible. In particular the unit X -> Z is null.
The localization equivalence Map_*(Z,Z) -> Map_*(X,Z) then makes the
identity of Z null, proving Z contractible. QED.

The argument permits arbitrary cardinality, arbitrary H-space multiplication,
and arbitrary cohomological size. It does not require associativity, a loop
space structure, finite type, or a Krull-filtration hypothesis. The only use
of multiplication is the product preservation of P_A and Bousfield's
Lemma5.5, which controls all components of the mapping space, not just its
base component.

**Opened primary source.** A. K. Bousfield, *Homotopical localizations of
spaces*, American Journal of Mathematics119 (1997), 1321--1354,
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bous1.pdf.
Key Lemma5.3 and Lemma5.5 were read directly, including their hypotheses.

## Connected loops of acyclic H-spaces

**Claim.** If Y is a connected ordinarily A-acyclic H-space, then the base
component Omega_0 Y is ordinarily A-acyclic. Thus every iterated connected
loop space Omega_0^r Y is ordinarily A-acyclic.

**Proof.** Y is primary: A is Z[1/p]-homology acyclic, and the nullification
unit is a Z[1/p]-homology equivalence. A connected H-space is nilpotent, so
the Serre-class theorem shows that its homotopy groups are p-primary; the
same holds for Omega_0 Y and its integral homology. Since A is connected,
nullification acts component by component on Omega Y. Bousfield1997
Theorem5.1 says that each component of P_A Omega Y is a GEM. In particular
N=P_A(Omega_0 Y) is a connected GEM. It is primary, since the nullification
unit preserves Z[1/p]-homology, and it is A-null by definition.

An A-null primary GEM must be contractible. Indeed, if G=pi_n N were a
nonzero p-primary group, it would have an element of order p. The GEM
retract K(G,n) would then satisfy

    pi_(n-1) Map_*(BZ/p,K(G,n)) = H^1(BZ/p;G) = G[p] != 0,

contradicting A-nullity (with pi_0 understood when n=1). Hence N=*.
The iteration follows since Omega_0 Y remains an H-space. QED.

This is not a statement about loops of an arbitrary acyclic space: the first
application requires that Y itself be an H-space. In particular the proof
cannot be applied to an arbitrary classifying space BG or an arbitrary
suspension merely because that space is A-acyclic. The precise opened
source is Bousfield1997 Theorem5.1; Theorem5.2 separately identifies
P_A Omega Y with Omega P_(Sigma A) Y and does not remove this restriction.

## Why ordinary nullity alone does not separate the reversible minimum

There is an explicit primary example. Apply Leary's metric Kan--Thurston
theorem to a simplicial model of K(F_p,2), obtaining an integral homology
equivalence

    t: BG -> K(F_p,2)

with G torsion-free. The construction is a locally CAT(0) cubical complex:
its universal cover is CAT(0) and contractible, and any finite group of
deck transformations would have a fixed point, so G has no nontrivial
finite subgroup. Leary's TheoremA, TheoremB.8 and TheoremB.11 cover the
possibly infinite-dimensional case.

BG is A-null, since every homomorphism Z/p -> G is trivial and pointed
mapping spaces between classifying spaces are homotopically discrete.
Its reduced homology is p-primary and nonzero. Moreover it maps trivially
to every simply connected finite target: simply connected targets are
integral-homology-local, as is proved by their principal Postnikov towers
from Eilenberg--Mac Lane spaces and closure under homotopy limits. Thus
the map t induces equivalences on these mapping spaces, and the source
K(F_p,2) has the Sullivan vanishing property. The same reasoning applies
to simply connected completed finite targets. If one includes nilpotent
finite targets in the definition of Miller space, G is perfect because
H_1(BG;Z)=0, so every homomorphism from G to the nilpotent fundamental
group of such a target is trivial; the maps lift to its simply connected
finite-dimensional universal cover and the same argument applies.

Nevertheless Sigma t is an equivalence: it is a homology equivalence
between simply connected spaces. Consequently

    Sigma BG ~= Sigma K(F_p,2),

which is A-acyclic. Therefore BG already belongs to minRev(A). This is an
explicit failure of the inference from nontrivial A-null primary Miller
source to strict reversible membership. It re-encodes the original
Eilenberg--Mac Lane source and does not solve the interval problem.

**Opened primary source.** Ian J. Leary, *A metric Kan--Thurston theorem*,
Journal of Topology6 (2013), 251--284,
https://arxiv.org/pdf/1009.1540.
TheoremA (local-coefficient homology equivalence), TheoremB.8
(infinite-dimensional CAT(0) criterion), and TheoremB.11
(finite-group fixed points) were checked in the original article.

## Exact limits of the H-space classification sources

Castellana--Crespo--Scherer, *Deconstructing Hopf spaces*, opened published
PDF https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CCSdeconstructingPublished.pdf:

* Theorem5.3 assumes T_V H^*(X;F_p) is of finite type for every elementary
  abelian p-group V. Under this assumption QH^*(X) in U_n is equivalent to
  Omega^(n+1)X being A-null.
* Theorem5.5, with the same finite-type hypotheses, gives a p-primary
  finite Postnikov fiber for X -> P_A X. It leaves an arbitrary A-null
  H-space as base and therefore does not prove that a Miller H-space is
  A-acyclic.
* Theorem7.2 requires the stronger hypothesis that H^*(X;F_p) is finitely
  generated as an algebra over the Steenrod algebra. It then makes
  P_A X mod-p finite. Theorem7.3 gives the corresponding finite Postnikov
  decomposition. Corollary5.6 retains loop structures for loop spaces.
* None of these statements classifies arbitrary primary Miller H-spaces.

The mod-p finite loop-space interface has another exact primary source:
Bauer--Pedersen, *The realizability of local loop spaces as manifolds*,
https://tilmanbauer.github.io/papers/the-realizability-of-local-loop-spaces-as-manifolds.pdf.
Corollary1.3 says every p-compact group is the p-completion of a compact
smooth parallelizable manifold. Lemma3.2 supplies a rational-mixing
construction with finitely generated, bounded Z_(p)-homology; for a simply
connected p-compact group its p-local mixing model is simply connected.
The general manifold statement does not explicitly assert a simply
connected or nilpotent manifold, so an application to our finite
simply connected target class must justify that interface. This source is
restricted to loop spaces; it has not been silently generalized to all
H-spaces.

### A complete finite-generation exclusion for simply connected loop spaces

**Claim.** Let X be a simply connected primary loop space. Suppose that
Map_*(X,K)=* for every simply connected finite CW complex K, and that
H^*(X;F_p) is finitely generated as an algebra over the Steenrod algebra.
Then P_A X=* (and therefore X belongs to the reversible minimum).

**Proof.** Put Z=P_A X. Nullification preserves simple connectivity.
CCS Theorem7.2 makes H^*(Z;F_p) finite-dimensional, while the loop-space
statement preceding Corollary5.6 makes Z a loop space. It remains primary,
because the A-nullification unit is a Z[1/p]-homology equivalence. The
p-completion Y=Z_p^ is therefore a simply connected p-compact group:
completion of this nilpotent loop space retains a loop-space structure,
and its mod-p homology is finite.

For clarity, the finite simply connected model needed here follows from
the proof of Bauer--Pedersen Lemma3.2, without assuming their manifold
model is nilpotent. Their construction first forms a rational mixing
pullback on classifying spaces, with rational model
BK=product_i K(Q,2d_i). Since Y is simply connected, no d_i=1 occurs;
the classifying-space pullback is 2-connected. Its loop space F is hence
simply connected and p-local. Lemma3.1 shows that H_*(F;Z_(p)) is bounded
and finitely generated, and the construction gives F_p^ ~= Y.

Here is the elementary finite-model step. Write R=Z_(p), and choose
N>=3 above the nonzero reduced R-homology of F. The relative Hurewicz
theorem permits the usual finite cellular approximation, in the
R-local simply connected homotopy category, giving a finite N-dimensional
simply connected CW complex C and an N-connected map C_(p) -> F.
Only finitely many cells in each dimension are needed, since the
relative homology modules are finitely generated over the noetherian
ring R. Attaching maps in localized homotopy groups can be represented
by ordinary attaching maps after multiplication by integers prime to p;
these integers are units in R, so this realizes each finite stage by an
ordinary finite CW complex.

Since H_N(F;R)=H_(N+1)(F;R)=0, the relative homology exact sequence and
relative Hurewicz give

    pi_(N+1)(F,C_(p)) ~= H_(N+1)(F,C_(p);R) ~= H_N(C;R).

The last module is finite free over R: C has dimension N, so its top
homology is a submodule of its finite free top cellular chain module.
Choose an R-basis, represent its relative homotopy classes by finitely
many (N+1)-cells, and attach them to C while extending the map to F.
Multiplying representatives by prime-to-p integers, if necessary,
retains a basis and gives ordinary integral attaching maps. The result
is a finite simply connected CW complex K. The boundary map from the
new (N+1)-cells onto H_N(C;R) is an isomorphism, so these cells kill
the last unwanted homology and create none in degree N+1. Thus
K -> F is an R-homology equivalence, and the simply connected localized
Whitehead theorem gives K_(p) ~= F. In particular Y ~= K_p^.

By the primary-source mapping-completion theorem (Miller1984 Theorem1.5),
Map_*(X,K_p^) ~= Map_*(X,K)=*. The target Y=K_p^ is A-null by Miller's
Sullivan theorem and completion. Hence the universal property of
P_A gives Map_*(Z,Y) ~= Map_*(X,Y)=*. In particular the completion unit
Z -> Y is null. But it is an isomorphism on mod-p homology, so the
reduced mod-p homology of Z vanishes. Since Z is primary, multiplication
by p being an isomorphism on every reduced integral homology group
forces all those groups to vanish. Finally Z is simply connected, so
the homological Whitehead theorem makes it contractible. QED.

The finite generation assumption is stronger than merely lying in a
finite Krull stage. The proof does not remove it. It also does not assert
that a general H-space is a loop space, or that passing to the universal
cover of an arbitrary Miller source preserves its Miller property.

**Audit status (14:54 UTC).** CCS Theorem7.2 and the loop-space statement
at Corollary5.6, Bauer--Pedersen Lemmas3.1--3.2 and their rational-mixing
proof, and Miller1984 Theorem1.5 were all read in primary sources.
Miller's source-mapping comparison has no finite-type or cardinality
restriction on the connected primary source; its nilpotent-target
hypothesis is satisfied by the finite simply connected K constructed
above. The finite-cell model argument is supplied here, rather than
claimed as part of Bauer--Pedersen's manifold corollary. An independent
adversarial review by the axioms/derivators agent passed the finite-cell
construction, denominator clearing, final top-boundary argument, and
localized Whitehead step at 14:56 UTC; no Wall obstruction remains in
this explicit construction. The standard identification of
nilpotent p-completion with mod-p homology localization, and its
preservation of simply connected loop-space structures, have not been
newly source-audited in this note. The latter also follows from product
preservation: the field Kunneth theorem makes X times Y -> L(X) times L(Y)
a mod-p equivalence, the product is local, and a product-preserving
localization retains the entire grouplike A-infinity structure. No
unrestricted finite-Krull or arbitrary-H-space extension is assumed.

The exact unresolved mathematical step in the broader source approach is
the existence or impossibility of a noncontractible primary BZ/p-null
Miller H-space outside this finite-generation range. The opened
classification theorems do not decide it. This note supplies no bound on
all reversible localizers with a fixed stable part and no strict
intermediate in the requested interval.

## Compact-Lie and compact-loop classifying sources

The rationalization-fiber candidate coming from BS^3, or more generally a
connected compact Lie group, does not give a separator. Castellana--Flores,
*Homotopy idempotent functors on classifying spaces*,
https://arxiv.org/pdf/1210.7772, Theorem4.10 computes P_A BG as
Z[1/p]-homological localization when G is connected. Proposition4.11 gives
the same conclusion for classifying spaces of p-local compact groups,
and Corollary4.12 for connected finite-loop classifying spaces. These
theorems were opened directly. The primary fibers of these nullification
units are A-acyclic, by the standard acyclic-fiber theorem for nullification.
This excludes those candidates; it gives no general statement about loops
or arbitrary inverse limits of A-acyclic spaces.

## The varying elementary-abelian James product also collapses

The proposed source X=product_(m>=1) Omega Sigma B(F_p^m) is ordinarily
A-acyclic. Indeed B(F_p^m)=A^m, and the actual finite-product suspension
splitting gives

    Sigma(A^m) ~= wedge_(empty!=S subset {1,...,m}) Sigma(A^(smash |S|)).

Apply Hilton--Milnor to this finite wedge, assigning each letter the weight
|S|. A basic word of total weight l gives exactly the factor

    Z_l = Omega Sigma(A^(smash l)).

For fixed m and l there are only finitely many letters and basic words of
total weight l. The factors' connectivities tend to infinity with l, so
the weak product in Hilton--Milnor agrees with the full product. Taking
the product over m and reordering gives

    X ~= product_(l>=1) Z_l^(kappa_l)

for suitable cardinal multiplicities kappa_l. Each Z_l has finite
p-primary homotopy groups in every fixed degree: Sigma(A^(smash l)) is
simply connected with finite-type p-primary homology, so the standard
Serre finiteness and Serre-class theorems apply. Each Z_l is ordinarily
A-acyclic by smash closure and the finite-stage James construction.
The finite-partition lemma proved in EH5_D3.md therefore makes every
identical power Z_l^(kappa_l) acyclic. Finally Z_l is (l-1)-connected,
so the remaining outer product is the filtered homotopy colimit of its
finite subproducts, and is ordinarily A-acyclic.

This proof also shows the source is primary and Miller, but already at
the lower endpoint. It needs no uniform Curtis exponent estimate and
makes no infinite-product suspension splitting assertion. Only finite
product suspension splittings are used before the infinite products are
reordered by fixed factor type.
