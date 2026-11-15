"""Reproduce archive validation, inventory, and PDF text caches used in the audit.

Run from the workspace root; only the authoritative attached archive is extracted.
The earlier archives are inspected for size and digest, not merged into the sources.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
records = []
for path in sorted((ROOT / 'upload').glob('*.zip')):
    with zipfile.ZipFile(path) as archive:
        records.append(dict(name=path.name, bytes=path.stat().st_size,
                            sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                            members=len(archive.namelist())))
print(json.dumps(records, indent=2))
expected = 'c4cd2af79619d296dadcb3b30b5b1740c8f0e408f538d820a2d0fddb83ac3c09'
archive_path = ROOT / 'upload' / '5_STRATA_background.zip'
assert hashlib.sha256(archive_path.read_bytes()).hexdigest() == expected
destination = ROOT / 'background'
if not destination.exists():
    with zipfile.ZipFile(archive_path) as archive:
        for name in archive.namelist():
            relative = Path(name)
            assert not relative.is_absolute() and '..' not in relative.parts
        archive.extractall(destination)

cache = ROOT / 'STRATA' / 'audit' / 'text'
cache.mkdir(parents=True, exist_ok=True)
targets = {
    'LurieHA': ('papers/Lurie_HA/HA.pdf', 1370, 1553),
    'Cisinski2009': ('papers/Cisinski_lcfunctors/lcmodcat3.pdf', None, None),
    'Carcacia2026': ('papers/2611.09718/2611.09718.pdf', None, None),
}
for key, (relative, first, last) in targets.items():
    path = destination / relative
    out = cache / (key + '.txt')
    command = ['pdftotext', '-layout']
    if first is not None:
        command.extend(['-f', str(first)])
    if last is not None:
        # The attached edition's page count can differ from the web edition.
        info = subprocess.check_output(['pdfinfo', str(path)], text=True)
        pages = int(next(line.split(':', 1)[1] for line in info.splitlines()
                         if line.startswith('Pages:')))
        command.extend(['-l', str(min(last, pages))])
    subprocess.run(command + [str(path), str(out)], check=True)
    print(key, 'extracted', out.stat().st_size, 'text bytes')
