#!/usr/bin/env python3
"""Build an intermediate full-paper driver and retain every diagnostic.

The driver uses the current manuscript verbatim except for a temporary merged
bibliography.  Missing sections are handled by the manuscript's IfFileExists.
This script does not modify the mathematical sources or the master driver.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import re
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
dest = root / "build/paper_check"
dest.mkdir(parents=True, exist_ok=True)
old_logs = list(dest.glob("run_*.txt")) + list(dest.glob("*.log")) + list(dest.glob("*.blg"))
if old_logs:
    history = dest / "history" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    history.mkdir(parents=True, exist_ok=True)
    for path in old_logs:
        shutil.copy2(path, history / path.name)
env = os.environ.copy()
env.update(json.loads((root / "build/tex_runtime/environment.json").read_text()))

bibpaths = [root / "DER_FOLLOWUP_references.bib"]
bibpaths += sorted((root / "notes").glob("*.bib"))
entries = {}
for path in bibpaths:
    source = path.read_text()
    starts = list(re.finditer(r"(?m)^@[A-Za-z]+\s*[({]\s*([^,\s]+)", source))
    for i, match in enumerate(starts):
        key = match.group(1)
        stop = starts[i + 1].start() if i + 1 < len(starts) else len(source)
        entries.setdefault(key, source[match.start():stop].rstrip())
(dest / "allrefs.bib").write_text("\n\n".join(entries.values()) + "\n")
source = (root / "DER_FOLLOWUP_paper.tex").read_text()
source = source.replace(r"\bibliography{DER_FOLLOWUP_references}",
                        r"\bibliography{build/paper_check/allrefs}")
(dest / "paper_check.tex").write_text(source)
commands = [
    ["lualatex", "-file-line-error", "-interaction=nonstopmode", "-halt-on-error",
     "-output-directory=build/paper_check", "build/paper_check/paper_check.tex"],
    ["bibtex", "build/paper_check/paper_check"],
    ["lualatex", "-file-line-error", "-interaction=nonstopmode", "-halt-on-error",
     "-output-directory=build/paper_check", "build/paper_check/paper_check.tex"],
    ["lualatex", "-file-line-error", "-interaction=nonstopmode", "-halt-on-error",
     "-output-directory=build/paper_check", "build/paper_check/paper_check.tex"],
]
results = []
for i, command in enumerate(commands, 1):
    run = subprocess.run(command, cwd=root, env=env, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (dest / f"run_{i}.txt").write_text(run.stdout)
    results.append({"command": command, "exit_code": run.returncode})
    if run.returncode and command[0] != "bibtex":
        print(run.stdout[-10000:])
        break

logfile = dest / "paper_check.log"
log = logfile.read_text(errors="replace") if logfile.exists() else ""
overflows = []
for match in re.finditer(r"Overfull \\hbox \((\d+(?:\.\d+)?)pt too wide\)", log):
    next_lines = "\n".join(log[match.start():].splitlines()[:8])
    sections = re.findall(r"\(\./(sections/[^\s()]+\.tex)", log[:match.start()])
    overflows.append({"overflow_pt": float(match.group(1)),
                      "last_opened_section": sections[-1] if sections else None,
                      "context": next_lines})
result = {
    "driver": "build/paper_check/paper_check.tex",
    "pdf": "build/paper_check/paper_check.pdf",
    "sections_present": [x.name for x in sorted((root / "sections").glob("*.tex"))],
    "bibliography_entries": len(entries),
    "commands": results,
    "overfull_hboxes": overflows,
    "over_2pt": sum(x["overflow_pt"] > 2 for x in overflows),
    "scope": "Intermediate integration check; final delivery build remains the parent's responsibility.",
}
(root / "code/outputs/G_paper_build_check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
if results and results[-1]["exit_code"]:
    raise SystemExit(results[-1]["exit_code"])
