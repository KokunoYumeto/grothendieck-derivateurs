# Shape of the companion after PRETOT

Claude Fable 5.2 (effort max), Dérivateurs expert, 12 November 2026. Inputs: the review of PRETOT by Claude Opus
5.5 (§§1–2, 10–11) and its FINDINGS. Nothing else read; no new mathematics.

## 1. Shape

Write these places as classifications.
- **II ms. 36–36ter.** Total = colimits of sets are homotopy colimits. Componentwise filtered = the same for
  `Cat`-valued or abelian diagrams (F.4, F.6). Among sifted categories total = filtered (F.3), so `Δ°` is not
  total; `Δ_inj` separates. Drop the route through Contre-exemple 2.20.
- **XII ms. 87–114.** Presheaf totality: on `Δ`, the acyclic, resp. contractible, simplicial sets (A.2); on
  finite-height bases, only representables (A.10; answers the footnote at ms. 108). `W_Z` and `W∞` differ
  exactly by `π₁(U/H)` (A.5). Sieve classes: the table of B.3; ms. 111, 113, 114 answered (B.2, D.2).
- **XII ms. 102–103 and Déf. 2:** E.3, E.5, E.6, E.8. **XIIapp:** one category of type `S²` at ms. 9, 10–11, 15;
  the gluing is POLES G.19. **VII §§4–6, §10:** F.12–F.15; F.16 waits for PATHS.

My results. Confirmed: the theorem on filtered shapes, with the hypothesis corrected to non-empty connected
(my step took `colim_A * = *`; correction added to `RESULT_FILTERED_BY_ONE_TYPES.md`); `H₁ = Z²⁸`; F2-11; F-G4;
F-G1 (finite witnesses). Proved by the return: my hunch H7 (F.3) and the abelian form (F.6). Refuted:
my hunch H3 (A.5); I expected the opposite. Open: H1, total ⇒ exact.

## 2. Next pushes, in order

1. Review PATHS (A.P2, C.P2 against F.16): it gates the VII blocks and INDLOCAL Part C.
2. TOTAL_EXACT with the review's edits: total ⇒ exact is the one open inclusion; `Ty^op` first.
3. Finish the GALOIS review (Parts C–G), then STRATA, BISITE, RESIDUE.
4. REVERSIBLE_LOCALIZERS.
5. One follow-up for C.4, E.9, F.10, F.16 and the extension of A.5 to `End_Δ([n])`.

## 3. Unsent prompts

- **REVERSIBLE_LOCALIZERS.** Part G.1 states "every accessible `W` is `W_D` for `D = HOT_W`" as fact; it is my
  unchecked aside: make it an item to check. R10 (c) rests on a theorem of Bousfield quoted from memory (E.4
  says so). Part E.1–E.2 duplicates the planned H6 prompt.
- **INDLOCAL.** Parts C3–C4 must not use PATHS before its review (the inserted text says so).
- **FINMON.** `PRO_PROMPT_EMAIL_CLAIMS.md` was its byte-identical copy; if only FINMON was edited, keep one.
- **S2COUNT.** In R4, "finitely dominated ⇒ `[BC, S²]` countable" is my one-line remark, unchecked: label it.
