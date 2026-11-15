"""Package this incomplete record under a fresh, never-overwritten ZIP name."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
allowed_root = {"README.md", "TOTEX2_paper.tex", "TOTEX2_paper.pdf",
                "TOTEX2_paper.aux", "TOTEX2_paper.bbl", "TOTEX2_results.csv",
                "TOTEX2_references.bib", "TOTEX2_report.md", "MANIFEST.json"}
allowed_code_suffixes = {".py", ".mjs", ".out", ".json", ".png"}
allowed_work_suffixes = {".tex", ".md", ".csv", ".bib"}


def files():
    selected = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if path.is_symlink() or not path.is_file():
            continue
        if any(p in {".build", "node_modules", "__pycache__", "sources", "akr_ocr"} for p in rel.parts):
            continue
        if len(rel.parts) == 1 and rel.name in allowed_root:
            selected.append(path)
        elif rel.parts[0] == "code" and path.suffix in allowed_code_suffixes:
            selected.append(path)
        elif rel.parts[0] == "work" and path.suffix in allowed_work_suffixes:
            selected.append(path)
    return sorted(selected)


def write_manifest():
    entries = []
    for path in files():
        if path.name == "MANIFEST.json":
            continue
        content = path.read_bytes()
        entries.append({"path": path.relative_to(ROOT).as_posix(), "bytes": len(content),
                        "sha256": hashlib.sha256(content).hexdigest()})
    manifest = {"status": "INCOMPLETE", "archive_root": "TOTEX2",
                "self_hash": "The manifest does not recursively hash itself.",
                "files": entries}
    (ROOT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2)+"\n")


def write_zip(target):
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in files():
            z.write(path, "TOTEX2/" + path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        manifest = json.loads(z.read("TOTEX2/MANIFEST.json"))
        for entry in manifest["files"]:
            data = z.read("TOTEX2/"+entry["path"])
            assert len(data) == entry["bytes"]
            assert hashlib.sha256(data).hexdigest() == entry["sha256"]
        assert z.read("TOTEX2/TOTEX2_report.md").startswith(b"INCOMPLETE\n")
        return len(z.namelist())


assert json.loads((ROOT / "code/package_verification.json").read_text())["status"] == "PASS"
assert json.loads((ROOT / "code/visual_review.json").read_text())["status"] == "PASS"
index = 1
while True:
    archive = ROOT.parent / f"TOTEX2_checkpoint_{index:02d}.zip"
    if not archive.exists():
        break
    index += 1
record = {"status": "INCOMPLETE", "archive_filename": archive.name,
          "rule": "Fresh sequential checkpoint; no existing archive replaced.",
          "contents": "Integrated paper, index, marked bibliography, report, supporting sources, all retained research programs and outputs.",
          "omitted": "Full downloaded primary-source bodies, source-page OCR intermediates, TeX cache, runtime dependency links, and temporary review renders.",
          "verification": "The script checks ZIP CRCs and every manifest size/hash before returning successfully."}
(ROOT / "code/package_checkpoint.out").write_text(json.dumps(record, indent=2)+"\n")
write_manifest()
count = write_zip(archive)
print(json.dumps({"archive": str(archive), "files": count,
                  "bytes": archive.stat().st_size,
                  "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                  "archive_integrity": "PASS", "mathematical_status": "INCOMPLETE"}, indent=2))
