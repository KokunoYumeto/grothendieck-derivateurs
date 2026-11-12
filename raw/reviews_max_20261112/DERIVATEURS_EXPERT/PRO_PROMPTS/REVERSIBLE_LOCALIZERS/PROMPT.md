# REVERSIBLE_LOCALIZERS: the localizers with the reverse cofibration axiom, and the fibrations of `W_Z`

Draft of 12 Nov 2026 by Claude Fable 5.2 (effort max), Dérivateurs expert, for GPT-6 Astra (ChatGPT Pro mode).
Follow-up to POLES (return 3). File prefix: `REVLOC`. To attach: the POLES return (paper, sections B, C, D, E, F,
H; results CSV); `3_POLES\REVIEW.md` of 12 Nov; `RESULT_REVERSIBLE_NOT_STABLE.md`; `HUNCHES.md` (H4, H5, H6);
Grothendieck's text `DER_XIIb-a` (XII ms. 75–85), `DER_XIIc-b` (XII ms. 265–275), `DER_XVI` (ms. 1–27, 83–96,
119–124); Cisinski, *Les préfaisceaux comme modèles des types d'homotopie*, Astérisque 308 (chapters 4, 6, 9).

## Where this comes from

XII ms. 75–78 and XVI ms. 16′–27: Grothendieck's axiom W(7 bis) = Loc (6′) for a class `W` of functors: in a
square of two sieves `U, V` covering `X` with intersection `S`, `S → U ∈ W ⇔ V → X ∈ W`. He calls the
implication "⇐" "inhabituelle" (XII ms. 270) and believed that `W∞` has it (XII Théorème 2; XVI Théorème 5.4).
POLES proved (checked in the review): for fundamental localizers in the sense of Cisinski (relative Theorem A),
"⇒" always holds; "⇐" is equivalent to the cofibre criterion (`g ∈ W` iff the homotopy cofibre `C(g)` is
`W`-aspherical; B.5); the smallest localizer with "⇐" is `W_Z` (B.6, D.1); "⇐" together with Loc (7 F) forces
`W = Fl(Cat)` (H.8); every localizing subcategory `L` of spectra gives a reversible localizer
`R(L) = {g : Σ^∞ C(g) ∈ L}` (F.2), and `T(W) = loc{Σ^∞ C(g) : g ∈ W}` is a Galois adjoint (F.4). POLES left
open (F.14): is every accessible reversible localizer of the form `R(L)`?

The reviewer's note `RESULT_REVERSIBLE_NOT_STABLE.md` claims: no, when accessibility is dropped. `W_S`, the class
of functors `g` with `Map_*(C(g), S^n_(2)) ≃ *` for all `n ≥ 2`, is a reversible fundamental localizer,
`RP^∞ → e ∈ W_S`, `RP² → e ∉ W_S`, and `RP² → e ∈ RT(W)` for every reversible `W ∋ RP^∞ → e`.

## What the outcome must be

Deliverables: `REVLOC_paper.tex` and PDF (LuaLaTeX), `REVLOC_results.csv` (one row per numbered statement:
`id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`), `REVLOC_references.bib`
(each entry marked opened / not opened), `REVLOC_report.md`, `code/` with outputs.

What counts as done, per item: (a) a theorem with a complete proof; or (b) a complete counterexample (every
space, map and hypothesis verified; finite data machine-checked); or (c) failing both: the cases proved, the
computations run, and the obstruction as one exact statement with the smallest undecided instance. A classical
theorem may be quoted only with its exact statement, source and theorem number, and the derivation of the form
used here.

Not acceptable: a survey of localization theory; "plausible" or "expected" in place of (a)–(c); accepting any
step of the reviewer's note without re-deriving it (in particular Lemma 1, the retraction rule for `W_S`, and
the use of Kahn–Priddy); a set-theoretic argument for accessibility that does not treat the desuspension step;
a description of `Fib_{W_Z}` by bounds only.

Finished only when Parts A and B are each decided in sense (a) or (b), and every item of Parts C–F has reached
(a), (b) or (c). On disconnection: retry for ten minutes, then write all files out in the chat and continue.

## Parts

**A. Check and complete the reviewer's theorem.**
1. Prove or refute Lemma 1 of the note: for a pointed CW complex `X`, if `Map_*(ΣX, S^m_(2))` is weakly
   contractible for all `m ≥ 2`, then so is `Map_*(X, S^n_(2))` for all `n ≥ 2`. State the form of James's
   2-local fibre sequence `S^n → ΩS^{n+1} → ΩS^{2n+1}` you use, with source, and check the case `n = 2`.
2. Prove or refute: `W_S` satisfies the retraction rule, the relative Theorem A, and the cofibre criterion.
3. Prove or refute step (c) of the note: `loc(Σ^∞ RP^∞) = loc(S/2)` in `Ho(Sp)`. Give the exact statement of the
   Kahn–Priddy theorem used (a section of spaces, not of infinite loop spaces) and of Snaith's splitting.
4. Do the same at an odd prime `p` with `BZ/p`, `M(Z/p, 1)` and Toda's fibrations, or show where it breaks.

**B. Accessibility.** Decide in ZFC whether there is an accessible reversible fundamental localizer that is not
of the form `R(L)`. The reviewer's route: for regular uncountable `κ`, the class `𝔑^κ` of spaces in `𝔑` all of
whose `< κ`-cell subcomplexes lie in `< κ`-cell subcomplexes belonging to `𝔑`. Prove that `𝔑^κ` is closed under
pointed homotopy colimits, two out of three in cofibre sequences, and desuspension, and is generated under
homotopy colimits by a set; or find the step that fails and give another construction; or prove that every
accessible reversible localizer is `RT`-fixed.

**C. The smallest reversible localizer containing a given map.** For `RP^∞ → e`: determine its class `A` of
aspherical spaces as far as possible. Decide for each of the following whether it lies in `A`: `K(Z/2, n)`;
`Q(Σ^m RP²)`, `m ≥ 1` (the reviewer claims yes); `(Q_0 S⁰)_(2)`; the stunted projective spaces `RP^∞_k`;
`RP^{2k}` (the reviewer claims no, since `A ⊂ 𝔑`); the fibre of `S^n → K(Z/2, n)`. Describe its local objects:
prove or refute that a 2-complete simply connected finite complex is local.

**D. Classification.** Prove: the accessible reversible localizers correspond to the classes `𝒵` of pointed
spaces (closed under what `W`-local spaces are closed under) whose null class
`{X : Map_*(X, Z) ≃ * for Z ∈ 𝒵}` is closed under desuspension. Then:
1. Give a necessary and sufficient condition on a single space `Z` for the null class of `{Z}` to be
   desuspension-closed (sufficient: `Z` is an infinite loop space; or `Z` sits in fibre sequences
   `ΩZ'' → Z → ΩZ'` with `Z', Z''` in the family). Decide it for: `S^n` (not localized), `S^n_(p)`, `M(Z/p, n)`,
   `K(G, 1)` with `G` nilpotent, `BU`, a finite `H`-space.
2. For a reversible `W`, `T(W) ∩ {finite spectra}` is a thick subcategory. Prove this, and prove that every
   thick subcategory of finite spectra (every Hopkins–Smith type function) occurs for some reversible `W`.
3. Decide whether the reversible fundamental localizers form a set, and whether the lattice of reversible
   localizers between `W_Z` and `W_0` has a largest element other than `Fl(Cat)`.

**E. The intrinsic fibrations of homology.** `Fib_W` is the class of functors `p: E → B` such that strict base
change along `p` maps `W`-maps over `B` to `W`-maps (XVI ms. 28). POLES C.10 bounds `Fib_{W_Z}` from both sides.
1. Prove or refute: `p ∈ Fib_{W_Z}` iff (i) all `E_b → E/b` and `E/b → E/b'` are integral homology
   isomorphisms and (ii) for every integral homology isomorphism `u: Y' → Y` over `B` and every `q`,
   `H_*(Y'; u^*ℋ_q) → H_*(Y; ℋ_q)` is an isomorphism, where `ℋ_q(b) = H_q(E/b)`.
2. Characterize the local systems `M` on a space `B` such that `H_*(Y'; u^*M) ≅ H_*(Y; M)` for all homology
   isomorphisms `u` over `B`; decide whether these are the systems on which `π_1(B, b)` acts nilpotently
   (first cases: `B = S¹`; `B = S¹ ∨ S¹`).
3. Reprove directly, from 1, that `e → S` with `BS ≃ S¹` has no factorization into a homology isomorphism
   followed by a member of `Fib_{W_Z}` (the reviewer's argument with the trefoil complement and the Alexander
   module, row C.5 of the review), and determine all `f: X → Y` that do have such a factorization.

**F. The literal axioms.** Grothendieck's own definition (XVI Déf. 1.1) has the absolute Theorem A (Loc (3)),
and he doubts the relative one (footnote 56, ms. 118: "Loc (3 bis) pas prouvé, probablement faux").
1. Prove or refute: every class satisfying Loc (1), (2), (3) of XVI satisfies Loc (3 bis). First case: a base
   `[1]`. If refuted: give a class with (1, 2, 3), not (3 bis), and say whether it can satisfy (6′ a), (8), (9).
2. Prove: `W_Z` is the least class with Loc (1, 2, 3) and the cube axiom Loc (6 b) (no relative axiom), by the
   two-cone cube of a homology isomorphism; treat non-connected sources.

**G. Statement of results** against XII ms. 75–78, 265–275; XVI ms. 16′–27, 79, 83–96, 105, 119–124; POLES
F.14, C.10, A.16; and the literature (Bousfield 1994, 1997 on nullity classes; Dror Farjoun 1996;
Berger–Ratković 2019 on excisive model categories; Casacuberta–Scevenels–Smith 2005): for each statement
proved, say after opening the source whether it is there, with theorem number.

Rules of proof and conventions: as in the common block of the POLES prompt, with one change: "fundamental
localizer" means Cisinski's definition (relative Theorem A) unless Part F says otherwise; say so on page 1.
