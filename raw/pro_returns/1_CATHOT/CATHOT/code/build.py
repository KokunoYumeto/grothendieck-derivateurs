"""Build the complete paper with LuaLaTeX and BibTeX; retain exact logs."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
commands = [
    ['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'CATHOT_paper.tex'],
    ['bibtex', 'CATHOT_paper'],
    ['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'CATHOT_paper.tex'],
    ['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'CATHOT_paper.tex'],
]
for index, command in enumerate(commands, 1):
    print(f'PASS {index}: ' + ' '.join(command), flush=True)
    proc = subprocess.run(command, cwd=ROOT, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = ROOT / 'code' / f'build_pass_{index}.out'
    out.write_text(proc.stdout)
    print(f'  exit={proc.returncode}, log={out.name}, lines={len(proc.stdout.splitlines())}', flush=True)
    if proc.returncode:
        print(proc.stdout[-12000:], flush=True)
        raise SystemExit(proc.returncode)
print('Build finished successfully.', flush=True)
