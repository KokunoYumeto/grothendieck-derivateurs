# Reproducing the TOTEX return

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

The mathematical proofs are in the standalone `../TOTEX_paper.tex` and PDF. The scripts verify finite constructions and the consistency of the delivered record. A finite sample is not used to infer totality for all set-valued functors.

## Requirements

The recorded Python environment was Python 3.12.14 with SymPy 1.14.0 and Pillow 13.0.0. AKR computations, basic shape checks, support-orbit counts, and the independent PRETOT certificate reader use only the standard library. The affine interpolation, PRETOT generator, and sign-resolution checks also use SymPy. PDF compilation requires LuaLaTeX; rendering and the final package check use Poppler (`pdftoppm`, `pdftotext`, and `pdfinfo`). Rendering additionally uses Pillow. The results-ledger authoring uses Node.js and `@oai/artifact-tool`; its exact inputs and roundtrip checks are described in `totex_results_REPRODUCE.md`.

## Mathematical computations

Run the following from this `code/` directory. The AKR commands and parameter conventions, including the distinction between repaired C.1 and general B.9, are in `akr_REPRODUCE.md`.

```sh
python3 basic_shape_checks.py
python3 examples_colored_words.py
python3 examples_support_orbits.py
python3 examples_affine_base.py
python3 main_sign_reflection_check.py > outputs/main_sign_reflection_check.json
python3 pretot_audit/main_counterexample.py > pretot_audit/outputs/main_counterexample.out
python3 pretot_audit/audit_certificate.py > pretot_audit/outputs/independent_certificate_audit.out
python3 pretot_audit/semisimplicial_affine_checks.py
```

The first four programs write their named JSON or text output automatically. The PRETOT generator also writes its finite JSON data and integral projectivity certificate under `pretot_audit/outputs/`. The independent reader checks those supplied certificate files without trusting the generator. The affine base program is an identical copy of the audited semisimplicial program, placed beside the colored-word program so that its import remains portable; their recorded output is identical.

`source_fetch.py` records the two direct source-access attempts in `source_fetch.out`. Running it again requires network access and may produce different access results. It is not needed to reproduce any mathematical computation. Source PDFs are not included in this return.

## Paper, ledger, layout, and archive

From the package root:

```sh
python3 code/build_pdf.py
```

Then regenerate the ledger as described in `code/totex_results_REPRODUCE.md`, so that its numbers and pages match the current auxiliary file. The delivered label cache permits the original ledger to be reproduced without first rebuilding the PDF. Next run:

```sh
python3 code/render_pdf_qa.py
python3 code/verify_package.py --zip
```

The rendering script checks page count and text bounds and writes temporary page PNGs and contact sheets under `.build/pdf_qa/`. It does not perform a human visual review; the report records the assistant's review of the delivered PDF. The final verifier checks the 58-statement bijection, exact CSV columns and statuses, label and citation resolution, bibliography access markers, recorded integral ranks, and final source/PDF hashes. Its `--zip` option builds `TOTEX_return.zip` and verifies every archived byte against its source. This is a consistency check, not an independent proof checker.

The ZIP contains the five requested main files and this `code/` tree. Temporary TeX formats, authoring section files, rendered page images, and downloaded source papers are excluded. Every program's mathematical or audit output is retained alongside it or under `outputs/`.
