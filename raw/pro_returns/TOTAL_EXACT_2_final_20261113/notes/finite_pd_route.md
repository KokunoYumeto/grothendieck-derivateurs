# Finite projective dimension and the free-factor comparison

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026.
No priority claim. This note records the former proof route and its
resolution by the independently audited predimension separator.

## 1. The finite-projective-dimension vanishing proposal is false

The now proved total strict-predimension category A has, over every
nonzero commutative unital ring R, the exact presentation

    0 -> R[A(W,-)] --D--> R[A(V,-)]^2 -> Q -> 0,
    D[e]=([ev2]-[ev1], [ev3]-[ev1]).

Both terms on the left are projective. Their colimits are R and R^2,
and the colimit map is zero. Therefore

    T_1^A(Q)=R,       pd_(RA)(Q)=1.

The projective dimension is exactly one: the presentation gives at
most one, whereas a projective Q would have vanishing T_1. This
refutes the proposed statement that totality forces T_1(M)=0 for
every finite-projective-dimension module. It does so for the constant
right coefficient R in the actual question, without using a
nonconstant relative-injective coefficient module.

## 2. A valid uniform tensor bound, with its precise limit

For any total A and any Z A-module M of projective dimension d,

    T_i(M tensor_Z Z[H])=0       for every A-set H and every i>d.

Indeed, tensor a length-d projective resolution of M pointwise with
Z[H]. This stays exact because each Z[H(a)] is free. A projective
P is a retract of a sum of representables P_a. Hence P tensor Z[H]
is a retract of a sum of

    P_a tensor Z[H] = Z[A(a,-) times H],

which are colimit-acyclic by totality. This is a length-d acyclic
resolution, so it computes derived colimits and gives the bound.
The identical proof works over any commutative coefficient ring R.

If M is objectwise flat over Z, the r-fold tensor product of the
bounded projective resolution resolves M^{tensor r} objectwise.
Each term is a retract of sums of permutation modules on products
of representables. Consequently

    T_i(M^{tensor r})=0       for i>rd.

Over a field, the flatness condition is automatic. These two bounds
were independently checked by `main_compact_duality`. Neither
annihilates degrees 1 through d; the separator's Q proves that no
unconditional periodicity argument can deduce that conclusion.

## 3. The total-index free-factor weak comparison also fails

The same category gives a stronger obstruction than the earlier
parallel-pair example in `sections/freefactor_nerve.tex`.

For X in A, introduce generators u_x,v_x for every actual V-arrow
x:V→X. For every actual W-arrow e:W→X, impose the relator

    u_(ev2) u_(ev1)^(-1) v_(ev3) v_(ev1)^(-1)=1.          (1)

Renaming along an arrow X→Y defines a group diagram G. Its
abelianization is exactly Q from §1.

### Free values

Any nonempty finite family of r distinct W-arrows has r distinct
image hyperedges, since an increasing embedding of W is determined
by its image. If their union has v vertices, positivity gives
2v>3r. Thus some vertex belongs to exactly one of the r edges.
The corresponding V-arrow exists by composition. If that private
vertex is ev1, ev2, or ev3, respectively, one may select u_(ev1),
u_(ev2), or v_(ev3). This generator occurs precisely once, with
exponent ±1, in its relator, and in no other relator of the family.
Eliminating it and that relator is a Tietze elimination. Repeating
for the remaining finite family eliminates all relators and proves
that G_X is a finitely generated free group.

### Free-factor transitions

Identify an arrow Y→X with its closed induced image. An actual
point or W-arrow of X whose image is contained in Y is exactly an
actual arrow in Y: one implication is composition, the other is
restriction of closedness. Consider a nonempty family of r new
W-arrows, meaning ones not contained in Y, and put U equal to Y
together with their vertices. Then U properly contains Y, and

    2|U\Y| > 3|E_X(U)\E_X(Y)| >= 3r.

Every vertex of U\Y belongs to one of the selected edges. The
selected edges have at most 3r incidences outside Y, so some outside
vertex occurs in precisely one selected edge. The elimination used
above can therefore always choose a generator outside Y. It never
changes an old generator or an old relator. Eliminating all new
relators leaves exactly a presentation of G_Y together with extra
free generators. Consequently the actual transition G_Y→G_X is a
free-factor inclusion. The argument applies to every arrow after
identifying its image.

### The comparison and its nonzero second homology

The group colimit of G is F(u,v). To see this without assuming a
set colimit commutes with products, use its generators and relations:
each of the two representable generator sets has singleton set
colimit, and the free-group functor preserves colimits. Every
relator (1) then becomes `u u^(-1) v v^(-1)=1`, imposing no
additional group relation.

For the homology spectral sequence of the homotopy colimit of BG,
the only nonzero objectwise homology rows are H_0=Z and H_1=Q,
because every G_X is free. Totality gives H_i(BA;Z)=0 for i>0.
Thus the term T_1(Q)=Z at bidegree (1,1) has neither a nonzero
incoming nor outgoing differential, and it is the only contribution
to total degree two. Hence

    H_2(hocolim_A BG_X;Z)=Z,
    H_2(B(colim_A G_X);Z)=H_2(BF(u,v);Z)=0.

The canonical weak comparison is therefore not a weak equivalence,
even though the index is total, all group values are finitely
generated free, every transition is a free-factor inclusion, and
the group colimit is free. This conclusion is proved from the
universal separator construction and the explicit eliminations;
bounded word checks are not a substitute for those arguments.

## 4. A bounded-rank case remains true

If G:A→Grp is such a free-factor diagram over a total A and its
free ranks have a single finite upper bound, the canonical weak
comparison is an equivalence. Let C be the nonempty full cosieve
of maximal-rank objects. Common successors make C connected and
make every a↓C nonempty. Condition I connects any two objects of
a↓C by a commuting square. The cosieve C is total: extend an
arbitrary C-set by empty sets outside C, and its element category
is unchanged. Hence a↓C, a connected element category over C,
is contractible. Thus C→A is homotopy final and final.

Every transition in G|C is an isomorphism, since a free factor of
equal finite rank is the whole free group. Since BC is contractible,
this locally constant diagram is naturally isomorphic, after choosing
a base object, to a constant group diagram: the groupoid completion
of C is the indiscrete connected groupoid. Its ordinary group
colimit is that group and its homotopy colimit of nerves is its
classifying space. This proves the weak comparison in this bounded
case. The separator necessarily escapes the rank bound.

## 5. Primary literature checked before the counterexample

The following source checks did not produce the proposed vanishing
theorem, and they do not conflict with its now explicit refutation.

- **Jibladze and Pirashvili (1991), Proposition 2.6, Proposition 2.10,
  and Theorem A, pp. 259–263.** The cubical terms are projective in
  specified categories of all functors on full module subcategories;
  the two-sided cubical bar construction resolves the inclusion
  functor; Theorem A identifies the resulting Ext with Mac Lane
  cohomology for an additive target. The proof through the end of
  Theorem A was read. These statements do not transfer finite
  projective dimension from an arbitrary indexing category A to
  that larger all-functor category. Source:
  https://rmi.tsu.ge/~jib/pubs/jipicat.pdf . Local PDF:
  `sources/JibladzePirashvili1991.pdf`.

- **Gaudens and Schwartz (2005), Theorems 1.1, 1.2, 3.1 and 4.1.**
  The four-page primary article was read in full. Its vanishing
  statements involve Boolean-algebra-valued sources and reduced
  polynomial targets in the functor category on finite F_2-vector
  spaces, with the finite-value hypotheses and later extensions
  stated there. They do not give an arbitrary-A pullback theorem.
  Source: https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2005.06.008.pdf .
  Local PDF/text: `sources/GaudensSchwartz2005.pdf` and `.txt`.

- **Pirashvili (2002), Theorem 3.5, printed p. 380.** The primary
  PDF and formula image were inspected. Over F_2 the displayed
  calculation gives Ext^i(I,S^{2^h})=F_2 in degrees divisible by
  2^{h+1} and zero otherwise. In particular I has infinite projective
  dimension in the full functor category, despite a vector space
  at a one-object indexing category having projective dimension
  zero. The proof uses finite-*type* resolutions, not finite
  projective dimension. Source:
  https://numdam.org/item/SB_1999-2000__42__369_0.pdf . Local PDF:
  `sources/Pirashvili2002_polynomial.pdf`.

- **Pirashvili (1996), opening theorem, Lemma 4.1 and §5.** The
  primary six-page preprint identifies cubical homology with stable
  Eilenberg–Mac Lane homology and proves the Kan-extension statement.
  It supplies no contraction of the colimit cubical complex over an
  arbitrary total A. Source:
  https://archive.mpim-bonn.mpg.de/id/eprint/4178/1/preprint_1994_143.pdf .
  Local PDF: `sources/Pirashvili1996_kan.pdf`.

The Johnson–McCarthy (1998) AMS article/PDF returned HTTP 403; no
body was obtained and no theorem from it is used. The requested
Cambridge PDF for Pirashvili's *Simplicial degrees of functors*
(1999) redirected to an abstract page; again no body theorem is
used. The exact access records are
`code/finite_source_fetch_pd.py/.out` and
`code/finite_source_fetch_pd_more.py/.out`. The latter records
successful PDF byte counts and SHA-256 hashes for the three archived
sources. Search phrases included `finite projective dimension
permutation modules homology vanishing`, `finite projective dimension
functor Mac Lane`, `homotopy colimit free factor groups`, and the
exact article titles above. Search snippets were not used as proofs.

### Bibliographic details

Gaudens, G., & Schwartz, L. (2005). Un théorème d’annulation en
cohomologie de MacLane. *Comptes Rendus Mathématique, 341*(2), 119–122.
https://doi.org/10.1016/j.crma.2005.06.008

Jibladze, M., & Pirashvili, T. (1991). Cohomology of algebraic theories.
*Journal of Algebra, 137*(2), 253–296.
https://doi.org/10.1016/0021-8693(91)90093-N

Pirashvili, T. (1996). Kan extension and stable homology of Eilenberg
and Mac Lane spaces. *Topology, 35*, 883–886.

Pirashvili, T. (2002). Polynomial functors over finite fields.
*Astérisque, 276*, Exposé 877, 369–388.
