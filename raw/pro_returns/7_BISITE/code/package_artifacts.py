"""Create and verify the single BISITE return archive.

The manifest hashes every delivered file except itself. The archive is
deterministic for fixed inputs; generated TeX caches and supplied sources
are deliberately excluded. This program's JSON output is also included.
"""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / "BISITE.zip"
MANIFEST = ROOT / "MANIFEST.json"
OUTPUT = Path(__file__).with_suffix(".out.json")
ALLOWED_SUFFIXES = {".tex", ".pdf", ".csv", ".bib", ".md", ".py",
                    ".json", ".txt", ".bbl", ".log", ".blg"}
EXCLUDED_NAMES = {"missfont.log"}


def payload_files():
    result = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if not path.is_file() or path == MANIFEST:
            continue
        if any(part.startswith(".") or part == "__pycache__" for part in rel.parts):
            continue
        if path.suffix not in ALLOWED_SUFFIXES or path.name in EXCLUDED_NAMES:
            continue
        result.append(path)
    return sorted(result, key=lambda p: p.relative_to(ROOT).as_posix())


def digest(data):
    return hashlib.sha256(data).hexdigest()


rows = list(csv.DictReader((ROOT / "BISITE_results.csv").open()))
validation = json.loads((ROOT / "code/validate_package.out.json").read_text())
visual = json.loads((ROOT / "code/visual_qa.out.json").read_text())
pdf_hash = digest((ROOT / "BISITE_paper.pdf").read_bytes())
assert validation["pdf_sha256"] == visual["pdf_sha256"] == pdf_hash
assert validation["pdf_pages"] == visual["pages_reviewed"] == 76
assert len(validation["finite_certificate_reruns"]) == 9
assert visual["result"] == "passed"
assert len(rows) == 126

# Write the output before hashing, so it can itself be covered by the
# manifest. It is printed only after all archive verification succeeds.
OUTPUT.touch(exist_ok=True)
files = payload_files()
result = {
    "archive": ARCHIVE.name,
    "archive_root": ROOT.name + "/",
    "payload_files": len(files),
    "archive_entries_including_manifest": len(files) + 1,
    "statements": len(rows),
    "statuses": dict(Counter(row["status"] for row in rows)),
    "pdf_pages": validation["pdf_pages"],
    "pdf_sha256": pdf_hash,
    "manifest_scope": "Every delivered file except MANIFEST.json itself",
    "verification": ["ZIP CRC", "unique safe paths", "required files",
                     "all payload bytes match their SHA-256 manifest entries",
                     "PDF identity agrees with validation and visual review"],
    "status": "passed"
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
entries = []
for path in files:
    data = path.read_bytes()
    entries.append({"path": path.relative_to(ROOT).as_posix(),
                    "bytes": len(data), "sha256": digest(data)})
manifest = {
    "package": "BISITE",
    "credit": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "date": "2026-11-11",
    "algorithm": "SHA-256",
    "manifest_self_excluded": True,
    "files": entries
}
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as zf:
    for path in [*files, MANIFEST]:
        name = ROOT.name + "/" + path.relative_to(ROOT).as_posix()
        info = zipfile.ZipInfo(name, date_time=(2026, 11, 11, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        zf.writestr(info, path.read_bytes(), compresslevel=9)

with zipfile.ZipFile(ARCHIVE) as zf:
    assert zf.testzip() is None
    names = zf.namelist()
    assert len(names) == len(set(names)) == len(files) + 1
    assert all(name.startswith("BISITE/") and ".." not in Path(name).parts
               and not any(part.startswith(".") for part in Path(name).parts)
               for name in names)
    required = {"BISITE_paper.tex", "BISITE_paper.pdf", "BISITE_results.csv",
                "BISITE_references.bib", "BISITE_report.md", "README.md",
                "MANIFEST.json", "code/package_artifacts.py",
                "code/validate_package.out.json", "code/visual_qa.out.json"}
    assert {"BISITE/" + name for name in required} <= set(names)
    for entry in entries:
        data = zf.read("BISITE/" + entry["path"])
        assert len(data) == entry["bytes"]
        assert digest(data) == entry["sha256"], entry["path"]
    assert json.loads(zf.read("BISITE/MANIFEST.json")) == manifest

print(json.dumps(result, indent=2))
