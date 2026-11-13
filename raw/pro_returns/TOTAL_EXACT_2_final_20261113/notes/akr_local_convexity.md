# Local convexity and first-stage safe sources

Status: complete proof in `sections/akr_local_convexity.tex`. These
statements concern every admissible repaired C.1 construction. The
subsequent independently audited proof in
`sections/akr_universal_components.tex` settles universal C.1.

## Counting an outside excursion

For an arrow image `h(Y)` at stage `m`, take a simple binary graph path
with its two endpoints inside and all internal vertices outside. If its
length is `r`, the `r` corresponding W-arrows are distinct. None factors
through `h`; hence each meets `h(Y)` in at most one actual point, by
`(c_m)`. The union of their actual W-images outside `h(Y)` contains at
most `r-1` internal path vertices plus `r` third points. Therefore

`a_m r <= 2r-1`, or `r >= 1/(2-a_m)`.

This proves local strong convexity through the integral radius
`R_m = ceil(1/(2-a_m))-1`. Since every `a_m>3/2`, all actual arrow
images are uniformly two-convex. The assertion is about simple paths
and geodesics, not arbitrary walks with backtracking.

## Fixed sets

For fixed source vertices `u,v` at distance at most `R_m`, both maps
carry the entire finite shortest-path interval bijectively onto the
same target interval. Local convexity is enough: a target shortest
path has length no larger than the source distance and lies in either
image; inducedness lifts it. The permutation `g^{-1}f` of the source
interval has no nontrivial cycle by AKR property (4), so it is the
identity. Hence every source shortest path between the two fixed
vertices is fixed.

In particular any source whose binary components have diameter at
most two is safe at every later stage. Component injectivity is not
needed for this argument.

## Every K1 object is a safe source, forever

The first-stage graph classification is exact for all admissible
necklace lengths:

- identity targets and sums: isolated vertices, edges, or stars;
- equal pair `v1,v1` or `v2,v2`: one star plus isolated third points;
- equal pair `v3,v3`: a matching plus an isolated point;
- a distinct pair involving `v3`: a matching, one two-edge star,
  and isolated vertices (all component diameters at most two);
- the two pairs `v1,v2` and `v2,v1`: the protected circle plus
  isolated third points.

All cases except the two protected sources follow from the uniform
two-convexity lemma. For a pair of distinct arrows from a protected
source, two nonadjacent fixed marked vertices would factor one arrow
through the other. Since the source has only the identity endomorphism,
the arrows would be equal. The fixed subset of the circle is therefore
at most one edge and is connected; isolated components cause no issue.

Thus no later attachment whose **domain** is an object of K1 can kill
any old binary H2 class. This strengthens the prior result about the
first class surviving the second stage: the target and the later
stage are unrestricted, and the whole old colimit K is preserved.

## Subsequent resolution

The local argument alone confines any possible killing attachment
to a later source with a component of diameter at least three.
The subsequent birth-cover/component induction rules out such
attachments altogether: every fixed subset is an existing arrow
image and every actual arrow is injective on binary components.
Hence every exact fixed-path attachment kernel vanishes, and the
initial binary H2 class survives every admissible infinite continuation.
