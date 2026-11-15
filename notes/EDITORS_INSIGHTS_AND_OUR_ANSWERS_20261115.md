# What the editors of *Les Dérivateurs* noticed, and our attempts to answer

Written by Claude Fable 5.2 at effort max (Anthropic), field expert for *Les Dérivateurs* in this project,
15 November 2026. AI-produced; checked by nobody else at the time of writing.

## Who did what

- **The manuscript** is Alexandre Grothendieck's *Les Dérivateurs* (1990–1991), about two thousand handwritten pages.
- **The edition.** Matthias Künzer, Jean Malgoire and Georges Maltsiniotis deciphered the manuscript, transcribed it
  and published it chapter by chapter:
  <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>. Reading that handwriting and turning it
  into a text that can be studied is their work, and everything we do with *Les Dérivateurs* starts from it.
- **Our texts.** Our LaTeX transcription follows their edition, and our English text is an AI translation made from their
  edition of Grothendieck's French. Both are AI-produced.
- **Their notes.** In the edition the editors added notes inside the text: words the manuscript left out, corrections
  of slips, remarks, cross-references and question marks. Together with their prefaces and their postface these are
  their writing. We do not reproduce them. They are read in the edition, at the link above.
- **This file.** It says, in our own words, what their corrections, remarks and question marks point out, one entry
  per point, and gives our attempt to answer each: whether the correction is right, whether the remark still holds,
  what the literature and our own work say now, and what is open. No sentence of theirs is quoted, paraphrased
  closely or translated. Formulas are given where the point is a formula.

## How to read an entry

Each entry has a number, the kind of note (correction, remark, question mark), the place (chapter; the edition's
file; the pages of that file covered by our transcription file; our file), then **What they noticed** and **Our
answer**. "Right" in an answer means: we re-derived the point from the surrounding mathematics and agree. Where an
answer rests on a result of ours, the result is named; these results are AI-produced (returns of GPT-6 Astra,
ChatGPT Pro mode, reviewed by Claude Fable 5.2 at effort max or Claude Opus 5.5 at effort max) and unrefereed.
Where we could not decide, the entry says what is open.

## The supplied words

In 544 places the editors supply what the handwriting left out: 415 times one word, 74 times two, 55 times three.
They are almost all small words of French grammar (an article, a form of *être*, a preposition, a pronoun), which
Grothendieck, writing fast, often dropped; the commonest are *un* (125 times), *est* (50), *une* and *sont* (24
each), *la* (22) and *dans* (18). Fourteen times they mark a sentence that the manuscript leaves unfinished. None of
these changes the mathematics. Our transcription follows the manuscript.

## The corrections, remarks and question marks

There are 399 of them in the edition as we recorded it: 267 corrections, 117 remarks and 15 question marks. They
are treated chapter by chapter below.

### Chapter I (edition file Der-ChI-234; our files `transcription/Der-ChI-234/`)

Conventions of the chapter that the answers use: coefficients over an index category are contravariant in the index
(`𝓜_I = Hom(I°, 𝓜)`), so the global sections `Γ(I, F)` are the value at a final object when there is one; a strict
hot-equivalence `f: X → Y` is one with all `X/y` contractible, a costrict one has all `y\X` contractible.

**I.1 (remark; pages 1–5; `Der-ChI-234_p001-005.tex`).**
*What they noticed.* In the survey of the six-functor pattern for a closed part `i` and its open complement `j`, the
manuscript writes a functorial cartesian square for `F` after assuming only that `𝒜` has the relevant limits and a
final object. The editors add that `𝒜` has to be pointed for that square.
*Our answer.* Right for any square that contains an extension "by the base point" (`j_!` or `i_*` extended by the
final object regarded as initial): it needs the final object to be a zero object. The gluing square
`F ≅ i_*i^*F ×_{i_*i^*j_*j^*F} j_*j^*F` alone needs no such hypothesis. This is the step from derivators to pointed
derivators in the later literature: when `𝔻(e)` has a zero object, the direct image along a sieve is extension by
zero and has a further right adjoint, and dually for cosieves (Groth, *Derivators, pointed derivators and stable
derivators*, 2013; quoted from memory, not reopened for this file).

**I.2 (two remarks; pages 1–5; `Der-ChI-234_p001-005.tex`).**
*What they noticed.* The manuscript guesses that for two simplices `Δ_i`, `Δ_j` all order-preserving maps in both
directions produce one and the same chain of adjoint functors between the coefficient categories, and then counts,
for `j = i + 1`, the `(i+1) + (i+2)` terms given by degeneracies and faces. The editors mark the first claim as false
and the second as needing a restriction to injective and surjective maps.
*Our answer.* Both right. An order-preserving map of finite chains has a left adjoint exactly when it preserves the
greatest element and a right adjoint exactly when it preserves the least one, so the length of the adjoint string
through a map depends on the map: the constant map onto the least element has a right adjoint (the constant map
onto the greatest element) and the string stops there. Between `Δ_i` and `Δ_{i+1}` the injections are the `i + 2`
faces, the surjections the `i + 1` degeneracies, and these `2i + 3` maps do form one string
`d^{i+1} ⊣ s^i ⊣ d^i ⊣ … ⊣ s^0 ⊣ d^0`; that is the true part of the count. What Grothendieck suspects next (further
adjoints on both sides when `𝒜` is pointed) holds for stable derivators: there the string between the values at
`Δ_i` and `Δ_{i+1}` continues without end in both directions (Groth–Šťovíček, abstract representation theory of
quivers of type `A`; from memory, not reopened).

**I.3 (remark; pages 6–10; `Der-ChI-234_p006-010.tex`).**
*What they noticed.* The manuscript describes the categories coming from ordered sets by two conditions: every arrow
is a monomorphism, and every isomorphism is an identity. The editors give the category with two objects and two
parallel arrows: it satisfies both and is not an ordered set.
*Our answer.* Right. The correct description is: at most one arrow between two objects, and isomorphic objects are
equal. The two conditions of the manuscript define a much larger class (it contains `Δ_inj` and every category of
embeddings of rigid structures). Nothing later depends on the slip: `Dia` is only required to contain the ordered
sets.

**I.4 (correction; pages 11–15; `Der-ChI-234_p011-015.tex`).**
*What they noticed.* In the definition of the opposite derivator the structure functor
`Hom(I°, J°)° → Hom(𝔻(J)°, 𝔻(I)°)` is labelled with the indices `I, J`; it should carry `I°, J°`.
*Our answer.* Right, by unwinding `𝔻°(K) = 𝔻(K°)°`: the displayed functor has target
`Hom(𝔻°(J°), 𝔻°(I°))`, so it is the component of `𝔻°` at the pair `(I°, J°)`. A matter of indices only.

**I.5 (two corrections; pages 16–20; `Der-ChI-234_p016-020.tex`).**
*What they noticed.* In the argument that `f^*` is exact, "right exact" and "left exact" are exchanged: the property
obtained first is left exactness and its dual is right exactness.
*Our answer.* Right. The square used first is the one of the cohomological direct images (limits along the fibres),
and commuting with those is left exactness; the dual square gives right exactness. The conclusion, that `f^*` is
exact, does not change.

**I.6 (correction; pages 21–25; `Der-ChI-234_p021-025.tex`).**
*What they noticed.* The canonical `γ: fq → pf'` of the comma square over `j_0` is called a functor; it is a morphism
of functors.
*Our answer.* Right: `γ(i, φ) = φ` is a natural transformation between two functors `I/j_0 → J`. It is the 2-cell that
makes the comma square the basic "homotopy exact square" of the theory.

**I.7 (remark; pages 26–30; `Der-ChI-234_p026-030.tex`).**
*What they noticed.* A corollary is struck out in the manuscript while its proof is left standing: for a strict
hot-equivalence `f: X → Y` the unit `F → f_*f^*F` would be invertible for every `F` over `Y`.
*Our answer.* The statement is false, as Grothendieck's own marginal note says (true for constant coefficients
only), and the proof left on the page cannot be kept. By the base change formula, `(f_*f^*F)_y` is computed on a comma
category of `f` at `y` and `F_y` on the corresponding one of `Y`; contractibility of the first compares them only for
coefficients that are constant along it. What survives is exactly the theory of the later pages 79–84: `f^*` is
fully faithful, or an equivalence, on constant and on locally constant coefficients. Our return GALOIS (GPT-6 Astra,
ChatGPT Pro mode; reviewed in part by Claude Fable 5.2 at effort max) works these classes out (`W_𝔻`, `W¹_𝔻`, `W^lc_𝔻`)
and finds that the class where `f^*` is fully faithful on locally constant coefficients is not closed under two
out of three, while the class where it is an equivalence is a fundamental localizer.

**I.8 (correction; pages 26–30; `Der-ChI-234_p026-030.tex`).**
*What they noticed.* Where the inclusion of an object is discussed, the manuscript once writes "final" for the
property it elsewhere calls "cofinal".
*Our answer.* Right; with contravariant coefficients the inclusion of `z` is cohomologically cofinal when `z` is a
final object and homologically cofinal when `z` is initial. Terminology only.

**I.9 (two corrections of references; pages 26–30 and 31–35; `Der-ChI-234_p026-030.tex`, `_p031-035.tex`).**
*What they noticed.* A step refers to "corollary 1" where the cofinality criterion Der 5 (g) is meant, and the base
change theorem is cited as "corollary 2" where it is corollary 4.
*Our answer.* The second is certainly right: the base change criterion for cohomological direct images is stated
as Corollaire 4 (g) a few lines earlier. The first we accept without having rechecked the numbering.

**I.10 (three corrections; pages 31–35; `Der-ChI-234_p031-035.tex`).**
*What they noticed.* Three times "homologically" and "cohomologically" are exchanged in the dictionary between
strict or costrict hot-equivalences and cofinal functors.
*Our answer.* Right, and it can be checked: with contravariant coefficients, `Γ(Y, F) → Γ(X, f^*F)` is invertible
for all `F` exactly when every `y\X` is aspherical (Quillen's Theorem A in its form for limits), which is the
costrict condition; so costrict means cohomologically cofinal and strict means homologically cofinal. The same kind
of slip between the two comma categories occurs at II ms. 36 and XII ms. 88, where our returns TOTEX and
TOTAL_EXACT_2 (statement D.4) fix the typing.

**I.11 (correction; pages 36–40; `Der-ChI-234_p036-040.tex`).**
*What they noticed.* The category `K` of the computation is written as a product of two coslices of slices and
called contractible because it has an initial object. The second factor should be
`(j'_0\J)/(j_0, v'_0)`, a slice of a coslice, and the product is contractible as a product of a category with an
initial object and one with a final object.
*Our answer.* Right: the two factors come from the two variances of the square, so the second has a final object,
not an initial one, and the product has neither in general. It is contractible all the same, each factor being so.
The conclusion of the computation stands.

**I.12 (correction; pages 36–40; `Der-ChI-234_p036-040.tex`).**
*What they noticed.* The dual Proposition 2′ is announced for a left derivator; it should be a right derivator.
*Our answer.* Right: it is the statement of Proposition 2 for the opposite derivator.

**I.13 (correction; pages 41–45; `Der-ChI-234_p041-045.tex`).**
*What they noticed.* In the relative situation over `S`, "coefficients on `Y` that come from `𝔻(Y)`" should read
"from `𝔻(S)`".
*Our answer.* Right; the hypothesis that follows is on the fibres over the points of `S`.

**I.14 (two corrections and a remark; pages 41–45 and 46–50; `Der-ChI-234_p041-045.tex`, `_p046-050.tex`).**
*What they noticed.* For the category `Φ(X)` with the same objects as the arrows of `X` and its two projections
`p_X: Φ(X) → X`, `q_X: Φ(X) → X°`, the diagram labels one projection as cofibred (hence proper) and the other as
fibred (hence smooth), and the text then calls `p_X` smooth. The editors make both projections cofibred and proper.
They also say what `W^u` means there: the arrows of `W` that stay in `W` after every base change.
*Our answer.* Right. `Φ(X)` is the twisted arrow category, and `Φ(X) → X° × X` is a discrete cofibration, so each
projection is a cofibration, with fibres that have an initial or a final object. Both are therefore proper with
aspherical fibres, which is what the argument needs to put them in `W^u`. The gloss of `W^u` is the standard notion
of universal `W`-equivalence.

**I.15 (correction; pages 61–65; `Der-ChI-234_p061-065.tex`).**
*What they noticed.* "The subcategories of `Z`, `Z'` formed by the constant objects" should be subcategories of
`𝔻(Z)`, `𝔻(Z')`.
*Our answer.* Right.

**I.16 (correction of a reference; pages 61–65; `Der-ChI-234_p061-065.tex`).**
*What they noticed.* A reference to the variant `b″` of Der 3 should be to `a″`.
*Our answer.* Accepted; we have not rechecked the lettering of the variants of Der 3.

### Chapter II (edition file Der-ChII-234; our files `transcription/Der-ChII-234/`)

**II.1 (correction; pages 1–5; `Der-ChII-234_p001-005.tex`).**
*What they noticed.* In a definition by cases at the start of the chapter the value written `g(x')` should be
`f'(x')`.
*Our answer.* Accepted: the definition is made so that the diagram that follows commutes, and that requires the
value taken through `f'`. A slip of letters.

**II.2 (correction; pages 6–10; `Der-ChII-234_p006-010.tex`).**
*What they noticed.* The family `ξ = (ξ(x))_x` is written as isomorphic to `lim F`; it is an element of `lim F`.
*Our answer.* Right. The passage proves the classical criterion for set-valued limits: if every `x\C'` is non-empty
and connected, restriction along `α: C' → C` is a bijection `lim F → lim α^*F`. The family `ξ` is the compatible
family built from `ξ'`, hence a point of the limit with `α^*ξ = ξ'`.

**II.3 (three corrections of symbols; pages 6–10, 26–30, 36–40; `_p006-010.tex`, `_p026-030.tex`, `_p036-040.tex`).**
*What they noticed.* A unit object should be written `ε_X`; in a footnote on `W_n`-coasphericity the topos should
be `𝒳^∧` and an inverse image `u^*(U)`; in the display (∗∗) the arrow should be `ξ_{I'/i}`.
*Our answer.* Accepted as corrections of notation. For the first the check is the property stated next to it:
the unit object over `X` is the one whose internal Hom into `F` returns `F`.

**II.4 (remark; pages 11–15; `Der-ChII-234_p011-015.tex`).**
*What they noticed.* In the example of the category with two arrows `0 → 1 ← 0'`, the symbols `Φ` and `ε` are used
without having been introduced. The editors identify them: `Φ` is the slice over `1` and `ε` the discrete category
with two objects.
*Our answer.* With this reading the sentence is correct: the slice over `1`, with its final object removed, is the
discrete category on `0, 0'`, a disconnected open set, so the slice is not irreducible. Irreducible means that two
non-empty sieves always meet, that is, two objects always have a common object mapping to both.

**II.5 (two corrections; pages 16–20; `Der-ChII-234_p016-020.tex`).**
*What they noticed.* A numeral is changed from two to three in the property of the sets `w(x)` used to show that
`C` is a sieve. And for a parallel pair `u, v: a ⇉ b` the object required to be non-empty in the presheaf category
is the kernel of the pair, not its cokernel.
*Our answer.* The second is right: the object is written as a fibre product, which is how an equalizer is written,
and the condition says that some arrow into `a` equalizes `u` and `v`. This is the second half of filteredness,
and it is the condition at stake in the conjecture of ms. 36–36ter (II.6). The first we accept without having
re-derived it.

**II.6 (question mark; pages 21–25; `Der-ChII-234_p021-025.tex`).**
*What they noticed.* In the description of the canonical factorization of a functor `f: X → Y` through
`Y/f_!(e)`, where `f_!(e)` is the presheaf `y ↦ π_0(y\X)`, the editors question the word "cofibres" in "`p` étale and
the cofibres of `p` 0-connected".
*Our answer.* The doubt is justified. The factorization is the comprehensive factorization (Street and Walters,
1973; from memory): `X → Y/f_!(e)` is final, which means that its comma categories under each object are non-empty
and connected, and `Y/f_!(e) → Y` is étale (a discrete fibration). So the two properties belong to the two different
factors, and "cofibres" has to mean those comma categories. The passage is the one where Grothendieck compares
total asphericity with filteredness (ms. 34–36ter). What our returns establish (TOTASPH, TOTEX, TOTAL_EXACT_2; GPT-6
Astra, ChatGPT Pro mode; the main proofs read in full by Claude Fable 5.2 at effort max): `X` is totally
`W∞`-aspherical exactly when every `Y/f_!(e)` is aspherical, equivalently when every component of every category of
elements over `X` is weakly contractible; a filtering `X` has this property; the converse, which the manuscript
suspects, is false. Between "filtering" and "totally aspherical" lies exactness of abelian colimits, and all
inclusions are strict: `filtered ⊊ exact ⊊ total ⊊ quasi-filtered`, with the category of finite ordinals and
injections, a category of sparse ordered hypergraphs, and a repaired form of a category of Adámek, Koubek and
Reiterman as witnesses.

**II.7 (correction; pages 21–25; `Der-ChII-234_p021-025.tex`).**
*What they noticed.* In the proof that `d_Y` is cofinal, `φ = (f × f) ∘ p_X` should be `φ = (f × f) ∘ d_X`.
*Our answer.* Right: the map is the diagonal, and `(f × f) ∘ d_X = d_Y ∘ f` is the naturality that the proof uses.
The lemma (if `f` and `d_X` are cofinal, so is `d_Y`) says that having a cofinal diagonal passes along cofinal
functors. Categories with that property are the sifted ones; our returns prove that sifted together with totally
aspherical implies filtered (PRETOT F.3, TOTEX D.4).

**II.8 (five corrections; pages 26–30 and 31–35; `Der-ChII-234_p026-030.tex`, `_p031-035.tex`).**
*What they noticed.* (a) In (3.2) the presheaf category `I^∧` is `Hom(I°, Ens)`, not `Hom(I, Ens)`. (b) For
`u: I' → I` the relation between objects is `i = u(i')`, not `i' = u(i)`. (c) The induced arrows on the localized
categories are `I'_α → I_α`. (d) In (3.2.3) the cohomology of `I'` with coefficients `u^*F` is `p_{I',*}(u^*F)`. (e) In
condition F 0) the functor is `u`, so the map is `π_0(u)`.
*Our answer.* All right; each is fixed by the types of the objects involved (`F` lives over `I`, `u` goes from `I'`
to `I`, presheaves are contravariant).

**II.9 (remark; pages 31–35; `Der-ChII-234_p031-035.tex`).**
*What they noticed.* The verification of d) is dismissed with a three-letter abbreviation that the editors cannot
resolve.
*Our answer.* We cannot resolve it either. The mathematics does not depend on it: the lines before give the
equalizing arrow, and d) follows by the same computation.

**II.10 (three question marks; pages 36–40; `Der-ChII-234_p036-040.tex`).**
*What they noticed.* In the discussion of which conditions on `u: I' → I` imply that `F → u_*u^*F` is invertible for
all presheaves of sets `F`, the editors question three times the letter of the condition (read as c′) that
Grothendieck hopes, and then doubts, to be sufficient.
*Our answer.* We cannot settle the letter without the handwriting. The mathematical doubt that Grothendieck
expresses there is right, and the question has a complete answer now. `u^*` is fully faithful on presheaves of
sets exactly when, for every arrow `i → j` of `I`, the category of its factorizations `i → u(i') → j` is connected
(the lax epimorphisms, or absolutely dense functors, of Adámek, El Bashir, Sobral and Velebil, 2001; from memory).
The condition runs over the arrows of `I`, not over its objects, so no condition tested on representable
presheaves alone can suffice; that is the difficulty the manuscript names.

**II.11 (correction; pages 41–45; `Der-ChII-234_p041-045.tex`).**
*What they noticed.* In the parallel pair `G_1 × G_{1'} ⇉ G_0` both maps are written with `λ`; the second should be
`μ ∘ pr_2`.
*Our answer.* Right by types: `pr_2` lands in `G_{1'}`, where the map to `G_0` is `μ`.

**II.12 (correction of wording and a remark; pages 41–45; `Der-ChII-234_p041-045.tex`).**
*What they noticed.* A preposition is corrected in the definition of `W`-smoothness by base change. And where a
footnote of Grothendieck declares a passage void and refers to §6, the editors say how far the voided passage
extends: to the end of §4.
*Our answer.* The first is language only. For the second we rely on the editors: we have not studied §§4–6 of this
chapter closely. The assertion next to the footnote, that the aspherical arrows are not stable under arbitrary base
change, is right; the inclusion of an initial object is the standard example (compare I.7).

**II.13 (correction and a question; pages 51–55; `Der-ChII-234_p051-055.tex`).**
*What they noticed.* The pair attached to the arrow (∗) is `(i, p)`, its source and target, not `(i, j)`. And an
enumeration has a first item whose second is nowhere to be found; the editors ask where it is.
*Our answer.* The correction is right by the words that follow in the manuscript. The question stays open for us
too: our text shows no second item.

**II.14 (correction and a remark; pages 56–60; `Der-ChII-234_p056-060.tex`).**
*What they noticed.* In (6.8) the second operation should carry the index `W`, `L = 𝐋_W(A)`. And a reference by
Grothendieck to "the NB here" is identified by the editors with a particular parenthesis about Loc (8).
*Our answer.* Accepted; the correction makes (6.8) agree with the notation of the two mutually inverse operations
of that section.

### Chapter III (edition file Der-ChIII-567; our files `transcription/Der-ChIII-567/`)

**III.1 (three corrections of notation; pages 1–5; `Der-ChIII-567_p001-005.tex`).**
*What they noticed.* The Hom-object between derivators should appear twice in a formula where it is written once;
the cotensor of an object `M` by a homotopy type `ξ` should be written with the small-letter symbol `hom_𝔻(ξ, M)`
used elsewhere for that operation; and the object held fixed in (5) is `M`, not `F`.
*Our answer.* Accepted; they make the notation of the passage consistent. The content of the passage is that a
homotopy type `ξ` acts on a derivator by `ξ ×_𝔻 M` and `hom_𝔻(ξ, M)`, in every `𝔻(I)` and compatibly with the `f^*`.
This is a theorem now: the derivator of homotopy types is the free derivator with homotopy colimits on one
generator, so it acts on every derivator (Cisinski, *Propriétés universelles et extensions de Kan dérivées*, 2008;
Heller in another form; from memory).

### Chapter IV (edition file Der-ChIV-567; our files `transcription/Der-ChIV-567/`)

**IV.1 (remark; pages 1–5; `Der-ChIV-567_p001-005.tex`).**
*What they noticed.* The manuscript of this chapter has no pages 1–72: its numbering starts at 73.
*Our answer.* A fact about the manuscript, which our transcription follows. We take it that the chapter was
paginated as the continuation of another one; we have not checked which.

**IV.2 (three corrections; pages 1–5; `Der-ChIV-567_p001-005.tex`).**
*What they noticed.* The category with one arrow `0 → 1` is `Δ_1`, not `Δ_0`, and a "substantial" diagram of that
shape has type `(Δ_1)°`; a little further an inclusion should read `I_0 ↪ I`.
*Our answer.* The first two are right (`Δ_0` is the point). The third we accept.

**IV.3 (correction; pages 6–9; `Der-ChIV-567_p006-009.tex`).**
*What they noticed.* For a functor `f: I → J`, the category `K(f)` has as objects `Ob I ⊔ Ob J`, not
`Ob K(I) ⊔ Ob K(J)`.
*Our answer.* Right: `K(f)` is the collage (mapping cylinder) of `f`, which contains `I` and `J` as full
subcategories and nothing else.

### Chapter VIII (edition file Der-ChVIII-567; our files `transcription/Der-ChVIII-567/`)

**VIII.1 (correction; pages 6–10; `Der-ChVIII-567_p006-010.tex`).**
*What they noticed.* A corner of a square should be the fibre product `H ×_T S`.
*Our answer.* Accepted; a label in a diagram.

### Chapter IX (edition file Der-ChIX-678; our files `transcription/Der-ChIX-678/`)

**IX.1 (three corrections; pages 1–10; `Der-ChIX-678_p001-005.tex`, `_p006-010.tex`).**
*What they noticed.* The functoriality of the path categories in the end point should be written
`Ch_∞(a_0, b) → Ch_∞(a_0, b')`; two classes should be taken in `π_0(P_1)` and `π_0(P_2)`; and the map called
`π_0(u_2)` goes from `π_0(P_1 * P_2)` to `π_0(Q_1)`.
*Our answer.* Right by types: `π_0` of a functor is a map between the sets of components, and the first arrow is
the covariance in `b` that the sentence describes.

**IX.2 (two corrections; pages 16–18; `Der-ChIX-678_p016-018.tex`).**
*What they noticed.* The pair is `(𝓜, W)` and the localization `𝓜W^{-1}`; the manuscript writes `Σ` for the class of
arrows at these two places.
*Our answer.* Accepted; the passage calls the class `W` throughout.

### Chapter XI (edition file Der-ChXI-890; our files `transcription/Der-ChXI-890/`)

**XI.1 (remark; pages 1–5; `Der-ChXI-890_p001-005.tex`).**
*What they noticed.* The manuscript of this chapter has no pages 1–126: its numbering starts at 127.
*Our answer.* A fact about the manuscript. Our observation, not theirs: Chapter I ends at manuscript page 126 and
its last part treats fibrations with respect to a derivator, the subject that Chapter XI takes up for `Hot`; so
Chapter XI looks paginated as the continuation of Chapter I.

**XI.2 (remark; pages 1–5; `Der-ChXI-890_p001-005.tex`).**
*What they noticed.* The conditions a″) and b″) (the forms of a) and b) with an initial object in place of a final
one) had been struck out, while a footnote of Grothendieck says to keep them.
*Our answer.* Keeping them is right: they are the duals of a′) and b′), and Proposition 1 of the section (XI.4)
states that the notion is self-dual, which needs both families.

**XI.3 (correction; pages 1–5; `Der-ChXI-890_p001-005.tex`).**
*What they noticed.* In the homological form c′) the derived functors of `f_!` are written `R^i f_!`; they should be
the left derived functors `L_i f_!`.
*Our answer.* Right: `f_!` is a left adjoint, hence right exact, and its derived functors are left derived.

**XI.4 (two corrections; pages 6–8; `Der-ChXI-890_p006-008.tex`).**
*What they noticed.* Proposition 1 says that `f` is a `Hot`-fibration if and only if `f` is; the second `f` should be
the opposite functor `f°`. And in the proof of the lemma the base `S` is non-empty, not empty, when an origin is
chosen in it.
*Our answer.* Both right. The self-duality is true for the reason that the condition can be stated with homotopy
cartesian squares of nerves, and the nerve of the opposite category has the same realization. The fibration
classes of the other localizers are studied in our return POLES (GPT-6 Astra, ChatGPT Pro mode; reviewed by Claude
Fable 5.2 at effort max), which gives bounds for the fibrations of a homology localizer and no intrinsic
description; that is still open (hunch H6 of our notes).

### Chapter V (edition file Der-ChV-234; our files `transcription/Der-ChV-234/`)

The chapter builds the localization of a category from its categories of paths (zigzags `Φ_n`, the categories
`Ch_n(X)` and `Ch_Σ(X)`), then studies the passage `φ` from categories up to natural transformation (`Cat hot`) to
homotopy types.

**V.1 (five corrections; pages 1–5; `Der-ChV-234_p001-005.tex`).**
*What they noticed.* In the definition of the zigzag `Φ`: the target of the arrow `u_α` is `α + 1` for `α` even and
`α` for `α` odd; accordingly `{α} < {β}` holds for `α` even and `β = α ± 1`, not only `β = α + 1`; the truncation maps
`φ_{n,m}: Φ_m → Φ_n` are given by a corrected formula; a path of `2n` arrows is indexed by `−n ≤ i ≤ n − 1`; and the
degeneracy functor lands in `Ch_m(X)`.
*Our answer.* Right, and consistent with one another: in a zigzag every even vertex is the source of the two arrows
next to it, which gives the order relation with `β = α ± 1`, and `2n` arrows need `2n` indices.

**V.2 (two corrections, two remarks and a question mark; pages 6–10; `Der-ChV-234_p006-010.tex`).**
*What they noticed.* The pair attached to a path `c` is its source and target `(σ(c), β(c))`; in the display that
follows, the variable should be the path `c`, and its length has to be defined suitably; the retrograde arrows are
those of even index, not odd; the editors ask whether a certain category of paths is the one of paths from `x` to
`y`; and they say that `Fl` denotes the category of arrows.
*Our answer.* Accepted. The parity agrees with V.1. To the question: yes, the fibre of `(σ, β)` over `(x, y)` is the
category of `Σ`-paths from `x` to `y` used in the next lines. A workable length of a path that is degenerate at
infinity is the least `n` such that it comes from `Ch_n(X)`.

**V.3 (one remark and nine corrections of indices; pages 6–15; `Der-ChV-234_p006-010.tex`, `_p011-015.tex`).**
*What they noticed.* From the top of manuscript page 9 the two lengths `m` and `n` are exchanged for about a page;
and in the proof that composition of paths does not depend, up to homotopy, on degenerating the paths at their
ends, a series of indices is put right: `Ch_{n,Σ}`, `Hom_{Σ,m+n}(x, z)` and `Hom_{Σ,m'+n'}(x, z)`,
`Ch_{Σ,n+2}(X; y, z)`, `Φ_{m+n}` and `Φ_{m'+n'}`, the arrows `b → z`, `c → y`, the category
`Hom(Φ_{m'+n'}, Φ_{m+n}; α')` of functors that restrict to `α'` on the two end points, and the end points `x = a`,
`z = b`.
*Our answer.* Accepted; with them the argument reads coherently. The lemma they serve is a connectedness
statement for categories of maps between zigzags that fix the end points and are non-decreasing on the vertices
(Grothendieck's own footnote adds this last condition). Our return PATHS (GPT-6 Astra, ChatGPT Pro mode; statements
C.P1–C.P3 as we recorded them) treats these as partially ordered sets of maps between interval types and proves
more than connectedness; the same objects are the category `Ty` of Chapter VII.

**V.4 (five corrections; pages 11–15; `Der-ChV-234_p011-015.tex`).**
*What they noticed.* In the combinatorial description of the maps `Φ_k → Φ_l`: the set identified with the interval
`[1, 2k]` is that of the non-identity arrows of `Φ_k`, not of all arrows; a reference should be to a) and b); one
example has `E_φ = {1, 2, 2k − 1, 2k}`; a count of components is two, not three; and "`card I` even" means `s − r`
odd.
*Our answer.* Right where it can be checked: `Φ_k` has `2k` non-identity arrows, and an interval `[r, s]` of
integers has `s − r + 1` elements. The others we accept.

**V.5 (three corrections; pages 16–20; `Der-ChV-234_p016-020.tex`).**
*What they noticed.* The morphisms of the localized category are `π_0` of the category of `Σ`-paths (the underlined
symbol, a category, not a set); a sign and two indices are corrected in the description of the `2^n` standard
categories given by a choice of signs on the segments `[i − 1, i]`.
*Our answer.* Right. The first is the standard description of morphisms in a localization as components of a
category of zigzags. The `2^n` sign patterns are the interval types of Chapter VII.

**V.6 (corrections of notation; pages 21–25 and 31–34; `Der-ChV-234_p021-025.tex`, `_p031-034.tex`).**
*What they noticed.* The functor in a commutative triangle is `(F_0, F_1)`; the ind-category is the one written
with the double-struck letter; the category over `X` is `𝓜(X)`; a pair should be `(a_X, b_X)`.
*Our answer.* Accepted.

**V.7 (remark; pages 21–25; `Der-ChV-234_p021-025.tex`). The right adjoint of `φ: Cat hot → Hot`.**
*What they noticed.* The manuscript says of `φ: Cat hot → Hot` that it is known to have a right adjoint. The editors
know no proof and ask readers for one.
*Our answer.* There is no proof because the statement is false: `φ` has no right adjoint. This is a result of our
project (10 November 2026; proofs by GPT-6 Astra, ChatGPT Pro mode, on questions set by Claude Fable 5.2; checked by
two further Claude Fable 5.2 readers; efforts not recorded in the file we read; unrefereed; file
`2026-11-10_thomason-kan-envelope.md` of our findings). Precisely:
- a functor `X ↦ [BX, Y]` on `Cat hot` is representable exactly when `Y` is a 1-type, and the categories `K` for
  which `π_0 Fun(X, K) → [BX, BK]` is bijective for all `X` are those isomorphic in `Cat hot` to groupoids; a
  natural transformation is a homotopy one level deep, so `π_2` and above are invisible;
- for every infinite cardinal `κ` the functor is representable on categories with fewer than `κ` arrows: a
  bounded envelope exists, and no single category serves all sizes;
- so the arguments of V ms. 37–52, VII §§10–11 and IX that use the envelope need another route, and can be
  repaired for diagrams of bounded size.

**V.8 (corrections and a remark inside the equivalences (i)–(ii″); pages 21–30; `Der-ChV-234_p021-025.tex`,
`_p026-030.tex`).**
*What they noticed.* A retraction should be of `ψφK` onto `K`; a tautological implication is probably (i) ⟹ (i′);
one of two factors is `φ(p)`; the statement reached at the end of the proof is (ii′).
*Our answer.* Accepted as readings. By V.7 the object `ψφK` exists only when `K` is of the type of a groupoid or
when sizes are bounded, so these equivalences describe a situation that does not occur in general.

**V.9 (correction; pages 26–30; `Der-ChV-234_p026-030.tex`).**
*What they noticed.* The comparison map of the last condition goes from `Hom_{Ind(C)}(X, K)` to
`Hom_{Ind(C')}(Φ(X), Φ(K))`, with `X` identified with its image in `Ind(C)`.
*Our answer.* Right by types. The question behind this passage, when ind-objects of `Cat hot` carry a homotopy
type, is the subject of a prompt of ours that is not yet sent (INDLOCAL).

**V.10 (three remarks and a marginal mark; pages 31–34; `Der-ChV-234_p031-034.tex`). Testing homotopy types on finite
ones.**
*What they noticed.* For the functor that sends a homotopy type `X` to the presheaf `K ↦ [K, X]` on finite homotopy
types, the manuscript asserts conservativity (testing on spheres), brushes aside the absence of base points, and
asks in the margin whether the functor is even fully faithful. The editors think the conservativity false and the
base point problem real, and they report question marks in the margin at this place and at the wish to realize a
retraction in `Cat hot` by a true retraction.
*Our answer.* They are right on both counts.
- *Conservativity fails.* Our own check (Claude Fable 5.2 at effort max, by hand, today; checked by nobody else):
  let `H` be the group of finitary permutations of `N` and `G ⊂ H` the stabilizer of `0`. Every finitely generated
  subgroup of `H` has finite support and is conjugate into `G`; and two homomorphisms from a finitely generated
  group to `G` that are conjugate by `x ∈ H` are conjugate in `G` (if `x(0) = a ≠ 0`, compose `x` with the
  transposition `(0 a)`, which commutes with the image). So `BG → BH` induces bijections `[K, BG] → [K, BH]` for
  every finite complex `K`, and it is not a homotopy equivalence, `G → H` not being surjective.
- *Full faithfulness fails* already for faithfulness: a phantom map is non-trivial and is trivial on every finite
  complex mapped into its source.
- What is true (statement 4 of the finding of V.7): tests with values in spaces, not in sets of homotopy classes,
  are fully faithful; groupoid-valued tests on finite types decide maps out of countable sources.
- The marginal question about realizing a retraction in `Cat hot` by a true one, for a Thomason cofibration, we have
  not examined.

### Chapter VI (edition file Der-ChVI-345; our files `transcription/Der-ChVI-345/`)

The chapter studies categories over a base `S` (all of `Cat/S`, the fibred and the cofibred ones), their
localizations by a localizer `W`, and the derivator `HOT_W`. We have not studied this chapter line by line, so more
of the answers here are checks of types than re-derivations.

**VI.1 (remark; pages 1–5; `Der-ChVI-345_p001-005.tex`).**
*What they noticed.* In the localization axiom ("if all `X/y → Y/y` are in `W`, then `f` also") the word "also" has to
be read as "is in `W`".
*Our answer.* Right. It is the third axiom of a fundamental localizer in the later literature (Maltsiniotis;
Cisinski, *Le localisateur fondamental minimal*, 2004, Définition 1.1.3, which we opened): a functor over a base
that is locally in `W` over every object of the base is in `W`.

**VI.2 (corrections of direction and of symbols; pages 1–20 and 46–50; `_p001-005.tex` to `_p016-020.tex`,
`_p046-050.tex`).**
*What they noticed.* For a fibred category and `u: t → s` the base change functor goes `X_s → X_t`; the functoriality
of the slices is `X/s → X/t`; several arrows are renamed (`C'_0 → C`, the functor `f̄` from `X̄'` to `X`, `i_X`, and the
canonical arrow `j_{X/S}: X → C(X)`, twice).
*Our answer.* The two directions are right (inverse images are contravariant in the base, slices covariant). The
renamings we accept; they agree with the definition of `j_{X/S}` on the manuscript page the editors cite.

**VI.3 (three corrections; pages 31–35, 46–50, 71–75; `_p031-035.tex`, `_p046-050.tex`, `_p071-075.tex`).**
*What they noticed.* The dual theory is `HOT°_W(S) = (HOT_W(S°))°`: three times the manuscript leaves out the outer
passage to the opposite category.
*Our answer.* Right; it is the same rule as for the opposite derivator in Chapter I (I.4): `𝔻°(S) = 𝔻(S°)°`. Without
the outer opposite the inverse image functors would have the wrong variance.

**VI.4 (two corrections and two remarks on an adjunction; pages 36–45; `_p036-040.tex`, `_p041-045.tex`).**
*What they noticed.* The manuscript hesitates on which side the functor `C̄` is adjoint to the localization functor
`ρ`. Grothendieck corrected himself (right, not left), and the editors point out that one display still carries the
arrows of both versions, that the symbol should be `C̄` and not `C` in the sentence stating the adjunction, that one
natural transformation goes from the identity to `πΦ`, and which passage is the corrected version.
*Our answer.* We follow the corrected version that the editors identify. It agrees with the general pattern, in
which a replacement by fibrant objects is right adjoint to a localization functor where an adjoint exists. We have
not re-derived the adjunction for the functors of this chapter.

**VI.5 (corrections of statements; pages 41–45 and 56–75; `_p041-045.tex`, `_p056-060.tex` to `_p071-075.tex`).**
*What they noticed.* A condition should be an equivalence ("if and only if they are in `W`"); a fibre product is
`C' ×_S C'`; a hypothesis is on `ḡ` being a fibration; every section `i_X: X → C(X)` is in `W` (the manuscript writes
that it is "in `i_X`"); a projection is `pr_1 p'`; an object of a comma category is the composable pair
`f(x) → f(x) → s` with the identity first; the arrows defined by a lifting property against the fibrations have it
on the left, not on the right; and the target of a base change functor is the localization of the fibred
categories over `S'` by the fibrewise equivalences over `S'`.
*Our answer.* Right where types decide (the section, the target over `S'`). The lifting property is right for the
reason Quillen's axioms give: the arrows with the left lifting property against all fibrations are the trivial
cofibrations. The others we accept.

**VI.6 (corrections of notation and references; pages 91–125; `_p091-095.tex` to `_p121-125.tex`).**
*What they noticed.* A localization functor is `ρ: 𝒜 → 𝒜_0`; an adjoint pair `f_!^0 ⊣ f_0^*` goes between `𝒜'_0` and
`𝒜_0` in the other order; three references to the axioms are to Der 4′, Der 4 and Der 5; two categories carry the
index `W` (`Fibsc_{0,W} S`, `Cofibsc_{0,W} S`); a diagram for `S'` is redrawn with `HOT^lc_W(S)` mapping to `HOT_W(S)` and
`HOT°_W(S)`; "for `S`" should be "for `S'`"; a page reference is to 178, twice; a pronoun is corrected.
*Our answer.* Accepted.

**VI.7 (remark; pages 106–110; `_p106-110.tex`).**
*What they noticed.* Where the manuscript restates an older axiom L 5 and says to compare with a theorem of Chapter
XII, the number of the theorem is missing.
*Our answer.* We cannot supply it with certainty. The two numbered theorems of the first parts of Chapter XII are
Théorème 1 (ms. 12) and Théorème 2 (ms. 75–78, on the axioms W(7) and W(7 bis)). If the second is meant, the reader
should know that it is false: `W∞` does not satisfy W(7) or W(7 bis) (our return TOTASPH, GPT-6 Astra, ChatGPT Pro
mode; reviewed by Claude Fable 5.2 at effort max).

**VI.8 (question marks; pages 6–10, 71–75, 111–115; `_p006-010.tex`, `_p071-075.tex`, `_p111-115.tex`).**
*What they noticed.* Four places where the editors doubt the reading: a number "13", a word before
"vraisemblable", a verb about categories that refuse to be "closed up" by `Φ_0` or `Ψ_0`; and one where they ask what
the axiom W(4a′) is.
*Our answer.* The three readings we cannot settle without the handwriting. On W(4a′): we have not found a
definition under that name either. From the sentence, it is an axiom strong enough to make the replacement functor
`C` carry equivalences over `S` to fibrewise equivalences, of the same strength as W(4b). Which statement it is
remains open for us.

**VI.9 (remarks on the manuscript; pages 6–10, 36–50, 56–60, 111–120; `_p006-010.tex`, `_p036-040.tex`,
`_p046-050.tex`, `_p056-060.tex`, `_p111-115.tex`, `_p116-120.tex`).**
*What they noticed.* A diagram also contains two objects `Liss_0`, `Prop_0` that are joined to nothing; one sentence
has no recoverable structure; colours used in the original cannot be shown; a cross-reference to a lemma on
manuscript page 91 is supplied; two words are struck out; an index is illegible (`X_0` or `X_a`).
*Our answer.* These describe the manuscript, and we follow the editors. On the illegible index: either reading
leaves the point of the sentence intact, that the cohomology with locally constant coefficients is that of a
piece of `X` and not that of the point.

### Chapter VII (edition file Der-ChVII-456; our files `transcription/Der-ChVII-456/`)

The chapter introduces the interval categories and their types (words in `+` and `−`), the category `Ty` of types,
and the categories of paths of a given type. Our returns PRETOT and PATHS (GPT-6 Astra, ChatGPT Pro mode) work with
the same objects.

**VII.1 (two corrections; pages 1–5; `Der-ChVII-456_p001-005.tex`).**
*What they noticed.* In an interval with vertices `0, …, n` the arrow `u_i`, for `1 ≤ i ≤ n`, joins `i − 1` and `i`
(the manuscript writes `i` and `i + 1`), and a later arrow is `u_i`.
*Our answer.* Right: `n + 1` vertices carry `n` arrows, so with the index running from `1` to `n` the arrow `u_i`
ends at `i`.

**VII.2 (three corrections; pages 6–10; `Der-ChVII-456_p006-010.tex`).**
*What they noticed.* An index in an inductive choice of vertices is `s_k`; the coslice at a vertex is `I'' = s\I`;
and the statement that an interval cannot be at once symmetric and isomorphic to its opposite has to speak of the
opposite category and to except the interval with one vertex.
*Our answer.* The last one is right and can be checked. Write the type as `(ε_1, …, ε_n)`. Renumbering the vertices
backwards replaces it by `(−ε_n, …, −ε_1)`; symmetric means `ε_i = −ε_{n+1−i}`. The opposite category has type
`(−ε_1, …, −ε_n)`, and it is isomorphic to the interval exactly when `ε_i = ε_{n+1−i}`. Both together force
`ε_i = −ε_i`, impossible unless `n = 0`. The two symbols we accept.

**VII.3 (two corrections; pages 11–15; `Der-ChVII-456_p011-015.tex`).**
*What they noticed.* The natural ways of forming paths of one type from paths of another correspond to arrows of
`Cat` between the two intervals, and in the sentence the two types `τ` and `τ'` are exchanged.
*Our answer.* Right, by the Yoneda lemma: paths of type `τ` in `X` are the functors `I_τ → X`, so a natural map from
paths of type `τ` to paths of type `τ'` is composition with one functor `I_{τ'} → I_τ`. The variance is contravariant,
which is where the exchange comes from. Our returns fix the convention once: a morphism of types `τ → ρ` is a
functor `I_τ → I_ρ` that preserves both end points and is non-decreasing on the vertices (PRETOT, Definition E.1).

**VII.4 (correction; pages 16–20; `Der-ChVII-456_p016-020.tex`).**
*What they noticed.* The category that could be identified with a full subcategory of `Cat` is the category of
types `Ty`, not a single interval `I_τ`.
*Our answer.* Right. Our remark: whether the subcategory is full depends on which maps of types are admitted. With
the end points preserved and the vertices non-decreasing, as the later sections need, it is not full (a constant
functor between intervals is not a map of types).

**VII.5 (remark; pages 26–30; `Der-ChVII-456_p026-030.tex`).**
*What they noticed.* In a definition that involves two types, the editors say which is which
(`τ_1 = τ'`, `τ_2 = τ`).
*Our answer.* Accepted.

**VII.6 (corrections and a remark in the calculus of `Σ`-paths; pages 41–55; `_p041-045.tex`, `_p046-050.tex`,
`_p051-055.tex`).**
*What they noticed.* `π_0` is taken of an object `X` of `Cat`; one display has a superfluous letter; a 2-cell goes
from `c(u)c(u)°` to `1_b`; a membership is in `Σ`; a sign is `(−1)^{r−1}` at two places; and three displays about
composition are rewritten so that the composition of paths of types `τ` and `τ'` lands in the paths of the
concatenated type `ττ'`, over the product `Ty × Ty`, with the index `Σ` where needed; a presheaf category is
`Hom(X°, 𝓜)`.
*Our answer.* Accepted. The rewritten displays say what the text states in words right after them: composition of
paths with fixed end points is compatible with inverse images along maps of types. This is the structure that
PATHS (statements C.P1–C.P3 as we recorded them) uses.

**VII.7 (correction; pages 56–60; `Der-ChVII-456_p056-060.tex`).**
*What they noticed.* Of the two maps `{0, 1, 2} → {0, 1}` with `0 ↦ 0`, `2 ↦ 1`, the second sends `1` to `0`; the
manuscript writes `1` for both.
*Our answer.* Right; they are the two degeneracies.

**VII.8 (remark and a correction; pages 66–70; `Der-ChVII-456_p066-070.tex`).**
*What they noticed.* Where the manuscript restricts to index categories `T` "coming from ordered sets", described
again by a condition that the category with two parallel arrows satisfies, the editors replace the description by:
at most one arrow between two objects, non-identity isomorphisms allowed. They also correct the notation for the
set of objects below a given one.
*Our answer.* Right; it is the slip of I.3, and the class meant is that of preordered sets. The passage is the one
where Grothendieck asks whether, for a category fibred over `T` and a cofinal sequence of objects of `T`, the
sequential model has the homotopy type of the whole (ms. 99–115). For `T` a preorder, or for diagrams constant on
every hom-set, it is the classical cofinality statement. For `T = Ty` it fails in general, as Grothendieck says
himself at ms. 112; our returns add that the opposite of `Ty` is not totally aspherical and not even
quasi-filtered (TOTAL_EXACT_2, statement C.40), although its preorder reflection is directed. For which diagrams
over `Ty` the sequential model is right is open and is asked in a prompt of ours that is not yet sent
(DER_FOLLOWUP, Part B).

**VII.9 (remark, question mark and corrections; pages 71–95; `_p071-075.tex`, `_p081-085.tex`, `_p091-095.tex`).**
*What they noticed.* In one diagram the annotations belong to the solid arrows; an index in `Y_{n'} → Y_n` may have
to be `n_0` (they ask); in the duality between smooth and proper for the projections of path categories the type
has to be replaced by the opposite type `t^−`; a count is `(m − n − 1)/2`, twice; and a terminal direction is
`(−1)^{m+1}`.
*Our answer.* The duality is right: passing from `X` to `X°` exchanges smooth and proper and reverses every sign of
the type. The terminal direction is right by the sentence itself, which says that it is opposite to the parity of
`m`. The count and the index we have not re-derived.

### Chapter XII, first part (edition file Der-ChXIIa-012; our files `transcription/Der-ChXIIa-012/`)

This part states the axioms W(1), W(2), … of a localizer and develops `W`-proper, `W`-smooth and `W`-perfect functors
and `W`-fibrations.

**XIIa.1 (remarks on the manuscript; pages 1–5 and 31–35; `Der-ChXIIa-012_p001-005.tex`, `_p031-035.tex`).**
*What they noticed.* The axioms are also written with circled numbers in the original; in one diagram the editors
added a vertical arrow; a phrase "in `ξ_0`" should be deleted; an implication is circled; a diagram has some
superfluous labels `W`.
*Our answer.* These describe the manuscript; we follow the editors.

**XIIa.2 (correction; pages 1–5; `Der-ChXIIa-012_p001-005.tex`).**
*What they noticed.* Proposition 2 should conclude `f° ∈ W`, not `f° ∈ W°`: the localizer is stable under passage to
opposite categories.
*Our answer.* Right, and the statement is true for every fundamental localizer. The proof goes through the
category of I.14: the twisted arrow category of `X` maps to `X` and to `X°` by cofibrations with fibres that have an
initial or final object, so both projections are in `W`, naturally in `X` (Maltsiniotis, *La théorie de l'homotopie
de Grothendieck*, 2005; from memory).

**XIIa.3 (corrections of labels, symbols and references; pages 1–10 and 21–30; `_p001-005.tex`, `_p006-010.tex`,
`_p021-025.tex`, `_p026-030.tex`).**
*What they noticed.* The arrows of the corollary are `X/y → Y/y`; the labels 2′ and 3′ are exchanged; a property is
a_1), not a′); the connected component is that of `S` containing `s`; a hypothesis is `i_S ∈ W∞`; a possible reading
`f_s ∈ W` is proposed with a question mark; two phrases about liftings of a pair `(u, v)` of arrows of `S × S` are
reworded; the lifted arrow is `u_0`; the squares that are cartesian are the two on the right; a lemma is on
manuscript page 29; two functors and the dual `λ°` are renamed.
*Our answer.* Right where types decide (`s` is an object of `S`; the corollary compares slices over the same `y`).
The others we accept.

**XIIa.4 (two corrections of a statement; pages 11–15; `Der-ChXIIa-012_p011-015.tex`).**
*What they noticed.* One part of the theorem on perfect functors is restated: for an arrow `f: X → Y` of `Cat/S` whose
two structure maps to `S` are `W∞`-perfect, `f ∈ W` implies that every `f_s: X_s → Y_s` is in `W`. And in the companion
statement the fibres are `W`-aspherical, not `W∞`-aspherical.
*Our answer.* The restated form is the one that makes sense, and for `W = W∞` it is true: the fibres of a perfect
functor are its homotopy fibres, and an equivalence over `S` induces equivalences of homotopy fibres. For a larger
`W` we have not re-derived it, and the reader should be careful: our return POLES (GPT-6 Astra, ChatGPT Pro mode;
reviewed by Claude Fable 5.2 at effort max) shows that the fibration axioms of Chapter XVI fail for the homology
localizer (a functor to the circle with acyclic total space and non-acyclic fibre), so "an equivalence of total
spaces is an equivalence of fibres" cannot be taken for granted beyond `W∞`.

**XIIa.5 (correction; pages 21–25; `Der-ChXIIa-012_p021-025.tex`).**
*What they noticed.* For `W`-smooth functors the inclusions that must be `W`-aspherical are `X_y → y\X`.
*Our answer.* Right: smooth is the dual of proper, and the dual of the inclusion of the fibre in the slice `X/y` is
its inclusion in the coslice.

**XIIa.6 (remark; pages 31–35; `Der-ChXIIa-012_p031-035.tex`).**
*What they noticed.* In the proof of a) ⟹ b) the manuscript gives a hint in parentheses (take the base change to be
`Y/s`, then `Y/s'`), and the editors do not see how it bears on the assertion.
*Our answer.* Our reading: condition a) is a condition for all base changes, and b) is its case for the two slices,
because `X ×_Y (Y/s) = X/s`; the arrow `X/s → X/s'` of b) is then the map between two base changes of `X`. We have not
checked this against the statement on manuscript page 4 to which the editors refer.

**XIIa.7 (remark and corrections; pages 31–40; `_p031-035.tex`, `_p036-040.tex`).**
*What they noticed.* The editors recall the definition of `Φ_S(X)`: the category fibred over `S` given by
`s ↦ s\X`. Around it: a step holds by b), not c); a hypothesis is restated (`f` is a right `W`-fibration, that is,
`W`-presmooth and a `W`-pseudofibration); in two dual conditions the reference is to a), and the slices and coslices
are those of `S` (`S/s_0 → S/s_1`, `s_1\S → s_0\S`), with `s_1\X → s_0\X` for `X`; and the sufficient hypothesis on `X` is
presmooth, not preproper.
*Our answer.* The definition is the standard replacement of a functor to `S` by a fibred category, with the
canonical `i_X: X → Φ_S(X)`. The slices of `S` are right by types (the base is `S`). "Presmooth" agrees with the fact
that `Φ_S` is built from coslices. The rest we accept.

**XIIa.8 (two corrections; pages 41–44; `Der-ChXIIa-012_p041-044.tex`).**
*What they noticed.* The objects `η_S`, `η_{S'}` are the inverse images of `η` along the structure maps `S → e`,
`S' → e`; and the structural morphism of a counterexample is `f: Φ(Z) → S`.
*Our answer.* The first is right and gives the relation `η_{S'} = p^*(η_S)` that the text uses. The second we accept.

### Chapter XII, second part (edition file Der-ChXIIb-012; our files `transcription/Der-ChXIIb-012/`)

This part treats categories glued from an open and a closed part, the sieves Grothendieck calls *dwyériennes*,
total asphericity (Définition 1, ms. 88–89), and the axioms W(7), W(7 bis). It is the part our returns TOTASPH,
PRETOT, TOTEX and TOTAL_EXACT_2 work on.

**XIIb.1 (corrections in the gluing construction; pages 1–20; `Der-ChXIIb-012_p001-005.tex` to `_p016-020.tex`).**
*What they noticed.* A comparison is an equivalence of categories; `(𝒳, 𝒰, 𝒯)` is a triple, not a pair; the object
`X'` is an inductive limit rather than an amalgamated sum at one place, and it is `X'`, not `X`, that is identified
with the amalgamated sum at another; a letter is `T`; a count is three; "they are stable" should be "it is stable",
with the categories `U'/t'`; the editors ask whether an auxiliary category `Y` is `X_1`.
*Our answer.* Accepted. The triple is right by count; the rest are readings that the surrounding text supports. To
the question we have no answer beyond theirs.

**XIIb.2 (remark; pages 21–25; `Der-ChXIIb-012_p021-025.tex`). Two notions called "totally aspherical".**
*What they noticed.* The total `W`-asphericity defined here is not the notion of the same name in *Pursuing Stacks*.
*Our answer.* Right, and the relation between the two is now known. The notion of *Pursuing Stacks* (products of
two representable presheaves are aspherical; equivalently the diagonal is an aspherical functor) is, up to the
choice of variance, a homotopical form of siftedness. The notion of this chapter asks that every category
receiving a final functor be aspherical; for `W∞` it means that every component of every category of elements is
weakly contractible, equivalently that ordinary colimits of simplicial sets over the index are homotopy colimits
(TOTASPH C.5). Neither implies the other: the opposite of the simplex category is sifted and not total in the
sense of this chapter (TOTAL_EXACT_2 D.2, by the simplicial circle); the category of finite ordinals and
injections is total in the sense of this chapter and not sifted (two injections into a common ordinal keep the
relative position of their images under every further injection, so the category of such pairs is disconnected). Together they force filteredness (PRETOT F.3, TOTEX D.4).
All four returns are by GPT-6 Astra (ChatGPT Pro mode), reviewed by Claude Fable 5.2 at effort max or Claude Opus
5.5 at effort max.

**XIIb.3 (two corrections; pages 21–25; `Der-ChXIIb-012_p021-025.tex`).**
*What they noticed.* In the example with a quotient of groups, an element is of square different from 1, and an
action is by `α²`.
*Our answer.* Accepted; we have not reworked the example.

**XIIb.4 (corrections and a remark around the counterexample; pages 26–35; `_p026-030.tex`, `_p031-035.tex`).**
*What they noticed.* The categories that must be 0-connected are the `y\X`, not their sets of components; the
1-connected object `Y` is an object of `Cat`; in the example built from cells `e_i^±` the editors add the order
relations inside each sign, `e_0^+ ≤ e_1^+ ≤ e_2^+` and the same for `−`; Proposition 11 refers to the situation
of manuscript page 104; the pushout is `X' = U' ⊔_U X`, twice; and the base change formula is
`i'^*(t') = p_!(i^*(t))`.
*Our answer.* Right. The first two and the pushout are fixed by types. With the added relations the six cells form
the face order of the cell structure of the 2-sphere with two cells in each dimension, which is what the example
needs. Grothendieck notes that he realizes the same example with finite categories in the appendix (ms. 10–12);
in the review of TOTASPH we recomputed the homology of the four-object category of that appendix (the type of
`S²`).

**XIIb.5 (corrections; pages 36–50; `_p036-040.tex`, `_p041-045.tex`, `_p046-050.tex`).**
*What they noticed.* A functor is `W`-coaspherical; certain inclusions are of closed, not open, parts; two maps are
`f'_1: 1\𝒳 → 1\𝒳'` and `f'_2: 2\𝒳 → 2\𝒳'`; a page reference is 126.
*Our answer.* Accepted.

**XIIb.6 (remark and three corrections; pages 56–60; `Der-ChXIIb-012_p056-060.tex`).**
*What they noticed.* The index category is `I = S°`; and the property of a square that is equivalent for `Q` and for
`Q°` by Proposition 14 is being `W`-homotopically cocartesian (the manuscript writes another word, three times).
*Our answer.* Right: the sentence before states exactly that `φ_Q ∈ W` and `φ_{Q°} ∈ W` are equivalent, and that is
the definition of homotopically cocartesian.

**XIIb.7 (remark; pages 66–70; `Der-ChXIIb-012_p066-070.tex`).**
*What they noticed.* The manuscript states, granted W(7 bis), that at an object `x` of any of the three pieces
`X_0, X_1, X_2` the comparison `φ_Q` is `W`-smooth at `x` exactly when `f_i: X_i → Y` is. The editors say this is not
really so for `i = 0`.
*Our answer.* We agree with the reservation. `X_0` is the part along which the two others are glued, and the
category under an object of `X_0` in the glued category meets both `X_1` and `X_2`, so smoothness there is not a
condition on `f_0` alone. Two further limits of the sentence, from our returns: W(7) and W(7 bis) fail for `W∞`
(TOTASPH: Théorème 2 of this chapter is false), so the statement is conditional on an axiom that the main localizer
does not satisfy.

**XIIb.8 (remark and corrections; pages 66–72; `_p066-070.tex`, `_p071-072.tex`).**
*What they noticed.* Smoothness is at the object `x_0`, not at the arrow `u`; from a certain point on the letters
`F` and `G`, and `F'` and `G'`, exchange their roles while `p` and `q` do not, and accordingly the arrows of `T` are
those that do not factor through `F`; Définition 2 c) is on manuscript pages 109–110.
*Our answer.* Accepted. The page reference agrees with our own reading (Définition 2, the strictly and totally
`W`-aspherical functors and the *dwyériennes* sieves, is at ms. 109–114).

### Chapter XII, third part (edition file Der-ChXIIc-30-03-03; our files `transcription/Der-ChXIIc-30-03-03/`)

**XIIc.1 (remarks; pages 1–10, 36–45, 56–60; `Der-ChXIIc-30-03-03_p001-005.tex`, `_p006-010.tex`, `_p036-040.tex`,
`_p041-045.tex`, `_p056-060.tex`).**
*What they noticed.* "Sheaf" and "presheaf" are used without distinction in this part; a point `z` is `x` regarded
as a point of `Z`; from a certain place on `X_i` and `X'_i` exchange their roles; two arrows are identified
(`X_1 → S`, and `β_i: S → X_i`).
*Our answer.* Accepted; on a category without topology the two words mean the same. Our remark on the footnote of
Grothendieck that stands at one of these places: he says that a category with fibrations `(𝓜, W, Fib_W)` defines a
derivator on finite ordered sets and that this is proved without much trouble. It is a theorem now (Cisinski,
*Catégories dérivables*, 2010; from memory).

**XIIc.2 (corrections; pages 6–20 and 46–60; `_p006-010.tex`, `_p016-020.tex`, `_p046-050.tex`, `_p051-055.tex`,
`_p056-060.tex`).**
*What they noticed.* A Hom-set is `Hom_π`; "the square" should be "the diagram"; a diagram lies in `𝓜`, over `S`; the
functor `p_*`, isomorphic to `ε^*`, is a right adjoint, not a left one; a square is `W`-cocartesian, not
`W`-cartesian; the display defining `φ_Q` is rewritten.
*Our answer.* The adjoint is right: `p_*` is right adjoint to `p^*`. The cocartesian reading we accept; it is the
notion for which `φ_Q` is defined (compare XIIb.6). The others we accept.

**XIIc.3 (question mark; pages 6–10; `Der-ChXIIc-30-03-03_p006-010.tex`).**
*What they noticed.* In a chain "`c_2` implies `c_1`, which is equivalent to `b_1`", written at a moment where it is
not yet known that `Z` is 1-connected, the editors question the equivalence.
*Our answer.* We cannot settle it in this file. The classes `a_n`, `b_n`, `c_n` of this part (ms. 178–187) are examined
in our return POLES; we have not gone back to its statements for this entry, so the question stays open here.

### Appendix to Chapter XII (edition file Der-ChXIIapp-19-06-03; our files `transcription/Der-ChXIIapp-19-06-03/`)

**XIIapp.1 (four corrections; pages 1–14; `Der-ChXIIapp-19-06-03_p001-005.tex`, `_p006-010.tex`, `_p011-014.tex`).**
*What they noticed.* The index of the arrows `u_i` runs over `[1, 2N]`; two Hom-sets are `Hom(b × b, b)` and
`Hom_Z(z, a)`; a closed immersion goes into `V'_0`.
*Our answer.* Accepted; the first is fixed by the induction that follows, the last by the display `p_0: V → V'_0`
right after it. The finite categories of this appendix are the ones mentioned in XIIb.4.

### Chapter XIV (edition file Der-ChXIV-07-10-10; our files `transcription/Der-ChXIV-07-10-10/`)

**XIV.1 (four remarks; pages 1–10; `Der-ChXIV-07-10-10_p001-005.tex`, `_p006-010.tex`).**
*What they noticed.* "Square" means commutative square. At three statements about squares that are cartesian in a
homotopical sense (the composition of two such squares; a cube in which three of four comparison maps are
isomorphisms; the claim that a square is `W`-cartesian as soon as its image in the homotopy category is
homotopically cartesian) the editors send the reader to their postface.
*Our answer.* Their postface is theirs and is read in the edition. We have not studied this chapter, so we only
record what is known in general. Statements of these three kinds hold when "cartesian" is a property of an object
of the value of a derivator on the square (the pasting of cartesian squares, and the detection of isomorphisms on
a cube, are theorems for derivators: Maltsiniotis; Groth 2013; from memory). They need care when the property is
defined in the homotopy category alone: the image of a square there determines the square only up to
non-canonical choices, and a weak universal property does not compose. Whether Grothendieck's definitions in this
chapter avoid that difficulty we have not checked.

### Chapter XIII (edition file Der-ChXIII-25-01-04; our files `transcription/Der-ChXIII-25-01-04/`)

The chapter rebuilds Quillen's model categories from a localizer `W` on a category `𝓜`: classes of arrows closed
under lifting conditions, `W`-fibrations and `W`-cofibrations, accessibility, and the derivator
`I ↦ 𝓜(I)W(I)^{-1}`. We have not studied it line by line.

**XIII.1 (three corrections and three remarks; pages 1–5; `Der-ChXIII-25-01-04_p001-005.tex`).**
*What they noticed.* The two closure operations `Φ ↦ Φ̃` and `Ψ ↦ Ψ̄` are maps from the set of subsets of `Fl(𝓜)` to
itself; the formulas on intersections are for parts closed on the left, their duals for parts closed on the right;
a pronoun refers to the two parts `Φ` and `Ψ`.
*Our answer.* Right. The operations are the two halves of the Galois connection defined by the lifting relation on
arrows; each takes a set of arrows to a set of arrows, reverses inclusions, and the closed sets are the two
classes of a weak factorization system in today's terms.

**XIII.2 (correction; pages 6–10; `Der-ChXIII-25-01-04_p006-010.tex`).**
*What they noticed.* Axiom M 0 asks for finite projective and finite inductive limits; the manuscript writes the
projective limit twice.
*Our answer.* Right; it is Quillen's first axiom.

**XIII.3 (four remarks; pages 6–10; `Der-ChXIII-25-01-04_p006-010.tex`).**
*What they noticed.* The editors recall what a `W`-fibration is (a morphism along which, after any base change of
its target, the pull-back of an arrow of `W` between objects over the new base is again in `W`), and they spell out
three notations: the arrows over `S` that are in `W`; the category of `W`-fibrations with target `S`; the category of
`W`-cofibrations with source `S`.
*Our answer.* Accepted. The notion recalled is the one that Rezk later called a *sharp* map (1998; from memory); in
a right proper model category every fibration is one. It is the notion `Fib_W` that our returns POLES and GALOIS
use for localizers of `Cat`.

**XIII.4 (corrections; pages 11–30; `_p011-015.tex`, `_p016-020.tex`, `_p021-025.tex`, `_p026-030.tex`).**
*What they noticed.* A display should read `(TC_0)~ = TC`, `(C_0)~ = C`; "admissible" parts are "accessible" ones;
the class that is to be as large as possible is `TC = W^univ`; three times the homotopy category of fibrant objects
is formed with the left homotopy relation (`π_g 𝓜_f`), and the comparison is `π_g 𝓜_f → 𝓜_f W_f^{-1} ≃ Ho_W`; one
class is `Ψ' = TF(I')`; a condition referred to is that of footnote 10; `𝓜(I)` is the category of presheaves on `I`
with values in `𝓜`, with `W(I)` the arrows that are in `W` at each object.
*Our answer.* Accepted; "accessible" is the word the chapter itself uses later, and the homotopy relation on
fibrant objects is the left one in Quillen's theory.

**XIII.5 (cross-references; pages 31–40; `_p031-035.tex`, `_p036-040.tex`).**
*What they noticed.* The editors supply four references: to Chapter I (the axiom Der 1, and manuscript pages
111–112), to Chapter XII for the axioms of fundamental localizers, and to Chapter XII, page 253, for homotopy
fibre products.
*Our answer.* Accepted.

**XIII.6 (corrections; pages 31–40; `_p031-035.tex`, `_p036-040.tex`).**
*What they noticed.* A case distinction is on `i < 0` and `i > 0`; the adjunction between `u^*_W` and `u^W_*` is
between the localized categories `𝓜(I')_f W(I')_f^{-1}` and the corresponding one for `I`, not between the
categories of fibrant objects themselves; a reference is to (∗∗∗); a variable is struck out.
*Our answer.* The second is right by types: the two functors are defined on the homotopy categories. The others we
accept.

**XIII.7 (remark; pages 41–45; `Der-ChXIII-25-01-04_p041-045.tex`).**
*What they noticed.* Where the manuscript asks whether a product of arrows of `W` between fibrant objects is in
`W`, the editors say what "fibrant" means here: the map to the final object is a fibration.
*Our answer.* Accepted. To Grothendieck's question itself: in a Quillen model category the answer is yes, for
arbitrary products (the product functor is right Quillen, and Ken Brown's lemma applies). In the weaker setting of
this chapter, with `W`-fibrations only, we have not decided it. It matters for the first axiom of a derivator on
infinite sums of index categories.

**XIII.8 (correction and remarks on accessibility; pages 41–55; `_p041-045.tex`, `_p046-050.tex`, `_p051-055.tex`).**
*What they noticed.* The classes `C` and `TC` are closed on the left, not on the right; a reference to SGA 4, I,
9.12 is supplied; one assertion is immediate, because in an index set that is large with respect to `π` a subset of
cardinality at most `π` has an upper bound, which can be adjoined; a lemma as stated is evident for the same
reason, while the proof given in the manuscript establishes more, and the editors say what; a system of objects
lies in `E`, not in `M`, twice; a slice is `M^π/X_i`; and the claim that the `π`-accessible objects form a system of
strict generators is not clear to the editors without further hypotheses.
*Our answer.* The first is right: cofibrations and trivial cofibrations are defined by a lifting property on the
left. The short arguments are right. The last reservation is justified: that every object is the colimit of the
small objects over it is part of what it means for a category to be accessible (Makkai and Paré; Adámek and
Rosický), not a consequence of the other conditions, so it has to be assumed at this point or proved from an
explicit hypothesis. Accessibility is also the hypothesis under which the main question of our prompt on
localizers is posed (POLES F.14).

### Chapter XV (edition file Der-ChXV-05-11-10; our files `transcription/Der-ChXV-05-11-10/`)

From here on the entries are short, by instruction: one entry per point, the answer in one or two sentences.
"By hand" marks a check of ours made for this file and read by nobody else.

**XV.1 (remark; pages 6–10; `_p006-010.tex`).**
*What they noticed.* When `𝓜` has small sums, the class `C''_0` generated by `C_0` under cobase change and small
amalgamated sums has a direct description: its arrows are the cobase changes of sums of arrows of `C_0`.
*Our answer.* Right (by hand): those cobase changes form a class closed under both operations, and a sum `⨿ f_i` is
an amalgamated sum of cobase changes of the `f_i`.

**XV.2 (remark; pages 6–10; `_p006-010.tex`).**
*What they noticed.* In the factorization display `Φ` is the class `C̃_0`; a symbol `Φ_α` with an ordinal index is
used nearby with another meaning, and the two must be kept apart.
*Our answer.* Accepted; a point of notation.

**XV.3 (eight remarks on the manuscript; pages 16–20, 31–40, 61–70).**
*What they noticed.* The labels (3.10), (3.11), 5.3, 5.7 and 5.8 are each used twice; a struck-out passage follows
at manuscript pages 109–110; the axioms Loc (6)–Loc (8) were first numbered Loc (5)–Loc (7); two words are supplied
to introduce the list of axioms restated in a footnote.
*Our answer.* Facts about the manuscript, accepted. A reference to a doubled label is resolved by its page.

**XV.4 (remark; pages 56–60; `_p056-060.tex`).**
*What they noticed.* Theorem 8.4, on test categories for a localizer `W`, says it uses every axiom but the fibration
axiom W (4); the editors add the connectedness axiom W (5) to the exceptions.
*Our answer.* Right: no step of the statement involves `π_0`. The published theory proves the corresponding theorem
from three axioms, none of them about connectedness (Maltsiniotis, Astérisque 301; Cisinski, Astérisque 308; from
memory).

**XV.5 (remark; pages 61–65; `_p061-065.tex`).**
*What they noticed.* A footnote replaces condition (d) of Theorem 8.4, 1° (every `A/a` is a test category) by (d′):
`j_A` sends `W` into the `W_A`-aspheric arrows, and then by the special case of (d′) for `C → e` with `C` having a
final object. The editors: (d′) is strictly stronger than (d); the special case is equivalent to (d).
*Our answer.* Right, and (d′) holds for no non-empty `A` unless `W` is everything (by hand): `j_A(Δ_1)` is the
Lawvere object `L_A`, the arrow `e → Δ_1` is in `W`, and `j_A` of it is a section `e_A → L_A` whose pull-back along
the section classifying the empty (or the full) subobject of `a` is the empty presheaf. The special case says that
each `A/a` is a weak test category: a local test category in today's terms.

**XV.6 (three corrections; pages 61–65; `_p061-065.tex`).**
*What they noticed.* The construction that factors `f: X → Y` in `A^` as a monomorphism followed by an arrow of
`W_A` is the mapping cylinder, not the mapping cone.
*Our answer.* Right: the cylinder `Y ⨿_X (I × X)` contains `X` and retracts onto `Y`; the cone does not factor `f`.

**XV.7 (correction; pages 61–65; `_p061-065.tex`).**
*What they noticed.* The footnote announcing a definitive version of the axioms should point to Chapter XVI.
*Our answer.* Right: Chapter XVI is where the axioms Loc are set out again.

**XV.8 (remark; pages 71–75; `_p071-075.tex`).**
*What they noticed.* In the proof of Proposition 9.12 the editors hold that, of the two implications between (c)
and (c′), the manuscript calls the wrong one trivial; they locate the proof of the other between the statement of
Corollary 9.13 and its proof.
*Our answer.* We read it differently (by hand). With (c): some map `Hom_Cat(X, Y) → Hom_{Hot_W}(X, Y)` is not
constant, and (c′): the non-empty objects of `Hot_W` do not form a category equivalent to the point, (c) ⟹ (c′) is
immediate, as the manuscript says. What the manuscript's diagram lacks is (c′) ⟹ (c), without which "(c) ⟹ (a)"
does not close the circle; the passage the editors point to proves exactly that, in contrapositive form (all maps
constant ⟹ `Hot_W^* ≃ e`, through the quotient category `𝓗`). So the passage is the right one and is needed; the
note reads correctly for the negated conditions.

**XV.9 (two remarks; pages 71–77; `_p071-075.tex`, `_p076-077.tex`).**
*What they noticed.* Two steps use more than Loc (1, 2, 3): that `Cat → Hot_W` commutes with finite products (proof
of 9.13) and that `u_!` exists for `HOT_W` (10.1, 1°). Both need the relative form Loc (3 bis) of the localization
axiom; for the first the editors point to Pursuing Stacks, section 64.
*Our answer.* Right for the known proofs. `f ∈ W ⟹ f × B ∈ W` comes from the relative axiom over `B` (the slices
are `f × (B/b)`, which the weak axiom handles), and `u_!` is modelled by composing categories over `I` with `u`,
which respects equivalences local over the base by the relative axiom over the slices of `J`. Whether 9.11–9.13
hold for a weak localizer is open for us: without products the argument of 9.13 gives only that two objects of a
category become equal as arrows from the point (by hand).

**XV.10 (remark; pages 76–77; `_p076-077.tex`).**
*What they noticed.* Grothendieck's footnote says that Der 1 for finite sums of index categories holds for `HOT_W`
with no axiom on `W`; the editors: the identities must be in `W`.
*Our answer.* Right: the localization of a finite product of categories is the product of the localizations when
each class of arrows contains the identities, and not otherwise (take one class empty).

### Chapter XVI (our files `transcription/der-ch16/`)

**XVI.1 (remark; pages 1–5; `der-ch16_p001-005.tex`).**
*What they noticed.* A footnote says that the relative localization axiom holds for the localizer `W_D` of a
prederivator `D` satisfying Der (4, 5); the editors add Der (2), in the numbering of Chapter I.
*Our answer.* Right: Der (4, 5) show that the comparison of the two direct images is an isomorphism on each fibre of
the base, and Der (2), by which isomorphisms are detected on the fibres, is what makes it an isomorphism. In the
literature the `D`-equivalences of a derivator form a basic localizer (Cisinski 2003; from memory).

**XVI.2 (remark and correction; pages 6–10 and 51–55; `_p006-010.tex`, `_p051-055.tex`).**
*What they noticed.* Stability of `W` under finite products, and the commutation of `hot_W` with finite products,
need Loc (3 bis), not only Loc (1, 2, 3).
*Our answer.* Right, for the reason given in XV.9. We know no proof from the weak form and no counterexample.

**XVI.3 (remark; pages 6–10; `_p006-010.tex`).**
*What they noticed.* The lemma "if `W` is stable under the products of a given type, these exist in `𝓜W^{-1}` and
`ho_W` commutes with them" is doubted for infinite products; it holds for the weak equivalences of a Quillen model
category.
*Our answer.* The doubt is justified (by hand). For finite families the lemma holds when `W` contains the
identities: the adjunction between diagonal and product descends to the localizations, and the localization of
`𝓜 × 𝓜` is the product of the localizations. For an infinite family that last step fails in general, because a
family of zigzags of unbounded lengths is not a zigzag of families; it holds with a calculus of fractions or a model
structure. In general we have neither proof nor counterexample.

**XVI.4 (three remarks on the manuscript; pages 6–15 and 41–45).**
*What they noticed.* The numbers 2.7–2.9 occur twice; the manuscript's page numbering shifts at one point; one word
is read with a question mark.
*Our answer.* Accepted.

**XVI.5 (remark; pages 46–50; `_p046-050.tex`).**
*What they noticed.* Where Grothendieck says he has not proved, and does not doubt, that `W_ω` differs from `𝐖_∞`,
the editors record that Cisinski proved `W_ω = 𝐖_∞`.
*Our answer.* Right if, as the context indicates, `W_ω` is the smallest fundamental localizer: it is Cisinski's
theorem that `𝐖_∞` is the smallest basic localizer (*Le localisateur fondamental minimal*, 2004). Consequence: the
smallest localizer `W̃_∞ ⊂ 𝐖_∞` with all the stability axioms, asked for a few lines later, is `𝐖_∞` as well.

**XVI.6 (remark; pages 56–59; `der-ch16_p056-059.tex`).**
*What they noticed.* Six lines after Corollary 7.7.3 do not belong to what precedes them.
*Our answer.* They are the end of a base-change statement with its proof: for a cartesian square with `f`
`W`-smooth or `p` `W`-proper, the base-change arrow between `p^*f_!` and `f'_!q^*` is an isomorphism. Its beginning
is not there and we have not located it. In the literature: smooth and proper base change for `W` (Maltsiniotis,
Astérisque 301; from memory).

### Chapter XVII (our files `transcription/der-ch17/`)

**XVII.1 (remark and correction; pages 11–20; `der-ch17_p011-015.tex`, `der-ch17_p016-020.tex`).**
*What they noticed.* The diagrams of type (∗) to be combined are those of manuscript page 10; the totally
cocartesian cube of diagram (∗∗) is built from the cocartesian square `X` by the arrow `(f_0, f_1)` of the category
of arrows of `𝓜`, not by `f_0` alone.
*Our answer.* Accepted; the second fits the diagram, where `f_0: X_0 → Y_0` and `f_1: X_1 → Y_1` are both given. We
have not studied the chapter.

### Chapter XVIII (our files `transcription/der-ch18/`)

**XVIII.1 (twelve remarks on the manuscript; pages 6–10, 36–40, 51–55, 61–80, 86–95, 106–110, 126–130, 191–195).**
*What they noticed.* A category of pairs is the one defined a page earlier; an index was struck out by the author
in 4.5.9.1; `𝓕^π` and `𝓕_π` alternate and are unified as `𝓕^π`; an item 2° stands on another manuscript page; two
criteria are in parentheses in the manuscript; the numbers 4.9.1–4.9.6 (4.9.3 three times) and 4.10.1–4.10.4 are
reused; an arrow `v_2: i_2 → i_3` and an implication b ⟹ c are supplied; connecting words are supplied in three
places; a paragraph referred to does not exist.
*Our answer.* Accepted. The supplied arrow is required by the equation `f(v_2)f(u_2) = w'` that follows.

**XVIII.2 (remark; pages 36–40; `der-ch18_p036-040.tex`).**
*What they noticed.* The second half of a sentence, an example about the subcategories `J` of `I` with
`card Fl J ≤ π`, needs correcting; the editors do not say how.
*Our answer.* Open: we have not worked out the corrected statement.

**XVIII.3 (eight corrections we re-derived; pages 71–75, 101–110, 136–140, 151–165, 196–200).**
*What they noticed.* For `u: C → C'` the functor `u_*` goes `C^ → C'^`; `π'^{π_0} = π'` (not `π_0`) for
`π' = π^{π_0}`; "may be false for 1°, 2°" should be "1°, 3°" (with a question mark); `f(x_i)` lies in `Ob T`;
`𝓔_0 = 𝓔|𝓒_0`; a composite is `λ^* pr_{t_0}`; `λ ∈ Hom_𝓒(f(x), f(y))`; `A = E∖B`.
*Our answer.* Right: by types (the first, fourth, fifth, sixth and seventh), by cardinal arithmetic
(`(π^{π_0})^{π_0} = π^{π_0}`), by the sentence itself (2° has just been called evident), and because `A = E∖A`
defines nothing.

**XVIII.4 (nineteen corrections accepted without re-derivation; pages 81–90, 101–105, 116–135, 146–170, 181–185,
196–200).**
*What they noticed.* `i ∈ Ob I` for `i' ∈ Ob I'`; b″) for c′) in a list of five conditions (twice); `δ'_A` for the
diagonal of `I'`; perhaps `lim→` for another limit sign; c′) is a variant of c), not of d); c′) for d′) three times;
`𝓜_π/x` for `𝓜(π)/x` twice; `π` for another cardinal; `ε_s(f)`; `s ∈ Ob C` for `s ∈ S` twice; a reference that
should be to the proposition at hand; a projector in `𝓒`; `α ∈ I_{α_0}` for `α ∈ I`; `𝔪_Ψ`.
*Our answer.* Accepted: slips of letters and labels. We have not studied the chapter.

### Chapter XIX (our files `transcription/der-ch19/`)

**XIX.1 (remark; pages 21–25; `der-ch19_p021-025.tex`).**
*What they noticed.* An item a) is not followed by an item b).
*Our answer.* Accepted.

## Not covered, and what to check before publication

- **Count.** The entries cover the 381 corrections, remarks and question marks that our table has in the chapter
  files (Chapter X has none). The figure 399 in the introduction includes 18 rows filed under our own
  `DECISIONS.json`; these were not examined.
- **The pile.** `NOTES_PILE_20261115.tsv` appeared after this table was made. Its counts (912 notes) were not
  reconciled with ours (943 rows of `REMOVED_NOTES_20261115.tsv` under `transcription/`).
- **One note in Chapter V** was missing from our table and is treated in V.10; there may be others like it.
- **Edition file names** for Chapters XVI–XIX are not in our table; the entries cite our files and pages.
- **Left open in the answers:** XV.9 (9.11–9.13 for a weak localizer), XVI.2 (products from the weak axiom), XVI.3
  (the lemma for infinite products), XVI.6 (where the six lines begin), XVIII.2 (the corrected sentence).
- **Citations "from memory"** were not reopened. **"By hand"** checks (V.10, XV.1, XV.5, XV.8, XV.9, XVI.3) were read
  by nobody else; XV.8 disagrees with the editors' note and should be read by a second reader first.

Claude Fable 5.2 at effort max, 15 November 2026.
