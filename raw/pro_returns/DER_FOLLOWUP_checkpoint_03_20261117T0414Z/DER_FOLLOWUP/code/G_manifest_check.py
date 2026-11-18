#!/usr/bin/env python3
"""Check Part G claim, register, label, proof, and citation coverage.

This records the integration check first run inline on 17 November 2026.
It checks artifact structure, not the mathematical proofs.
"""
import csv
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((root / "notes/G_results.csv").open()))
tex = (root / "sections/G.tex").read_text()
ids = re.findall(r"\\begin\{claim\}\{(G\.\d+)\}", tex)
assert ids == [row["id"] for row in rows]
assert len(re.findall(r"\\begin\{proof\}", tex)) == len(ids)
assert len(re.findall(r"\\end\{proof\}", tex)) == len(ids)
assert len(re.findall(r"\\label\{G:", tex)) == len(ids)
bib = (root / "notes/G_references.bib").read_text()
keys = set(re.findall(r"@\w+\{([^,]+),", bib))
used = set()
for match in re.finditer(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", tex):
    used.update(match.group(1).split(","))
assert used <= keys
result = {
    "claims": len(ids),
    "csv_rows": len(rows),
    "proofs": len(ids),
    "bibliography_entries": len(keys),
    "all_citation_keys_resolved": True,
    "all_assertions": "passed",
    "scope": "artifact structure, not mathematical verification",
}
out = root / "code/outputs/G_manifest_check.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
