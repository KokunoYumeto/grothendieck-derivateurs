# GALOIS: review by the author of the prompt

Claude (Fable 5.2, Anthropic), 11 November 2026. Review of the answer of GPT-6 Astra (ChatGPT Pro mode) to prompt `4_GALOIS` (74 statements: 52 Proved, 10 Known, 7 Refuted, 5 Open), read against my four leads, against the nine checks listed in `3_POLES\PROMPT_UPDATES.md`, and against the companion's audit of Chapter I.

## What I read and checked

Read: `GALOIS_report.md` in full; `GALOIS_results.csv` (all 74 statements); `sections/A.tex` and `sections/B_general.tex` in full with their proofs; in `B.tex` the proofs of B.9, B.10; `B_KT.tex` (B.11, B.12) in full; in `B_loc67.tex` the proof of B.6 and of B.7 as far as the classification of (7 a, b, c) and the start of "(7 F) is properness"; in `D.tex` the proofs of D.3–D.7 and D.12; `research/D_audit.csv` against the 21 rows of `DER_I-b_claims.csv`; the statements of Parts C, E, F, G, whose arguments I reconstructed myself where a verdict below says so. Opened: Cisinski, *Locally constant functors*, 3.4–3.13 (in the 4_GALOIS zip); Di Vittorio, arXiv:2309.05216v2, Definitions 3.1.1, 3.1.5, Theorem 3.1.14, Propositions 3.2.21–3.2.22, Conjecture 3.2.23; Kaledin, arXiv:2409.17489v3, Definitions 2.1.5.3, 6.1.1.2–6.1.1.3, Corollary 6.1.2.5, Theorem 7.3.1.3, and its arXiv record. Not read: the proofs of B.1, B.2, B.4, B.8, D.2, D.8–D.11, E.2, E.3, E.9, F.4–F.6, G.3–G.5; the PDF; the `research/` notes other than `D_audit.csv`. Nothing in the answer's `code\` folder was run.

Own checks: `checks_author\check_galois.py`, output `check_galois.out`, written from the statements with my own code.
1. A.5: for the regular `C_2`-set, 4 functions and 2 equivariant ones; no fixed point, one orbit.
2. D.3 and D.12: the categories `B` (2 objects, 5 arrows) and `E` (4 objects, 10 arrows) built from the definitions, all composable triples associative; `E → B` is a covering; the fibres of `E → [1]` have 2 and 1 components, the second with exactly one arrow between each ordered pair.
3. D.4, D.5: the face poset `K` of the boundary of the tetrahedron (14 objects, 50 arrows, 36 strict inclusions, 24 chains of length two), the twisted extension `H` (100 arrows, 1552 composable triples, all associative) and `E = B ×_K H` (15 objects, 116 arrows, 2064 triples); `H_1(−; F_2)` is 0 for `H` and `E` with the cocycle supported on one triangle and `F_2` with the zero cocycle; the fibre of `E` over `0 ∈ [1]` is `BC_2`.
All counts agree with the answer's (five and ten arrows; 1 552 and 2 064 triples; 14 and 50).

Verdict words: **proved** (I followed the argument step by step and found it complete, given the named classical inputs); **proved, with the part named unverified**; **unverified**; **false**.

## Verdicts on the central results

### 1. `W_D^lc` is a fundamental localizer for every derivator: proved

B.3 is the main theorem of the answer: for a derivator with Der 1–4 in presheaf variance, on all small categories, with no enhancement and no strongness, the relative Theorem A holds for the ordinary categories `LC_D(−)`. I followed the whole proof.

- *The projectors.* For a subcategory `R ⊂ T`, the inclusion of the objects of `D(T)` inverting `R` has both adjoints. This is Cisinski's argument for 3.10 and 3.13 with a set of arrows in place of all arrows. I opened the paper: Theorem 3.6 is stated for an arbitrary set `S` of arrows; Lemma 3.9 is stated for all arrows, and its proof (diagrams of spaces inverting given arrows are stable under homotopy colimits) is the same for a subset. So the step is sound.
- *Fibres of an opfibration.* For `π: T → S` an opfibration and `x` over `t`, the comma category `x\T_s` is the disjoint union over `α: t → s` of categories with initial object the cocartesian lift; so `(i_{s!}F)(x) = ∐_α F(α_! x)` and `i_{s!}` sends locally constant objects of the fibre to vertically locally constant objects. Taking right adjoints of `j_T i_{s!} = i_{s!} j_{T_s}` gives `i_s^* Q_T ≅ Q_{T_s} i_s^*`. Checked, variance included.
- *Base change.* For a map `v` of opfibrations preserving cocartesian arrows, `T_s/x′ → T/x′` has a left adjoint (transport), hence in presheaf variance restriction along it computes the same limit; so `i′_s{}^* v_* ≅ v_{s*} i_s^*`. I checked the variance on set-valued presheaves: for `r ⊣ i` one has `r^* ⊣ i^*`, which is what is used.
- *Conclusion.* The adjunction `v^* ⊣ Q v_*` on vertically locally constant objects has unit and counit that restrict to the fibrewise ones; Der 2 finishes. Full local constancy is reflected along `v^*` because the fibre restrictions are conservative and every arrow is cocartesian followed by vertical. The Grothendieck construction `∫_s A/s` reduces the relative Theorem A to this. The compatibility of the two mate isomorphisms with units and counits is asserted and standard; I did not write out the diagrams.

With A.4 (two-out-of-three and retracts for `W_D^lc`, formal) and the terminal-object case this gives the three axioms. `W∞ ⊂ W_D^lc` is Cisinski's Corollary 3.8 (opened).

### 2. The 1-complete class is not a fundamental localizer: proved (the lead was wrong)

A.5: for set coefficients `e → BC_2 → e` has composite and second map in `W^1` and first map not (my check 1). So `W_D^1`, `W_D^{coh}`, `W_D^{hom}` fail two-out-of-three already for sets; only the cancellation "`f`, `gf` in the class implies `g` in it" holds (A.4, followed). The unit-only half of B.3 shows that `W_D^1` nevertheless satisfies the relative Theorem A. Lead 1 of the prompt is therefore true for `W_D^lc` and false for `W_D^1`.

A.3 corrects a sentence I wrote in the prompt: for a map to the point the constant and the 1-complete conditions are literally the same condition, so `BA → e`, `A` acyclic, is 1-complete. Correct. The separating maps are `e → BA` (in `W_D`, not in `W_D^1`) and `BA → e` (in `W_D^1`, not in `W_D^lc`).

Accessibility (B.4: `W_𝒞` and `W_𝒞^lc` set-generated for every presentable ∞-category `𝒞`) is **unverified**: I did not read the proof. It is used in D.6, D.11, E.7, E.10. For a bare derivator it is left open (B.13).

### 3. The coefficient calculations of Part C: proved (C.2, C.4, C.5, C.7, C.9, C.10, C.12, C.13 by my own reconstruction); C.11, C.14 unverified

I did not read the proofs of Part C; I derived the statements independently and they agree.
- C.2: `v^*` is fully faithful iff the counit `v_! v^* G → G` is invertible, and `(v_! v^* G)(y) = F_y ⊗ G(y)`; for the cohomological class test on the coinduced systems `i_{y*}M`, whose pullback has sections `M^{F_y}`. So the three middle classes coincide with "`F_y ⊗ M → M` invertible for all `y`, `M`".
- C.4, C.5: for `r`-truncated spaces the constant class is `W_r`, the middle class is "homotopy fibres `r`-connected" (`π_{≤r}` isomorphic, `π_{r+1}` onto), and `W^lc = W_{r+1}`; the inclusion `W^lc ⊂ W_{r+1}` I take from the standard fact that an `(r+1)`-type is recovered from its `r`-truncated local systems. Strictness and failure of two-out-of-three by `* → K(A, r+1) → *`.
- C.7: restriction of scalars along `C_*(ΩS; k) → C_*(ΩT; k)` is an equivalence iff the map of algebras is; `H_0` gives a bijection `π_1 S → π_1 T` because `k[X] → k[Y]` is bijective only for a bijection `X → Y` when `k ≠ 0`; the passage between loop spaces and universal covers reduces to fibres of maps of simply connected spaces.
- C.9: I proved the arithmetic statement separately: for a complex `C` of free abelian groups and a ring `k ≠ 0`, `C ⊗ k` is acyclic iff `C ⊗ F_p` is acyclic for every prime `p` not invertible in `k` and, when `char k = 0`, `C ⊗ Q` is acyclic (the pair `Z/p^∞ ⊗ k`, `Tor(Z/p^∞, k)` is the cokernel and kernel of `k → k[1/p]`, both zero only when `p` is a unit). Hence `W_{D(k)}^lc = W∞` iff no prime is invertible in `k`; in particular for `Z`.
- C.10: spectra give the classes of `D(Z)` (connective spectra, Hurewicz). C.13: for `Q` the class is "`π_0`, `π_1` isomorphic, higher homotopy rationally isomorphic"; the attribution to Rivera–Wierstra–Zeinalian 2021 I did not open.
- C.11 (the `E`-local description; `π_1` is forced: checked; strictness for Morava `K(n)`: not checked) and C.14 (Toën's schematization strictly weaker; the reversed implication after his Definition 3.1.1) are unverified.

So Lead 2 is right in every value. The table C.15 can be used.

### 4. The repaired fibration theory of Part D: the refutations are proved; the repair is known; D.7 proved

- D.3 (composition fails for the weak rational fibrations of I ms. 117–118): proved; my check 2. This is the companion's block at ms. 118 with the same example.
- D.4 (the "2-complete over aspherical bases" notion of I ms. 122 is not stable under composition, for set coefficients): proved. `H → K` is a fibration and opfibration with fibre `BC_2` and identity transports, so `BH → BK = S²` is a fibre sequence and `π_1 BH` is a quotient of `C_2`, hence equal to `H_1`; my check 3 gives `H_1(H; F_2) = 0` for the cocycle on one triangle and `F_2` for the zero cocycle. Over a weakly contractible base the cocycle is a coboundary and the pullback is a product with `BC_2`; `q` is a universal `W_1`-equivalence because its fibres are simply connected; the test `{0} → [1]` on the composite gives `BC_2 → E` with `E` simply connected. Grothendieck's "(que je sache!)" is thereby settled: the notion is not stable under composition.
- D.5 (a total equivalence need not be a fibrewise one, for both blanket substitutions): proved; `H → K` over `K`, and the section of `R → [1]`.
- D.12 (`e → BC_2` pulled back along `EC_2 → BC_2` changes `π_0`): proved; my check 2. The companion's row I-b-B079-07 has the same example.
- So **Lead 3 is false**: replacing **D**-equivalences by 2-complete or 1-complete ones throughout does not make I ms. 79–84 true.
- D.6 (the repair: Thomason fibrations of an accessible `W`; a `W`-map between two of them over `S` is fibrewise in `W`; no right properness): proved from Cisinski 2006, Théorème 5.2.15 (not opened) by a standard argument (pullback to a point is right Quillen on the slice, and both objects are fibrant there). It applies to `W_D^lc` when that class is accessible (B.4, unverified).
- D.7 (row I-b-B084-01: if every strict pullback of `u` is a constant-coefficient equivalence then `u^*` is fully faithful on all of `D(B)`): proved. The comma category `z\v` of `A/b → B` decomposes over `γ: z → b` into the pullbacks of `u` to the factorization categories `J_γ`, which have a terminal object; each receives the fibre `A_b` by a constant-coefficient equivalence; the mate is then a coproduct of isomorphisms.
- D.2, D.8–D.11 (what the local-coefficient repair proves; the case of spaces; the six further false rows; the doubled-arrow construction): unverified. D.9's corrections agree with what the companion's rows already say (see the list at the end).

### 5. The tower and the realization (Part E): E.5, E.7, E.8, E.10 proved in outline, with B.4 unverified; E.2, E.3, E.9 unverified

- E.7: for a product-stable localization `L` of spaces the constant class of the derivator of local spaces is the class inverted by `L` (`S ⊗ M = L(S × M)`; test on `M = *`). Every accessible fundamental localizer is of this kind. Checked. This answers row X024 for accessible localizers.
- E.10: with `V_0` the rational homology equivalences and `V_{r+1}` = "bijective on `π_0`, and `Ωf ∈ V_r`", the description "`π_i` isomorphic for `i ≤ r`, rationally isomorphic above" follows by induction from C.13; strictness by `K(Z/p, r+1)`; intersection `W∞`. The identification `W^lc_{D_r} = V_{r+1}` for the derivator of `V_r`-local spaces is by monadicity of evaluation on a connected `X` (monad `M ↦ L(ΩX × M)`), which I followed in outline.
- E.4, E.8: the answers to the question of the prompt are: local systems of `Q`-linear categories do see `K(Z/p, 2)` and `K(Z, 2)` (characters `Z/p → Q(ζ_p)^×`, `Z → Q^×`) and do not see `K(Z/p, 3)`; the second stage is "`π_0, π_1, π_2` exact, rational above". Consistent with E.10; the proof of E.2 (the constant class of presentable `R`-linear categories is `W^lc_{Mod_R}`) I checked only in the form `X ⊗ 𝒜 = Fun(X, Mod_R) ⊗_R 𝒜`.
- Lead 4 is thus realized for sets and rationally. A functorial raising **D** ↦ **D′** on bare derivators is open (E.11, G.6), correctly labelled.

### 6. Reconstruction (Part F): F.1–F.3, F.7 proved; F.4–F.6 unverified except the citations below

F.1 (Yoneda in `Fun(Π_1 X, Set)`), F.2 (monadicity of evaluation), F.3 (shape of `𝒮_{/X}`; `[X, Z]` from the terminal object and the constant functor) are standard and correct as stated; F.8 is honestly left open. F.4 (Hoyois, Theorem 3.13, Corollary 3.20) was not opened.

### 7. The Kan–Thurston statement and CATHOT E.17: proved

- B.9 (acyclic maps are epimorphisms in the unpointed homotopy category): followed; van Kampen and local-coefficient Mayer–Vietoris on the double mapping cylinder.
- B.10 (acyclic simple overgroups of prescribed cardinality): followed; HNN extensions with cyclic subgroups generated by words of infinite order, mitosis with the Künneth argument, alternation. I did not open Baumslag–Dyer–Heller.
- B.11 (KT_μ): followed in full. The step I had named as unchecked (injectivity of `π_1 T(L) → π_1 T(K)` for subcomplexes) is proved by building `T(K)` from `T(L)` in two stages, each a graph of aspherical spaces with injective edge groups; the induction hypothesis is used for `(n−1)`-dimensional subcomplexes only, and the two constructions give the same space because the choices are attached to simplices. Acyclicity is for all local systems on the target; the kernel is the normal closure of the cone groups, perfect, and killed by every homomorphism to a group of size at most `μ`.
- B.12: followed. The point that needed an argument, `H′(Y) = colim_i [Y, BK_i]`, is obtained from left Kan extension along the localization `𝓗 → Hot`; then `H′(τ_1 Y) → H′(Y) → H′(⊔ BG_c)` has bijective composite and injective second map.
So CATHOT E.17 holds for small filtered index categories, and the citations of B.11–B.12 in `6_PATHS`, LM3 and LM5 stand.

## The nine POLES checks

1. *Loc (7).* B.7: for `W ⊂ W_0`, each of (7 a, b, c) holds iff `W = W∞`; so `W_D^lc` has them exactly for sets of coefficients with `W_D^lc = W∞` (spaces, `D(Z)`, spectra, `D(k)` with no invertible prime) and not for sets, `r`-types, `D(Q)`, `D(F_p)`. Agrees with POLES E.5. The implication (7 c) ⇒ `W∞` is taken from Cisinski 2006, 6.4.22 (not opened); POLES E.5 gives it independently.
2. *Loc (7 F).* B.7: for accessible `W`, (7 F) iff proper iff generated by maps `A → e`; `W_{D(k)}^lc` has it iff no prime is invertible in `k`; `W_{D(k)}` never. Agrees with POLES E.2, C.5, C.9 (`W_{r+1} = W^lc` of `r`-types is proper). My own test of `W_{D(Q)}^lc` by the criterion asked for: its aspherical objects are the simply connected spaces with torsion homotopy; `K(Z, 2)` is local for the nullification at all of them (`H^2(A; Z) = H^1(A; Z) = 0`), and multiplication by `p` on `K(Z, 2)` is in `W_{D(Q)}^lc` and is not an equivalence; so the class is not generated by its aspherical objects and fails (7 F). Agrees.
3. *Loc (6 b), (6 c).* B.6: both fail for `W_D^lc` of every non-trivial **D**, and (6 b) for `W_D^1`; every `W_E` satisfies (6 a, b, c). No table gives a class both (6 b) and (7 F), or (6 b) and detection of `π_1`. Agrees with POLES B.5–B.6, C.3, F.2. I followed the non-thin case (the double cone on `BG`, `G` acyclic, is contractible while `BG → e` is not in `W^lc`). In the thin case every `BG → e` is in `W_D^lc`, and the answer uses the fold of two points, whose double cone is a circle: the example of POLES B.13.
4. *Loc (4), (5), (8), (9).* B.5, G.1, G.2: `W_D^lc` has (4), (6 a), (8) always and (5) iff `D(e)` is not trivial; `W_D` has (5) iff `D(e)` is not a preorder, which for `E`-local spectra is `E ≠ 0`, as POLES C.2. (9) is B.4 (unverified).
5. *Which Theorem A.* Both: the absolute form in B.1, the relative form (Loc (3 bis)) in B.3. POLES A.16 is not needed.
6. *The classes of XII ms. 178–187.* The answer calls only `W_D` and `W_D^lc` localizers and proves that the three middle classes fail two-out-of-three. For `r`-types the middle class is "fibres `r`-connected" (POLES's `a`-class) and `W^lc = W_{r+1}` (the `b`-class), as POLES E.7. My inference is confirmed: for `D(Z)` the class `W^{coh} = W^{hom} = W^1` is the class of acyclic maps (C.7 with `k = Z`), which fails two-out-of-three.
7. *Values and strictness.* `W_{D(Z)} = W_Z` (C.7). No class is identified through its aspherical objects alone; the strict inclusions are shown on maps (`e → BA`, `BA → e`). POLES F.8's endomorphism of the free group is in every `W_{D(k)}` and not in `W^1` (not surjective on `π_1`): consistent.
8. *Tower.* Every `V_r` contains `W∞` and lies in `V_1 = W_{D(Q)}^lc`; none other than the intersection satisfies Loc (7); no sphere is `V_r`-aspherical, so no `W_n` is contained in a `V_r` (B.8). Consistent with POLES D.3 and TOTASPH F.28.
9. *`D ↦ W_D`.* G.3–G.5 claim no injectivity or monotonicity; C.10 gives `W_{Sp} = W_{D(Z)} = W_Z`, an instance of POLES F.7.

No contradiction with POLES in any of the nine.

## The slips reported in the printed text

Checked on the rendered pages of the edition (`packages\DER_I-b\DER_I-b_pages.pdf`, PDF pages 21 and 36, printed pp. 57 and 72; `packages\DER_XVI\DER_XVI_pages.pdf`, PDF pages 26 and 44, printed pp. 24 and 42).

| Place | What the page prints | Edition or ours |
|---|---|---|
| I ms. 93, condition b) | `H^*(Z,k)^G → H^*(Z,k)^G` "ne soit pas [un] isomorphisme" | The edition's text. Our transcription reproduces it and already carries a `[sic]` note proposing `H^*(Z,k)^G → H^*(Z,k)`. |
| XVI ms. 78, the order on pairs | `(X_i, Y_i) ⊂ (X_j, Y_j) ⟺ X_i ⊂ Y_i et X_j ⊂ Y_j` | The edition's text. Our transcription reproduces it with a `[sic]` note giving `X_i ⊂ X_j et Y_i ⊂ Y_j`. |
| XVI ms. 39, Loc (7), F) | "Cat muni de `(W, Fib_W)` est une catégorie à cofibrations (propre, et même de Brown, …" | The edition's text (also the unclosed parenthesis). Our transcription is faithful. |
| I ms. 122 | "a le grand tort de ne pas être stable par composition (que je sache!)" | The edition's text; no slip, a qualification. Our transcription is faithful. D.4 turns it into a theorem. |

None of the four is an error of our transcription. The answer's report calls them "transcription corrections" and the register note of B.4 "corrects subcategory-order transcription": both should read "corrections to the printed text".

## Di Vittorio and Kaledin

- Di Vittorio (arXiv:2309.05216v2; Adv. Math. 485 (2026) 110726): confirmed in the paper. `Dia` is the 3-category of small simplicially enriched categories (Definition 3.1.1); a 2-prederivator is a trihomomorphism `Dia^op → GRAY` (3.1.5); for a combinatorial `sSet_Joyal`-enriched model category the associated 2-prederivator is constructed (3.1.14) and (HDer 1)–(HDer 4) are proved; (HDer 5) is proved for the represented 2-prederivator (3.2.21), is stable under shift when assumed (3.2.22), and for model categories is **Conjecture 3.2.23**. My sentence in the prompt, "the axioms are verified in several models", was too strong; E.6 is right.
- Kaledin (arXiv:2409.17489v3): confirmed. `Pos` is the category of partially ordered sets of finite chain dimension (after Definition 2.1.5.3), not of finite posets; `Pos⁺` the left-bounded ones; a small enhanced groupoid is a family of groupoids over `Pos` (6.1.1.3); Corollary 6.1.2.5 is for uncountable regular cardinals; Theorem 7.3.1.3 is as quoted. "Chapters 6 and 7 are still preliminary" is not in the PDF; it is in the comments field of the arXiv record, which I opened: "Introduction and Chapters 1-5 are now in their final form … while Chapters 6 and 7 are still preliminary." So F.5 is right, and the theorem I cited in the prompt (7.3.1.3) is in the preliminary part.

## What I could not check

B.1 (Cisinski 2008, Proposition 3.7, not opened), B.2, B.4, B.8 (Cisinski 2006, 9.2.17), the second half of B.7 (properness; Cisinski 2006, 9.4.5–9.4.7) and its `W^1` clauses; the strictness for `K(n)` in C.11; C.13's citation and the Gómez-Tato–Halperin–Tanré hypotheses; C.14; D.2, D.8–D.11; E.2 in full, E.3, E.9; F.4 against Hoyois, F.5's use, F.6; G.3–G.5. The five statements left open stay open: B.13, B.14, E.11, F.8, G.6.

## What is wrong

I found no statement labelled Proved or Refuted that is false, and no gap in the arguments I followed. Remarks:
- The four "transcription corrections" are corrections to the edition (above).
- D.5 says it "also refutes the qualification in I-b-B084-07" after two replacements (complete asphericity, 2-complete equivalences). That is a refutation of the lead, not of the companion's repair of that row, which keeps constant-coefficient equivalences over a completely **D**-aspherical base; for `D(Q)` and homotopy fibres that repair holds (the fibre of `F → X` is `ΩS`, connected and rationally acyclic).
- B.3 is stated for derivators on all small categories; the proof uses Kan extensions along infinite coproducts of the base (`∐_α`), so it does not transfer to a domain of finite categories without change. The answer does not claim that it does.

## Changes needed in the companion (not made here)

**Chunk I-b** (`checks\DER_I-b\`)
1. New development block at ms. 99–100: the class `W_D^lc`; it is a fundamental localizer for every derivator (B.3, with the proof); `W_D^1` satisfies the relative Theorem A and fails two-out-of-three (A.5); the chain `W∞ ⊂ W^lc ⊂ W^1 ⊂ W^{coh} ∩ W^{hom} ⊂ W_D` (A.2); for a map to the point, constant = 1-complete (A.3).
2. Rows I-b-B097-03, B098-03, B100-03, Ib-C034, C036, C037, C038, C039 (the axioms Der 3 a′, b′, a″, b″, "assumed"): notes: they hold for every derivator (Cisinski 2009, Corollary 3.8; A.2). No status change if the companion already says so.
3. Rows Ib-C087–C090 (Der 3 c): add which derivators satisfy them: `W_D = W_D^lc` for spaces only among the computed cases; fails for sets, `r`-types, `D(k)`, spectra (C.5, C.12).
4. Row I-b-B079-03, B079-04: repair made exact by D.2: a 1-complete input gives a constant-coefficient output, not a 1-complete one; strike "or restrict to completely D-aspherical test bases" unless proved separately.
5. Row I-b-B081-04 and the block at ms. 118: add that the 2-complete variant fails as well (D.4), with a pointer to the block at ms. 122.
6. Block at ms. 122: Grothendieck's "(que je sache!)" answered: the 1-/2-complete fibrations are not stable under composition (D.4; the 14-object example, proof as in verdict 4). Compare with the companion's existing counterexample there and keep the smaller.
7. Row I-b-B084-01: from conjectured to answered **yes**, with the proof of D.7 as a development block at ms. 84.
8. Row I-b-B084-06: add the positive replacement D.6 (Thomason fibrations of the accessible localizer; fibre detection without right properness), marked as depending on accessibility.
9. Row I-b-B084-07: no status change; note that the 2-complete variant is false (D.5) while the repair with constant equivalences over a completely aspherical base stands.
10. Row I-b-B096-04: answered under Der 3 a′ (D.8, unverified): leave conjectured until D.8 is read; note the pointer.
11. Row I-b-A069: add D.11 (the doubled-arrow gluing holds for `W_D^lc` and `W_D^1` of every derivator), unverified.
12. Rows Ib-C021, C026, C048, C069, C092, C096: no change (already "proved in modern theory"); add C.5/C.15 as the statement that spaces are the only computed case where the five classes coincide.
13. Rows Ib-C018, Ib-C047, Ib-C082: note C.2: with an ∞-categorical enhancement the cohomological, homological and 1-complete classes coincide, without internal Homs.
14. Rows I-b-B087-05, B093-04, B093-05, B095-01, Ib-C003: no change; D.9 agrees with the repairs already recorded.
15. Overview of I-b: one paragraph: the chapter's unnamed object is the localizer `W_D^lc`; Lead "replace by 2-complete throughout" is false.

**Chunk I-a** (`checks\DER_I-a\`)
16. Block at ms. 60–66 (**D**-equivalences): pointer to the I-b block of item 1 and to the values of C.15; rows I-a-L063, I-b-A020 (strict **D**-equivalences: composition and the cancellation rule): note that the same closure pattern, without two-out-of-three, is that of `W_D^1` (A.4).

**Chunk VIII-X** (`checks\DER_VIII-X\`)
17. Row X021 (ms. X:2, `W_D` satisfies the localizer axioms): cite B.1 (Cisinski 2008, Proposition 3.7) and add `W_D^lc` (B.3).
18. Row X024 (ms. X:3, realize a localizer as some `W_D`): answered **yes** for accessible fundamental localizers, by the derivator of local spaces (E.7); open otherwise.
19. Rows X038, X042 (ms. X:5, component detection La): corrected expectation: `W_D ⊂ W_0` iff `D(e)` is not a preorder; `W_D^lc ⊂ W_0` iff `D(e)` is not trivial (G.1, G.2).
20. New development block at ms. X:5: the table C.15 (constant, middle and locally constant classes for sets, `r`-types, spaces, `D(k)`, spectra), with the arithmetic criterion of C.9 and its proof.
21. Row X022 (ms. X:3): note that the fibration statements of Chapter I do not extend to a general `W` (B.7, POLES E.5).

**Chunk VI-a** (`checks\DER_VI-a\`)
22. Blocks at ms. 32–38 and 65–69 (`HOT^lc(S)` and the reflection `ρ`): note A.6 and B.3: the locally constant objects form a reflective and coreflective subderivator for every derivator, and invariance under relative weak equivalences holds on a bare derivator. Rows VIa-141, 146, 148, 160: no status change.

**Chunk XIIc-a** (`checks\DER_XIIc-a\`)
23. Block at ms. 187 and rows A050, A062: add the coefficient meaning: `b_n = W_n` is `W^lc` of `(n−1)`-types and the connectivity class `a_n` is its 1-complete class, which fails two-out-of-three (C.4, C.5); this is why `a_n` cannot define the localizer (row A050).

**Chunk XI-XIIa** (`checks\DER_XI-XIIa\`)
24. Block at the opening of XI (Hot-fibrations): pointer to D.8 (for spaces the four notions of Chapter I coincide with universal preservation of `W∞`) and to D.1 (the test on contractible bases is a different notion for other localizers); unverified.

**Chunk XVI** (`checks\DER_XVI\`)
25. Row XVI-C019 (ms. 79: all localizers in use satisfy Loc (8), (9)): add `W_D^lc`, `W_D` for presentable coefficients (B.4, B.5; B.4 unverified); for a bare derivator accessibility is open (B.13).
26. Block at ms. 124 (properness and (7 F)): add the family `W_{D(k)}^lc`: (7 F) iff no prime is invertible in `k` (B.7), with the `K(Z, 2)` argument of check 2 for `Q`.
27. Block at ms. 27 or ms. 17′ (reverse excision): add that every `W_D^lc`, **D** non-trivial, fails (6 b) and (6 c) (B.6).
28. Block at ms. 78: the `[sic]` on the order relation is the edition's; no change in the text; mention in the block if not already there.

**Chunk XIIapp** (`checks\DER_XIIapp\`)
29. Row XIIapp-G23 (ms. 18, `n`-gerbes): note the tower of E.5 and E.10 as the precise form of "higher degrees through `n`-gerbes" (coefficients in `r`-types give `W_{r+1}`).

**Chunk III-V** (`checks\DER_III-V\`), from B.11–B.12
30. Rows V-I052, V-I053 and the block at V ms. 46 (where CATHOT E.17 was left open): for a small filtered index category, invariance of `H` under all weak equivalences forces the ind-object to be isomorphic to its stagewise fundamental groupoids (B.12); new development block with (KT_μ) (B.9–B.11). Row V-I057 (essential constancy "should almost never occur"): note the consequence.

## For the prompts

No GALOIS statement cited in `5_STRATA`, `6_PATHS`, `7_BISITE`, LM3, LM4, LM5 was found false. Checked among those cited: A.2–A.5, A.6 (the cited theorem opened), A.7 (the fence example), A.8/C.1 (the adjunction argument), B.3, B.5 (as a consequence of B.3), B.6, B.9–B.12, C.2, C.4, C.5, C.7, C.9, C.10, C.13 (the statement), D.3–D.7, D.12, E.5, E.7, E.10, F.1–F.3, F.5 and E.6 (against the papers), G.1, G.2. Still unverified among those cited: B.4, the properness half of B.7, C.11, C.14, D.1, D.2, D.8, D.9, D.11, E.2–E.4, E.8, F.4, F.6, F.7. The prompts say that the statements are unverified; that sentence stays.
