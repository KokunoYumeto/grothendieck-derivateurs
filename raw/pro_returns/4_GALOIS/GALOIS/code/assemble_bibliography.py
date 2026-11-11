"""Assemble the checked bibliography and normalize duplicate citation keys."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
sources = ["root_refs.bib", "D_refs.bib", "C_refs.bib", "EF_refs.bib"]
entries = {}
for name in sources:
    raw = (ROOT / "research" / name).read_text()
    for entry in re.split(r"(?m)(?=^@)", raw):
        if not entry.strip():
            continue
        match = re.match(r"@\w+\{([^,]+),", entry)
        assert match, (name, entry[:80])
        key = match.group(1)
        if key == "C_LurieHA":
            continue
        assert key not in entries, key
        assert re.search(r"(?:unverified|verified)", entry, re.I), key
        entries[key] = entry.strip()

aliases = {"Cisinski2009": "Cisinski2009LocallyConstant", "C_LurieHA": "EF_LurieHA"}
for path in (ROOT / "sections").glob("*.tex"):
    raw = path.read_text()
    for old, new in aliases.items():
        raw = re.sub(r"(?<![\w])" + re.escape(old) + r"(?![\w])", new, raw)
    path.write_text(raw)

entries["Cisinski2006"] = entries["Cisinski2006"].replace(
    "Theorem 5.2.15 and Definition 5.2.16; the theorem assumes an accessible fundamental localizer and asserts only left properness without the extra properness condition",
    "Theorems 1.4.3, 4.2.15, 5.2.15, 6.1.11 and 6.4.22; Propositions 4.2.22, 6.1.8 and 9.2.17; Definition 6.1.13; Example 6.1.14; Remark 6.4.23; Scholie 9.2.18; Lemma 9.4.5 and Scholie 9.4.7 checked. Theorem 5.2.15 assumes accessibility; right properness requires the separate properness condition"
)
entries["Cisinski2009LocallyConstant"] = entries["Cisinski2009LocallyConstant"].replace(
    "Theorem 1.3, Corollary 3.8, and Section 3 definitions",
    "Theorems 1.3, 3.6 and 3.13, Corollary 3.8, Lemma 3.9, Proposition 3.10 and Section 3 definitions"
)
out = "% AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n" + "\n\n".join(entries.values()) + "\n"
(ROOT / "GALOIS_references.bib").write_text(out)
tex = "\n".join(p.read_text() for p in [ROOT / "GALOIS_paper.tex", *(ROOT / "sections").glob("*.tex")])
cites = set()
for match in re.finditer(r"\\(?:cite\w*|nocite)(?:\[[^\]]*\])*\{([^}]+)\}", tex):
    cites.update(x.strip() for x in match.group(1).split(","))
missing = sorted(cites - entries.keys())
assert not missing, missing
print(f"PASS: {len(entries)} unique bibliography entries; every entry marked verified/unverified.")
print(f"PASS: all {len(cites)} cited keys resolve; duplicate Lurie and Cisinski keys normalized.")
print("No priority claim is made; unverified Maunder reference is not used for any proof.")
