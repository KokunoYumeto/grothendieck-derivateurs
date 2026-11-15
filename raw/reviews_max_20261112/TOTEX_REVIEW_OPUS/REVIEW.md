# Review of the Pro return TOTAL_EXACT (TOTEX), 12 November 2026

Claude Opus 5.5 (effort max), 12 Nov 2026. No sub-agents.

**Reviewed.** The return of GPT-6 Astra (ChatGPT Pro mode) to `pro_prompts_max_20261112\TOTAL_EXACT\PROMPT.md`, unpacked in
`longue_marche_pro_pilot_20261104\answers\TOTEX_unzipped\`: `TOTEX_paper.tex` (read in full, 1,978 lines; the PDF was not
opened), `TOTEX_results.csv` (58 rows: 43 Proved, 5 Known, 4 Refuted, 6 Open), `TOTEX_report.md`, the bibliography inside the
TeX, and every mathematical program of `code\` with its recorded output.

**Compared with.** The prompt and its R1–R10; the PRETOT return (paper TeX from the prompt's zip, F.1, F.3, F.4, F.6, F.8, E.1,
F.12) and the PRETOT review (`PRETOT_REVIEW_OPUS\REVIEW.md`, `FINDINGS.md`); the Dérivateurs expert's
`RESULT_FILTERED_BY_ONE_TYPES.md` and `HUNCHES.md` (H1, H7) from the zip.

**Sources opened by me.** Adámek–Rosický–Vitale 2010 (attached PDF, §1, Remark 1.1); Charney–Davis 1995, author PDF
(downloaded; text layer unusable, pp. 9–12 read as rendered images); Bojańczyk–Klin–Lasota 2014, arXiv 1402.0897 (downloaded;
§9.1, Fact 9.2, Theorem 9.3, Corollaries 9.4–9.5 with proofs); Isbell–Mitchell 1976, *Exact colimits and fixed points*, Trans.
AMS 220 (downloaded from ams.org, read in full; the return records it as inaccessible); Isbell–Mitchell 1973 (attached; Theorems
1–3, Lemma 1, Corollaries 1–2); Adámek–Koubek–Reiterman 1981 (attached scan; pp. 378–380 and 384–385 read as images); Lurie,
HTT (attached; located 5.3.3.3, 5.5.8.11, 6.5.1.10); the transcription at II ms. 36–36ter, XII ms. 88, 113. Papers I downloaded
are in `papers\`; the attachments I used were extracted from the prompt's zip into `bg\` (with page renderings of the scans).

**Computations.** All 14 mathematical program runs of the return were repeated with `python -I` (Python 3.13.9, SymPy 1.13.1;
the return used 3.12.14 and 1.14.0) in `rerun\code\`, through `rerun\tools\run_isolated.py` (puts only the program's own folder
on `sys.path`). All exit 0; every output is identical to the shipped one modulo CR/LF, JSON compared parsed
(`rerun\out\COMPARISON.txt`, `RUNLOG.txt`). My own code, written from the paper without importing the return's code, is in
`indep\` (§5).

## 0. Result in brief

| Verdict on the 58 statements | Number | Statements |
|---|---|---|
| correct | 44 | all others |
| correct with a gap | 1 | F.4 (source table: IM 1976 marked unavailable, so A.5 and D.14 are not attributed; §4) |
| known | 7 | A.2, A.3 (Isbell–Mitchell 1973), A.5 (Isbell–Mitchell 1976, Cor. 4.4), C.5 (cone attachment), D.14 (Isbell–Mitchell 1976, Remark p. 296), E.4 (Bojańczyk–Klin–Lasota), F.3 |
| open as stated | 6 | A.7, B.7, C.6, D.16, D.20, F.5 (F.5 partly superseded: IM 1976 is open access) |
| wrong | 0 | — |

**Part A is not decided.** The return stops with outcome (c): pairs have affine equalizers (R4), the first undecided case is a
triple `a₀, a₁, a₂: p → q`, and the open statement is `aug(K₁ ∩ K₂) = ℤ`. What it adds to Part A is one restriction on a
separator (not sifted, D.4) and the computation that the Adámek–Koubek–Reiterman category `K*` keeps a nonzero `H₂` through
its whole second stage. The new mathematics of the return is elsewhere: the classification of the classes `𝒯_n` (D.9–D.10),
the fixed-degree Eilenberg–MacLane test (D.7), the final-image exclusion for coloured words (E.5), the defects of AKR B.5–B.6
and the stage computations (C.1–C.4), and the animated reflection (D.17–D.19). I found nothing wrong.

## 1. Table of verdicts

V = proof followed in full; C = recomputed by my code (§5); S = cited source opened by me; M = manuscript read; O = read in
outline (spot check).

| Id | Claim (short) | Return | Verdict | Checked |
|---|---|---|---|---|
| A.1 | R1 audit: totality ⟺ acyclic ⟺ contractible element components | Proved | correct (= TOTASPH C.5) | O |
| A.2 | R2: exact ⟺ `Aff_ℤ` filtered (components) ⇒ total | Known | known (IM 1973 Th. 1, Lemma 1) | S, O |
| A.3 | `Δ_inj` total, exact, not filtered, not sifted | Known | known (IM 1973 Th. 3; proof Isbell 1974) | S, O |
| A.4 | total ⇒ common successors, span completion, pair affine equalizers | Proved | correct (= TOTASPH C.11; AKR Th. [1]) | V |
| A.5 | weakly terminal object: total ⟺ filtered | Proved | known: IM 1976 Th. 4.1, Cor. 4.3–4.4 | V, S |
| A.6 | PRETOT A.5 does not touch R1–R6 | Proved | correct | O (reruns identical) |
| A.7 | Part A open; first case a triple; `aug(K₁∩K₂) = ℤ` | Open | open as stated (precise; §6) | V |
| B.1 | R7: triple ⟺ `ε(K₁∩K₂) = ℤ`; `T₁(P_q/(K₁+K₂)) ↠ (εK₁∩εK₂)/εL` | Proved | correct; under totality the map is an isomorphism onto `ℤ/εL` (F2) | V |
| B.2 | `H₁, H₂, H_j` of `El H₃` via `K = ker(P_q² → P_p)` | Proved | correct | V |
| B.3 | presentation-graph formula for `H₁` | Proved | correct | V |
| B.4 | finite relation graph: `H₁, H₂, H₃` | Proved | correct | V |
| B.5 | quasi-filtered ⇒ `H₁` of every element component is 0 | Proved | correct | V |
| B.6 | quasi-filtered ⇒ element components simply connected | Proved | correct | V |
| B.7 | the missing bridge to `ε(K₁∩K₂)` | Open | open as stated (sharpened in F2) | V |
| C.1 | AKR B.6: (11) fails under restriction; sign misprints; repair satisfies (9)–(11) | Refuted | correct (scan pp. 378–380 read; repair recomputed) | V, S, C |
| C.2 | repaired `K₁`: 17 objects, 1,263 arrows; `H_*` = (ℤ,0,ℤ) pair, (ℤ,0,ℤ⁴) triple | Proved | correct | C |
| C.3 | the `K₁` class injects into `H₂` of the full `K₂` | Proved | correct (input `H₂(El_{D_T}) = 0` recomputed for all 17 `T`) | V, C |
| C.4 | selected `K₂`, `K₃` substages keep `H₂ = ℤ`; B.9 variant: `ℤ³ → ℤ²` | Proved | correct | C |
| C.5 | cone-attachment exact sequence | Known | known (standard) | V |
| C.6 | persistence to `K₃` and `K*` undecided | Open | open as stated | V |
| C.7 | adjoining a terminal object: filtered, total, exact | Proved | correct, but trivial: prompt item C.2 not addressed (F12) | V |
| D.1 | R8 in general = componentwise filtered | Refuted | correct (= PRETOT F.1) | V |
| D.2 | inherited actions; doubled action gives common successors | Proved | correct | V |
| D.3 | RAAG audit of R8 | Proved | correct (Charney–Davis checked; = PRETOT F.4) | V, S |
| D.4 | sifted + total ⇒ filtered | Proved | correct (= PRETOT F.3; ARV 1.1(i) used correctly) | V, S |
| D.5 | abelian one-types suffice; `∫M → B colim M` for all `M` ⟺ filtered | Proved | correct (= PRETOT F.6, not credited) | V |
| D.6 | low homology of `K(M,n)`; discrete self-equivalences | Proved | correct (standard) | V |
| D.7 | total + one fixed `n ≥ 1` EM test ⇒ filtered | Proved | correct (new for `n ≥ 2`) | V |
| D.8 | hocolim preserves `n`-connective maps | Proved | correct (standard; HTT 6.5.1) | O |
| D.9 | simply connected `C` in `𝒯_n` (`n ≥ 1`) is filtered | Proved | correct (new) | V |
| D.10 | `𝒯_n` (`n ≥ 1`) ⟺ all `C_a` filtered; `𝒯₁ = 𝒯₂ = ⋯` | Proved | correct (new) | V |
| D.11 | finite data in the criterion; `ℕ ∈ 𝒯_n` | Proved | correct | V |
| D.12 | `π_i hocolim HM = L_i colim M`; EM ⟺ exact | Proved | correct (standard) | V |
| D.13 | total ⇒ `L_i colim R[H] = 0` | Proved | correct | V |
| D.14 | `R`-affine criterion | Proved | known: IM 1976, Remark p. 296 | V, S |
| D.15 | separate `ℚ`, `F_p` finite tests | Proved | correct (elementary) | V |
| D.16 | integral / `ℚ` / `F_p` implications open | Open | open as stated | V |
| D.17 | `LG_F ≃ colim^{D(ℤ)≥0} F`, `π_i = L_i colim F` | Proved | correct | V |
| D.18 | `π_i(LG) = H_i(C_•(G))` | Proved | correct | V |
| D.19 | `G = Hom(−,ℤ)/±1`: `π_{2j}(LG) = ℤ/2`, odd 0 | Refuted | correct | V, rerun |
| D.20 | special `G_F` = the main question | Open | open as stated | V |
| D.21 | R9: products, opfibrations, element components | Proved | correct | V |
| D.22 | final images preserve both classes | Proved | correct | V |
| D.23 | non-empty full cosieves | Proved | correct | V |
| D.24 | localization, idempotent completion | Proved | correct | V |
| D.25 | filtered colimits along final transitions | Proved | correct | V |
| D.26 | no separation by the four operations | Proved | correct (preservation only) | V |
| E.1 | coloured-word categories `W_m` | Proved | correct | V |
| E.2 | `W_m`: `Aff_ℤ` filtered, total, exact, not filtered, not sifted; `W₂,W₃,W₄` inequivalent | Proved | correct | V, rerun |
| E.3 | RAAG test fails (`π₁ = ℤ²`, `H₂ = ℤ²`); no final `W_m → Δ_inj` | Proved | correct | V |
| E.4 | least supports for `Aut(ℚ,<)` | Known | known (BKL Th. 9.3, Cor. 9.5) | S, V |
| E.5 | no final functor `Δ_inj^r × I → W_m` (`m ≥ 2`, `I` filtered) | Proved | correct (new) | V |
| E.6 | `W₂, W₃, W₄` meet Part E | Proved | correct | V |
| F.1 | II ms. 36ter false; strengthened forms | Refuted | correct | V, M |
| F.2 | class diagram | Proved | correct | V |
| F.3 | historical sources | Known | known | S |
| F.4 | attribution table | Proved | correct with a gap (§4) | O |
| F.5 | Oberst 1968, IM 1976, Gabriel–Ulmer not obtained | Open | open as stated; IM 1976 now opened (F3) | S |

Checked fully (V or C): 50 statements. By spot check (O, or the cited source alone): A.1, A.2, A.3, A.6, D.8, F.3, F.4, F.5.
Not checked at all: none of the 58 statements; outside them, the PDF, the results-ledger builder and the packaging scripts.

## 2. Decisive results, checked in the requested order

### 2.1 D.4: sifted and total implies filtered

ARV Remark 1.1(i) (opened, p. 253): "a small, nonempty category `D` is sifted if and only if the diagonal functor
`Δ: D → D × D` is final. This means that for every pair of objects `A, B` of `D` the category `(A,B) ↓ Δ` of cospans on
`A, B` is connected", spelled out as (a) a cospan exists and (b) any two cospans are joined by a zigzag; ARV credit Gabriel–Ulmer
and Lair. TOTEX's `C_{p,q} = El_A(A(p,−) × A(q,−))` is exactly `(p,q) ↓ Δ`, and a total category is non-empty, so the use is
correct. The rest: `C_{p,q}` inherits simply connected element components (D.2: `R(a) = ∐_{(a,s) ∈ C} T(a,s)` gives
`El_A R ≅ El_C T`), so it has common successors (D.2: the doubled action on `C` glued along the disjoint cosieves `U_p ⊔ U_q`
has `H₁ = ℤ` by Mayer–Vietoris, `H₁(BC) = 0`); a common successor of `(q; u, id_q)` and `(q; v, id_q)` is `f, g: q → r`
with `fu = gv`, `f = g`. Correct.

**Comparison with PRETOT F.3.** Same theorem (PRETOT Lemma `F:sifted-total`: "if `A` is sifted and satisfies `𝒫₁(A)`, then
`A` is filtered"), same hypothesis (simply connected element components suffice), same proof, nearly the same words. TOTEX
credits it ("checks … the short argument in the supplied PRETOT Lemma F.3"). Both correct. Consequence for Part A: a separator
is not sifted.

### 2.2 D.5/D.7, D.9/D.10, and the RAAG step

**D.5** is PRETOT F.6 (Theorem `F:abelian-tests`): the same statement ("for every small `A`, `∫_A M → colim^{Ab}_A M` is a
weak equivalence for all `M` iff `A` is filtered") with the same proof (the diagram `ℤ[A(p,−)] ⊕ ℤ[A(q,−)]` gives a free
group of rank 2; the `H₂` edge image `colim Λ²M ↠ Λ²G` forces `E^∞_{1,1} = L₁ colim M = 0`; exact ⇒ total by `Σ_S`; the
cross summand of `Λ²(M ⊕ M')` gives `colim(M ⊗ M') ≅ colim M ⊗ colim M'`, i.e. connected cospan categories). Correct; PRETOT
not credited for it (§4).

**D.7** (fixed `n ≥ 2`; `n = 1` is D.5). Checked step by step: `X_M = hocolim_A K(M,n)` is `(n−1)`-connected (`BA ≃ *`);
the truncation hypothesis gives `X_M ≃ K(colim M, n)`; in the Bousfield–Kan sequence the rows `1, …, n−1` vanish, row `n+1`
vanishes because `H_{n+1}(K(M,n)) = 0` for `n ≥ 2`, row 0 vanishes in positive degrees, so `H_{n+1}(X_M) = L₁ colim M`, and
`H_{n+1}(K(G,n)) = 0` gives exactness. Exactness collapses the sequence, `colim H_{2n}(K(M ⊕ M', n)) ≅ H_{2n}(K(colim M ⊕
colim M', n))`; the Künneth cross summand `M ⊗ M'` in degree `2n` is natural because no Tor term can occur (positive indices
`≥ n` cannot sum to `2n−1`). So cospan categories are connected, `A` is sifted, D.4 applies. Correct. The prompt's D.3 first
question is answered positively.

**D.9.** `n = 1`: the doubled action `S` has `E²_{1,1} = H₁(El_C S) = ℤ`, which survives (`E²_{3,0} = H₃(BC) = 0`), while
`π₁ hocolim_C Bℤ[S] = colim^{Grp} ℤ[S] = ℤ`; a 1-type would force `H₂ = 0`. `n ≥ 2`: the projection `X_M → BC` has
`(n−1)`-connected fibres (D.8) which are `n`-types, hence `K(L,n)`; pointed `K(L,n)`-fibrations are classified by
`B Aut(L)`, trivial over the simply connected `BC`, so `(X_M, BC) ≃ (BC × K(L,n), BC × 0)` and `H_{n+1}(X_M, BC) = 0`
(Künneth: `H₁(BC) ⊗ L = 0`, `Tor(ℤ, L) = 0`, `H_{n+1}K(L,n) = 0`); the relative sequence gives `L₁ colim M = 0`. Correct.

**D.10.** The functor `Hom_{ΠA}(a, ℓ(−))` inverts arrows, so `B C_a` is the universal cover of the component of `a`; `𝒯_n`
passes to element categories by the dependent sum (`hocolim_A Σ_S Y ≃ hocolim_{El S} Y`; coproducts of `n`-types are
`n`-types) and to their components (extend by `∅`); D.9 gives `C_a` filtered. Conversely the pullback of the universal cover
along `hocolim X → BA` is `hocolim_{C_a} Xπ`, an `n`-type when `C_a` is filtered, and a covering is an isomorphism on `π_k`,
`k ≥ 2`. Correct, including `T₀` and `𝒯₀ ∩ 𝒯_n` = componentwise filtered. A cleaner wording (mine): `C_a` is the comma
category `a ↓ ℓ` of the groupoid completion `ℓ: A → ΠA`; **for `n ≥ 1`, homotopy colimits over `A` preserve `n`-types iff
every comma category of `A → ΠA` is filtered**, so `𝒯₁ = 𝒯₂ = ⋯` and the prompt's question "`𝒯_n ⊂ 𝒯_{n+1}`?" has the answer
"equal". Groups and the monoid `ℕ` are in every `𝒯_n`, `n ≥ 1` (D.11, checked: `C_*` is `(ℤ, ≤)`).

**RAAG / Salvetti (D.3, R8) against Charney–Davis.** I read the author PDF pp. 11–12: Theorem 3.1.1 (for right-angled `W`,
`Z_W` with its cubical structure is nonpositively curved), Remark 3.1.2 ("Any nonpositively curved, piecewise Euclidean, finite
complex is an Eilenberg–MacLane space"), Lemma 3.1.3 (the vertex link of `Σ̃_W` is a flag complex), Proposition 3.2.1 (`Z_W`
is the subcomplex of the torus `(S¹)^S` on the spherical subsets; all cellular boundary maps vanish). The citations are exact.
Charney–Davis treat finite `S`; TOTEX's passage to infinite bipartite graphs (directed union of finite full subgraphs, spheres
and null-homotopies are compact) is right. Bipartite graphs have no triangles, so the cells are circles and tori;
colour-preserving graph maps send tori to tori with degree `+1`; `H₂(X) = ℤ[colim(Q ⊔_E Q)]` and `* ⊔_{colim E} *` is one point
as soon as `E ≠ ∅`; `π₁(X) = colim^{Grp} M = ℤ²` needs `π₁(BA) = 1`, which kills the transport generators. Correct.

### 2.3 E.2, E.5, E.6: the coloured-word categories

**E.2.** For a word `w` of length `l`, `f̃_w(i) = m·f(i−1) + w_i` maps `w` into `R = (1…m)^N`; it is strictly increasing
(`m(f(i) − f(i−1)) ≥ m > w_i − w_{i+1}`) and colour preserving; `f̃_w ∘ a = (f a')~_p` for `a: p → w`, so the uncoloured
identity `ta = tb` of R3 lifts to `t_w a = t_w b` with `aug(t_w) = 1`. IM 1973 Lemma 1 and Theorem 1 give exactness, R2
totality. Not filtered (the two monic arrows `c ⇉ cc`), not sifted (the cospans of `(c, c)` fall into three components by
`<, =, >`), `W_m` has an initial object and exactly `m` atoms, so `W₂, W₃, W₄` are inequivalent. Correct.

**E.5 and the BKL step.** BKL Theorem 9.3 (opened): for any symmetry `(D, G)`, condition (1) (for finite `E` and `c ≠ d ∉ E`,
`c·G_E ⊆ c·⟨G_{E∪{c}}, G_{E∪{d}}⟩`) is equivalent to (2) "if `G_C ≤ H` and `G_D ≤ H` then `G_{C∩D} ≤ H`"; Corollary 9.5:
the total order symmetry `(ℚ, Aut(ℚ,<))` admits least supports. Taking `H = ⟨G_S, G_T⟩` in (2) gives TOTEX's
`⟨G_S, G_T⟩ = G_{S∩T}`; TOTEX's own verification of (1) is BKL's proof of Cor. 9.5 (an intermediate point `z`, two moves); the
extension to `G^r` (products of stabilizers, generated factorwise) is right. The main argument: the filtered colimit `L` of
`F` restricted along `J^r × I` (finite subsets of `ℚ`) carries a `G^r`-action with finite supports; the bijection
`colim Hom(w, F(−)) ≅ G^r∖Emb_col(w, L)` holds (choices of representing sets differ by `G^r`; morphisms are realized by
inclusions because `ℚ` is dense; injectivity through a common stage); finality makes `G^r` transitive on each `Emb(w, L)`; for
two colours the pairs `L_c × L_d` form one orbit (disjoint support coordinates) or at least three (overlapping coordinates:
before / after / meeting), whereas the words `cd`, `dc` force exactly two. Correct. **E.6** follows (products and composites of
final functors are final; `W₁` is excluded because `Δ_inj ⊂ W₁` is final).

### 2.4 B.1–B.4

**B.1.** `T₁(C) = ker(colim S → ℤ)` from `0 → S → P_q → C → 0`; `0 → L → K₁ ⊕ K₂ → S → 0` and right exactness give the
surjection onto `(ε(K₁) ∩ ε(K₂))/ε(L)`; correct, and TOTEX's correction (the pairwise hypothesis is needed for the target
`ℤ/ε(L)`) is accurate. **Sharpening (mine, F2).** Under totality `colim K_i → ℤ` is an isomorphism (it is injective because
`H₂` of the pair quotient `A(p,−)/(ca₀ ∼ ca_i)` is `ker(colim K_i → ℤ)`, and onto because its `H₁ = ℤ/ε(K_i)` vanishes), so
`colim S = ℤ²/{(n, −n) : n ∈ ε(L)}` and

  **for total `A`: `T₁(P_q/(K₁ + K₂)) ≅ ℤ/aug(K₁ ∩ K₂)`** (the R7 map is an isomorphism).

So the triple obstruction is *exactly* the non-vanishing of one derived colimit of one non-permutation module.

**B.2** (`ℤ[H₃]` has the presentation `P_q² → P_p → ℤ[H₃] → 0`; `colim J → ℤ` is zero since `colim d = 0`), **B.3**,
**B.4**: correct; the expected formulas `ℤ²/aug(K)` and `ker(colim K → ℤ²)` hold, with `K ⊂ P_q²` (not `K₁ ∩ K₂`), as TOTEX
stresses. **B.5** (partition an affine equalizer by `z = H(c)k`; coefficients of a basis composite `g` only come from `c` with
`H(c)k = H(g)h`) and **B.6** (cyclic covers flattened to actions on `A`) are correct: quasi-filtered categories have simply
connected element components, so `H₂` is the first condition beyond quasi-filteredness, as R7 said.

### 2.5 The reduction of Part A

Exactness ⟺ simultaneous affine equalizers of all finite families (IM 1973 Th. 1 with Lemma 1, given common successors) is
right; pairs are settled (R4); a triple has a simultaneous affine equalizer iff `ε(K₁ ∩ K₂) = ℤ` (B.1, with common successors);
the triple is therefore the smallest undecided instance. **But the triple is not a reduction of Part A.** A proof for all
triples does not formally give quadruples: after equalizing `a₀, a₁, a₂` by `s`, the next step is to equalize the *affine* pair
`(s a₀, s a₃)`, whose supports are large. The exact general form (mine, F4): by IM 1973 Lemma 1, Part A ⟺ every pair of affine
arrows has an affine equalizer ⟺ every `z ∈ ℤ[A(p,r)]` with `aug(z) = 0` has an affine annihilator ⟺

  **`T₁(P_p/⟨z⟩) = 0` for every `z` of augmentation 0** (one generator, one relation; `T₁(P_p/⟨z⟩) = ℤ/ε(ann z)`),

and totality gives exactly the binomial case `z = c − c'`, where `P_p/⟨z⟩` is a permutation module. The "missing comparison"
of A.7, B.7, D.16 is stated correctly; B.7's bridge "a surjection from groups known to vanish onto `ℤ/ε(K₁∩K₂)`" can now be
read as: show `T₁(P_q/(K₁+K₂)) = 0`, which under totality is equivalent to the claim itself (F2). D.16's diagnosis of the
free-resolution attempt is right: in the bar resolution `⋯ ⇉ ℤ[Uℤ[F]] → ℤ[F] → F` the face `d₀ = ε` is linear, not induced by
a set map, so totality does not control the resolution.

The restrictions on a separator stated by the return follow: no weakly terminal object (R5; in fact IM 1976 Cor. 4.4), hence
infinitely many objects (finitely many objects with common successors give a weakly terminal one), and not sifted (D.4). §6.3
adds five more.

### 2.6 Part C (AKR)

**Source defects (C.1), checked on the scan.** P. 378, Lemma B.5: (c) prints `x − y = 4k − i + j`, (d) `4k + 1 − i + j`; the
proof's case β gives `x − y = 4k − (i + j)`, and substitution gives `4k + 1 − i − j` in case γ: the statement has sign
misprints, as TOTEX says. P. 379, B.6: `Z = Y₀^e ∪ (Y₀^* × s̄) ∪ (Y − Y₀) × I` while `α_i = β_i^{(α)} w` lands in `s̄ × I`: a
target-type slip. Pp. 379–380: "… and so does any domain-range restriction of `{β_i^{(α)}}` as a quasi-filter for any
domain-range restriction of `Φ_n^{(α)}, Ψ_n^{(α)}`." This is false: from the displayed formula, `β₀³(x) = x` and
`β_{4k}³(x) = x` for `x ≤ 1`, so on the two-point path `{0,1}` the consecutive images coincide (two points) while the
identified composite has one point, violating (11). The repair (actual path length `n_j`, common `k ≥ max n_j`) and its interval
table are correct; my own construction from the paper's formulas verifies the neighbour identities and (11) for every
quasi-filter built (0 failures repaired; failures present in the literal common-`n` variant); the return's program also checks
(9) and (10). The defect does not refute AKR Theorem C.2: Construction C.1 (p. 384) recalls (9)–(11) for the induction of
(c_m), (d_m) (p. 385), and the repaired quasi-filters satisfy them, as the return says. (I read the proof only up to the start
of that induction.)

**Stage computations (C.2, C.4).** My independent construction (`indep\akr_indep.py`) reproduces every count and every Betti
number over `F₂, F₃, F₅, F_{1000003}`: repaired `K₁` 17 objects, 1,263 arrows, nerve (428, 1656, 1230), pair `H` = (1, 0, 1),
triple nerve (21, 1246, 1230), `H` = (1, 0, 4); selected `K₂` substage 18 objects, 21,461 arrows, nerve (7161, 35470, 48966,
20655), (1, 0, 1, 0); critical `K₃` substage 19 objects, 81,430 arrows, nerve (27250, 162191, 322323, 267570, 80190),
(1, 0, 1, 0, 0) over `F₂` and `F_{1000003}`; literal variant `K₁` 1,257 arrows, (1, 0, 3), triple (1, 0, 10), `K₂` substage
21,301 arrows, (1, 0, 2, 1). The return's unit-elimination certificate proves torsion-freeness; my primes exclude 2-, 3-, 5-torsion
independently.

**C.3 (the class survives the whole second stage).** Followed in full: every arrow into a second-stage quasi-filter target
factors through some `α_i: T → Z`, so each link projects into the down-set `El_{D_T}(H|D_T)` (a full subcategory closed under
predecessors), and sum links lie over one summand; distinct new targets are unrelated. The input `H₂(El_{D_T}) = 0` for all 17
objects `T` of `K₁` I recomputed (`indep\out_downsets.txt`). Correct.

**New computation (mine, F11).** At every object of every computed stage (repaired `K₁`, `K₂` and critical `K₃` substages;
literal `K₁` and `K₂`), the triple `v₁, v₂, v₃` has no simultaneous affine equalizer over `ℚ`, `F₂` or `F₃`
(`indep\akr_triple_equalizers.py`), while each pair is equalized exactly at the targets built for it. In the literal B.9
variant an `H₂` class of `El(h_V/(cv₁ ∼ cv₂))` dies at the selected second-stage attachment and still no triple equalizer
appears there.

### 2.7 D.17–D.19 (animated abelian groups)

D.17: `jF(a) = Hom(−, F(a))` is product preserving, colimits in `𝒫(𝒞)` are pointwise, R1 identifies the pointwise hocolim with
`G_F`, and `L` (a left adjoint) fixes `jV`; with `𝒫_Σ(𝒞) ≃ D(ℤ)_{≥0}` the result is `L colim F`. D.18: the density
hocolim over `E_G` (each pointwise component has the initial object `(Q, z, id)`), then the bar complex. D.19: pointwise the
square `(y0)_{hC₂} → (yℤ)_{hC₂}`, `y0 → G` is a homotopy pushout (`C₂` acts freely off 0), `L` gives
`LG ≃ (ℤ_sign)_{hC₂}`, and `H_*(C₂; ℤ_sign)` is `ℤ/2` in even degrees, 0 in odd degrees (I recomputed the resolution).
Correct; the rerun of `main_sign_reflection_check.py` is identical. D.20 is right: for total `A`, all `LG_F` are discrete iff
`colim_A` is exact; the reflection is a reformulation, not a tool.

### 2.8 The rest (lighter)

D.21–D.26 (followed: the opfibration fibre inclusion has a left adjoint, so it is homotopy final; localization is final by
partial words; `Kar(A)` inclusion is homotopy final and `El_{Kar A} H̄ ≅ Kar(El_A H)`; filtered colimits along final
transitions) are correct; D.26 answers the prompt's D.6 for preservation only, as it says. F.1's manuscript corrections are right
where I checked them: II ms. 36 prints "`y∖Y` 0-connexes" where `y∖X` (comma along `f`) is meant; XII ms. 88 prints
`U'/t' ≃ U/H'` for `U'/H'`; XII ms. 113 `X' = U' ⨿_U X'` is already corrected in the transcription to `U' ⨿_U X`.

## 3. New mathematics, with the literature searched

**N1. Classification of the truncation-preserving shapes (D.9–D.10, D.11).** For `n ≥ 1` and every small `A`: homotopy colimits
over `A` preserve `n`-types iff every comma category of the groupoid completion `A → ΠA` is filtered; so `𝒯₁ = 𝒯₂ = ⋯`, groups
and `ℕ` are in all of them, and `𝒯₀ ∩ 𝒯_n` is the componentwise filtered class. *Why it matters:* it answers TOTAL_EXACT D.3
completely and places Grothendieck's question at II ms. 36 in a hierarchy: total = "preserves 0-types", filtered = "preserves
0-types and `n`-types" for any single `n ≥ 1`.

**N2. One Eilenberg–MacLane degree detects filteredness under totality (D.7).** If `A` is total and `hocolim_A K(M(a), n)` is
`n`-truncated for every abelian `M`, for one fixed `n ≥ 1`, then `A` is filtered. `n = 1` is PRETOT F.6 with F.3; `n ≥ 2` is
new here.

**N3. Coloured-word categories (E.2–E.6).** `W_m` (`m ≥ 2`) are total, exact, not filtered, not sifted, pairwise
inequivalent, and not final images of `Δ_inj^r × I` with `I` filtered; the proof uses least supports of the ordered atoms.
*Why:* Part E asked for examples beyond `Δ_inj`; the final-image exclusion is a genuine invariant, not a size count.

**N4. The AKR construction (C.1–C.4).** Two misprints and a false restriction claim in AKR B.5–B.6 (confirmed on the scan), a
repair, exact stage homology, and a proof that the first `H₂` class survives the full second stage. *Why:* it is the only known
quasi-filtered non-exact category; R10's expectation (not total) now has computed support but no proof.

**N5. Animated reflection (D.17–D.19).** `π_i(LG_F) = L_i colim_A F` for total `A`; a chain criterion for discreteness; the
sign-orbit presheaf has `π_{2j}(LG) = ℤ/2`.

**Literature searched.** The return's searches (listed in F.4) found none of N1–N5. Mine (web, 12 Nov): "homotopy colimits
preserve n-truncated spaces indexing category characterization filtered universal cover"; "category whose colimits of sets are
homotopy colimits, category of elements contractible components, exact colimits abelian groups"; "which homotopy colimits
preserve 1-types n-types shapes"; "exact colimits not filtered quasi-filtered fixed points Isbell Mitchell Adámek Koubek
Reiterman". Found: the expected background (truncated objects closed under filtered colimits; Thomason's theorem; the
Isbell–Mitchell / Adámek–Reiterman / AKR papers); none states N1, N2, N3 or N5. Opened in full: Isbell–Mitchell 1976, which
contains none of N1–N5 but does contain A.5 and D.14 (§4). Not opened by anyone: Oberst 1968 and Gabriel–Ulmer 1971 (bodies
unavailable), Isbell 1968 and Isbell 1974. No priority is claimed by the return; none should be claimed in the companion before
Oberst and Gabriel–Ulmer are read.

## 4. Credits omitted

- **D.5 = PRETOT F.6** (statement and proof), and with PRETOT F.3 it already settled "the abelian form of R8", which the CSV note
  of D.5 claims as settled here. Not cited. (D.4 = PRETOT F.3 and D.1 = PRETOT F.1 are cited.)
- **D.3** is the check of the expert's R8 note and of PRETOT F.4; the CSV row D.3 lists neither among its dependencies (the paper
  says "the RAAG argument", and A.6 mentions PRETOT's shape statements).
- **A.5 = Isbell–Mitchell 1976, Theorem 4.1 and Corollaries 4.3–4.4.** Theorem 4.1 is the minimal-period signed-measure argument
  of TOTASPH C.13; Corollary 4.4: "If `C` satisfies I and IV and is connected with a weak terminal object, then `C` is filtered."
  Totality gives I and IV (R4). The return marks A.5 "Proved" from TOTASPH and lists IM 1976 as unobtainable; it is open access
  at ams.org.
- **D.14 = Isbell–Mitchell 1976, Remark p. 296**: for commutative `R`, Theorem 3.1 and Proposition 3.3 hold with `aff_R C`.
- **`Δ_inj`:** IM 1973 Theorem 3 states and sketches it; IM 1976 (p. 289) attributes the proof to Isbell, *Exact colimits I*,
  Ann. of Math. 100 (1974). Not cited (I did not open Isbell 1974).
- **D.4's criterion** is Gabriel–Ulmer's (and Lair's), as ARV say; citing ARV alone is acceptable since Gabriel–Ulmer was not
  available, but the original should be named.
- **The question itself:** IM 1976 (p. 298) asks for "an example of a category with the fixed point property whose affinization
  is not filtered, or in other words, one satisfying I and IV, but not III" — AKR 1981 answered it; Part A is the same question
  with totality in place of the fixed point property. The return cites AKR's answer but not the question's source.
- **The expert's results:** R7 (B.1), R8 (D.3, D.5), R9 (D.21), R10 (C.5) are cited by their R-numbers, as the prompt required.
  Not mentioned: H7 (sifted + total ⇒ filtered, settled by D.4 = PRETOT F.3) and H1 point 2, the 2-sphere class
  `κ = (ρ₁ − ρ₃, ρ₃ − ρ₂) ∈ H₂(El H₃)`, which is the natural object for a proof attempt (§6.5, P3).
- **PRETOT overlaps otherwise:** D.23's cosieve step = PRETOT B.4 (cited); PRETOT F.8 (`W_n` tests for `Cat`-valued diagrams)
  is a different question from D.10 and is not duplicated.

## 5. Programs

| Program (return) | Rerun | Output vs shipped |
|---|---|---|
| `akr_stages.py` (`--partial-k2`; `--triple --verify-field`; `--critical-k3`; `--literal-common-n --partial-k2`; `--literal-common-n --triple`) | exit 0 (0.0–11.2 s) | identical (text mod CR/LF; JSON parsed) |
| `akr_component_checks.py` | exit 0 | identical |
| `examples_colored_words.py`, `examples_support_orbits.py`, `examples_affine_base.py`, `basic_shape_checks.py` | exit 0 | identical |
| `main_sign_reflection_check.py` | exit 0 | identical |
| `pretot_audit/main_counterexample.py`, `audit_certificate.py`, `semisimplicial_affine_checks.py` | exit 0 | identical (incl. the 40,619-byte certificate) |

Not run: `build_pdf.py`, `build_totex_results.mjs`, `render_pdf_qa.py`, `verify_package.py`, `source_fetch.py` (typesetting,
ledger, packaging, network; no mathematics).

My code (`indep\`, pure Python integers; outputs `indep\out_*.txt`):
- `akr_indep.py`: the repaired and literal constructions from the paper's formulas, closure and endomorphism checks, the quotient
  functors, nerves, `d² = 0`, Betti numbers over four primes (§2.6); re-verifies the neighbour identities and (11).
- `akr_downsets.py`: `H_*(El_{D_T})` for all 17 objects of `K₁` (the input of C.3): `H₂ = 0` everywhere.
- `akr_triple_equalizers.py`: for every object `r` of every computed stage, whether `aug` lies outside the row space of
  `t ↦ (t(v₂ − v₁), t(v₃ − v₁))` (rational / `F₂` / `F₃` equalizer at `r`), and the same for the two pairs (§2.6).

## 6. THE STATE OF PART A

### 6.1 The exact open statement

For every small non-empty connected `A` all of whose element categories `El_A(H)`, `H: A → Set`, have contractible components:
is `colim_A: Ab^A → Ab` exact? Equivalent forms, all checked:
1. every finite family `a₀, …, a_k: p → q` has `t ∈ ℤ[A(q, r)]`, `aug t = 1`, `t a_i = t a₀` (IM 1973 Th. 1, Lemma 1);
2. every `z ∈ ℤ[A(p, r)]` with `aug z = 0` has an affine annihilator; i.e. `T₁(P_p/⟨z⟩) = ℤ/ε(ann z)` vanishes (F4);
3. for every abelian `M`, `hocolim_A HM` is an Eilenberg–MacLane spectrum (D.12); equivalently, for total `A` and any one
   `n ≥ 2`, `H_{n+1}(hocolim_A K(M, n); ℤ) = 0` for all `M` (D.7's spectral sequence gives `H_{n+1} = L₁ colim M` from
   totality alone; asking for `n`-truncation instead is filteredness, D.7); equivalently every `LG_F` is discrete (D.17).
Pairs (`k = 1`, binomial `z`) are proved from totality (R4). Nothing beyond pairs is proved.

### 6.2 The smallest undecided instance

A triple `a₀, a₁, a₂: p → q` in a total category: is `aug(K₁ ∩ K₂) = ℤ`, `K_i = {t ∈ ℤ[A(q,−)] : t(a_i − a₀) = 0}`? Under
totality this is equivalent to `Tor₁^{ℤA}(Δℤ, P_q/(K₁ + K₂)) = 0` (F2), while totality already gives
`colim K ≅ ℤ²`, `L_i colim K = 0` for `K = ker(P_q² → P_p)`, `colim K_i ≅ ℤ`, `L_i colim K_i = 0`. In one-relator form the
smallest undecided relations are trinomials, e.g. `z = 2c₀ − c₁ − c₂` (the affine pair `(2c₀ − c₁, c₂)`). A positive answer
for triples would not yet give Part A (§2.5); a negative answer for one triple refutes it.

### 6.3 Every known restriction on a separator

A separator is a total category `A` with a finite family `a₀, …, a_k: p → q` (necessarily `k ≥ 2`) without simultaneous affine
equalizer. Then:
1. `A` is quasi-filtered: common successors, span completion, affine equalizers of pairs (R4; IM 1976 conditions I and IV ⟺ I
   and V by their Lemma 2.1). All element components are simply connected (B.6).
2. No weakly terminal object (IM 1976 Cor. 4.4; R5), hence infinitely many objects; not a monoid; not a preorder.
3. Not filtered, not sifted (D.4), in no `𝒯_n`, `n ≥ 1` (D.10 with `ΠA ≃ *`).
4. **`A(q, p) = ∅`** for the failing family, and no object reachable from `q` maps to `p` (mine, from IM 1976 Cor. 4.3: under
   IV every finite family in `A(p, q)` is equalized by an actual arrow as soon as `A(q, p) ≠ ∅`).
5. **`sup_X |A(p, X)| = ∞`** (IM 1976 Prop. 4.5/Cor. 4.6, due to Adámek–Reiterman: with I and V, a bounded indecomposable
   `A(p,−)` satisfies II, which equalizes the family by actual arrows).
6. Every finite family of endomorphisms of an object is equalized, together with the identity, by an actual arrow (IM 1976 Cor.
   4.3).
7. **Without loss of generality `p` is weakly initial** (mine): the full cosieve `U_p` of objects receiving an arrow from `p` is
   total (D.23) and contains every possible equalizer, so it is again a separator. Likewise the cosieve `U_q` is total and not
   exact.
8. `A` is not a final image of an exact category (D.22), so not of a filtered category, `Δ_inj^r × I` or `W_m`; it is not
   obtained from exact categories by finite products, opfibrations with exact base and fibres, idempotent completion,
   localization or filtered colimits along final functors (D.21–D.26).
9. If it is the union of a chain of finite stages built by attaching new maximal objects, every `H_n` class of every element
   category must die at a later stage (C.5): stage-by-stage permanence would contradict totality.

### 6.4 Candidates

| Candidate | Known | Unknown |
|---|---|---|
| AKR `K*` (Construction C.1, repaired as in TOTEX C.1) | quasi-filtered; `v₁, v₂, v₃` have no simultaneous affine equalizer, even rationally (AKR Th. C.2: any `r` distinct maps `W → X` cover `> 3r/2` points, while a triple equalizer forces `≤ 3r/2`); no `ℚ/F₂/F₃` equalizer at any object of the computed stages (F11); `H₂(El(h_V/(cv₁∼cv₂))) = ℤ` at `K₁`, injecting into all of `K₂` (C.3) and surviving a selected `K₃` attachment | whether the class survives to `K*` (if it does, `K*` is not total and is no separator — R10's expectation) |
| General B.9 completions (literal common-`n`, violating (11)) | an `H₂` class dies at a selected `K₂` attachment (`ℤ³ → ℤ²`, kernel `ℤ`), and the triple still has no equalizer there (F11) | whether AKR's invariant (c_m), (d_m) survives without (11); totality of any completion |
| `Ty^op` (Grothendieck's interval types, VII ms. 25–31; PRETOT E.1, F.12) | not filtered (PRETOT F.12); not sifted (PRETOT review); initial object (the empty type); directed preorder; the F.12 pair has the affine equalizer `h₁ + h₂ − h₃` (verified by hand); **the full subcategory on alternating types is isomorphic to the alternating part of `W₂`** (for alternating `ρ`, `Ty(τ, ρ)` is the set of sign-preserving subword embeddings `ρ ↪ τ`), which is total and exact by E.2's lift with the alternating target `(+−)^N`; the F.12 pair lies there; the inclusion of the alternating part is **not final** (over `(++)` the comma category splits according to whether vertex 1 is hit), so exactness of `Ty^op` does not follow (F13) | totality; `Aff_ℤ`-filteredness on families involving the stretch maps (a letter covering a run, e.g. `(+) → (++)` in `Ty`) |
| Monomial / substitution variants of `Δ_inj`, `W_m` (expert's H1) | every example built so far is exact by a lifted affine cone | a family where the cone lift fails while totality holds |
| A "free total completion" of the triple `p ⇉⇉⇉ q` | not constructed | everything |

### 6.5 Lines of attack for the next prompt

**For a proof.**
- **P1 (exact module target).** Prove `T₁(P_q/(K₁ + K₂)) = 0` for total `A` (F2), by exhibiting `P_q/(K₁+K₂)` (or a module
  surjecting onto `ℤ/ε(K₁∩K₂)` in `T₁`) as built from permutation modules of a total category obtained from `A`: `A × A`,
  components of `El_A(H₃)` and of iterated element categories, cosieves, `Kar`, localizations (all total by D.21–D.25). Note
  `P_q/K_i ≅ J_i = im(·(a_i − a₀)) ⊂ P_p` and `J_i = ker(P_p → ℤ[H_{0i}])`; the target is the pushout `J₁ ⊔_{P_q} J₂`.
- **P2 (one relator).** Prove `T₁(P_p/⟨z⟩) = 0` for the trinomial `z = 2c₀ − c₁ − c₂` (affine pair `(2c₀ − c₁, c₂)`), then
  by induction on the support of `z`; the binomial case is R4.
- **P3 (integrate the null-homology).** Totality kills the 2-sphere class `κ = (ρ₁ − ρ₃, ρ₃ − ρ₂) ∈ H₂(El H₃)` (expert's H1)
  and `T₁(K) = H₃(El H₃)`; analyse a bounding 3-chain and extract an element of `K₁ ∩ K₂` of augmentation 1, or show that
  bounding chains carry no such element (that would describe the counterexample).
- **P4 (dual certificates).** No rational equalizer of the triple at `r` ⟺ there are `φ₁, φ₂: A(p, r) → ℚ` with
  `φ₁(ca₁) − φ₁(ca₀) + φ₂(ca₂) − φ₂(ca₀) = 1` for all `c: q → r`. Such potentials pull back along arrows; a compatible family
  is impossible (it would be constant on the connected `p/A`). Rational failure is a system `r ↦ P(r)` of non-empty affine
  spaces with empty limit. Prove that totality forces a compatible family (a Mittag-Leffler / `lim¹` argument) — AKR's counting
  proof is such a certificate, for a non-total category.

**For a counterexample.**
- **C1 (settle `K*` first).** For a new quasi-filter element `(Z, h)` over `f, g: R → S`, the link is the union of the
  contractible sieves `U_i ≅ El/(S, h_i)` (when `H(α_i)` is injective); if AKR's (9)–(11) make consecutive intersections
  slices of `R`-elements and non-consecutive ones empty, every link is homotopy equivalent to a graph, `H₂` classes never die
  (C.5), and `K*` is not total. The computed relative homology (circles at the two `K₁` targets, zero at the selected `K₂`,
  `K₃` attachments) fits. Prove or refute this link lemma; then test it at the full `K₃` (smallest open stage).
- **C2 (expansion invariant + higher quasi-filters).** Build a total category inside finite sets and injections containing
  `K₀ = (V ⇉⇉⇉ W)` that keeps AKR's inequality (C.2(a)): any `r` distinct maps `W → X` cover more than `3r/2` points. Kill each
  `H_n` class of each element category by a "higher quasi-filter" (copies of an old object indexed by a cell structure of a
  ball, glued along the boundary sphere) and control the loss in the expansion constant as AKR do with `a_m → a_{m+1}`.
  Smallest test: the 2-sphere of `El(h_V/(cv₁∼cv₂))` at the repaired `K₁` (two disks over one circle), and the `ℤ⁴` of the
  triple quotient.
- **C3 (B.9 flexibility).** The literal common-`n` attachments kill `H₂` classes without creating triple equalizers (F11).
  Decide whether AKR's (c_m), (d_m) hold for such attachments, and whether all `H₂, H₃, …` of all element categories can be
  killed by them.
- **C4 (`Ty^op`).** Decide `Aff_ℤ`-filteredness by extending the coloured cone of E.2 to types with runs (the stretch maps),
  or find a family through `(++)`-type objects without affine equalizer; then decide totality.
- **Finite checks are useless** except as pieces of an infinite construction (R5, restriction 2). Every candidate must have a
  weakly initial object without loss of generality (restriction 7) and unbounded `|A(p, −)|` (restriction 5).

## 7. Limits of this review

The PDF was not opened. Not opened by me: Cegarra 2020, Husainov 2002, Badzioch 2002, Lurie HA, Gabriel–Ulmer 1971, Oberst
1968, Isbell 1968 and 1974; their statements were taken as the return gives them where used (none carries a decisive step).
AKR was read only on pp. 378–380 and 384–385. HTT 6.5.1.14 was located but not read; D.8 is standard. D.21–D.26 were followed but
not recomputed. The manuscript was checked only at II ms. 36, XII ms. 88 and 113. I did not recompute the coloured-word or
support-orbit counts with my own code (reruns identical). My Ty observations (F13) are proved in the review only for the
statements made; totality of `Ty^op` is not decided.

## 8. Findings

- **F1. No statement is wrong.** 44 correct, 1 correct with a gap (F.4), 7 known, 6 open as stated. Part A is not decided; the
  return used outcome (c).
- **F2. (Mine) The triple obstruction is exactly one Tor group.** For total `A`, `Tor₁^{ℤA}(Δℤ, P_q/(K₁+K₂)) ≅
  ℤ/aug(K₁∩K₂)`: R7's surjection is an isomorphism, because totality makes `colim K_i → ℤ` an isomorphism (pair quotients
  have `H₁ = H₂ = 0`).
- **F3. Isbell–Mitchell 1976 is open access** (ams.org; downloaded to `papers\IsbellMitchell1976.pdf`, read in full). It contains
  A.5 (Cor. 4.4, with Th. 4.1 = the argument of TOTASPH C.13) and D.14 (Remark p. 296), and asks the fixed-point form of Part A
  (p. 298), answered by AKR 1981 for the weaker hypothesis.
- **F4. (Mine) One-relator form of Part A.** Part A ⟺ `T₁(P_p/⟨z⟩) = 0` for every `z` of augmentation 0
  (`T₁(P_p/⟨z⟩) = ℤ/ε(ann z)`); totality gives the binomials. Triples are the smallest undecided instance but do not reduce
  Part A to themselves.
- **F5. (Mine, from IM 1976) Two new restrictions on a separator:** the failing family `p → q` has `A(q, p) = ∅` (Cor. 4.3), and
  `|A(p, X)|` is unbounded (Prop. 4.5/Cor. 4.6).
- **F6. (Mine) A separator may be assumed to have a weakly initial object** (the total cosieve `U_p`).
- **F7. D.4 = PRETOT F.3** (credited); **D.5 = PRETOT F.6** (not credited); D.3 = the expert's R8 note and PRETOT F.4 (CSV
  dependencies omit both). ARV Remark 1.1(i) is used correctly; the criterion is Gabriel–Ulmer's.
- **F8. D.10, restated:** for `n ≥ 1`, hocolims over `A` preserve `n`-types iff every comma category of the groupoid completion
  `A → ΠA` is filtered. `𝒯₁ = 𝒯₂ = ⋯`. Not found in the literature searched.
- **F9. D.7 is new for `n ≥ 2`;** `n = 1` is PRETOT F.6 + F.3.
- **F10. AKR 1981 has the defects TOTEX names** (scan read): sign misprints in Lemma B.5 (c), (d); the summand `(Y − Y₀) × I`
  for `s̄ × I` in B.6; and the false claim that (9)–(11) survive arbitrary domain–range restriction ((11) fails on a two-point
  path). Theorem C.2 is not affected for the repaired construction.
- **F11. (Mine, computed) The AKR triple stays unequalized at every computed stage**, over `ℚ`, `F₂`, `F₃`, including the
  literal B.9 substage where an `H₂` class dies; each pair is equalized exactly at its own targets. All of C.2–C.4 reproduced
  by independent code; the input of C.3 (`H₂(El_{D_T}) = 0` for the 17 objects of `K₁`) verified.
- **F12. C.7 is trivial** (adjoin a terminal object) and destroys the triple obstruction; the prompt's C.2 (the smallest
  modification of `K*` that becomes total, and whether the triple then acquires an equalizer) is not addressed.
- **F13. (Mine) `Ty^op` contains `W₂^alt`:** for alternating `ρ`, `Ty(τ, ρ)` is the set of sign-preserving subword embeddings of
  `ρ` into `τ`, so the alternating full subcategory of `Ty^op` is the alternating part of `W₂`, total and exact by E.2's lift with
  target `(+−)^N`; the PRETOT F.12 pair lives there. The inclusion is not final (comma category over `(++)` disconnected), so
  `Ty^op` itself stays undecided.
- **F14. The link lemma for `K*`** (§6.5 C1) would prove `K*` not total (R10) by showing `H₂` classes can never die in the
  repaired construction; it is the shortest route to settling C.1.
- **F15. Reruns identical** (14 runs, modulo CR/LF); my code reproduces every AKR count and Betti number over four primes.
- **F16. Charney–Davis citations are exact** (Th. 3.1.1, Rem. 3.1.2, Lemma 3.1.3, Prop. 3.2.1, pp. 11–12); the infinite-graph
  extension is the return's own and correct. **BKL citations are exact** (Th. 9.3, Cor. 9.5, pp. 28–30).
- **F17. Manuscript readings checked:** II ms. 36 (`y∖X` for the printed `y∖Y`), XII ms. 88 (`U'/H'`), XII ms. 113 (already
  corrected in the transcription).
- **F18. Unopened sources remaining:** Oberst 1968, Gabriel–Ulmer 1971 (needed before any novelty claim for N1–N3),
  Isbell 1968, Isbell 1974.
