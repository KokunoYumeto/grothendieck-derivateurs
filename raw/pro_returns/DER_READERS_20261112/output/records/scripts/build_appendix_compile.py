#!/usr/bin/env python3
"""Compile the integrated companion and write path-sanitized build records.

Requires a working LuaLaTeX distribution and BibTeX. Run from the package root:
  python records/scripts/build_appendix_compile.py --companion companion --records records

The source-construction step is in build_appendix.py. This command performs four
LuaLaTeX passes with BibTeX after the first pass, preserving the final bibliography.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

def sanitize(text: str, roots: list[Path]) -> str:
    for root in sorted(roots, key=lambda p: len(str(p)), reverse=True):
        text = text.replace(str(root), "[build-root]")
    # TeX may wrap a path at its maximum print-line length. Collapse the known
    # continuation before suppressing remaining absolute filesystem references.
    text = re.sub(r"(?<=/)([^\s()]*)\n([^\s()]+)", r"\1\2", text)
    text = re.sub(r"(?<![A-Za-z0-9:/])/(?:[A-Za-z0-9_.+-]+/)+[^\s()<>\[\]{}]*", "[system-file]", text)
    text = re.sub(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[e-mail address removed]", text)
    return text

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--companion", type=Path, required=True)
    ap.add_argument("--records", type=Path, required=True)
    ap.add_argument("--engine", default="lualatex")
    ap.add_argument("--format", help="Format name for a LuaTeX binary, when needed")
    args = ap.parse_args()
    directory = args.companion.resolve()
    records = args.records.resolve()
    records.mkdir(parents=True, exist_ok=True)
    engine = shutil.which(args.engine)
    if not engine:
        raise SystemExit("LuaLaTeX executable unavailable; install a working TeX distribution.")
    job = "LesDerivateurs_companion"
    command = [engine]
    if args.format:
        command.append("--fmt=" + args.format)
    command += ["-interaction=nonstopmode", "-file-line-error", "-halt-on-error", job + ".tex"]
    roots = [Path.cwd().resolve(), directory, records]
    roots += [Path(x) for x in os.environ.get("TEXMFCACHE", "").split(os.pathsep) if x]
    runs = []
    for pass_number in range(1, 5):
        run = subprocess.run(command, cwd=directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        runs.append({"program": "LuaLaTeX", "pass": pass_number, "exit_code": run.returncode})
        (records / f"APPENDIX_pass{pass_number}.log").write_text(sanitize(run.stdout, roots))
        if run.returncode:
            raise SystemExit(f"LuaLaTeX pass {pass_number} failed; see its sanitized log.")
        if pass_number == 1:
            bibtex = shutil.which("bibtex")
            if not bibtex:
                raise SystemExit("BibTeX unavailable; install it to rebuild the bibliography.")
            bib = subprocess.run([bibtex, job], cwd=directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            runs.append({"program": "BibTeX", "exit_code": bib.returncode})
            (records / "APPENDIX_bibtex.log").write_text(sanitize(bib.stdout, roots))
            if bib.returncode:
                raise SystemExit("BibTeX failed; see its sanitized log.")
    log = (directory / (job + ".log")).read_text(errors="replace")
    (records / "APPENDIX_compile.log").write_text(sanitize(log, roots))
    pdf = directory / (job + ".pdf")
    output = re.search(r"Output written on .*?\((\d+) pages, (\d+) bytes\)", log, re.S)
    stats = {
        "runs": runs,
        "pages": int(output[1]) if output else None,
        "pdf_bytes": pdf.stat().st_size,
        "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
        "latex_error_lines": len(re.findall(r"^!", log, re.M)),
        "package_or_latex_warnings": len(re.findall(r"(?:LaTeX|Package \S+) Warning:", log)),
        "missing_glyph_warnings": len(re.findall(r"Missing character:", log)),
        "overfull_boxes": len(re.findall(r"Overfull ", log)),
        "underfull_boxes": len(re.findall(r"Underfull ", log)),
    }
    (records / "APPENDIX_REBUILD_STATUS.json").write_text(json.dumps(stats, indent=2) + "\n")
    # Keep only the sanitized records in the deliverable tree.
    for suffix in (".aux", ".log", ".out", ".toc", ".blg"):
        path = directory / (job + suffix)
        if path.exists():
            path.unlink()
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
