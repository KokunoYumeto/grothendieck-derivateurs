# Generic ordering obstruction after checkpoint02

New files only; the included checkpoint02 sections were not modified.

The claim that every repaired beta target of increasing finite-order
maps is orderable at every k bounding the point-path sizes is refuted
by `C:ordered-necklace-short-warning` in
`sections/akr_ordering_counterexample.tex`.

For any k≥2 set d=2k, s=4k+1, M=d(d+1), and use ordered sets
S={0,…,M}, T={0,…,2M+s} with f(r)=2r,g(r)=2r+s. Their images are
disjoint, so every nontrivial point path has two vertices. The cyclic
overlap labels decrease by d in the first d+1 copies and increase by
d+1 in the final d copies. Every resulting incoming old point is
exactly one smaller than the outgoing old point. The neighboring
identifications concatenate these into an s-cycle of strict
precedence constraints, which no target order can satisfy.

The exact verifier `akr_ordering_counterexample.py` uses k11,n3,s45,
so the numerical C.1 ratio is also satisfied with a0=2,a1=8/5. It
builds the507-point source,1058-point old target,24795-point repaired
target and the complete45-edge contradiction cycle. The output and
JSON are retained alongside the script.

This is generic ordered-set data, not a parallel pair exhibited in an
actual C.1 stage. It does not alter the proved selected large-target
counterexample: for each fixed ordered pair, the ordering proposition
still holds for all sufficiently large k. It does show why an
all-choice proof cannot simply remove that proposition's largeness
condition without using additional structure of the generated arrows.
