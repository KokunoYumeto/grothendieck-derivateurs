# Programs and reproduction

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

The mathematical status is **INCOMPLETE**. Finite calculations in this directory do not establish totality of an infinite category or survival through every AKR attachment. Consult the paper and the scope statements in each output.

## Requirements

Python 3.12 was used. Most finite category and graph programs use only the standard library. The integer normal-form programs use SymPy. PDF rendering uses Pillow and Poppler (`pdftoppm`, `pdftotext`); the paper uses LuaLaTeX and BibTeX. No internet access is needed for the mathematical calculations or paper build once these dependencies are installed. The `finite_source_fetch*` scripts are separate, optional provenance records of public-source retrieval attempts.

## Build the deliverables

From the package root:

```bash
python3 code/build_bibliography.py
python3 code/build_pdf.py
python3 code/build_register.py
python3 code/render_pdf_qa.py
```

The register reads the actual compiled labels from `TOTEX2_paper.aux`; build the paper first. The report is assembled from `notes/report_body.md`, `notes/literature.md`, and the item table in `build_register.py`. The bibliography builder uses the included supplied metadata under `code/inputs/` plus the two bibliography supplements under `notes/`. The PDF driver supports a normal complete TeX Live installation. Its documented local Type 1 bootstrap is only for the stripped runtime used in this session.

The final build checks for undefined references and citations, duplicate labels, and overfull boxes. Rendering does not itself certify visual quality: the separately recorded review identifies the pages actually inspected. Each page can be regenerated; the archive keeps contact sheets, text extraction, and QA diagnostics rather than all individual intermediate page images.

## Mathematical programs

| Program | Purpose and output |
|---|---|
| `algebra_column_torsion.py` | Exhaustive finite-category axioms and exact order-three torsion certificate for the P1 counterexample; `algebra_column_torsion.out`. |
| `finite_rational_p1.py` | Symbolic associativity of every arrow-family triple, Laurent-polynomial diagonalization and eigenvector certificates, and the universal modulo-prime determinant certificate for the torsion-free integral strengthening. |
| `finite_freefactor_nerve.py` | Free-factor inverses, exact quotient identities and integral Mayer–Vietoris matrix; a separately identified bounded word enumeration supplements the full proof. |
| `cyclic_linear_cuts.py` | Exhaustive four-cut and six-three-simplex certificates for the linear/cyclic-order candidate. |
| `finite_ty_verify.py` | Interval-type variance, composition, and the target-independent separating functional, with finite enumeration; matching `.out`. |
| `akr_nonmonic_comma_circle.py` | Complete finite nonmonic comma-graph counterexample, including identities, composition and associativity; matching `.out`. |
| `finite_ordered_graphs.py` | Exact searches over Q, F2 and F3; exhaustive through six vertices and a separately identified random seven-vertex sample. |
| `finite_ordered_graphs_verify.py` | Independent verification of the printed six- and seven-vertex integral certificates and saved search certificates. |
| `main_coloring_cycles.py` | Exact integer affine-marginal obstruction for proper three-colorings of finite cycles; includes an explicit signed C5 certificate. This is not a category counterexample. |
| `akr_stage_model.py` | Supplied earlier stage model, copied as a self-contained dependency. Uses actual path lengths by default. `--literal-common-n` explicitly denotes the source-rule-violating variant. |
| `akr_point_pair_stage.py` | Integral absolute and relative nerve homology for the P12 binary-edge point attachment, including a nonzero quotient K/F. |
| `akr_v3_mix.py` | Integral homology for the P12 third-coordinate branch, cross P12+P13 branch, and P13 binary-edge point branch; exact invocations and parameters are recorded in the matching outputs and notes. |
| `finite_akr_point_fixed.py` | Exact fixed subsets, graph components, and component-path checks for the specified point and mixed branches. Includes the point/component path-inflation counts. |
| `ordered_beta_orderability.py` | Finite precedence-DAG tests for repaired necklaces of increasing injections; 9,035 monotone pairs through target size eight. The universal eventual-orderability proof is separate. |
| `akr_connected_convex_search.py` | Exhaustive generic connected graph-atlas search within its printed range, explicitly separating tests outside the proved diameter bound. These graph configurations are not presumed to occur in C.1. |
| `akr_connected_convex_counterexample.py` | Complete connected generic counterexample with a 46-edge path, 94-cycle target and s=45 repaired gluing; verifies all maps and the exact shorter path. Not an actual C.1 configuration. |
| `akr_fixed_components.py` | Fixed-point subgraphs for selected repaired stages; options `--k2`, `--critical`. |
| `akr_next_fixed_subsets.py` | Potential subsequent fixed subsets; options `--critical` and `--pair 0,22` identify saved runs. |
| `akr_right_division.py` | Checks a candidate right-division invariant; its failure is retained. |
| `akr_right_division_WV_aborted.py` | Costly variant explicitly terminated; its partial output is not an exhaustive conclusion. |
| `akr_private_incidence.py` | Private-vertex peeling and independent certificate replay; `--critical` produces the retained critical-stage JSON certificate. |
| `akr_protected_cycles.py` | Absolute and relative free-edge collapses for protected filling cycles; `--critical` produces the retained all-incoming-arrow finite check. |
| `akr_small_repaired_search.py` | Thirty-two exploratory repaired B.9 attachments at s=13, outside C.1's expansion parameter bounds. |
| `finite_akr_intersections.py` | Exact image intersections at `--stage selected_k2` or `--stage critical_k3`; optional `--closure`. |
| `finite_akr_convex.py` | Exhaustive graph-distance checks in the specified finite stage, using the same stage names. |
| `finite_akr_graph_gluing.py` | Complete two-edge/thirteen-copy generic repaired-gluing counterexample. It is not asserted to occur in C.1. |

The corresponding `.out` files are retained next to the programs. The full private-incidence certificate is JSON. No saved failed or terminated exploration is silently counted as a success. Some large finite runs are expensive; reproducing the local theorem certificates does not require rerunning every exploratory search.

The ordered-graph search invocations were:

```bash
python3 code/finite_ordered_graphs.py --max-n 6
python3 code/finite_ordered_graphs.py --max-n 0 --random-n 7 --samples 20000 --output finite_ordered_graphs_random7.json
python3 code/finite_ordered_graphs_verify.py
```

The sample seed is fixed in the source and recorded in the report. Search JSON includes the scope and exact certificates; output names are relative to the code directory as implemented.

## Provenance and packaging

`finite_source_fetch.py`, `finite_source_fetch_additional.py`, `finite_source_fetch_followup.py`, and `finite_source_fetch_topos.py` retain attempted primary URLs and actual response statuses. The source bodies are not silently assumed when a fetch failed. User-provided AKR scan pages used in the proof audit are retained in `akr_source_images/`; externally fetched source PDFs are excluded from the archive. Full source access and theorem-level use are recorded in `notes/literature.md`.

`package_checkpoint.py` writes a new, non-overwriting ZIP and a SHA-256 manifest. It excludes the local TeX bootstrap, Python caches, external research-source downloads and individual intermediate PDF page images. Earlier checkpoint archives are immutable. A final package can preserve an earlier checkpoint verbatim under `checkpoints/`, ensuring the earlier file versions and passages remain available.
