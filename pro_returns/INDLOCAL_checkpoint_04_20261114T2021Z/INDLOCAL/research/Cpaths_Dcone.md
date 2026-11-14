# The cone test for the remaining D uniformity question

This note proves two facts relevant to the relative-cylinder experiments.
It makes no assertion that the cone inclusion used below is a Thomason
cofibration in the particular contractible-cylinder example.

## 1. A four-step relative comparison after the explicit cone inclusion

For a small category `L`, define `K(L)` to have two copies `L_0,L_1`
and one additional object `x`. Between the copies set

`Hom((a,0),(b,1))=Hom_L(a,b)`.

There are no arrows from the upper copy to the lower copy, no arrows
between `x` and the lower copy, and one arrow from `x` to each object
of the upper copy. Composition between the copies uses composition in
`L`; composition starting at `x` is unique. Thus

`K(L)=(L×[1]) ∐_{L×{1}} L^◁`,

where the new initial object belongs to the upper copy's cone. This is
the functor `K` of Meier–Ozornova, *Fibrancy of partial model categories*,
§4, Remark 4.1 (primary PDF opened at the complete definition and proof).

The lower inclusion `L_0 -> K(L)` is an actual Dwyer map. It is a full
sieve; its generated cosieve is `L×[1]`; projection to `L` is a right
adjoint to the lower inclusion on that cosieve. Its counit is the
identity on the lower copy and the given lower-to-upper arrow elsewhere.

The endofunctor `U` fixing `x` and sending both copies of each object
and arrow to the upper copy has transformations

`id_{K(L)} -> U <- const_x`.

The first transformation uses the lower-to-upper arrows and identities;
the second uses the unique arrows from `x`. Consequently `K(L)` is
categorically contractible. For weakly contractible `BL`, the actual
inclusion `L -> K(L)` is therefore a weak equivalence.

Put `P_n=c Sd² Delta^n` and `A_n=boundary P_n`. Let `p,q:P_n->L`
be any two functors agreeing on the common boundary functor `h:A_n->L`.
Then the lower-copy composites are connected relative to `A_n` by four
natural transformations, with orientations `+,−,+,−`, in `K(L)`.

To prove this, write `T={0,...,n}`. The interior objects of `P_n`
are the center flag `{T}` and the flags `A∪{T}` for nonempty boundary
flags `A`. Define `P^up` to use the lower copy of `p` on the boundary
and the upper copy on the interior. Every mixed arrow goes from the
boundary to the interior and is mapped to the corresponding cross-copy
arrow. Define `Q^up` in the same way. There are transformations
`p->P^up` and `q->Q^up`, stationary on the boundary.

Define `R:P_n->K(L)` as follows:

- On the boundary use `h` in the lower copy.
- Send the center `{T}` to `x`.
- Send a noncentral interior flag `A∪{T}` to `(h(A),1)`.

Inclusions of noncentral interior flags are sent to the arrows of `h`.
An arrow from a boundary flag `B` to `A∪{T}` has `B⊆A` and is sent
to the cross-copy arrow represented by `h(B⊆A)`. Arrows out of the
center are sent to the unique arrows from `x`. These prescriptions
preserve compositions. There are transformations `R->P^up` and
`R->Q^up`: their rim components are `p(A⊆A∪{T})` and
`q(A⊆A∪{T})` in the upper copy, their center components are the
unique arrows from `x`, and their boundary components are identities.
The squares on the rim are the functoriality squares of `p,q`; the
center squares commute by uniqueness. This proves the actual zigzag

`p -> P^up <- R -> Q^up <- q`.

For `n=0`, the boundary is empty and the same construction consists of
the two upper-copy objects and the new apex, so it remains valid.

Apply this to the corrected D.11 cylinder quotient
`L=c Sd² C_n`. Its nerve is weakly contractible by the explicit
relative deformation retraction of `C_n` and the Thomason comparison.
The above map `L->K(L)` is a weak Dwyer map. Compose it with a
Thomason fibrant replacement `K(L)->F`. The two quotient end maps now
have the displayed four-step relative comparison in the fibrant target
`F`. Thus the computed lower bounds inside the finite quotient are
not preserved by arbitrary weak Dwyer extensions to fibrant targets.
The assertion concerns these actual composites and the exhibited
four transformations.

## 2. Cone units are not Thomason cofibrations for all cofibrant inputs

Let `L` be the four-element crown, with two lower elements, two upper
elements, and all four arrows from a lower to an upper element. This
is cofibrant: it is a finite one-dimensional poset, covered by
May–Stephan–Zakharevich, Proposition 6.4. That proof and Proposition 6.2
were read in the supplied primary full text.

Push out `L_0->K(L)` along `L->*`. The result is the poset

`S^0 ⊕ L`,

with two incomparable minimum elements and the old upper copy of `L`
above both. To check the category pushout, the Dwyer pushout formula
gives a unique arrow from the collapsed lower object to every upper
object. The new apex also has one arrow to each upper object. There
are no arrows between the two minima, and the upper morphisms are
exactly those of `L`. Hence this is the six-element three-level poset
with two elements at each level and every comparison between different
levels. Proposition 6.2 of that primary paper proves this poset is not
Thomason-cofibrant.

The point is cofibrant. If the crown's cone inclusion were a Thomason
cofibration, its pushout `*->S^0⊕L` would be a cofibration and would
make that six-element poset cofibrant, contradicting Proposition 6.2.
Thus this particular cone inclusion is not a Thomason cofibration.

Meier–Ozornova Lemma 4.2 does establish the requisite lifting for cone
units on subdivided horns: `c Sd² Lambda_i^n -> K(c Sd² Lambda_i^n)`
is a retract, as an arrow, of the generating horn inclusion. Its
explicit retraction was read. That special result does not identify
the cone unit of the contractible quotient `c Sd² C_n` with one of
those retracts. No such identification has been established here.

## 3. Every corrected quotient is strongly contractible

For every `n>=0`, the quotient `L_n=c Sd² C_n` of the corrected
relative cylinder is categorically homotopy equivalent to a point.
The following explicit endofunctors prove this for all dimensions.

Use the notation `pi:[n+1]->[n]` identifying `n,n+1`, and
`W=pi^{-1}(boundary Delta^n)`. Put `Q=c Sd² Delta^{n+1}`.
Its objects are nonempty flags of nonempty faces. Starting with each
face `S`, insert the vertex `n` into every face containing `n+1`,
processing original face cardinalities from `n+2` down to one.
For each cardinality use an intermediate flag retaining both the old
and the new image of its face, then delete the old image. Next delete
`n+1` from these images, processing original cardinalities from one
to `n+2`, with the same retain-both intermediate stage.

These are functors on flags. At insertion, each larger affected face
already contains `n`; at deletion, each smaller affected face has
already lost `n+1`. Thus old and new faces in every intermediate
flag remain comparable. Repeated image faces are deleted as repeated
members of a set. Inclusion of flags is preserved because the image
of each original face is prescribed independently of the flag.
At every second step the intermediate flag contains both neighboring
flags, giving `4(n+2)` alternating natural transformations.

Every face and every intermediate image have the identical `pi`
image. Hence these functors preserve `c Sd² W` and commute there
with the map to `boundary P_n`. They descend, by the actual category
pushout, to endofunctors of `L_n` fixing its boundary. Their first
endofunctor is the identity. Their last sends `n+1` to `n`, so is
exactly `j r`, where `r:L_n->P_n` is induced by `pi` and `j:P_n->L_n`
is the first end-facet inclusion. The identity `r j=id` holds strictly.

Finally `P_n` contracts by the two comparisons from its identity
to the endofunctor adjoining the full face to a flag, and from the
constant full-face flag to that endofunctor. Composition with `j,r`
therefore extends the preceding sequence to an actual contraction
of `L_n` in `4(n+2)+2` natural transformations.

The independent verifier `code/cpaths_dcone_checks.py` checks every
quotient endofunctor, every order relation, every boundary identity,
and both comparisons of the final contraction in dimensions one and
two. It also gives separate beat-point certificates:

| Dimension | Quotient objects | Beat deletions | Core objects | Sweep and final contraction |
|---|---:|---:|---:|---:|
| 1 | 21 | 20 | 1 | 14 transformations |
| 2 | 113 | 112 | 1 | 18 transformations |

The JSON output records the actual deleted point and its retraction
witness at every step. Each deletion is verified as a monotone
idempotent retraction, with its pointwise natural transformation.
The general flag argument above supplies the unbounded statement.
This contraction alone supplies no lifting property for
`L_n->K(L_n)`; that cofibration question remains separate from the
explicit comparisons proved here.
