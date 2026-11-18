# Exact order of the degree-eight spherical element

Status: proved, 15 November 2026. The complete proof is D.2.18 in
`sections/D2_seven_skeleton.tex`. The written proof has passed an
independent audit by the axioms/derivators agent; the separate source
quotient has also passed the simple/higher agent's audit.

Put B=K(F2,2), Y=Sigma²B and T=Omega²Y. The exact conclusions are

    pi5(T)=Z/4 {alphaBar},
    pi6(T)=pi8(Y)=Z/4 {rho},
    2 rho=alphaBar eta5 != 0.

Here alphaBar is the double adjunct of the bottom Hopf composite
u4 nu4. Every element rho with mod-two Hurewicz image

    r=b²+{a,b}+f+ac+a³

has order four and satisfies the same doubling relation. This includes
the actual rank-two-framed Pontryagin--Thom representative constructed
in D.2.17. Its order is established by the homotopy calculation, not by
assuming that a framed product embedding represents two-torsion.

## Decisive calculation

The bottom-class map T -> B has the unit section. Translation splits
T as B times its three-connected fiber F. Thus pi6(F) is stable. The
complete fiber mod-two homology in degrees 4--7 has dimensions
1,2,3,4. Its primary squares, first Bocksteins, and the explicit second
Bockstein beta2(b²)=xi a give integral groups
H4(F)=Z2, H5(F)=Z4, H6(F)=Z2².

Take a finite stable cell model through dimension eight, cancel all
odd-unit adjacent incidences, then truncate the eight-cells. This
preserves pi6 and removes extraneous seven-cells. Its six-skeleton is

    C_1^6 vee M(Z4,5) vee S6,

where C_1^6=cofib((2,eta):S4 vee S5 -> S4). The cofiber long exact
sequence injects pi6(C_1^6) into Z2{eta5}+Z{identity6} with image
Z2+2Z. Thus pi6(C_1^6)=Z{gamma}+Z2{delta}, with quotient images
(0,2) and (eta5,0). Integral degrees and Sq2 from the two five-cells
detect every possible seven-cell attaching component. There is no
unknown secondary invariant in this stable range.

The complete relations are

    gamma+t,  gamma+2rho+delta,  delta,  0,

with t the Moore bottom eta class. Their cokernel is exactly Z4,
with 2rho=t. The degree-five generator is alphaBar, so t=alphaBar eta.

## Source extension

The source quotient calculation is in `notes/I_seven_cell_quotient.md`.
It includes all four degree-seven source classes, including the
nonprimitive product A0 B0. Its only nonzero correction obstruction is

    alphaBar eta5+2rho.

The exact target relation cancels it. The construction therefore gives
an actual ordinary map on the seven-skeleton of Q Sigma B with the
six-dimensional D.2.17 values unchanged. Eight-cell and later extension
conditions remain open.

## Primary-source audit

* Oka, *Homotopy of the exceptional Lie group G2*, Proceedings of the
  Edinburgh Mathematical Society 29 (1986), 145--169, Section 2,
  equation (2.1), printed page 149, was opened directly at the original
  publisher PDF. It gives the first two stable stems and eta² != 0.
  Equations (2.2)(a)--(b) additionally give the Moore lift identity,
  but the manuscript uses the displayed cofiber exact sequence instead.
  Existing bibliography key: `I_Oka1986`.
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9BF563A8A92B6BF87DAA39E8DAD092BE/S0013091500017557a.pdf/homotopy-of-the-exceptional-lie-group-g2.pdf
* Cohen--Lada--May, Chapter III, Theorems 1.2--1.4 and 3.1--3.2,
  and the configuration-chain conventions in Lemma 3.10, p.232,
  are the previously opened primary inputs for the full operations
  table. The second Bockstein is proved by an explicit integral chain
  in D.2.17 rather than inferred from a primary-square pattern.
* Serre1953 Section 2 nos.8--9, Mahowald1964 Section 2.3/proof of
  Lemma6.1, and Snaith1974 Theorem1.1/Section2 are the opened exact
  source interfaces for the quotient's integral groups and cell counts.
* An earlier search opened Jin--Zhu, arXiv:2402.11226, Section4.2,
  equations(32),(35),(37), computing pi8(C_1^6)=Z2+Z4 and identifying
  the nondivisible bottom i nu4 eta7 summand in that low Chang complex.
  This does not settle the higher cells of Y and is not used as a
  premise of D.2.18. The fiber calculation bypasses that unstable
  higher-cell issue completely.
  https://arxiv.org/pdf/2402.11226

Full independent companion proof: `notes/FGH_D2_pi8_fiber.md`.
