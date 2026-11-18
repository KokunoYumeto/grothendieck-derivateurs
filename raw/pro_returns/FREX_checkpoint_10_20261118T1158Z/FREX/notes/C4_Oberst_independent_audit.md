# Independent audit of Oberst (1968)

Auditor: predimension agent, GPT-6 Astra, 18 November 2026, 08:36 UTC.

Primary source: Ulrich Oberst, *Homology of Categories and Exactness of Direct Limits*, Mathematische Zeitschrift 107 (1968), 87–115. The complete original scan was obtained by the integrating agent from the public GDZ article endpoint https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0107/LOG_0022.pdf . The source scan and OCR remain outside the deliverable under `background/research`; no source pages are copied into this note. Printed page 108 was independently rendered and visually checked to resolve the variance in the key hypothesis.

## Definitions and main theorem

Definition II.1.2, printed p.108, uses F1 for common successors and F2 for actual postcomposition equalizers. F3 is the commutative-square condition I of the present task. The extra hypothesis F2-prime says: if two parallel arrows alpha1,alpha2 admit a common PREcomposition beta with alpha1 beta = alpha2 beta, then they admit a POSTcomposition gamma with gamma alpha1 = gamma alpha2. The OCR's missing primes and diagram spacing must not be used to reverse this condition.

Theorem II.2.1, printed pp.109–110, states equivalence of integral exactness of colimits, exactness for every AB5 abelian coefficient category, and filteredness of the category of elements of the constant integral functor on the additive envelope of the integral linearization of X. The objects in that last category include finite tuples of category objects together with integer weights. This is not filteredness of X itself. Its underlying flatness result II.1.3 is explicitly attributed to Oberst–Röhrl [8].

Theorem II.4.1, printed pp.111–114, proves (i) integral exactness implies F3; and (ii), under F2-prime, integral exactness is equivalent to filteredness of every connected component. The proof of (i) extracts a common ordinary composite from a nonzero equality of integral linear combinations. No positivity assumption is used. The proof of (ii) first treats groupoids: induction from subgroupoids is exact because the relevant comma groupoids have simply connected components; restricting to a cyclic subgroup forces its H1 to vanish, so all vertex groups are trivial. For a general exact X its universal groupoid therefore has simply connected components. F2-prime together with F3 supplies a calculus of left fractions. Equality of the two fractions representing a parallel pair then produces an actual postcomposition equalizer. Connectedness plus F3 gives common successors. These arguments check with their stated hypotheses.

Corollary II.4.2, printed pp.111–112, lists groupoids, categories whose arrows are all epimorphisms, categories admitting coequalizers, and commutative monoids as examples satisfying F2-prime. Corollary II.4.3, printed p.115, isolates simple connectedness of the universal groupoid of an integrally exact category.

## The false extension and its reduction claim

Remark II.4.4, printed p.115, and the introduction p.88 conjecture that F2-prime can be removed. That conjecture is false: the nonempty finite ordered-set injection category is integrally exact but not filtered. In this category F2-prime fails already for two different injections from a two-point order to a three-point order that agree at one endpoint: they have a one-point pre-equalizer, while no injection can post-equalize them.

The remark also says that proving the arbitrary monoid case would suffice. That proposed reduction is untenable: the monoid assertion is true, as established by the opened Isbell (1968) source and by the direct finite-cycle argument in C.6, while the general statement is false. It must not be retained as a valid reduction. No assertion in Oberst's proved theorem supplies the missing all-prime-exact plus total implies rational-exact implication of C.4.

## Homology-cofinality scope

Theorem I.2.3, printed pp.93–94, states that for a functor i:X to Y between small categories, the following are equivalent: every comma category y\X is nonempty, connected, and integrally acyclic; all derived-colimit comparison maps are isomorphisms for every abelian coefficient category with exact direct sums; and the same comparison assertion for abelian groups alone. Its resolution formulation is also equivalent. The proof tests representable coefficient modules to recover the homology of the comma categories. This is a homological statement, not a theorem asserting weak contractibility of the commas or a homotopy equivalence. The distinction agrees with the explicit bar comparisons used elsewhere in the manuscript.
