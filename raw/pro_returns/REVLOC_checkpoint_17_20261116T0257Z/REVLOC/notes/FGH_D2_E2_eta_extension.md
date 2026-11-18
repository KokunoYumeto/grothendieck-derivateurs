# The twice-adjoint eta extension: exact low E2 data

2026-11-15. Research note, not a new manuscript claim.

Current status, after D.2.16: every ordinary extension of the specific
eta attachment considered below has been excluded, already at the fourth
stabilization stage. The all-choices proof is in
`sections/D2_eta_nonextension.tex`. The calculations below are retained as
the historical route to that theorem; their former undecided-extension
boundary is superseded. General first-cone and later-nullification questions
are distinct. D.2.27 handles mixed first attachments of exponents
zero/two/three/at least five, D.2.28 reduces exponent one to one coefficient,
and D.2.30 realizes that coefficient through a ten-skeleton. Exponent four
has the fixed-canonical obstruction of D.2.29 and the genuine finite-cell
indeterminacy recorded in `FGH_D2_k4_spherical_indeterminacy.md`.

Historical scope: this note verifies the reduced-J convention, records
the first low-degree calculation, and identifies why its apparent
Bockstein contradiction is false. These low calculations by themselves
neither construct an extension nor exclude all ordinary maps.

Put B=K(F_2,2), X=Sigma B, Y=Sigma^2 B and T=Omega^2 Y. The map

    h_0 = eta_2 smash id_B : Sigma^3 B -> Sigma^2 B

has twice adjunct g_0:Sigma B -> T. A solution of the actual attachment
problem is a map g:Q Sigma B -> T restricting to g_0. Such a map is
NOT assumed to be an H-map, an E2-map, or to commute with Dyer--Lashof
or Browder operations. It does commute with homology coproducts and
Steenrod operations.

## 1. The reduced J operation, rather than the unreduced BV action

Gaudens--Menichi, *Batalin--Vilkovisky algebras and the J-homomorphism*,
was opened at

<https://math.univ-angers.fr/~lmenichi/finalcour5.pdf>.

The exact interfaces are Theorem 3.1 (printed p.5), Proposition 5.4
(p.9), Theorem 5.10 and Corollary 5.11 (p.11), and Remark 6.3 (p.13).
The source-rotation operator BV_S differs from diagonal rotation.
Diagonal rotation vanishes on the unit B -> Omega^2 Sigma^2 B, but
this does not imply that source rotation vanishes there.

More precisely, the rotation loop is based at the identity self-map of
S^2. Translating it to the constant component gives J:S^1 -> Omega^2_0 S^2,
whose adjoint is eta_2. The actual map g_0 is the reduced composition
of this J with the unit labels. In characteristic two, Proposition 5.4 says

    BV_S(z) = sum (z_(1) circle eta) z_(2).

Consequently the actual label value z circle eta is the convolution
BV_S * chi, with chi the Pontryagin antipode. It is not generally BV_S(z)
for a nonprimitive label z. In particular, every value of g_0 is primitive,
because Sigma B is a suspension.

## 2. The top Nishida correction is essential

Cohen--Lada--May, *The Homology of Iterated Loop Spaces*, Chapter III,
Theorem 1.3(3), printed pp.217--218, was read from the original author scan

<https://www.math.uchicago.edu/~may/BOOKS/homo_iter.pdf>.

The formula on printed p.218 was checked visually. Write xi=xi_1=Q_1
for the top operation on an E2-space, so |xi z|=2|z|+1, and write
{z,w}=lambda_1(z,w). Then

    beta xi(z) = (|z| mod 2) z^2 + {beta z,z}.

The low higher formulas obtained from the same theorem are

    Sq_*^2 xi(z) = xi(beta z) + {z,Sq_*^2 z},

    Sq_*^3 xi(z) = (|z| mod 2)(beta z)^2
                   + {z,Sq_*^3 z} + {beta z,Sq_*^2 z}.

Chapter III, Theorem 1.2 supplies the Browder Cartan/Nishida laws and
{z,z}=0 at the prime two. Theorem 1.4 supplies homology suspension,
including sigma xi_1=xi_0 sigma and sigma lambda_1=lambda_0(sigma,sigma).
Theorems 3.1--3.2 and Lemma 3.8 give the free E2 homology algebra used
below. These statements, including the restriction to actual E2 maps
for operation naturality, were read in the source.

The images rendered for the exact top formula are
`FGH_CLM_114_right.png` and `FGH_CLM_115_left.png` in this directory.
They show printed pp.217 and 218, respectively.

Gaudens' subsequent paper, *Relations in the modulo 2 homology of framed
disks algebras*, <https://arxiv.org/pdf/1307.3148>, was also opened.
Its Corollary 4.5 is compatible with these formulas. No replacement of
source BV by diagonal BV is made here.

## 3. Labels and the low table

Serre's primary calculation gives H^*B=F_2[u,v,w,...] in the degrees
used here, with |u|=2, v=Sq^1u of degree3 and w=Sq^2v of degree5.
Use the following distinct homology labels in H_*B, and also their
images under B -> T:

| Label | Degree | Dual cohomology monomial |
|---|---:|---|
| a | 2 | u |
| b | 3 | v |
| c | 4 | u^2 |
| d | 5 | w |
| e | 5 | uv |
| f | 6 | u^3 |
| x | 6 | v^2 |

The needed data are

    beta b=a, Sq_*^2 c=a, Sq_*^2 d=b,
    beta d=Sq_*^2 e=beta e=0,
    beta x=d+e, Sq_*^2 x=c, Sq_*^3 x=b,

and reduced diagonals

    Delta' c=a tensor a,
    Delta' e=a tensor b+b tensor a,
    Delta' f=a tensor c+c tensor a,
    Delta' x=b tensor b.

The labels a,b,d are primitive. The twice-adjoint map has low values

| Input in H_*(Sigma B) | g_0 image in H_*T |
|---|---|
| sigma a | 0 |
| sigma b | a^2 |
| sigma c | xi a |
| sigma d | b^2 |
| sigma e | {a,b} |
| sigma f | {a,c} |
| sigma x | xi b |

Here the superscripts 2 mean Pontryagin squares in T. They do not mean
the label c dual to u^2, or the label x dual to v^2.

### Verification of the table

The cofiber of h_0 is CP^2 smash B. With t in H^2(CP^2), its old
classes are t times classes of B and their products are t^2 times the
corresponding products in B. Thus the quadratic part of the once-adjoint
map Sigma^2 B -> Omega Sigma^2 B is exactly the shifted reduced diagonal
of B. In the degrees at issue it is its complete homology map: the
linear part is zero since h_0 is homology-zero, and word length three
in H_*Omega Sigma^2 B=T(H~_*Sigma B) starts in degree9, beyond all the
degrees (at most8) used in the table.

The chain-level primary interface for this assertion was opened in
Halperin--Lemaire, *The fibre of a cell attachment*, Proc. Edinburgh
Math. Soc. 38 (1995), 295--311,

<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/51067699B6F3ADA6EAFB4AFFA43A3F85/S001309150001909Xa.pdf/the-fibre-of-a-cell-attachment.pdf>.

Section 3.1, printed p.300, identifies the quadratic part of a minimal
Adams--Hilton differential with the reduced homology diagonal and the
attaching differential with the homology of the adjoint. Section 7,
proof of Proposition 7.4, printed p.309, explicitly gives the same
relative model for the cone of a map whose source is an AH-suspension.
Our source and target are suspensions, and h_0 is homology-zero, so
the relative model is minimal. This avoids assuming a stronger,
unverified formula for the entire unstable James--Hopf invariant.

Now use homology suspension H_*T -> H_{*+1}Omega Y. It sends xi a to
(sigma a)^2, {a,b} to sigma a sigma b+sigma b sigma a, {a,c} to
sigma a sigma c+sigma c sigma a, and xi b to (sigma b)^2. It kills
Pontryagin products. The free E2 basis shows that the primitive kernel
of this suspension is zero in degree5 and degree7 and is spanned by
b^2 in degree6. In degree4 it is spanned by a^2.

For completeness, in degree7 the product part is spanned by ad,ae,bc,
a^2b, and a xi(a). None of their nonzero linear combinations is primitive:
their reduced diagonals have, successively, unique a tensor d,
a tensor e, b tensor c, a^2 tensor b, or a tensor xi(a) terms. In degree6 the product
part is spanned by ac,b^2,a^3; only b^2 is primitive. In degree5 the
only product is ab and it is not primitive.

It follows first that g_0(sigma c)=xi a, g_0(sigma x)=xi b and
g_0(sigma f)={a,c}. The exact top Nishida formulas then give

    beta xi b=b^2+{a,b},
    Sq_*^2 xi b=xi a,
    Sq_*^3 xi b=a^2.

The last equality and Sq_*^3 x=b force g_0(sigma b)=a^2. The possible
b^2 ambiguity in degree6 is resolved using Sq_*^2 d=b and Sq_*^2 e=0,
because Sq_*^2(b^2)=a^2 while Sq_*^2{a,b}=0. This proves the remaining
two entries. All the low relations are therefore consistent; in
particular beta x=d+e requires the Browder correction and does not
produce a contradiction.

## 4. Why the next product test is not yet an obstruction

Use capitals A=sigma a, C=sigma c and X_0=sigma x for source labels
in H_*Q Sigma B, of degrees3,5,7. They are primitive. Cartan gives

    Sq_*^2(C X_0)=A X_0+C^2.

In the target, Sq_*^2((xi a)(xi b))=(xi a)^2. But an arbitrary g
does not send the source product C X_0 to that target product, and
g(A X_0) need not vanish even though g(A)=0. Its coproduct only says
that g(A X_0) is primitive; (xi a)^2 is a primitive element of the
correct degree10. Thus a primitive correction can absorb the apparent
square discrepancy. Likewise g(C^2) is not forced to equal (xi a)^2.
No Pontryagin multiplicativity is available to remove this freedom.

This does not assert the existence of a full algebraic extension in
all degrees. It records exactly why the first proposed product argument
does not exclude all actual extensions.

### A necessary failure of multiplicativity

There is, however, a definite restriction on every putative extension:
its homology map cannot preserve Pontryagin multiplication. This uses
Steenrod naturality, not Dyer--Lashof naturality of the unknown map.

Retain C=sigma c of degree5, so g(C)=xi a. In the infinite loop source,
the ordinary Nishida formulas give

    Sq_*^2(Q^8 C)=Q^6 C,    beta(Q^6 C)=Q^5 C=C^2.

Here beta C=0 and the coefficient binomial(6,2) is odd. Let lambda
denote the coefficient of the basis monomial (xi a)^2 in H_10(T),
and let mu denote the coefficient of xi(xi a) in H_11(T). The free
E2 algebra and the top formulas imply

    lambda beta = mu,    mu Sq_*^2 = 0 on H_13(T).

To check the first identity, beta xi(xi a)=(xi a)^2. Among all other
top generators in degree11, xi d and xi e have Bocksteins d^2 and
e^2. Bocksteins of bracket generators contain a bracket factor, so
cannot contribute the pure monomial (xi a)^2. A product could do so
only if some degree6 factor had Bockstein with a xi a component.
The degree6 basis listed above has no such element.

For the second identity, Steenrod operations of products stay
decomposable, and operations of bracket generators retain a bracket
factor (after expanding the derivation law). The only remaining
possible degree13 generators are top operations xi z for degree6
Lie generators z. Their Sq_*^2 is xi(beta z)+{z,Sq_*^2z}. The latter
term has a bracket, while beta z has no xi a component. Thus there
is no xi(xi a) term. Equivalently, in the free restricted Lie basis,
the pure restricted power of the single label a is independent of
the bracket basis elements.

Steenrod naturality now forces

    lambda g(C^2)
      =lambda beta Sq_*^2 g(Q^8 C)=0.

But lambda(g(C)^2)=lambda((xi a)^2)=1. Therefore every full extension
has a nonzero Pontryagin multiplication deviation. In particular no
H-map extension exists, even if no preservation of Dyer--Lashof
operations was assumed. This remains consistent with the original
problem, which permits arbitrary pointed maps.

## 5. Current finite-stage boundary

The independent compactness and connectivity arguments are in
`I_eta_attachment.md`. They show that a genuine negative answer is
detected at a finite stabilization stage and a finite relative subpair.
The quotient X/S^3 and homotopy-pullback construction gives an extension
of the canonical second-stage map over relative cells through dimension11.
The first possible obstruction is therefore in relative dimension12.

The low E2 table above does not decide that obstruction. In particular,
the double-loop Hurewicz class a^2 has {a^2,a^2}=0 by the Browder
derivation law. This cannot detect a possible two-torsion Whitehead
square of the corresponding degree6 homotopy class. Moreover even a
failure of the canonical second-stage choice would not exclude another
ordinary extension with the same prescribed unit restriction.

No full eta-extension, no all-choices finite-stage obstruction, and no
nontriviality of P_(Q Sigma B)(Sigma^2 B) is claimed.

## 6. What the abelian-group structure does and does not supply

Since B=Omega K(F_2,3), the Ganea evaluation sequence is

    Sigma(B smash B) -> Sigma B -> K(F_2,3).

After looping, its section is the suspension-loop unit on B, giving
Omega Sigma B equivalent as a space to B times Omega Sigma(B smash B).
This identifies a concrete Hopf-construction route, but suspending this
fiber sequence does not give a fiber sequence for Sigma^2 B. No map
Sigma^2 Q Sigma B -> Sigma^2 B has been obtained from it.

There is a concrete obstruction to the simplest proposed factorization.
The map g_0 does **not** factor through the evaluation
e:Sigma B -> K(F_2,3). Write t in degree3 for the fundamental class of
K(F_2,3). Its degree6 cohomology is spanned by t^2 and Sq^2 Sq^1 t.
The evaluation pullback sends these to 0 and sigma w, respectively.
Therefore e_* kills sigma e, where e is the B-homology class dual to uv.
But the low table gives g_0*(sigma e)={a,b}, a nonzero free E2
homology class. Thus there is no map K(F_2,3) -> T whose composite
with this evaluation is g_0. The Hopf-construction/fiber contribution
cannot simply be discarded. This conclusion does not exclude a
factorization through Q Sigma B.

Coherent abelian multiplication alone cannot prove such an extension
for every B. Take B=S^1=K(Z,1), which is already an infinite loop space.
An extension would give Sigma^2 Q S^2 -> S^3 restricting to the nonzero
eta_3:S^4 -> S^3. After 2-localizing the source and 2-completing the
target, this is impossible: the connective 2-primary infinite-loop
fiber of Q(S^2_(2)) -> K(Q,2) is BZ/2-acyclic by the Levy theorem used
in the manuscript, while completed finite spheres are BZ/2-null.
K(Q,2) is mod-2 acyclic, so its based mapping space into the double
loop of the completed sphere is contractible. Any positive Ganea
construction in the present case must therefore use additional
properties of K(F_2,2), rather than just its coherent multiplication.


## 7. Promoted finite-stage theorem: D.2.13

The coefficient audit in Section 4 was independently checked by simple_higher
and the root. It gives the stronger finite-stage assertion now written in
`sections/D2_hopf_extension.tex`. At C_4X the operation xi_3 C=Q^8 C
is top, so the exact CLM III.1.3 formula is

    Sq_*^2 xi_3 C = Q^6 C + lambda_3(C,A_0),
    beta Q^6 C=C^2,  beta C=beta A_0=0.

Therefore beta Sq_*^2 xi_3 C=C^2 even though the uncorrected top
Nishida equality is false in general. The target identity
lambda beta Sq_*^2=0 forces lambda G(C^2)=0 for every ordinary
G:C_4X -> Omega^2Y. A G restricting to the canonical double-loop
g_2 must instead give lambda G(C^2)=1. Thus canonical h_2 cannot
extend to S_4. No multiplicativity of G was used.

The finite positive range through relative dimension eleven and the
finite-stage/finite-subpair compactness reduction were independently
checked against `notes/I_eta_attachment.md` and incorporated in the same
claim. The top-operation formula was checked visually in the author scan
by both this agent and simple_higher. The direct source computation uses
only the g_0(C)=xi a entry of the table, whose AH and primitive-kernel
proof is included in full.

**Boundary at the time of D.2.13 (superseded below):** the full ordinary extension might alter the
primitive image of C^2. Neither this theorem nor finite-stage compactness
proves that any E_m is empty. D.2.4 remains Open.

## 8. The ordinary extension is now excluded: D.2.16

The subsequent proof in `sections/D2_eta_nonextension.tex` closes the
all-choices boundary for this particular Hopf attachment. For every
ordinary map G:C_4(Sigma B) -> Omega^2 Sigma^2 B, the coefficient of
xi a in G(sigma c) is zero. An actual multiplication-deviation map on
(Sigma B) smash (Sigma B), together with exact target cohomology
identities, reduces the assertion to a nine-dimensional Steenrod
calculation on H^8(B smash B). Both this agent and root independently
checked the target coalgebra interface and the complete source calculation.
The resulting contradiction excludes every extension of eta_2 smash B
at the fourth stabilization stage, and hence excludes a full Q Sigma B
extension. The positive canonical extension range through relative
dimension eleven remains valid.

The older open-boundary statements in Sections 4--7 record the state
before this additional argument and are not the current conclusion.
No survival through arbitrary subsequent nullification attachments,
and no nontriviality of P_(Q Sigma B)(Sigma^2 B), follows merely from
the exclusion of this particular Hopf attachment. D.2.4 remains Open.
