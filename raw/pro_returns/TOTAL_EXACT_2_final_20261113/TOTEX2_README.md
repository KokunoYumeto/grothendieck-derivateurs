# TOTEX2 — completed proof and audit package

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 13 November 2026. No priority is claimed.

Every requested Part and every lettered Lead is proved or refuted. The current paper and outcome table supersede the incomplete status summaries inside the immutable earlier checkpoints.

## Read first

- **TOTEX2_paper.pdf** — the complete paper, with numbered Proved / Refuted / Known statements and full proofs.
- **TOTEX2_report.md** — the 25-row outcome table first, followed by the proof-route record, corrections, computations and source-access audit.
- **TOTEX2_results.csv** — one row for every numbered statement, with its compiled number, status, proof location, dependencies and scope.
- **TOTEX2_references.bib** — each entry explicitly marks whether its body was opened.
- **TOTEX2_paper.tex** and **sections/** — the complete LuaLaTeX source.
- **code/** — mathematical programs, outputs, exact certificates, build scripts and visual-review records. See code/README.md for reproduction.
- **notes/** — proof-development records and independent mathematical audits. Historical stopping points are identified as superseded where they concern the final conclusions.
- **checkpoints/** — immutable earlier checkpoint archives, preserved verbatim.
- **MANIFEST.sha256.tsv** — byte lengths and SHA-256 hashes for the packaged files.

## Main conclusions

The ordered predimension category C_delta in Theorem A.1 is total for every covariant set action, but its three point arrows into one hyperedge have no affine equalizer over any nonzero unital ring. The column cokernel has projective dimension exactly one and first derived colimit R. Thus A.1, both coefficient versions of A.2, and B.1 are refuted by the same explicit category and triple.

The full all-action proof is in A.21–A.34, especially the finite alternating bridge A.30, the stabilizer results A.31–A.32, and the two homotopy-final comparisons A.33. Theorem A.34 combines them. The private-incidence obstruction is A.24.

Universal repaired AKR survival is proved in C.19–C.28. Every admissible repaired C.1 construction is non-total: every attachment preserves the old binary cycle colimit, and the first-stage class kappa_+−kappa_- survives the infinite union. The source/component induction gives the sharp path bound L_H≤L_U+1 and does not add the older selected construction's diameter or ordering requirements.

Consequently D.1 gives three strict inclusions:

filtered ⊊ exact ⊊ total ⊊ quasi-filtered.

The algebraic Leads are treated in B.2–B.10. The finite-test, link, interval-type and minimal-separator Leads are treated in C.2–C.6 and C.38–C.41. The report distinguishes formal assertions proved from explanatory glosses or literal overstatements refuted.

## Reproduce the document

From this directory, with Python, the listed Python dependencies, LuaLaTeX, BibTeX and Poppler installed:

```bash
python3 code/build_bibliography.py
python3 code/build_pdf.py
python3 code/build_register.py
python3 code/render_pdf_qa.py
```

The source-access audit distinguishes opened bodies from failed retrievals. Externally fetched research-source PDFs are not redistributed; exact URLs and inspected locations are recorded. No theorem is attributed to an unopened body. Independent mathematical reviews and finite computation certificates have different scopes, which are stated explicitly.
