# D.2.10 — stable sphere annihilation and finite targets

## Status and exact conclusion

The manuscript proof is in `sections/D2_stable_miller.tex`, claim D.2.10.
It proves

\[
F(\Sigma^\infty Y,\mathbb S)=0
\Longrightarrow
\operatorname{Map}_*(Y,K)=\operatorname{Map}_*(Y,K_{(p)})=*
\]

for arbitrary pointed Y, finite simply connected K, and every prime p.
Consequently R(ann S) is contained in W_S and so is R(I_p), where
I_p=loc Σ∞K(F_p,2) is the zero-finite-part ideal of D.2.6.
This excludes finite simply connected target tests as separators for that
candidate. It does not settle RT-fixedness or the adjacent Q-suspension chain.

Root proposed the Segal/Goodwillie route and the clean rational arithmetic
argument. `simple_higher` independently checked the structural proof and
specifically confirmed the genuine finite coefficient and rational-vector
steps. Root separately opened the decisive Segal input and is reviewing the
remaining cited interfaces.

The subsequent independent `fibrations_groups` audit read the saved proof
and reopened all cited primary interfaces. It passed every step, including
Moore duality in completion, the fixed sphere and splitting, the transfer,
the finite BG AHSS, rational arithmetic, genuine finiteness of the actual
coefficient, and arbitrary-source convergence. The transfer equivalence
can also be seen without a general completion theorem: its connective
cofiber has zero mod-p homology, hence its Moore cofiber is zero by stable
Hurewicz, so its p-completion is zero.

## Exact primary sources opened

1. Bergsaker–Rognes, *The Segal conjecture for smash powers*, J. Topology
   16 (2023), 567–587, DOI 10.1112/topo.12290.
   <https://arxiv.org/pdf/2207.13408>, version 2, Theorem 1.1, pp1–2;
   published HTML also opened.
   The theorem is explicitly a p-completed comparison from genuine fixed
   points to homotopy fixed points for finite p-groups. The introduction
   explicitly says B=S gives the genuine sphere S_P. This avoids any
   unsupported identification of I-adic and p-adic completions.
   Web refs: turn668view0, turn679view1.

2. Carlsson, *A survey of equivariant stable homotopy theory*, Topology
   31 (1992), 1–27, DOI 10.1016/0040-9383(92)90061-L.
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/carlsson-survey.pdf>.
   Corollary 2.3, print p11, gives the tom Dieck splitting; Section 3
   explains the spectrum formulation. Pages 9–10 discuss equivariant
   duality and transfer. Theorem 4.9 and the p-group remark were also opened.
   Web refs: turn665view0, turn666view1–2, turn675view1, turn684view1.

3. Arone–Mahowald, *The Goodwillie tower of the identity functor and the
   unstable periodic homotopy of spheres*, Invent. Math. 135 (1999),
   743–788. Existing key EH5AroneMahowald1999.
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/arone-mahowald.pdf>.
   Theorem 2.1, printed p755, is the layer formula using the dual of
   the finite partition complex. Its finite simplicial construction in
   Sections 1–2 supplies the specific action, rather than merely an
   underlying finite spectrum. Web refs: turn675view0, turn676view0.

4. Goodwillie, *Calculus II: Analytic functors*, K-Theory 5 (1992),
   295–332. Example 4.3, p321, proves the identity is 1-analytic.
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/goodwillie-calc2.pdf>.
   Web refs: turn679view0, turn684view0.

5. Goodwillie, *Calculus III: Taylor Series*, Geometry & Topology
   7 (2003), 645–711.
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/goodwillie-calc3.pdf>.
   Theorem 1.13, p665, gives convergence for a rho-analytic functor on
   spaces whose map to the base is (rho+1)-connected. Proposition 1.18
   supplies filtered-colimit preservation of layers. Section 8, pp703–705,
   independently describes the finite partition model.
   Web refs: turn670view0, turn674view0–1.

6. Cross-check only, not needed as an extra bibliography dependency:
   Arone–Ching, *Goodwillie Calculus*, arXiv:1902.00803, Theorem 1.17,
   Example 1.18, Definition 3.1 and Theorem 3.2.
   <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/arone-ching.pdf>.
   Web refs: turn670view1, turn671view2–3, turn674view2.

## Interfaces checked to prevent hidden changes of hypotheses

- All stable cohomotopy shifts are required. A vanishing degree-zero group
  alone is not the hypothesis.
- The p-completed genuine fixed sphere splits into the completions of the
  finitely many tom Dieck summands. The H=1 summand is BP_+.
- Completion of F(BP_+,S) is F(BP_+,S_p^): compute completion as the
  inverse limit of Moore cofibers, and use exactness/dualizability before
  taking the inverse limit. No unjustified commutation with a colimit.
- The Sylow transfer composite need only induce multiplication by the
  index on ordinary mod-p homology. No equality with that scalar map in
  stable homotopy is used. Invert the completed composite to obtain the
  actual retract.
- The bar resolution is finite in each degree, not finite in length.
  The reduced connective AHSS has a finite filtration in each total
  degree and yields finite |G|-primary stable homotopy groups.
- Rational spectra enter through a cofiber of S→product_p S_p^.
  The quotient (product Z_p)/Z is a nonzero Q-vector space. A Q retract
  gives HQ; every H of a Q-vector is a retract of a product of HQ.
  No arbitrary coproduct closure of coloc(S) is asserted.
- The p-local sphere is recovered by the arithmetic pullback with
  S_p^, HQ, and HQ_p. The reduced BG p-localization is its p-completion,
  by the already proved finite homotopy-group calculation.
- An arbitrary finite spectrum with a naive action is not declared
  genuinely finite. The particular coefficient is the genuine dual of
  a finite partition G-complex smashed with the finite G-complex K^k.
  Finite genuine orbit cells descend to classifying spectra BH_+.
- The tower converges for K_(p) even though it need not be a finite
  ordinary CW complex: it is simply connected, the identity is
  1-analytic, and the layer formula extends by filtered homotopy colimits.
- Map(Y,-) preserves the inverse limit for every Y. No finiteness or
  compactness of the source is inserted.
- The final inclusion is applied to the actual pointed cofiber C(f),
  exactly as R is defined. Stable sphere-annihilation forces reduced
  H_0 to vanish; nonbasepoint components would split off a sphere.

## Related primewise note, kept out of a new theorem

The D.3.8 argument also has a torsion primewise extension: split connected
torsion infinite-loop generators into their p-primary spectral factors;
the weak product is a filtered colimit of finite products, and every
factor is a retract. The primewise stable ideals are determined by the
whole stable part. Applying the two D.3.8 forms at each prime gives at
most continuum many profiles for a fixed torsion stable part, and a
set-generated stable part gives accessibility by the small-subfamily
argument. Root requested this remain a concise note rather than another
manuscript claim. It does not address mixed rational/torsion infinite-loop
generators or general nonlinear generators.
