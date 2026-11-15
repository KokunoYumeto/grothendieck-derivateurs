"""Compile the paper with LuaLaTeX and BibTeX, stopping on an actual error.

On a standard TeX installation run this script directly. In this restricted
workspace prepare_tex_runtime.py supplied the private environment first.
Only diagnostic output is recorded; environment variables are not printed.
"""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
private = ROOT.parent / "tmp" / "tex_runtime" / "environment.json"
env = os.environ.copy()
if private.exists():
    env.update(json.loads(private.read_text()))
commands = [
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "GALOIS_paper.tex"],
    ["bibtex", "GALOIS_paper"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "GALOIS_paper.tex"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "GALOIS_paper.tex"],
]
for i, cmd in enumerate(commands, 1):
    p = subprocess.run(cmd, cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log = ROOT / "code" / f"build_pass_{i}.out"
    log.write_text(p.stdout)
    print(f"Pass {i}: {' '.join(cmd)}; exit {p.returncode}; log {log.name}", flush=True)
    if p.returncode:
        print(p.stdout[-16000:])
        raise SystemExit(p.returncode)
print(f"PASS: generated {ROOT.name}/GALOIS_paper.pdf ({(ROOT/'GALOIS_paper.pdf').stat().st_size:,} bytes).")
