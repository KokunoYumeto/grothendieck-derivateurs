#!/usr/bin/env python3
"""Package only the deliverables and their reproducibility records.

Run from any directory.  The default destination is ../PATHS.zip.  Copyrighted
source extracts, local TeX caches and transient failed build logs are excluded.
Every distributed file except the manifest itself is listed by SHA-256.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = [
    'PATHS_paper.tex', 'PATHS_paper.pdf', 'PATHS_results.csv',
    'PATHS_references.bib', 'PATHS_report.md',
]
EXCLUDED_AUDIT = {'compile_initial.txt'}


def contents():
    paths = [ROOT / name for name in ROOT_FILES]
    for directory in ['sections', 'code', 'research', 'audit']:
        for path in (ROOT / directory).iterdir():
            if not path.is_file() or path.name.startswith('.'):
                continue
            if directory == 'research' and path.suffix not in {'.md', '.bib', '.json', '.txt'}:
                continue
            if directory == 'research' and path.name in {'dk_calculating.txt', 'dk_function.txt'}:
                continue
            if directory == 'audit' and path.name in EXCLUDED_AUDIT:
                continue
            if directory == 'code' and path.suffix not in {'.py', '.md', '.json', '.jsonl', '.txt', '.out'}:
                continue
            paths.append(path)
    assert all(path.is_file() for path in paths)
    return sorted(set(paths), key=lambda path: path.relative_to(ROOT).as_posix())


def make_and_verify(destination):
    paths = contents()
    manifest = ROOT / 'PATHS_manifest.sha256'
    manifest.write_text(''.join(
        hashlib.sha256(path.read_bytes()).hexdigest() + '  ' +
        path.relative_to(ROOT).as_posix() + '\n' for path in paths))
    paths.append(manifest)
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in paths:
            z.write(path, 'PATHS/' + path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(destination) as z:
        assert z.testzip() is None, 'ZIP CRC failure'
        assert set(z.namelist()) == {
            'PATHS/' + path.relative_to(ROOT).as_posix() for path in paths}
        for line in z.read('PATHS/PATHS_manifest.sha256').decode().splitlines():
            digest, name = line.split('  ', 1)
            assert hashlib.sha256(z.read('PATHS/' + name)).hexdigest() == digest, name
    return len(paths)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(ROOT.parent / 'PATHS.zip'))
    args = parser.parse_args()
    destination = Path(args.output).resolve()
    assert not destination.is_relative_to(ROOT), 'Store the ZIP outside its input directory'
    verification = json.loads((ROOT / 'audit/final_verification.json').read_text())
    assert verification['passed']
    inventory_path = ROOT / 'audit/package_inventory.json'
    packaging_log = ROOT / 'code/make_zip_output.txt'
    # The inventory describes payload files; it excludes the inventory and the
    # packaging log to avoid a recursively self-describing length or checksum.
    payload = [p for p in contents() if p not in {inventory_path, packaging_log}]
    inventory = {
        'payload_files': len(payload),
        'files': [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size}
                  for p in payload],
        'exclusions': ['original source corpus and extracts', 'local build runtime',
                       'rendered page intermediates', 'transient failed build log'],
    }
    inventory_path.write_text(json.dumps(inventory, indent=2) + '\n')
    # Verify a complete snapshot before recording success, then repeat after
    # inserting the success record.  The final archive is never self-hashed.
    make_and_verify(destination)
    packaging_log.write_text(
        'PASS: the ZIP CRC and every SHA-256 inventory entry were checked.\n'
        'PASS: the exact expected file set was checked.\n'
        'PASS: the final archive repeats these checks after this log is included.\n'
        'The archive checksum is external; the internal manifest covers every other distributed file.\n')
    count = make_and_verify(destination)
    summary = {
        'archive': destination.name,
        'files': count,
        'bytes': destination.stat().st_size,
        'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
        'crc_and_manifest_verified': True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
