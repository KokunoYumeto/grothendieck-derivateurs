# Second independent audit of universal AKR component injectivity

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026.
Reviewer: `finite_tests_literature`. No priority claim.

## Status

**Passed for every canonical actual-path-size repaired C.1 construction.**
I read `sections/akr_universal_components_draft.tex` in full, together
with `sections/akr_birth_cover_descent.tex`, the set-necklace threshold
in `sections/akr_component_necklace.tex`, and the cell-fibre/graph-colimit
part of `sections/akr_attachment_fixed_paths.tex`. I also inspected the
original definition of the point bounded-chain condition (4), printed
p. 375 of AKR, and the supplied prior construction record. The new proof
uses the already audited preservation of (4); it does not replace it
by an assumption about graph components.

After the independent audits the accepted proof was promoted to
`sections/akr_universal_components.tex`, with labels
`C:component-two-intersection`, `C:component-path-inflation`,
`C:universal-components`, and `C:universal-nontotal`. That is the
final proof file; the draft is retained as a historical record.

The three maintained assertions are H-injectivity, Helly for each
component cover at birth, and forbidden-component-pair routing by
**actual arrows**. Each has a separate role. The fact that old graphs
and incoming-arrow categories are permanent after birth makes these
fixed source-cover assertions legitimate throughout later stages.

## 1. The full intersection is retained in the descent

Let I be an intersection of two H-images with at least two elements.
If h does not factor through g, the inverse image of I under H(h)
contains no forbidden component pair. Its entire inverse image lies
in one generating H-cover image by Helly. Replacing h by he therefore
retains every element of I and introduces no element outside the old
H(h)-image. Its intersection with the H(g)-image is still exactly I.

Each unsuccessful factorization step strictly lowers source birth
rank, with V ranked below the original W. It cannot reach V while
retaining two components. At W the two components form a forbidden
pair for the singleton cover, so retaining them forces actual
factorization. At the stopping step the whole current H-image lies
in the H(g)-image and its intersection is I; hence that whole image
is I. Composing the actual descent and factorization arrows gives
`hu=gv` and `H(hu)(H(R))=I` exactly as claimed.

For a distinct parallel pair f,g with source S, a factorization
f=gq would make q an endomorphism of S. The generated construction
has only identity endomorphisms. Thus the descent has at least one
step and R is strictly older than S. The proof never attempts to
lift a singleton component intersection to equality of raw points.

## 2. The reduced component relation has the correct orientation

From `fu=gv`, the reduced relation is **v(r)→u(r)**. If an original
path has vertices D_0,...,D_(r-1) and source components C_i, its
internal match is `H(g)C_i=H(f)C_(i+1)`. Exact coverage of I and
injectivity of H(f),H(g) give a unique component of R with v-image
C_i and u-image C_(i+1). Therefore the reduced path has r-1
vertices. Its vertices remain distinct because their H(f)-images
were distinct. A nontrivial original cycle similarly supplies the
closing reduced transition and becomes a reduced cycle of the same
length. Induction on source rank rules out the cycle; it is not
assumed absent in order to define or prove the bound.

## 3. The endpoint of the lifted point path is genuinely new

For a reduced nonconstant point path x_0→...→x_(p-1), p>=2,
the actual span gives `g(x_i)=f(x_(i+1))`. Hence the original
point relation contains the walk

    f(x_0) -> f(x_1) -> ... -> f(x_(p-1)) -> g(x_(p-1)).

The first p vertices are distinct. If the final vertex equals
f(x_j) with j<p-1, the suffix closes a nontrivial point cycle,
contradicting condition (4). If it equals f(x_(p-1)), the preceding
match says this same point is g(x_(p-2)); injectivity of g then
contradicts distinctness of the last two x's. The special last-loop
case is necessary and is handled explicitly in the draft.

Thus every reduced nonconstant point path has one more vertex when
lifted, so `L_U(v,u)<=L_U(f,g)-1`. When the reduced relation has no
nonconstant path, its conventional maximum is one and f≠g gives
L_U(f,g)>=2, proving the same inequality. A component overlap of
size at most one permits no cycle and at most three path vertices.
For larger overlaps the source induction gives

    r-1 <= L_H(v,u) <= L_U(v,u)+1 <= L_U(f,g).

Together these prove the asserted universal bound `L_H<=L_U+1`.

## 4. New H-copy injectivity comes before the routing step

At an old stage the three structural hypotheses imply the path
bound for every old pair, by the preceding separate source-rank
induction. For the defining pair of a new target, L_U<=n therefore
implies L_H<=n+1. The C.1 inequalities give `s=4k+1>=15n` and
`k>=n+1` for every allowed positive n.

The graph attachment is the strict graph colimit by its actual
vertex and edge fibres. Taking graph components preserves this
colimit: components are the quotient of the vertex set by the
endpoint equalities, so this is a statement about commuting set
colimits, not a false discrete-graph adjunction. Its component set
is consequently the set necklace of H(f),H(g).

These old maps are injective, their partial relation is acyclic,
and every path has at most n+1<=k vertices. The actual-path-size
set-necklace result therefore proves all new H-copy maps injective,
with exact adjacent overlaps and proper visibility intervals of
length at most 2n. Only **after** this step does the proof use those
overlaps to extend routing. The parameter inequalities also give
`2k<=s-2(n+1)` and `s>3(2n)`, respectively the shortest-arc range
and the circular-interval Helly bound.

## 5. Component routing still factors entire actual arrows

Write h=alpha_j h* and g=alpha_i g*. If two fixed forbidden source
components have images in H(g), their two images are visible in
copies j and i. The component visibility result places them in the
next neighboring overlap along the shortest index arc. Exactness
of that overlap and injectivity of H(alpha_j) put their old
H(h*)-images in H(phi_r)(H(R)). The old forbidden-pair assertion
then gives an **actual** factorization h*=phi_r l.

The **actual** necklace equation
`alpha_j phi_r=alpha_(j') phi_t` reroutes the whole h to the next
copy. Repeating reaches copy i. Injectivity of H(alpha_i) and the
old routing assertion then factor the entire actual h through g.
At no point is equality of H-maps promoted to equality of arrows.

The new source's own routing base case is immediate: it has only
its identity as an outgoing arrow within its birth stage, and every
proper incoming map factors through a birth copy, which cannot
contain a forbidden component pair. Sums have disjoint covers and
reduce routing to one summand. Distinct new targets have no arrows
between them. These checks close the simultaneous stage induction
without using the new routing assertion to prove the H-injectivity
that was needed to establish it.

## 6. Consequence for the fixed-path kernel and C.1

The previously proved fixed-set descent gives an actual arrow
e:R→S whose image is the fixed point set of a defining pair, unless
that set is empty. The AKR edge-routing invariant makes its graph
the induced image of G_R. Universal H-injectivity of e says that
this image meets each component of G_S in at most one of its own
components. Hence the fixed subgraph is connected in every source
component that it meets, exactly the sufficient hypothesis for the
already proved fixed-path kernel theorem.

Each attachment therefore has zero old cycle-colimit kernel. Sums
also have zero kernel; targets born in one stage give independent
attachment relations, so the full stage map is injective. The two
first-stage protected cycles have augmentation-one generators and
give the nonzero kernel element kappa_+−kappa_- in the binary H_2.
Every finite nerve chain lies in a finite stage. Thus this element
survives the increasing union, proving that every canonical repaired
C.1 category is not total.

The scope is all admissible C.1 numerical choices and relabelings,
not merely selected large targets. No conclusion is extended to the
unrepaired common-n construction where exact overlaps fail.

## 7. Optional enlargement by unused underlying points

The later added paragraph was checked separately and its mathematical
argument is valid. A point is represented when it is the value of a
V-arrow. Generated arrows preserve and reflect representedness:
assuming this for old arrows, both endpoints of every defining point
transition have the same status as its source point. Each entire
transition path therefore has constant status. Beta identifications
stay in one such whole path; fixed and private pieces do not mix
statuses either. A newly adjoined point outside all generating images
is unrepresented. This proves the induction, including reflection.

Restricting to represented points consequently retains whole actual
paths and all visibility identities. It does not reproduce the invalid
domain-range truncation warned about in the supplied repair. The
actual binary graph has exactly those represented vertices, so its
strict colimit and component-cover arguments are unchanged.

For a fixed represented vertex set, the point descent remains actual
arrow descent. If two composites differ only on unused points, they
are still distinct actual arrows and may be descended further; the
nonempty fixed represented subset persists. At V nonempty agreement
forces equality of the actual maps. Stopping therefore gives exactly
the represented-point image required for the fixed subgraph. Keeping
L_U on the full underlying sets preserves the inference f≠g ⇒ L_U>=2.

I requested one expository adjustment if the final corollary is meant
to include this optional enlargement: cite the represented fixed-set
version from the added paragraph, rather than literally invoking the
canonical full-underlying-point equalizer statement. The canonical
theorem and its proof need no such adjustment. The requested wording
has been incorporated into the final proof file named above.
