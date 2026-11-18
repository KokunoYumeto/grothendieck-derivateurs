# A free-limit criterion for the C_delta comparison

Working note, GPT-6 Astra, 17 November 2026. The propositions below are
proved from the all-action reduction in R17. They rule out a class of
candidate counterexamples. They do not settle whether every FreeMon
diagram over C_delta passes its comparison.

## 1. Setup and precise input

Work in the concrete category A of all nonempty finite closed
substructures of the rich countable limit U, with all closed embeddings
as arrows. This is equivalent to C_delta. Let G=Aut(U), and let I be the
directed poset of these same substructures with inclusion arrows only.
The R17 proof `predimension_totality_reduction.tex` was reopened in full
for the following uses:

* Condition I synchronizes finitely many arrows with the same source.
* Every nonempty full cosieve in a slice a/A is contractible.
* G is strongly homogeneous on finite closed substructures.
* For every Set diagram H, eventual-equality injectivization followed
  by saturation gives weak equivalences of categories of elements.
* A is total and BA is contractible.

All these inputs were proved there for arbitrary actions, not only
finite or injective ones. No new external source is used in this note.

For any monoid diagram M on A, put

    S = colim_{B in I} M(B)

in monoids. Filtered colimits of monoids are computed on underlying
sets. This S has a continuous G action by monoid automorphisms:

    g.[B,m] = [gB, M(g|B)(m)].

Each element represented at B is fixed by the open subgroup G_B.

## 2. The saturation comparison preserves monoid colimits and hocolimits

Define T_S(B)=S^{G_B}. For a closed embedding f:B→C, extend f to
g∈G and use s↦g.s. This gives a monoid functor, independent of the
extension. The maps η_B:M(B)→S^{G_B} form a natural monoid map η.

**Lemma 1 (proved).** For every finite k≥0, the induced map

    El_A(M^k) → El_A(T_S^k)

is a weak homotopy equivalence. Consequently η induces both

    hocolim_A BM(a)  ≃  hocolim_A B T_S(a)

and an isomorphism

    colim_A^Mon M  ≅  colim_A^Mon T_S.

**Proof.** First identify eventual equality with equality in S. If
M(f)m=M(f)m′ for f:B→C, extend f to g∈G. Applying the isomorphism
M(g^{-1}|C) gives equality after the inclusion B⊆g^{-1}C. Conversely,
equality in the filtered colimit S is witnessed after an inclusion,
which is an arrow of A. Thus M^{inj}(B) is exactly the image of
M(B) in S. In particular its filtered colimit over I is again S.

Eventual-equality injectivization commutes with finite products. The
only nonformal direction is that k separate witnesses for coordinate
equalities can be replaced by one witness: repeatedly use condition I
to complete arrows with common source to commuting squares. Therefore

    (M^k)^{inj} = (M^{inj})^k.

The injectivization relation is a monoid congruence by the same
synchronization argument. Filtered colimits commute with finite
products, and fixed subsets commute with finite products. Hence the
injectivization and saturation maps for the Set functor M^k are exactly
the k-th powers of those for M. R17's two homotopy-finality proofs
apply to them and give the displayed element-category equivalence.

For the homotopy-colimit conclusion, use the nerve of a one-object
monoid category, whose k-th simplicial set is M^k. The simplicial
replacement in A gives a bisimplicial set. The previous equivalences
are weak equivalences of its rows, so diagonal realization gives the
claimed weak equivalence. This is also the usual Grothendieck
construction model for the homotopy colimit of the monoid categories.

Taking π0 of the element-category equivalence gives isomorphisms

    colim_A U(M) ≅ colim_A U(T_S),
    colim_A U(M^2) ≅ colim_A U(T_S^2),

compatible with both projections, multiplication, and the unit.
The ordinary monoid colimit has the presentation with one generator
for each element of colim_A U(M), relations [x][y]=[xy] indexed by
colim_A U(M^2), and the unit relation. Indeed it is the quotient of
the free monoid on the disjoint union of the M(a) by transition,
multiplication, and unit relations; transition relations give exactly
the displayed Set colimits. The two compatible bijections therefore
give an isomorphism of these presentations. This proves the monoid
colimit assertion. ∎

The proof does not claim that ordinary Set colimits commute with
products. Instead, the maps on the two separate Set colimits of M
and M^2 are both bijections. This distinction is essential.

## 3. Free filtered limits force passage

**Proposition 2 (proved).** Let M:A→FreeMon be arbitrary, including
noninjective transition maps and infinite bases. If its filtered
limit S over I is a free monoid, then the comparison

    hocolim_A BM(a) → B(colim_A^Mon M)

is a weak homotopy equivalence.

**Proof.** Let B be the canonical set of atoms of the free monoid S.
Every automorphism of S permutes B. Its G action therefore restricts
to a continuous discrete G-set action on B. A finite word is fixed
by G_F exactly when each of its ordered letters is fixed by G_F.
Consequently there is a natural monoid isomorphism

    T_S(F) = FreeMon(B^{G_F}).

Thus T_S is a basis-map diagram. For any Set functor X on a total
category with contractible BA, the comparison for FreeMon(X) is a
weak equivalence. One direct verification uses the natural inclusion
of the bouquet of X(a)-indexed circles into B FreeMon(X(a)). The
inclusion is an objectwise homotopy equivalence and is natural for
basis maps. Its homotopy colimit is obtained from BA by attaching
cylinders B El_A(X)×[0,1] with both endpoints attached by the
projection to BA. Each component of B El_A(X) is contractible by
totality; BA is contractible as well. The resulting comparison to
the bouquet of circles indexed by colim_A X is therefore a weak
equivalence. The target monoid is FreeMon(colim_A X).

Apply this to X(F)=B^{G_F}, then use both conclusions of Lemma 1.
They fit into the natural square of comparison maps; the vertical
maps are a weak equivalence on the source and an isomorphism on the
target monoid. The bottom comparison is a weak equivalence, hence
so is the top one. ∎

This criterion isolates a genuine remaining possibility: a failing
diagram, if one exists, must have a filtered limit S that is not a
free monoid. Such limits can exist, for example dyadic subdivision
systems. The proposition does not assert that every cancellative,
conical, equidivisible limit is free, or that it has an integer length.

## 4. First-return kernel diagrams cannot give a counterexample here

Suppose X:A→Set, K:A→Grp, and α:FreeMon(X)→U(K) is a natural
monoid map. Put

    R(a) = {w in FreeMon(X(a)) : α_a(w)=1}.

Every R(a) is a free monoid: its canonical generators are nonempty
return words with no proper nonempty prefix mapping to 1. Cut an
arbitrary return word at every prefix that maps to 1. The pieces are
first-return words, and these cut positions uniquely determine the
factorization. Conversely a product of first-return words returns
to 1. No injectivity hypothesis on the group transitions is needed.

The maps of R are strict positive substitutions in these bases;
a first-return word can split into several first-return words when
the group map kills an intermediate prefix. This means the diagram
need not be a basis-map diagram at its original finite stages.

**Corollary 3 (proved).** Every such first-return kernel diagram R
over C_delta passes its FreeMon comparison.

**Proof.** Restrict to I. Write X_∞=colim_I X and K_∞=colim_I K.
FreeMon preserves filtered colimits and filtered colimits commute
with finite limits of underlying sets. In particular the equation
α(w)=1 is detected at a finite stage. Hence

    colim_I R = ker(FreeMon(X_∞) → K_∞)

as monoids. This kernel is again free by the first-return argument.
Proposition 2 applies. ∎

The group target could be replaced by any monoid for which this
first-return factorization is valid. The group case above is enough
for the suggested construction and avoids an unnecessary extension.

## 5. Remaining question

Neither Proposition 2 nor Corollary 3 proves the universal C_delta
FreeMon assertion. In a general diagram the saturated limit need
only be a filtered colimit of free monoids; it can have no atom
basis. Comparing its orbit nerve with the nerve of its monoid
coinvariants remains the specific unresolved step.
