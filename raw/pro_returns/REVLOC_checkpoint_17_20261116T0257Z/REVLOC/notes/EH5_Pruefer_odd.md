# Odd-primary resolution of the Pruefer stable ideal

**Subsequent all-prime result:** D.2.15, proved in `sections/D2_CPinf.tex`
and audited in `notes/EH5_CPinf_detector.md`, removes the eta obstruction
at 2 and proves loc(Sigma-infinity CP-infinity)=Sp. The Pruefer ideal is
therefore loc(S/p) at every prime. This note retains the eta-zero input
and its original odd-primary application.

Written 2026-11-15. The argument was independently checked by
root and the axioms/derivators agent; the local-system orientation step
is included explicitly below. Numbering and manuscript integration are
being coordinated with root.

## Statement

Let D be the reduced suspension spectrum of CP-infinity. If R is an
E1 ring, F(D,R)=0, and the stable Hopf element eta has zero image
in pi_1 R, then R=0. In particular, for every odd prime p,

    loc(D smash S/p) = loc(S/p).

By the previously established reduction this also computes

    loc(Sigma-infinity B(C_{p^infinity})) = loc(S/p)

for odd p. Thus the Pruefer generator has the full finite p-primary
thick part at odd primes. This argument alone does not settle p=2.

## The two Euler cofiber sequences

Write G=S^1 and let V=C be its standard one-dimensional complex
representation. In the stable category of spectra with G-action the
unit-sphere inclusion gives the Euler cofiber sequence

    G_+ -> S -> S^V.

Taking homotopy orbits gives

    S -> Sigma-infinity BG_+ -> Th(L),

where L is the universal complex line over BG=CP-infinity. The first
map is induced by EG=EG times_G G -> BG; since EG is contractible,
it is the inclusion of a basepoint up to homotopy. Therefore

    Th(L) = D.

Now tensor the equivariant Euler sequence with S^{-V}, then take
homotopy orbits. The result is

    S^{-2} --j--> Th(-L) -> Sigma-infinity BG_+ --delta--> S^{-1}. (1)

The left object is S^{-2} because G_+ smash S^{-V} is induced from
the underlying fiber S^{-2}. The map j is the inclusion of a Thom
fiber. More formally, in local systems over BG the map from the free
G-object is the counit from the left Kan extension of its fiber at
the chosen basepoint; applying the colimit functor gives precisely
the canonical map from that fiber to the Thom colimit. No assertion
about Eilenberg--Moore convergence enters these constructions.

These are also the standard circle-transfer sequences. The transfer
fiber is identified explicitly in Madsen--Schlichtkrull, *The circle
transfer and K-theory*, introduction, first displayed homotopy
fibration (opened original author preprint):

https://data.math.au.dk/publications/pp/1999/imf-pp-1999-17.pdf

The restriction delta to the basepoint sphere is a stable map
S -> S^{-1}, hence belongs to pi_1 S=Z/2. It is the Hopf class eta
(its sign is immaterial). For the odd-primary conclusion it suffices
that this group is 2-torsion; no identification of its generator is
needed.

## Extending the unit

Let u:S^{-2}->Sigma^{-2}R be the shifted unit. The obstruction to
extending u along j in (1) is

    Sigma-infinity BG_+ --delta--> S^{-1}
      --Sigma u--> Sigma^{-1}R.                          (2)

Since BG_+=S wedge D stably, the assumption F(D,R)=0 implies that
restriction to the basepoint induces an isomorphism

    [Sigma-infinity BG_+,Sigma^{-1}R]
      -> [S,Sigma^{-1}R].

The restriction of (2) is the image of eta in pi_1 R, which is zero
by hypothesis. Hence (2) is nullhomotopic. Exactness of mapping out
of the cofiber sequence supplies a map

    t:Th(-L) -> Sigma^{-2}R

whose restriction to the chosen Thom fiber is u.

## Why this is a genuine Thom orientation

The cohomology class t is used through the Thom colimit adjunction,
not through a bare claim that cohomological information determines
all twists. After extending R-linearly, it is a map

    R smash Th(-L) -> Sigma^{-2}R.

The left side is the colimit of the local system of invertible
R-modules obtained by tensoring the sphere local system S^{-L} with
R. The map therefore corresponds to a natural transformation

    R smash S^{-L} -> constant(Sigma^{-2}R)

over BG. Its component at the chosen basepoint is the identity of
Sigma^{-2}R, because t extends the unit. BG is connected. For every
other point, a path to the basepoint identifies the two components
by equivalences and by naturality. Every component is consequently
an equivalence. A natural transformation in a functor category is
an equivalence exactly when all its components are equivalences.
Thus t trivializes the full R-line local system, including its
higher coherences.

This is precisely the orientation criterion in Ando--Blumberg--Gepner--
Hopkins--Rezk, *An infinity-categorical approach to R-line bundles,
R-module Thom spectra, and twisted R-homology*, Journal of Topology
7 (2014), 869--893, Definition2.20, Definition2.22, Theorem2.24;
the Thom colimit and adjunction appear immediately before those
statements. The original paper was opened at

https://www.math.columbia.edu/~thaddeus/blumberg/5.pdf

The E1 strengthening uses left/right module duality instead of
a commutative Picard groupoid. Applying F_R(-,R) pointwise to
the left-module equivalence gives an equivalence of right-module
local systems S^L smash R = constant(Sigma^2 R), because sphere
lines are dualizable. Taking Thom colimits and
then the augmentation BG_+ -> S gives a map

    Th(L)=D -> Sigma^2 R

restricting to the unit on the bottom Thom fiber S^2. The assumption
F(D,R)=0 makes this map null. Its restriction is therefore null,
so the unit S->R is null. Unitality implies id_R=0, hence R=0.

## Applying the exact local-unit criterion

The preceding result excludes every nonzero derived-p-complete
CP-infinity-null E-infinity ring when p is odd: multiplication by
2 is invertible on a derived-p-complete spectrum, so eta maps to
zero. The fully proved criterion in EH5_Pruefer_transfer.md says
that such a ring exists exactly when loc(D/p) is proper inside
loc(S/p). Therefore equality holds at every odd prime.

The final manuscript is sections/D2_Pruefer.tex, claim D.2.14. Its
proof includes the complete exact local-unit criterion and the
Pruefer-to-CP-infinity ideal comparison, so it is self-contained.

For p=2 this argument identified the additional obstruction:
a nonzero CP-infinity-null local unit would have eta nonzero. It
does not justify replacing R by R/eta as a ring, or claiming that
eta acts trivially on the finite spectrum C eta. Those require
separate arguments and are not asserted here. The required separate
argument is now D.2.15: the bottom reduced transfer kills nu_R, which
makes eta vanish on R smash Ceta, and its finite endomorphism ring
then brings the eta-zero detector back into play.
