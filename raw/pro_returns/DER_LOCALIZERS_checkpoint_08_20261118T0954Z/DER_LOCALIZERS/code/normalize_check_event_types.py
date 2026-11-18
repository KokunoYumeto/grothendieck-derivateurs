"""Normalize event labels to the controlling brief's exact vocabulary.

This changes labels only; it preserves the actor and outcome and never upgrades
an ordinary review to an independent re-proof.
"""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
mapping = {
    "independent proof check": "targeted proof check",
    "primary-source check": "used and rechecked in this run",
    "proof": "targeted proof check",
    "independent proof review": "targeted proof check",
    "source-access check": "targeted proof check",
    "accessibility": "targeted proof check",
    "program": "computation or formal certificate",
    "source-audit": "used and rechecked in this run",
    "correction": "targeted proof check",
    "program-correction": "computation or formal certificate",
    "executable exact arithmetic": "computation or formal certificate",
    "model recognition and comparison audit": "targeted proof check",
    "hypothesis refinement": "targeted proof check",
    "full proof and primary-source audit": "targeted proof check",
}
allowed = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found",
    "refuted, with the refined statement's id",
}
count = 0
for path in sorted((root / "notes").glob("*_checks.tsv")):
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields, rows = reader.fieldnames, list(reader)
    changed = False
    for row in rows:
        old = row["type"]
        new = mapping.get(old, old)
        if new not in allowed:
            raise ValueError((path.name, row["statement_id"], old))
        if new != old:
            row["type"] = new
            print(path.name, row["statement_id"], repr(old), "->", repr(new))
            count += 1
            changed = True
    if changed:
        with path.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
print("Normalized", count, "event labels; actor, date, outcome, and statement unchanged.")
