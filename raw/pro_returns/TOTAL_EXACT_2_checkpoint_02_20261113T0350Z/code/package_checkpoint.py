"""Create a non-overwriting research checkpoint with a SHA-256 manifest.

This is packaging, not a mathematical verification.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def included(path):
    rel = path.relative_to(ROOT)
    if not path.is_file():
        return False
    if any(p in {".build", "__pycache__", "sources"} for p in rel.parts):
        return False
    if rel.parts[:2] == ("code", "qa") and path.name.startswith("page-") and path.suffix == ".png":
        return False
    if rel.name == "MANIFEST.sha256.tsv":
        return False
    if len(rel.parts) == 1 and path.suffix in {".log", ".blg", ".out", ".toc"}:
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="New ZIP basename, e.g. TOTEX2_checkpoint_01.zip")
    args = parser.parse_args()
    if Path(args.name).name != args.name or not args.name.endswith(".zip"):
        raise SystemExit("Supply a ZIP basename only")
    target = ROOT.parent / args.name
    if target.exists():
        raise SystemExit("Refusing to overwrite existing archive: " + str(target))
    files = sorted(p for p in ROOT.rglob("*") if included(p))
    # Snapshot each file once: the manifest and ZIP must describe the same
    # bytes even if a separate research worker later updates a working file.
    snapshots = [(str(p.relative_to(ROOT)), p.read_bytes()) for p in files]
    records = [(name, len(content), hashlib.sha256(content).hexdigest())
               for name, content in snapshots]
    manifest = ROOT / "MANIFEST.sha256.tsv"
    manifest.write_text("path\tbytes\tsha256\n" + "".join(
        f"{name}\t{size}\t{digest}\n" for name, size, digest in records))
    snapshots.append(("MANIFEST.sha256.tsv", manifest.read_bytes()))
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for name, content in snapshots:
            z.writestr("TOTEX2/" + name, content)
    with zipfile.ZipFile(target) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError("CRC failure: " + bad)
        for name, size, digest in records:
            content = z.read("TOTEX2/" + name)
            assert len(content) == size
            assert hashlib.sha256(content).hexdigest() == digest
    print(json.dumps({"archive": str(target), "files": len(snapshots),
                      "bytes": target.stat().st_size,
                      "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                      "manifest_and_crc": "PASS",
                      "mathematical_status": "INCOMPLETE"}, indent=2))


if __name__ == "__main__":
    main()
