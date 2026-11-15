# INDLOCAL

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 14 November 2026.
No priority is claimed.

**This return is incomplete.** The exact cardinal frontier in dimension two
is unresolved. The smallest remaining instance is an acyclic map
`BG -> S²` with an actual two-dimensional classifying space and no
nontrivial homomorphism from `G` to a countable group; an uncountable `G`
is allowed. The report gives the exact proved cases and the remaining step.

## Main deliverables

- `INDLOCAL_paper.pdf`: the reviewed 101-page manuscript.
- `INDLOCAL_paper.tex` and `sections/`: the complete LuaLaTeX source.
- `INDLOCAL_results.csv`: 95 stable statement records, with proof locations,
  dependencies, manuscript pages and unresolved status.
- `INDLOCAL_references.bib`: references marked verified or unverified,
  with the scope of the source examination stated in each entry.
- `INDLOCAL_report.md`: requested-item register, findings, failed approaches,
  the smallest unresolved instance, checkpoint records and typesetting QA.
- `research/`: authored calculations, source audits and work notes.
- `code/` and `logs/`: reproducible computations and their retained records.

The current paper and results register state the conclusions of this return.
Earlier wording is preserved for audit in `history/`, when present. The
history manifest identifies every retained checkpoint member by its original
path and SHA-256 hash. It explicitly lists the two omitted downloaded source
reproductions from checkpoint 06. Every authored proof, note, script, log and
review image from all checkpoints is retained byte for byte.

## Reproduce the document and computations

From this directory, regenerate the statement register and bibliography with:

```sh
python3 code/assemble_results.py
```

Build the paper with LuaLaTeX and BibTeX:

```sh
python3 code/build_pdf.py
```

A standard complete TeX Live installation is sufficient. The script includes
a documented local Type 1 bootstrap for the supplied minimal runtime. It
writes only inside this package and does not change a system installation.
The build exits unsuccessfully on unresolved references or overfull boxes.

Each mathematical verification program in `code/` documents its own finite
model. Its saved `.json` or `.out` result is retained beside it. The principal
checks cover the strict two-groupoid counterexample, type maps and padding,
the crown and suspension examples, and the finite cofibration constructions.

Visual QA is separate from compilation. `logs/PDF_QA_PASSED.json` records the
reviewed PDF hash and all 21 inspected page numbers; the contact sheets are
in `logs/rendered/`. Rebuilding changes the PDF hash and does not by itself
constitute a fresh visual review.

## Verify or restore checkpoint history

The final package includes a content-addressed history, with no duplicate
copies of identical member bytes. To verify it:

```sh
python3 code/preserve_checkpoint_history.py --verify
```

To restore the retained contents of checkpoint 03 into a new directory:

```sh
python3 code/preserve_checkpoint_history.py --restore 3 --destination /tmp/INDLOCAL_checkpoint_03_restored
```

The destination must not already exist. This reproduces retained member
contents and paths, without modifying the immutable checkpoint archives.

The attached source collections are reference inputs and are excluded from
this deliverable. The authored source-access and proof-audit records retain
their exact locators and the limits of what was checked.
