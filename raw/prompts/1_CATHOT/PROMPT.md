# CATHOT: what categories modulo natural transformations can represent

Package 1 of 7 on Alexander Grothendieck, *Les Dérivateurs* (1990–91). File prefix for your deliverables: `CATHOT`.

## What is to be settled

In Chapter V (ms. 11–13) Grothendieck writes `Cat hot` for the category of small categories with `Hom_{Cat hot}(X, K) = π0 Fun(X, K)`: functors modulo finite zigzags of natural transformations. The localization functor is `φ: Cat hot → Hot`. He asserts (V ms. 37) that `φ` has a fully faithful right adjoint `ψ`,

    Hom_Hot(φX, Y) ≅ Hom_{Cat hot}(X, ψY),

calls `ψφ(K)` the *enveloppe de Thomason–Kan* of `K` (ms. 42–43), and uses it to pass from ind-objects of `Cat hot` representing the Hom-functors of a localization to homotopy types (V ms. 37–52; VII §§10–11; IX). The editors ask for a proof of the adjoint; the companion's audit (III-V block "The unproved reflection must remain a hypothesis") could neither prove it nor find it in the literature. He also asks repeatedly whether homotopy types can be tested on *finite* categories: whether `Hot → Hot_0^` (presheaves of sets on the homotopy types of finite categories) is faithful, fully faithful or conservative (V ms. 52; VII ms. 121–127 and 150; IX ms. 9–13). The companion answered these negatively for sets of unpointed homotopy classes.

This package settles what `Cat hot` can and cannot represent, replaces the envelope by correct statements at every place he uses it, and gives the exact positive form of the finite-test idea.

## Leads (unverified; prove or refute each)

- **Lead 1.** `ψ` does not exist. There is no small category `K` with a bijection `π0 Fun(X, K) ≅ [BX, K(Z/2, 2)]` natural in `X ∈ Cat`. Sketch: taking `X = e` gives `π0 K = pt`. Let `G` be the finitary alternating group on a set of cardinality greater than that of the set of arrows of `K`. `G` is simple, so every homomorphism from `G` to an automorphism group of an object of `K` is trivial; every functor `BG → K` is constant on arrows, `Fun(BG, K) ≅ K`, and `π0 Fun(BG, K) = pt`. But `[BG, K(Z/2, 2)] = H²(G; Z/2) = Hom(H_2(G; Z), Z/2) = Z/2`, since `G` is perfect with `H_2 = Z/2`.
- **Lead 2.** Call `K` *local* when `π0 Fun(X, K) → [BX, BK]` is bijective for every small `X`. Groupoids are local, and so is every category isomorphic in `Cat hot` to a groupoid. Conjecture: these are all the local categories, and the homotopy types `Y` for which `X ↦ [BX, Y]` is representable on `Cat hot` are exactly the 1-types.
- **Lead 3.** For the ∞-category of spaces the finite-test statement is true: spaces are the Ind-completion of finite spaces, so restriction of the space-valued Yoneda functor to finite spaces is fully faithful. The failures are produced by passing to sets of homotopy classes; in the homotopy 2-category conservativity already returns (Arlin–Christensen, Theorem 4.3).

## Parts

**A. The setting.** Define `Cat hot`, `φ`, the class inverted by `φ`, and prove the formal facts he uses (V ms. 38–42, Propositions 1 and 2 and their corollaries on reflective localizations and ind-categories), separating what is formal from what depends on `ψ`. State precisely what Thomason's model structure gives: a formula for `[BX, BK]` in terms of functors into a fibrant replacement of `K` after replacing `X` (which replacement, and why it cannot be omitted; the companion's counterexamples in VII ms. 136 are attached).

**B. Lead 1**, with a complete proof: the universe and cardinality bookkeeping, the simplicity of finitary alternating groups, the computation of `H_2`, and the identification of `π0 Fun(BG, K)`. Then the sharper statements: non-representability of `X ↦ [BX, Y]` for every `Y` in a class you determine (all simply connected non-contractible `Y`? all `Y` that are not 1-types?). This needs, for a given `Y`, groups `G` of unbounded cardinality admitting no non-trivial homomorphism to any group of smaller cardinality and an essential map `BG → Y`: construct them or find the obstruction.

**C. Lead 2.** Classify the local categories and the representable homotopy types. Decide in particular: whether a local `K` must have `BK` a 1-type; whether a local `K` with `BK` a 1-type is isomorphic in `Cat hot` to a groupoid; whether the local objects form a reflective or coreflective subcategory of `Cat hot` (the 1-truncation `X ↦ Π1 X` is a candidate reflector: prove what is true).

**D. Bounded and ind-versions.** (i) For an infinite cardinal `κ`, is `X ↦ [BX, Y]`, restricted to categories with fewer than `κ` arrows, representable by a category `K_κ` (necessarily large relative to `κ`)? (ii) Restricted to finite categories `X`: is it representable, or ind-representable in `Cat hot` by a sequence of finite categories, as his "ind-catégories" `(K_n)` suggest (V ms. 43–46)? (iii) Is `X ↦ [BX, Y]` on all of `Cat hot` a filtered colimit of representables in any useful sense (indexed by cardinals)? Give constructions or obstructions; `Y = K(Z/2, 2)` and `Y = S²` are the test cases.

**E. Repairing the manuscript.** Go through every use of `ψ`, of Thomason–Kan envelopes and of "catégories de Thomason–Kan" in V ms. 37–52, VII ms. 108–136 and 150–156, and IX ms. 9–13 and 22–25. For each, give the corrected statement that is true, with proof: typically an ind-object statement in `Hot` that needs no adjoint (the companion has one such, V block "Finitely many objects already give a uniform stage"), or a statement about derived mapping spaces. Explain his own observation (VII ms. 136) that the path categories "n'ont aucune tendance à être des catégories de Thomason-Kan" in the light of B and C.

**F. Finite tests, exactly.** Collect the negative results with proofs or precise citations (non-conservativity and non-faithfulness of `Hot → Hot_0^`; the companion's permutation-group and telescope examples; a finite category need not have a homotopy-finite nerve). Prove Lead 3 in a form usable here. Then determine, for each `n ≥ 1`, what the homotopy `n`-category of spaces recovers from finite tests (conservative? faithful? full?), with examples where it fails. State which of his intended applications (associativity of path composition in `Hot`, VII ms. 127 and IX ms. 13; the identity `T² = 1`, VII ms. 150) can be obtained from a test at which level.

**G. Finite categories as presentations of homotopy types.** (i) Which homotopy types are nerves of finite categories; which are nerves of finite monoids. (ii) For `S¹, S², S³` and for the Moore space `M(Z/2, 1)`: the least number of objects and the least number of arrows of a category with that classifying space, among all categories, among posets, among monoids. Prove lower bounds; find the minima by exhaustive search where feasible, with the code. The companion has examples to start from (a four-object `S²`, a six-object `S³`, a three-object, 21-arrow category of type a wedge of 2-spheres, a two-object category whose first non-zero cohomology is in degree 3; XIIapp blocks). This part is exploratory: deliver a table with proofs of what is certain.


---

CONVENTIONS (fix them on your first page and keep them)
- `Cat`: small categories for a fixed universe. `BX = |NX|`. `W∞`: functors whose nerve is a weak homotopy equivalence. `Hot = Cat[W∞^{-1}]`. A *fundamental localizer* is a class `W` of functors satisfying Grothendieck's Loc (1)–(3) of Chapter XVI §1 (weak saturation; a category with a terminal object maps to the point by a map in `W`; the relative Theorem A axiom). State the exact form you use. `X` is `W`-aspherical when `X → e` is in `W`.
- For `u: A → B` and `b` in `B`: `A/b` has objects `(a, u(a) → b)`, `b\A` has objects `(a, b → u(a))`. `u` is *final* (in the usual covariant sense) when every `b\A` is non-empty and connected. Grothendieck's "cofinal", "asphérique", "coasphérique", "propre", "lisse" must be translated with the variance of the page you are reading; the manuscript takes coefficients on `X` to be presheaves (`X^op → D(e)`), and the companion's blocks record the variance at each place. A sieve ("ouvert") is a full subcategory closed under sources of arrows; a cosieve ("fermé") under targets.
- Manuscript locations are given as chapter and manuscript page ("XII ms. 76"). The attached `DER_<id>_text.tex` files mark them with `\msp{page N}`.

WHAT IS ATTACHED
A zip with (1) the LaTeX transcription of the relevant parts of Grothendieck's text (`DER_<id>_text.tex`; AI-made from the edition of Künzer, Malgoire and Maltsiniotis, good but not guaranteed: where a formula looks wrong, say so and reason from the mathematics); (2) for the parts already audited, the companion's files (`_overview.tex`, `_blocks.tex` commentary, `_claims.csv` audit; AI-produced by GPT-6 Astra, ChatGPT Pro mode, in earlier sessions; treat them as a colleague's draft, not as authority); (3) the LaTeX sources or PDFs of the background papers; (4) `FABLE_PILOT_OVERVIEW_20261110.md` and its addendum, where the leads below come from. `MANIFEST` lists every file with its origin.

RULES OF PROOF (they bind every statement you deliver)
1. State the actual claim with all its data: quantifiers, size and universe conditions, variance, which localizer, pointed or unpointed, which numbered axiom in which of its versions. Do not replace it by a convenient special case. If you prove a special case, name it as one and keep the general statement on your list as open.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you use (functor over the base, natural, in `W`, cartesian, compatible with which action). Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "it suffices") comes with its comparison map and a proof that the exact property needed transfers in the direction needed. Passing to a nerve, a localization, a fibre, a truncation, a cofinal subsystem or a homotopy category transfers nothing by itself.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism in `Cat`; equivalence of categories; isomorphism in `Cat hot` (functors modulo zigzags of natural transformations); isomorphism in `Hot`; weak equivalence of a specified map. A bijection on components is not an equivalence. An abstract isomorphism is not the canonical map.
5. Check the edge cases in scope: empty categories, several components, non-surjective maps on `π0`, categories with non-trivial idempotents or endomorphisms, infinite families.
6. A counterexample is given completely (objects, arrows, composition, the verification of every hypothesis and of the failure) and, when finite, checked by a program whose code and output you attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep the two apart.
7. No authority. Grothendieck's assertions, the companion's, and the leads marked "Lead" below (inferences by Claude, Anthropic, made in one reading and not checked by anyone) are all to be proved or refuted. If a lead is wrong, say so plainly and show where.
8. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails, and the smallest undecided instance. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never invent a reference; mark each entry of the bibliography `verified` (you opened it) or `unverified`.

WHAT TO DELIVER
One ZIP containing:
- `<ID>_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics, in the order of the parts below, every statement numbered and labelled Proved / Refuted / Known (with citation) / Open, with complete proofs. English, first person plural, the register of a careful research paper; quote Grothendieck in French where his wording matters. No bullet lists where an argument belongs, no summaries of what you are about to do, no closing recapitulations.
- `<ID>_results.csv`: one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_rows_or_pages_settled, notes`.
- `<ID>_references.bib`.
- `<ID>_report.md`: what you read, what you computed, every correction to the leads, to the companion and to the transcription, and the list of what remains open.
- `code/`: every program you ran, with its output.
The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an interruption loses little.
