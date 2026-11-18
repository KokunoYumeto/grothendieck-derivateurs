# Part G work log

2026-11-17: Read REVLOC F12.tex in full, R20 expert note, Chapter XVI axioms Loc (1)-(3 bis), XV propositions 9.11-9.13 and 10.1.

Early findings: Wtilde (REVLOC W-dagger) satisfies literal XVI Loc (1), since its four tests are isomorphism tests after applying functors (fundamental groupoid up to equivalence). Its product stability is false: degree-two map S^2 -> S^2 lies in Wtilde, but its product with S^1 induces multiplication by two on H3. Use face posets of suspended C8 -> suspended C4 and C4; gives finite explicit 400 -> 208 object functor.

Wtilde preserves components, so all six conditions of Proposition 9.12 hold; Corollary 9.13 is vacuous. Arbitrary disjoint unions detected componentwise, so all three conditions of 9.11 hold. Thus those propositions cannot be refuted by Wtilde even though products fail. Need decide general weak-localizer version, and bare existence of u_! separate from its standard formula.

Infinite-product localization source search found Mathlib Localization/FiniteProducts and candidate paper Gabriel--Zisman Localizations, Products, Coproducts, and Product Categories; opening primary texts next.

## Completed checkpoint, 17 November 2026

`sections/G.tex` now contains fourteen fully stated and labelled claims G.1--G.14 and complete arguments for every prompt Part G item. `notes/G_results.csv` has one row per claim and `notes/G_references.bib` has the exact opened/not-obtained status. Bibliography keys have prefix G to avoid collisions during parent integration.

Key additional results:

- Wsharp (G.4) classifies components by vanishing/nonvanishing H1, uses weak equivalences on zero-H1 components, and direct-sum H1 isomorphisms over each positive target component. It satisfies literal Loc (1)--(4), including the gf/fg rule, but merges two circle components to their wedge. Global H1 survives localization, so it has infinitely many homotopy isomorphism classes and nonconstant comparisons on actual hom sets. This refutes each of XV 9.11, 9.12, 9.13 separately (G.5).
- The exact unconditional implication chain and both c/c-prime implications are proved in G.6. R20's direction reading is confirmed; the edition's affirmative-direction remark is reversed. The target of h=(f0,f1) at XV 133 quinquies is Y.
- Arrow-retract closure restores all three propositions (G.7), by a whisker construction reducing any component failure to the two-point collapse and absolute Theorem A. Loc (8) implies arrow-retract closure via the constant idempotent sequence. This explains why Wtilde passes 9.11--9.13 despite failing products.
- Bare nonexistence of the span's left Kan adjoint is proved in G.8. The degree-two and degree-one sphere maps give an automorphism a of the localized diagram and a suspension endomorphism b of degree two on integral H3. An adjoint would represent a natural cocone by beta with beta L(a)=b beta, forcing im H3(beta)=2 im H3(beta) in Z, hence zero. The explicitly defined rational mapping-cone invariant makes the same cocone an isomorphism on Q, a contradiction. This does not merely refute the usual formula.
- F.1.1 is checked in G.9 via the exact Cisinski axiom chain. Last-vertex squares identify the resulting fundamental localizer without conflating the ordinary nerve with the right adjoint to the simplex-category functor. No accessibility is inserted.
- G.10 gives the corrected products and left Kan theorem under the relative axiom, including the actual Maltsiniotis cross-adjunction and all variance. Weak axioms suffice for the diagram/slice equivalence; relative Theorem A is precisely what is needed for composition over bases.
- The infinite-product lemma is false (G.12). The free countable product completion of 0→1←2→3←... with W the bijective coordinate maps has countable-product-closed W, but no localized map from (0) to the unbounded tuple (n). Each singleton (n) is nevertheless isomorphic to (0). The finite, fraction-calculus, and model-category versions are proved in G.11, G.13, G.14.

Programs run successfully:

- G_finite_witnesses.py: sphere posets 50/26 objects, relative witness 77/53, product witness 400/208, suspension posets 52/28, Wsharp witness 12/11. All arrow orders, maps, adjunctions, integer degree and homology matrices checked; all assertions passed.
- G_zigzag_bound.py: finite labels through 30, exact minimum zigzag distances, 29,660 finite tuple maps; forward/inverse bounded-label estimates checked. All assertions passed. Infinite conclusion comes from the written uniform proof.

No claim of priority. The Zhang 2026 primary abstract was retrieved but full text remained inaccessible; no theorem-level content from it was used. Parent has been informed that G is ready for integration and independent review of G.4 and G.8. Child next assists parent on B4 interval contractibility / D1⇒D, keeping G complete.

## Integration and independent Part B audit

The bounded-interval proof has been completed in `notes/B_interval_moment_proof.tex` and incorporated by the parent as `sections/B_interval_proof.tex`. The moment-body realization gives actual closed balls, and the relative simplex-category comparison is proved by Reedy cofibrancy with explicit locally finite triangulations of simplex complements. Hirschhorn's exact fibrant-constants and homotopy-colimit comparison statements were opened and recorded separately in `notes/B_interval_sources.md` and `notes/B_interval_references.bib`.

Parent's B.3 strictification was independently checked: `q:H(r)→F(r)` is left adjoint to the fibre section; the other map's composite with that section is the actual local unit. Both diagram maps are strictly natural. Parent's B.4 classification on countable colored orders was independently checked, including noninjective sequential transitions, finite factorization, the initial image object in the finite-subset finality comma, and the ordered-sum contraction of `L↓Ω`. The universal homotopy-colimit cocone left Kan extends to a natural comparison from `BF^ω` to the constant global homotopy colimit, which identifies the exact roofs used in condition D. No mathematical corrections were needed. Parent's marked-pair D1-not-D counterexample and both amalgam contractions were independently checked.

## LuaLaTeX layout check

The system TeX tree had no generated LuaLaTeX format, font maps, luaotfload, lualibs loader, or Unicode-algorithm Lua modules. `code/G_setup_tex.py` constructs a workspace-local format and local font map, installs the four archived CTAN downloads with SHA-256 verification, and writes `build/tex_runtime/environment.json`. All original source/package licenses are retained in the local tree or download archives. No system files or security settings were changed. A workspace-relative `TEXMFCACHE` is needed because LuaTeX correctly rejects absolute cache writes in its normal restricted mode. Builds run with cwd `DER_FOLLOWUP_work`.

`code/G_build_check.py` successfully compiled G with the original fontspec/Latin Modern preamble through LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX. One unbreakable module path previously overflowed by 50.8849 pt; explicit allowed breaks fixed it. The final log has zero overfull boxes and no warnings or errors, as recorded in `code/outputs/G_build_check.json`. The standalone PDF is an internal QA artifact, not an additional deliverable. `code/G_build_paper_check.py` now runs a temporary full-paper build, merging the current available bibliography fragments and keeping all logs without altering the master or other mathematical sources.

The full intermediate paper build then succeeded through all four passes, with sections A, A_general_kan, A_Kstar, B, B_interval_proof, C, D, E, and G. The only source-level build fixes were loading `mathrsfs` for A's existing script-letter notation and loading `xurl` so the long Fiedorowicz reference URL can wrap. The workspace font map was extended to the installed RSFS Type 1 fonts. The final integrated log has zero overfull boxes. At that checkpoint the only warnings were four bibliography keys still being assembled by the parent: BCegarraHeredia2015, BAraMaltsiniotis2014, StacksDK, Kervaire1969. `code/outputs/G_paper_build_check.json` and `build/paper_check/run_*.txt` contain the result. Both build-check scripts now archive previous logs before a subsequent run. `code/G_tex_run.py` runs an arbitrary supplied TeX command with the same runtime and cwd for the parent's final deliverable build.
