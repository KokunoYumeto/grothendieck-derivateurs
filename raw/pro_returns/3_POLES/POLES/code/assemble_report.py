#!/usr/bin/env python3
"""Combine the substantive source/proof/verification reports without omissions."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
parts = [root / "research" / f"{prefix}_report.md" for prefix in ("Root", "AG", "CE", "F")]
chunks = []
for i, path in enumerate(parts):
    text = path.read_text()
    if i:
        text = re.sub(r"^(#+) ", lambda m: "#" * min(6, len(m.group(1)) + 1) + " ", text, flags=re.M)
    chunks.append(text.rstrip())
target = root / "POLES_report.md"
target.write_text("\n\n".join(chunks) + "\n")
print(f"Combined {len(parts)} source reports into {target.name}; {len(target.read_text().split())} whitespace-delimited words.")
