# Birth-cover descent in the actual C.1 category

Status: full proofs in `sections/akr_birth_cover_descent.tex`, checked
as dependencies of the independently audited universal-component
theorem. These statements use the actual generating
factorizations, monicity, (10), (11), and the C.1 numerical bound.
They are not statements about arbitrary graph embeddings.

## Forbidden-pair routing

For a source object P fixed at its birth, call two source points
forbidden if no incoming generating copy contains both. A forbidden
pair forces routing of the whole P-arrow through any comparison
arrow whose image contains that pair's images. This is exactly the
protected nonadjacent-pair proof, with the special first-stage circle
replaced by the birth-cover property. The source pair is unchanged
as the whole arrow is moved along a shortest copy-index arc.

## Helly bound

Proper point visibility intervals in a repaired target have at most
`w=max(1,2n-2)` indices. C.1 gives `s>=15n>3w`. If a point subset
has no forbidden pair, its visibility intervals meet pairwise.
Fix one proper interval; all the others have unique lifts meeting
it inside a common window of span at most `3w-3<s`. Pairwise
circular intersections are then ordinary interval intersections,
so they have a common copy. Full-circle visibility sets add no
restriction. For a sum, this is immediate from disjointness.

## Two unconditional consequences

1. Every nonempty intersection `h(P) ∩ g(Q)` is exactly the image of
   an existing commuting span `R→P, R→Q`. If h does not factor
   through g, the preimage of the intersection has no forbidden
   pair, hence lies in one older generating copy. Restrict h to
   that copy without changing the intersection, and descend.
   The process must stop by V, where a nonempty intersection
   factors because every point is represented by a V-arrow.
   This also proves the analogous assertion for finite intersections.

2. Every nonempty pointwise equalizer of an actual parallel pair
   `f,g:S⇉T` is exactly the point image of an existing arrow
   `e:R→S` on which the composites agree. A forbidden fixed pair
   would force f to factor through g; the factor must be the sole
   endomorphism `1_S`, contradicting f≠g. Helly puts all fixed
   points in one older copy. Repeat until the restricted composites
   agree, retaining exact equality of the fixed subset with the
   eventual image, not just containment.

The statements are at the level of point images and actual spans.
Categorical pullback/equalizer universal properties are not claimed.

## A permanent finite safe-source certificate

If all incoming arrows `e:R→S` are injective on binary components,
then the equalizer-image theorem proves connected fixed sets for
every future pair from S, at every future target. This is a finite
condition at S's birth: later full stages add neither arrows into S
nor new older source objects. An ancestor-complete finite substage
therefore suffices to certify S permanently. In particular, the
already exhaustive incoming component-injectivity checks in the
selected ancestor-complete branches have a stronger consequence
than finite persistence alone: those particular source objects
can never be the domain of a killing attachment in any continuation.
This is not a certificate for unexamined source objects elsewhere
in the full stages.

## Resolution of the component issue

If every arrow is injective on binary graph components, the second
consequence makes every fixed subgraph connected within each source
component, and the exact fixed-path attachment kernel vanishes.
`sections/akr_universal_components.tex` now proves this hypothesis
for every repaired C.1 choice by a simultaneous induction. Component
forbidden-pair routing and Helly give an actual older factorization
span for any component-image intersection with at least two elements.
Component paths reduce by one vertex along this span, while reduced
point paths extend by one vertex. Source-rank induction proves
acyclicity and `L_H(f,g) <= L_U(f,g)+1`. C.1's `s>=15n` gives
`k>=n+1`, so component beta gluing preserves injectivity and the
routing/Helly hypotheses. This closes the stage induction and proves
universal survival. The actual examples with point path size 2 and
component path size 3 show that the extra one in the bound is sharp.

## Related structural diagnostics

`code/akr_graph_blocks.py` and its retained output inspect six actual
generated substages. The selected K2 W-pair attachment already has
a subdivided 153-spoked wheel as its nontrivial block, with each
rim segment of length 43; an explicit K4-subdivision certificate
is in `code/akr_selected_wheel_certificate.json`. Hence neither
cactus nor series-parallel structure is available universally.

A new valid K2 point attachment to the two leaves of P13's two-edge
star creates a unique induced 306-cycle. A proper generating P13
image meets it in a two-edge path. Thus the protected first-stage
one-edge overlap statement cannot be extended verbatim to every
newborn primitive cycle.

### Exact geometry of the wheel

In the retained tagged model the selected W-pair into P12 is
`f=(0,1,45)`, `g=(0,16,84)`. The two binary edges share their
first endpoint, and the rest of the old 45-cycle is a 43-edge path
between their other endpoints. In the new s=153 necklace the shared
first endpoint is fixed in every copy. The two other binary endpoints
form the repaired two-point portal necklace. Each of its 153 rim
steps is replaced by the old 43-edge path, whose interior vertices
are private to that copy. The short old edges become the 153 spokes.
Thus the only nontrivial binary component has 6,580 vertices and
6,732 edges. Choosing three rim vertices and the center gives a K4
subdivision with three spoke paths and the three complementary rim
arcs. The retained certificate checks all six paths and their pairwise
disjoint interiors; their edge lengths are 1,1,1,43,43,6493.

### Arbitrarily long proper overlap paths

The two-edge P13 example is the smallest convenient instance; there
cannot be a uniform absolute bound on a generating image's overlap
with every newborn induced cycle. Choose a first-stage protected
circle of admissible length s0 large enough, two of its vertices
at distance L with s0-L≥2, and attach a V-pair necklace between
them. The cyclic concatenation of the chosen L-edge path in all
s new copies is an induced cycle of length sL. A generating old
copy meets it in an L-edge path. Taking s0 arbitrarily large allows
arbitrary L. The new cycle represents the additional rank-one
quotient modulo the s copied old circle cycles: the whole connected
graph has cycle rank s+1 and the old copies contribute rank s.
The completed proof uses birth-cover descent and the component-path
bound; no additional conjecture about primitive-cycle overlaps is needed.
