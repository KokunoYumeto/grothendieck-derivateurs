# Part C proof and source audit

This audit accompanies `sections/C_paths.tex`, `sections/C_crown.tex`, and
`sections/C_manuscript.tex`. Their 22 result records are in
`research/Cpaths_results.json`; the primary-source bibliography is
`research/Cpaths_references.bib`. The complete quantified arguments are in
the three TeX files. This file records the checks and the scope of the
comparisons used there.

The additional finite-bound result is now B.9 in `sections/B_finite.tex`,
with its separate record in `research/Cpaths_Bfinite_results.json`.

## Proof inventory

| Claims | Exact comparison or obstruction checked |
|---|---|
| C.1–C.2 | Endpoint-preserving nondecreasing vertex maps; fibred arrow `(u, eta):c -> d u`; run-clamp retraction; arbitrary-vertical two-action; explicit failure of its restricted-vertical version. |
| C.3 | The enriched restriction equivalence uses its derived unit. The two comma calculations prove finality for the actual opposite indexing functors. Both legs of the specified Grothendieck span are tracked. |
| C.4–C.6 | The left, right and symmetric padding maps commute as vertex functions. Every one-sign system has a categorical homotopy equivalence to its effect set, with the negative composition in the opposite order. The crown refutes the universal mapping-space comparison while retaining these padding and composition results. |
| C.7 | The comma presheaf is a strict replacement. The positive and negative deletion/padding adjunctions have their indicated directions. Restriction of the negative coefficient equivalence along padding is the identity. The full all-type presheaf is local and satisfies the representable localization property. |
| C.8 | Interval localization gives an equivalence of complete type diagrams; its inverse data form a contractible space. The resulting cocone is the specified map under the representable. Lists of intervals supply a map of Segal objects and prove all composition, unit and endpoint coherences. |
| C.9 | The first-type simplicial map to the reduced-hammock colimit is checked on every face and degeneracy. Latching maps are identity-edge inclusions with the stated intersections. The matching categories for constant fibrations have the endpoint-and-turning-vertex initial object. The marking enlargement and its actual comparison are explicit. |
| C.11 | The vertex/letter correspondence reverses composition. The injective-versus-constant linear functional proves the affine obstruction over every nonzero ring. Its integral kernel calculation gives the stated first homology. The collage gives an ordinary-final functor with non-aspherical target. |
| C.17 | The universal lift defines the stage winding functor. The geodesic sections commute with actual padding. The other inverse uses the proved path formula in a finite fence, applied to the whole fixed winding category; only finitely many windings require a common later stage. This establishes the ind-isomorphism on every small test, including tests with infinitely many objects. The lifted excursion bound also directly excludes a categorical homotopy inverse for each actual padding map. |
| C.20 | Both proofs use the literal exponential identification of fixed-type categories. Localization equality is a finite witness even for an infinite test. Coherent type homotopies compare that witness with the actual transitions of the selected sequence. |
| C.21 | Run number is monotone. Unbounded run number is equivalent to preorder cofinality. A bounded run sequence stabilizes at a reduced type up to the specified categorical homotopies. The finite fence gives the sharp universal counterexample. |
| C.22–C.23 | The interval concatenation is the explicit endpoint pushout. Finite-object sources suffice only for the full-inclusion union statement. General filtered colimits use finite arrows and relations. The uniform fibration assertion is proved with the exact comma criterion; its necessity is tested on a representable diagram. The incoming and outgoing lift categories for the smooth/proper test each have two components. |
| C.24 | Finite horns extend in the specified symmetric-group stages and their union. The shift is ind-identical by three stage transformations. The actual union map on fundamental groups is the proper inclusion fixing zero. The infinite fence and terminal fork establish the other two stated homotopy-length obstructions. |
| C.25 | The finite sphere is the suspension of the crown. Its eight oriented triangles give a nonzero cycle. The comparison on the parallel-arrow source is trivial, while the displayed loop in the diagram category has infinite order. |
| C.26 | The pointed five-arrow category and its two zero endofunctors satisfy the asserted representabilities directly. Bounded finite-dimensional rational complexes satisfy the finite model-category axioms used by Dwyer–Kan. The cosimplicial resolution stays in that small category degree by degree; normalized homology computes its mapping-space homotopy groups. |
| C.27 | The universal colimit assertion is tested first on set actions and then on the explicitly defined bipartite right-angled Artin groups. The homology diagrams in degrees one and two are sums of representables, so the bar calculation has no unaccounted differential. The actual group colimit is the free abelian group on the two color classes. |
| C.28 | Only finite sphere models are used to force a one-type. For the finite-category comparison, finite presentation of its fundamental groupoid supplies the compactness argument. No finite-dimensional or finite-CW assertion about a general finite category nerve is used. The specified comparison is identified by the commuting square of stage units. |

## Manuscript coverage

The sentence-by-sentence replacement table is in C.28. It covers V ms.
46–49; VII ms. 26–32, 48–58, 99–103, 108–115 and 125–132; and IX ms.
22–23. The underlying proofs are C.20–C.27 together with the root claims
B.1, C.13–C.16 and D.1–D.2. C.17 supplies the actual path-union
counterexample and the failure of the infinite-test comparison. C.28 now
refers to C.14 for the exact invariance criterion and to C.15 for the
nontrivial mapping-space fundamental group example.

The strict-retraction row states only the results proved in Part D. It
does not infer strict retractions from an unproved strictification of
homotopy-commutative squares.

## Primary-source steps read

| Source | Used step and verified scope |
|---|---|
| Lurie, *Higher Topos Theory*, A.3.3.8 | Official full text and proof opened. Used with simplicial-set enrichment and projective diagram structures; the hom objects are cofibrant. |
| Arakawa–Cnossen, arXiv:2608.19870 | Supplied complete LaTeX read at the relative-category convention, 1.9, 1.11, 4.7, 4.8, 4.16 and the relevant proofs. The source marks all equivalences; C.9 explicitly adjoins ordinary isomorphisms before applying it. |
| Dwyer–Kan, *Simplicial localizations of categories* | Definition 4.1 and the saturation comparison in 5.1, with the supporting constructions, read in the supplied primary PDF. Used for the actual marking enlargement. |
| Dwyer–Kan, *Calculating simplicial localizations* | Definition 2.1, Proposition 2.2 and the used calculus results read in full text. The hammock comparison is natural in the marking and compatible with its structural maps. |
| Dwyer–Kan, *Function complexes in homotopical algebra* | Definition 1.4 and §4 read, including 4.4–4.5, 4.7–4.8. The definition requires finite limits and colimits. The fibrant-target half of 4.4 applies to the explicit cosimplicial rational-complex resolution. |
| Low–Mazel-Gee, *From fractions to complete Segal spaces* | Complete supplied LaTeX read at zigzag categories, homotopical three-arrow calculus, reduction and Segal/completeness arguments. Its marked vertical arrows and fraction hypotheses are retained. |
| Mazel-Gee, *Hammocks and fractions in relative infinity-categories* | Complete supplied LaTeX read at the construction and fraction theorem. Its introduction does not establish the general universal property later supplied by Arakawa–Cnossen. No stronger statement is imported. |
| Cisinski, *Higher Categories and Homotopical Algebra*, 7.2.8 and 7.2.10 | Author's full text opened. The right-calculus-of-fractions hypotheses are retained in the literature comparison. |
| Carranza–Kapulkin–Lindsey, arXiv:2306.02218 | Full primary PDF opened; 10.8, 10.10 and their proofs checked, including the CLF/CRF hypotheses and the universe convention. |
| Arakawa–Carranza–Kapulkin, arXiv:2509.10288 | Full primary PDF opened; the three resolution conditions and the proof of 2.2 checked. Used as a comparison with the explicit presheaf proof, without dropping a resolution condition. |
| Guillén–Navarro–Pascual–Roig, *A Cartan–Eilenberg approach to homotopical algebra* | §1.2 read in the full primary PDF. Its arbitrary-vertical hammock quotient proves an ordinary localization formula; no mapping-space theorem is attributed to that section. |
| Maltsiniotis, *Structures d'asphéricité, foncteurs lisses, et fibrations* | Definition 1.1 and Theorem 1.2(b), with the relevant proof and duality, read in the primary Numdam PDF. C.23 computes the precise lift categories in that criterion. |
| Charney, *An introduction to right-angled Artin groups* | Full author preprint opened; Theorem 2.6's flag-link proof and the cellular homology calculation read. C.27 uses only the displayed bipartite Salvetti complexes and their color-preserving maps. |
| MathOverflow 351366 | Question and answer opened as a record of the arbitrary-vertical question. No theorem or priority claim is based on the discussion. |

Source searches also covered arbitrary-vertical hammocks, relative
localization, Segal presentations and fraction comparisons. All research
claims in C.12 identify their proof and actual comparison; none asserts
novelty or priority from search silence.

## Reproducible finite checks

Both programs use only the Python standard library and print their bounds.

- `code/cpaths_checks.py`: 961 vertex/letter pairs, 2,731 compositions,
  5,503 maps in 1,213 nonempty clamping cases, 224 one-sign crown cases,
  16 padding squares, and 7,937 R8 certificate arrows to 1,023 words.
- `code/cpaths_manuscript_checks.py`: 2,575 bounded-run fence words,
  73,978 symmetric-filtration associativity triples, 148 shift naturality
  arrows, the two marking counterexamples, the sphere cycle, the finite
  pointed category, the terminal fork, the two lift-category obstructions,
  17 crown geodesics and eight excursions.

The `.out` files record successful runs. These computations audit finite
formulas; the TeX arguments prove their stated unbounded quantifiers.

## Independent review of Part E

All six claims were read independently. Gagna's primary paper was opened
at §§1–2 and 6.3–6.9, including the poset-unit homotopy. Ara's primary
paper was opened at §3 and Appendix A.11, and the attached manuscript's
positive Alexander–Whitney construction was read. E.3 uses the resulting
localization equivalence and nerve homotopies; it does not require a
transferred model structure from the unrefereed attached paper.

For clarity the nerve homotopy can be written as the typed composite

`O_m --delta_m--> O_m tensor O_m --(F tensor O_theta)--> X tensor D_1 --P--> Y`,

where `delta_m` is the positive Alexander–Whitney diagonal, `F` is an
`m`-simplex of the Street nerve and `theta:[m]->[1]`. The two counit
identities give the endpoints, and naturality gives all simplicial
operators. This is an explicit check of the comparison used in E.3.

In E.4, strict interchange verifies the stated triple group law. The
inverse of `(f,g,alpha)` has structural cell
`g^{-1} * alpha^{-1} * f^{-1}`. The equations at `hh^{-1}` and
`h^{-1}h` force each lax cell to be invertible. Under the specified
normal Gray convention, identity higher source cells supply no additional
data. Quotient descent therefore holds on the actual functor and
transformation categories. The cardinal estimate is valid in all finite
dimensions and in dimension infinity when total cell cardinality is used.

## Independent review of B.7 and B.8

The positive B.7 proof uses `nu=mu^+` and tests of size at most `nu`, so
the strict inequality `mu^+<kappa` is correct. Nerves, simplex categories,
finite horn attachments, countable Kan replacement and cylinders all
remain of size at most the infinite cardinal `nu`. Maps to a Kan model
and their homotopies therefore give the full restricted localization,
not only essential surjectivity. Every R2 object needed for a stage
fits this same bound. The resulting inverse of the ind-unit is a global
ind-morphism. At `kappa<=mu^+`, the element construction stays at size
at most `mu`; the finite sphere test proves failure of a global
ind-groupoid presentation in the stated example.

For B.8, the prescribed map `C_Z -> C` fixes the `B` summand and collapses
the fence of copies of `A`. The nerve homotopy-colimit realization on
those copies is `BA` times a subdivided interval. Collapsing it gives the
double mapping cylinder relative to `BB`, proving the required weak
equivalence. The two stated finite conditions are precisely the common
upper-bound and parallel-arrow equalization conditions for the element
category. For uncountable `kappa`, the size computation works at singular
cardinals as well: each finite construction uses finitely many sizes
below `kappa`, and countable simplicial operations cost at most
`max(lambda,aleph_0)<kappa` for the one infinite bound `lambda` chosen
for that construction.

### Additional proved finite-bound fact

Let `m` be a nonnegative integer, and let a small filtered diagram in
`Cat_hot` have at most `m` arrows in every stage. Its ind-object is
isomorphic to the constant ind-object of a category with at most `m`
arrows.

Here is the complete proof. Choose the full subcategory `D` with one
representative of each isomorphism type of category with at most `m`
arrows. There are finitely many such structures, and each functor set,
hence each homotopy-class set in `D`, is finite. The given diagram can
be transported into `D`. Put `F=colim h_{K_i}` on `D`. For each `A`, its
value has cardinality at most `max_{K in D}|D(A,K)|`: any larger finite
family of distinct colimit elements would have representatives at one
stage, contradicting that bound. Thus the element category of `F` is a
finite filtered category. A cocone on its finite identity diagram gives
an object `e` and arrows `t_d:d->e` satisfying `t_e t_d=t_d` and
`t_e^2=t_e`. The colimit presheaf is therefore the image of the
idempotent endomorphism `t_e` of the representable at `e`, hence a
retract of that representable. The ind-embedding of a full subcategory
is fully faithful by the limit–colimit Hom formula, so this is also a
retract of a finite stage in the global ind-category.

Represent its idempotent class by an actual endofunctor `f:K->K`.
The set of endofunctors is finite, so its powers are eventually
periodic. Choose a positive exponent `r` beyond the preperiod and
divisible by the period. Then `f^{2r}=f^r` strictly, while
`[f^r]=[f]` because the class of `f` is idempotent. Let `L` be the
subcategory of fixed objects and fixed arrows of `f^r`. It is closed
under identities and composition. The inclusion `i:L->K` and
retraction `r_K:K->L` satisfy `r_K i=id_L` and `i r_K=f^r` strictly.
This splits the original homotopy-idempotent and gives the required
constant ind-object, with `|Mor L|<=m`. For `m=0`, every stage and `L`
is empty, so the same conclusion holds directly.

This fact establishes a structural strengthening for uniformly finite
stages. No additional global locality conclusion from finite-test
invariance is asserted here.

## Independent review of D.11–D.13

The original relative cylinder omitted the common end face
`V={0,...,n-1}` from its gluing locus. At `n=1` that omission leaves
an extra isolated vertex; hence its projection cannot be a weak
equivalence. This was reported immediately and corrected to
`W=pi^{-1}(boundary Delta^n)`, the union of that common face and the
side facets missing an index below `n`. The order homotopy identifying
`n+1` with `n` now descends to the required relative deformation
retraction. The two end facets still give the indicated monomorphism.

After that repair the D.11 formulas were checked independently for
arbitrary dimension: larger faces acquire the new vertex before smaller
ones do; smaller faces lose the old vertex before larger ones do; each
flag has at most one face of each size; every projected flag is the
original flag. The common boundary face remains fixed, and the other
boundary flags stay in a side facet, so all boundary components become
identities after the chosen filler.

In D.12 the edge assigned to a natural transformation is strictly
natural under restriction because both the adjunction unit and the
chosen functor `P4->[1]` are fixed. The two lifted edges therefore lie
over the very same edge `a`, not merely its homotopy class. The
two-horn with edges `02=u` and `12=v` lies over `s_0(a)`; its missing
edge is in the strict fiber. This validates application of D.11.
The common orientation pattern, padding by identity pairs, simultaneous
gluing, iteration, and arrow-retract equations were also checked.

D.13's finite-support argument is valid. A finite attaching category
uses finitely many preceding cells; their chosen dependency trees are
finitely branching and have strictly decreasing cell ordinals. König's
lemma makes the dependency closure finite. The resulting subcomplexes
form a filtered union under the whole original source category, which
may itself be infinite. Finite presentation in that undercategory
therefore supplies the stated retract of a finite relative cell complex.

The independent review establishes these stated fixed-dimension,
finite-stage and relative finite-presentation assertions. The universal
quotient computations in dimensions one and two give relative lengths
eight and twelve before fibrant completion. No preservation of those
lower bounds by fibrant completion has been proved, so those computations
are not used to assert a general failure of prescribed extension.

## Independent review of the countable rigid fibrant counterexample

The later general counterexample uses a different construction from the
finite-dimensional quotient lower bounds. Start at the one-point poset
`F_0={a}` and, at each finite stage, attach a fresh copy of every generating
Thomason horn along every map of its finite domain into the current stage.
Already filled horn maps must also receive fresh cells. The countable union
`F` is countable, cofibrant, fibrant and weakly contractible: each attachment
is a generating trivial cofibration, and each finite horn map into the union
occurs at some finite stage. The standard construction that declines to add
already available fillers would not have this argument's branching property.

Here is an independent check of the crucial invariant under an arbitrary,
possibly noninjective, attaching map. In the face poset of an `n`-simplex,
the two faces absent from its `i`-th horn are `A=[n]\\{i}` and `T=[n]`.
The new objects of the second subdivision are exactly the nonempty flags
containing at least one of these faces. New-to-new arrows are inclusions
of flags, and the old stage is a full sieve in the pushout. A one-face
new flag is minimal, since it has no old horn subflag. A new flag of
length at least three has two distinct maximal proper subflags still
containing a chosen absent face; these remain new, incomparable lower
objects. A two-face new flag has either two new singleton subflags or
one new singleton and the image of its old singleton. In the second
case those two lower objects are incomparable: the new singleton has
no old predecessor, and no new object maps to an old object. Thus every
new nonminimal object lacks a greatest strict predecessor. Identifications
between old faces do not change any of these comparisons. Old principal
ideals remain unchanged. A new principal ideal is the union of its
finitely many new subflags and the finite principal ideal below the
image of its largest horn subflag. Induction therefore proves that `F`
has finite principal ideals and no downbeat points.

Every strict pair `x<z` appearing at a stage gets a fresh one-horn cell
at `x` on the next pass. In its four-edge fence, the first new maximum
`y` satisfies `x<y`, and `y,z` have no common upper bound. At that pass
the old lower ideal of `y` is exactly the ideal of `x`; distinct newly
attached cells have no arrows between their new objects. Subsequent
Thomason cofibrations of posets are actual Dwyer inclusions. Their
retractions on the upper closure of the old subposet show that a newly
created common upper bound would yield an old common upper bound.
Consequently the absence of a common upper bound persists to `F`.

For any monotone endomap `g<=id_F`, choose a minimal moved point `x`.
All strict predecessors are fixed, so `g(x)<x` is their greatest element,
contradicting the no-downbeat invariant. Thus `g=id_F`. For `g>=id_F`,
a moved point gives `x<z=g(x)`; choose the preceding branch point `y`.
Monotonicity and the pointwise inequality make `g(y)` a common upper
bound of `y,z`, again impossible. Since natural transformations between
poset maps are exactly pointwise inequalities, `id_F` is isolated in
the functor category and hence in its finite-zigzag homotopy class.

The inclusion `{a}->F` is a cofibration. Take a strict upper neighbor
`z` of `a` in its first attached one-horn and prescribe the arrow `a->z`
at the source of this cofibration. An extension starting at `id_F`
would end at a functor `g` in its finite-zigzag class with `g(a)=z`.
Isolation makes this impossible. This proves general prescribed-endpoint
extension failure with a specified countable fibrant target, rather than
inferring it from the finite quotient computations. The D agent records
the independent finite horn-pushout certificates and the collage converting
this example into a strict-retraction obstruction.
