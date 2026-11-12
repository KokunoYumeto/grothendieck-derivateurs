# Reproducing the results ledger

The single CSV has exactly the seven columns requested in the prompt and one row for every numbered theorem, proposition, lemma, corollary, definition, example, obstruction, audit, or remark. The authoring input is `totex_results_metadata.json`. It contains the mathematical summaries, normalized statuses, dependency labels, manuscript-page annotations, and mappings to every requested item. The executable builder obtains the numerical identifiers and PDF start pages from `TOTEX_paper.aux`; the supplied `totex_labels_cache.json` preserves exactly those labels when the auxiliary file is absent.

## Running the builder

Use Node.js with `@oai/artifact-tool` available. In the provided runtime, create a task-specific directory under the operating system's temporary directory and put a `node_modules` symlink there pointing to `CODEX_PRIMARY_RUNTIME_NODE_MODULES`. Copy `build_totex_results.mjs` into that temporary directory, then run:

```sh
"$CODEX_PRIMARY_RUNTIME_NODE" build_totex_results.mjs /absolute/path/to/the/deliverables
```

The path argument must identify the directory containing `TOTEX_paper.tex` and `code/`. The final standalone TeX is sufficient; the builder also accepts the earlier authoring layout with `sections/A.tex` through `sections/F.tex`. It never edits the paper. If a current auxiliary file exists, it takes precedence and refreshes the label cache. Rebuild the PDF before regenerating the ledger after changes that might alter statement numbers or pages. If no auxiliary file exists, the supplied cached labels allow reproduction before a PDF rebuild.

## Authoring and validation

The builder authors the complete table in an artifact-tool worksheet as text, recalculates it, and checks an exact readback against the input matrix. The documented API exposes CSV import but no CSV export. The builder therefore serializes the worksheet's read-back values as UTF-8 RFC 4180 CSV with CRLF record endings. It checks both a separate CSV parser roundtrip and reimport through `Workbook.fromCSV`. No XLSX file is created.

The validator requires an exact bijection between numbered TeX statements, metadata entries, auxiliary labels, and CSV rows. It checks consecutive numbering, allowed statuses and their agreement with the TeX headings, resolved internal dependencies, descriptive statements, explicit repair notes where applicable, no spreadsheet formulas, and coverage of A, R1–R10, B.1–B.3, C.1–C.2, D.1–D.6, E, and F. It also scans the supplied TeX for unexpected control characters, Unicode replacement characters, and bidirectional formatting controls; this detects accidental programming-language escapes such as a tab substituted for the start of a TeX arrow command. The validated source uses spaces, rather than literal tabs, for indentation. The CSV roundtrips preserve Unicode exactly. A coverage tag does not convert an open item into a proved one.

`where_proved` gives the current paper location. `manuscript_pages_settled` instead refers to the relevant pages of Grothendieck's manuscript. Its blank cells mean that the row does not settle a specific manuscript-page assertion; they are intentional and are preserved as empty fields. Labels in notes and dependencies remain stable if the numerical identifiers change.

## Outputs

- `../TOTEX_results.csv`: the requested final table.
- `outputs/build_totex_results.out`: the recorded execution summary.
- `outputs/totex_results_audit.json`: schema, statement, status, source-hash, roundtrip, coverage, and limitation checks.
- `outputs/totex_results_source_records.json`: extracted statement/proof text, source locations, cross-reference and citation mentions, and curated dependency annotations.
- `outputs/totex_results_values.json`: exact authored cell values for independent checks.
- `outputs/totex_results_inspect.ndjson`: bounded worksheet inspection.
- `outputs/totex_results_preview.png`: a visual audit of the first four rows and first three columns, not an additional spreadsheet deliverable.

The ledger preserves the unresolved integral/rational/mod-p implications, the missing full K2 rank and later persistence proof, the restricted minimality of the terminal-object repair, and the three inaccessible source bodies. It distinguishes the repaired C.1 model's persistence results from the separate general B.9 model's verified rank-one class death: the latter's full specified K2 and infinite completion are still undecided. Its source-comparison rows distinguish an opened paper body from a publisher record or abstract.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.
