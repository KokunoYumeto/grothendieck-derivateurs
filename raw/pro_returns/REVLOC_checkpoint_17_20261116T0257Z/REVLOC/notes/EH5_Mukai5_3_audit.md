# Exact Hurewicz and relative-torsion checks for Mukai Lemma 5.3

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026. Independent audit for the universal Moore-composition
route. Both checks below pass. Neither evaluates the remaining bottom
sphere coefficient or the full composite `h_M l_4`.

## 1. Primary statement and notation

The original scan of J. Mukai, *Generators of some homotopy groups of
the mod 2 Moore space of dimension 3 or 5*, Kyushu J. Math. 55 (2001),
63–73, was reopened directly:

<https://www.jstage.jst.go.jp/article/kyushujm/55/1/55_1_63/_pdf>.

Printed p.71 was visually inspected. Lemma 5.3 states

\[
 \widetilde\eta_4[\iota_6,\iota_6]
   \equiv i\widetilde{2\nu_7}\pmod {i\tau_5}.
\]

Here `A_5=S^4 cup_(2[ι4,ι4]) e^8`, `i:A_5→P^5(2)`, and
`C=widetilde(2ν7)` is the order-four summand of `π11 A_5` in
Lemma 4.1(iii), p.69. The same statement gives
`j τ_5=3[γ_8,ι_4]` in the relative group.

## 2. The retained tau coefficient is zero

Use the integral Adams–Hilton model

\[
 T(a_3,c_7),\qquad da=0,\qquad dc=4a^2.
\]

In degree ten its only words are `ac` and `ca`. Their differentials
are `−4a^3` and `4a^3`, respectively. There are no degree-eleven
words and hence no boundaries into this degree. Therefore

\[
 H_{10}(\Omega A_5;\mathbb Z)=\mathbb Z\{ac+ca\}.
\]

In the relative quotient of this chain model by `T(a)`, the two
degree-ten words are independent cycles. The relative Samelson
Hurewicz image of `[γ_8,ι_4]` is `ca+ac`: both shifted degrees
are odd, so the commutator has the plus sign. The absolute-to-relative
homology map takes `ac+ca` to that same sum and is injective here.
Consequently the exact relative equality for `τ_5` implies

\[
 h_{\mathbb Z}(\tau_5)=\pm3(ac+ca).
\]

The finite-order element `C` has zero integral Hurewicz image in this
torsion-free group. Its mod-two Hurewicz image is also zero, by
naturality of the coefficient map on the fundamental class of a sphere.

For the inclusion into `P^5(2)`, the mod-two James algebra is
`T(a_3,b_4)`. The degree-seven chain generator `c` maps to `ab+ba`.
One way to fix this assertion without silently choosing a top-cell
extension is to compare the canonical map `P^8(2)→A_5→P^5(2)`
with the actual generalized Whitehead map. They agree on the bottom,
so their difference factors through `S^8`. The two generators of
`π8 P^5(2)`, `widetildeη_4 η_6^2` and `i_5 ν_4 η_7`, have zero
once-loop Hurewicz in degree seven: they factor through `S^6` or
through `η_7:S^8→S^7`, whose corresponding loop homology group in
that degree is zero. Thus this difference cannot change the indicated
James-algebra coefficient.

It follows that the mod-two Hurewicz image of `i τ_5` is

\[
 a(ab+ba)+(ab+ba)a=a^2b+ba^2\ne0.
\]

On the other hand, the once-adjoint of `widetildeη_4:S^6→P^5(2)`
has degree five, in which the James algebra has no homology. Its
Whitehead square therefore has zero once-loop Hurewicz. Applying
Hurewicz to Mukai's congruence forces the coefficient of the order-two
class `i τ_5` to be zero. Thus the two-primary equality is exact:

\[
 \widetilde\eta_4[\iota_6,\iota_6]=iC.
\]

Since the actual bottom Moore eta-coextension maps to zero in
`Y=Σ²K(F_2,2)`, this supplies the corresponding exact vanishing of
the image of `iC` in `Y`. It does not identify a bottom-sphere
representative of `Cν_11`.

## 3. The composite C nu is genuinely a bottom image

The relative group on p.69 has two-primary splitting

\[
 \pi_{11}(A_5,S^4)\cong
 \mathbb Z\{[\gamma_8,\iota_4]\}
 \oplus\mathbb Z/8\{\widehat\nu_7\}.
\]

There is no need to infer the relative torsion coordinate from the
pinch alone. Identify this relative group with
`π10 hofib(S^4→A_5)`. Under this identification the characteristic
relative class `γ_8` is an actual sphere map from `S^7` to that
fiber. Postcomposition induces a group homomorphism on `π10 S^7`.
Hence `γ_8·ν_8` has order dividing eight. Its pinch is `ν_8`,
of exact order eight, so it has exact order eight and generates the
relative torsion summand. In particular it has no free mixed-bracket
coordinate.

The class `C` has order four, so `jC` is torsion. Its pinch is
`2ν_8`, and the pinch is an isomorphism on this relative torsion
summand. Thus, after matching the odd-unit generator convention,

\[
 jC=2\gamma_8\cdot\nu_8.
\]

To compose with `ν_11`, use the same actual homotopy-fiber model;
the relevant sphere composition is `2ν_7ν_10=0`. Equivalently
one may use its suspended relative notation. Therefore

\[
 j(C\nu_{11})=0,
 \qquad C\nu_{11}\in
 \operatorname{im}(\pi_{14}S^4\longrightarrow\pi_{14}A_5).
\]

This is a relative exactness conclusion, not an unstable covariant
exact-sequence assertion for a cofiber. It leaves the precise
combination of `ν_4σ′`, `Eε′`, and `η_4μ_5` undecided.

## 4. Scope of the earlier tentative Toda bracket

The exploratory bracket `⟨iν_7,4,2ν_10⟩` used
`i:S^7→M(Z/4,7)`, followed by the low target `K`. It was a
possible description of a twelve-cell `2pν` composite. It was
not a statement that the mod-two Moore element `l_4` belongs to
such a bracket in `P^8(2)`. No such containment is used above.
The proved D.2.45 fourteen-skeleton result already shows that
twelve-cell calculations alone cannot make the required class zero.

## 6. A different, exact Moore-four composite

Added 16 November 2026; independently checked by axioms_derivators.
This concerns the pure Moore-four space, not the closed `A5` route.
Let `M4=M(Z/4,7)` with bottom `i:S7→M4` and pinch `p:M4→S8`.
There is a unique class

\[
 m_4\in\pi_{11}M_4,\qquad p_*m_4=2\nu_8.
\]

The uniqueness follows from `π11S7=π4^S=0`; existence is the
coextension of `2ν7`, whose composite with the degree-four map is
zero. The standard actual cofiber definition of the Toda bracket gives

\[
 m_4\nu_{11}\in
 i_*\{4\iota_7,2\nu_7,\nu_{10}\}.
\]

The small bracket on the right contains zero. Indeed
`{4ι3,ν′,ν6}` is defined two-locally: `4ν′=0` and
`ν′ν6∈π9S3_(2)=0`. Its values lie in `π10S3_(2)=0`.
Suspending four times and using `E^4ν′=2ν7` gives zero in
the displayed bracket. Its full indeterminacy is

\[
 4\pi_{14}S^7+\pi_{11}S^7\circ\nu_{11}
       =\langle4\sigma'\rangle.
\]

The bottom inclusion kills this indeterminacy. In fact `S7` is an
H-space, so degree-four postcomposition on `σ′` is additive:
`(4ι7)σ′=4σ′`. The defining Moore cofiber gives `i(4ι7)=0`.
Consequently

\[
                         m_4\nu_{11}=0.
\]

No unspecific stable-zero remainder such as `i(2σ′)` remains in this
particular composition. The sphere inputs and the suspension relation
are the primary Toda data recorded in Strickland's author note and
`Toda.m`, directly reopened on 16 November at
<https://strickland1.org/toda/toda.pdf> and
<https://strickland1.org/toda/Toda.m>; the note's first-page example
explicitly records `π10S3_(2)=0` from Toda Proposition 5.15.
Signs of the chosen coextension do not affect this zero conclusion.

For the coupled low target `K`, this implies only
`2(s0ν11)=m4ν11=0`, since `2s0=m4`. It does not evaluate
`s0ν11`, `rν8²`, or the independent free-lift composites
`pν11,qν11,xν11,yν11` in the actual eleven-skeleton. Those
coordinates must remain in any twelve-cell matrix.
