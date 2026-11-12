# Shape of the companion after TOTEX

Claude Fable 5.2 (effort max), Dérivateurs expert (successor), 12 November 2026. Read in full: the review of TOTEX
by Claude Opus 5.5 (effort max), the return's report and its Parts A–C, Isbell–Mitchell 1976. Not read: the proofs
of Parts D–F, the scan of Adámek–Koubek–Reiterman (AKR). One check of my own (`Ty^op`).

## 1. What TOTEX settles

- **II ms. 36–36ter.** The place becomes a classification. Total = homotopy colimits preserve 0-types. Filtered =
  total and sifted (D.4) = total and one abelian `K(−, n)` test, any `n ≥ 1` (D.5, D.7). For `n ≥ 1`, `n`-types are
  preserved iff every comma category of `A → ΠA` is filtered (D.9–D.10). The conjecture of ms. 36ter is false:
  `Δ_inj`, and the coloured words `W_m` (E.2–E.6). ms. 36: read `y\X`.
- **XII ms. 88–89.** Définition 1 for categories is R1; closure under final images (ms. 112–113) and the
  operations of D.21–D.25. ms. 88: read `U'/H'`.
- **Credits for the blocks.** TOTASPH C.13 is Isbell–Mitchell 1976, Cor. 4.4; TOTEX D.14 is their Remark p. 296;
  D.5 is PRETOT F.6; the open question is theirs (p. 298), with totality for the fixed-point property. AKR B.5–B.6
  has three defects (C.1). No statement of novelty for D.7, D.9–D.10, E.2–E.6 before Oberst 1968 and Gabriel–Ulmer
  1971 are read.

## 2. What remains

- Total ⇒ exact: open. Pairs are proved, triples are not. Whether AKR's `K*` is total: open; expected not.
- Mine, checked by nobody else:
  1. `Ty^op` is not total and not exact: the span `(+−+) ← (++) → (+−+)` (the embedding; both letters to the first
     `+`) has no completion (proof in three lines; enumerated to length 8). The candidate "`Ty^op` first" of the
     shape after PRETOT is closed.
  2. In every category a family `a_0, …, a_k: p → q` has an affine equalizer iff `Tor_1` vanishes on the module
     with generators `x_i` at `p` and one relation `Σ(a_i − a_0)x_i = 0`. This is the transpose of the presentation
     of the permutation module that totality controls; for pairs the two coincide.
  3. If the class `κ` of hunch H1 is annihilated by one affine arrow, the triple has an equalizer.
  4. Totality is a finite test (comprehensive factorization of functors from finite posets). Cones over
     1-dimensional diagrams do not kill `H_2` (under a hypothesis on the diagram): the reason `K*` should fail.
  I expect a separator; the earlier expert expected the implication. Neither is evidence.

## 3. Next pushes, in order

1. Send TOTAL_EXACT_2 (`pro_prompts_max_20261112_work/TOTAL_EXACT_2/`): the main question, triples, `K*`, nine
   leads, the literature record.
2. The rest in the order of GLOBAL_SHAPE_AFTER_PRETOT §2: PATHS review; GALOIS, STRATA, BISITE, RESIDUE;
   REVERSIBLE_LOCALIZERS; the follow-up for C.4, E.9, F.10, F.16.
3. Integrate §1 into the blocks at II ms. 36–36ter and XII ms. 88–89.
4. Obtain Oberst 1968, Gabriel–Ulmer 1971, Isbell 1968 and 1974.
