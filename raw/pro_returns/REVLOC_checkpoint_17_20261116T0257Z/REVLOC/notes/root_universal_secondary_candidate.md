# A universal-space route to the remaining Adams differential

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. **Full argument independently audited and passed.**
The algebraic, primitive-normalization, universal-space and actual
secondary-operation/Adams-differential interfaces were checked by root
and both independent readers. Sections1--4 retain the stages and
promotion gates of the investigation; Sections5--6 close them.

## 1. The exact degree-nine relation

Use the stable Steenrod relation

    R = Sq1 Sq8 + Sq2 Sq1 Sq6 + Sq8 Sq1 = 0.

Indeed Sq1 Sq8=Sq9, Sq1 Sq6=Sq7 and
Sq2 Sq7=Sq9+Sq8 Sq1. On the actual bottom a7 of L, all
three inner operations Sq1,Sq6,Sq8 vanish, by D57 and instability.
The associated secondary operation has degree eight and values in
H15(L;F2), with the usual positive-primary indeterminacy.

A stable construction fixes what is meant. Put H=HF2 and form the
fiber P of

    (Sq1,Sq6,Sq8): Sigma7 H -> Sigma8 H + Sigma13 H + Sigma15 H.

The row (Sq8,Sq2 Sq1,Sq1) maps the target to Sigma16 H. A fixed
nullhomotopy of its composite, supplied by R, gives a secondary map
P->Sigma15 H. The fiber restriction is the loop of the row. A lift
of a7 to P therefore gives a definite secondary class. Changing the
three primary nullhomotopies changes that class only by the three
positive-operation images; all are annihilated by a primary-annihilated
degree15 homology class.

## 2. A smaller actual universal space controls the choices

Let

    F = hofib(Sq6 rho : K(Z4,7) -> K(F2,13)).

The fundamental mod-four class supplies a nullhomotopy of Sq1 rho,
and Sq8 rho is universally zero by instability on K(Z4,7). Choose
these two universal nullhomotopies once. The fiber supplies the
Sq6 nullhomotopy. The preceding stable construction consequently
gives a particular class phi in H15(F;F2).

Its restriction to the fiber K(F2,12) is exactly

    Sq2 Sq1 iota12.

This is the middle component of the looped row; the two base-chosen
nullhomotopies restrict to their constant choices. A lift L->F
exists because a7 lifts modulo four and Sq6 a7=0. Its pullback of
phi is one admissible value of the R-secondary operation.

Double looping gives a fibration with base K(Z4,5), target K(F2,11),
and fiber K(F2,10). Its defining map is Sq6 rho on a degree-five
class and hence null by instability. Choosing one nullhomotopy
gives an actual space equivalence

    Omega²F ~= K(Z4,5) x K(F2,10).

Write x5 and y6 for the reduction and higher coefficient connecting
class of K(Z4,5), and z10 for the other factor. There is no mixed
positive product in degree13, since 5+10>13. Fiber restriction thus
forces

    sigma² phi = Sq2 Sq1 z10 + eta,
    eta in H13(K(Z4,5);F2).

Serre's original Section2 no11, Theorem4 and its preceding proof,
printed pp204--205, were independently reopened by root. Every
polynomial generator of this GEM is a positive Steenrod operation
on x5 or on y6=delta2(x'_5), except these two fundamental generators
themselves. Therefore eta is a sum of positive-primary images of
x5,y6 and decomposables. Both x5,y6 pull back from double cohomology
suspensions of actual classes on L; coefficient connecting maps
commute with suspension. The source is the already opened
I_Serre1953, https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf.

## 3. Every relevant class admits a primitive preimage with Sq2 zero

D58 proves H13E -> H15L onto. E is four-connected. In degree13 its
reduced diagonal has only bidegrees (5,8),(6,7) and their reverses;
all these lower-degree factors are primitive. The nine product
directions u H8E and H6E H7E realize every such symmetric diagonal.
Subtracting a suitable sum of these products makes any preimage
primitive without changing its double suspension.

Let z be such a primitive preimage of a primary-annihilated class
in H15L. Then Sq2_* z is primitive and lies in the exact D56 kernel

    <uD,uE6,xi u> in H11E.

The first two products have independent nonzero reduced diagonals.
Thus Sq2_* z is a multiple of xi u. That coefficient is always
zero, even before restricting to E. In the ambient free E2 algebra,
a degree13 restricted generator is xi(y6), with restricted-Lie
input y6 one of f,x,{a,b}. Their Bocksteins are 0,d+e,0; none has
the u=xi a coefficient. By top Nishida, none can produce the outer
generator xi u under Sq2. Labels, ordinary Lie words and products
cannot produce that outer generator either. The known injection
H11E -> H11T therefore gives

    Sq2_* z=0.

Root and the simple reader independently checked this whole lemma.
It requires no new degree13 cover-edge isomorphism.

The proposed universal secondary class consequently evaluates zero:
eta's decomposable part vanishes on primitive z; its positive-primary
part is a suspended positive operation from L and vanishes on the
chosen primary-annihilated image; and the fiber term pairs with
Sq1_* Sq2_* z=0. Thus the proposed argument gives

    <pullback(phi), any primary-annihilated H15L class>=0.

This uses a chosen actual universal value, not an assertion that all
the arbitrary indeterminacy after looping is annihilated. In
particular it avoids the invalid step of discarding Sq1 H12E on
the K1 and K2 representatives, whose Bocksteins in E are nonzero.

## 4. Remaining promotion gate

The above operation must be identified, with its actual normalization,
with a linear functional on the incoming Adams d2 whose value on the
bottom image of h0h3 is one. The fibrations reader has a universal
module and complete cobar certificate supporting this identification,
but the actual topological secondary-operation pairing still needs
a full proof or an exact opened theorem and derivation.

For comparison with the sphere's minimal resolution, substitute
Sq6=Sq2 Sq4+Sq5 Sq1 in R. Its syzygy becomes

    Sq8 e1 + (Sq5+Sq4 Sq1)e4 + Sq1 e8.

The last Sq1 e8 coefficient shows that this degree-nine syzygy is
not generated by lower-degree relations, which have no e8 component.
The sphere Ext group in bidegree (2,9) is one-dimensional on h0h3.
This is a useful normalization check, not a replacement for the
general Adams differential comparison on L.

Until that gate is closed, no Adams permanence, n parity, stable
sphericity, actual h value or solution of D.2.4 is asserted here.

## 5. Explicit track comparison, submitted for independent audit

Root opened Baues--Jibladze, arXiv:math/0407031v3, construction (4.1),
Theorem4.2, the Adams coresolution construction of Section6, and the
entire proof of Theorem7.3 on printed pp19--21. In particular the latter
identifies the differential with the composite of the two zero tracks,
and Lemma7.7 verifies the associated lift-of-fiber comparison. Root also
opened Adams1960 Section3.6, including axioms, Lemma3.6.3 and the proofs
of Theorems3.6.1--2, and Section3.8's resolution comparison.

Here is the additional argument needed to apply those sources to this
exact relation. Put M=H*(L;F2), and use the nonminimal free bar resolution

    P0=A tensor M,
    P1=A tensor bar(A) tensor M,
    P2=A tensor bar(A) tensor bar(A) tensor M.

The first two differentials are

    d1([b]m)=b tensor m + 1 tensor bm,
    d2([a|b]m)=a[b]m + [ab]m + [a](bm).

For the three-term relation cycle r, the last two sums cancel, because
each inner operation kills a7 and the sum of composites is R=0. Hence

    d2 r = Sq8[Sq1]a7 + Sq2 Sq1[Sq6]a7 + Sq1[Sq8]a7.

The cycle r has only scalar coefficients on three free P2 generators;
it can therefore be made one basis vector by an ordinary basis change.
Realize the first stages by GEM spectra A0,A1,A2 and a genuine secondary
Adams coresolution L --g0--> A0 --d1--> A1 --d2--> A2. Write eta0 for
the zero track on d1 g0 and eta1 for that on d2 d1. The actual coherence
equation is eta1 g0 = d2 eta0. We retain that equation; choosing arbitrary
algebraic zero tracks instead would miss the secondary structure of L.

In the r coordinate, d2 is the row (Sq8,Sq2 Sq1,Sq1) on the three A1
coordinates in degrees8,13,15. A chosen stable nullhomotopy H of R gives
a zero track on this coordinate of d2 d1, factoring the degree7 bottom
coordinate of A0. The difference eta1_r-H is an ordinary stable map

    q:A0 -> Sigma15 HF2.

By the coherence equation, pulling q back along g0 is exactly the
R-secondary operation on a7 with the chosen inner nullhomotopies, up
to its stated positive-primary indeterminacy.

A primary-annihilated x in H15(L;F2) gives c:S15->A0 by the augmentation
pairing. It is a cocycle, so choose gamma: d1 c ~ 0. The cited Adams
track formula gives the r coordinate of d2(x) as

    eta1_r c + (Sq8,Sq2 Sq1,Sq1) gamma.

The three relevant looped A1 coordinates have degrees7,12,14; their
maps from S15 are zero. We may choose c with only degree15 coordinates
in A0, so its bottom degree7 coordinate is constant. Thus Hc is zero
as well. The displayed value is consequently qc, which by the definition
of c equals <g0* q,x>. It follows that

    <r,d2(x)> = <Phi_R(a7),x>.

Changing H changes the pullback by a degree8 primary operation on a7;
changing inner nulls changes it by the row's positive-primary images.
Both are killed by x. Thus the equation uses the definite universal-space
value from Sections1--3 without a hidden normalization choice.

This is a candidate complete proof of the promotion gate; it was sent
to both independent readers at 02:40 UTC for checking before promotion.

## 6. Completed audit and consequences, 02:44 UTC

The fibrations reader and axioms reader independently passed the exact
track comparison in Section5. The latter reopened construction(4.1),
Theorem4.2 and the entire proof of Theorem7.3 of Baues--Jibladze. Both
readers also passed the actual universal-F evaluation and primitive
preimage lemma. Root therefore accepts the pairing and the vanishing
of its value on every primary-annihilated source in H15 L.

The relation functional pairs one with the bottom h0h3 class and zero
with every incoming Adams d2. No higher differential can enter its
filtration2 position. The bottom sphere map excludes outgoing
differentials by naturality. The class is permanent and detects a
nonzero stable 2 alpha sigma. In the stable cellular sequence, the
bottom target is the Z4 proved in D57; every nonzero subgroup of Z4
contains its double. Its sole remaining differential d8 must therefore
have zero image. There are no later incoming differentials by
connectivity of the sphere spectrum, and no outgoing bottom ones.

The detecting cycle of D54 is now permanent. The stable integral
Hurewicz criterion of D51 consequently gives h=h_M l4=0. The actual
class q=alpha sigma-prime has nonzero stable image 2 alpha sigma;
the already proved relation 2h=2q gives 2q=0. Thus q has exact order2.
This reasoning determines the original integer coefficient n only to
be even; it does not select n modulo4 when that finer choice is retained.

The full fourth-suspension extension and its role in all later
nullification cones are separate questions. This closes one concrete
homotopy obstruction, not D.2.4. The fibrations reader is preparing the
complete D.2.61 manuscript statement and exact four-term certificate.
