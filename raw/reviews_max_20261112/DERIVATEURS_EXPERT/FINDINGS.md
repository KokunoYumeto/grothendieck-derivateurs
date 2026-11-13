# Findings and implications (running list; Dérivateurs expert, Claude Fable 5.2, effort max)

Every potential finding, sharpening or connection noticed while reading, with its source. "Mine" = found or proved
by me in this review; "return" = in the return, checked by me; "G." = Grothendieck. A section "Compared with the
earlier review" is added per return only after my own REVIEW.md of that return is complete.

## General (from the reading of Grothendieck, before any return)

- F-G1 (mine). **XII Théorème 2 (ms. 78), "`W∞` satisfait à W(7)", is false**, and so is the reverse half of
  W(7 bis) for `W∞`: `X = A ⋆ {t, s}` with `A` connected, acyclic, not aspherical. Grothendieck did not write the
  verification ("je devrais sans doute réparer cette omission"). Everything in XII that uses "W(7 bis) forme forte"
  (his own footnotes 104, 105 mark these places: Th. 4 Cor. 4 and 5; also the Corollary of ms. 85, Prop. 7, and
  the uses at ms. 105, XIIapp ms. 7 and 15) holds for homology localizers and not for `W∞`. (Also in TOTASPH A.13;
  it is the starting point of POLES.)
- F-G2 (mine). In II ms. 36ter (Contre-exemple 2.20) the step through "XII th. 4 cor. 4" must be replaced by:
  `i ∈ W∞` iff `X/H` is connected and acyclic (when `X` is aspherical). The counterexample stands.
- F-G3 (mine). The "collage test" presented as Lead 1 in the TOTASPH prompt is Grothendieck's own (II ms.
  36bis–36ter, in the presheaf variance).
- F-G4 (mine). Checks of the examples of XII ms. 104–107 and XIIapp ms. 5–7, 12–16 for `W∞` without the strong
  axiom: Prop. 11 (ms. 107) is right for `W∞` (the pushout is the suspension of a 1-connected, non-contractible
  `Y`); the XIIapp Proposition (ms. 13: the boundary of `Φ_n × Φ_m` is not a `W`-cofibration) is right for `W∞`
  (the cobase change has the type of `S³`), but his parenthesis "dans le cas où `W ⊆ W_1`, car `π_1 ≅ Z`" is wrong:
  the category in question is the `Z` of ms. 10–11, of type `S²` (his own footnote 7), so the argument works for
  localizers in which `S³` is not aspherical, not for `W_1`, `W_2`.
- F-G5 (mine). II Cor. 2.16–2.17 assume the limit axiom Loc (8). By Cisinski's minimality theorem (2004,
  Th. 2.2.11) it is not needed: filtered categories are totally `W`-aspherical for every fundamental localizer.
- F-G6. The gluing question of XIIapp ms. 17–18 (is `∫(X_0 ← X̃_01 → X_1) → X` in `W∞`?) has the answer yes; the
  one-point case is TOTASPH A.10 with an explicit model. (STRATA treats it; to be reviewed there.)

## Return 2 (TOTASPH)

- F2-1 (return, checked). **Characterization of total asphericity** (C.5): `A` is totally `W∞`-aspherical iff it
  is totally `W_Z`-aspherical iff `A` is non-empty, connected and every component of every category of elements
  `El_A(H)`, `H: A → Set`, is weakly contractible; equivalently (B.11) ordinary colimits over `A` of simplicial
  sets are homotopy colimits. I had (4) ⇒ (1) and the acyclicity half of (1) ⇒ (4) on my own; the covering trick
  (C.4) completes it.
- F2-2 (return, checked; attribution corrected by me). **Grothendieck's conjecture at II ms. 36ter is false**:
  `Δ_inj` (non-empty finite ordinals and injections) is totally `W∞`-aspherical and not filtered. The category and
  the key fact ("aff Δ is filtered") are Isbell–Mitchell, *Exact colimits*, Bull. AMS 79 (1973), Theorem 3; the
  return re-proves it by polynomial interpolation and did not open the 1973 note. New: the bridge C.5–C.6 from
  exact colimits to total asphericity, which turns the 1973 counterexample to Oberst's conjecture into a
  counterexample to Grothendieck's.
- F2-3 (return, checked). With a weakly terminal object (monoids, finitely many objects, finite categories)
  total ⇔ filtered (C.13), already for `W_n`, `n ≥ 2` (D.13). So Grothendieck's conjecture is true in the range
  where he tested it (finite examples), and his footnote-42 variant ("2-connexe") has the same truth value.
- F2-4 (mine, from C.11, C.14, D.16). **Grothendieck's second Question at II ms. 36** ("`X` totalement
  `W∞`-asphérique ⟹ `X°` totalement 0-connexe? Ou du moins implique PS 1′?") is settled: PS 1′ yes, and also span
  completion (the dual PS 1); "`X°` totalement 0-connexe" (= `X` sifted) no (`Δ_inj`).
- F2-5 (mine). Placement in the literature: `Aff_Z`-filtered (Isbell–Mitchell) ⊂ total ⊂ quasi-filtered
  (Adámek–Reiterman 1976, Adámek–Koubek–Reiterman 1981; ⇔ fixed-point property). Whether the first inclusion is
  an equality is the open problem D.7; hunch H1.
- F2-6 (mine). Total categories are closed under: final images (G., XII ms. 112), products, Grothendieck
  op-fibrations with total fibres over a total base (iterated homotopy colimits), passage to components of
  categories of elements (C.3–C.5). The first three also preserve exactness of abelian colimits.
- F2-7 (mine). `H_1(El_A(H))` for a presented `H` = (cycles of the presentation graph)/(augmentations of
  syzygies); quasi-filteredness kills it for all `H`. `H_2` is the first place where coherence between affine
  equalizers enters (see H1).
- F2-9 (mine, from the return's research record). Provenance of the proof of C.9: the return could not open
  Isbell–Mitchell 1973/1976 (HTTP 403 at ams.org during its run) and took the gap-polynomial interpolation
  construction from **our own Open Maths lesson "Derived colimits over a small category" (20 Oct 2026, AI-written
  by Claude Opus 5.5, CC0)**, found by its web search, then re-proved and machine-checked it. I opened the 1973
  Bulletin note myself (free at ams.org on 12 Nov): Theorem 3 is the statement, with a different sketched proof.
  So the chain is: Isbell–Mitchell (1973) → our lesson (Oct 2026) → the return's proof → refutation of
  Grothendieck's conjecture through C.5–C.6. The lesson should be credited in any write-up, with Isbell–Mitchell
  as the source of the theorem.
- F2-10 (return, checked by me against the corrected French). Two slips of XII not yet marked in
  `corrected_french_20261111\DER_XIIb-a.tex`: ms. 88 "`U'/t' ≃ U/H'`" (should be `U'/H'`) and ms. 89 the label
  "`F ↦ F/V`" (should be `V/F`); also footnote 65 at ms. 85 cites "cor. 4 de la proposition 15, page 149" where the
  result is Corollaire 4 of Théorème 4. To check on the edition's PDF and record.
- F2-11 (mine). C005 (XII ms. 103) follows from Grothendieck's own remarks: the endpoint functor of
  `Ch(Y; y_0, −)` is final when `Y` is 1-connected (ms. 102–103), totality passes to final images (Lemma, ms. 112),
  and `Ψ` is aspherical and not total (his footnote at ms. 103). General form: for `Y` simply connected,
  `Ch(Y; y_0, −)` total ⇒ `Y` total. Open: the converse, starting with `Y = e` (the category of interval types).
- F2-12 (return, checked). For `W∞`, Grothendieck's Dwyer programme (XII §2.4) comes out as follows:
  dwyérienne ⇒ `W`-cofibration with no extra axiom (his Cor. 1 assumed W(7)); couniversal equivalence =
  cofibration ∩ `W`; the converse "cofibration ⇒ dwyérienne" fails (C035); the stable class he wants at ms. 114
  does not exist (only isomorphisms), which explains why no enlargement of the Dwyer class worked for him; his
  XIIapp ms. 13 Proposition is the first instance of the obstruction.
- F2-13 (earlier review; re-derived by me on 12 Nov). **B.11 is about simplicial sets, not categories.** For
  `Cat`-valued diagrams total asphericity of the shape does not make `∫D → colim_Cat D` a weak equivalence:
  `A = Δ_inj`, `D([n]) = N^{[n]}` (free commutative monoid, one object). `colim_Cat D` is the monoid `N`
  (`BN ≃ S¹`), while `B∫D ≃ hocolim T^{n+1}` has `H_q = colim_n Λ^q Z^{[n]} = Z` for every `q`
  (`Λ^q Z^{[n]} ≅ Z[Hom_inj([q−1], [n])]` without signs, and colimits over `Δ_inj` are exact). The nerve does not
  commute with colimits over `Δ_inj`. Open: which shapes `A` make `∫D → colim_Cat D` an equivalence for all
  `Cat`-valued `D` (filtered ones do; the class is strictly inside the total ones). Bears on VII §10 and on
  PATHS (its items A.5–A.8).
- F2-8 (return, checked). Meaning for the manuscript: total asphericity is the condition under which the
  1-categorical colimit of diagrams of sets or simplicial sets indexed by `A` is already the homotopy colimit.
  The companion can state it this way at XII ms. 88–89.

### Return 2: compared with the earlier review

Earlier review: `pro_reviews_20261110\2_TOTAL_ASPHERICITY\REVIEW_author.md` (Claude Fable 5.2 at effort medium,
10–11 Nov), opened on 12 Nov only after my own REVIEW.md was complete. `PROMPT_UPDATES.md` in that folder not read.

**Where it was right.** All its verdicts agree with mine: no statement of the return labelled Proved, Refuted
or Known is false; D.7 and F.27 are the two open items. It also saw that the counterexample `Δ_inj` is
Isbell–Mitchell's (through the report of it in Adámek–Koubek–Reiterman 1981, A.5), that G.5 is two lines from the
manuscript, that A.16 is in Grothendieck's footnotes, and it mapped the result onto the audit rows II-C-010 (the
second Question of II ms. 36) and II-C-004 (footnote 42), as I did independently (F2-4, D.13).

**What it had that I did not.** (1) The caveat F2-13 above (B.11 fails for `Cat`-valued diagrams and colimits in
`Cat`), with the example `D([n]) = N^{[n]}` over `Δ_inj`; I re-derived it and it is right. (2) More machine checks
by its own programs: the endpoint pushout of F.23 for `n = 2, 3`; the 35-object category of A.12 and its double
cone; the monoid lemma C.12 against all 170 monoid tables of order ≤ 4; B.5, B.6, E.3, F.10, F.18. I did not
repeat these; my own programs cover the `n = 2` affine cone and the homology of `Z` only.

**What it missed or left weaker.**
1. It did not open Isbell–Mitchell 1973. I did: Theorem 1 (exact ⇔ components of `aff C` filtered), Lemma 1,
   Theorem 2 and Corollary 1 (exact and weak terminal objects ⇒ filtered components), Theorem 3 (`aff Δ` filtered,
   with the same target size as C.9). So C.9 and D.4 are known theorems with exact references, and C.13 is the
   analogue, for totality, of their Corollary 1.
2. It did not notice the provenance of the return's proof of C.9 (our own Open Maths lesson of 20 Oct 2026; F2-9).
3. It "did not check that AKR's quasi-filtered is the fixed-point property of D.17". It is: their Theorem [1],
   p. 369. This gives the placement `Aff`-filtered ⊂ total ⊂ quasi-filtered (F2-5), which the earlier review does
   not state, and with it the right way to pose D.7.
4. No attack on the two open items. Mine: for D.7 the reduction to `aug(K_1 ∩ K_2) = Z`, the `Tor` formulation,
   the identification of quasi-filteredness with the vanishing of `H_1` only, and the cone argument showing that
   the free example `K*` of AKR is unlikely to be total (H1); for F.27 the cases of groups and the failed
   candidate over `Δ_inj` (H3).
5. It did not say that Lead 1 is Grothendieck's Contre-exemple 2.20 (F-G3), nor that the step of II ms. 36ter
   through XII Th. 4 Cor. 4 must be replaced (F-G2).
6. It did not examine Grothendieck's examples of XII ms. 104–107 and XIIapp ms. 5–15 for `W∞` (F-G4: they survive;
   one parenthesis of XIIapp ms. 15 is wrong).
7. Transcription: it did not compare the return's list of slips with the corrected French (F2-10: ms. 88 and 89 are
   not yet marked there).
8. Closure properties of total categories (F2-6) and the general statement "for `Y` simply connected,
   `Ch(Y; y_0, −)` total ⇒ `Y` total" (F2-11) are not in it.

**Where it was wrong or too weak.** Nothing wrong found. Too weak: its statement that F.7 "should be followed by
a second reader" — I followed F.7 and F.8 step by step (collage `Z`, slices `X'/Q_y`); they are right. Its
reading of G.1 was against the audit rows only; mine against VII ms. 24–26 only; a full check waits for the
reading of Chapter VII.


## Return 3 (POLES): findings

Verdicts: 104 items, 102 correct, 2 unproved (A.16, F.14), 0 wrong, 0 gap. Review: `..\3_POLES\REVIEW.md`.

- **F3-1 (the two poles, final form).** For Cisinski-style fundamental localizers: (a) every fibration condition
  of XVI §4 (A, B, C, D, relative or not) holds only for `W∞` and `Fl(Cat)`; (b) the reverse cofibration axiom in
  any form (Loc (6 b), (6′ b), (6 C), (6 c), W(7), W(7 bis)) is the cofibre criterion "`g ∈ W` iff `C(g)` is
  `W`-aspherical"; its least solution is `W_Z`; (c) (6 b) together with the weakest fibration condition Loc (7 F)
  forces `Fl(Cat)`. For Grothendieck's text: XII Théorème 2 (ms. 78) false; XVI Théorème 5.4 false in its
  parenthesis; XVI 6.4 b) `W̃∞` is `Fl(Cat)` (his reading of Loc (6)) or `W∞`.
- **F3-2 (Loc (7 F) = properness).** For accessible `W`: Cat has enough `W`-fibrations in the sense of XVI
  (functors along which base change preserves `W`) iff `W` is generated by maps `A → e` iff the Thomason model
  structure of `W` is right proper iff the localization of spaces is a nullification (a modality). The ingredients
  are in Cisinski, Ast. 308, Chapter 6 (his "`W`-fibrations faibles" of 6.1.13 are Grothendieck's `Fib_W`); the
  identification with Grothendieck's axiom and the converse direction are in the return (E.2). Implication for
  the reader of XVI: the "structure homotopique droite" Grothendieck wants in 6.4 c) and 7.4 exists exactly for
  the nullification localizers (`W∞`, the `W_n`, plus-constructions, …), and never for homology localizers.
- **F3-3 (answers to questions Grothendieck leaves open in XVI), with sources:**
  ms. 17′ ("je présume que c'est pareil pour les `W_n`"): yes, `W_n` satisfies (6 a) and not (6 b) (C.3).
  ms. 23 ("(6′ a) implique-t-il (6 a)?"): for modern localizers both are theorems (B.2).
  ms. 65–66 ("D ⇒ A?", "D_{W_0} ⇒ A?"): yes, trivially: each holds only for `W∞` and `Fl(Cat)` (A.17).
  ms. 70, 91, 124 ("tester sur les `W_n`" for (7 F)): `W_n` satisfies (7 F) (C.7; my factorization
  `X → Y ×_{P_n Y} P_n X → Y`).
  ms. 105 ("[Loc (6 a, 8, 9)] impliquent-ils tout au moins Loc (7 F)? Je ne hasarderais aucune conjecture"):
  no; `W_Z` (C.5; my direct proof with the trefoil).
  ms. 87 (`W_ω ≠ W∞`? `W̃∞ ≠ W∞`?): `W_ω = W∞` also for his literal definition (Cisinski 6.1.18); `W̃∞` as in F3-1.
  ms. 122–123 (is the smallest localizer with Loc (6′ a, 8) "spécial", and `≠ W∞`?): it is `W∞`, which is special.
  ms. 123–124 (7.9: does Thomason's structure extend to special localizers?): yes (Cisinski, Th. 5.2.15); but it
  does not give (7 F), contrary to what he infers there (F3-2).
  XII ms. 111, Question (a): no (`{a} ⊂ (a ⇉ t)`); XII ms. 179 ("chacune de ces implications est stricte"): no,
  `c_2 = b_2`; footnote 117 (counterexamples to `c_n ⇒ b_n`): yes for `n ≥ 3`; XIIapp ms. 17–18 (open/closed
  gluing): proved (G.19).
- **F3-4 (mine). Loc (8) is automatic** (Cisinski, Ast. 308, Cor. 4.2.22), as are Loc (1 ter), (3 bis), (4 a),
  (6 a). So **"localiseur spécial" (XVI ms. 121) = accessible fundamental localizer**, and Grothendieck's
  closing theorem of XVI (Loc (6′ a, 8, 9) ⇒ `HOT_W` is a derivator) is the theorem that accessible localizers
  give derivators. Not stated in the return.
- **F3-5 (mine). Direct proof that `W_Z` and `W_k` fail (7 F)** (trefoil complement over a base of type `S¹`;
  the Alexander module appears in `H_1` of the base change). Independent of Cisinski's properness theory.
- **F3-6 (sharpening, from the earlier review / the companion; argument re-checked by me).** `W_Z ⊂ W` holds
  for every **weak** localizer (absolute Theorem A, i.e. Grothendieck's own Déf. 1.1) satisfying the **cube**
  axiom (6 b): apply (6 b) to the map of two-cone covers `(X, C_+X, C_−X, ΣX) → (Y, C_+Y, C_−Y, ΣY)` of a homology
  isomorphism `f`; the cone maps are in `W`, and `Σf` is a homology isomorphism which is a weak equivalence
  (for connected `X`, between simply connected spaces; in general `ΣX ≃ ⋁ ΣX_i ∨ ⋁ S¹` and one argues on
  universal covers), so in `W∞ ⊂ W` by Cisinski 6.1.18. So "the least localizer with (6 b) is `W_Z`" does not
  depend on the open point A.16; the single-square form (6′ b) does (it uses B.2).
- **F3-7 (structure theory, open).** Reversible localizers correspond to classes `A` of pointed spaces closed
  under contractible homotopy colimits, two out of three in cofibre sequences, and desuspension; I showed such a
  class is a smash ideal, closed under extended powers, `Ω^n Σ^n`, `Q`, and that on finite complexes it is a
  thick subcategory of finite spectra (so Hopkins–Smith classifies its finite part). Whether `A` is always
  determined by its suspension spectra is F.14 (1) = hunch H4.
- **F3-8 (connection between returns 2 and 3).** The category `Z ≃ S²` of the appendix is the common source of:
  `Ψ` not totally aspherical (return 2), "every sieve is a cofibration iff `W ⊃ W_1`" (H.5), the failure of the
  pushout-product (H.6). The sphere `S²` is the threshold object on the cofibration side (Cisinski 9.2.17), as
  the acyclic non-contractible space is the threshold object on the reverse side.
- **F3-9 (connection to recent results).** OpenAI family 317 (Thomason model structures on strict
  `n`-categories, claimed, unrefereed) uses for `n = 2` the Grothendieck–Cisinski theory of basic localizers; by
  F3-2 the properness of such Thomason-type structures is where "enough fibrations in Grothendieck's sense"
  lives. I did not find any 2026 result on fundamental localizers of Cat themselves (search of the scoreboard
  and inventory; see READING_BASE §0).
- **F3-10 (texts).** Edition-level slips confirmed: XII ms. 265 (Prop. 6 quoted backwards); ms. 273 "cartésien"
  for "cocartésien" in Cons 2; XVI ms. 19 "`f_1 = j_1`" for "`f_2 = j_1`"; XVI ms. 39 "à cofibrations" for
  "à fibrations"; XVI Théorème 4.4.13 (4 a) "Loc (7 F)" where Cor. 4.4.6 and both diagrams have "(7)"; XII ms. 263
  direction of `λ`; XII ms. 187 (`a_n` named as the localizer of `n`-types).

- **F3-11 (mine; a result, written up in `RESULT_REVERSIBLE_NOT_STABLE.md`). A reversible fundamental localizer
  that is not detected by spectra.** `W_S` = functors whose homotopy cofibre `C` has `Map_*(C, S^n_(2)) ≃ *` for
  all `n ≥ 2`. It satisfies the full W(7) of Grothendieck, contains `RP^∞ → e` (Miller) and not `RP² → e`, while
  `RT(W) ∋ RP² → e` for every reversible `W ∋ RP^∞ → e` (Kahn–Priddy, Snaith). So the first question of POLES
  F.14 has a negative answer without accessibility; the accessible form reduces to a routine verification.
  The mechanism: the 2-local EHP fibre sequences make the null class of the spheres closed under desuspension.
  Implication for the reading of XII §5 and XVI §3: the axiom W(7 bis) "⇐" does not single out homology
  theories; it singles out the localizers whose aspherical objects are closed under desuspension, and unstable
  homotopy theory (EHP) produces such classes. Framing: new as far as I can tell (the return left the question
  open after a literature search; I have not searched further); it uses only classical theorems, so the check
  asked of GPT-6 Astra is short. Prompt: `PRO_PROMPTS\REVERSIBLE_LOCALIZERS\PROMPT.md`.

## Return 3: compared with the earlier review

Earlier review: `pro_reviews_20261110\3_POLES\REVIEW_author.md` (Claude Fable 5.2 at effort medium, 11 Nov),
opened only after my REVIEW.md was complete.

- **Where it was right.** Its verdict on every central result agrees with mine: XVI Th. 5.4 false in the Loc (6)
  entry; (6 b) forces `W ⊃ W_Z` (B.5, B.6 followed step by step); `W_Z` least; the two corrections to Lead 3;
  D.3; H.8 (it reconstructs the argument correctly); C.5; both readings of `W̃∞`; Lead 6 false. Its five own
  checks (the category `A`, the two-cone category, `K(g)` for the fold, `α`, the 456 monotone maps) agree with
  mine where they overlap. It found no false statement; neither did I.
- **What it did not check (by its own list) and I did:** all of Part A (the axioms against the text; the proof
  of Brown's lemma A.8; A.13–A.15; A.19 with Cisinski 6.1.18 opened); C.8–C.10; E.3; E.4; E.7; F.9–F.13; Part G
  including G.8, G.17, G.19 and the main steps of G.26; H.2–H.7. It opened none of Cisinski's Astérisque 308; I
  opened Déf. 3.3.2, Prop. 4.2.4, Cor. 4.2.22, Th. 5.2.15, 6.1.11–6.1.18.
- **What it missed.** (1) Loc (8) automatic and the identification "spécial = accessible", with the answers to
  XVI ms. 122–123 and 7.9 (F3-4). (2) That Grothendieck's inference in 7.9 (model structure ⇒ (7 F)) is invalid.
  (3) An independent proof of the failure of (7 F) for `W_Z` (F3-5). (4) The criticism of the prompt's Part H
  (stability asked for the unpointed derivator). (5) The partial structure theory of reversible classes (F3-7).
- **What it had and I lacked.** The comparison with the companion's blocks, and from it the sharpening F3-6
  (minimality of `W_Z` for weak localizers under the cube axiom), which I then checked. Its list of sixteen
  companion rows to change is a work list I did not make (it is outside my task).
- **Where it was too weak.** It reports "proved" for the central items on the strength of B and D alone and
  lists the rest as unverified; nothing in it is wrong.

## Return 4 (GALOIS): findings so far (Parts A and B reviewed; Parts C–G not yet read)

Verdicts so far: 22 rows of 74 (A.1–A.8, B.1–B.14): 20 correct, 2 unproved (B.13, B.14: the return's own open
questions). Review: `..\4_GALOIS\REVIEW.md`. No comparison with the earlier review yet (my review is not complete).

- **F4-1 (return, checked).** `W^1` (full faithfulness on locally constant coefficients) is not a localizer: it
  fails two out of three (A.5: `e → BC_2 → e`). I had this before reading (`work\checks_4\own_thoughts_before_reading.md`).
  The GALOIS prompt's Lead 1 is false for `W^1`.
- **F4-2 (return, checked; against my expectation).** The relative Theorem A holds for `W^lc_D` for every derivator
  with Der 1–4, no enhancement (B.3). One input not yet opened by me: Cisinski 2009, *Locally constant functors*,
  Th. 3.6/3.13 for an arbitrary subcategory.
- **F4-3 (return, checked, with my own direct argument for non-properness).** The two localizers of a derivator sit
  at opposite poles (B.6, B.7): `W^lc_D` never has the reverse cofibration axiom; the constant `k`-homology
  localizer has it and has none of Loc (7 a, b, c, F); `W^lc_{D(k)}` has Loc (7 F) iff no prime is invertible in `k`
  iff it is `W∞`. My test for non-properness: a `W`-equivalence between spaces that are null for all `W`-aspherical
  spaces (`K(Z, 2) → K(Z[S⁻¹], 2)`, `K(Z, 2) → K(∏ Z_p, 2)`).
- **F4-4 (mine).** Criterion: an accessible fundamental localizer is proper (= Loc (7 F), F3-2) iff the homotopy
  fibres of all localization maps `X → L_W X` are `W`-aspherical. For `W^lc` of `E`-local spectra, `L X = B L_E ΩX`
  on simply connected `X`; so it is proper iff for every connected loop space `Z`, `π_1 Z → π_1 L_E Z` is onto and
  the fibre of `Z → L_E Z` is `E_*`-acyclic. Granted Bousfield's theorem that `K(n)_*`-equivalences are
  isomorphisms on `H_1(−; Z/p)` (from memory, not opened), `W^lc` of `K(n)`-local spectra is not proper: the
  instance `E = K(1)` that B.14 leaves unevaluated. `E = KU` stays open.
- **F4-5 (return B.10–B.12, checked; connection between returns 1 and 4 and the CATHOT expert).** The
  cardinal-controlled Kan–Thurston theorem and "small ind-objects of `Cat hot` see at most 1-types" are proved in
  GALOIS by a construction different from the CATHOT expert's (`..\1_CATHOT\OWN_RESULTS.md`, 3.1–3.2), which I
  also read (`CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`). Two proofs by two systems. This is the project's envelope
  finding (V ms. 37, 46) in its ind-form.
- **F4-6 (mine; a result, `RESULT_FILTERED_BY_ONE_TYPES.md`; found on 12 Nov while revising the prompts).**
  **A small category is filtered iff colimits over it of sets and of groupoids are homotopy colimits**;
  equivalently iff `∫_A D → colim^{Cat}_A D` is in `W∞` for every `D: A → Cat`. Proof: totality gives common
  successors and makes the Bousfield–Kan spectral sequence collapse on permutation coefficients; for a parallel
  pair `u, v` the right-angled Artin groups of the bipartite graphs `f — fu`, `f — fv` have `π_1(hocolim) = Z²`
  and `H_2(hocolim) = Z[* ⊔_{colim E} *]`, `E` the functor of equalizing arrows; 1-truncatedness forces
  `E ≠ ∅`. What it settles: the question of F2-13 and of Part F of the draft PRESHEAF_TOTALITY; the true form of
  Grothendieck's conjecture at II ms. 36ter (false for set-valued diagrams: `Δ_inj`; true when `Cat`-valued
  diagrams are allowed); it bears on VII §10. New as far as I know; no literature search; unchecked. Framing:
  "totalement asphérique" is the 0-truncated half of filteredness, and the 1-truncated half is what `Δ_inj` lacks.
  Abelian remark: 1-truncatedness for diagrams of abelian groups already gives exact abelian colimits and
  siftedness.
- **F4-7 (prompt, judged).** The GALOIS prompt says an acyclic group gives `BA → e ∈ W_D ∖ W^1`; for a map to the
  point `W_D` and `W^1` agree (A.3), so that sentence is wrong. (To be completed when the review is.)
