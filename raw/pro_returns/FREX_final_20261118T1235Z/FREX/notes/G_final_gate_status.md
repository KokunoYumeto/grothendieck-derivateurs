# Part G: exact remaining gates at 12:28 UTC

This is a status record, not a claim of completion. Numbered proofs through
G.43 are in `sections/G.tex`, with their independent checks in
`CHECK_EVENTS_G.tsv`. The principal universal questions remain unresolved.

## Requested conclusions

1. The specified raw-point gap diagram passes the homotopy-colimit comparison
   (G.5), including all point-closure colors. G.15 extends this to fixed-source
   embedding-gap diagrams with arbitrary fixed coordinate listings.
2. No free-monoid diagram on C_delta with nonzero T1 of its abelianization has
   been constructed, and universal vanishing has not been proved.
3. The universal free-monoid comparison on C_delta has not been proved or
   refuted. The intrinsic group test in G.18 is a reduction, not a complete
   classification of the class F.
4. The inclusions exact ⊆ F ⊆ total are rechecked. Neither requested strictness
   question has been settled.

## Strongest proved universal homology reduction

For a smooth locally free G-monoid S, put K=S^gp, H=K⋊G,
X=|(NS)/G|, and Y=|NT/H|, where T is the canonical prefix tree.
G.33 gives

    0 → H2(X;Z) → H2(Y;Z) --d2→ ⊕_[C] C
      → (K_G)_ab → H1(Y;Z) → 0,

and Hi(X;Z) ≅ Hi(Y;Z) for i≥3. The sum is over H-conjugacy classes of
nontrivial cut stabilizers, which are maximal root-closed locally cyclic
subgroups. This is a coherent spectral-sequence calculation, not an asserted
collapse of the remaining row. For the first derived-colimit question the
remaining issue is precisely ker(d2). Higher source homology is the higher
homology of Y. Passing the actual monoid comparison still requires its own
homotopy/local-coefficient argument; ordinary homology alone is insufficient.

G.34 proves that neither H2(Y)=0 nor injectivity C→K_G can be imposed as a
universal shortcut: its explicit finite-rank injective diagram has all higher
abelianized derived colimits zero, but H2(Y) and d2 are nonzero. Its d2 is
injective, so it is not a counterexample to the main question.

## What the last interval/tree work accomplished

G.40 realizes the stabilizer of every bounded cut by a finite binary meet or
join. The original cut itself need not be finite-parameter. G.41 then proves
that adjoining every smooth bounded cut preserves the H-orbit tree homotopy
type, using the same stabilizer normal subgroup and simply connected covers.

G.42 removes the suspected blowup of canonical rooted-meet supports. The meet
of two points is fixed by one endpoint stabilizer. On each raw support-pair
pattern it is an equivariant function of one endpoint, so a finite union of
vertex orbits has a finite-orbit meet/turn skeleton. These skeletons have
contractible nerves in the original prefix orientation. Relative skeletons
also enclose strict finite direct diagrams of fixed K translations.

The limitation is concrete. Finite vertex-orbit count does not imply finitely
many pair or chain orbits. Face transports chosen after taking quotients can
commute only up to stabilizer elements; they are not automatically strict
translation diagrams. Monoid products can involve strong closure coordinates
outside both input supports. No proof has turned the skeletons into a coherent
exact template preserving these operations.

G.43 constrains monotone cuts between two lex-support chain orbits to a common
initial flag. It treats actual tuple configurations and incompatible closure
ties explicitly. A simultaneous pure-order extension for finite chain unions
has a plausible recursive construction (interleaving blocks, common first
pivots, closure-color ties, and redundant-coordinate refinements), but this
has not supplied a product-compatible monoid template or a d2 calculation.

## Construction routes and their exact scope

- The whole original positive DF incidence-relator lift is excluded by G.20.
  This does not exclude arbitrary signed group-word lifts or arbitrary derived
  classes.
- The twisted rectangle has exact finite models (G.22), including the X11
  configuration. A global extension remains unproved. G.24 forces its two
  factor-chain flags to coincide, leaving24 regimes. Finite length feasibility
  and finite word unification are not global existence theorems.
- G.38 gives injective strictly positive integral matrices with a rational
  first-derived-colimit obstruction. Their coherent lift to word substitutions
  remains missing.
- G.39 refutes unrestricted amalgamation even for bifix embeddings inducing
  group isomorphisms with identical unimodular positive abelian cones.
- The extra saturation certificates in
  `notes/G_positive_saturation_current.md` exclude two narrower blanket
  proposals: saturated inputs can have conflicting cones, and requiring
  saturated output maps fails even where an ordinary amalgam exists. They do
  not rule out every cone-compatible saturated-input span or the specific
  global twisted construction.

No finite computation, literature search, or auxiliary tree refinement is
being promoted here to a completed universal free-monoid result.


## Last primary-source boundary check

Man Gao and Jie Wu, *Simplicial Monoid Actions and The Associated Universal Simplicial Monoid Construction* (2013), https://arxiv.org/pdf/1303.3718, was opened at12:32: Theorem1.1, Proposition1.2, Lemma3.4 and its proof, and Lemma3.6's statement. Their cofiber formula requires categories equivalent to totally disconnected categories, or the corresponding unit-orbit condition for actions. Contractibility alone is insufficient. Thus this source does not justify replacing a general interval monoid's classifying space by its poset nerve with vertices identified. No theorem from it is imported into the numbered proofs.
