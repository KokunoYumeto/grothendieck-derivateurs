# The genuine eta attachments in the binary C2 Moore layer

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
15 November 2026, independently checked with simple_higher immediately
before checkpoint14. Exact finite source normal form, followed by
the subsequent actual normalization and doubled integral comparison.
Sections 7--8 identify the doubled commutator with the loop Hurewicz
image of the specified obstruction and prove that this image is zero.
They do not evaluate the obstruction in homotopy or the integral
cohomology square. Section 4 was added on 16 November after the root
supplied the six-suspension realization range; its lower-weight
calculation independently agrees with simple_higher.

Put `M=M(Z/2,2)` and

\[
 D=D_2^{(2)}M=(C_2(2)_+\wedge M^{\wedge2})_{C_2}.
\]

This is the actual binary extended-power space, equivalently the
homotopy mapping torus of interchange on `M smash M`. It starts in
dimension four and has a finite cellular model through dimension
seven. Its occurrence as a Snaith weight in `C_2M` is a stable
splitting; this does not give an ordinary inclusion `D→C_2M`.

## 1. The specified integral coordinates

Retain the root's fixed cellular chains, rather than replacing them
by unnamed abstract homology generators. With `|a|=2`, `|b|=3`,
and `db=2a`, write

\[
 U=e_1aa,\quad H=e_1ab,\quad J=e_1ba,\quad Z=e_1bb.
\]

The exact equations are

\[
 dH=ab-ba-2U,\qquad dJ=ba-ab-2U,
\]
\[
 D_6=-H-J,\qquad V_6=bb-H+J,
 \qquad dD_6=4U,\quad dV_6=0,\quad dZ=2V_6.
\]

In particular

\[
 V_6=bb+D_6+2J.
\]

The root's `code/D2_C2_Moore_integral_chain.py` and its saved PASS
certificate give the explicit unimodular change of bases and the
cancellation of the unit pair. The remaining integral homology is
`H4=Z/2`, `H5=Z/4{U}`, `H6=Z/2{V}`. The certificate by itself
makes no stable splitting claim.

## 2. Steenrod data and the stable cell normal form

Write `P4=a²` for the bottom class and `B5=ab` for its first
Bockstein predecessor. Modulo two, the six surviving classes have

\[
 \beta B=P,\quad \beta Z=V,
 \quad Sq_*^2D_6=0,\quad Sq_*^2V_6=P,
 \quad Sq_*^2Z=U.
\]

All other second-square values in these degrees are zero. These
are the same restricted-square/Browder formulas already used for
the binary part of D.2.18: `D6={a,b}`, `V6=b²+{a,b}`, and
`Z=ξb`. The beta-two Moore-four pair is `(U,D6)`.

Let

\[
 C_1^6=\operatorname{cofib}
       ((2,\eta_4):S^4\vee S^5\longrightarrow S^4).
\]

The six-skeleton is

\[
 D^{(6)}\simeq C_1^6(P,B,V)\vee M(\mathbb Z/4,5)(U,D_6).
\]

The first factor's free class `γ_C∈π6 C_1^6` is normalized by
quotient coordinates `(0,2)`, hence has integral Hurewicz `2V`.
Its other possible component is the order-two `δ` detected by
the second square to `B`. The Moore-four summand contributes the
order-two bottom-eta class `i_Uη5`. Integral boundary `2V` and
the complete second-square vector of `Z` therefore identify its
seven-cell attachment as

\[
                 \gamma_C+i_U\eta_5.
\]

There is no `δ` component, because `Sq_*²Z` has zero `B`
coordinate. There are no Whitehead terms in this attaching degree:
the target is three-connected and its degree-six homotopy is stable.
Thus this finite normal form is also realized by an ordinary CW
model of the extended-power space. It is not the wedge of the
three Moore chain blocks: both displayed eta attachments matter.

## 3. The current target comparison boundary

The actual Browder map with the spherical `U:S5→T` gives a map
`Σ6 C2M→T` which lifts to the connected cover `E`. Its restriction
to the actual `U` sphere is null: after double adjunction it is
the Whitehead square of `α7:S7→Y`, and

\[
 [\alpha_7,\alpha_7]=\alpha_{7*}[\iota_7,\iota_7]=0
\]

because `S7` is an H-space. This statement concerns the actual
sphere before a stable weight projection.

After the corresponding homology suspension, the desired Moore
top-coordinate image is related to the integral mixed cycle
`u6 D7−D7 u6` in `ΩL`. The exact chain relation above retains
the correction `2J`. Neither the finite normal form nor the
vanishing of the actual sphere restriction identifies that correction
inside the cover. A stable Snaith projection must also retain any
lower-weight homotopy component of the chosen sphere, even if its
homology is pure weight two. No integral square or stable Hurewicz
conclusion is drawn from the abstract normal form alone.

## 4. The actual six-suspended inclusion and the exact U correction

The preceding stable-inclusion caution can be resolved for this
specific finite range. The stable Snaith inclusion of `D` into `R=C2M`,
after six suspensions, has source dimension thirteen and target
`Σ6R` seven-connected. Freudenthal therefore realizes it uniquely
as an ordinary based map

\[
 j_2:\Sigma^6D\longrightarrow\Sigma^6R.
\]

Write `j1` for the similarly realized linear inclusion. Composing
`j2` with the specified high Browder map and its connected-cover lift
gives an actual map

\[
 f_2:\Sigma^6D\longrightarrow E.
\]

The sphere representing `U` before weight projection is the double
adjunct of `i4 ν4:S7→Σ²M=P5(2)`. The linear Snaith projection is
the canonical stabilization `C2M→QM`. Consequently the linear
component of this particular sphere is **exactly** the bottom
stable class `iν`, not a general element of `π3(S/2)`. Its order
is at most two; no assertion that the whole Moore homotopy group
is cyclic is needed.

All weights at least three start in degree six, so they cannot
contribute to this degree-five sphere. In the binary layer itself,

\[
 \pi_5D\xrightarrow{\cong}H_5(D;\mathbb Z)=\mathbb Z/4\{U\}.
\]

Indeed the `C1^6` factor has zero fifth homotopy group because its
six-cell kills the bottom eta, while the Moore-four factor supplies
the displayed bottom group. The top seven-cell does not change it.
The integral Hopf-invariant-one normalization of `ν4` makes the
binary component the named `U`, up to the chosen common orientation.
After six suspensions the stable equality thus becomes the actual
homotopy-group equality

\[
 \Sigma^6(U_{\mathrm{actual}})
   =(j_1)_*(\Sigma^6 i\nu)+(j_2)_*(\Sigma^6U).
\]

Postcomposition by the high Browder map is a homomorphism on this
sphere homotopy group. Its value on the left is zero, since its
double adjunct is `[α7,α7]=0`. Its value on the linear correction
is also zero: the restriction of the high map to the linear bottom
`S8` is `λ1(U,a)`, whose actual vanishing follows from D.2.20's
injective mod-two Hurewicz map and the restricted-Lie identity
`{ξa,a}=0`. The composition with the subsequent stable `ν` is
therefore zero as well. It follows that

\[
                         f_2(U)=0.
\]

All vanishing statements here concern the specified actual Browder
map; no ordinary map is presumed to preserve operations.

## 5. What the null bottom does and does not force

Choose a nullhomotopy of `f2(U)`. The ordinary cofiber of the bottom
sphere inclusion has the explicit decomposition

\[
 D/S^5_U\simeq
       (C_1^6\cup_{\gamma_C}e^7)\vee S^6_D.
\]

This follows directly from the cell model: collapsing the Moore-four
bottom leaves its top sphere, and the `Uη` summand of the seven-cell
attachment becomes zero. Therefore the map restricted to the
Moore-four block factors through an actual sphere `S12→E`. Its
choice is determined only modulo `4π12E`, by the Moore Puppe
sequence. The top sphere is a free coordinate of this quotient;
the source eta attachments alone impose no order-two condition on
its image. In particular the exact chain comparison
`V=bb+D+2J` still requires compatibility of the specified nullhomotopy
on `dJ`. The genuine realization and exact lower-weight correction
remove an ambiguity about the bottom restriction; they do not remove
that separate integral compatibility term.

## 6. Matching the whole Moore-four restriction

Added 16 November 2026. The following stronger normalization was
independently read and passed by simple_higher. It still gives no
order bound for the top sphere factor in Section 5.

The actual sphere `U:S5→R` has order four. Indeed it is the double
adjunct of `i4ν4:S7→P5(2)`, and the Hopf--Hilton argument of
D.2.17 applies already in `P5(2)`: `4i4ν4=0`. Its image in `T`
has exact order four by D.2.18. Choose an extension

\[
 \mu_0:M(\mathbb Z/4,5)\longrightarrow R.
\]

Its top mod-two image is exactly `k={a,b}`. To check this before
mapping to `T`, the complete degree-six homology of `R` has basis
`a³,b²,k`. Primitivity excludes `a³`; `Sq_*²=0` excludes `b²`;
the second Bockstein to the nonzero `U` fixes the coefficient of
`k` to be one. Thus no choice of an ambient higher label is used.

Write `v` for the linear stable Snaith projection of `μ0`. After
desuspending its shifts, it is a stable map

\[
 v:\Sigma^3(\mathbb S/4)\longrightarrow\mathbb S/2
\]

whose bottom restriction is `iν`. A cofiber square, with left
vertical map `2ν` and right vertical map `ν`, gives one such
extension: it commutes since `2∘(2ν)=ν∘4`. Its pinch is `2ν` on
the top sphere. All extensions with this bottom differ by
`π4(\mathbb S/2)`. The Moore exact sequence and
`π4^S=0`, `π3^S_(2)=Z/8{ν}` identify this group with `Z/2`,
and its pinch is `4ν`. Therefore every possible linear projection
has

\[
                  qv=(2+4\epsilon)\nu\,q_4,
                       \qquad \epsilon\in\{0,1\}.
\]

The high linear Browder restriction `f1:Σ6M→E` has actual null
bottom by Section 4, so it factors through a sphere
`ζ:S9→E`. Every such factor has order at most two, because
D.2.31 computes `π9E` as an elementary abelian two-group. After
six suspensions the displayed pinch formula is in the ordinary
stable range of the sphere and Moore targets. It follows as an
actual composition that

\[
 f_1\Sigma^6v=\zeta(2+4\epsilon)\nu_9q_4=0.
\]

There is no omitted higher-weight contribution to `μ0`. Weight
three starts in degree six and has just its bottom Hurewicz class
`a³` there; a map from this Moore source into that five-connected
layer is detected by its top mod-two homology. That coordinate is
zero. Weights four and higher start in degree eight.

The quadratic projection of `μ0` is a same-bottom extension of
`U` into `D`. The normal form above gives

\[
                  \pi_6D=(\mathbb Z/2)\{\delta,t\},
                      \qquad t=i_U\eta_5.
\]

Consequently its difference from the specified Moore summand
inclusion is a top-sphere shift by `εδ+ε't`. On the six-skeleton,
modify the Moore inclusion by this shift and leave `C1^6` fixed.
The modification fixes `U` and therefore preserves the complete
seven-cell attachment `γ_C+i_Uη5`. It extends over that cell
and induces the identity on integral homology, hence is an actual
self-equivalence of `D`. Retuning `j2` by this self-equivalence
aligns the entire quadratic Moore restriction with `μ0`.

After applying `f`, the linear correction is zero by the calculation
above, and there is no higher-weight correction. Thus the finite
source can be normalized so that, on its entire Moore-four block,

\[
 f_2\big|_{\Sigma^6M(\mathbb Z/4,5)}
       =\lambda_1(U,\mu_0)
\]

as actual homotopy classes. This is a normalization of the genuine
Moore restriction; it does not fix a compatible nullhomotopy on
the noncycle `J`. In particular the free-sphere coordinate and the
even `2J` term in Section 5 are still retained. The homology-identity
self-map need not preserve a separately chosen chain-level
nullhomotopy, so no chain equality is inferred from its existence.

## 7. The doubled integral commutator is the loop Hurewicz obstruction

Added 16 November 2026. The chain-choice calculation below has
passed simple_higher's independent audit. The primary odd-Hurewicz
normalization is opened explicitly at the end of this section.
The result identifies the unresolved even term; it does not set it
to zero.

Use `L=Y<7>` and write `M4=M(Z/4,7)`. Let `a6` be a cycle in an
actual Pontryagin differential graded algebra for `Omega L`
representing the specified bottom generator, and choose `b7` with
`db=4a`. Put

\[
                    z_L=ab-ba\in H_{13}(\Omega L;\mathbb Z).
\]

The names here distinguish this homology commutator from the
cohomology class `z8` in D.2.47. In particular
`H7(Omega L;Z)=H8(L;Z)=Z/2` is an assertion about **homology**;
the integral cohomology group `H^8(L;Z)` is instead `Z/4`.
We claim the exact, orientation-independent equality

\[
 2z_L=h_{\mathbb Z}\bigl(\operatorname{adj}(h_Ml_4)\bigr)
             \quad\text{in }H_{13}(\Omega L;\mathbb Z).
 \tag{7.1}
\]

### 7.1 Independence of all top-chain choices after doubling

First `d(b²)=4(ab-ba)`, so `4z_L=0`. Suppose the chosen bottom
cycle changes to `a'=a+dv`, with `|v|=7`. Replacing the top chain
first by `b'=b+4v` changes the commutator by the exact boundary

\[
 a'b'-b'a'-(ab-ba)=d(vb+bv+4v^2).
 \tag{7.2}
\]

This uses `|a|=6`, `|b|=|v|=7` and the ordinary graded Leibniz
rule; it is a literal chain identity. Any remaining change in
the top chain is a cycle `r7`. It adds `[a',r]=a'r-ra'` to
the commutator. Since `H7(Omega L;Z)=Z/2`, there is an `R8`
with `dR=2r`, and

\[
                 2[a',r]=d(a'R-Ra').
 \tag{7.3}
\]

Consequently `2z_L` is independent of the bottom representative,
the chosen nullchain for four times that representative, and
the integral top-cycle addition. No evaluation of the noncycle
`J` is needed for this doubled comparison. An odd change of
orientation also leaves `2z_L` fixed, since its order is at most
two.

### 7.2 An actual Moore factorization of the specified map

Let `P5=P^5(2)` and `alpha_P=i4ν4:S7→P5`. The argument in
Section 6 gives `4alpha_P=0`, so it extends to some map
`mu0:M4→P5`. Let `c24:P8(2)→M4` be the suspension cofiber
map with bottom degree two and top degree one. The actual map
`-w=-[i4,id_P5]:P8(2)→P5` and `mu0 c24` have the same bottom
restriction `2alpha_P`, by the Hopf--Hilton relation. Their
difference therefore factors through the top pinch `q2:P8→S8`.
Since `q4 c24=q2`, changing `mu0` by the corresponding top-sphere
coaction makes

\[
                         \mu_0c_{24}=-w
 \tag{7.4}
\]

exact as actual homotopy classes. The comparison `c24` is a
suspension map, so this use of the Moore Puppe sequence has no
uncontrolled Hilton correction. Composing into `Y` and taking
the unique lift through `L` defines `mu:M4→L`. All sources in
this paragraph are six-connected, so those lifts and homotopies
are unique through the six-type quotient.

The D.2.43 natural quadratic boundary gives

\[
 c_{24}l_4=\pm\partial(2c_4),
      \qquad
 \ker(\pi_{14}M_4\to\pi_{14}^sM_4)
         =\mathbb Z/8\{\partial c_4\}.
 \tag{7.5}
\]

Together (7.4)--(7.5) identify the specified actual obstruction,
up to sign, with `mu partial(2c4)`.

### 7.3 The precise integral loop normalization

The James chain algebra of the suspension `M4` is

\[
 T(A_6,B_7),\qquad dB=4A.
\]

In degree thirteen its only words are `AB,BA`; in degree
fourteen the only possible boundary is that of `B²`.
It follows directly that

\[
 H_{13}(\Omega M_4;\mathbb Z)
     =\mathbb Z/4\{AB-BA\}.
 \tag{7.6}
\]

There is a stably trivial relative Whitehead generator of
`pi14 M4` whose mod-two loop Hurewicz image is the nonzero
commutator. This is an exact primary result, not a claimed
desuspension of a stable class: Zhu--Pan,
*Complexes equivalent to S^(2k-1)-fibrations over S^(2k)*,
arXiv:2508.13800v3 (13 April 2026), Theorem 1.7(ii)--(iii)
and Corollary 1.8, printed pp.6--7, with proof pp.8--9.
Their criterion Theorem 1.4 applies to this relative lift.
The order is eight, so (7.5) makes it an odd multiple of
`partial c4`. Hence

\[
 h_{\mathbb Z}(\operatorname{adj}(\partial c_4))
            =t(AB-BA),\qquad t\text{ odd}.
 \tag{7.7}
\]

The integral assertion follows from (7.6): its reduction is
nonzero precisely for an odd coefficient. Alternatively the
proof constructs a stably trivial Cohen element with its full
mod-four commutator coefficient, which gives the same conclusion.
The independent pinch-kernel presentation is also recorded in
Zhu--Pan, *Homotopy classification of S^(2k-1)-bundles over
S^(2k)*, arXiv:2508.14341v3 (13 July 2026), Lemma 2.2,
printed p.6. Both current primary PDFs were opened on
16 November; their bibliography keys are
`EH5ZhuPanComplexes2026` and `EH5ZhuPanClassification2026`.

The actual loop map `Omega mu` sends the James chains to some
allowed pair `a,b` with `db=4a`. Naturality, (7.5), and (7.7)
give the right side of (7.1) as `2t z_L`. Since `4z_L=0`,
that is `2z_L`. Equations (7.2)--(7.3) identify this result
with the doubled commutator for every allowed choice of the
specified integral chains in the target.

This proves (7.1). In particular the formerly unmeasured even
comparison is spherical, but it is not thereby zero. D.2.46
places its right side in the subgroup generated by the loop
Hurewicz image of `e=u4 E epsilon'`; it does not select that
image rather than zero when the remaining cyclic coefficient
is undetermined. The integral square and the full fourth-
suspension extension remain unresolved.

## 8. The doubled commutator vanishes in the actual connected cover

Added 16 November 2026. The actual desuspension and Toda argument
were obtained by axioms_derivators and independently checked by this
author and the root. The chain-choice comparison of Section 7 was
also independently checked by simple_higher. This is a vanishing of
the specified integral loop-homology class, not of the original
homotopy class.

Put `X0=Sigma B` and write `u3:S3→X0`, `u4=E u3:S4→Y`.
Section 16 of `FGH_D2_universal_moore_composition.md` computes

\[
 \pi_6X_0=\mathbb Z/2\{\beta_0\},\qquad
 E\beta_0=2\alpha\in\pi_7Y=\mathbb Z/4\{\alpha\}.
 \tag{8.1}
\]

In particular this suspension is injective. For clarity, the actual
source calculation is as follows. The Ganea fiber
`G=Sigma(B smash B)` of `X0→K(F2,3)` identifies `pi6 X0`
with `pi6 G`. Its six-skeleton is `M(Z2,5) wedge S6`, with
homotopy group `Z2{bottom eta} plus Z{C6}`. The two integral
seven-cycles `ac,ca` have zero free degree and nonzero second-square
detector, so kill exactly the bottom eta. The `bb` cell attaches
by `±2C6+bottom eta`. Thus `pi6 G=Z2`. In the first James pair,
the relative sixth group is `Z2=H3X0 tensor H3X0`, and the actual
Hopf-invariant-one representative alpha hits its generator. This
proves (8.1), including injectivity.

The already established Hopf--Hilton identities give

\[
 u_4E\nu'=4\alpha=0.
\]

This is the suspension of `u3 nu'`, so (8.1) implies the actual
unstable identity `u3 nu'=0` in `pi6 X0`.

The classical element `epsilon':S13→S3` belongs to the indexed
Toda bracket `{nu',2nu6,nu9}_3`, hence to the ordinary bracket
with those same three maps. Postcomposition naturality and the
just-proved zero put

\[
 u_3\epsilon'
   \in\{0,2\nu_6,\nu_9\}
   =\pi_{10}(X_0)\,\nu_{10}.
 \tag{8.2}
\]

The last equality retains the entire ordinary indeterminacy. With
the first map identically zero, a constant first nullhomotopy gives
the zero bracket representative; changing it supplies exactly the
composites of `Sigma nu9=nu10` with maps `S10→X0`. The other
indeterminacy is postcomposition by the zero first map and is zero.
Thus no assertion of uniqueness of the ordinary bracket is needed.

There is consequently an actual `t:S10→X0` such that, up to the
irrelevant common sign,

\[
 e=u_4E\epsilon'=(Et)\nu_{11}.
 \tag{8.3}
\]

Every map `S11→Y` and its homotopies lift uniquely to
`L=Y<7>`. Hence (8.3) holds for the unique lift of e to L and
factors that lift through `S11`. Its once-adjoint factors through
`Omega S11`, whose integral James homology is concentrated in
degrees divisible by ten. Therefore

\[
 h_{\mathbb Z}\bigl(\operatorname{adj}(e:L)\bigr)=0
                   \quad\text{in }H_{13}(\Omega L;\mathbb Z).
 \tag{8.4}
\]

This use of `S11` is essential. The evident factorization of e
through `S4→Y` only gives zero downstairs in `H13(Omega Y)`:
the bottom map `S4→Y` does not lift to L, and no injectivity of
`H13(Omega L)→H13(Omega Y)` has been assumed.

The lift of alpha already factors through `S7→L`, and
`H13(Omega S7;Z)=0` since the James generator has degree six.
Thus the once-loop integral Hurewicz image of `alpha sigma'`
is also zero. D.2.46 puts `h_M l4` in the cyclic subgroup
generated by `alpha sigma'+e`; the same is true after the unique
lift to L. Its once-loop integral Hurewicz image is therefore zero.
Equation (7.1) now gives the unconditional conclusion

\[
                         \boxed{2z_L=0.}
 \tag{8.5}
\]

The primary Toda interface was reopened directly in Strickland's
author note, <https://strickland1.org/toda/toda.pdf>, printed p.4
(definition of epsilon') and Proposition 2 on p.6, and in the
author program <https://strickland1.org/toda/Toda.m>, the declaration
`epsilonprime` with its explicit Toda VI(iv) locator. The indexed
bracket is used only for inclusion into the ordinary bracket;
all subsequent indeterminacy is accounted for in (8.2). This does
not claim that the original Toda book page was opened.

Finally, (8.5) supplies an actual integral chain `W14` in an
actual Pontryagin chain model with `dW=2(ab-ba)`. It removes the
previously undetermined even class represented by the noncycle-J
comparison. It does not prescribe the compatible higher relation
on W, nor the degree-fifteen Adams--Hilton differential that can
encode the degree-sixteen integral cohomology extension. Thus
neither `b8²=0`, the half-product's stable-spherical pairing, nor
`h_M l4=0` is inferred here. The full fourth-suspension question
remains open.
