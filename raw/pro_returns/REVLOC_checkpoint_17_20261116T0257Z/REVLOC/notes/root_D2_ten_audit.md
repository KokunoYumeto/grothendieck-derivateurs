# Independent audit of D.2.22--D.2.24

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Root audit completed 15 November 2026, approximately 18:40 UTC.

## Target and exact scope

The reviewed target is the actual group pi9(T), T=Omega2 Sigma2
K(F2,2). It is computed using the four-connected cover E of the
three-connected double-loop fiber F. The loop counit retraction of
E, combined with the nine-connected Freudenthal unit, identifies
pi9(E) with its stable value. This argument is not valid with F in
place of E and is not used that way.

I checked the complete H10(F) basis and the operation table, the
integral order-eight configuration-chain calculation, both third
Bocksteins, the low Koszul ranks for E, the integral H9 injection,
and the complete stable cell-component presentation. The component
detectors are independent before being used to identify attaching
maps; no unmeasured torsion component is discarded. Both B5 and B6
have beta3 image N. Retaining just one gives the wrong extension
calculation, as the historical notes explicitly record.

The final presentation has generators p,x,y,s and relations
2p=2s=0, 2x=a p, 2y=b p, with a=b in {0,1}. The common bit is not
computed. Both possibilities have exponent at most four and the
same integral Hurewicz kernel, the nonzero order-two class s=rho nu.
All eta composites from the preceding actual homotopy group vanish.
These statements do not require selecting the common bit.

## Independently reopened primary interfaces

May 1968, printed p334, was opened directly from the author's PDF.
Only the general simply connected, finite-type, field-coefficient
Eilenberg--Moore convergence/Tor interface is used. Injectivity of
the base cohomology is not substituted for a collapse proof; all
positive low Tor groups are calculated explicitly.

Angeltveit--Rognes 2005, equation (8.4), printed p1279, was opened
directly. The formula eta on Ceta = i nu q gives the free-lift eta
composite after applying the degree-two quotient, not a guessed
Moore extension relation.

I read the author's original Clément thesis TeX for Sections 2.4
and 3.2. Section 2.4 proves the divided-power transversality used
for the order-four and order-eight Eilenberg--MacLane classes.
Section 3.2 explicitly writes d3(u^4)=u^2(uv+w). Its opening
Cartan-complex proof splits off the even-degree elementary factor
X' and factors of reduced homology exponent two. In odd degree
nine, X' has no reduced homology, and every tensor or Tor term
involving another factor has exponent two. This proves the exact
H9(B) bound used here. The introductory compressed exponent sentence
is not used to infer an odd-degree group without this derivation.

The CLM operation interfaces, Snaith splitting, and low stable
stems had been opened earlier and were rechecked against the stated
uses. The integral quadratic-chain retract is algebraic: it does
not assert a topological Moore retract of B.

## Actual square and universal unit obstruction

The exact relation Psi=Sq4(e6 dual)+Sq2(J1 dual)=0 follows by
evaluating on all eighteen H10(F) basis classes; both terms detect
exactly B4,B5. It is not a relation only on spherical classes.

For the actual canonical Browder square, D.2.22 leaves two possible
values, zero and rho nu. The ordinary cone of rho nu has Psi value
one on its new cell. The free E2-to-E3 attachment on the bottom
four-sphere has a class Q6(x4) with both relevant squares zero.
The map from C3 S4 to Q S4 is ten-connected, so the stable Nishida
calculation is valid in the required lower groups. Its pushout
therefore has Psi value zero. This identifies the actual square
as zero. The first James cell fixes the normalization with no
extra factor of two. It proves only the canonical summand's
relative ten-extension.

For every ordinary map Sigma B to T, the unit ten-class has Sq4
equal to the suspended w-label and Sq2 zero. The same exact Psi
relation forces its e6 coefficient to vanish. Thus the dangerous
pattern constructed through dimension nine cannot extend through
the unit ten-skeleton for any choices. This proof needs no target
homotopy-group computation, hidden secondary coefficient, H-map
hypothesis, or ordinary-map Dyer--Lashof naturality.

The full-Q-source corollary follows from the earlier first and
second Bockstein relations. It kills the k=2 commutator functional
on the entire relevant attachment homology group, not just on the
kernel of its linear part.

## Exact certificates and remaining mathematical obligation

`code/D2_ten_exact_certificate.py` checks the Smith invariants
(1,8), both relevant integral chain identities, all eighteen Psi
evaluations, four independent source Cartan tests, and all four
parameter cases of the final presentation. It checks 1,024 group
addition/Hurewicz identities and the order-two condition forcing
a=b. All pass. The earlier separate polynomial programs check the
seven polynomial basis vectors and twenty-one operation values.
These finite certificates do not replace any geometric argument.

The first simultaneous cone is still under investigation. An
individual attachment may have its commutator functional factoring
through its linear homology image, while attachments with different
factors can cancel linearly in a simultaneous wedge. A single
uniform factorization is required. Even that first-cone result
would not establish persistence through subsequent cones: their
new cohomology and operation relations must be controlled anew.
D.2.4 and D.3.2 remain Open.

## Layout verification

The initial new layout had one display exceeding the margin by
43.25752pt and invalid multi-column split alignments. They were
repaired in the source; failed logs are retained. The completed
178-page build has zero overfull boxes, zero exceeding 2pt, zero
missing characters, and no undefined citations. Pages 77--89 and
178 were rendered and visually read; all are legible and unclipped.
Bibliography pages 170 and 174 were also inspected; the continuing
entries are checked with the next bibliography update.


## First-cone extensions audited, approximately 18:54 UTC

D.2.25 passes independently: the complete primitive beta/Sq2-cycle
subspace in H8F is span(W,J2), so evaluation of Psi on the unit
u4-dual kills the entire exponent-three commutator functional.
The exponent-five assertion uses the actual bottom homomorphism
Z2 to Z4 rho; larger exponents have no input in the degree at issue.
The provisional fourth-exponent Moore basis error was withdrawn
and does not enter a numbered statement.

I fully read D.2.26 and its expanded note. The minimal AH degree
argument gives an actual natural loop-homology injection. The
coaction proves independence of lifts. The actual singular-AW/MV
proof gives the cochain secondary product, including the precise
common factor across a simultaneous wedge. The relative AH model
proves the exact suspended-source test and the per-vector comparison
theta-L in the image of one common target class. I independently
opened Halperin--Lemaire Section3.1 p300 and the entire proof of
Proposition7.4 p309 in the original Cambridge PDF, and verified
the stated model interfaces and characteristic-two scope.

I also fully read D.2.27 and the preceding research proof. The
path-spectral-sequence bidegrees, the product-dual d5, uniqueness
of the two lifts, and kernel of double suspension in degree12
all check. The second kernel is a mixed product of degrees5 and6;
its reduced coproduct is injective, so it cannot meet the first
suspension image. The remaining first kernel is the square of
the sole bottom class. The universal counit comparison normalizes
the actual secondary cup class once for all maps. All five source
witnesses were also checked by hand. Their consequences agree
with the separate full source calculation in D2_Qsource_primary.py.
This proves exact uniform k0 vanishing, not only per-cone safety.
Exponents1 and4 and later-cone persistence remain unresolved.


## Post-checkpoint09: mixed families and D.2.28--D.2.29

Root read the complete mixed-exponent addition to D.2.27. For a
suspended attaching map with exponent k>=2, the same universally
normalized class pulls back as the double suspension of G*(e6 dual).
Thus the earlier exponent-specific vanishing is genuinely compatible
with the unsuspended choice. Every mixed family using exponents
0,2,3,5,6,... has zero whole tuple in the exact D.2.26 criterion.
This does not include exponent1 or4 and does not propagate to later
cones automatically.

Root read every line of D.2.28 independently. The suspension ranges
H8W -> H7F (isomorphism) and H9W -> H8F (injection) follow from the
same connectivity calculation used in D.2.27. The full H8F table,
including its nonprimitive C and all products, gives exactly
Sq2(e6 dual)=J1 dual+J3 dual and beta(R dual)=J3 dual.
Therefore lambda9=Sq2 theta7+beta R8 is an actual full-space relation.
Its substitution into the suspended Psi relation uses the correct
cohomological Adem order Sq2 Sq2=Sq3 Sq1. Root recomputed all four
unit Cartan expressions and the independence of u5,w2,u2v2.
The full-source witness Q6C5 has Sq2 zero and Sq4 Q4A0, by the
explicit binomial coefficients in the ordinary source Nishida
relation. The last remaining functional is exactly alpha3 beta4,
not an unspecified arbitrary H7 class. Root also checked its claimed
algebraic compatibility with r8=alpha3 Sq2 alpha3. No full-H11W
bar-quotient model or space-map realization is required or asserted.

Root read every line of D.2.29 and independently opened Arkowitz's
primary publisher PDF, Definitions2.2--2.3 and Theorem2.4, pp10--13:
https://msp.org/pjm/1962/12-1/pjm-v12-n1-p02-s.pdf
The remark after Definition2.3 explicitly supplies the mapping-cylinder
construction for general based spaces; root added that qualification
to the manuscript to avoid a hidden locally-finite-polyhedron
restriction on K(F2,2). The exact unit is the generalized Whitehead
map [u4,idY]:Sigma5B -> Y. Only the primitive a,b labels enter its
homology calculation. No blanket formula on nonprimitive labels is
used; the previously tempting one is explicitly withdrawn in the
fibrations note. Its b value is k, the next homology suspension is
the tensor commutator, and the following one is zero. Hence the
exact D.2.26 cone criterion makes the old cup product nonzero.

The iterated counit formula for h_m,m<=4, and its compatibility are
ordinary adjunction triangle identities. The fourfold adjunct is the
actual E4 map Omega4 h0. Thus it preserves Q7 on B0, and two homology
suspensions carry that value to xi1(k). Root independently checked the
free-E2 basis proof that xi1(k) is not a first-Bockstein boundary:
outer restricted-square generators have odd degree, degree14 has
none, and Bocksteins of labels, products and ordinary Hall brackets
cannot acquire the independent outer square of k. The restricted-Lie
identity removes inner restricted squares without producing an outer
one. CLM ChapterIII's top Bockstein formula has the coefficient
(|z| mod2) on z squared, as printed. At C6, Q8B0 is below top and
beta Q8B0=Q7B0. Bockstein naturality alone then contradicts an
extension of the fixed C4 map. The source C5 formula would instead
have a Browder correction; it is retained and no C5 claim is made.

These two new theorems do not settle D.2.4: the once-suspended
product coefficient remains, an ordinary fourth-suspension extension
need not have the canonical C4 restriction, and subsequent cone
stages remain uncontrolled. Both source restrictions are explicit
in the claims, register and crosswalk.
