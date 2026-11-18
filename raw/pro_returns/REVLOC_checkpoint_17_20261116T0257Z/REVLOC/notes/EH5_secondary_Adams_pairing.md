# The degree-nine relation and the actual Adams differential

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Proved as D.2.61. Root and the axioms reader independently passed
the complete final manuscript. The simple reader is auditing the final
actual-operation input; its constituent lemmas were already independently
checked. Root and the fibrations reader independently checked the
track comparison below. No conclusion about the full D.2.4 nullification
map follows from this calculation alone.

## 1. A direct four-term certificate

Let M=H*(L;F2). The actual bottom a7 satisfies Sq1 a=Sq6 a=Sq8 a=0.
The Adem relation

    R=Sq1 Sq8+Sq2 Sq1 Sq6+Sq8 Sq1=0

gives the normalized bar two-cycle

    r=[Sq1|Sq8]a+[Sq2 Sq1|Sq6]a+[Sq8|Sq1]a.

Its differential is the product relation plus the three inner-operation
terms, hence zero. In the declared left Milnor convention its dual
functional has exactly four supported coordinates:

    [xi1|xi1^8]a, [xi1^3|xi1^6]a,
    [xi2|xi1^6]a, [xi1^8|xi1]a.

It pairs one with the bottom h0h3 cycle. The authored script
`code/EH5_secondary_relation_certificate.py` checks all 166 incoming
columns of the complete actual degree-fifteen input and saves every
column and supported term. The symbolic relation already proves the
identity independently of those matrices.

## 2. Actual secondary representative with controlled fiber restriction

Write H=HF2. The fiber P of

    (Sq1,Sq6,Sq8):Sigma7 H -> Sigma8 H + Sigma13 H + Sigma15 H

has a secondary map to Sigma15 H, obtained from a chosen null of the
composite with the row (Sq8,Sq2Sq1,Sq1). Its fiber restriction is the
loop of that row. This is the usual stable universal construction.

Let F=hofib(Sq6 rho:K(Z4,7)->K(F2,13)). Choose based nullhomotopies
of Sq1 rho and Sq8 rho on the BASE K(Z4,7): the first exists by the
mod-four lift, and the second by instability. Combine them with the
tautological Sq6 path. This gives an actual map F->Omega-infinity P.
The resulting class phi15 restricts on K(F2,12) to EXACTLY
Sq2Sq1 iota12. The other two chosen nulls restrict constantly there;
there is no unconstrained Sq3 iota12 term.

Any actual mod-four lift of a7 on L, with a chosen null of Sq6 a7,
gives L->F. Double looping F gives K(Z4,5) times K(F2,10), since
Sq6 on a degree-five class is zero. There are no mixed products in
degree thirteen. Thus sigma²phi is Sq2Sq1 z10 plus a class from
K(Z4,5). Serre's original Theorem4 gives that the latter is a sum
of positive-primary images of x5 and y6=rho beta4(x5), and products.
Both x5 and y6 pull back from double suspensions of actual L classes.

## 3. Primitive preimages and the exact zero evaluation

Double homology suspension H13E->H15L is onto by D58. Every class
has a primitive preimage: all degree13 reduced diagonals have only
5+8 and6+7 bidegrees, and the nine products uH8E and H6E H7E
independently realize their symmetric tensors. Those products vanish
under double suspension.

For a primary-annihilated class x in H15L, let z be such a primitive
preimage. Sq2 z is primitive and belongs to the D56 kernel
<uD,uE6,xi u> in H11E. The two product diagonals exclude the first
two terms. The xi-u coefficient is zero in the ambient free E2
model: the only restricted inputs of degree six are f,x,{a,b},
whose Bocksteins are respectively0,d+e,0. The top Nishida formula
cannot produce the outer xi u, and labels, ordinary Lie words and
products cannot produce that outer generator. Injection H11E->H11T
therefore proves Sq2 z=0. No degree13 cover-edge theorem is used.

The K(Z4,5) part of sigma²phi pairs zero with z: its products vanish
by primitivity and its positive-primary terms are suspended from L
and vanish on x. The fiber term evaluates as beta_* Sq2_*z=0.
Hence one actual representative Phi_R(a7) pairs zero on every
primary-annihilated H15L class. Its indeterminacy consists of
positive-primary images on L and is also annihilated by such classes.

## 4. Exact pairing with Adams d2

Use the nonminimal free bar resolution P_i of M. It is realized by
the ordinary GEM Adams coresolution (equivalently, take the standard
free resolution and its coherent comparison to that coresolution).
Write X=Sigma-infinity L -> A0 -> A1 -> A2, with actual zero tracks
eta0 for d1 g0 and eta1 for d2 d1, satisfying eta1 g0=d2 eta0.

In the free resolution,

    d_P([a|b]m)=a[b]m+[ab]m+[a](b m).

Thus the r-coordinate of d2 is exactly the row(Sq8,Sq2Sq1,Sq1)
on the three A1 coordinates of degrees8,13,15. Choose the relation
null H of this row on A0 to factor through the bottom Sigma7 H
coordinate. The difference eta1_r-H is an actual stable map
q:A0->Sigma15 H. Coherence says

    g0* q = Phi_R(a7)

for the value defined by eta0. This is the point where the actual
nullhomotopies, rather than primary relations alone, enter.

Represent x in Ext^(0,15) by c:S15->A0 and choose gamma nulling d1c.
Baues--Jibladze Eq4.1/Th4.2 and Th7.3 identify the Adams d2 with
the glued track eta1 c + d2 gamma. Its r-coordinate is
eta1_r c + row gamma. The relevant gamma components map S15 to
Omega Sigma8 H, Omega Sigma13 H, Omega Sigma15 H, all zero. The
bottom component c:S15->Sigma7 H has a unique null in the relevant
track range, since pi15 and pi16 of Sigma7 H are zero. Consequently
Hc contributes zero after these null identifications. What remains is

    <r,d2 x> = c* q = <g0* q,x> = <Phi_R(a7),x>.

Changes in the primary nulls give precisely the three positive-primary
indeterminacy terms. A change in the relation null gives a degree-eight
primary operation on a7. All pair zero with x. The formula is thus
independent of every such choice. It is a genuine track-level Adams
comparison, not an inference from matching degrees or from a primary
cobar calculation alone.

## 5. Consequences and limits

The pairing is zero on the whole incoming Adams d2 image and one on
the bottom h0h3 image. Therefore the latter cannot be hit. Sphere
naturality prevents outgoing differentials; later incoming sources
have negative filtration. Connective finite-type Adams convergence
gives a nonzero stable bottom2alpha sigma in pi14^s L.

The entire bottomZ4 in the stable AHSS survives: any nonzero incoming
d8 subgroup would contain twice its generator and kill this actual
bottom stable class. There is no lower cell filtration in total14
into which this bottom image could disappear. Thus d8=0 on the full
source at (15,0), and the D54 detecting integral class survives.
D51 then gives h_M l4=0. D53 gives2alpha sigma'=0, while its stable
image2alpha sigma is nonzero; hence q=alpha sigma' has exact order2.
This settles the specified Moore composite, not the entire fourth-
suspension extension or the original D2.4 nullification test.

## Primary source audit

- Adams1960, *On the Non-Existence of Elements of Hopf Invariant One*,
  https://yifeizhu.github.io/7064/Hopf-secondary.pdf ; original primary
  scan, Section3.6 pp68--74, especially axioms pp69--70, Theorems3.6.1
  and3.6.2, Lemma3.6.3 pp71--72. The universal-fiber restriction and
  uniqueness up to a primary operation were read directly. Root
  independently opened the same section and Section3.8.
- Baues--Jibladze, *Secondary derived functors and the Adams spectral
  sequence*, https://arxiv.org/pdf/math/0407031 ; version3, 6 July2004.
  Section4 Eq4.1/Theorem4.2, printed pp13--15, and Section7 Theorem7.3
  and complete proof, printed pp19--21, identify the glued-track
  differential with actual Adamsd2. Root independently read Sections4,
  6 and7. No secondary algebra algorithm is substituted for this proof.
- Serre1953, existing I_Serre1953, original Section2 no11 Theorem4,
  printed pp204--205, opened directly by root and the fibrations reader.
  Its higher coefficient generator is rho beta4 of the mod-four class.
