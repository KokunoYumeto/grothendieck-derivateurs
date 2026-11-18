# The remaining unstable Pruefer comparison

Research probe after D.2.15, 2026-11-15. No equality or strictness is
claimed in this note.

Let A=B(C_{p^infinity}) and B=BC_p. Write W_A and W_B for their
smallest reversible localizers. Filtered finite cyclic-group extensions
give W_A contained in W_B. D.2.15 now proves that their stable parts
are both loc(S/p). D.2.7 gives the exact remaining comparison:

    W_A = W_B  iff  P_A(Sigma B)=*.

The elementary fact P_A B=B does not decide this reversible question.
In particular no distinction is inferred merely from the fundamental
groups or the lowest ordinary cohomology degree.

## A concrete mapping-space reduction

Put Y=Sigma BC_p. This is simply connected and has finite p-primary
integral homology in each positive degree. Its homotopy groups are
finite p-groups, by induction using its finite Postnikov sections and
the relative Hurewicz/Serre exact sequence. Equivalently this is the
usual simply connected Serre-class argument. Thus Y is p-complete.

The map A->CP-infinity used in D.2.14 is a mod-p homology equivalence.
Since Y is mod-p local, it induces

    Map_*(CP-infinity,Y) = Map_*(A,Y).

This applies to the whole derived mapping space. Contractibility of
this mapping space would prove strictness: Y would be nonzero and
A-null, hence could not be A-acyclic. But its contractibility has not
been proved here.

Every unsuspended map CP-infinity->Y is zero on positive mod-p
cohomology. Indeed every positive product in H*(Y;Fp) vanishes,
whereas H*(CP-infinity;Fp)=Fp[x] has no nonzero nilpotents. This is
only a cohomology statement, not a nullhomotopy statement.

There is also a concrete obstruction to a proposed blanket
Steenrod-module vanishing argument. At p=2, let t be the degree-one
class of RP-infinity and x the degree-two class of CP-infinity. The
assignment

    Sigma(t^(2k+1)) -> Sigma^2(x^k), k>=1,
    Sigma(t^(2k))   -> 0,
    Sigma(t)        -> 0

defines a nonzero homomorphism of unstable Steenrod modules from
reduced H*(Sigma RP-infinity;F2) to reduced
H*(Sigma² CP-infinity;F2). Odd squares have zero image on both sides;
for even squares the identity

    binom(2k+1,2j) = binom(k,j) mod2

checks compatibility. This is an algebraic possibility only. No map
of spaces realizing it is asserted. Thus even the primary-operation
calculation needs an unstable realization obstruction before it can
establish the desired mapping-space nullity.

## The actual Thom-space interface

Let L be the universal complex line on CP-infinity. The sphere bundle
S(L^p) is BC_p. Taking the homotopy cofiber of its projection to the
disk bundle gives the genuine unstable sequence

    BC_p -> CP-infinity -> Th(L^p) -> Sigma BC_p.

The stable version is also displayed in Behrens, *Root invariants in
the Adams spectral sequence*, Section8:
<https://www3.nd.edu/~mbehren1/papers/rootpub.pdf>.
The geometric sphere-bundle description supplies the unstable form
directly and fixes the line-bundle convention.

On the other hand, P_A CP-infinity=K(Z[1/p],2), as proved in the
earlier source note. Hence multiplication by p on CP-infinity is an
A-equivalence. It does not follow that the map of Thom spaces induced
by pulling L back along p is an A-equivalence. Such an inference
requires control of the full sphere-bundle twist; nullification is
not known here to preserve this parametrized construction. The stable
Thom orientation argument in D.2.15 uses a ring coefficient spectrum
and duality and does not supply this unstable comparison.

## Scope checks on possible theorems

Bousfield, *Unstable localization and periodicity* (1996),
<https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/bousfield-ulp.pdf>,
was reopened through Sections1--4. Theorem2.10 computes nullification
on infinite-loop spaces; Theorem4.6 computes it on finite Postnikov
spaces; neither computes Sigma BC_p. Theorem3.3 supplies the already
used finite-suspension nullity relation. The general lowest transition
P_(Sigma A)Y -> P_A Y can have a non-GEM fiber: the text following
Theorem1.8 explicitly distinguishes it from the higher transitions.
It cannot be treated as a GEM merely because Y is a suspension.

No general theorem extending finite-dimensional Sullivan targets to
arbitrary finite-category targets is being used. Such a blanket
statement is false; suspension targets already carry their own
identity in a positive homotopy group of the relevant mapping space.
Likewise, finite homotopy groups of Y remove certain phantom issues
but do not turn cohomologically trivial maps into null maps.

The current unresolved object remains P_A(Sigma BC_p). The steps
above neither prove an additional point in the fixed-stable-part
fiber nor prove collapse of its Pruefer and finite-cyclic generators.

## Exact failure of the proposed untwisted transfer

The genuine Pontryagin--Thom boundary has source Th(L^p), not
Sigma^2 CP-infinity. The difference is detectable integrally. If U is
the Thom class in degree two and x is the base generator, then

    H~*(Th(L^p);Z)=U Z[x],     U^2=p xU,
    (x^i U)(x^j U)=p x^(i+j+1)U.

For any map f:Sigma^2 CP-infinity -> Th(L^p), the pullback of U is
zero because the source has no reduced cohomology in degree two.
All positive products on the source vanish. Applying f* to
U(x^j U)=p x^(j+1)U therefore gives p f*(x^(j+1)U)=0. Integral
cohomology of the source is torsion-free, so every such class pulls
back to zero. Thus f* is zero on all reduced integral cohomology.
The integral cohomology of both spaces is free and concentrated in
even degrees, so the same holds after reduction modulo p.

Consequently no such untwisting map can realize the nonzero q=2
Steenrod-module pattern above. This does not exclude a map directly
from Sigma^2 CP-infinity to Sigma BC_p which fails to factor through
Th(L^p), and does not prove contractibility of the full mapping space.

There is a second, independent error in a tempting orbit argument.
The pth-power map on complex fibers identifies Th(L^p) with the
ordinary C_p-orbit of Th(L). But the fixed locus in the latter is the
zero section CP-infinity together with the separate Thom basepoint,
namely CP-infinity_+. Thus the Borel-to-orbit correction at the fixed
locus involves BC_p smashed with CP-infinity_+, including a BC_p
summand. Replacing this by BC_p smashed with reduced CP-infinity
would discard exactly the generator whose reversible membership is
at issue. Hence the orbit construction does not prove the desired
comparison from the established stable ideal equality.

Current precise obstruction: neither an unstable construction killing
Sigma BC_p from BC_(p-infinity), nor an A-null target detecting it,
has been obtained. The line-bundle twist cannot be removed by the
proposed ordinary transfer or orbit argument.

## An exact geometric fibration, without a nullification claim

The integral Thom class defines a map u:Th(L^p)->CP-infinity. Its
restriction to the zero section is multiplication by p on
CP-infinity. The homotopy fiber of u is Sigma^2 BC_p.

Here is a direct model. Pull the principal circle bundle classified
by u back over the Thom pushout. Over the disk-bundle piece it is the
sphere bundle E=S(L^p)=BC_p; over the cone on E it is trivial. The
resulting homotopy pushout for its total space has maps

    E <- E x S^1 -> S^1,

where the first map is the principal circle action and the second is
projection. The homeomorphism (e,z) |-> (ze,z) of E x S^1 identifies
this diagram with the two projections. Its homotopy pushout is the
join E*S^1, equivalent to Sigma^2 E. This yields the actual fibration

    Sigma^2 BC_p -> Th(L^p) --u--> CP-infinity.

The fibration rephrases the missing unstable comparison; it does not
compute the A-nullification of its fiber. In particular, no inference
that nullification preserves this fibration is made from the fact
that multiplication by p on the base is an A-equivalence.

The geometric fibration calculation was independently checked by the
axioms/derivators agent: the boundary trivialization is the canonical
tautological unit vector in the pulled-back line, and the circle-action
change of coordinates is global. No extra lift or arbitrary framing
has been assumed.
