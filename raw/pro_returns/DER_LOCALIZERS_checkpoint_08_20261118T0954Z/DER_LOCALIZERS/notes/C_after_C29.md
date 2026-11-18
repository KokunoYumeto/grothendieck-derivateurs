# Raw-adjoint continuation after C.29

18 November 2026, GPT-6 Astra, inherited effort, DER_LOCALIZERS/linear_case.

C.29 has a complete proof in the main section and independent root, intervals,
and schematization audits. It supplies a concrete necessary restriction on a
pointwise raw counterexample: no compatible small linear presentation can have
all Hom modules finitely generated projective over k. We do not claim strict
separation from the union of all preceding sufficient criteria without an
example proving that separation. In particular C.28 is outside the flat and
countable-form assumptions but inside the split/finite-component criteria.

## The relative finite presentation argument

The useful change from C.27 is to keep the entire unit as a fixed summand in
every stage. Write J as the quotient of U plus a sum of representables by
representable relations. Each single relation has finite support in the
generator sum. Finite sets of generators and relations therefore give a
filtered system under U, without requiring U itself to be finitely presented.
Finite Hom modules ensure that every stage, evaluated at any object, is a
finitely presented k-module. The quotient by the image of the one generator
of U(a)=k is finitely presented too. Monicity after tensoring all scalar
copowers makes the inclusion pure; finite-equation lifting splits it. The
adjunction and homology argument only needs these pointwise splittings, not
projectivity or flatness of a stage as an A-module.

For arbitrary projective Hom modules, the same relative presentation exists,
but its evaluation can be a cokernel between infinitely generated projective
k-modules. Its unit quotient need not be finitely presented or pure-projective.
That is the precise remaining failure of this argument. Merely invoking
projectivity of the Hom modules does not split a pure unit inclusion into such
a quotient.

## Focused searches and scope

The query `pure monomorphism finitely presented quotient split module finite
equations` located standard purity discussions, including the article
*Cofibrant generation of pure monomorphisms* and older pure-exactness results.
No new theorem from an unopened search result is used: C.29 proves the needed
finite-equation statement directly, consistent with the purity background
already read for C.14. The relative-generator construction is likewise proved
directly rather than inferred from an unverified accessibility theorem.

Further exploratory queries were `projective coalgebra over commutative ring
fundamental theorem finitely generated subcoalgebra locally finite` and
`coalgebras von Neumann regular ring finitely generated projective subcoalgebra
fundamental theorem`. They aim to test whether a coherent pointwise tensor's
coalgebra structure on Hom modules can replace the missing finite generation.
These are research leads only; no coalgebra result has yet been applied.

One must distinguish scalar purity at each evaluation from categorical purity
of presheaves. The latter would require lifting maps from finitely presented
presheaves, and does not follow from the former. In particular the ordinary
simplicial interval has pointwise split unit inclusions without a presheaf
retraction. A cofibrant-generation theorem for categorical pure monomorphisms
cannot silently be applied to this weaker pointwise condition.

## Coherence and a resolution attempt: still a gap

For coherent k, products of flat modules are flat. Thus a raw image of a
projective disk product has flat evaluations when each representing complex
has projective components. This observation alone does not solve the gate:
C.20's Boolean example already warns against deducing the desired vanishing
from exactness, pure-injective tests, and flat output values.

A projective resolution of J/U can be pulled back to a resolution of J whose
degree-zero term contains U evaluationwise split. If tensoring with the raw
image is exact at evaluations, its total F-image resolves the null interval
tensor. However the counit-extension argument then lands in a total complex,
not in F of one actual presheaf. The extension does not yield an adjunction
retraction of the original presheaf. This is a missing comparison, not a proof.

## Coalgebra sources actually opened

Additional queries were `A local finiteness theorem for corings over
semihereditary rings`; `Cofree objects in the categories of comonoids von
Neumann regular coalgebras`; `Generators for comonoids and universal
constructions arxiv`; `Hiroshi Kihara local finiteness pdf`; `Matric generators
of coalgebras and bialgebras pdf`; `Cofree objects locally projective finite`;
and `Cofree objects in the categories of comonoids Abdulwahid thesis`.

Opened Abdulwahid--Iovanov, *Generators for comonoids and universal
constructions*, arXiv:1603.00108v1, 1 March 2016, at
https://arxiv.org/pdf/1603.00108 . Read Section 3, including Proposition 3.2
and its preceding construction, Theorem 3.3 (Cohn's finite-equation criterion),
Theorem 3.5 and its construction, and Proposition 3.6 with proof, printed
pp.5--6. Proposition 3.2 gives countably generated pure subcorings over a von
Neumann regular ring, not finitely generated ones. The general cardinal bound
retains the cardinality of the fixed base ring. Neither statement supplies a
countable scalar form or controls every incoming Hom argument in raw G.

Opened Adnan Hashim Abdulwahid's University of Iowa 2016 dissertation,
*Cofree objects in the categories of comonoids in certain abelian monoidal
categories*, DOI 10.17077/etd.4fj41erw, from its indexed public repository PDF.
Read printed pp.74--75, including Theorem 4.2 and its proof. With a von Neumann
regular base and both-sided local projectivity of the coring, it does give a
finitely generated subcoring containing any finite set. The proof uses the
finite sub-bimodule over the two dual rings and the automatic purity over a
von Neumann regular ring, citing Brzezinski--Wisbauer 19.10 and 19.12. Those
book passages were not independently opened in this continuation, so the
thesis statement is recorded as a research lead, not silently strengthened or
used to close the raw gate.

Opened Hiroshi Kihara's publisher abstract and metadata for *A local finiteness
theorem for corings over semihereditary rings*, Archiv der Mathematik 106
(2016), 507--513, DOI 10.1007/s00013-016-0902-6. The PDF link returned the same
subscription preview; the original full text was not obtained. The abstract
states semihereditarity and projectivity assumptions, but gives no license to
infer finite subcategories compatible with arbitrary composition. The related
2019 matric-generators paper appeared in search, but was not opened or used.

## Finite coalgebra support does not control all incoming relations

This explicit check addresses a proof shortcut, not the manuscript theorem.
Let R=Z[t,t^{-1}] with its usual grouplike coproduct Delta(t)=t tensor t.
Let U=Z be its augmentation module, and put

\[
 P=(R u\oplus R y)/\bigl((t-1)u,(t-3)y-u\bigr).
\]

There is an exact sequence 0 -> Z u -> P -> Z[1/3] -> 0. To check the left
injection directly, a relation combination producing a constant multiple of
u must have zero y-coefficient. Since R is a domain and t-3 is nonzero, the
coefficient of the second relation is zero. The remaining relation is a
multiple of (t-1)u and has zero augmentation, so that constant is zero.
Quotienting by u gives R/(t-3)=Z[1/3]. The quotient is flat over Z, hence the
inclusion of U is pure and remains monic after every scalar tensor product.

It does not split over Z. A retraction rho would give integers
m_n=rho(t^n y), for every integer n, with m_(n+1)-3m_n=1. Therefore

\[
 2m_{n+1}+1=3(2m_n+1).
\]

For negative n this says that 3^r divides 2m_0+1 for every r>=0. The only such
integer is zero, which would force m_0=-1/2. This is impossible.

P is a finite relative presentation under U, with one generator and one
relation R -> U plus R, r |-> (-epsilon(r),(t-3)r). The relation coefficient
t-3 belongs to the finite free subcoalgebra spanned by 1 and t. Nevertheless,
all incoming powers t^n, including negative n, impose the infinite system
above. Closing a finite set under comultiplication is therefore insufficient
to replace the full incoming column by a finite Hom module in C.29.
Composition closure and the unrestricted Hom maps in G remain separate
requirements. This category fails the manuscript normalization (Tor_1^R(Z,Z)
is Z), and P is not a null interval; no raw-adjoint counterexample is asserted.
Moreover the scalar ring here is Z, already covered by C.7 (and by C.14 with
the pointwise tensor). This countable-ring datum cannot itself test the
outstanding raw gate, even if those missing manuscript conditions were repaired.
