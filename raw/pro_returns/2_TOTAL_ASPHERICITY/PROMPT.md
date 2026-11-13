# TOTASPH: total asphericity, filtered categories, and Grothendieck's Dwyer-type immersions

Package 2 of 7 on Alexander Grothendieck, *Les Dérivateurs* (1990–91). File prefix for your deliverables: `TOTASPH`.

## What is to be settled

In XII §5 (ms. 88–89, Définition 1) Grothendieck calls a presheaf `H` on a small category `U` *totalement `W`-asphérique* when, for every functor `p: U → U'`, the category of elements `U'/p_!H` of the ordinary left Kan extension is `W`-aspherical; a category `V` is totally `W`-aspherical when its terminal presheaf is, that is, when for every `f: V → V'` the category of elements of `v' ↦ π0(v'\V)` is `W`-aspherical. (The editors note that this is not the total asphericity of *Pursuing Stacks*.) By the comprehensive factorization this says: every target of an ordinary final functor out of `V` is `W`-aspherical (companion, XIIb-a block at ms. 97). The notion first appears in II ms. 36 as a question: is it the same as being filtered?

On it he builds: strictly and totally `W`-aspherical functors (ms. 109, Définition 2), `W`-dwyériennes and totally `W`-dwyériennes open immersions (sieves `U ⊂ X` such that every non-empty crossing presheaf `Hom_X(−, t)|U`, respectively its category of elements `U/t`, is totally `W`-aspherical; ms. 107–113), and a programme of `W`-cofibrations stable under the operations he needs (ms. 111–114). He leaves a string of questions, which the companion's audit could not settle from the literature:

- II-C-003 (II ms. 36): does total `W∞`-asphericity of `A` imply that `A` is filtered? (Filtered implies it. The companion proves the converse for preorders, by showing that it forces common successors; the equalization of parallel arrows is what remains.)
- XIIb-a-B035 (XII ms. 94–97): if a presheaf `H` on `U` is totally `W`-aspherical, is `U/H`? (Proved there for subterminal `H`.)
- XIIba-C005 (ms. 103): if `Y` is `W∞`-aspherical, is the path category `Ch(Y; y0, −)` totally `W∞`-aspherical?
- XIIba-C035 (ms. 111): is an open immersion which is a `W`-cofibration, or even a couniversal `W`-equivalence, necessarily `W`-dwyérienne?
- XIIba-C045, C047 (ms. 113–114): are `W`-dwyériennes immersions, strictly `W`-aspherical functors, totally `W`-aspherical functors stable under composition?
- XIIba-C048 = XIIbb-A001 (ms. 114): find a class of open immersions that are `W`-cofibrations, stable under cobase change and under the endpoint pushout-product with `{0, 2n} → Φ_n` (`n ≥ 2`; `Φ_n` the alternating interval).

The aim is to settle all of them, for `W = W∞` first, then for the homology localizers and for a general fundamental localizer.

## Leads (unverified; prove or refute each)

- **Lead 1 (collage test).** Let `H: A → Set` be a covariant functor and let `A_H` be `A` with one new object `x`, `Hom(x, a) = H(a)`, no arrows into `x` except its identity. The inclusion `A → A_H` is final if and only if the category of elements `El(H)` is non-empty and connected. By the open–closed gluing formula proved in the companion (XIIapp block at ms. 18), `B(A_H)` is the homotopy pushout of `pt ← B El(H) → BA`. Hence: if `A` is totally `W∞`-aspherical, then `El(H)` is acyclic for every `H` with `El(H)` connected.
- **Lead 2.** For parallel arrows `a, b: p → q` and `H = Hom(p, −)/(ca ∼ cb)`, `H_1(El(H); Z) = Z/g`, where `g` generates the subgroup of total weights `Σ n_k` of the families `Σ n_k c_k ∈ Z[Hom(q, r)]` with `Σ n_k (c_k a − c_k b) = 0`. So total asphericity forces an integer combination of total weight 1 of post-compositions to equalize `a` and `b`.
- **Lead 3.** The monoid `M = {1, e, f}` with `xy = y` for `x, y ∈ {e, f}`: `BM` is contractible and cofiltered, not filtered, and the left `M`-set `{h, i}` with `e` and `f` constant at `i` has `B El ≃ S¹`, so `BM` has a final image of type `S²`.
- **Lead 4.** `A` is totally `W∞`-aspherical if and only if `A` is filtered. For the integral homology localizer `W_Z`, `A` is totally `W_Z`-aspherical if and only if `colim_A` is exact on abelian-group-valued functors (the condition studied by Isbell and Mitchell).
- **Lead 5.** A presheaf `H` on `U` is totally `W∞`-aspherical if and only if `U/H` is filtered, that is, `H` is a filtered colimit of representables; an open immersion `U ⊂ X` is `W∞`-dwyérienne if and only if the inclusion of `U` into the cosieve-closure it generates has an ind-right adjoint. Classical Dwyer maps are the case of a right adjoint.

## After CATHOT (added 11 November 2026)

Package CATHOT of this series has been answered (GPT-6 Astra, ChatGPT Pro mode); the parts of its answer named below are attached. Its statements are cited by their numbers. Those marked *checked* were followed step by step by the author of this prompt; the others are that answer's own claims and are to be treated like the leads: verify before use.

- **Finite monoids as test cases.** CATHOT G.9 and G.10 give monoids with 5 and 7 elements whose classifying spaces are `S²` and `S³` (the first is a 2-by-2 rectangular band with an identity adjoined; homology recomputed independently through degree 4). G.4 and G.5 state that a finite monoid with finite-dimensional classifying space has trivial universal group and that the finite CW types realized by finite monoids are exactly the simply connected ones (not checked). For the monoid case of Part C this gives the first sieve: a totally `W∞`-aspherical monoid has contractible classifying space, and the bands (left-zero, right-zero, rectangular, each with an identity) are the smallest family in which filtered, cofiltered, contractible and non-contractible all occur. Classify total asphericity on that family first; Lead 3 is its smallest non-filtered contractible member.
- **The infinite fence** (CATHOT C.5, *checked*): a poset with contractible nerve in which the identity functor is not joined to a constant one by any finite zigzag of natural transformations. It is not filtered, so by the companion's theorem for preorders it is not totally aspherical; use it to test any argument in Parts B and C that passes from finite to infinite categories.
- **Nothing in this prompt is settled by CATHOT.** Leads 1 to 5 stand as they were.

### After the second review of CATHOT (added 11 November 2026)

A second, independent reader (a separate Claude agent) has checked the CATHOT answer; its review is attached (`REVIEW.md`). Statements it followed step by step are called *confirmed* below.

- In "Finite monoids as test cases": G.4 (a finite monoid whose classifying space is finite-dimensional has trivial universal group) is *confirmed*, given Miller's theorem on maps from classifying spaces of finite groups. G.5 (finite simply connected complexes are realized by finite monoids) is a citation of one unrefereed preprint (O. Ben-Bassat, arXiv:2610.38760) and remains unchecked: do not build on it. The minima for spheres were confirmed by an enumeration of all labelled monoids of order at most 6.
- A caution for Parts B and C: finite categories are not compact objects of `Hot`, and an isomorphism of ind-objects of categories modulo natural transformations implies nothing about weak equivalence of the colimits (CATHOT E.4, *confirmed*). Any argument for filtered or sequential families must work with the actual transition functors.

## Parts

**A. Definitions and the formal theory.** State Définitions 1 and 2 and the Dwyer-type notions exactly, with their variance; prove the reformulation through the comprehensive factorization (Street–Walters), closure under final images, and the known implications (filtered ⇒ totally aspherical for every fundamental localizer satisfying which axioms? the companion uses Cisinski's theorem that filtered categories are aspherical for every fundamental localizer; give the exact statement). Record which of his propositions 7–9 (ms. 84–100) survive, using the companion's audit and correcting it where needed.

**B. Lead 1–3**, with complete proofs; the homotopy type of `A_H` in general (when `BA` is not assumed contractible); the iteration (total asphericity passes to final images, so `A_H` is again totally aspherical: extract every further necessary condition this gives); other families of final functors out of `A` (quotients by congruences, localizations, idempotent completion) and what each forces.

**C. The main theorem.** Prove or refute Lead 4 for `W∞`: total `W∞`-asphericity ⇔ filtered. If you refute it, give a non-filtered totally aspherical category with the complete verification, and then characterize the totally aspherical categories. If the general case resists, settle it completely for monoids (one-object categories) and for categories with finitely many arrows, and state exactly what remains.

**D. Other localizers.** The `W_Z` half of Lead 4 (both implications, with the precise form of the Isbell–Mitchell condition), then `W_R`, the `n`-equivalences `W_n` (for `W_0` the notion is elementary: say what it is), and a general statement for fundamental localizers, as far as it can be proved. The companion shows that total `W∞`-asphericity is not invariant under weak equivalence (XIIb-b block at ms. 120); place that example.

**E. Presheaves.** Row B035 and Lead 5: total asphericity of `H` against that of `U/H`, in both directions, for `W∞` and in general.

**F. Dwyer-type immersions.** With C–E in hand: characterize `W∞`-dwyériennes and totally `W∞`-dwyériennes open immersions; settle C035 (compare with `h`-cofibrations in the sense of Batanin–Berger and with the discretely flat cofibrations of Hackney–Ozornova–Riehl–Rovelli: exact inclusions between the classes, with separating examples), C045 and C047 (composition), and C048 (exhibit a class with the required stability, or prove that none of the natural candidates has it and say what does). Re-examine his Théorème 3 and Corollaire (ms. 107–112) and the interval-product calculation (ms. 114–115).

**G. Row C005.** For a `W∞`-aspherical `Y`, decide whether `Ch(Y; y0, −)` (the category of paths with fixed origin, XII ms. 101–103, VII §§5–7) is totally `W∞`-aspherical; under C this asks whether it is filtered.

**H. Statement of results** against the rows listed above: for each, settled (how) or open (exactly what).


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
