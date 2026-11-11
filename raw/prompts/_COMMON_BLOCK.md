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
