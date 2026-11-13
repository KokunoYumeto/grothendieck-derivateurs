"""Refresh the surviving source-audit fragments without changing root files."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
source = root.parent / "TOTEX2"
polynomial_audit = r"""We also read the full interpolation verification in TOTASPH C.8--C.10.
The integral coordinate change $x_i=z_i-z_{i+1}$ reduces compatible
coface data to coordinate-hyperplane interpolation, whose alternating
sum preserves homogeneity and augmentation one. The prescriptions
$D_iC_{n,k}=C_{n-1,2k}\prod_{l\ne i}y_l^k$ agree on adjacent
intersections directly and on nonadjacent intersections by the
inductive normalized-face identity. Gap encoding turns the resulting
polynomial into an affine arrow equalizing all cofaces. The simplicial
identities then equalize every ordinary parallel family. This confirms
the exactness used here without treating the unopened 1974 body as a proof."""
latest = (source / "work/manuscript_audit.tex").read_text()
anchor = "does not identify which adjacent inclusion is strict."
assert latest.count(anchor) == 1
latest = latest.replace(anchor, anchor + "\n\n" + polynomial_audit)
(root / "work/manuscript_audit.tex").write_text(latest)
for name in ("literature_main.md", "literature_results_fragment.csv", "literature_report_fragment.md",
             "fraisse_coinvariants.md", "source_audit.tex", "literature_references.bib"):
    src = source / "work" / name
    if src.exists():
        shutil.copyfile(src, root / "work" / name)
bib = root / "work/literature_references.bib"
bib.write_text(bib.read_text().replace('pr{"a}sentierbare', r'pr{\"a}sentierbare'))
print("Refreshed latest literature fragments; retained independent polynomial audit.")
print("Original TOTEX2 assembly unchanged.")
