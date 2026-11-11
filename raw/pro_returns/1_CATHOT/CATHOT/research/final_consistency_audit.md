# Final artifact consistency audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

This is a read-only consistency audit of the assembled paper sources, final statement register, report, bibliography, and the attached task prompt. No mathematical source, statement register, bibliography, or report was edited. Compilation logs were not inspected. No new mathematical research was performed.

## Inventory and cross-reference checks

The recursively included paper has exactly **90 distinct assertions**: A 7, B 11, C 6, D 9, E 27, F 13, and G 17. The statuses are **59 Proved, 14 Refuted, 11 Known, and 6 Open**. The final CSV has exactly the same 90 identifiers and statuses, with the required seven column names. Every recorded proof-location file exists.

The open identifiers are **D.6, E.6, E.17, E.26, E.27, and G.17**. This list and the status totals agree with the final report. F.12 is consistently Refuted; no stale assertion that its finite-height questions remain open was found in the assembled deliverables. E.19 is included between E.18 and E.20 and is Known in both paper and register.

All section inputs exist. No duplicate assertion identifiers, duplicate bibliography keys, undefined citation keys, undefined reference labels, or references to nonexistent numbered assertions were found. There are 33 bibliography entries and 30 cited keys. The three uncited entries are BC_Schur1911, MartinianSteinberg2025, and Thomason1979; retaining these as documented consulted or inaccessible references is not a defect. Every bibliography entry explicitly labels verification status. In particular, Thomason1979's phrase "unverified full text:" is a valid status label, not a missing note.

## Two assembly items identified

1. **E.19 text synchronization.** At the audited snapshot, the source uses `\mathcal H_W`, while its CSV row still uses `\mathscr H_W`. No mathematical statement or status differs. Regenerating the register after final TeX edits resolves this mismatch with the report's promise that CSV statements reproduce the normalized source text.

2. **Pending validation program.** The report states that `code/validate_package.py` performs structural/package checks, but that program was not present at the audited snapshot. It should be included with the actual output before that assertion is retained in the final delivered report. The parent was still preparing final validation, so this is an assembly item rather than a finding about the mathematics.

## Scope alignment with the prompt

The main file includes Parts A–G in order, beginning with the universe, variance, localizer, and finiteness conventions. The requested attribution and no-priority statement are present. The manuscript correction table names the requested ranges and now distinguishes the proved canonical path construction from the open arbitrary-cofinal-type and relative/arbitrary-block assertions. The report preserves the same distinction.

D.6 retains the sequential S² question. E.6 retains only the requirement that a strict retraction have the original Cat-hot class, while its following argument supplies the weaker always-existing retraction in the same Hot class. E.17 retains the small-index local-presentation implication and does not confuse it with the proved descent or enlarged-index counterexample. E.26–E.27 retain the original general path-system quantifiers. G.17 retains the RP² poset-arrow minimum and the remaining infinite-dimensional realization classification. These are explicit remaining questions rather than omitted tasks or falsely completed claims.

The finite-model table consistently distinguishes separate object and arrow optimization, finite models from arbitrary small models, and the unresolved interval [28,49]. The report distinguishes local exhaustive computation from the externally imported five-/six-element monoid classification. Bibliography notes distinguish inspected primary versions from inaccessible original texts. The source, register, and report do not claim that a noncompact finite-category nerve is a finite CW test.

## Reproducible check

The audit script is `code/f_final_consistency.py`; its recorded output is `code/f_final_consistency.out`. The script reads the source tree, register, bibliography, and report and does not modify those artifacts. Its recorded discrepancies describe the audit-time snapshot and should be rerun after final assembly to record their resolution.

## Final assembly resolution

Both assembly items were resolved before packaging. The register was regenerated from the final source, including E.19's `\mathcal H_W` notation. `code/validate_package.py` and its successful output are present. The consistency script was rerun against this completed tree; its packaged output is the final run, with no statement-text mismatch or missing-program finding. The stricter package validator also checks the exact full statements, final PDF page references, clean compilation log, and archive hashes.
