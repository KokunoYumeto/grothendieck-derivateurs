"""Build the full POLES paper with LuaLaTeX, BibTeX, and converged references.

Run: python code/build_lualatex.py
For an ordinary complete TeX Live installation: add --system-tex.
The repair path installs dependencies only inside this workspace; see
f_tex_runtime.py and f_tex_dependencies.json for its explicit package list.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess

from f_tex_runtime import tex_environment


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--system-tex", action="store_true", help="use the ordinary TeX installation without workspace repair")
    parser.add_argument("--source", default="POLES_paper.tex")
    parser.add_argument("--output-directory", default=".")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    env = os.environ.copy() if args.system_tex else tex_environment()
    outdir = root / args.output_directory
    outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(args.source).stem
    job = Path(args.output_directory) / stem
    latex = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", f"-output-directory={args.output_directory}", args.source]
    commands = [latex, ["bibtex", str(job)], latex, latex]
    output = root / "code" / "build_lualatex_output.txt"
    with output.open("w") as log:
        for number, command in enumerate(commands, 1):
            heading = f"PASS {number}: {' '.join(command)}\n"
            print(heading, end="", flush=True)
            log.write(heading)
            log.flush()
            run = subprocess.run(command, cwd=root, env=env, text=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            log.write(run.stdout)
            log.flush()
            if run.returncode:
                print(run.stdout[-12000:], flush=True)
                raise SystemExit(run.returncode)
    tex_log = (outdir / f"{stem}.log").read_text(errors="replace")
    warnings = re.findall(r"(?:LaTeX|Package [\w-]+|Class [\w-]+) Warning:[\s\S]*?(?=\n\n)", tex_log)
    missing_chars = [line for line in tex_log.splitlines() if line.startswith("Missing character:")]
    boxes = [line for line in tex_log.splitlines() if re.match(r"(?:Over|Under)full \\[hv]box", line)]
    backend = [line for line in tex_log.splitlines() if "warning" in line.lower() and "pdf backend" in line.lower()]
    summary = {
        "source": args.source,
        "engine": "LuaLaTeX (LuaHBTeX)",
        "passes": len(commands),
        "pdf": str(job.with_suffix(".pdf")),
        "warnings": warnings,
        "missing_characters": missing_chars,
        "box_warnings": boxes,
        "backend_warnings": backend,
    }
    (root / "code" / "build_lualatex_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2), flush=True)
    print(f"Build succeeded; complete transcript: {output}", flush=True)


if __name__ == "__main__":
    main()
