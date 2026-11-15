# The first nullification attachment: the exact Hopf-invariant boundary

Current status (2026-11-15, after D.2.16): the low-homology first-cone
statement is proved in D.2.12, and D.2.16 now excludes every ordinary
extension of the specific eta_2 smash B attachment, already at the
fourth stabilization stage. Sections 3--6 preserve the earlier research
sequence; their former all-choices extension boundary has been resolved
by D.2.16. The generic A_r-attaching-map question remains open. No
separator or second-stage persistence is asserted in this note.

Write B=K(F_2,2), X=Sigma^r B, A_r=QX, Y=Sigma X, and n=r+2>=3.
All homology in the main discussion has coefficients F_2.

## 1. What the first attachment provably preserves

The first-cone corollary in `sections/D2_unstable_obstruction.tex`
proves that every map h:Sigma^k A_r -> Y, k>=0, is zero on homology
in target degrees n+1,n+2,n+3. In degree n+4 its image is confined to
the line dual to the suspended class uv in H^5(B).

For k=0, the additional argument restricts h along X->QX. Freudenthal
makes this an isomorphism on H_(n+1). A bottom hit would give, on
suspended cohomology, u |-> v=Sq^1u and then u^2 |-> w=Sq^2v.
This is incompatible with Sq^1(u^2)=0 and Sq^1w=v^2!=0. The k=1
case is D.2.12, and k>=2 is excluded in the bottom degree by
connectivity. Sq_*^1 b=a and Sq_*^2 c=a propagate the vanishing to
the next two degrees.

Consequently H_i(Y)->H_i(C_h) is injective for n+1<=i<=n+3.
This also holds for the first simultaneous attachment along any small
wedge of such maps. The bottom integral group H_(n+1)(Y;Z)=Z/2
injects as well, by the universal coefficient and cofiber sequences.
No integral injection in degree n+3 is inferred from this mod-2
statement.

Exact primary Freudenthal check: Hatcher, *Algebraic Topology*,
Corollary 4.24, printed p.360 (PDF p.368), explicitly includes an
arbitrary (n-1)-connected CW complex, not just spheres:
https://pi.math.cornell.edu/~hatcher/AT/AT.pdf . This was reopened and
the exact statement checked. Serre's low-degree computation and the
Adem relation are already source-audited in D.2.12.

## 2. The quadratic question which low homology does not decide

The loop target initially has H_*(Omega Y)=T(V), V=H~_*(X).
Let a,b be its bottom generators in degrees n,n+1. The obstruction in
D.2.12 uses the nonzero commutator

    c=ab+ba,    |c|=2n+1.

Every first cofiber C_h remains n-connected. In the cobar filtration
for Omega C_h, all letters have degree at least n. Thus a word of
length at least three has degree at least 3n>2n+1. In this low degree,
the only possible boundary relation on the old length-two class is
the quadratic reduced-diagonal map

    H_(2n+3)(C_h)
       -> H_(n+1)(C_h) tensor H_(n+2)(C_h)
          + H_(n+2)(C_h) tensor H_(n+1)(C_h).

It is the full image of this map that matters, rather than a lone
coefficient when new low homology classes are present. A boundary
equal to a tensor b+b tensor a kills the old commutator. Higher
word-length corrections cannot occur in its total degree.

For k>=2 the two low homology groups of C_h are exactly the old
one-dimensional groups. In this case the risk is precisely a nonzero
cup product u_C Sq^1u_C in degree 2n+3, where u_C is the unique lift
of the old bottom cohomology class. For k=0,1 new low classes may
appear, and a nonzero coefficient alone need not kill the old
commutator: it may only relate it to another commutator.

For k>=n+3, H_(2n+2)(Sigma^k A_r)=0, so H_(2n+3)(Y) surjects
onto H_(2n+3)(C_h). Those classes have zero reduced diagonal, since
Y is a suspension. Such individual attachments cannot create the
quadratic boundary. The remaining genuine question lies in the
range 0<=k<=n+2. These degree observations are not a substitute for
computing an actual attaching map in that range.

The cobar argument here is the ordinary strongly convergent
simply-connected loop-space calculation; its complete primary-source
audit has not yet been added. It is being used as a research reduction,
not as a new numbered manuscript result.

## 3. An actual dangerous attachment with the unit source

There is an explicit model showing that even zero homology in every
degree does not preserve the commutator in general. Set r=1, n=3.
Let eta_2:S^3->S^2 be the Hopf map and form

    h_0=eta_2 smash id_B : Sigma^3 B -> Sigma^2 B.

Its homology map is zero in every degree. Its cofiber is CP^2 smash B.
If x is the degree-two class of CP^2, the old degree-four and
degree-five target classes lift to xu and xv. Their cup product is

    (xu)(xv)=x^2 uv != 0 in H^9(CP^2 smash B;F_2).

Here x^2 and uv are both nonzero. Thus the new reduced diagonal
contains precisely the old a tensor b+b tensor a term, and the
commutator dies. The Hopf map, its CP^2 cone, and the projective-space
cohomology ring are the standard primary calculations in Hatcher
sections 3.2 and 4.B; Serre gives uv!=0.

This is NOT yet an A_1-attachment. The exact missing extension is

    Sigma^2 Q Sigma B -> Sigma^2 B

restricting to h_0 along Sigma^3B -> Sigma^2 Q Sigma B. At this point
in the investigation its existence was undecided; D.2.16 subsequently
proved that no such ordinary extension exists, even at the fourth stage.

The analogous eta_(r+1) smash B for r>=2 is already a suspension,
so its cofiber has zero products and does not give this particular
dangerous quadratic example. The r=1 case is the concrete candidate
being tested, not a claimed uniform construction.

## 4. Two actual finite-stage extensions

For m=1 and m=2, suspension-loop evaluation supplies

    Sigma^2 Omega^m Sigma^(m+1) B -> Sigma^3 B,

restricting to the identity on Sigma^3 B along the stabilization unit.
For m=1, evaluate one loop and retain one outer suspension; for m=2,
evaluate two loops. Composing with h_0 gives actual extensions to
these first two stages of Q Sigma B. This was checked independently
by simple_higher. These positive finite-stage maps remain valid.
D.2.16 subsequently excluded all choices of extension at the fourth
stage, so there is no compatible extension through the full telescope.

## 5. Primary Steenrod and coalgebra data allow the proposed extension

Let f_0:Sigma^2B -> Omega Sigma^2B be the adjunct of h_0. The stable
Snaith weight-one projection induces a Steenrod-module retraction

    H~_*(Q Sigma B) -> H~_*(Sigma B).

Suspend this once and compose with H_*(f_0). It gives a homomorphism

    H~_*(Sigma Q Sigma B) -> H~_*(Omega Sigma^2B)

which extends the homology map of f_0 along Sigma^2B. It commutes
with every primary Steenrod operation. Its image is primitive,
because f_0 is a map from a suspension; the whole reduced homology
of Sigma Q Sigma B is likewise primitive. Thus it also extends to
a homology coalgebra homomorphism. All higher Snaith weights can
be sent to zero.

In particular the map sends the separate weight-two class a^2 in
H_6(Q Sigma B) to zero. It respects the root's Nishida obstruction
to sending that class to ab+ba when n is odd. The desired Hopf
invariant is instead on the linear unit summand, dual to uv in
H^5(B), so that special Nishida calculation does not exclude it.

This is only an algebraic extension at the one-adjunction level.
D.2.16 now proves that no actual space map realizes the required full
extension: its double adjunct and actual multiplication deviation
satisfy additional constraints not present in this one-adjunction map.
It shows that the primary homology, coproduct and Steenrod machinery
of D.2.12 cannot by itself rule out this particular first-attachment
example. The additional double-adjunction and multiplication-deviation
argument needed to close that gap is precisely D.2.16.

## 6. Boundary of the current calculation

After excluding the specific eta_2 smash B extension by D.2.16, no
actual map from a suspension of A_r has been produced that kills
the old commutator, and no universal vanishing theorem for that Hopf
invariant has been obtained. The actual unit-source example proves
why bottom-homology injection alone cannot establish survival.
Neither second-cone persistence nor nontriviality of P_(A_r)Y is
claimed. Independently, the exact looping formula is
P_A Omega Y = Omega P_(Sigma A)Y, not Omega P_A Y; a calculation
with A-attachments to Omega Y would still require the latter index
comparison before addressing the original question.

## 7. Exact remaining twice-suspended case after D.2.16

This section fixes r=1. Write A=Q Sigma B and T=Omega^2 Sigma^2 B.
Let A0,B0,C,D,E,F,X0 denote the suspended labels a,b,c,d,e,f,x of
D.2.13; their degrees are 3,4,5,6,6,7,7. Put k={a,b} and
p3=f+ac+a^3 in H_6(T). All coefficients below are in F_2.

For an arbitrary map G:A -> T, D.2.16 first gives G(C)=0, not merely
zero on its xi a coefficient. Indeed primitive H_5(T) is spanned by
d, e+ab, xi a. The relations beta C=0 and Sq_*^2 C=A0, together
with G(A0)=0, kill the first two coefficients. Here G(A0)=0 follows
from beta B0=A0, since primitive H_4(T) is spanned by a^2, whose
Bockstein is zero. Write G(B0)=s a^2.

The primitive degree-six basis is exactly

    b^2, k={a,b}, p3=f+ac+a^3,

with Sq_*^2 images a^2,0,a^2 and zero Bocksteins. The primitive
degree-seven basis is exactly

    xi b, {a,c}, P=g+ae+bc+a^2b, Q=h+ad,

where g,h are the B-labels dual to u^2v,uw. Its operations are

    beta(xi b)=b^2+k,  beta P=p3,  beta Q=beta{a,c}=0,
    Sq_*^2(xi b)=xi a,  Sq_*^2P=Sq_*^2Q=e+ab,
    Sq_*^2{a,c}=0,  Sq_*^3P=a^2,  Sq_*^3Q=0.

These are complete basis calculations from the polynomial/free-Lie
basis and the ordinary coproduct. In particular p3 really is primitive:
Delta' f=a tensor c+c tensor a,
Delta'(ac)=Delta'f+a^2 tensor a+a tensor a^2, and
Delta'(a^3)=a^2 tensor a+a tensor a^2.

Write G(D)=d1 b^2+d2 k+d3 p3 and G(E)=e1 b^2+e2 k+e3 p3.
The source relations Sq_*^2 D=B0, Sq_*^2 E=0,
beta X0=D+E, Sq_*^2 X0=C, Sq_*^3 X0=B0 give

    d1=e1, d2=e2=epsilon, d1+d3=s, e1=e3.

There is also no degree-six image on the extra source class A0^2.
Indeed R=Q^4 A0 satisfies beta R=A0^2 and Sq_*^2 R=0. The latter
identity excludes a xi b component in G(R), so beta G(R) can only
be a multiple of p3. Applying Sq_*^2 to G(A0^2), and using
Sq_*^2 p3=a^2, excludes that multiple too. Thus G(A0^2)=0.

### The exact second Bockstein

There is a direct integral chain proof of

    beta_2[b^2]=[xi a],   [b^2]=[k] on the second Bockstein page.

Use the bottom Moore space P^3(2) -> B, with reduced integral chains
a in degree2 and b in degree3, db=2a. In the arity-two little-disks
model use free equivariant circle cells e0,e1 with

d e1=(tau-1)e0. The action of tau on the labels includes the Koszul
sign, so tau(bb)=-bb and tau(ab)=ba. Put

    x=e0(b tensor b), h=e1(a tensor b), z=e1(a tensor a).

Then

    dx=2(e0(a tensor b)-e0(b tensor a)),
    dh=e0(b tensor a)-e0(a tensor b)-2z,
    d(x+2h)=-4z.

The mod-2 classes of x and z are b^2 and xi a. The same chain
calculation gives beta(e1(b tensor b))=b^2+k. Thus the displayed
integral boundary proves the asserted beta_2 equality; the previously
computed degree-six Bockstein basis shows xi a is not a beta_1 boundary.
Naturality along P^3(2)->B gives the formula in T. These are the same
configuration-chain conventions used in the proof of Cohen--Lada--May,
Chapter III, Lemma3.10, printed p232; that page was reopened and visually
checked (local audit image FGH_CLM_page122.png). The explicit mixed-label
calculation above was independently checked by simple_higher.

On the source beta_2[D]=[C], since H_4(B;Z)=Z/4; equivalently the
cohomological integral Pontryagin-square identity is
rho_2 beta_4 P(u)=w+uv. The exact original identity is Mahowald1964,
Section2.3, p1336, independently opened by simple_higher and root.
Thus naturality and G(C)=0 imply d1=d2=epsilon. Altogether

    G(D)=epsilon(b^2+k)+(s+epsilon)p3,
    G(E)=epsilon(b^2+k+p3).

This does NOT yet force epsilon or s to vanish.

### What is required to kill the old commutator

Homology suspension sends k to the old tensor commutator ab+ba,
sends b^2 to zero, and sends p3 to the linear f-label. A quadratic
boundary killing the old commutator must therefore come from an element
in the kernel of the ordinary attaching homology map, rather than from
an arbitrary nonzero commutator coefficient. The extra source A0^2 has
zero image, as proved above. On span{D,E}, the linear f coefficients
are s+epsilon,epsilon and the commutator coefficients are
 epsilon,epsilon.

If s=0, the linear and commutator functionals agree, so the
commutator functional vanishes on the kernel of the linear map.
If epsilon=0, there is no commutator term. The only remaining dangerous
case is therefore

    s=epsilon=1,
    G(B0)=a^2,
    G(D)=b^2+k,
    G(E)=b^2+k+p3.

In that case D has zero linear image and a nonzero commutator image.
No actual map realizing this pattern, and no obstruction excluding it,
has yet been proved. This is the exact remaining k=2 first-cone case;
it is narrower than the extension excluded in D.2.16 and cannot be
identified with that earlier prescribed Hopf map.

## 8. The fifth-suspension case cannot create this commutator

For h:Sigma^5 A -> Y, take its once-adjunct
phi:Sigma^4 A -> Omega Y. If its bottom degree-seven image had a
nonzero ab+ba coefficient, beta B0=A0 would force the primitive
class phi(sigma^4 B0) in degree8 to have bb coefficient one.
The complete degree-eight tensor basis has one-letter terms and
ac,ca,bb. Primitivity forces the coefficients of ac and ca to agree.
But Sq_*^2(bb)=aa, Sq_*^2(ac+ca)=0, and square operations on
one-letter terms remain one-letter. Thus Sq_*^2 of that image has
nonzero aa coefficient, contradicting Sq_*^2 B0=0. This argument
uses only Steenrod and coalgebra naturality, not multiplicativity.
Together with the degree argument for k>=6, this leaves k=0,1,2,3,4
for the actual generic first-cone question. The surviving k=2 case is
specified in Section7; the other cases and all subsequent cones remain
unsettled.

## 9. The spherical adjustment exists (16:55 update)

The possible degree-six spherical adjustment is now realized, not just
allowed by operations. The independent construction and original-source
audit are in `notes/EH5_degree8_spherical.md`. Akhmetiev--Repovs--Skopenkov,
Topology Appl.113(2001), proof of Theorem1.1 on p9, explicitly embeds
RP^3 x RP^3 x I^2 smoothly in R^8. Restriction to the middle slice
provides a genuine rank-two normal frame. Pontryagin--Thom followed by
the K(F_2,2)-class rs on the product gives an actual map S^8->Y whose
Hurewicz image is Sigma^2 f: (rs)^3 evaluates to1, whereas
(Sq^1(rs))^2=r^4s^2+r^2s^4 is zero. Its double adjunct has Hurewicz
image exactly z=b^2+k+p3. Primitivity, Sq_*^2 and the beta_2 calculation
above force the three coefficients to agree, and the f coefficient
forces each to be1. This agent reopened the complete original paper,
including its explicit smooth-category convention and thickened
embedding, and independently checked all steps.

Consequently the top-cell extension of a map M(Z/4,5)->T can be changed
by this actual sphere class. Combined with simple_higher's six-skeleton
Moore correction of the canonical map, this permits the dangerous
(s,epsilon)=(1,1), gamma=0 pattern on the finite six-skeleton. This is
not a map on the full source A: the next attaching maps, beginning with
the seven-cells, and all later extension conditions remain to be checked.
