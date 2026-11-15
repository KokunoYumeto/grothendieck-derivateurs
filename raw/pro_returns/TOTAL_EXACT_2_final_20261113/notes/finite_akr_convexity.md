# Independent C.1 intersection and convexity audit

AI-produced; no priority claim. This supplements the AKR agent's work,
without asserting all-stage persistence.

## Proven reduction

`sections/akr_convexity.tex`, Lemma `C:convex-fixed`: two component-injective
induced graph embeddings with geodesically convex images have a convex
fixed-point set whenever their nontrivial point-transition relation has
no directed cycles. Between fixed endpoints, both embeddings map the
finite interval of all shortest paths bijectively onto the same ambient
interval. Their quotient is a permutation of that finite interval. A
nontrivial permutation orbit contradicts the no-cycle hypothesis, so
the entire interval is fixed. This is a complete elementary proof.

For an arbitrary repaired C.1 attachment, what remains is an induction
showing component injectivity and geodesic convexity of all old-arrow
images, then the full cycle-space comparison across exceptional links.
The current work does not provide that induction.

## Exact finite runs

```
python TOTEX2/code/finite_akr_intersections.py --stage selected_k2 --closure > TOTEX2/code/finite_akr_intersections_k2_closure.out
python TOTEX2/code/finite_akr_intersections.py --stage critical_k3 --closure > TOTEX2/code/finite_akr_intersections_critical_closure.out
python TOTEX2/code/finite_akr_convex.py --stage selected_k2 > TOTEX2/code/finite_akr_convex_k2.out
python TOTEX2/code/finite_akr_convex.py --stage critical_k3 > TOTEX2/code/finite_akr_convex_critical.out
```

The scripts import the AKR agent's current `akr_stage_model.py`. They
construct the category from functions and independently construct the
graph G_X from W-arrows. No source PDFs or uploads are changed.

The selected K2 run has 18 objects and 21461 arrows; all H maps are
injective. Its new target has 154 distinct incoming image sets of
sources size>=4, including the identity. All 11781 unordered pairs
were checked; 306 have an intersection of cardinality>=2. Closing under
all intersections gives 307 sets of cardinality>=2, using 47278
intersection steps. Every new set already occurs as a pairwise
intersection. None splits into two connected components with the same
ambient H-label.

The critical K3 run has 19 objects and 81430 arrows; all H maps are
injective. Its new target has 892 incoming images of larger sources,
397386 unordered pairs, and 2673 pairs intersecting in>=2 vertices.
Its full intersection closure contains 1189 such sets, using 1060588
intersection steps. Again, all new sets were pairwise intersections,
and every intersection is connected within each ambient H-component.

The enumeration deliberately restricts to source cardinality>=4.
All small objects are explicitly classified in the output. Singleton
sources give trivial intersections. Size-three sources have a bijective
incoming W-arrow, so source C.2(c_m) says that any intersection with
another arrow image is either the whole W-image or has at most one
point. The only size-two source is S(V,V), and its two points stay in
distinct H-components by the independently checked H-map injectivity.
These facts explain why the restriction loses no dangerous connectedness
case in these two stages, conditional on the already audited C.2(c_m).

The convexity program checks all proper larger-source images, not a sample.
For each vertex it computes intrinsic distances, then an ambient BFS
truncated at the intrinsic eccentricity. An additional Boolean records
whether **any** shortest path to a vertex leaves the image, so equal-length
outside paths are detected as well as strict shortcuts. If there were a
failure, a separate BFS on `(vertex, has_left_image)` states reconstructs
an explicit outside path of the asserted length. Componentwise tests on
point and edge components are tautological.

- Selected K2: 153 proper images, 6732 source BFS checks,
  21611862 ambient vertex visits, 11.846 seconds, no failures.
- Critical K3 top target: 891 proper images, 52272 source BFS checks,
  3455892 ambient visits; complete run 4.293 seconds, no failures.

## Induction ideas and limits

Pairwise connected intersections alone would be insufficient: three
subgraphs in a theta graph can have connected pairwise intersections
and a disconnected triple intersection. This motivated the full finite
intersection closure test.

Geodesic convexity would imply connectedness of all finite image
intersections, provided all component maps remain injective. It also
gives the proven fixed-interval lemma above. Gatedness is stronger and
can fail for two odd cycles joined along an edge; no gatedness claim is
made.

A possible metric proof would encode a path through quasi-filter copies
by its entrance/exit through f(S),g(S). Backtracking and opposite-sign
turns can be shortened through a convex overlap. The repaired full-circle
word has signed count one, but arbitrary winding still requires control.
The current argument has not converted that observation into a theorem
that all new copies remain convex. In particular, no selected finite
calculation is promoted to an all-stage claim.

The AKR agent separately develops a stronger marked-cycle counting
invariant and relative collapses of complexes obtained by attaching
protected first-stage cycle cells. This note does not claim that those
pointwise facts imply injectivity after category colimits.

## A verified limitation of a generic metric induction

Convexity and point-level boundedness alone do not ensure that a new
quasi-filter remains injective on connected components. This can be
seen outside C.1 in the following fully explicit graph example. Let T
be the two disjoint edges 0--1 and 2--3; let S be two isolated points;
let f=(0,2), g=(3,1). Both graph embeddings are component-injective,
and every image component is a convex singleton. The nontrivial point
transition relation consists of 0->3 and 2->1, hence is bounded and
has no cycle. Its action on the two graph components interchanges them.

Apply the repaired actual-path-size beta construction with k=3,s=13.
The resulting graph is the 26-cycle. In particular the two old components
of the alpha_0 copy become connected; the program prints a path of
length 13 between them. `code/finite_akr_graph_gluing.py` and `.out`
give all point labels, maps, edges, and the checked path. This configuration
is **not asserted to occur among the arrows generated by C.1**. It is a
counterexample only to the proposed generic preservation lemma with those
insufficient hypotheses. An all-stage proof must use source-specific
control of component-level partial transitions, or a different invariant.

The literature query `finite graph convex partial isometry cyclic
amalgamation extension` led to work on the extension property for partial
isometries (Solecki and later authors). No theorem from that literature
was applied to the specific repaired beta construction. The existence
of some finite isometric extension would not establish the property of
the prescribed target, even if its source were opened.
