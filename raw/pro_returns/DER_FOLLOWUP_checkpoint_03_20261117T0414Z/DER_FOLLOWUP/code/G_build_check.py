#!/usr/bin/env python3
"""Build the G section with the shared preamble and record overflow diagnostics.

This is an intermediate layout check; the parent still verifies the final PDF.
All subprocess output is kept under build/G_check.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import re
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
dest = root / "build/G_check"
dest.mkdir(parents=True, exist_ok=True)
old_logs = list(dest.glob("run_*.txt")) + list(dest.glob("*.log")) + list(dest.glob("*.blg"))
if old_logs:
    history = dest / "history" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    history.mkdir(parents=True, exist_ok=True)
    for path in old_logs:
        shutil.copy2(path, history / path.name)
env = os.environ.copy()
env_file = root / "build/tex_runtime/environment.json"
if env_file.exists():
    env.update(json.loads(env_file.read_text()))
preamble = (root / "DER_FOLLOWUP_paper.tex").read_text().split(r"\begin{document}")[0]
# The installed LuaTeX tree lacks luaotfload.  This retains the same Latin
# Modern family while using its installed Type 1 fonts and TFM metrics.
if not (root / "build/tex_runtime/texmf/tex/luatex/luaotfload/luaotfload-main.lua").exists():
    preamble = preamble.replace(r"\usepackage{fontspec}", r"\usepackage[T1]{fontenc}" + "\n" + r"\usepackage{lmodern}")
    preamble = preamble.replace(r"\setmainfont{Latin Modern Roman}", "")
driver = preamble + r"""
\begin{document}
\input{sections/G.tex}
\bibliographystyle{plainnat}
\bibliography{notes/G_references}
\end{document}
"""
(dest / "G_check.tex").write_text(driver)
commands = [
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build/G_check", "build/G_check/G_check.tex"],
    ["bibtex", "build/G_check/G_check"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build/G_check", "build/G_check/G_check.tex"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory=build/G_check", "build/G_check/G_check.tex"],
]
for num, command in enumerate(commands, 1):
    run = subprocess.run(command, cwd=root, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (dest / f"run_{num}.txt").write_text(run.stdout)
    if run.returncode:
        print(run.stdout[-6000:])
        raise SystemExit(run.returncode)
log = (dest / "G_check.log").read_text()
widths = [float(x) for x in re.findall(r"Overfull \\hbox \((\d+(?:\.\d+)?)pt too wide\)", log)]
result = {
    "driver": "build/G_check/G_check.tex",
    "pdf": "build/G_check/G_check.pdf",
    "overfull_hboxes": len(widths),
    "over_2pt": sum(x > 2 for x in widths),
    "maximum_overflow_pt": max(widths, default=0),
    "scope": "intermediate Part G layout; final integrated PDF still needs verification",
}
(root / "code/outputs/G_build_check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
