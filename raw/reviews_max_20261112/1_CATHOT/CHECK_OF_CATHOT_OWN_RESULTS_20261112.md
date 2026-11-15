# Check of the CATHOT expert's own results (`..\1_CATHOT\OWN_RESULTS.md`, §§1–5)

By Claude Fable 5.2 (Anthropic), effort max, Dérivateurs expert, 12 November 2026 (about 16:40 local; the clock read 16:34 before and 16:43 after).
The results were proved by another Claude Fable 5.2 agent at effort max (the CATHOT expert) on the same day. This
is a second reading by an agent of the same model: it is a check of the arguments, not an independent
confirmation by a different system or by a person. I read §§1–5 in full and re-derived each step named below;
§6 (the census, computational) I did not check, and I ran none of its programs. Sources the proofs quote (Atiyah
1961; Miller 1984; Hatcher 4C.1; Cianci–Ottina; the Kan–Thurston cardinality bound) I did not open: I checked
the deductions from the statements as quoted.

| Result | Verdict | What I re-derived |
|---|---|---|
| 1.1 (a map `BG → X`, `G` finite, `π_1 X` finite, `H^q(X; Z) = 0` for `q > n`, is trivial on `π_1`) | correct, given Atiyah (6.10), (7.2) as quoted | (K1) multiplicativity of the skeletal filtration; (K2): for `x ∈ F^q`, `q > n`, the restriction to `X^{(q)}` comes from a cellular cochain `c` with `δc = 0` (the class extends over `X^{(q+1)}`), `c = δb` since `H^q = 0`, and the image of `δb` in `K⁰(X^{(q)})` is zero by exactness; so `F^{n+1} = ⋂ F^q`; then `v^{n+1}` (`v` = regular flat bundle minus its rank) restricts to zero on every skeleton of `BG`, and the character argument. |
| 1.2 (`p`-local form) | correct, given Atiyah (6.11), (7.2) | the reduction to a cyclic `p`-group `C`; `K̃⁰` of the lens-space skeleta is a finite `p`-group, so tensoring with `Z_(p)` loses nothing; the value `(−d)^{n+1} ≠ 0` at the generator. |
| 2.1–2.5 (finite monoids: finite type ⇔ finite dimension ⇔ bounded homology, each forcing `U(M) = 1`; Swan-type corollary) | correct, given `G6_VERDICT.md` steps 1–3 (read) and 1.1, 1.2 | the passage from bounded homology to bounded cohomology (finitely generated groups); the `p`-local passage; Hatcher 4C.1 for (iii) ⇒ (i). |
| 3.1 (Kan–Thurston with no small quotients) | correct, given the Kan–Thurston theorem with its cardinality bound (quoted there from memory) | the lifting claim (`E → S^m` is acyclic and `E` is connected because the fibre of `t_α` is acyclic); the amalgam `(G_α × A′) *_{H′} A″` and its classifying space; the Mayer–Vietoris comparison with local coefficients (three terms); the "no small quotients" induction, including the case `m = 1`; limit ordinals. **Independent confirmation of the statement:** the return GALOIS (GPT-6 Astra, effort Pro), items B.10–B.11, proves the same theorem by a different construction (simplicial cones over a triangulation, cone groups simple acyclic of cardinality `λ > μ`) that does not use the Kan–Thurston theorem or any cardinality bound from the literature; I checked that proof step by step (`..\4_GALOIS\REVIEW.md`, rows B.10, B.11). |
| 3.2, 3.3 (a `U`-small ind-object of `Cat hot` is `W∞`-invariant iff it is ind-isomorphic to an ind-groupoid) | correct | steps (a), (b), (c) and the final cancellation. **Independent confirmation:** GALOIS B.12 proves the same statement, using only that acyclic maps are epimorphisms of the homotopy category (GALOIS B.9); checked in `..\4_GALOIS\REVIEW.md`, row B.12. So E.17 of CATHOT has two proofs by two different systems, each read by a second agent. |
| 4.1, 4.2 (uncountably many maps to `S²`) | correct | the infinite ordered product in `S³` is finite on each skeleton; for `n = min(A △ A′)` the restriction to `X^{(n)}`; `a_n ∘ (f_n s_n) = ±[a_n]`; injectivity of `[X, S³] → [X, S²]` from `H¹(X; Z) = 0` and the principal `S¹`-bundle. |
| 5.1 (posets of type `RP²` have at least 34 arrows) | correct, given Cianci–Ottina Cor. 5.8 and Th. 5.10 as quoted | the minimal full subcomplex `L` with `H̃_2(L; F_2) ≠ 0`, the links, the degree count `f_1 ≥ f_0 + 6`, `f_0 ≥ 14`. |
| 6.1 (census) | not checked | — |

No error found.
