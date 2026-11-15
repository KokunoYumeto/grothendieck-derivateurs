# Independent check of the simultaneous fixed-space theorem

## Source and exact scope

The source is OpenAI, *Nonsingular systems of equations over arbitrary
groups*, preprint dated 5 October 2026, in the official `openai/math`
repository:

<https://github.com/openai/math/blob/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026/nonsingular-systems-over-arbitrary-groups.pdf>.

The official source page was opened independently. The local complete
PDF is `research/D_nonsingular_2026.pdf`. I read the full proof of
Theorem 2 on printed pages 3–7 and checked the steps below. The
operator and planar parts of Theorem 1 were read and independently
checked by the root and D agents; their full audit is recorded in
`research/D_nonsingular_audit.md`. The bibliographic key is
`D_OpenAI2026Nonsingular`.

This note records a check of the specified proof. It does not infer
any further asphericity, torsion-freeness, or dimension-preservation
statement from the nonsingular-system theorem.

## Theorem 2, step by step

1. **Nested minors and target dimensions.** Reordering the positive
   block dimensions gives `k_1 >= ... >= k_r`. Since the first `t`
   rows of a full-row-rank matrix have rank `t`, the already selected
   `t-1` columns remain independent upon adding row `t` and can be
   extended by one column. Thus the nested minors in (2.2) really
   can all be chosen nonzero. Assigning `l_(j_t)=k_t` respects
   `l_j<=d_j`, because the new selected column has a nonzero entry
   in a row `i<=t` and hence contains a block of dimension at least
   `k_t`. Both required dimension equalities in (2.3) follow.

2. **Compatible primitive generators.** In the last-column fibration
   `U(d-1)->U(d)->S^(2d-1)`, the only possible differential is
   `d_(2d-1)`. Every fiber algebra generator has degree at most
   `2d-3`, so that differential vanishes on generators and hence on
   all products. The restriction map is an isomorphism below degree
   `2d-1`; the sphere generator gives the additional class. For the
   mixed Kunneth part of a prospective primitive identity, both
   positive degrees are at most `2d-2`. Restriction to the two
   smaller unitary groups is therefore injective on every such
   bidegree. On that product the difference is zero, by induction
   for old generators and by the vanishing of the sphere class on
   the fiber for the new one. This proves (2.6) with precisely the
   compatible choices claimed. Pullback along `(X,X^-1)` then gives
   the inversion sign.

3. **Incidence cycle and its leading coefficient.** The space
   `R(d,l)` is the stated compact oriented bundle over the complex
   Grassmannian, with fiber `U(d-l)` and dimension `d^2-l^2`.
   Its pushforward fundamental class has a Poincare dual even
   though its image is not asserted to be a submanifold. An
   exterior monomial of length `u` has degree at least `u^2`,
   giving the unique possible length-`l` term of its class.

   For `f(X)=X direct_sum (-I)`, the only intersection pair has
   `X=I` and the fixed plane equal to the first summand. The
   upper-left directions come from `f`, the lower-right directions
   from the incidence fiber, and the off-diagonal directions from
   `T -> [T,W_0]W_0^-1=2T`. These fill the tangent space, proving
   transversality and intersection multiplicity plus or minus one.
   On restriction to `U(l)`, terms with an index above `l` vanish,
   while any shorter monomial in the remaining generators has
   degree less than `l^2`. Therefore the coefficient `c_(d,l)` in
   (2.7) is nonzero. The cases `l=0` and `l=d` are also valid.

4. **Exact pullback formula.** Each block-diagonal map is the product
   of its individual coordinate-block maps. Primitivity, the block
   restriction formula, and inversion give (2.8), including repeated
   positive and negative occurrences of one matrix variable.
   Translation by the fixed matrix is homotopic to the identity
   because the unitary group is connected.

5. **Top exterior degree and determinant product.** The exterior
   algebra of the source has exactly `sum_i k_i` generators, and
   its top degree is the sum of all their positive degrees. A
   proper subset of these generators cannot have that degree.
   Pullback in (2.8) preserves exterior length on each nonzero
   term, so any shorter term from an incidence class contributes
   zero to the final top-degree product. For each generator index
   `a`, precisely the first `t_a` rows and the corresponding first
   `t_a` selected columns occur. Their wedge product is exactly
   the nested determinant displayed in (2.9), up to the single
   harmless orientation sign. Every factor is nonzero.

6. **Nonzero pairing forces an actual common point.** The product
   incidence domain and the source have dimensions complementary
   in the product of the target unitary groups. A nonzero pairing
   cannot arise from disjoint compact images: sufficiently small
   transverse perturbations would still be disjoint and have
   zero intersection count. Thus an actual common point exists,
   and its fixed planes have the separately assigned dimensions.
   Their sum is the required lower bound.

No gap was found in these steps. In particular, the proof uses
rational cohomology and full rational row rank; it does not silently
require a determinant of plus or minus one.

## Independent reduced-power audit

The explicit target in Claim A.19 was separately checked by the
D agent and the root. The finite-support subgroup of `E^N` is
normal, the diagonal coefficient group embeds, and solving the
first `n` equations at coordinate `n` makes every fixed equation
eventually equal to one. Thus the countable system has a literal
solution in the quotient. Its cardinality is at most
`|E|^(aleph_0)`, with `aleph_0` replacing finite input cardinalities.
