# Texts to insert: Dérivateurs line

Claude Fable 5.2 at effort max (Dérivateurs successor), 13 November 2026, after 16:05 local (last clock reading; the
context guard then stopped all commands, so the time of writing is not checked and the lint was NOT run on these
blocks: run `push_rule_pro_prompts.py --lint-math` on each prompt after pasting). Written from what I had read
before; nothing opened for it. Each block names its target and place. The text to paste is between the rules of
its block. Where I have not read the target prompt (DER_FOLLOWUP beyond its outline, REVERSIBLE_LOCALIZERS), the
place is given by subject and the numbering is to be adjusted. Statements marked "Lead" are mine and unchecked.

## 1. FRAISSE_EXACT, Part C: new item 7, after item 6 ("Prove or refute (conference item FE-3) ...")

---
7. A test of R11 in degree 2 over an index with four objects (from the reply of the previous Dérivateurs expert,
   Claude Fable 5.2 at effort max, at the experts' conference of 13 Nov 2026; not checked by the drafter). Let `X` be
   the exit-path category of `P¹` stratified by `{0, 1, ∞}`. As the drafter reads it: objects `0, 1, ∞, U`;
   `X(U, U) = π_1(P¹ ∖ {0, 1, ∞}) = F_2 = ⟨γ_0, γ_1, γ_∞ | γ_0 γ_1 γ_∞ = 1⟩`; `X(x, U) = F_2/⟨γ_x⟩` for
   `x ∈ {0, 1, ∞}`, with `F_2` acting by composition; no other non-identity arrows. First write `X` down completely
   from the exit-path construction (the side on which `F_2` acts, the composition) and correct this description if
   it is wrong. Then prove or refute each of the following.
   (a) `BX ≃ S²`; so for the constant diagram `T_1(Z) = 0` and `T_2(Z) ≅ Z`.
   (b) `lim¹_{X^op}` of the constant diagram `R/Z` is `0` and `lim²_{X^op}(R/Z) ≅ R/Z`: compute both from the cobar
   complex, give a cocycle generating `lim²`, and check the result against R11.
   (c) `X` is not quasi-filtered: the pair `id, γ_0: U ⇉ U` has no affine equalizer over any non-zero ring (the group
   ring of `F_2` over a domain has no zero divisors). Give a diagram `M: X → Ab` with `T_1(M) ≠ 0` and the dual
   torsor diagram on `X^op` without a point.
   (d) Decide (CH), (CC) and (CT) for `X` (its hom-sets are infinite, so (Re) as defined does not apply; `F_2` is not
   amenable). Say in one statement what this index shows: for constant compact coefficients the first non-zero
   derived limit is in degree 2, while non-constant ones already have `lim¹ ≠ 0`.
---

## 2. FRAISSE_EXACT: the cross-reference

(a) Header, paragraph "Related prompts": replace the sentence "none of that is to be done here. Part B.5 below treats
one category only and feeds that prompt." If the new A.2 of block 3 is adopted, also delete there the words "and for
a second check of TOTAL_EXACT_2 C.10, C.19–C.28".

---
none of that is to be done here. Parts B.5 and B.6 below concern the categories of setting (S) only; the general
question whether `𝒬_n = 𝒬_{n+1}` for some `n ≥ 2`, for all small categories (PRETOT C.4), stays in DER_FOLLOWUP,
Part A.3.
---

(b) Part B, end of item 6 (after "... and (FA) fails for them over bases that are empty in one sort."): append.

---
   State every separation found here in the form DER_FOLLOWUP Part A.3 needs: the category given completely, the
   proof that every action component is `(n−1)`-connected, and a named non-zero class in `H_n` of a named action
   component.
---

## 3. DER_FOLLOWUP

(a) Part A, item 2 (the item that begins "The implication of PRETOT C.4 fails for `n = 2`"): replace the whole item.

---
2. The implication of PRETOT C.4 fails for `n = 2`, by Lead 1 (c) and R14. The proofs behind R14 (TOTAL_EXACT_2
   C.10, C.19–C.28) have been read in full twice on our side: by the intake (Claude Fable 5.2 at effort high) and by
   the field expert (Claude Fable 5.2 at effort max, 13 Nov 2026): no gap; the step of C.27 that reruns C.19 with
   components as the marked pair is written out in `reviews/REVIEW_MAIN_PROOFS_TOTEX2.md`, §4 (attached). They are
   not an item here; rule 7 applies where you use them. Write out the counterexample of Lead 1 (d): the category
   `E^◁`, its cosieve, and both verifications. (A second witness that needs no construction by stages is expected
   from the prompt FRAISSE_EXACT, Part B.5: the category of TOTAL_EXACT_2 A.11, finite sets with a linear order and
   an independent cyclic order, whose classifying space is simply connected with `H_2 = Z`. It is not asked here.)
---

With it: add `reviews/REVIEW_MAIN_PROOFS_TOTEX2.md` to the zip (source:
`derivateurs_companion_20261109/pro_reviews_max_20261112/DERIVATEURS_EXPERT/REVIEW_MAIN_PROOFS_TOTEX2.md`) and to
"What is attached"; in the status lines of R14 and R17 replace "read ... in the intake" by "read in full by the
intake (Claude Fable 5.2 at effort high) and by the field expert (Claude Fable 5.2 at effort max): no gap"; in R14
name `K*` as "the Adámek–Koubek–Reiterman construction with the repaired quasi-filters".

(b) Part A, item 3: delete the sentence or sentences that propose the predimensions `δ = a|V| − b|E|` as a route
(added on 13 Nov from the intake's block; they contain the word "predimension"), and put this in their place.

---
   Routes, with what is known about each.
   (i) Not the predimension family: for `δ = a|V| − b|E|` on ordered `k`-uniform hypergraphs, with `a, b ≥ 1`
   integers, the proofs of TOTAL_EXACT_2 A.21 and A.30–A.34 use only submodularity, integrality and positivity, so
   every such category is expected to be total and to lie in every `𝒬_n`. This is asked in the prompt
   FRAISSE_EXACT, Part D.1, and is not to be redone here.
   (ii) The Galois route (Lead of Claude Fable 5.2 at effort max; unchecked; its proof and the search among Fraïssé
   classes are asked in FRAISSE_EXACT, Lead 7 and Parts B.2, B.5, B.6). Let `A` be the category of strong embeddings
   of a Fraïssé class with limit `M` and group `G = Aut(M)`, with an amalgamation that is functorial over
   non-empty bases. Then every action component of `A` is equivalent to the category `E_U` of an open subgroup
   `U ≤ G` (objects: the finite strong `B ⊆ M` with `G_B ≤ U`; arrows `B → C`: the maps `u|_B`, `u ∈ U`, `uB ⊆ C`). If
   moreover every open subgroup is the pointwise stabilizer `G_F` of a finite strong set, every action component is
   weakly contractible or weakly equivalent to `A`, so `A ∈ 𝒬_n` if and only if `BA` is `(n−1)`-connected. On this
   route a separation `𝒬_n ≠ 𝒬_{n+1}` is such a class with `BA` `(n−1)`-connected and not `n`-connected; `n = 2` is
   expected from the category of TOTAL_EXACT_2 A.11. If the return of FRAISSE_EXACT (prefix `FREX`) is attached,
   use its statements with their numbers; otherwise prove these two sentences before using them.
   (iii) Not by joins (Lead, unchecked): for `A = (A_1^◁ × A_2^◁) ∖ {(∅, ∅)}` one has `BA ≃ BA_1 * BA_2`, but the
   objects with non-empty first coordinate form a cosieve weakly equivalent to `A_1`, hence an action component;
   a join is never in a higher `𝒬_n` than its factors.
   The question of this item is the general one, for all small categories, and its outcome is as stated under
   "For Part A in particular".
---

(c) Section "Leads": new Lead after the last one (Lead 6 if the Leads are numbered 1–5), and Part A: new item after
item 3.

---
**Lead 6 (hunch H2 of the first Dérivateurs expert, Claude Fable 5.2 at effort max; not checked).** For a
fundamental localizer `W ⊇ W∞`, a non-empty small category `A` is total for `W` if and only if `A` is `W`-aspherical
and, for every action `L: A → Set`, the unreduced suspension of the nerve of every component of `El_A(L)` is
`W`-aspherical. Known cases, each proved separately in TOTASPH: `W∞` (C.5), `W_Z` and `W_R` (D.2, D.12 as numbered
there), `W_n` (D.12: every action component `(n−1)`-connected and `BA` `n`-connected; the covering trick of C.4 turns
the homological condition on all actions into the homotopical one), and the degenerate form D.19 for `W ⊇ W_1`.
Expected: true for the localizers of homology theories and for the `W_n`; not decided for a general `W`.
---

---
4. Prove or refute Lead 6 for every fundamental localizer `W ⊇ W∞`. If it fails, determine the class of localizers
   for which it holds and give, for one localizer outside it, the category and the action that separate the two
   sides. Then express `𝒬_n` and the tower of Part A in these terms: for which `W` is "every action component has
   `W`-aspherical suspension" a condition strictly between two consecutive `𝒬_n`.
---

## 4. REVERSIBLE_LOCALIZERS: two new Parts, after its last Part (letters to be adjusted)

Background they rest on, to attach as LaTeX: the GALOIS return (sections A, B with B.13; its definition of `LC_D`
and `W^lc_D`), the POLES return (D.4–D.6, F.14), `DER_XVI.tex` (XVI ms. 87–96), and the section of the LM8 return
with B.6 and B.9. I have not read LM8; what block (b) says about it is the intake's account.

---
**F. Accessibility of `W^lc_D` (GALOIS B.13; hunch H9 of the first Dérivateurs expert, Claude Fable 5.2 at effort
max), and the localizers of group quotients.**

Setting. Two universes `𝒰 ∈ 𝒱`. A derivator is a prederivator on the `𝒰`-small categories with values in
`𝒱`-categories that satisfies Der 1–4, as in the GALOIS return. `LC_D(X) ⊆ D(X)` is the full subcategory of locally
constant objects and `W^lc_D` the class of functors `f: X → Y` of `𝒰`-small categories with `f*: LC_D(Y) → LC_D(X)` an
equivalence. A fundamental localizer is accessible when it is the smallest fundamental localizer containing a
`𝒰`-small set of functors.

1. Prove or refute: for derivators `D_i` indexed by a set `I ∈ 𝒱`, the product `∏ D_i` is a derivator and
   `W^lc_{∏ D_i} = ⋂_i W^lc_{D_i}`.
2. Prove or refute, in ZFC with the two universes and Vopěnka's principle for `𝒰`: `W^lc_D` is accessible for every
   derivator `D`. Expected: true, from Cisinski, Astérisque 308, 4.2.17 (open it and derive the statement used).
3. Prove or refute, in ZFC with the two universes and the hypothesis that `𝒰` contains no measurable cardinal: there
   is a derivator `D` for which `W^lc_D` is not accessible. Lead (unchecked): by item 1 one needs derivators `D_κ`,
   `κ` a cardinal of `𝒰`, with `⋂_κ W^lc_{D_κ}` not accessible; the expected source is the theorem of Casacuberta,
   Scevenels and Smith (2005, to be opened) that without measurable cardinals some localization with respect to a
   proper class of group homomorphisms is not a localization with respect to a set, carried to fundamental
   localizers containing `W_1` through the localizers of item 5.
4. Prove or refute in ZFC: for a represented derivator `X ↦ C^X`, `C` complete and cocomplete, `W^lc` is `W_1` when
   `C` is not a preorder and `W_0` when it is a preorder with more than one isomorphism class. Lead (unchecked):
   `LC(X) = Fun(Π_1 X, C)`, and the powers `c^I` carry the symmetric groups. So represented derivators do not
   decide item 3.
5. The localizers `W_𝔞` of LM8 B.6 (for a quotient functor `𝔞` on groups: abelianization, `π/π''`, `π/Γ_{c+1}`, the
   pro-`ℓ` completion, the rational unipotent completion, the virtually abelian pro-quotient; definition as in
   LM8 B.6, each a fundamental localizer containing `W_1`; LM8 B.9 classifies the finite coverings in `Fib_{W_𝔞}`).
   For each `𝔞` of the list decide, with proof: (i) whether `W_𝔞` is accessible, with a generating set; (ii)
   whether it satisfies Loc (6 b), equivalently (POLES, Lead 3 there) whether it contains `W_Z`: expected yes for
   the abelianization, the nilpotent quotients and the two completions (Stallings), to be decided for `π/π''` and
   the virtually abelian quotient; (iii) whether it is of the form `R(L)`: expected no for every `𝔞` with
   `W_𝔞 ≠ Fl(Cat)`, because `S² → e` lies in `W_1`; (iv) `Fib_{W_𝔞}` on all functors, beyond finite coverings. Then
   prove or refute: the fundamental localizers containing `W_1` correspond to the classes of groups closed under
   the operations you determine, `W ↦ {G : BG is W-local}`, and place the `W_𝔞` in that correspondence.

This Part is finished only when each of its items is proved or refuted; the hunch "accessibility is not decided by
the axioms of a derivator" is the conjunction of items 2 and 3 and is settled only by both.
---

---
**G. Simple homotopy types in `Cat` (XVI ms. 87–96; POLES D.4–D.6; hunch H5 of the first Dérivateurs expert,
Claude Fable 5.2 at effort max).**

Where it comes from. At XVI 6.4 b)–6.5 Grothendieck looks for a localizer strictly inside `W∞` whose homotopy
category would carry Whitehead torsion, asks for "opérations élémentaires à la Whitehead dans Cat" (ms. 88–89), and
notes at ms. 95 that for the hexagon `I` the subdivision `sd(I)` and `I` are not homotopic in `Cat`. POLES D.4–D.6
(to be re-read in the attached return): no fundamental localizer does it, and `sd(I) → I` is a simple homotopy
equivalence without a categorical homotopy inverse. Throughout, posets are finite, `K(P)` is the nerve, maps are
order-preserving.

1. Prove or refute: `P` and `Q` are connected by a zigzag of maps each having a left or a right adjoint if and
   only if their cores (no beat points) are isomorphic. Expected: true (Stong; Barmak–Minian, to be opened); so
   adjunctions alone give the strong homotopy types, which are finer than simple homotopy types: give two posets
   with collapsible nerves and non-isomorphic cores.
2. Prove or refute: `K(P)` and `K(Q)` have the same simple homotopy type if and only if `P` and `Q` are connected
   by a zigzag of maps each of which either has a left or a right adjoint or is a subdivision map `sd(R) → R`.
   Not decided by the drafter.
3. Prove or refute: `K(P)` and `K(Q)` have the same simple homotopy type if and only if `P` and `Q` are connected
   by a zigzag of inclusions `R ∖ {x} ⊆ R` that are weak equivalences. Expected: true (one-point extensions along
   a weakly contractible link have zero torsion; Barmak–Minian for the converse). Then say which of these
   inclusions are Dwyer immersions with a retraction by an adjunction, and so give Grothendieck's elementary
   operations in `Cat` an exact form.
4. Prove or refute: for every finitely presented group `π` and every `τ ∈ Wh(π)` there are posets `P, Q` and a map
   `f: P → Q` in `W∞` with torsion `τ`; and `τ(f) = 0` whenever `f` is a composite of maps of the kind in item 2.
5. Prove or refute: the Whitehead torsion of a map of posets in `W∞` depends only on its class in the 2-category of
   posets, functors and natural transformations localized at the maps of item 3, and on no fundamental localizer.
   State the precise invariance and prove it, or give the map that violates it.

**Outcome for this Part.** Each of items 1–5 is finished only when it is proved or refuted. A list of the known
theorems on finite spaces does not finish an item: "Known" counts only with the derivation, from the opened source,
of the statement as it is worded here, for all finite posets. An item that is refuted comes with the strongest true
statement in its place.
---
