# BISITE: review by the author of the prompt

Claude (Fable 5.2, Anthropic), 11 November 2026, written about 13:30–14:00 UTC. Review of the answer of GPT-6 Astra (ChatGPT Pro mode) to prompt `7_BISITE` (AI-produced; 126 statements: 72 Proved, 32 Refuted, 18 Known, 4 Open), read against the four leads of the prompt, the items carried from POLES, GALOIS, STRATA and PATHS, the expected answer for Part B recorded in `6_PATHS/REVIEW_author.md`, and the companion's audit of XII ms. 207–227, XVI ms. 1–3 and the rows named below.

## What I read and checked

Read in full, proofs included: `BISITE_report.md`, `README.md`, `sections/A.tex` (A.1–A.34), `sections/B.tex` (B.1–B.22), `sections/E_b062.tex` (E.11, E.12), and the proofs of D.2 (to the end of the induction on downsets), E.3, E.6, F.2, F.19, G.2, and F.16 up to the case of a general multicurve. For every other statement of Parts C–G I read the statement in the register (first 560 characters) and the report's account of the proof; **those proofs were not read** and the tables below say so statement by statement. Nothing in `code/` was opened or run.

Checked against the transcription (`checks/DER_XIIc-a/DER_XIIc-a_text.tex`, `checks/DER_XVI/DER_XVI_text.tex`): XII ms. 215–218 (axioms a, b, the question about c), ms. 220 (the classes `W_S^𝓛`), ms. 222 (`𝓛^`, "J'ignore s'il est égal"), ms. 225–226 ("tels que (peut-être) `Liss ∩ Prop ⊆ Fib_W`"; clauses a, b, c); XVI ms. 1–3 (Loc (1) with a, b, c; Loc (1 bis), (1 ter), (2), (3), (3 bis); Définition 1.1). The readings of A.1, A.10, A.13, A.14 and A.32 agree with the text. Not checked against the text by me: II ms. 65–89, VI ms. 81–84, XII ms. 221, 223–224, 240–248, 273–275, XIII, XVI §4, I ms. 79–81, 102, 117–123.

No cited source was opened in this review. Opened in the PATHS review and used here: Cisinski 2006, 5.3.1, 5.3.2, 5.3.4, 4.2.19; Maltsiniotis 2005, 1.1, 1.2.

Own checks: `checks_author/check_bisite.py`, output `check_bisite.out`, written from the statements.
1. E.12 (row XIIc B062): the six-element lattice; all meets; `W` has two-out-of-three; the table of intrinsic fibrations over the six bases is as stated (`{0}`, `{0,1}`, `{0,2}`, `{0,3}`, `{0,1,4}`, `{0,3,5}`); axiom (b) at every base; `R`, `T` monotone, preserving `W`, with components `T(x) → x` and `T(x) → R(x)` in `W`; `W` is exactly the set of arrows that `R` sends to identities; inside `{0,3,4,5}` no non-identity arrow is weak and 3, 4 are incomparable; `4 → 5` has no factorization as a weak arrow followed by an intrinsic fibration.
2. A.8: `T_W(A)` is all arrows except `1 → 3`; `K_W T_W(A) = A`.
3. B.12: `K` has 14 objects and 50 arrows, `H` has 100 arrows and 1,552 composable triples (all associative), `H ×_K H` has 200 arrows and 12,416 triples; every arrow of `H` is cartesian and cocartesian; the cochain is non-zero on exactly one of the 24 triangles of `BK`, each edge lies in two triangles, the Euler characteristic is 2; `dim H¹(−; F_2)` is 0, 0, 1 for `K`, `H`, `H ×_K H`.
4. B.10 (`n = 0`), A.32: the comma category `E/c` has 4 objects, 8 arrows and 2 components; `E × BC_2` is connected with `H¹(F_2)` of dimension 1 and `E` has dimension 0.
5. B.11: in `S_3` the image of `y x y x⁻¹ y⁻¹` is `(12)`; the orbits are `{1,2,3}` before and `{1,2}`, `{3}` after.
6. B.7: every lifting poset of the four-element poset over `[1]` has a greatest element, the one from `x` over `0 → 1` has no least element; for `V`: `ps = 1`, `sp ≤ 1`, and `b` has no outgoing lift.
All counts agree with those the answer reports.

Verdict words: **proved** (followed step by step, complete given the named inputs); **proved in outline** (followed, no gap found, cited machinery not unfolded); **known** (a citation; not opened in this review unless said); **statement checked** (the proof was not read, and I verified the statement by an argument of my own, given in a few words); **unverified** (read, not checked); **false**.

## Summary

**No statement labelled Proved, Known or Refuted was found false**, and I found no gap in a proof I followed. Parts A and B are followed in full; of Parts C–G I followed eight proofs and checked about twenty further statements by short arguments of my own or on an example; 44 statements are unverified (list after the tables).

The return against the expected answer for Part B: it confirms it and goes further.
- `W∞`-smooth and proper implies `W`-smooth and proper for every `W` (first lines of the proof of B.9): as in the PATHS review.
- `Liss_W ∩ Prop_W ⊂ Fib_W` **holds exactly for `W = W∞` and for the class of all functors** (B.9), with no accessibility hypothesis. I followed the proof: a factorization of every functor as a `W∞`-equivalence followed by a `W∞`-smooth and proper functor makes `W` stable under homotopy pullback; a non-contractible `W`-aspherical fibre is looped until it is disconnected; two points in different components have empty homotopy pullback; then `∅ → e` is in `W` and `W` is everything. The coarse localizer (non-empty categories aspherical) is covered: the inclusion fails there by a component inclusion.
- The cases named in the expectation are each given: `W_0` (B.10, the covering `EC_2 → BC_2`), every homology localizer including non-connective spectra (B.11), rational homology (B.13, the path functor over `C_2`).
- **The case `W_n`, `n ≥ 1`, which the PATHS reviewer had added and nobody had checked, is confirmed twice**: by the general theorem B.9 and by B.10, which uses the same example (the path functor over the face poset of the boundary of an `(n+2)`-simplex; `π_n ΩS^{n+1} = Z`).
- New beyond the expectation: a **finite** witness for `W_1` and for the localizer of rational local systems (B.12: a central `C_2`-extension of the face poset of the tetrahedron boundary, 14 objects and 100 arrows, a bifibration); coverings **are** in `Fib_{W_1}` and in `Fib` of the rational local-system localizer (B.13), so the homology witnesses do not serve for these; the simplicial version (B.22).

Main new results (not known to us before this return):
1. **Row XIIc B062 is answered: no** (E.12 = A.13). His axioms (a) and (b), at every base, do not imply (c); a six-element lattice. Followed by hand and reproduced by program.
2. **Row XIIc-a C023 is answered: yes** (B.6). `𝓛^ = Liss_W` for every fundamental localizer; dually the maximal class for the other variance is `Prop_W`. Followed in full; it rests on Maltsiniotis 2005, Théorème 1.2 (c).
3. **Row XIIc-a C033**: the threshold theorem B.9 above.
4. **POLES A.16 is answered: no** (A.32). The literal Loc (1), (2), (3) of XVI ms. 1–2, that is Grothendieck's Définition 1.1 of a localiseur fondamental, do not imply Loc (3 bis): the class `W†` (bijection on components, and a weak equivalence when the source is connected) with a triangle of finite groupoids over `BC_2`. Followed in full and reproduced. The class is not closed under retracts; with Loc (1 bis) or (1 ter) the question stays open.
5. The two fine localizations of `Cat/S` are `Fun(NS^op, Spaces)` (tests `s\X`) and `Fun(NS, Spaces)` (tests `X/s`), as localizations of ∞-categories, by explicit inverse relative functors (B.3); the literal slice recipe is false over a non-fibrant simplicial base (B.4, over `Λ²_1`) and true with the covariant and contravariant structures (B.22).
6. The uniform theorem of XIII ms. 57–72 holds under its own hypotheses: a closed exact weak Quillen structure is a closed model structure (A.27), and every functor whose ordinary right Kan extension exists is admissible (A.28). I followed A.27 and A.28; the reading of XIII ms. 57 was not checked by me against the text.
7. Topological spaces: over a finite Alexandrov base the localization of `Top/P` at the maps that are weak equivalences over every open set is `Fun(P, 𝒮)`, cosheaves (D.2, followed); strict pullback along a proper map does not preserve the class (D.4: `(0,1] → [0,1]` and the point `0`; verified by hand); the general base is open (D.12).
8. Six operations: the two base-change theorems with converses by lifting categories (F.2, followed); a correspondence formalism on the smooth class (F.10, unverified) that is not a geometric set-up in the later convention (F.12), and in the discrete-fibration set-up the cohomologically proper maps are exactly the finite discrete bifibrations (F.19, followed).
9. Lead 4 corrected: the dualizing datum is a covariant spectral weight acting by a coend (G.2, followed; on `[1]` I recomputed `w = (0 → S)` and `p_* F = F(1)`), not a pointwise twist (G.3, verified by hand); the canonical transform is an equivalence exactly under Aoki's criterion (G.9, known, not opened).

What the answer says about the leads: Lead 1 true over quasicategorical bases and with the model structures, false with literal slices over arbitrary simplicial sets; Lead 2 proved for finite Alexandrov bases, its raw-pullback reading for proper maps false, the general statement open; Lead 3 true with its qualifications (projection formula only for smooth maps or locally constant second argument: F.4, F.5); Lead 4 false as a pointwise twist, true as a weighted colimit.

Remarks, none an error in a statement:
1. B.6 defines the maximal class with respect to the tests `X/s`. That this is the class `W^g = W^𝓛` of XII ms. 222 uses that the "isomorphismes locaux" contain the functors `S/s → S` and are `W`-smooth; I did not read ms. 221, where they are defined. The text at ms. 222 itself says that `𝓛^` contains `Liss_W`, which agrees.
2. E.12 has no factorization of `4 → 5` through an intrinsic fibration; the answer says so. Grothendieck's question at ms. 217–218 does not assume one (checked), and his footnote 123 points to ms. 240 ff. where more is assumed. So the row is answered as asked; with "enough intrinsic fibrations" added the implication is open (E.11 proves it with a coaugmented replacement functor).
3. A.32: `W†` satisfies the weak saturation of Maltsiniotis and Cisinski (identities, two-out-of-three, the split-retraction clause), so it is a "localisateur fondamental faible" in their sense that is not a fundamental localizer. Whether such an example is in the literature I do not know; the answer reports a limited search and claims no novelty. To be checked before anything is said about it in public.
4. The π_1 computation in B.12 by Tietze moves is in the answer's code, which I did not run. My check is `H¹(−; F_2)`, which decides it given the exact sequence of the bifibration (the groups are quotients of `C_2` and `C_2²`): trivial and of order 2, as stated. Equivalently the cocycle evaluates to 1 on the fundamental cycle of the sphere, so the extension class generates `H²(S²; Z/2)`.
5. "Known" in B.17, D.6–D.8, G.9, G.12, F.13, F.15 means a citation I did not open.

## The inference of the PATHS review, against the return

| Expected | Return | Verdict |
|---|---|---|
| `W∞`-smooth and proper ⇒ `W`-smooth and proper, all `W` | B.9, first lines; B.19 | agrees |
| inclusion holds for `W∞` | B.7 | agrees; also strictness of both inclusions |
| fails for `W_0` | B.10 | agrees, same example |
| fails for rational homology | B.13 | agrees, same example (PATHS E.9) |
| fails for every homology localizer | B.11 | agrees, same example (POLES C.10), non-connective spectra included |
| fails for `W_n`, `n ≥ 1` (reviewer's addition, unchecked) | B.9, B.10 | **confirmed**, same example |
| "only `W∞` and the class of all functors" (suggested by POLES E.5, STRATA G.5) | B.9 | **proved**, without accessibility |

## Verdicts, statement by statement

### Part A (the proposal and its premises)

| Id | Label | Verdict |
|---|---|---|
| A.1 | Proved | **Proved**; checked against XVI ms. 1–3. |
| A.2 | Proved | **Proved.** |
| A.3 | Proved | **Proved**; the classes are those of XII ms. 220 (checked). |
| A.4 | Proved | **Proved.** |
| A.5 | Proved | **Proved**; the second definition of ms. 222 (checked). |
| A.6 | Proved | **Proved** (the Galois connection; both directions followed). |
| A.7 | Proved | **Proved.** |
| A.8 | Refuted | **Proved**; check 2. II ms. 86 not opened. |
| A.9 | Proved | **Proved** as mathematics; the definitions at II ms. 66, 89 not opened; "peut-être" at ms. 225 checked. |
| A.10 | Proved | **Proved**; the three axioms checked against ms. 215–218. |
| A.11 | Proved | **Proved.** |
| A.12 | Proved | **Proved.** |
| A.13 | Refuted | **Proved** (= E.12); check 1. |
| A.14 | Proved | **Proved**; ms. 225–226 checked ("une pure tautologie" for clause a). |
| A.15 | Proved | **Unverified** against XVI §4 (a reading; the POLES review covers the same ground). |
| A.16 | Proved | **Proved.** |
| A.17 | Proved | **Proved**; the mapping-path argument followed in full, with the identities `fq = g(w^*f)` verified. |
| A.18 | Refuted | **Proved** (GALOIS D.3, followed in the GALOIS review; reread). |
| A.19 | Proved | **Proved in outline.** |
| A.20 | Refuted | **Proved** (by hand). |
| A.21 | Proved | **Proved.** |
| A.22 | Proved | **Proved**, given the reading of XIII ms. 8, 10 (the PATHS review checked ms. 7–10). |
| A.23 | Proved | **Proved.** |
| A.24 | Refuted | **Proved** (by hand). |
| A.25 | Proved | **Proved**; followed in full. |
| A.26 | Refuted | **Proved** (as PATHS D.9). |
| A.27 | Proved | **Proved**; the retract argument followed. |
| A.28 | Proved | **Proved**, given the reading of the hypothesis of XIII ms. 57, which I did not check. |
| A.29 | Proved | **Proved**; II (5.20) not opened. |
| A.30 | Refuted | **Proved** (by hand). |
| A.31 | Proved | **Proved in outline** (a reading; ms. 222 and 225 checked, VI ms. 81–84 and XII ms. 224 not). |
| A.32 | Refuted | **Proved**; followed in full, check 4. |
| A.33 | Refuted | **Proved** for the example (by hand); its fit with Théorème 3° of XII ms. 274 not checked (POLES G.17–G.18 has the same correction). |
| A.34 | Refuted | **Proved** (by hand). |

### Part B (categories and simplicial sets)

| Id | Label | Verdict |
|---|---|---|
| B.1 | Proved | **Proved.** |
| B.2 | Known | **Known**, not opened (Cisinski 2019, 4.4.29–4.4.30, 4.4.14); the reduction read. |
| B.3 | Proved | **Proved in outline**: the functor `T(K) = Δ/K`, the identification `T(K)/s ≅ Δ/(K ×_{NS} N(S/s))` and the two natural transformations followed; the last-vertex equivalence and straightening are cited. |
| B.4 | Refuted | **Proved** (the simplices of `(Λ²_1)_{/2}` computed by hand). |
| B.5 | Known | **Known**, consistent with what the PATHS review opened (Cisinski 2006, 5.3.1–5.3.4) and with HTT 4.1.2 from memory; Cisinski 2019, 4.4.36 and its errata of July 2026 not opened. |
| B.6 | Proved | **Proved**; followed in full (the functor `j_X`, its comma categories, the square with three sides in `W^co`). |
| B.7 | Proved | **Proved** for categories; check 6. The first example is STRATA D.6. The simplicial sentence rests on Cisinski 2019, 4.6.2, 4.6.5, not opened. |
| B.8 | Proved | **Proved**; the initial objects of the stages and the filtered union followed (it is PATHS E.4–E.5 for a fixed left end). |
| B.9 | Proved | **Proved**; followed in full. The factorization can be taken from B.19 instead of Cisinski 2006, 5.3.14. |
| B.10 | Refuted | **Proved**; check 4. |
| B.11 | Refuted | **Proved**; check 5. |
| B.12 | Proved | **Proved**, with the π_1 statement verified through `H¹(F_2)` and the exact sequence (check 3, remark 4); the criterion for rational local systems rests on Rivera–Wierstra–Zeinalian, Theorem 3, not opened (the GALOIS review derived the simply connected case, which is all that is used for `p` itself). |
| B.13 | Proved | **Proved in outline.** |
| B.14 | Refuted | **Proved** (both examples followed). |
| B.15 | Proved | **Unverified** in its table (8 rows, 3 columns); the constructions were read. |
| B.16 | Proved | **Proved in outline**; Cisinski 2019, 7.9.8 with its hypotheses not opened. |
| B.17 | Known | **Known**, not opened (Cisinski 2006, 6.2.3, 9.2.1, 9.2.15); the elementary case `n = 0` followed. |
| B.18 | Proved | **Proved.** |
| B.19 | Proved | **Proved** (= PATHS E.4, E.5, reproved). |
| B.20 | Refuted | **Proved** (= PATHS E.3, reproved; the smoothness argument is new and followed). |
| B.21 | Open | Open (= STRATA E.11 = PATHS E.11). See FOLLOW_UPS, item D1, for a partial result of this review. |
| B.22 | Proved | **Proved in outline**; rests on Cisinski 2019, 4.4.4, 4.4.18. |

### Part C (presheaf categories; strict higher categories)

| Id | Label | Verdict |
|---|---|---|
| C.1 | Proved | **Unverified** (formal; statement read). |
| C.2 | Refuted | **Statement checked**: `A/X → A/S` is a discrete fibration, so `s\(A/X)` retracts onto the discrete fibre, and a `W_0`-equivalence there is a bijection; `(A/X)/s` is the category of elements of the pullback to a representable. |
| C.3 | Refuted | **Statement checked** for the first two sentences (a discrete fibration is smooth; its outgoing lifting categories are discrete sets); the sentence on autoequivalences of simplicial sets unverified. |
| C.4 | Proved | **Unverified** (formal). |
| C.5 | Known | **Unverified citation** (Ara–Maltsiniotis). |
| C.6 | Proved | **Unverified.** |
| C.7 | Proved | **Unverified.** |
| C.8 | Known | **Unverified citation** (Ara–Maltsiniotis, Theorem 6.27, Corollary 6.32). |
| C.9 | Proved | **Unverified**; conditional on the unrefereed claim above dimension two, as the statement says. |
| C.10 | Open | Open. |

### Part D (topological spaces)

| Id | Label | Verdict |
|---|---|---|
| D.1 | Known | **Unverified citation** (HA 5.5.5, A.3). |
| D.2 | Proved | **Proved in outline**: the adjunction `D ⊣ E`, the continuity of the jump homotopy on both kinds of generators and the induction on downsets followed; the rectification step is HTT 4.2.4.4. |
| D.3 | Refuted | **Statement checked** (`Fun(P, 𝒮)` and `Fun(P^op, 𝒮)` are not equivalent for the three-element fork; not computed beyond that). |
| D.4 | Refuted | **Statement checked** (by hand: over every open set of `[0,1]` the inclusion `(0,1] → [0,1]` is a weak equivalence; over the point `0` it is `∅ → pt`). |
| D.5 | Proved | **Unverified.** |
| D.6 | Known | **Unverified citation** (HTT 7.3.1.18; Volpe). |
| D.7 | Known | **Unverified citation** (Volpe 2025, 3.23–3.27). |
| D.8 | Known | **Unverified citation** (HA 5.5.5.1; Volpe 6.9). |
| D.9 | Refuted | **Statement checked** on `{0} → [1]` (a skyscraper at the open end is not constructible for the least-vertex strata). |
| D.10 | Proved | **Unverified** (STRATA D.8; reviewed there). |
| D.11 | Proved | **Unverified.** New and not small: the comparison for every proper map of finite posets. Checked by hand on `{1} → [1]` and on `[1] → e` only. |
| D.12 | Open | Open. |
| D.13 | Proved | **Unverified.** |

### Part E (the abstract theorem)

| Id | Label | Verdict |
|---|---|---|
| E.1 | Proved | **Proved** (= A.3, A.4). |
| E.2 | Refuted | **Statement checked** (by hand: `0\{1} → 0\[1]` is `e → [1]`). |
| E.3 | Proved | **Proved**; followed. The hypotheses are strong (compact projective generators that jointly detect equivalences), and the answer says that none follows from the factorization axioms. |
| E.4 | Proved | **Unverified.** |
| E.5 | Proved | **Unverified** (instances; depends on B.3, D.2). |
| E.6 | Refuted | **Proved**; followed. |
| E.7 | Proved | **Proved** (the non-formal step is A.11). |
| E.8 | Known | **Known** (Cisinski 2006, 5.2.15, 6.1.11; POLES E.2, followed in the POLES review). |
| E.9 | Proved | **Unverified** (formal; consistent with B.19). |
| E.10 | Proved | **Unverified.** |
| E.11 | Proved | **Proved** (= A.11, A.12). |
| E.12 | Refuted | **Proved**; followed in full, check 1. |
| E.13 | Refuted | **Statement checked** (PATHS D.20, STRATA C.7). |
| E.14 | Proved | **Unverified** (rests on Rijke–Shulman–Spitters 2020). |

### Part F (six operations)

| Id | Label | Verdict |
|---|---|---|
| F.1 | Known | **Unverified citation** (Groth 2013, 1.5). |
| F.2 | Proved | **Proved in outline**; the fibre formulas and the converse through the left mate followed; I checked the variance on prefibrations and on `{1} → [1]`. Agrees with STRATA D.3–D.4. |
| F.3 | Refuted | **Statement checked** (endpoint inclusions, as E.2). |
| F.4 | Proved | **Unverified.** |
| F.5 | Refuted | **Unverified.** |
| F.6 | Proved | **Unverified**; its counterexample checked (two points and a two-element set: 2 against 4). |
| F.7 | Proved | **Unverified** (mates). |
| F.8 | Proved | **Statement checked** (formal). |
| F.9 | Known | **Unverified citation.** |
| F.10 | Proved | **Unverified.** The coherence of the correspondence functor is asserted from uniqueness of adjoints; Mann 2022, A.5 not opened. The statement most in need of a second reader in Part F. |
| F.11 | Proved | **Unverified.** |
| F.12 | Refuted | **Statement checked** for the diagonal of `[1]` (not smooth: the object `1` has no incoming lift over the arrow `(0,1) → (1,1)`, since no object of `[1]` maps to `(0,1)`); Heyer–Mann 2024 not opened. |
| F.13 | Known | **Unverified citation** (Hörmann 2017, 6.12). |
| F.14 | Proved | **Unverified.** |
| F.15 | Known | **Unverified citation** (Jansen 2023; the STRATA review opened 3.18, 3.23, 6.6, 6.7). The answer takes the entrance category as the opposite of Jansen's; to compare with STRATA Part F when integrating. |
| F.16 | Proved | **Unverified** beyond the reduction to the poset of refinements and the tree argument for `σ = ∅`, which I followed; the kernel of `Z² → Z` is `Z` (trivial). Agrees with STRATA F ("proper and not smooth"). |
| F.17 | Proved | **Unverified.** |
| F.18 | Open | Open. |
| F.19 | Proved | **Proved**; followed (the two fibre computations redone), given Heyer–Mann 4.6.1–4.6.4, not opened. |

### Part G (duality on finite bases)

| Id | Label | Verdict |
|---|---|---|
| G.1 | Known | **Unverified citation** (Groth–Shulman 2.14; Cisinski–Tabuada A.11). |
| G.2 | Proved | **Proved in outline**; recomputed on `[1]`. |
| G.3 | Refuted | **Statement checked** (by hand: the presheaf `(M → 0)` on `[1]` has limit `M` and every pointwise twist has colimit 0). |
| G.4 | Proved | **Unverified.** |
| G.5 | Refuted | **Unverified.** |
| G.6 | Proved | **Unverified** (pointwise duality on finite objects). |
| G.7 | Refuted | **Statement checked** (homotopy fixed points of `C_2` over `F_2` do not commute with countable sums: the classical statement). |
| G.8 | Proved | **Statement checked** (the norm with `|G|` invertible). |
| G.9 | Known | **Unverified citation** (Aoki 2022); on `[1]` the criterion fails at `P_{>0}` = a point and `V_P F = (0, F(1))` is not an equivalence, which agrees. |
| G.10 | Proved | **Unverified** (STRATA A.4; the coarsening step was unverified there as well). |
| G.11 | Refuted | **Statement checked** for the second half (previous row); the first half unverified. |
| G.12 | Known | **Unverified citation** (Aoki, Theorem 6.13). |
| G.13 | Refuted | **Unverified.** |
| G.14 | Known | **Unverified citation** (Groth–Šťovíček 9.19, 9.23). |

Counts: 126 statements. Confirmed by this review, with the qualifications in the tables: 78 (Part A 33; Part B 20, of which B.2, B.5 and B.17 are citations not opened here; Part C 2; Part D 4; Part E 9; Part F 5; Part G 5). Of the 78, 20 in Parts C to G are "statement checked" or checked on an example without the proof having been read. Unverified: 44 (A.15; B.15; C.1, C.4 to C.9; D.1, D.5 to D.8, D.10, D.11, D.13; E.4, E.5, E.9, E.10, E.14; F.1, F.4 to F.7, F.9 to F.11, F.13 to F.17; G.1, G.4 to G.6, G.9, G.10, G.12 to G.14). Open in the answer: 4 (B.21, C.10, D.12, F.18). False: none.

## Corrections to my leads and to earlier records

- Lead 1: true over quasicategories and for nerves of categories; the literal slices are wrong over a general simplicial base (B.4); the nerve comparison is an equivalence of localizations, not a Quillen equivalence (B.3).
- Lead 2: the raw-pullback reading for proper maps is false (D.4); sheaves and cosheaves of spaces are not exchanged unstably (D.3); proved only over finite Alexandrov and discrete bases (D.2).
- Lead 3: "the projection formula holds when **D** is monoidal" needs `f` smooth or the second argument locally constant (F.4, F.5).
- Lead 4: "limits are colimits twisted by a dualizing object" is false pointwise (G.3); the weight is covariant and acts by a coend (G.2); "finite EI" needs the group orders invertible (G.7, G.8).
- The handoff says of STRATA that Kan extensions are topological direct images "only for closed inclusions and product projections". STRATA D.8 proves it for those; BISITE D.11 claims it for every proper map of finite posets. The word "only" in the handoff is not a theorem; D.11 is unverified.
- `6_PATHS/REVIEW_author.md`, "the `W_n` case is mine and unchecked": now checked (B.9, B.10).
- POLES A.16 was "open": refuted for the literal axioms (A.32).

## What is left

- Open in the answer: B.21 (a strict bifibration over the five-element monoid), C.10 and F.18 (strict higher categories), D.12 (`Top/Y` for `Y` not Alexandrov; first case the real line).
- Left by the answer's own qualifications: B062 with enough intrinsic fibrations added; Loc (1 bis), (2), (3) ⇒ Loc (3 bis); minimality of the six-element example among all finite categories.
- Not verified by me: the 44 statements listed above; every cited source of this return; the code; the readings of II, VI, XIII and XVI §4.
- The follow-up list is `FOLLOW_UPS.md`; the integration list is `COMPANION_INTEGRATION.md`; the seven returns together are in `COMBINED_REVIEW.md`.
