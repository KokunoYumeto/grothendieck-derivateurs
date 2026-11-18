# An integral diagonal test for the remaining James--Hopf image

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Exact necessary condition; the target mod-four
product and the stable Hurewicz image have not been evaluated.

**16 November 2026 update (D.2.50):** the total integral square is now
proved nonzero of exact order two. The canonical-cobar proof constructs
an integral fifteen-cycle with half-product evaluation one. Its stable
sphericity remains unknown; the stable-spherical pairing is still open.
See `I_integral_square_cobar.md` and the complete D.2.50 proof. The earlier
sections below retain the exact reductions that led to this result.

Let L=Z'=Y<7>, with the low stable model and quadratic coordinates
of D.2.43:

    K=(M(Z4,7) vee S8_r) union_(i eta7+2r) e9,
    pi15 D2 L = Z8{c} plus Z2{u}.

The unresolved actual composition is the metastable boundary of 2c.
The following supplies a concrete integral test for the possible
James--Hopf image, distinct from the mod-two operation tests.

## 1. The exact transfer identity

Klein, *On the stable Hopf invariant*, Theorem A(iii), gives

    tr H(f) = (f smash f) Delta_source - Delta_target f.

Theorem B identifies this H with the Segal--Snaith operation, hence
with the James--Hopf map used in D.2.43. For a stable map
f:S15->L the source reduced diagonal is stably zero, so

    tr JH(f) = -Delta_L f                              (1)

as a stable map into L smash L. This identity is about the actual
stable James--Hopf operation; an arbitrary choice of an operation
having only a similar vanishing criterion is not being substituted.

Primary source opened and read:
<https://arxiv.org/pdf/2603.07854>, version 3 dated 7 July 2026.
Theorem A(iii) is on printed p.3, Theorem B on p.4; the transfer
proof is on pp.12--13 and the full comparison proof on pp.13--16.
The latter checks the first and second Snaith weights explicitly
using the configuration model and eliminates higher weights by
the homogeneous-functor argument. The transfer proof is the
forgetful map applied to the defining equivariant difference.
The published primary HTML was also opened:
<https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/on-the-stable-hopf-invariant/F0D66B5EA77A0AABA4F98119DA7F15BC>.

## 2. Integral transfer in the specified low coordinates

Use label chains a7,b8,r8,s9 with db=4a and ds=2r. The eta
attachment has zero integral cellular differential. Cells of L
above dimension nine cannot affect H15(L smash L), because a
new ten-cell first contributes a product in dimension seventeen.
The ordinary tensor complex has cycles

    t=ab+ba,   v=ar,   w=ra

in degree fifteen, with relations 4t=0, 2v=0, 2w=0.
Thus

    H15(L smash L;Z) = Z4{t} plus Z2{v,w}.              (2)

For the regular two-fold cover, the integral transfer on the
resolution model is the norm in resolution degree zero and is
zero in positive resolution degree. This is a chain map:
the norm annihilates the first resolution differential, and
commutes with the internal tensor differential. It sends

    c=e0(ab)+2e1(aa) -> ab+ba=t,
    u=e0(ar) -> ar+ra=v+w.                             (3)

The stable Hurewicz map on the quadratic source group in D.2.43
is an isomorphism. Hence if JH(f)=2c, equations (1)--(3) imply

    (Delta_L)_* h_Z(f) = -2t ≠ 0.                     (4)

In particular f cannot have zero integral stable Hurewicz value.
More generally, if the Tor-coordinate of the reduced integral
diagonal is zero on every stable-spherical H15 class of L, every
James--Hopf image has c-coordinate divisible by four and cannot
equal 2c. Vanishing of the entire integral diagonal would give the
stronger bound im JH subset <4c>; neither vanishing has been proved.

## 3. An equivalent mod-four cup pairing for the necessary condition

Let a7 in H7(L;Z4) be the fundamental coefficient class and let
b8 be the mod-four reduction of its integral coefficient connecting
class beta4(a7). In the low cellular model, these are the duals of
the a and b labels; b8 is zero on r. The Tor cycle t in (2) is
detected by a7 tensor b8, while v and w are not. Therefore (4)
has the necessary consequence

    <a7 cup b8, h_Z(f) reduced modulo4> = ±2 in Z4.    (5)

This is a concrete target calculation that would exclude the
remaining image if its left side always vanished for stable
spherical classes. A vanishing statement only modulo two does
not suffice, because the required value in (5) is already even.
Likewise, the proved mod-two square y8²=0 and the secondary class
of D.2.42 do not determine this mod-four mixed product.

The condition is necessary, not sufficient: a stable-spherical
homology class satisfying (5) need not have James--Hopf value
exactly 2c rather than another class with the same transferred
Tor-coordinate. The kernel of the integral transfer on the
quadratic group is <4c>, and there is also the independent u
coordinate to retain. No nullification or all-choices conclusion
is drawn from this reformulation.

## 4. The exact half-product class

The mod-two product in question is zero on this actual L. Here is
the required low-degree argument, separately from any integral
claim. In H*(Omega L;F2), use the degree-six class u and degree-seven
classes D,E. Their images in the James tensor algebra
H*(Omega Y;F2)=T(Sigma H~*(B;F2)) are

    u -> aa,   D -> ab+ba,   E -> f.

These are the same actual homology-suspension coordinates used in
D.2.42. The four degree-thirteen products uD,Du,uE,Eu have the
distinguishing tensor words aaab, abaa, aaf, faa, respectively.
Their images are therefore linearly independent. In a minimal
mod-two Adams--Hilton model for the six-connected L, a differential
in degree thirteen has no cubic term: a tensor generator has
degree at least six, so cubic terms start in degree eighteen.
The complete possible quadratic terms in this degree are precisely
uD,Du,uE,Eu. The quadratic differential is dual to the reduced
diagonal. Their independence in loop homology therefore forces
every H7(L;F2) times H8(L;F2) product to be zero. This is the same
actual Adams--Hilton interface proved in D.2.26 and used in D.2.42;
it does not replace integral chains by the mod-two word table.

Write a=a7, b=red4 beta4(a), and let i:F2->Z4 be 1|->2.
The coefficient sequence 0->F2->Z4->F2->0 now gives

    a cup b = i(theta),   theta in H15(L;F2),             (6)

where theta is determined exactly modulo Sq1 H14(L;F2).
There is a useful integral cochain construction. Choose an
integral lift A7 of a with dA=4B8. The class of B is beta4(a).
Since (A cup B) mod2 is zero in cohomology, choose an integral
cochain C14 with dC congruent to A cup B modulo two. Set

    E15=(A cup B-dC)/2.

The division is a division of an even integral cochain, not of a
cohomology class. Singular cup products satisfy Leibniz exactly,
so

    dE=2(B cup B),
    theta=[E mod2],
    beta_Z(theta)=[B cup B] in H16(L;Z).                 (7)

Here beta_Z is the integral Bockstein for 0->Z --2-> Z->F2->0.
In particular (6) and (7) retain a possibly nonzero integral
square even though its mod-two reduction is zero.

For every integral cycle z, coefficient compatibility gives

    <a cup b,z mod4> = 2<theta,z mod2> in Z4.             (8)

This pairing is independent of the stated ambiguity. If theta is
changed by Sq1(v), then its value on z mod2 is zero, because the
homological first Bockstein vanishes on the reduction of an
integral cycle. Equivalently Sq1(v) is the reduction of the
integral two-torsion class beta_Z(v), whose evaluation on an
integral cycle is zero. Stable sphericity is not needed for this
well-definedness assertion.

Consequently the necessary transfer test (5) is exactly

    <theta,h_Z(f) mod2> = 1.                            (9)

No value of this stable-spherical pairing has yet been proved.
There is an exact comparison for ALL integral cycles. Put
T=H15(L;Z), a finite torsion group. The coefficient connecting
map Hom(T,F2)->Ext(T,Z) for 0->Z --2-> Z->F2->0 is injective,
because Hom(T,Z)=0. Naturality of the universal-coefficient
sequence identifies beta_Z(theta) with the image under this
injection of theta's evaluation homomorphism on T. The Ext term
from H14(L;Z) contributes zero to this connecting map. Therefore

    B²=0  iff  theta pairs zero on every integral H15 class.

Equivalently, if beta_Z(theta)=0 then theta has an integral lift;
that lift is torsion because L is rationally acyclic, so its
evaluation on an integral cycle is zero. The converse restricted
to stable-spherical cycles is not asserted: that subgroup can be
smaller than T. The cochain construction and ambiguity were
independently read and passed by the axioms agent; the root
independently supplied and checked this UCT sharpening.

There is also a useful exact exponent restriction. Section 6 constructs
a mod-four lift theta4 of theta. For an integral cycle of order at
most two, the evaluation of theta4 lies in the subgroup {0,2} of
Z4; reducing that value modulo two gives zero. Hence theta vanishes
on H15(L;Z)[2]. In particular a stable map with JH value 2c must
have integral Hurewicz image of order at least four. This is only
a necessary restriction on the stable-spherical subgroup, not a
claim about the exponent of that subgroup.

## 5. Why the ordinary Postnikov square does not resolve (9)

Emery Thomas, *The suspension of the generalized Pontrjagin
cohomology operations*, Pacific J. Math. 9 (1959), 897--911,
Section 2, formula (2.1), printed p.899, defines the model
Postnikov square using the coefficient homomorphism

    Z/q -> Gamma_2(Z/q)=Z/(2q),   1 |-> q.

For q=4 this is 1|->4, not 1|->2. Its integral representative
in the present notation is A cup dA=4A cup B modulo eight.
It therefore sees only the mod-two parity of a cup b. In
particular the value two modulo four required in (5) maps to
zero. Theorem I and its full proof in Section 5 identify this
operation as the suspension of the Pontryagin square; that
identification does not repair the lost coefficient information.

The primary publisher PDF was opened and the definition and proof
read at
<https://msp.org/pjm/1959/9-3/pjm-v9-n3-p26-p.pdf>.
The related Browder--Thomas axiomatization, Section 4, printed
pp.59--60, was also read at
<https://webhomes.maths.ed.ac.uk/~v1ranick/papers/browthom.pdf>.
The latter's coefficient notation must be interpreted through
the explicit defining cochain formula, rather than inferred to
be the injective map Z4->Z8. No primary-operation argument here
annihilates the half-product theta.

## 6. The exact link with the secondary class of D.2.42

This is a relation of chosen coefficient lifts; it does not identify
theta with the restriction of the D.2.42 class. Continue to write
dE=2B². Choose an integral cochain C15 lifting the mod-two square
nullhomotopy c15 used in D.2.42. Since dc15=(B mod2)², there is an
integral cocycle D16 with

    dC15=B²+2D16.

Then

    theta4=[E-2C15 mod4] in H15(L;Z4),
    red2(theta4)=theta,   beta4(theta4)=-[D16].           (10)

In particular theta has this explicit mod-four lift; this also
follows from Sq1(theta)=red2(B²)=0.

Let q:L'=Y<10>->L. Since L' is nine-connected, choose an integral
cochain P7 with dP7=q*B. The integer cochain

    I15=q*E-2P7 cup q*B

is closed. The mod-two class of q*C15-P7 cup q*B is exactly the
secondary class Theta15 of D.2.42, with its square nullhomotopy
and coefficient primitive chosen compatibly. Direct equality of
cochains now gives

    q*theta4=red4[I15]-i(Theta15),
    beta_Z(Theta15)=q*[D16]=-q*beta4(theta4).             (11)

The sign comes from d(E-2C15)=-4D16. No graded commutativity
replacement is needed: the singular products occur in the same
order throughout. If the common square nullhomotopy is changed by
a degree-fifteen cocycle ell, theta4 changes by -i(ell), while
Theta changes by q*ell. Thus the single global normalization in
D.2.42 preserves (11), after making the corresponding change of
theta4. The integral class I15 is unchanged by this normalization.

Because L' is rationally acyclic and of finite type, [I15] is
torsion. On the reduction of any integral fifteen-cycle z' of L',
equation (11) consequently gives

    <q*theta4,z' mod4> = -2<Theta15,z' mod2>.             (12)

This is a genuine integral refinement of the earlier secondary
class. In contrast, q*theta itself has zero pairing on every such
integral cycle: by (6), i(q*theta)=q*(a cup b)=0, so q*theta lies
in Sq1 H14(L';F2). Thus the obstruction in (9), if nonzero, has
to be detected by stable classes of L outside this higher-cover
image. Nonvanishing of Theta, or its established failure to be a
specified sum of Steenrod operations, does not by itself determine
that obstruction. Equations (10)--(12) were independently read and
passed by the axioms agent.

## 7. An actual Stiefel-cone check and the fourteen-dimensional bound

There is an independent geometric check of the coefficient two for
the particular boundary under investigation. Morisugi--Mukai,
*Lifting to mod 2 Moore spaces*, printed p.523, the paragraph
immediately before Lemma 2.7 and Lemma 2.8(ii), identify

    M(Z/2,7) union_(l4) e15 = V_(9,2).

This primary passage was reopened at
<https://www.jstage.jst.go.jp/article/jmath1948/52/3/52_3_515/_pdf>.
The Stiefel manifold is the unit tangent sphere bundle of S8.
Its mod-two degree-seven and degree-eight generators x,y have
x cup y equal to the nonzero top class: this follows either
from mod-two Poincare duality, or directly from the sphere-bundle
Serre sequence. The integral Euler class is twice the generator
of H8(S8;Z), so the mod-two sequence has zero transgression and
the product of the fiber and base generators is the top class.

Put alpha_K=m0 l4:S14->K and C_alpha=K union_(alpha_K)e15.
The actual map of cones V_(9,2)->C_alpha has top-cell degree one
and restricts on the Moore part to the specified bottom-two,
top-one map m0. Extend the low classes a in H7(K;Z4) and
b=red4 beta4(a) uniquely over the fifteen-cell. On V_(9,2),
their pullbacks are

    a |-> i(x),
    b |-> red4 beta2(x),

where i:F2->Z4 is 1|->2, and beta2 is the integral Bockstein.
Coefficient naturality gives beta4 i=beta2 and
red2 beta2(x)=Sq1x=y. Thus

    pullback(a cup b)=i(x cup y)=2[top] in H15(V_(9,2);Z4).

Consequently the mod-four cup coefficient in C_alpha is exactly
two. This proof uses only the actual cone map and coefficient
naturality; it does not assume additivity of a generalized Hopf
invariant or a converse to the transfer identity.

Let P be obtained from K by adjoining cells only in dimensions
ten through fourteen (and optionally the free nine-sphere R).
Its low classes a,b extend uniquely. If alpha_K became null in
P, its nullhomotopy would give a map C_alpha->P fixing K. The
nonzero product just computed would then be pulled back from
H15(P;Z4)=0, a contradiction. Therefore alpha_K survives nonzero
through every such fourteen-dimensional extension. Its order can
decrease from four to two; this argument does not prevent that.

Equivalently, the transfer calculation proves that every fifteenth
stable James--Hopf value for P lies in the kernel <4c> of transfer,
because H15(P;Z)=0. Neither 2c nor 6c lies in that kernel. Thus
only actual fifteen-cells can kill this particular class. The
full target still requires precisely the stable-spherical test
(9); cells of lower dimensions can affect which fifteen-cell
cycles are stably spherical and therefore cannot be erased from
that subsequent calculation.
