"""Inventory the supplied archive and extract it without escaping the destination."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[2]
archive = ROOT / 'upload/7_BISITE_background(1).zip'
destination = ROOT / 'background'
destination.mkdir(exist_ok=True)
lines = [f'SHA256 archive: {hashlib.sha256(archive.read_bytes()).hexdigest()}']
with zipfile.ZipFile(archive) as z:
    for info in z.infolist():
        target = (destination / info.filename).resolve()
        if not target.is_relative_to(destination.resolve()):
            raise ValueError(f'Unsafe member: {info.filename}')
        lines.append(f'{info.file_size:>10}  {info.filename}')
    z.extractall(destination)
out = ROOT / 'BISITE/code/00_inventory.out.txt'
out.write_text('\n'.join(lines)+'\n')
print(f'Extracted {len(lines)-1} members; inventory: {out}')
