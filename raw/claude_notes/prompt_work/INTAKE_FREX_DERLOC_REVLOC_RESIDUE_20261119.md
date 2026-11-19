# Intake of FREX (final), DER_LOCALIZERS (checkpoint 08), REVLOC (checkpoint 17, the rest) and RESIDUE (the rest)

Claude Opus 5.5 at effort max, a sub-agent of the main session, 19 Nov 2026 (started about 00:55 UTC; files written
from 01:10 UTC, clock read). Brief: the main session's message of 19 Nov (the user, ~00:4x UTC: [the user's words, omitted], [the user's words, omitted]). Sub-agents: none. No git, no paid API.
All four returns are GPT-6 Astra (ChatGPT Pro mode), unrefereed outside this project. "I" below is this intake.

Files written with this one, in the same folder:
- `ROWS_20261119.tsv`: all 484 register rows (FREX 147, DER_LOCALIZERS 100, REVLOC 152, RESIDUE 85), each with its
  claim, the run's status, where its proof is, new/known/ours, my check and the outcome.
- `CHECK_EVENTS_20261119.tsv`: 49 check events of this intake (41 targeted proof checks, 4 computations by my own
  programs, 4 independent re-proofs).
- `PROMPT_UPDATES_20261119.md`: the paragraph for the unsent FINMON_CP2 and items for successor prompts.
- `INTAKE_20261119_checks/`: my programs and their outputs (frex_a10_weights, frex_a18_parity, derloc_a8_perm,
  revloc_i8b_unit, the proof-location check, and the two generators of the TSV files).

## 0. Scope: what I read and what I did not

**Read for every row of the four registers:** the register row in full (statement, status, where proved,
dependencies, notes). For every row, a program of mine checked that the file named in "where proved" exists (all 484)
and located the statement in it. The 463 rows that are not Open records have their proof at the place named: 454 in a
proof environment, 9 inside the statement or assembled from the rows they name (FREX B.5, C.14, E.2, E.3; REVLOC C.6,
D.1.5, G.4; RESIDUE H.7, H.8). The 20 Open records (5 DER_LOCALIZERS, 2 REVLOC, 13 RESIDUE) and DER_LOCALIZERS's
record `C.general_M` (settled by C.26) have none. This check says the proof is **present**; it does not say it is
complete. Completeness is claimed only where the ROWS file says I read the proof.

**Also read:** the four prompts as sent (FREX: sections "Results", "Leads", "Outcome", "Parts" in full; DER_LOCALIZERS:
"Leads", "Outcome", "Parts", R3–R5; REVLOC: headings; RESIDUE: "What is to be settled", "Leads", "Parts"); the reports
in full for FREX and DER_LOCALIZERS, the first 98 lines (status table and audits) of the REVLOC report (1,321
lines), the first 40 lines of the RESIDUE report; the earlier intakes and notes of the field (`INTAKE_DER_FOLLOWUP_FINMON_20261117.md`,
`INTAKE_S2COUNT_REVLOC_20261117.md`, the expert's `KNOWLEDGE_HANDOFF.md`, `REVIEW_MAIN_PROOFS_TOTEX2.md`,
`NEW_PROMPT_ITEMS_20261117.md`, the RESIDUE passages of `pro_reviews_20261110/KNOWLEDGE_HANDOFF.md` and its
`8_RESIDUE/checks_author/` outputs); the ledger rows of the four runs; the unsent `07_FINMON_CP2/PROMPT.md` (lines
1–262).

**Proofs read, by run** (the depth of each is in the ROWS file and in CHECK_EVENTS):
- FREX: A.9, A.10, A.11, A.17, A.18, A.19, A.23, A.24 (once), A.25, A.26, A.31 (encoding step), A.32, A.33, C.10–C.13,
  D.3–D.6, G.12. A.12 re-proved by hand in its ring criterion.
- DER_LOCALIZERS: A.1–A.8 (sections/A.tex lines 1–186), A2.4, A5.1–A5.4 (all of A5.tex), B.3, B.4, D.1.
- REVLOC: none in full (F.1 had been followed by hand by the DF intake of 17 Nov; I did not redo it). One computation
  for I.8b.
- RESIDUE: B.2, B.3, B.4 (with an independent re-derivation of B.3); B.8 and D.8 re-proved by hand, proofs not read.

**Not read:** every other proof (about 420 rows are at statement level in the ROWS file); the sections D2_*.tex,
D3_*.tex of REVLOC (the D.2.11–D.2.61 computation); DER_LOCALIZERS C.tex (161 KB, the linear case) and A2_review.tex
apart from A2.4; the A34/A4 reviews; FREX G.tex apart from G.12 (209 KB); the notes, codes and bibliographies of all
four (except the RESIDUE author checks of 11 Nov); no return's program was run; no cited source was opened (each
citation is marked "to verify" where I was not sure of it); no PDF check of the four papers. The REVLOC report beyond
line 98 and the RESIDUE report beyond line 40 were not read.

## 1. The findings, most important first

| # | Finding | Rows | My check |
|---|---|---|---|
| 1 | **Exactness and amenability are independent in setting (S), both ways, under all the structural hypotheses.** Finite posets with an independent linear order: exact over every ring, total, all of (Rig), (SA), (FA), (FA∅), (St), (Op), and `Aut(M)` **not amenable**. Finite F₂-vector spaces with an independent order: total, all hypotheses including (WEI), (Fin), `Aut(M)` **amenable**, exact over Q, **not exact over F₂ or Z**. | FREX A.10, A.11, A.17, A.18, A.19, A.33 | targeted checks of every step of A.9–A.11, A.17, A.18, A.33; two programs of mine |
| 2 | **Exact over every F_p does not give exact over Q:** `A_r(Q)` (rational `r`-cocycle classes, `r ≥ 2`) is exact over every prime field, not over Q; field profile of every `A_r(Λ)`. The total-index version is open. | FREX C.10–C.13 | targeted checks |
| 3 | **The predimension family `C(k, a, b)` is classified:** total for all parameters; exact (over any non-zero ring), amenable and extremely amenable all hold exactly when `b ≥ (k−1)a`. | FREX D.1–D.9 | D.3, D.4, D.6 checked step by step; D.5 key steps |
| 4 | **Totality of the category of a Fraïssé class depends only on the topological group** `Aut(M)` (setting (S), no extra hypothesis); exactness already did (A.1). | FREX A.24–A.26, G.12 | A.25, A.26, G.12 step by step; A.24 once |
| 5 | **XVI Corollaire 7.7.2 is settled in all its hypotheses.** Loc (8) is needed for Loc (3 bis): a weak localizer `W_fin` with Loc (1)–(3), (6′ a), (1 ter), (9) fails relative Theorem A over the discrete category N (finite certificate: categories with 2 and 58 objects). Strong saturation needs neither Loc (8) nor (9). With REVLOC F.1 (no (6′ a)) and DF G.9 ((6′ a) + (8) suffice): Loc (6′ a) and Loc (8) are each necessary, Loc (9) is irrelevant. Footnote 56 is wrong for the hypotheses as printed and right once (8) is removed. This answers the expert's hunch 5. | DER_LOCALIZERS A5.1–A5.4 | A5.2, A5.3 step by step; A5.1 at its collage step |
| 6 | **Reverse excision at localizer level is reversibility, at derivator level it is homology.** W7 bis, W8 bis, XII W(7 bis), W(7) and XVI Loc (6 a, b, c) are equivalent for fundamental localizers (A.3), so the expert's `W_S` (accessible version: REVLOC B) answers the main question A.1 no. The final Der 6 of 105/052, or either unrestricted half of the provisional one, forces an `RT`-fixed localizer (A2.4, A2.9). | DER_LOCALIZERS A.1–A.9, A2.1–A2.14 | A.1–A.8 and A2.4 at key steps; A.8 by program |
| 7 | **RESIDUE (11 Nov) had refuted "absolute ⇒ relative Theorem A" first,** with a strongly saturated class `W_circ` (circles with non-zero degree added to `W_∞`), a 10-object/6-object poset certificate, and the failure of products (B.8) and of XV 9.9–9.13 (B.16, B.17) under the literal axioms: a week before REVLOC F.1 and DER_FOLLOWUP Part G, which do not cite it. POLES A.16 was closed on 11 Nov. | RESIDUE B.2–B.4, B.8, B.16, B.17 | B.2–B.4 step by step, B.3 re-derived; B.8 re-proved |
| 8 | **Intervals do not generate the trivial cofibrations for integral homology** (105/020), even with every acyclic interval: an explicit 17-vertex graph map, detected by maps to `K(S₃, 1)`; on simplicial sets the intervals give exactly the aspherical core, equality iff the localizer is proper. | DER_LOCALIZERS B.3, B.4, B.10 | B.3, B.4 step by step |
| 9 | **Local systems:** the naive finite-dimensional cohomology class fails two-out-of-three over every field; the repaired class (equivalence of perfect local systems) is a fundamental localizer whose equivalences are Toën's schematization equivalences. The expert's Lead 2 was false as stated. | DER_LOCALIZERS D.1–D.10 | D.1 step by step |
| 10 | The open gates, sharper: FREX A.3(iii) (amenable + (Rig), (FA), (FA∅), (Op) ⇒ exact over Q?) needs a non-metrizable universal minimal flow and a distortion (A.23, A.30); DER_LOCALIZERS A.3 reduces to one prime and one infinite-loop generator (A34.5, A34.6); A.4 to ordinary `BC₂`-acyclicity of countable sphere-null H-spaces (A4.5, A4.6); the linear "Thm(?)" is false in general (C.26), its corollary case open; free monoids over `C_δ` reduce to one transgression kernel (G.33). | FREX A.23, A.30, G.18, G.33; DER_LOCALIZERS A34.5–A34.6, A4.5–A4.8, C.26 | statement level |

## 2. FREX (prompt 04_FRAISSE_EXACT; final of 18 Nov 12:35 UTC; INCOMPLETE by the two-review stopping rule)

147 rows: 126 Proved, 13 Refuted, 8 Known. The register has no Open row; the open items are in the report's table
(A.3, C.4, F.1, G.1, G.2 INCOMPLETE). The state of the main question A.3: (i) refuted, (ii) refuted, **(iii) open**,
(iv) refuted, (v) both clauses refuted, (vi) first half proved, second half refuted, (vii) refuted, (viii) refuted.

**A.9–A.11 (exact over every ring, not amenable): sound, every step followed.**
- A.9 (signed averaging): if `H ≤ G` is co-precompact with exact smooth `k[H]`-coinvariants and `X = (G/H)^` carries a
  `G`-invariant finitely additive `μ: Clop(X) → k` with `μ(X) = 1`, then `N_G` is a natural retract of `N_H`
  (`s_N(n) = ∫ [g⁻¹n]_H dμ`), so `G`-coinvariants are exact. Positivity is not needed. Converse over a field.
- A.10 (weights on linear extensions): `w_P(π) = Σ_𝓑 (−1)^{n+|𝓑|}` over the consecutive antichain block partitions
  increasing in the reference order. I re-derived the restriction identity from the cell description: over a cell of
  `Q = P ∖ {x}` with `b` blocks and `m` heights inside the admissible interval of `t_x`, the `m+1` open and `m`
  equality cells contribute `(−1)^{b+1}`. My program checks normalization and all 6,143 restriction equations on all
  labelled posets with at most 4 points.
- A.11: `H` = automorphisms of the generic expansion by a linear extension (Ramsey: Bodirsky 2014, Cor. 1.4(3), not
  opened), co-precompact (double cosets ↔ linear extensions of a finite set, by homogeneity); A.10 gives an
  integer-valued invariant `μ`; A.9 gives exactness over every ring. Non-amenability: an invariant probability has
  `p(x ◁ y) = 1/2` for incomparable `x < y` (the two three-point configurations give `2p − 1 ≥ 0` and `1 − 2p ≥ 0`),
  then `λ(a ◁ c ◁ b) = 0` for `a ≺ b`, `c` incomparable, and a three-point antichain would have no middle element.
  So exactness (signed integer averages) and amenability (positive averages) separate. For the companion: this is the
  cleanest statement of the difference between (CT) and (CC).

**A.17–A.19, A.33 (amenable, total, Q-exact, not F₂-exact): sound in all steps read.**
- A.18: the five embeddings `F₂²∖0 → F₂³∖0` with images `(1,2,3), (1,6,7), (2,5,7), (3,4,7), (3,6,5)` (reference order
  `1<2<3<4<6<5<7`) have no affine equalizer over F₂ at any target. The proof uses an auxiliary binary order at the
  target, the identities `1_{x≺y} = ε_{x+y}(y)` and `1_{u+v between u,v} = ε_u(v) + ε_v(u)`, linearity of `ε` and the
  sums `1+2 = 5+6 = 3`, `1+6 = 2+5 = 7`, `3+7 = 4`. I followed every identity; my program checks both identities on
  all injective linear maps into F₂³ and F₂⁴ (165,312 cases).
- A.17 (amenability by random colourings): I checked the counts `e_r(n)`, the conditional expectation
  `H_i(u) = N m^{−(q−p)} ν_i(χ∘u)`, the variance bound `N²η_n` from extensions meeting outside `uP`, and the choice of
  `n`. Sound.
- A.33 (Q-exact): through the Ramsey category with a distinguished ordered basis (A.31; its Ramsey input,
  Hubička–Nešetřil 2019 Thm 4.46, not opened), the simplex-code embedding `Q → F₂^{Q^∨∖0}` and uniform orders; the
  marked basis closures of all `j a_i` have the same distribution (each functional on `P` occurs `2^{q−p}` times;
  `U_i ∩ j(Q) = j a_i(P)` by duality). The denominators are powers of 2, which is why the argument works over Q only.
- Not checked: A.16 (the structural hypotheses (S), (St), (Op), (WEI), (Fin) and totality of this class).

**C.10–C.13 (the cocycle field profile): sound.** The perfect group algebra lemma (Frobenius-stable ideals of
`F_p[V]`, `V` uniquely p-divisible, are radical; the lattice they generate is distributive, so pairwise compatible
marginals lift); coherent `F_p`-weights on the rational primitives of every finite cocycle object (two-subset
extension: `H^{r−1}` of two simplices vanishes for `r ≥ 2`); averaging through the Ramsey cochain expansion gives an
`F_p`-affine equalizer of every family; the two blocks `{0,…,r}` (cocycle value 1) and `{r+1,…,2r+1}` (value 0) give
`2(r+1)` face embeddings with no rational affine equalizer (alternating sums of a primitive give `aug t = 1` and `0`).
So `A_r(Λ)` is exact over F_p iff `p` is bijective on Λ, over Q iff Λ is torsion, over Z iff Λ = 0.

**D.1–D.9 (predimensions): sound where checked.** The atom lemma D.3 (four constructions: cycles for `k = 2`,
`a/2 ≤ b < a`; random edge sets for `k ≥ 3, b ≤ a` and for `k = 2, b < a/2`; core-and-petals for `b > a`; I checked each
bound and that they cover `b < (k−1)a`); D.4 (two strong copies of the atom meet in at most one vertex, so a private
vertex exists and the singleton family has no affine equalizer over any non-zero ring); D.6 (Hall assignments of edges
to vertices with capacity `⌈a/b⌉`, infinite `G_x`-orbits); D.5 (`b ≥ (k−1)a`: forests, strong sets are unions of
components, then a free amalgamation class with set-valued functions; the Ramsey theorem EHN 2021 Thm 1.3 not
opened). This replaces Lead 8 (b), (c), (e): the candidates `C(2,2,1)`, `C(3,3,1)` for "exact and not amenable" are
not exact (D.9); Lead 8(e)'s five-edge equalizer is right but equalizes only the initial triple (D.10).

**A.24–A.26 with G.12 (totality is a group invariant): sound.** A.25 (a full objectwise-cofinal subcategory of a
category with condition I is total iff the category is) uses G.12, which I checked: over a total index the derived
colimits of `N` and `N/K` (`K` = elements killed by some arrow) agree, by the free resolution by set actions and
synchronised kill-witnesses. A.26 passes through the canonical relational presentation, A.24 (followed once) and A.25.

**The rest of FREX (statement level).** Part B proves Lead 7 in setting (S) with three corrections (B.8: `E_U ≃
B(U/G_F)` needs `F ≠ ∅`; B.14: "(Rig) + (St) ⇒ (Op)" needs the intersection condition (Int); B.10: the orbit-category
dictionary of Lead 12 holds with the opposite variance to the standard Bredon convention); B.3 confirms the expert's
expectations (convex equivalence: total, Ramsey, (Op) fails; independent equivalence: `RP^∞` and every `BS_m`
occur); B.4 settles the R10 category ((St), (Op); quasi-filtered and not total, a fourth witness for
`total ⊊ quasi-filtered`). Part C proves R11 and Lead 3 (exactness = (CT)), Lead 10 (a)–(d), Lead 11, the exit-path
category (C.19–C.21: `BX ≃ S²`, `lim²` of constant `R/Z` is `R/Z`), and excludes eight families of constructions for
a total counterexample to "all F_p ⇒ Q" (C.22–C.31). Part E proves Lead 9 with corrections (E.1: the obstruction is
`ker(lim¹K → lim¹X)`; E.5: uncountable directed surjective systems can fail). Part G: the gap diagram of DF's Lead 3
passes (G.5; `M_ab = Z[raw points] ⊕ Z`, as the expert computed by hand, with raw points, not `A(V, −)`); bounded
rank, rank one, idempotent-free colimits and lexicographic embedding-gap diagrams pass; the class `𝓕` is a
group invariant (G.18); the remaining `H₂` question is the kernel of the transgression `H₂(Y) → A_cut` (G.33), and
G.34 shows neither shortcut works.

## 3. DER_LOCALIZERS (prompt 06_DER_LOCALIZERS; checkpoint 08 of 18 Nov 09:54 UTC, treated as final; INCOMPLETE)

100 rows: 55 Proved, 15 Proved under stated hypotheses, 19 Refuted, 6 Known, 5 Open (A3.decision, A4.equality,
A4.interval, A4.size, C.raw_gate) and the settled record C.general_M.

**A.1–A.9: sound at the steps read.** A.1, A.2 (the span/sieve comparison with the canonical adjunction `α ⊣ q`; the
cofiber criterion without accessibility); A.3 (the four forms of the reverse axioms are equivalent; W8 bis (a) must
read `f`, since with `f_a` the axiom would fail already for the span morphism `(e ← {0,1} → e) → (e ← e → e)`); A.4
(`W_Z` is the least reversible localizer); A.5 (`W_S`: EHP desuspension, Miller's Theorem C for `RP^∞`,
`[RP², S²_(2)]_* = Z/2`); A.6 (`loc(Σ^∞RP^∞) = loc(S/2)`, so `P → e ∈ RT(W_S) ∖ W_S` for the 7-object `RP²`
category); A.7 (the countable-enlargement class; accessible); A.8 (the 37-object `A ⋆ {t, s}` for the presentation
`⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩`; my program checks the `A₅` quotient and the unimodular relation matrix). A.5–A.9 recheck
results of ours (the expert's `W_S` of 12 Nov; REVLOC A–B, D.2.2; TOTASPH A.13); the new content is A.1–A.3.

**A2: the derivator level.** A2.4 (followed at its key steps): for a strong derivator with the final Der 6, the derived
pointing `D_*` is stable; free pointing `M ↦ (1 → 1 ⊔ M)` is conservative because the square `M → 1⊔M`, `N → 1⊔N` is a
pushout and hence a pullback; `Z` is a retract of `FUZ`; the spectral action (Cisinski–Tabuada A.11, not opened) gives
`W_D = R(L)`. A2.9, A2.10–A2.14 (statement level): either unrestricted half suffices; constant, locally constant and
arbitrary coefficients agree for pointed derivators; constant does not give locally constant for unpointed ones
(A2.12, an accessible counterexample whose localizer is still `W_Z`); for ∞-categorical derivators either constant
half already forces `RT`-fixedness (A2.14). Open beyond the return: the same for bare derivators. A2.8: the
replacement conjecture in Grothendieck's margin at 105/052 is false (two Higman complexes).

**A5: sound** (section 1, finding 5). The class `W_fin` (Π₁-equivalence, integral homology isomorphism, finitely many
bad components) and the functor `j: Q → P` (two poles with two parallel arrows into the double collage of the degree
one and degree two maps `S_6 → S_3` of suspended polygons): `BP` is the mapping torus of a degree-two self-map of `S²`,
`H₂` of the relative universal cover is `Z[t^{±1}]/(2t − 1) ≅ Z[1/2]`, so `j ∈ W_fin` is not a weak equivalence, and
`⊔_N j` over the discrete category `N` has infinitely many bad components.

**A3, A4 (the two rows REVLOC left open): statement level.** A34.5: every reversible localizer is the join of its
rational and p-primary parts, and is `RT`-fixed iff each p-part is. A34.6: the existence question A.3 is equivalent to
one accessible reversible closure of `A = QΣ³V` with a non-contractible primary `A`-null H-space separator in the
ideal of `Σ^∞A`; such a witness cannot have finitely generated unstable cohomology (for `m ≥ 2` loop structures).
A4.5–A4.8: the A.4 equality is equivalent to `P_{BC₂}H ≃ *` for every countable simply connected primary sphere-null
H-space; finite Steenrod generation is excluded; generators may be replaced by `Ω^mΣ^mX`. A34.4: `K(C_{p^∞}, 2)` and
`K(F_p, 2)` generate different stable ideals.

**B: B.3, B.4 sound.** B.4: for the integral homology localizer on simplicial sets, `N(S₃) → Δ⁰` has the lifting
property against every acyclic interval generator (acyclic means perfect `π₁`, and perfect to solvable is trivial),
while the mapping-cylinder inclusion of the graph map `a ↦ a, b ↦ b[a, b]` is a homology-equivalent monomorphism
without the extension property for `((23), (12))`. B.10 (statement level) gives the exact answer on simplicial sets.

**C (the linear case): statement level only.** C.1–C.4 prove the manuscript's lemmas with corrections (C.5: Lemme 3
needs the canonical normalization); C.26 refutes the unrestricted theorem by a three-sort square-zero construction
(`L₃φκ(W) = W**/W ≠ 0`); the corollary case with finitely presented projective generators keeps one open gate
(C.raw_gate), with eight sufficient conditions (C.7, C.11, C.14, C.16, C.17, C.19, C.21, C.22, C.27, C.29).

**D: D.1 sound** (`BC_ℓ → e` passes by averaging, `e → BC_ℓ` fails on the regular representation). D.2–D.10 at
statement level: the repaired class is a fundamental localizer (D.3), equal to the schematization equivalences
(D.4, from Toën, not opened), strictly between `W^lc` and `W_k` with explicit examples (D.6), and fails every reverse
axiom (D.7). D.10: cote 133/006–008 and *Pursuing Stacks* §110 do not state the local-system conjecture.

## 4. REVLOC (checkpoint 17 of 16 Nov 02:57 UTC; the 141 rows no intake had named)

152 rows: 136 Proved, 12 Refuted, 2 refuted as worded, 2 Open (D.2.4, D.3.2). The earlier intake read the titles; the
register gives titles and notes, which I read for every row. No proof was read here. What the other returns did with
these rows:
- A.1–A.7, B.1–B.4 (the accessible reversible non-`RT`-fixed localizer, small reversible closures accessible): rechecked
  by DER_LOCALIZERS A.5–A.7 (the same model, a second run); D.2.2 audited by DER_LOCALIZERS A.9; G.6–G.7 (the full
  sphere-null localizer is accessible in ZFC, which settles the point the expert's note of 12 Nov left open) rechecked
  in DER_LOCALIZERS A4.2; D.2.6, D.3.3, D.3.8 used there.
- D.2.4 and D.3.2 became DER_LOCALIZERS A.3 and A.4. The D.2.11–D.2.61 computation (a fourth-stage Hopf extension
  through the fifteen-skeleton, ending with D.2.61: the last Moore obstruction vanishes) is superseded as a route: DER_LOCALIZERS
  A34.3 excludes `BC_p ∧ K(F_p, 2)` (with REVLOC D.2.37, D.2.39), and A34.6 states the exact single test.
- C.7's acyclic 35-object/159-arrow category is the `A` of DER_LOCALIZERS A.8 (the binary icosahedral presentation).
- I.8b: my program confirms that `2 − t − 3t² − t³ + 2t⁴` is a unit of `Z[C₅]` of infinite order in `Wh(C₅)`
  (`|u(ζ)| = 6.854 = φ⁴`); the 253-to-2585-object inclusion itself was not checked.
- The rest (C, E, G, H, I, J) is at statement level, with the provenance in the ROWS file.

## 5. RESIDUE (return of 11 Nov 18:32 UTC; the 83 rows no intake had named)

85 rows: 54 Proved, 11 Refuted, 7 Known, 13 Open. Its report says "substantive but incomplete". No review of it
exists beyond author checks of Part E on 11 Nov (`pro_reviews_20261110/8_RESIDUE/checks_author/`, Claude Fable 5.2;
its effort is to be read from that agent's metadata): they reproduce E.1's posets through `n = 6` and E.3's catalogue
(1, 3, 14, 102 classes; 5,313 rows; 5,307 contractible; 6 exceptional).

**B.2–B.4: sound** (I derived B.3's functor before reading it). `𝒬` is the quotient of `Hot` by the maps factoring
through `S¹` (with an adjoined zero); the inverse image of isomorphisms under `(q, H₁(−; Q))` is exactly `W_circ`, so
it is strongly saturated, retract-closed, its aspherical categories are the weakly contractible ones, and absolute
Theorem A holds by Quillen. B.4: the crowns `C₈ → C₄` (`i ↦ i mod 4`, degree 2), suspended over `{o < +, o < −}`.
B.8 (re-proved by hand): `v × id_{C₄}` has degree 2 on `H₂` of the torus. B.16–B.17: `W_nb` (near-bijections on
infinite component sets) refutes XV 9.9–9.13 for the literal axioms; my remark: `W_nb` is not retract-closed
(`{0, 1} → e` is a retract of a member), so this agrees with DER_FOLLOWUP G.7 (Loc (1 bis) restores them).

**D.8: sound** (re-proved by hand): a covering with monodromy through a finite p-group is an intrinsic fibration for
mod-p homology (filtration of `F_p[F]` with trivial factors). D.12: for Z and Q exactly the trivial coverings.

**The rest (statement level):** A.1–A.4 prove Lead 2 and classify equivalence-transport bifibrations; A.5 enumerates
the monoids of order ≤ 5 (1, 2, 7, 35, 228; only the five-element rectangular band is not a 1-type); A.8 (non-equivalence
adjoint transports over that monoid) open. C.2 proves Lead 3; C.3 a five-object counterexample. D.2 proves Lead 1;
D.4: `Fib_W` is not a lifting class for `W_∞ ⊆ W ⊆ W₀`; D.11 the fibration-axiom table. E.2: `J` is an equivalence for
the marked chain; E.4: a transient `S¹` at a fixed four-object shape; E.6 open. F.3 classifies the full subcategories
of `Δ_inj` (total iff a singleton or unbounded) and free categories (total iff filtered). G.2, G.5 on maps
preserving open-test equivalences; G.3 open. H.1–H.8: second proofs of BISITE D.11, F.15–F.17, B.15 (H.7: a program
over 1,349,916 maps of posets with at most five elements). I.1: discrete fibrations are the largest diagonal-stable
smooth class; I.3 completes BISITE F.10; I.9 the second `W^lc` stages for spectra and `D(F_p)`. J.1 for 1-category
bases; J.2, J.3 open.

**Out of date in the RESIDUE register:** F.5 (total ⇒ exact) is refuted by TOTAL_EXACT_2 (`C_δ`, 13 Nov); F.6
(F.27) by PRETOT A.5 (`π₁ = SL(2,5)`); F.7 (PATHS A.8) answered by PRETOT F.6 (per the 12 Nov update in
`pro_reviews_20261110/KNOWLEDGE_HANDOFF.md`); E.6 (PATHS B.8) has an unverified proof in the PATHS intake's findings
F2–F3 of 12 Nov, which has to be reconciled with E.3–E.4; B.10 is answered in part by DER_FOLLOWUP G.11–G.14.

## 6. What follows for the programme

### 6a. Open items these results close, move or refute

| Item | Before | Now |
|---|---|---|
| FRAISSE_EXACT A.3 (i), (ii), (iv), (v), (vi) second half, (vii), (viii) | open | refuted (FREX A.7, A.8, A.11, A.12, A.19, A.33) |
| FRAISSE_EXACT A.3 (iii) | open | open; the gate: non-metrizable universal minimal flow and a distorted affine-relation image (A.23, A.30) |
| FRAISSE_EXACT A.1, the expert's question "is totality determined by `G`?" | open | yes (A.26) |
| FRAISSE_EXACT C.4, "all F_p ⇒ Q" (Lead 10) | open | refuted (C.12); the total-index version open, with eight construction families excluded |
| Lead 8 (the predimension family) | partly | complete table (D.9) |
| DF intake §7, free monoids over `C_δ` (FRAISSE_EXACT G) | open | open; the gap diagram passes; reduced to the transgression kernel (G.33) |
| DF intake §7 A.1 (W7 bis, W8 bis ⇒ homology?) | open | refuted (DER_LOCALIZERS A.3 with A.5–A.7) |
| DF intake §7 A.2 (repaired form) | open | settled (A2.1–A2.14); bare derivators with constant coefficients open |
| DF intake §7 A.5 (Loc (8) in 7.7.2) | open | settled (A5.1–A5.4) |
| DF intake §7 B.1 (`TC = C ∩ W`) | open | refuted for intervals; exact answer on sSet (B.10) |
| DF intake §7 C.1 (linear Thm(?)) | open | refuted in general (C.26); corollary case open (C.raw_gate) |
| DF intake §7 D.1 (local systems) | open | naive form refuted; repaired form proved (D.1–D.4) |
| REVLOC D.2.4, D.3.2 (NEW_PROMPT_ITEMS A1, A2) | open | open; reduced (A34.5, A34.6; A4.5–A4.8) |
| POLES A.16 | closed 15–16 Nov (REVLOC F.1) in our records | closed on 11 Nov (RESIDUE B.3) |
| POLES F.14 (1) | refuted | rechecked (DER_LOCALIZERS A.7, A.9) |
| RESIDUE F.5, F.6, F.7 | open in RESIDUE | closed by TOTAL_EXACT_2, PRETOT A.5, PRETOT F.6 |

### 6b. Earlier claims of ours that these results contradict or correct

1. **NEW_RESULTS 8** (quoted as R3 of the DER_LOCALIZERS prompt): "Everything in XII that uses the strong form of
   W(7 bis) holds for homology localizers only" is false (A.3 with A.7). NEW_RESULTS 7 (the expert's `W_S`) stands.
2. **R5 of the DER_LOCALIZERS prompt** paraphrased REVLOC D.2.5 too broadly; the proved hypothesis is
   `0 ≠ T(W) ⊆ loc(HQ)`.
3. **`INTAKE_S2COUNT_REVLOC_20261117.md`, row F.1**, "closes POLES A.16": RESIDUE B.3 closed it on 11 Nov. Its footnote
   sentence, already corrected by the DF intake, is now exact: footnote 56 is wrong for Loc (6′ a, 8, 9) and right
   once Loc (8) is removed (DER_LOCALIZERS A5.3).
4. **The DF intake's §5 table** (XVI ms. 2 footnote 1; XV 9.10–9.13; XVI ms. 118) and the editors'-insights entries
   XV.9 and XVI.2 credit DER_FOLLOWUP and REVLOC only; RESIDUE B.3, B.8, B.16, B.17 are earlier derivations of the same
   negative facts (the repairs differ: RESIDUE uses Loc (3 bis), DF G.7 the weaker Loc (1 bis)).
5. **The expert's Lead 2 of DER_LOCALIZERS** (local systems via the comma spectral sequence) is false as stated (D.1),
   and the locator of follow-up @270 (cote 133/006–008) does not state the conjecture (D.10).
6. **The expert's hunch 1 (FREX Lead 12)** needs the opposite variance (B.10); **Lead 7**'s finite-extension formula
   needs `F ≠ ∅` (B.8); "(Rig) + (St) ⇒ (Op)" needs (Int) (B.14).
7. **Conference items:** FE-1's odd-characteristic exactness is false (A.13); FE-4's spectral-sequence clause is false
   (D.12); FE-3 is refuted as the prompt expected (C.18).
8. **Lead 8 (e)**: the proposed "exact, not amenable" candidates `C(3, a, b)` with `2b < a` are not exact (D.9).
9. For the transcription: the glyph in W8 bis (a) at 105/052 must be `f` (A.3); Grothendieck's replacement margin at
   105/052 is false (A2.8).

### 6c. Hunches, each as the question a Pro prompt would take (mine, unchecked)

1. **Exactness as unimodularity in the dimension group of the flow.** For `G = Aut(M)` with a co-precompact extremely
   amenable `H` (metrizable universal minimal flow `X`), A.9 and its converse suggest: `colim_A` is exact over a field
   `k` iff the class of `1` is non-zero in `C(X, k)_G`, and exact over Z iff `[1] ∈ C(X, Z)_G` admits a homomorphism
   to Z sending it to 1; amenability is the existence of a positive state. *Prove or refute the Z-statement (A.9 gives
   one direction), and compute `C(X, Z)_G` for the posets of A.11 (where an integer state exists and no positive one)
   and for the convex equivalence class.* Reason: it would make A.11 and A.19 two instances of one dichotomy (integer
   versus positive invariant functionals on the clopens of one compact `G`-space).
2. **FRAISSE A.3 (iii).** *Prove or refute: in setting (S) with (Rig), (FA), (FA∅), (Op) and `G` amenable, every
   finite-family image `J` of (DG.1) has a linear filling bound.* By A.30 this is equivalent to the open implication;
   a counterexample must have a non-metrizable universal minimal flow (A.23).
3. **All primes against Q for total indices** (C.4 left): *prove or refute that a total category exact over every
   F_p is exact over Q*; any counterexample has torsion saturations of unbounded exponent (C.15) and no weakly
   terminal object (C.6).
4. **Free monoids over `C_δ`:** *prove or refute that the transgression `d₂: H₂(Y) → A_cut` of G.33 is injective for
   every smooth locally free `G`-monoid of `C_δ`*, then connect the abelian row to the monoid comparison.
5. **Corollaire 7.7.2 with sums in place of filtered colimits.** `W_fin` fails relative Theorem A exactly on an
   infinite coproduct. *Prove or refute: XVI Loc (1)–(3), Loc (6′ a) and closure under arbitrary sums imply
   Loc (3 bis).* Cisinski's route needs transfinite compositions, which sums alone do not give; a class closed under
   sums and failing sequential colimits would decide it.
6. **Bare derivators.** *Prove or refute: for every strong derivator (no enhancement), either constant-coefficient
   provisional half of Der 6 forces `W_D` to be `RT`-fixed* (A2.14 proves it for ∞-categories; A2.12 shows that
   constant coefficients do not give locally constant ones in the unpointed case).
7. **The bifibration over the rectangular band (RESIDUE A.8, VIc-C022).** *Decide whether a bifibration over `BM`
   with right-adjoint, non-equivalence transports and weakly contractible total category exists*, using the split data
   of A.4 (`D`, `A_i`, `B_j`, `β_{ji}`) and its clutching class.

## 7. Unsent prompts

The only unsent Dérivateurs prompt is `07_FINMON_CP2`. These four returns do not bear on its main question (the
17–21-arrow families of `CP²`) nor on its Part B in substance; one input fits: RESIDUE A.5's census of monoids of order
at most five, as a check of the corner catalogs. The paragraph and its files are in `PROMPT_UPDATES_20261119.md`,
with the items above (6c and the open gates) laid out for successor prompts of FRAISSE_EXACT and DER_LOCALIZERS.
I did not edit any prompt.

## 8. Not done

- The ~420 rows at statement level in ROWS; in particular REVLOC's D.2.11–D.2.61, DER_LOCALIZERS C, A34, A4, FREX G
  beyond G.12, FREX B, E, RESIDUE A, C, E–J.
- No cited source opened (Bodirsky 2014, Hubička–Nešetřil 2019, EHN 2021, Zucker 2016, Kechris–Sokić 2012,
  Cisinski 2006, Rădulescu-Banu 2009, Cisinski–Tabuada 2011, Toën, Higman/Malcev, OEIS A058129).
- No program of the returns run; the finite certificates of DER_LOCALIZERS A5.3 (58 objects, 518 arrows) and RESIDUE
  B.4 were checked by hand, not by a program of mine.
- No PDF check of the four papers.
- The registry, the ledger, STATUS and the RUNBOOK are the main session's.
