# Invariant orders on finite-support orbits

AI-produced by GPT-6 Astra, ChatGPT Pro mode, 17 November 2026.
This is a proved structural lemma using the audited R17 free-amalgamation,
homogeneity and finite-closure facts. It does not by itself prove the
C_delta free-monoid comparison. No external classification theorem is used.

## Statement

Let U be the rich ordered predimension limit, G=Aut(U), and let B be
a finite closed substructure (possibly empty). For a finite closed
extension B≤F, let Emb_B(F,U) be the G_B-orbit of closed embeddings
fixing B. Every G_B-invariant strict linear order on this orbit is a
signed lexicographic order on a finite list of vertex coordinates.

More precisely, there are vertices p_1,...,p_r of F and signs
epsilon_i in {+1,-1} such that, with

    B_0=B,   B_i=cl_F(B_{i-1} ∪ {p_i}),

one has p_i outside B_{i-1}, B_r=F, and two distinct embeddings f,g
are compared by the sign epsilon_i times the ambient-order comparison
of f(p_i),g(p_i), at the first index where these images differ.
Coordinates already forced by closure are skipped.

By R17 every open subgroup of G is a pointwise stabilizer of a
finite closed structure. Consequently this describes every continuous
transitive G_B-set carrying a G_B-invariant linear order, including
each G_B-orbit in the linearly ordered prefix cuts of a fixed monoid
element. The last application is only orbitwise: it does not classify
interleavings between different cut orbits or their behavior under
monoid multiplication.

## 1. The close-copy comparison is a Boolean voting rule

Write the vertices of F\B in their ambient order as p_1,...,p_m for
this paragraph only. Fix m disjoint small ordered intervals, one for
each such coordinate, inside the corresponding gaps of B. Consider
two copies of F, freely amalgamated over B, whose i-th vertices lie
in the i-th interval. Their joint isomorphism type over B is determined
exactly by the m signs comparing the corresponding vertices: all
cross-coordinate comparisons are already fixed by the disjoint
intervals, and there are no cross-copy hyperedges.

Thus the invariant order assigns a function

    epsilon : {-,+}^m -> {-,+}.

Reversing the two copies reverses every sign, so epsilon is odd.
Reverse the invariant order temporarily if needed so that the
all-positive sign vector has positive output.

Three freely amalgamated copies can be placed so that, independently
at each coordinate, their three vertices have any prescribed one of
the six linear orders. This follows from free amalgamation over B
and arbitrary order interleaving in each gap. Therefore epsilon,
applied pairwise to these coordinate orders, always gives a transitive
linear order on the three copies.

## 2. Elementary finite dictatorship lemma

Call A⊆{1,...,m} decisive when epsilon is positive on the sign vector
that is positive exactly on A. The full set is decisive, the empty
set is not, and exactly one of A and its complement is decisive.

If A and D are decisive, choose three formal alternatives x,y,z
with the following coordinate orders:

* on A∩D: x<y<z;
* on A\D: z<x<y;
* on D\A: y<z<x;
* outside A∪D: z<y<x.

Then the coordinates with x<y are exactly A, those with y<z are
exactly D, and those with x<z are exactly A∩D. Transitivity shows
that A∩D is decisive. A decisive set cannot be contained in a
nondecisive set, since intersection with the decisive complement
would make the empty set decisive. Hence the decisive sets form an
ultrafilter on a finite set. Its intersection is nonempty and contains
exactly one coordinate: two distinct coordinates can be separated by
a set and its complement. Thus it is the principal ultrafilter at
one coordinate p.

The comparison of close independent copies is therefore exactly the
comparison of their p-coordinates, or its reverse before the temporary
normalization. This proves the first selected coordinate and its sign.

## 3. From close copies to arbitrary copies

Let f,g be arbitrary copies over B with f(p)≠g(p). They need not be
independent and may overlap. Put both copies inside a finite closed
Y⊂U. Represent the finite ordered set Y by distinct real numbers.
Interpolate the coordinate tuples linearly from f to g, keeping B
fixed. Each tuple remains strictly ordered: every coordinate gap is
a convex combination of two positive gaps. Since there are finitely
many gaps, they have a common positive lower bound along this path.

Choose a sufficiently fine finite partition of the path. For each
intermediate tuple choose a separate formal copy of F over B.
Small perturbations avoid every accidental equality with Y or another
new vertex, preserve all coordinate inequalities, and keep the selected
p-coordinates strictly monotone. The partition can be chosen fine
enough that each consecutive pair has its corresponding coordinates
in disjoint ordered clusters; that is exactly the close-copy situation
of Section1.

Freely amalgamate all these new copies with Y over B. Their prescribed
linear interleaving extends the order on every factor, so this is an
allowed finite strong extension of Y. Embed it into U over Y by the
rich extension property. Each new copy is free from Y and the others
over B. Thus every consecutive pair, including the two endpoint
pairs, is a close independent pair. All comparisons have the same
direction determined by the monotone p-coordinate. Transitivity gives
the claimed comparison of f and g. Therefore the first coordinate
controls every pair for which its values differ, independently of any
hyperedge or overlap pattern between those copies.

## 4. Equality of a coordinate and recursion

Suppose f(p)=g(p). Set D=cl_F(B∪{p}). Closed embeddings preserve this
finite closure: since their images are closed in U, the closure of the
image set in U equals the image of its closure in F. Thus f(D)=g(D).
Both restrictions are increasing isomorphisms from the same finite
ordered D to that same image, so they agree pointwise.

The fibre of the p-coordinate is therefore a transitive G_{f(D)}-set
of copies of F over f(D). Restrict the invariant order and repeat the
preceding argument with base D. Homogeneity transports the resulting
coordinate choice and sign between fibres. Each step strictly enlarges
the finite closed base, so the process terminates at F. This gives
the asserted signed lexicographic rule.

## 5. Exact scope for prefix cuts

For a locally free, cancellative and conical G-monoid S, the prefixes
of a fixed word s are linearly ordered by Levi's lemma. G_B acts on
this chain whenever it fixes s. Any cut t has an open stabilizer in
G_B; by R17 it is G_F for a finite closed F containing B. The orbit
of that cut is therefore one of the above embedding orbits, and its
induced prefix order has the proved form.

The remaining comparison (NS)/G -> N(S_G) also involves concatenation
and contextual identifications. The next section adds a cross-orbit
order statement, but it still does not assert that the full monoid
action factors through the ordered-set reduct or through Delta_inj.

## 6. Cross-orbit interleavings

The following refinement was suggested independently in the localization
thread and checked here. Let a G_B-invariant linear order be given on a
union of two transitive continuous orbits O_1,O_2. Assume first neither
orbit is a singleton. Let p and q be their respective first selected
vertex coordinates from the proved classification, with signs sigma_1,
sigma_2. Then exactly one of the following occurs:

1. Every element of one orbit precedes every element of the other.
2. The p- and q-coordinates lie in the same gap of B, sigma_1=sigma_2,
   and elements with different p- and q-values are compared by that
   common signed ambient order. When the values coincide, restrict to
   the common coordinate fibre and repeat over its finite closed hull.

If one orbit is a singleton, the orbits are separated. This statement
does not require that the two supports have the same hypergraph type.

**Density fact.** Fix a finite closed H containing B. For any realized
G_H-orbit in O_1 whose p-coordinate is not in H, its p-values are dense
in their gap of H. Indeed take the finite closure K of H and a chosen
representative support. Freely copy K over H inside an ambient closed
structure containing any two prescribed bounds in that gap. Its new
vertices can be interleaved so that the new p-coordinate lies between
the bounds. Embed this strong amalgam into U and extend the isomorphism
of the two K-copies to an automorphism fixing H. This proves the
density assertion without assuming that an arbitrary vertex type can
be moved independently of its closure.

**Cuts fixed by a finite support.** For y∈O_2 let H be its support over
B and set D_y={x∈O_1:x<y}. This initial subset is G_H-invariant. It
cannot cut the p-values strictly inside any gap of H. If it contained
some x and omitted some x' in that gap with p(x)<p(x') in the signed
direction, the density of the G_H-orbit of x would move x beyond x'
while keeping it in D_y, contradicting initiality. The same argument
handles a boundary at an unrealized H-free point, or a partially
included fibre at such a point. Thus a nontrivial cut has a unique
boundary p=h at a vertex h of H lying in the relevant B-gap. All
elements on the earlier side of that coordinate are included, all on
the later side are excluded, and only the fibre p=h remains to decide.

The cut cannot be a nontrivial constant as y varies: a constant D_y
would be a G_B-invariant initial subset of the transitive O_1, hence
empty or all. The trivial cuts mean that the two orbits are separated.
In the nonseparated case the boundary vertex belongs to H\B. By
equivariance it is one fixed vertex-coordinate selector on copies of H.

**The selected boundary is the leading coordinate of O_2.** The map
y↦D_y is monotone for the order on O_2. If its boundary selector were a
coordinate h other than O_2's first selected coordinate q, choose two
close independent copies of H over B with opposite comparison signs
at q and h. Free amalgamation permits these signs independently, even
if h lies in the finite closure of q: the copies are disjoint outside
B. Their order in O_2 is governed by q, while strict inclusion of
their cuts is governed by h; strictness follows by choosing an O_1
p-value between the distinct boundary values. This contradicts
monotonicity. Hence the boundary selector is q. The same argument with
the same selector shows sigma_1=sigma_2. Their two coordinates must be
in the same B-gap, since otherwise every cut would be trivial.

Finally if p(x)=q(y)=z, both support embeddings agree on the finite
closed hull of B∪{z}. Each nonempty fibre is a transitive orbit for its
pointwise stabilizer. Apply the same statement recursively over that
closed base. If a fibre becomes a singleton, transitivity of the other
fibre forces separation there. Every recursion enlarges both relevant
finite closed supports until it terminates. This proves the asserted
pairwise lexicographic interleaving rule.

This determines comparisons between any two cut orbits. Turning these
pairwise rules into a global model compatible with concatenation, and
then proving the orbit-nerve/monoid-coinvariant comparison, is still a
separate missing step. No contractibility conclusion is claimed here.

## 7. Closest primary literature found

Bodirsky, Bodor and Marimon, *Taking model-complete cores*,
arXiv:2512.21278v1 (2025), Lemmas 4.34–4.35, printed pp.33–35,
classify the corresponding definable orders on increasing rational
tuples as signed lexicographic orders. Their complete proofs were
opened in the institutional primary PDF at
https://fis.tu-dresden.de/portal/files/81089088/2512.21278v1.pdf.
The local separated-coordinate argument and finite interpolation are
therefore known in that pure-order setting. The proof above checks
the additional closed-support and free-amalgamation steps directly;
the source is not being credited with the C_delta extension or any
monoid conclusion. The search log is in `CD_sources.md`. No priority
claim is made.
