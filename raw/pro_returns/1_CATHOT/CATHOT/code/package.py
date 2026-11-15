"""Build the requested one-ZIP deliverable from explicit artifact classes."""
from pathlib import Path
from hashlib import sha256
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parent / 'CATHOT.zip'
MANIFEST = ROOT / 'ARCHIVE_MANIFEST.json'
OUTPUT = ROOT / 'code' / 'package.out'
ROOT_NAMES = {
    'README.md', 'CATHOT_paper.tex', 'CATHOT_paper.pdf',
    'CATHOT_paper.bbl', 'CATHOT_results.csv', 'CATHOT_references.bib',
    'CATHOT_report.md',
}

def selected_files():
    paths = []
    for path in ROOT.rglob('*'):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(ROOT)
        if '__pycache__' in relative.parts or path.suffix == '.pyc':
            continue
        if len(relative.parts) == 1 and relative.name in ROOT_NAMES:
            paths.append(path)
        elif relative.parts[0] == 'sections' and path.suffix == '.tex':
            paths.append(path)
        elif relative.parts[0] == 'code':
            paths.append(path)
        elif relative.parts[0] == 'research' and path.suffix in {'.md', '.csv', '.bib'}:
            paths.append(path)
    return sorted(paths)

OUTPUT.touch(exist_ok=True)
paths = selected_files()
required = [ROOT / name for name in ROOT_NAMES]
assert all(path in paths for path in required), 'Required deliverable absent'
output_text = (
    f'Archive: {ARCHIVE.name}\n'
    f'Root directory: {ROOT.name}/\n'
    f'Files hashed: {len(paths)}\n'
    f'Archive members: {len(paths) + 1} (including the manifest)\n'
    'Included: paper/PDF/bibliography/CSV/report, section sources, authored code and outputs, authored audit metadata.\n'
    'Excluded: complete third-party papers and extracted texts, TeX runtime and caches, Python bytecode, transient root build auxiliaries, page-review rasters.\n'
    'Manifest uses SHA-256 and excludes its own hash.\n'
    'This program performs deterministic file selection and checks ZIP CRC integrity; mathematical and structural checks are separate.\n'
)
OUTPUT.write_text(output_text)
hashes = {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest()
          for path in paths}
MANIFEST.write_text(json.dumps({'schema': 'cathot-sha256-v1', 'hashes': hashes},
                               indent=2, sort_keys=True) + '\n')
with zipfile.ZipFile(ARCHIVE, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in paths + [MANIFEST]:
        archive.write(path, arcname=str(Path(ROOT.name) / path.relative_to(ROOT)))
with zipfile.ZipFile(ARCHIVE) as archive:
    assert archive.testzip() is None, 'ZIP integrity failure'
    assert len(archive.namelist()) == len(paths) + 1
print(output_text, end='')
