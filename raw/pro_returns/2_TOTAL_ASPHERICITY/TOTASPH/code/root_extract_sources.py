"""Read only the supplied archive; extract PDFs for local scholarly inspection.

Run from the parent of TOTASPH. Extracted source text stays outside the deliverable.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import zipfile

root = Path(__file__).resolve().parents[2]
archives = {}
for path in sorted((root / "upload").glob("*.zip")):
    with zipfile.ZipFile(path) as archive:
        archives[path.name] = {
            name: hashlib.sha256(archive.read(name)).hexdigest()
            for name in archive.namelist() if not name.endswith("/")
        }
base = archives["2_TOTAL_ASPHERICITY_background.zip"]
audit = {
    name: {"files": len(items),
           "missing_from_base": sorted(set(items) - set(base)),
           "different_common": [n for n in items if n in base and items[n] != base[n]]}
    for name, items in archives.items()
}
print(json.dumps(audit, indent=2))
destination = root / "background_text"
destination.mkdir(exist_ok=True)
for source in sorted((root / "background" / "papers").rglob("*.pdf")):
    target = destination / (source.parent.name + ".txt")
    subprocess.run(["pdftotext", "-layout", str(source), str(target)], check=True)
    print(f"{source.relative_to(root)} -> {target.relative_to(root)} ({target.stat().st_size} bytes)")
