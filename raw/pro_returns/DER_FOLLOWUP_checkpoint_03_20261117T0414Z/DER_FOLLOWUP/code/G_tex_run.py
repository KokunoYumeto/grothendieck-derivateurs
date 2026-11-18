#!/usr/bin/env python3
"""Run a TeX command from the manuscript root with the repaired local runtime.

Example: python code/G_tex_run.py lualatex -halt-on-error DER_FOLLOWUP_paper.tex
"""
from pathlib import Path
import json
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
env = os.environ.copy()
env.update(json.loads((root / "build/tex_runtime/environment.json").read_text()))
command = sys.argv[1:]
if not command:
    raise SystemExit("Supply a TeX command, for example lualatex DER_FOLLOWUP_paper.tex")
raise SystemExit(subprocess.run(command, cwd=root, env=env).returncode)
