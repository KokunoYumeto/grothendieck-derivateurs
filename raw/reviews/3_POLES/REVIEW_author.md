# POLES: review by the author of the prompt

Claude (Fable 5.2, Anthropic), 11 November 2026. Review of the answer of GPT-6 Astra (ChatGPT Pro mode) to prompt `3_POLES` (104 statements: 75 Proved, 14 Refuted, 13 Known, 2 Open), read against my six leads and against the companion's audit of XII and XVI, which was made in separate runs of the same model and already contains part of what the answer finds.

## What I read and checked

Read: `POLES_report.md` in full; `POLES_results.csv` (all 104 statements in short form, 38 in full); `sections/B.tex` and `sections/D.tex` in full with their proofs; the proof of E.4 as far as its reduction to Cisinski's theorems; the companion's XVI blocks at ms. 16′, 17′, 25, 27 (two blocks), 65, 87, 124 and the claim rows of XVI, XIIb-a, XIIb-b, XIIc-a (to ms. 209), XIIc-b that are open, conjectured or mention the reverse axiom; XVI ms. 79 and ms. 87–88 in the transcription. Not read: the proofs of Part A, of C.8–C.10, E.3, E.7, F.9–F.13, of Part G (G.26 in particular), of H.2–H.7; the PDF; the `research/` notes. Nothing in the answer's `code\` folder was run.

Own checks: `checks_author\check_poles.py`, output `check_poles.out`, written from the statements in B.tex, D.tex, F.tex with my own code.
1. The category `A` of B.7, built from its definition (face category of the cone triangulation of the presentation complex of `⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩`): 35 objects, 159 arrows; identities and associativity on all 677 composable triples; normalized nerve chains of ranks (35, 124, 90); integral homology `Z, 0, 0` by diagonalization over `Z` (no torsion). A functor from `A` to the group `A_5` built from `a ↦ (1 4 3 2 5)`, `b ↦ (1 2 3)`, verified on all 373 composable pairs, with non-trivial image: so `π_1(BA) ≠ 1`.
2. The two-cone category `X` of B.8: 37 objects, 231 arrows; `U = A ∪ {u}` and `V = A ∪ {t}` are sieves with terminal objects and `U ∩ V = A`; chain ranks (37, 194, 338, 180); integral homology of a point.
3. B.13: the four-object category `K(g)` for the fold of two points is connected with `H_1 = Z`.
4. F.8: `α(x) = x`, `α(y) = yxyx⁻¹y⁻¹` is the identity on the abelianization, and there are homomorphisms to `S_3` that agree on `x` and on `α(y)` and differ on `y` (`x ↦ (2 3)`; `y ↦ (2 3)` or `(1 2)`), so `α` is not surjective.
5. D.6: there are 456 monotone maps from the six-element circle poset to its subdivision and all have degree 0.
All counts agree with the answer's.

Verdict words: **proved** (I followed the argument step by step and found it complete, given the named classical inputs); **proved, with the part named unverified**; **unverified**; **false**.

## Verdicts on the central results

### 1. XVI Théorème 5.4 (ms. 79): false in one entry of its list; proved

The theorem says that `W∞` satisfies "tous les axiomes vus jusqu'à présent, savoir Loc (1 ter, 2, 3 bis, 4, 5, 6, 7, 8, 9)" and is `ℵ_0`-accessible. Loc (6) is by his own convention (XVI footnotes 11 and 13) the pair (6 a), (6 b). `W∞` does not satisfy (6 b), nor (6′ b), nor XII's W(7 bis) and W(7); so XII Théorème 2 (ms. 78) is false as well. The refutation (B.7, B.8) is complete and I reproduced it: with `A` connected, integrally acyclic and not simply connected, the two cones `U`, `V` on `A` are sieves covering `X = A ⋆ {u, t}`, `BX` is the suspension of `BA`, hence simply connected and acyclic, hence contractible; so `U → X` is in `W∞` and `A → V` is not, against W(7 bis) as printed at XII ms. 76 ("`A → V ∈ W` iff `U → X ∈ W`"); mapping the square to the constant square on `e` gives the failure of (6 b). The answer adds that the failure persists along a genuine Dwyer map (the cylinder of `A → e`, B.8 second half); I followed that argument and did not recompute its 141-object model.

What I did not check: that the rest of the list holds and the accessibility proof of ms. 80–83 as completed in G.22. These are standard for `W∞` (and the companion's block at ms. 79 completes the accessibility argument independently); I have no reason to doubt them.

The companion already has this verdict (row XVI-C021, false; row XIIba-A-058, false, with the same example on a larger poset). The answer and my check confirm it.

### 2. Loc (6 b) / W(7 bis) forces `W ⊃ W_Z`: proved

This was the unverified inference of the prompt (Leads 1 and 2). Both steps hold.

- B.5 (the cofibre criterion). For `g: A → B` the category `K(g)` (mapping cylinder `M_g` with a cone point `t` on the `A`-layer) is covered by the sieves `M_g` and `A ∪ {t}` meeting in `A`. If `K(g)` is `W`-aspherical then `A ∪ {t} → K(g)` is in `W`, the single-square reverse axiom gives `A → M_g ∈ W`, and `g` is its composite with the retraction `M_g → B`, which has a right adjoint. The converse direction (the criterion implies the cube forms (6 b) and (6 c)) goes through the square of pointed cofibres: three aspherical vertices give `C_3 ≃_W ΣC_0`, and the criterion applied to `C_0 → e` and then to `f_0` finishes. I followed both directions. Forward gluing (B.2) is by the relative Theorem A and is standard.
- B.6. A map `g` inducing isomorphisms on integral homology is bijective on components (the free abelian group on a function is an isomorphism only for a bijection); its cofibre is connected and acyclic; the suspension of the cofibre is simply connected and acyclic, so contractible; the criterion applied twice gives `g ∈ W`. Correct, empty and non-connected cases included.

The companion's block at XVI ms. 27 ("The least localizer satisfying reverse cube excision") proves the same inclusion by a different route: apply the cube axiom (6 b) directly to the two-cone cube of `f`, whose union map `Σf` is a homology isomorphism of simply connected spaces. I checked that argument too. It needs no cofibre criterion and works for weak localizers; it uses the cube form (6 b). The answer's route shows in addition that the single-square form (6′ b) suffices when the relative Theorem A is assumed. The two proofs are independent of each other in their middle step, which is some protection against a shared error.

### 3. `W_Z` is the least localizer with the reversible axiom: proved, with two corrections to the lead

D.1: `W_Z` is a fundamental localizer (relative Theorem A by the spectral sequence of the Grothendieck construction; the companion writes the same proof with an explicit double complex) and satisfies (6 a, b, c) by the short exact sequence of nerve chains of a sieve cover and the long exact sequence of the cones. With B.6 it is the least. I followed the chain-level argument for the cube axioms; the relative Theorem A for homology I take as classical.

Corrections to what I wrote in the prompt, both right:
- The localizers with the reversible axiom are **not** all the localizers containing `W_Z`. `W_0` contains `W_Z` and fails the criterion: the cofibre of the fold of two points is a circle, connected, while the fold is not in `W_0` (B.13; my check 3).
- "Loc (7) and Loc (6 b) together leave only the class of all functors" is right, and that class fails Loc (5); so with Loc (5) there is no localizer with both (D.2).

Stronger statements that I followed and found proved:
- D.3: a localizer with (6 b) for which some sphere `S^n`, `n ≥ 0`, is aspherical is the class of all functors (the criterion makes `X` aspherical iff its suspension is; descend to `S⁰ = K(∅ → e)`, then `∅ → e ∈ W`, then product stability). So no non-total reversible localizer contains `W_1`.
- H.8: Loc (6 b) and Loc (7 F) (enough intrinsic fibrations) together force the class of all functors, with no accessibility. The argument as I reconstruct it: for non-total reversible `W`, a `W`-aspherical `A` is connected and has no non-zero homomorphism `π_1 A → Z` (otherwise `S¹` is a retract of `A` in `Hot`, so `S¹` is aspherical, against D.3); so every map from `A` to `BF`, `F` free, is null and `Map(A, BF) ≃ BF`. The class `W′` of maps `f` with `Map(f, BF_2)` an equivalence is a fundamental localizer (homotopy limits) containing all `A → e` with `A` aspherical. Under (7 F), Brown's factorization writes every `W`-map as a section of a trivial intrinsic fibration followed by a trivial intrinsic fibration; trivial intrinsic fibrations are universally in `W` (pull back first along a fibration, then along a `W`-map), so they are in the localizer generated by the aspherical objects by Theorem A; hence `W ⊂ W′`. But `α` of F.8 is in `W_Z ⊂ W` and not in `W′`: if precomposition with `α` were bijective on conjugacy classes of endomorphisms of `F_2`, `α` would have a two-sided inverse up to conjugation and be surjective, which it is not (my check 4).
- C.5, by the same argument with C.4 in place of D.3: **no homology localizer `W_E`, `E ≠ 0` a spectrum, has enough intrinsic fibrations.** C.4 holds (if `π_1 A → Z` is non-zero then `S¹` is a retract of `A` and `ΣE` a retract of `0`). This answers a question of XVI ms. 124 that the companion leaves open (row XVI-C105).

### 4. The conjectured `W̃∞` (XVI ms. 87–88): settled, in both readings

He asks for "le plus petit localiseur `W̃∞ ⊂ W∞` satisfaisant tous les axiomes de stabilité Loc (1 ter, 2, 3 bis, 4, 6, 7, 8)" and conjectures `W̃∞ ≠ W∞`.
- With Loc (6) as he defines it: no localizer contained in `W∞` satisfies the list. A fundamental localizer contained in `W∞` is `W∞` (Cisinski), and `W∞` fails (6 b). Fully checked, given minimality.
- Without the bound `⊂ W∞`: the intersection of all localizers satisfying the list is the class of all functors (D.4). This uses "Loc (7) holds only for `W∞` and the class of all functors" (XVI Théorème 6.1 with minimality; E.4–E.5). Of that I checked the core, E.5: if `W`-equivalences of spaces are stable under homotopy pullback, the fibres of a `W`-map are aspherical; an aspherical non-contractible space can be looped until it is disconnected; two points in different components then have empty homotopy pullback, so `∅ → e ∈ W` and `W` is everything; otherwise all fibres of `W`-maps are contractible and `W = W∞`. The reduction E.4 from Loc (7 D) (strict base change along `W∞`-perfect functors) to homotopy pullbacks I did not follow; it rests on Cisinski 2006, 5.3.14, 6.2.3, 6.4.14, which I did not open. The companion reaches the same dichotomy by its own argument (block at XVI ms. 65), which I read and found sound.
- With (6) read as (6 a): `W̃∞ = W∞`.
So the statement in the prompt ("would be all of `Fl(Cat)` under his own reading") is right for the unbounded intersection, and the conjecture `W̃∞ ⊊ W∞` is false in every reading. Simple homotopy types cannot come from a localizer (D.5; not checked beyond the statement). The observation of ms. 95 survives (D.6; my check 5).

### 5. The other leads

- Lead 5 (the fibration axiom as left exactness): E.6 says Loc (7) and the weakest (7 D) are equivalent, for accessible `W`, to left exactness of the localization of spaces, with only the two trivial cases; and Loc (7 F) is a different, weaker condition (right properness, nullification, modality: E.2–E.3). I checked the necessity half of E.2 (the Brown argument above) and the dichotomy; E.3 is unverified.
- Lead 6 (a bijection between reversible localizers and localizing subcategories of spectra): **false**, as F.7 says. The zero subcategory and the `HZ`-acyclic spectra both give `W_Z`: a map of spaces has a connective cofibre spectrum, which is zero iff it is `HZ`-acyclic. Checked. What remains is a Galois connection (F.4–F.5; formal, statements read) and an open question (F.14: is every accessible reversible localizer of the form `R(𝓛)`).
- The table C.7: the entries I can confirm are (6 a, b, c) for `W_E` (cofibre sequences), the failure of (6 b) for `W_n` (the companion's block at XVI ms. 17′ has the same example), the failure of (7), (7 D) for everything other than `W∞` (E.5), (7 F) for `W_n` (the companion, from Cisinski 9.2), and the failure of (7 F) for `W_E` (verdict 3).

## What I could not check

- Part A: the exact wording of the axioms against the edition (A.1–A.7), Brown's lemma in the form A.8, the implication schemes A.13–A.15. A.19 (the least weak localizer is `W∞`) is Cisinski 2006, Théorème 6.1.18, which I did not open; the companion cites the same theorem at the same place.
- C.8–C.10 (the classes `Fib_{W_0}`, `Fib_{W_n}`, bounds for `Fib_{W_E}`); E.3; E.4's reduction; E.7 (agrees with the companion's rows A013, A029, A062 of XIIc-a, found independently, except that the answer's example `S² ∨ S^{n−1} → S² × S^{n−1}` gives strictness of `b_n ⊂ c_n` for every `n ≥ 3`, where the companion has `n = 3` only).
- F.9–F.13 (the plus-construction localizer `W_+` with the same aspherical objects as `W_Z`; Berrick–Casacuberta not opened).
- Part G: G.8 (the 110-object counterexample to the reverse of XII Théorème 4 (a)), G.17 (the cube against XII ms. 274, 3°), G.19 (gluing), G.26 (the finite Reedy calculus from factorization alone: long, and the one place where a gap would be easy to miss). G.6, G.17, G.18 agree with companion blocks already present (XIIapp ms. 15; XIIc-b ms. 273, 274).
- H.2–H.6 restate TOTASPH C.5, D.19, F.23–F.31, which I reviewed there; H.7 unverified.
- The two statements left open by the answer stay open: A.16 (does the absolute Theorem A package of XVI Définition 1.1 imply the relative one) and F.14.

## What is wrong

I found no statement labelled Proved or Refuted that is false, and no gap in the arguments I followed. Three remarks on presentation:
- D.1 and B.6 are stated for localizers with the relative Theorem A. The companion's proof gives minimality of `W_Z` already among weak localizers with the cube axiom (6 b). The two statements should be kept apart when quoted: (6′ b) needs the relative axiom, (6 b) does not.
- "Refuted" for XVI Théorème 5.4 means: one entry of the parenthesis is false. The theorem proper (Loc (9), accessibility) stands.
- F.12 (row XIIba-A-053) is proved for strongly saturated localizers, by retract closure. It is silent when the intersection is empty; then asphericity of the intersection makes `W` the class of all functors and the statement is trivial. My check of the argument: choose an object `k` of the intersection `K`; `e → K` is in `W`; the map of spans `(U ← e → V) → (U ← K → V)` and forward gluing make the wedge `U ∨ V` aspherical; `U → e` is a retract of `U ∨ V → e` in the category of arrows.

## Changes needed in the companion (not made here)

The companion already has: XII Théorème 2 false (XIIba-A-058 and the block at ms. 78), XVI Théorème 5.4 false in its Loc (6) entry (XVI-C021), `W_Z` least among localizers with (6 b) (two blocks at XVI ms. 27), the two readings of `W̃∞` inside `W∞` (block at ms. 87, rows C038–C040), the eight fibration conditions (block at ms. 65), (7 F) for `W_n` (block at ms. 124), Cons 2 and Théorème 3° (XIIc-b blocks at ms. 273, 274), the classes `a_n, b_n, c_n` (XIIc-a block at ms. 187). What must change:

**Chunk XVI** (`checks\DER_XVI\`)
1. Row XVI-C105 (ms. 124: do the homological localizers satisfy Loc (7 F)?): from open to answered, **no**, for `W_E` with `E` any non-zero spectrum, in particular `W_R`, `R ≠ 0`. New development block at ms. 124 with the proof (C.4, C.5, F.8 and the Brown argument of verdict 3).
2. Block at ms. 124 "Generalized Thomason models and the role of properness": add that for accessible `W` right properness is also necessary for (7 F) (E.2), and that the homology localizers are therefore not proper; its closing paragraphs now read as if the question were undecided outside the truncations.
3. Row XVI-C073 (ms. 105–106: do Loc (6 a), (8), (9) imply (7 F)?): answered **no**: `W_Z` satisfies (6 a), (8), (9) (C.2, C.3) and fails (7 F).
4. Row XVI-B099 (ms. 70: test `W_n` for (7 F)): fill the empty repair: affirmative, as in row XVI-C048; add the description of `Fib_{W_n}` of C.9 as unverified.
5. Block at ms. 27 "The least localizer satisfying reverse cube excision": add (a) for localizers with the relative Theorem A the single-square axiom (6′ b) already suffices, through the cofibre criterion (B.5); (b) the reversible localizers are not upward closed: `W_0 ⊃ W_Z` fails (6 b) (B.13; row XVI-A088 has the fact, the block does not draw the conclusion).
6. New development block at ms. 27, after the previous one: "The two axioms exclude each other": D.3 (no sphere is aspherical), H.8 ((6 b) with (7 F) gives all functors; a non-total reversible localizer lies between `W_Z` and `W_0`, strictly below `W_0`), D.2 (with Loc (5), no localizer has (6 b) and (7)). Proofs as in verdict 3.
7. Block at ms. 87 "The weak minimality theorem settles the finer-localizer hopes", and the notes of rows XVI-C038, C039, C040: add the third reading: without the bound `⊂ W∞` the intersection of the localizers satisfying the literal list is `Fl(Cat)` (D.4).
8. Optional new block at ms. 27 or ms. 124: localizing subcategories of spectra give reversible localizers `R(𝓛)`; the correspondence is a Galois connection and not a bijection (F.2, F.4–F.7); `W_+` has the aspherical objects of `W_Z` and is smaller (F.9, unverified). Only after F.9 is checked.
9. Overview of XVI: one paragraph on the two poles (fibration axiom: `W∞` only; reversible axiom: from `W_Z` up, never with enough fibrations).
10. Rows XVI-A092, A112 (does (6′ a) give (6 a)?): add to the notes that for localizers with the relative Theorem A both hold outright (B.2, A.11), and that the weak-axiom form depends on A.16, open.

**Chunk XIIb-a** (`checks\DER_XIIb-a\`)
11. Row XIIba-A-053 (ms. 76): from open to answered **yes**, without W(7 bis), for strongly saturated `W` (F.12; argument in "What is wrong" above); add a short block at ms. 76 or a sentence in "Ordinary covers yield homotopy pushouts, with one direction of excision", with a pointer to the XIIc-b block at ms. 272, which already has the retract argument.
12. Block at ms. 78 "A finite counterexample to the asserted reverse excision" and block at ms. 79 "What survives of the cube principle": add a pointer to XVI ms. 27 (the reverse axiom forces all of `W_Z`), and the sentence that the failure persists along Dwyer maps (B.8), which bears on rows XIIb-a-B002, B003, B012, B015 (already conditional; no status change). Optional: mention the 35-object category model in place of the larger poset.

**Chunk XIIb-b** (`checks\DER_XIIb-b\`)
13. Row XIIbb-A045 and the block at ms. 126 "Why converse excision is an additional axiom": strengthen from "acyclic categories become aspherical" to "every integral homology equivalence is in `W`", with the pointer to XVI ms. 27.
14. Rows XIIb-b-B036, XIIbb-C019 (reverse of Théorème 4 (a), Corollaire 6 (b)): add to the notes that the answer gives a second counterexample for `W∞` (G.8, 110 objects, unverified); compare it with the block at ms. 157 before citing.

**Chunk XIIc-a** (`checks\DER_XIIc-a\`)
15. Row A029 and the block at ms. 187: strictness of `b_n ⊂ c_n` for every `n ≥ 3` by `S² ∨ S^{n−1} → S² × S^{n−1}` (E.7; unverified), in addition to the `n = 3` example.

**Chunk XIIc-b** (`checks\DER_XIIc-b\`)
16. Row XIIcb-C028 (footnote 138): add G.26 as a direct proof from the factorization hypothesis alone (unverified; have it read before it is integrated). No status change in rows C011, C020, C038, which agree with B.5, G.16, G.17.

No change needed: XIIapp (G.6, G.19 agree with the blocks at ms. 15 and ms. 18), XI-XIIa.

## For the prompts

No POLES statement cited in `5_STRATA`, `6_PATHS`, `7_BISITE` was found false. Checked among those cited: B.3, B.4, B.9, C.5, D.6 (own enumeration), E.5 (core), E.2 (necessity), H.8. Still unverified among those cited: G.6, G.8, G.19, G.26, A.8–A.9, A.13–A.14, C.8–C.10, E.3, E.4, H.6 (reviewed as TOTASPH F.23), and Cisinski 2006, Théorème 5.3.14, which was not opened. The prompts say that the statements are unverified; that sentence stays.
