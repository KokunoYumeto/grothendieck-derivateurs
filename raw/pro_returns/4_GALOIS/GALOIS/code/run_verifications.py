"""Run the finite verifiers and metadata checks, preserving complete output."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
programs = [
    "A5_finite_counterexample.py", "B_verify_reverse_excision.py",
    "D_verify_finite.py", "D_verify_more.py", "D_verify_remaining.py",
    "ef_checks.py", "verify_coefficient_examples.py",
    "verify_toen_numbering.py", "D_build_audit.py", "make_C_register.py",
    "ef_register.py", "assemble_bibliography.py", "finalize_register.py",
]
for name in programs:
    p = subprocess.run([sys.executable, str(ROOT/"code"/name)],
                       cwd=ROOT.parent, capture_output=True, text=True)
    (ROOT/"code"/Path(name).with_suffix(".out")).write_text(p.stdout+p.stderr)
    print(f"{name}: {'PASS' if p.returncode == 0 else 'FAIL'}", flush=True)
    if p.returncode:
        print(p.stdout+p.stderr)
        raise SystemExit(p.returncode)
print(f"PASS: all {len(programs)} finite verification, source-numbering, and register programs completed.")
