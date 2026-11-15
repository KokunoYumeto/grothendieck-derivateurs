# PRETOT: the effort-max review of 12 November 2026

Review by Claude Opus 5.5 (Anthropic), effort max, of the return PRESHEAF_TOTALITY (PRETOT) of GPT-6 Astra (ChatGPT
Pro mode), 12 November 2026. The return is in [`../../pro_returns/PRETOT/`](../../pro_returns/PRETOT/), the prompt in
[`../../prompts_max_20261112/PRESHEAF_TOTALITY/PROMPT.md`](../../prompts_max_20261112/PRESHEAF_TOTALITY/PROMPT.md).

- `REVIEW.md`: the verdict on each of the 54 statements, the sources opened, the computations.
- `FINDINGS.md`: the findings F1–F21 that REVIEW.md refers to. F1 carries the check made after the review: the
  presentation complex of PRETOT Theorem A.5 is homotopy equivalent to Σ(2,3,5) minus an open ball, by Nicholson's
  Theorem A (arXiv:1905.12018) with m_ℍ(2I) = 2 computed exactly; the proofs of Nicholson's theorems and of Swan's
  cancellation theorem were not re-checked. `FINDINGS_before_poincare_20261112.md` is the file before that check
  was added.
- `POINCARE_SPINE_CHECK.md`: the check itself (Claude Opus 5.5, effort max, 12 November 2026), with its programs and
  outputs in `scratch_poincare_spine/scripts/` and `scratch_poincare_spine/out/`.
- `rerun/`: the rerun of the return's eleven programs. `rerun/out/` holds the outputs and `COMPARISON.txt`;
  `rerun/tools/` the scripts that ran and compared them; `rerun/indep/` the reviewer's own programs with their
  outputs. Of `rerun/pro_code/`, the copy of the return's programs, only the files whose content differs from the
  return's are here (the programs themselves are in `../../pro_returns/PRETOT/code/`).

Not included: the papers and book chapters by other authors read for the Poincaré check (Swan 1983 from GDZ,
Kirby–Scharlemann's *Eight faces of the Poincaré homology 3-sphere*, Hatcher's *Algebraic Topology* and his notes on
3-manifolds, Nicholson arXiv:1905.12018), with their extracted text and page renderings. The check cites each at the
place used.

In these copies the first name of the user who ran the project is replaced by "user", local paths included. Not
checked by a person; no priority claimed.
