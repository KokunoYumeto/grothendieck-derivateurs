# The incoming fifth differential at the bottom sigma coordinate

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026. Status: proved. Root, axioms and source agents independently
read and passed the complete proof, including the even Q normalization and
the old-K intersection argument. The full manuscript is D.2.55,
`sections/D2_stable_d5.tex`. The statement concerns the target quotient in D.2.54, not the final
eighth differential or the image of the theta-zero source subgroup.

## 1. Statement and the exact finite model

Put L=Y<7> and use the reduced two-local sphere AHSS of D.2.54. The claim is

    d5:E5_(12,3) -> E5_(7,7)=Z4 is zero.                 (1)

In fact the bottom stable subgroup Z4 in pi14 of the eleven-skeleton injects
after every twelve-cell of the model is attached. This stronger finite-cell
statement avoids replacing an actual page-five source by raw homology.

The double counit Sigma²E->L is twelve-connected, as proved in
`I_counit_twelve_cells.md` and used in D.2.43. Realize the twice-shifted finite
stable cell model of D.2.22 through dimension twelve as an actual
six-connected CW complex P12. Its cells and their attachments through that
dimension are in the stable realization range, and the counit comparison
requires no relative cells below dimension thirteen. Thus this is a valid
choice of the twelve-stage for the calculation (1). A possible thirteen-cell
which cancels the suspended u5² sphere is retained at the next stage; it
cannot introduce a new relation among old pi14 classes at the twelve-stage.

Let Pj be its skeleta. The core through dimension nine is

    K=(M4 vee S8_r) union_(i7 eta7 + 2r)e9,
    M4=M(Z4,7),
    K/S7=S8_b vee M(Z2,8)_r.                           (2)

There is also the separate S9_R in P9. It contributes no stable pi14, since
pi5(S)=0. Unless explicitly called an ordinary cone calculation, homotopy
groups in this note are stable. The chosen groups pi11(P11) are also ordinary
groups, by six-connectivity and Freudenthal.

The shifted D.2.22t5--t12 computations give

    pi11(K)=Z8{s0} plus Z2{z},
    2s0=m4,  z=r nu8,
    q(s0)=(nu8, eta9²),                               (3)

where the second coordinate denotes the specified Moore coextension, not a
bare map to its top cell. The class m4 is the mod-four Moore coextension
whose pinch is 2nu8. After the ten- and eleven-cells, the complete old
torsion subgroup in pi11(P11) is

    V=(Z2)^5{s,z,tau,w eta10,j eta10}.                  (4)

Here s is the image of s0, tau factors through M(Z2,9), and w,j are the two
free ten-spheres. The integral Hurewicz quotient has free basis p,q,x,y with

    h(p)=4N',  h(q)=2Q,  h(x)=K1,  h(y)=K5.            (5)

The last two formulas use D.2.31's proved a=b=0. In particular the K1 and K5
eleven-cell attaching maps are actually zero in their stable-range group;
they can be chosen as free eleven-spheres. Any change of x or y preserving
its full cellular Hurewicz lies in V and disappears on doubling.

The bottom stable subgroup is exactly

    im(pi14 S7 -> pi14 K)=Z4{i7 sigma}.                 (6)

Indeed the degree-four Moore attachment quotients pi7(S)=Z16 by four. The
additional nine-cell has zero pi14 composite: its possible source is
pi14 S8=Z2{nu8²}, and (i eta7+2r)nu8²=0 because eta nu²=0 and 2nu²=0.
The old pi14(K) injects through all ten- and eleven-cell attachments, since
their attaching spheres have pi14 equal to the zero fifth and fourth stable
stems. This is an ordinary stable cofiber exact-sequence assertion. If one
uses actual homotopy instead, the same injectivity follows from the
Blakers--Massey comparison in `I_counit_twelve_cells.md`, with no omitted
mixed terms. We use the stable statement for (1).

## 2. The exact doubled N-lift composite

The following argument is the independently developed refinement in
`FGH_D2_universal_moore_composition.md`, Section 21. It is included in full
to specify the coextension choices.

Orient the N' eleven-cell so that its attaching map is n=i7 nu7. The map

    Cnu7=S7 union_nu7 e11 -> P11

has bottom alpha=i7 and top degree one on N'. Since pi11 S7=0 and nu7 has
order eight, pi11(Cnu7) has a unique element v8 with top degree eight. It is
the ordinary coextension of 8 identity10 across nu7.

Normalize p as in D.2.22t12, so its second- and fourth-square mapping-cone
detectors are zero. Both 2p and the image of v8 have integral Hurewicz 8N'.
Their difference is therefore in V. The five complete detectors in
D.2.22t10 are injective on V. The detectors of 2p vanish by the degree-two
cone map. Those of the image of v8 vanish by naturality, because Cnu7 has no
cohomology in degrees eight or ten, which are the inputs of Sq4 and Sq2 on
the new degree-twelve cone class. Hence the difference is zero:

    2p = image(v8) in pi11(P11).                       (7)

The ordinary source bracket is exactly

    {nu7,8 identity10,nu10}={4sigma'} in pi14 S7.        (8)

The opened Strickland author program declares
{nu5,8 identity8,nu8}=sigma''' (Toda Lemma5.13) and
E sigma'''=2sigma'', E sigma''=2sigma' (Toda Lemma5.14). Two actual
suspensions give the displayed value. Its full indeterminacy is zero:
nu7 pi14 S10 + pi11 S7 nu11, both involving the fourth stable stem.
This is an ordinary unstable bracket calculation, not a K-local substitute.

The ordinary cone composition formula and (7) now give

    (2p)nu11 = alpha(4sigma')=0 in pi14(P11).           (9)

The last equality holds before the twelve-cells: alpha factors through M4,
and (4 identity7) sigma'=4sigma' because S7 is an H-space. Equivalently the
cyclic Hilton correction is the image of [identity7,identity7]=0. Stabilizing
preserves (9). No assertion that p nu11 itself is zero is made.

## 3. The remaining nu composites and the even ell normalization

The already audited pure Moore calculation gives

    m4 nu11=0.                                        (10)

For completeness, the coextension formula places it in the image of
{4 identity7,2nu7,nu10}. Four suspensions of the defined bracket
{4 identity3,nu',nu6} in pi10(S3)_(2)=0 show that this bracket contains zero;
its only indeterminacy is <4sigma'>. Its bottom image in M4 is zero by the
same S7 H-space argument. Exact primary locators and the full cone proof are
in `EH5_Mukai5_3_audit.md`, Section 6, and the universal note Section 15.

It follows from (3) that s0 nu11 and z nu11 have order at most two. Their
images under the ORIGINAL quotient (2) are independent:

    q(s0 nu11)=(nu8²,*),
    q(z nu11)=(0,i8 nu8²).                             (11)

The unspecified second coordinate of the first row is immaterial. The
essential statement is that the first row has first coordinate nu8²
nonzero, while the second has first coordinate zero and second coordinate
i8 nu8² nonzero. The latter is nonzero because
pi6(S/2)=Z2{i nu²}, by the stable Moore cofiber sequence and pi5(S)=0.
Thus their span maps injectively under (2) and meets the bottom subgroup (6)
trivially. Transport this conclusion to P11 using the old pi14 injection
proved above. No injectivity claim is made for the changed quotient P11/S7.

Also

    tau nu11=0,
    w eta10 nu11=j eta10 nu11=0,                       (12)

because pi14 M(Z2,9)=pi5(S/2)=0 and eta nu=0.

We need the full order bound

    4q nu11=0.                                        (13)

D.2.22t11 explicitly allowed the replacement ell->ell+2n. Retain that bit:
write the Q attaching map as R eta9+2c n, c in {0,1}. Slide its eleven-cell
by 2c times the N' cell, obtaining Q'=Q-2cN', whose attaching map is exactly
R eta9. The resulting Ceta9 subcomplex supplies q0 with

    h(q0)=2Q-4cN'.

Since pi14(Ceta9)->pi14 S11 is an isomorphism (the surrounding sphere
groups are the zero fifth and fourth stable stems), q0 nu11 pinches to
2nu11 and has order four. The full Hurewicz coordinates give

    q-q0-cp in V.

Equations (9), (4), and the order-four bound for q0 nu therefore imply (13).
This accounts for the even n normalization; it does not assume an arbitrary
changed ell coordinate is still literally R eta9.

Finally 2x nu11 and 2y nu11 have order four. Their free-sphere choices make
this immediate from the order-eight third stable stem; changes in V vanish
on doubling. Under collapse of all cells below dimension eleven, their
coordinates on the K1 and K5 spheres are respectively 2nu11, and q nu11
has coordinate 2nu11 on Q and zero on the other eleven-spheres. The possible
N' adjustment in the auxiliary q0 disappears in the normalized q.

## 4. Every twelve-cell and the intersection calculation

The complete twelve-cell list is D.2.22t13--t15 shifted twice, with a=b=0.
After composition with nu11, (9)--(13) reduce it to generators

    s nu11,
    s nu11 + z nu11,
    q nu11 + s nu11,
    2x nu11,
    2y nu11.                                          (14)

Specifically B5 supplies s nu, T supplies s nu+z nu, B4 supplies q nu+s nu,
B3/B7 supply 2x nu/2y nu. B6, Z, B2 are zero. B1 repeats the B3 image;
the other cells are zero or repeat the same list. This uses all integral
boundary directions, not just the zero-boundary twelve-cells.

Suppose an integral linear combination of (14) belongs to the old bottom
subgroup (6). Collapse to the independent Q,K1,K5 eleven-spheres. The
coefficients of the last three rows must each be divisible by four, since
their respective coordinates are 2nu in Z8. Their whole images then vanish,
by (13), the order-two bound for s nu, and the order-four bounds for 2x nu
and 2y nu. The putative bottom relation is now a combination of s nu and
z nu. It lies in the original K image, whose map into P11 is injective on
pi14. The independent quotient coordinates (11) force both coefficients
even, so this remaining relation is also zero. Therefore

    <all twelve-cell nu composites> intersect
       im(pi14 S7 -> pi14 P11) = 0.                    (15)

The stable cofiber sequence for attaching all twelve-cells identifies the
kernel pi14(P11)->pi14(P12) with exactly those composites, since
pi14(vee S11)=direct sum Z8{nu11}; no extra Whitehead terms occur in spectra.
Thus (15) proves that the bottom subgroup Z4 survives unchanged through the
twelve-stage.

In the cellular exact couple, an incoming d5 at (7,7) is a bottom stable
class killed on adjoining the twelve-stage after its lower filtration
components have been removed. Injection of the entire bottom subgroup is
stronger than its vanishing. Hence (15) proves (1), regardless of further
restrictions on the page-five source caused by thirteen-cell d1 boundaries.

## 5. Scope and remaining work

Together with D.2.54, the only incoming differentials still capable of
changing the Z4 target before d8 are now d6 from (13,2) and d7 from (14,1).
Their higher-cell coextensions are not evaluated by this argument. The old
K9 has pi13=Z2{i nu²}, hence its eta and eta² composites vanish, but an
attachment involving later-cell lifts need not factor through that core.

The affine source ambiguity d8(H0) from D.2.54 is unchanged. No value of h,
of the actual alpha sigma', or of the final stable Hurewicz pairing follows
from this target-page refinement alone.

Primary inputs are the already opened D.2.22/D.2.31 sphere/Moore formulas,
Strickland's original author program at https://strickland1.org/toda/Toda.m
(sigma''' declaration and its two successive suspension relations), and the
cellular exact-couple construction of Adams Part III Section 7 used in
D.2.54. Original Toda book pages are not represented as opened.
