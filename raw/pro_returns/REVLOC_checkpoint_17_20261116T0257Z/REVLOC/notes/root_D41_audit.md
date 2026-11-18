# Root audit of D.2.41

15 November 2026, 22:29 UTC. The complete final TeX proof passes.
The independent reader also passed it in notes/I_D41_audit.md.

The complete weight-three homology list in degrees 9--11 has the two
degree-ten Bocksteins equal to A cubed, and the sole degree-eleven
Bockstein equal to their sum. After an integral odd-unit normalization,
the ten-skeleton is M(Z2,9) wedge S10. One eleven-cell has boundary 2c;
even slides remove the other boundaries, preserving all mod-two square
vectors. A zero-boundary cell with nonzero Sq2 kills i eta. Thus pi10
is Z2 with nonzero Hurewicz, so a sphere whose mod-two homology is pure
weight two has no hidden weight-three stable component. Higher weights
start in degree twelve. This justifies isolating the quadratic component
of the actual sphere, rather than assuming the homology splitting detects
all stable components.

I reopened/read the original Morisugi--Mukai paper's Lemmas 2.7 and
2.8(ii) and their proof on printed p.523, including the Stiefel-cell
definition and the relative-pair exact sequence. The nu-squared lift has
nonzero stable pinch, whereas the l4 summand stabilizes to zero because
its suspension is a bottom Whitehead square. Hence the actual stable
kernel is Z4{l4}. The order-four quadratic projection forces the actual
fourfold adjunct to be plus or minus l4. This establishes the actual
order, not just a lower bound on it.

The difference of ordinary maps is taken in the loop-space target, with
a specified nullhomotopy on the Moore subspace, and hence factors through
the cofiber. Its unique lift to the five-connected cover is justified by
connectivity of that cofiber. The first stabilization at source dimension
eleven is surjective by Freudenthal and injective by the actual loop-unit
retraction; subsequent suspensions are in the bijective range. Therefore
the stable quadratic restriction is represented by an actual map into V,
and its value on the sphere is an actual equality in pi10V. Injectivity of
the suspension-spectrum map V->U is neither assumed nor needed.

The map 2id on the low Moore space factors through the top pinch and
either zero or i eta. Since the bottom is -2alpha and alpha eta=2rho,
this proves 2m=0. I reopened/read Arkowitz Proposition 3.4 and its entire
commutator proof on p.14. Its suspension hypotheses hold for S6 and
Sigma3 M. Thus the generalized Browder Moore map is zero. Its top-sphere
factor lies in 2pi10U by the Moore Puppe exact sequence; no vanishing of
that double is inferred. The Hurewicz image of the relevant relative
sphere consequently vanishes modulo two.

The source formulas beta Z=Y, Sq3 Z=Sq5 Z=0 then make the stated
beta+Sq3+Sq5 membership a sufficient target condition. The canonical
paired coefficient is one and the full infinite-loop-source coefficient
is zero by its Bockstein boundary; primitivity makes the difference
formula additive. D.2.36 excludes the alternative Moore top for all
dangerous entire-unit maps. The target membership itself and the value
h_M l4 remain unproved, and D.2.4 remains Open.
