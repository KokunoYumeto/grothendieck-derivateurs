"""Package only release deliverables, excluding caches and source-book extracts."""
from pathlib import Path
import csv
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ZIP = ROOT.parent / "GALOIS.zip"
required = ["GALOIS_paper.tex", "GALOIS_paper.pdf", "GALOIS_results.csv",
            "GALOIS_references.bib", "GALOIS_report.md", "GALOIS_paper.log",
            "GALOIS_paper.bbl", "README.txt"]
for name in required:
    assert (ROOT/name).is_file(), name
stats = json.loads((ROOT/"research/release_statistics.json").read_text())
assert stats["statements"] == 74 and stats["pdf_pages"] == 66
assert len(list(csv.DictReader((ROOT/"GALOIS_results.csv").open()))) == 74
assert len(list(csv.DictReader((ROOT/"research/D_audit.csv").open()))) == 21
assert (ROOT/"GALOIS_report.md").stat().st_size > 12000

support = ROOT.parent/"tmp/tex_runtime/upstream_packages.json"
if support.exists():
    (ROOT/"research/upstream_tex_packages.json").write_bytes(support.read_bytes())

def selected():
    result = [ROOT/name for name in required]
    result += sorted((ROOT/"sections").glob("*.tex"))
    result += sorted(p for p in (ROOT/"code").iterdir() if p.suffix in (".py", ".out"))
    result += sorted(p for p in (ROOT/"research").iterdir()
                     if p.suffix in (".md", ".bib", ".json", ".csv")
                     and "checkpoint" not in p.name)
    return result

output = (
    "PASS: release preflight matched 74 assertions, 66 PDF pages, and 21 manuscript audit rows.\n"
    "PASS: required deliverables and complete research report are present.\n"
    "Selected sources, code, outputs, audit, and metadata only; no caches, private environment, or background source extracts.\n"
    "Archive: GALOIS.zip; internal paths are rooted at GALOIS/.\n"
)
(ROOT/"code/build_release.out").write_text(output)
paths = selected()
manifest = "".join(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.relative_to(ROOT).as_posix()+"\n" for p in paths)
(ROOT/"RELEASE_MANIFEST.sha256").write_text(manifest)
paths.append(ROOT/"RELEASE_MANIFEST.sha256")
with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
    for path in paths:
        bundle.write(path, "GALOIS/"+path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(ZIP) as bundle:
    assert bundle.testzip() is None
    assert len(bundle.namelist()) == len(set(bundle.namelist())) == len(paths)
    for line in manifest.splitlines():
        expected, name = line.split("  ", 1)
        assert hashlib.sha256(bundle.read("GALOIS/"+name)).hexdigest() == expected, name
print(output, end="")
