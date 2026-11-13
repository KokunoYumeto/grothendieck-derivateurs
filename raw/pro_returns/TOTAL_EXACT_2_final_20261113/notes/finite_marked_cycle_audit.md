# Independent audit of the marked-cycle theorem

Auditor: finite-tests/literature agent, separately from the author of
`sections/akr_marked_cycles.tex`. AI-produced; no priority claim.

## Sources actually inspected

I read the original scan of AKR1981 at printed pp.379--380 for (9)--(11),
p.384 for Construction C.1's exact numerical assumptions, and every
step of C.2 at pp.385--389. Pages 379,380,384--388 are available in the
AKR agent's `code/akr_source_images/`; page389 was additionally rendered
to `sources/finite_AKR_p389.png`. The literal restriction assertion in
B.6 is not used: the current theorem assumes the repaired maps whose
(10),(11) were separately established in the preceding work.

## Audit conclusion

The threshold-three marked-set routing and the weighted counting
induction are valid. Mixed sources P+,P- cause no loss, because every
factorization keeps the source type and therefore its weight. The
relative two-cell collapse and the pointwise free quotient/split-monic
arrow conclusion are also valid. This is a mathematical audit of the
induction, not a conclusion inferred from finite programs.

The draft's phrases 'applies verbatim' and 'sweep' should be expanded
to show the steps below. I sent that request to the author. The trivial
comparison-arrow case g=1_X should be stated separately: routing is
immediate, and the weighted hypothesis is impossible for a nonempty
family because all marked sets have at least45 points.

## Exact routing check

Suppose X is a new quasi-filter target, comparison g=alpha_0 g*, and
h=alpha_j h* has at least three marked points in g(Y). Choose a shortest
index arc from j to0. Its length is at most2k, whereas s-2n>=2k+1 since
s=4k+1 and k>=n. At each step, property(10) contains the overlap with
alpha_0(T) in the overlap with the next neighbor on that arc. By (11)
that neighboring overlap is alpha_j phi_p(S) for an old defining-pair
map phi_p:S->T. Pulling back the three marked points along the injective
alpha_j gives at least three marked points of h*(S_mark) in phi_p(S).
The old marked routing assertion factors the **entire typed arrow** h*
through phi_p. The neighboring quasi-filter equality then moves h into
the next copy. Repetition reaches copy0. Pulling back along alpha_0 and
applying old routing to g*,h*_0 proves factorization through g itself.
The argument never requires that a source be W or have cardinality3.

## Exact weighted sweep check

Use source's first-available-copy partition H_0,...,H_{s-1}. Give each
typed arrow weight w_i=s_type-2. The s/(3n) consecutive disjoint blocks
of3n indices partition the whole weighted family. A minimum-weight
block beginning j0 therefore has weight at most (3n/s) times the total.
Discard it, retaining a set L. Reassign retained arrows by first available
copy in the order

`0,1,...,j0-1, s-1,s-2,...,j0+3n`.

This is exactly the source's sets L_t. It covers L because every retained
arrow had an original H-index outside the discarded block.

If j0>0, the initial batch lies in copy0 and old weighted counting applies
directly against g*. If j0=0, the initial batch lies in copy s-1. Its
marked intersection with the overlap alpha_{s-1}(T) cap alpha_0(T)
has at most two points for each member: three would route that arrow
into copy0, placing its first index in discarded H_0. Property(11)
expresses this overlap through one old phi_q, so old weighted counting
counts at least (a_m/a_1) times the batch weight outside it, and hence
outside g(Y).

For a forward batch at t<j0, all earlier copy overlaps are contained in
alpha_{t-1}(T) cap alpha_t(T), by (10), because t<=j0-1<s-2n. An arrow
in the new batch cannot meet this neighboring overlap in three marked
points: old routing would put it in the already available preceding
copy, contradicting its assignment. Pulling back (11) again lets old
weighted counting count new marked points, disjoint from everything
previously counted and from g(Y).

For a backward batch at r=s-t+j0-1, every earlier processed index lies
in the forward cyclic interval from r+1 through r+(s-2n). The largest
possible forward distance to a processed forward index is s-3n-1;
the distances to processed backward indices are smaller. When j0=0,
the comparison copy0 is separate from those processed indices; its
distance from r is at most s-3n, which is also at most s-2n. Thus (10)
contains all prior overlaps in alpha_r(T) cap alpha_{r+1}(T). The same
routing and counting argument applies. For the first backward batch
r=s-1, its neighbor0 is either already processed (j0>0) or in the
discarded H_0 block (j0=0), exactly the cases above.

Adding the disjoint new-point contributions gives
`(a_m/a_1) sum(retained weights)`. Since `3n/s <= 1-a_{m+1}/a_m`,
this is at least `(a_{m+1}/a_1) sum(all weights)`. Different types do
not affect any overlap inclusion, source-preserving factorization,
disjointness, or weighted averaging step.

## Disjoint sums and unconditional counting

Different summands have disjoint underlying points. In the comparison
summand apply the old relative bound. In any other summand choose one
marked arrow h_r as comparison. Each other typed arrow meets the full
image h_r(P_r) in at most two marked points: otherwise routing yields
an arrow P_i->P_r. Such arrows are absent between the two distinct
fresh first-stage objects, and End(P_r)={identity}; a same-type
factorization would force equality of arrows. Old relative counting
then bounds the union of the other marked sets outside h_r(P_r), and
adding the s_r points of h_r's marked set gives the unconditional
weighted bound. This argument works for different s+ and s- as well.

## Constants and collapse

At stage1, each P source has just its identity arrow into that stage,
and proper incoming V/W maps meet its marked circle in at most2 points.
The marked graph is a simple s-cycle, with an augmentation-one integral
cycle of coefficients plus/minus1. An active point path has2 vertices.
C.1 requires3n to divide odd s, so n is odd and n>=3. Its numerical
ratio is an integer strictly greater than4, because a1>3/2 and a0=2.
Thus s>=45 for either type. Also a_m/a1>3/4, whence
`(a_m/a1)(s-2)>s/2` for every type.

The strict half-incidence inequality gives a private marked vertex in
every finite family of protected circles. A boundary edge incident to
that vertex belongs to no other protected cell. Since each boundary
is embedded, this is a regular free face; removing the cell and edge
is an elementary collapse, and other cell boundaries remain intact.
Repeating gives a graph, hence the quotient cycle group is free abelian.

Relative to g(C_Y), the new cells are precisely typed arrows that do
not factor through g. Routing bounds their marked intersection with
the full image g(Y) by2, and relative counting gives a private marked
vertex outside g(Y). Its free edge is outside the old subcomplex, so
all collapses are relative. The final pair consists of the old complex
plus only0- and1-cells. Its first homology contains the old first
homology with free abelian cokernel (the extra cycle group of the
graph on old components). Therefore the induced map on M is a split
injection. No natural compatible splitting is supplied or needed.

## What remains unproved

These arguments prove pointwise and individual-arrow statements. They
do not show that colim F->colim K is injective. The boundary from T_1(M)
in the displayed long exact sequence can still, in principle, hit the
protected difference. Neither the weighted count nor the relative
collapse alone removes that colimit obstruction.

## Independent audit of the split-monic and free-group counterexamples

I also checked `C:split-monic-counterexample` and
`C:free-group-counterexample` in `sections/akr_links.tex`. Both proofs
are correct, and they decisively rule out the idea that the preceding
pointwise/individual-arrow conclusions alone make M colimit-acyclic.

For Q=coker(D:P_W->P_V^2), the already proved private-incidence property
makes D injective. Thus this is a projective resolution of length one;
on colimits its differential is zero from Z to Z^2, yielding T1(Q)=Z
and Ti(Q)=0 for i>=2.

For any arrow g:Y->X, every W-column not factoring through g meets
the full old point image in at most one point. Relative counting gives
more than3r/2 outside points for any family of r such columns. Since
there are at most3r incidences, one outside point belongs to precisely
one column. At that point the column's two coordinates are (-1,-1),
(1,0), or (0,1). A unit coordinate gives a row supported in that
column alone. Row elimination clears that column without changing
any other column. Repetition gives an integral unit-pivot reduction of
the relative matrix; its cokernel is free and its kernel zero. The
kernel--cokernel exact sequence then proves Q(g) split injective with
free cokernel. All matrices are finite at each X.

For the group version, the relator associated with h is
`x_(hv2,1) x_(hv1,1)^(-1) x_(hv3,2) x_(hv1,2)^(-1)`.
At a private point one coordinate generator occurs exactly once in
that relator and no other remaining relator; at hv1 the two coordinate
generators are distinct. Solving for that generator and removing the
relator is a Tietze elimination that leaves all other relators unchanged.
In the relative argument the private point is outside g(Y), so the
generator is new and absent from every old relator. Eliminating all
new relators fixes the entire old presentation and leaves extra free
generators. Hence the natural old group map is a free-factor inclusion,
not merely a homomorphism abstractly isomorphic to one. Abelianization
recovers Q exactly.
