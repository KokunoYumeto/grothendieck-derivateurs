GALOIS: locally constant coefficients, localizers, and relative Galois reconstruction
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026.
No priority is claimed.

CONTENTS

GALOIS_paper.pdf is the 66-page rendered research paper, in the requested A--G order.
GALOIS_paper.tex and sections/*.tex contain its complete editable source.
GALOIS_results.csv has one row for each of the 74 numbered assertions and the
seven requested fields. The statement field preserves the full mathematical
statement in LaTeX notation, including its hypotheses. Page references refer to
the enclosed PDF. Status totals: 52 Proved, 10 Known, 7 Refuted, 5 Open.
GALOIS_references.bib has 27 entries, each marked verified or unverified.
GALOIS_report.md records sources read, computations, corrections, and exact gaps.
research/D_audit.csv covers every one of the 21 requested manuscript audit rows.
code/ contains the verification and build programs, with their complete outputs.
research/ also contains the section reports and machine-readable source registers.
GALOIS_paper.log is the clean final LuaLaTeX log; GALOIS_paper.bbl is its APA
author-year bibliography. RELEASE_MANIFEST.sha256 checks every other archive file.

BUILD

On a standard TeX Live installation with LuaLaTeX, BibTeX, fontspec, Latin Modern,
apacite, amsmath, mathtools, tikz-cd, microtype, hyperref, and the standard LaTeX
packages, run from this folder:

    python3 code/build_paper.py

Equivalently, run LuaLaTeX, BibTeX, and LuaLaTeX twice on GALOIS_paper.
The supplied build output records four successful passes. The final log contains
no errors, warnings, unresolved citations, overfull boxes, or underfull boxes.
code/prepare_tex_runtime.py is an optional helper for the restricted execution
image used here. It downloads the four recorded upstream TeX support packages
into a sibling tmp folder and creates only local TeX configuration/cache files.
It is unnecessary on an ordinary complete TeX installation. Its package URLs
and SHA-256 checksums are recorded in research/upstream_tex_packages.json.

VERIFICATION

The finite category, presentation, and homology checks are independent Python
programs. Most use only the standard library; exact Smith normal forms in
ef_checks.py require SymPy. PDF review uses PyMuPDF, Pillow, and Poppler.

    python3 code/A5_finite_counterexample.py
    python3 code/B_verify_reverse_excision.py
    python3 code/D_verify_finite.py
    python3 code/D_verify_more.py
    python3 code/D_verify_remaining.py
    python3 code/ef_checks.py
    python3 code/verify_coefficient_examples.py

The corresponding .out files contain the successful exhaustive checks.
The mathematics is proved in the paper; these programs verify the finite
counterexample data and the numerical invariants used in those proofs.

To rerun code/run_verifications.py in full, first extract the supplied original
4_GALOIS_background.zip as a sibling folder named background, beside GALOIS.
Two source checks intentionally need that original input: D_build_audit.py reads
the original DER_I-b claim CSV, and verify_toen_numbering.py reads the supplied
Toen source. The archive does not duplicate the attached copyrighted background
books, papers, or large research text extractions. All source-independent finite
programs above can be run without the background folder.

The five numbered Open assertions are B.13, B.14, E.11, F.8, and G.6. Open means
unresolved by this work, not asserted to be open throughout the literature.
The ordinary rational derivator tower is constructed; its interpretation by
successively higher linear coefficient categories remains a separate gap.
