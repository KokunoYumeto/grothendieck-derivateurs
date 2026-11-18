# Part C after C.26: the remaining raw-adjoint question

18 November 2026. Working note by GPT-6 Astra, inherited effort, agent
`DER_LOCALIZERS/linear_case`. The unrestricted theorem is **Refuted by C.26**.
This note concerns the still-open raw-adjoint assertion in the small-projective-generator
corollary. It does not reopen the unrestricted theorem or count a failed proof route as
settling the corollary.

## Scope of the countable-form route

C.22 assumes cocontinuous symmetric monoidal tensor products over the two scalar
rings, scalar bilinearity, a common small linear category obtained by scalar
extension, and the stated projection formula. These are substantive assumptions.
The original manuscript only says bilinear for its internal tensor. Consequently a
proof covering every cocontinuous corollary tensor would itself enlarge the proved
scope, even before considering tensors that do not preserve colimits.

The finite-projective condition on the unit coordinates is automatic in a genuine
corollary presentation. Here is the direct check, independently reconsidered after
the coordinating agent pointed it out. Put U = 1(a). The functor U tensor_k - is
exact and preserves products, because it is evaluation of kappa. Exactness says U
is flat. Product preservation implies U is finitely generated: in U^S with S the
underlying set of U, the tuple listing all elements of U comes from a finite sum
in U tensor k^S, so its finitely many first factors generate U. Take a finite free
presentation k^n -> U with kernel K. Flatness gives exactness on the left after
tensoring with any k^S; comparison with the product of copies of the presentation
shows K tensor k^S -> K^S is an isomorphism. The same tuple argument makes K
finitely generated. Thus U is finitely presented and flat, hence projective.
This says nothing about finite presentation of the *whole unit presheaf* over the
small linear category. In particular it does not make its dual weight FP-infinity.

For a cocontinuous internal tensor, universal interval monicity can be written in
coefficient-module terms. If h_b is the representable at b, put

    B^a(b) = (J tensor h_b)(a).

The functor X -> (J tensor X)(a) is B^a tensor_A X. The map alpha tensor - at a
is represented by A(a,-) -> B^a. Its remaining-monic-after-tensoring property is
precisely purity of that coefficient inclusion. Likewise put

    B_n(b) = F_n(J tensor h_b).

The full interval nullity says that the coefficient complex B_* stays acyclic
after tensoring with every A-module. It is therefore pure acyclic. To see the
purity assertion directly, first test representables to obtain ordinary
acyclicity of B. Write Z_n for its cycles. Since B_{n+1} -> Z_n is epimorphic,
right exactness identifies H_{n+1}(B tensor X) with the kernel of
Z_n tensor X -> B_n tensor X. Vanishing for all X gives purity of each cycle
inclusion. This reformulation makes the interval conditions finite-equation
conditions in a many-sorted module language; it does not make the full raw Hom
functors finite-equation functors.

The exact missing step in a witnesswise countable reduction is this. A cycle in
F G K has finite support in the outer direct sums, but each of its chosen entries
can be a map on an arbitrarily large projective Hom module. Passing to countably
many scalar coefficients, objects, generators, and equations can preserve the
chosen maps as partial data. It does not identify a chosen countable Hom-sort
with *all* homomorphisms over the smaller category. The additional homomorphisms
in the full right adjoint over the smaller category may supply a boundary which
does not come from the original coefficient data. A downward elementary-submodel
argument therefore needs a separate full-Hom comparison theorem. None has been
proved here. C.20 is a specific warning against suppressing this issue: vanishing
on all pure-injective tests does not by itself give vanishing on the projective
test.

## A natural null-homotopy which does not solve the extension problem

Under cocontinuity, the inclusion of functor complexes

    F -> F(J tensor -)

is naturally null-homotopic in the category of cocontinuous k-linear functors.
The source components are projective objects of that functor category. The target
complex is acyclic there: evaluation at every representable is acyclic by the
interval hypothesis. Starting in degree zero, projectivity lifts F_0 -> B_0
through B_1 -> B_0; recursively alpha_n - h_{n-1} d has image in the cycle
module and lifts through B_{n+1}. Thus alpha = d h + h d naturally in X.

This gives a factorization through the standard contractible cone on F. Its
direction is F -> Cone(id_F) -> F(J tensor -). The counit extension required in
C.7 goes in the opposite direction, from F(J tensor G K) into K. A homotopy of
the first arrow does not supply that extension. In particular it does not change
a pure monomorphism into a split monomorphism, or make a projective coefficient
module injective. This fact was sent to the coordinating agent as a possible
ingredient, with the direction obstruction explicit.

## A positive interval-approximation argument: integrated C.27

The full proof is in `C27_draft.tex` and has been independently re-proved by the coordinating agent and the intervals agent, then integrated as C.27 in `sections/C.tex`. It assumes a pointwise tensor with unit values k, a filtered presentation
of J by finitely generated projective objects P_i, and factorization of alpha at
one stage. Finite presentation of the unit over A suffices for the last condition.

Every later alpha_i tensor X is monic because its composite into J tensor X is
monic. Scalar tests make k -> P_i(a) pure. Evaluation of a projective is
k-projective, so that pure map splits; an explicit finite-coordinate proof is in
the integrated claim. Pointwise tensor therefore makes every F(alpha_i tensor X)
degreewise split. For an acyclic projective complex K, C.7's counit-extension
argument produces a retraction P_i tensor G K -> G K at every stage.

The individual P_i tensor G K need not be null. A class from H_n(F G K) maps to
a class at one stage, which becomes zero in F(J tensor G K). Exactness of filtered
colimits of modules kills it at a later stage, where the independently chosen
retraction kills the original class. No compatible family of retractions is
needed. This is a direct proof of the raw gate under the additional interval
presentation condition. We have not shown that an arbitrary interval admits this
presentation.

## Literature actually opened in this continuation

These sources were investigated for the countable-presentation and definability
routes. None is cited as a theorem settling C.raw_gate.

* Mike Prest, *Definable Categories and Monoidal Categories*, Springer Proceedings
  in Mathematics & Statistics 450 (2024), pp.197--222,
  DOI 10.1007/978-3-031-53063-0_6. The publisher abstract, metadata, notes and
  bibliography were opened. The author PDF at
  https://personalpages.manchester.ac.uk/staff/mike.prest/AlmeriaFinRev.pdf failed
  first with a search-service timeout and then with HTTP503 on a direct read.
  The full chapter was not read. Publisher link:
  https://link.springer.com/chapter/10.1007/978-3-031-53063-0_6 .

* Rose Wagstaffe, *A monoidal analogue of the 2-category anti-equivalence between
  ABEX and DEF*, arXiv:2010.12029v1 (22 October 2020); published in Journal of Pure
  and Applied Algebra 227 (2023), article107210. The arXiv PDF was opened and its
  introduction, Sections2.1--2.3, and Theorem3.8 with proof were read. Theorem3.8
  assumes a closed symmetric monoidal finitely accessible category whose finitely
  presented objects form a monoidal subcategory, and starts with a *definable*
  subcategory. It cannot be applied merely by declaring the kernel of Lphi
  definable: preservation of products is precisely absent in the general raw
  question. The finite-presentation and fp-Hom hypotheses are also not automatic.
  Primary PDF: https://arxiv.org/pdf/2010.12029 .

* Leonid Positselski, *The categories of corings and coalgebras over a ring are
  locally countably presentable*, Acta Mathematica Hungarica176(1)(2025),58--85,
  DOI10.1007/s10474-025-01538-y. The publisher PDF was opened; the introduction,
  Theorem1.4's hypotheses, and Theorem3.2 with its inserter/equifier proof were
  read. Theorem3.2 supplies countable *presentations over the fixed ring R*, even
  when R is large. It does not identify a full coinduced Hom after passage to a
  countable subring. Primary PDF:
  https://link.springer.com/content/pdf/10.1007/s10474-025-01538-y.pdf .

* Leonid Positselski, *Resolutions as directed colimits*, arXiv:2312.07197v5
  (17 February 2026); Rendiconti del Seminario Matematico della Universita di
  Padova155(2026),41--83, DOI10.4171/RSMUP/166. The arXiv PDF was opened; its
  introduction and Proposition4.1/Theorem4.2 with proofs were read. These give
  controlled presentations of acyclic complexes under the stated coherence and
  accessibility assumptions. They do not assert that arbitrary Hom functors
  commute with the resulting colimits. The distinction is material here.
  Primary PDF: https://arxiv.org/pdf/2312.07197 .

Friedrich Ulmer's 1977 preprint *Bialgebras in locally presentable categories*
was found through the references of the preceding papers. Opening the linked
15.7MB scan through the search service was rejected for excessive content length.
No theorem from the original scan is treated as read or used. Its cited
inserter/equifier ideas were examined only in Positselski's opened proof.

Queries actually submitted included `pure subcategories monoidal category
countable subring descent module categories purity`, `"linear category"
"countable" "descent" "tensor"`, the exact Prest and Ulmer titles, the exact
Wagstaffe title, `"Resolutions as directed colimits" Positselski arxiv`,
`"linear test category" Grothendieck`, `"linear" "test categories" "interval"`,
`"Pursuing Stacks" "134" "linear"`, and `"Grothendieck" "linear case"
"projective"`. The last group did not yield a primary result closing the raw
gate in the results actually inspected. This is a limited search record, not a
claim of exhaustive coverage.
