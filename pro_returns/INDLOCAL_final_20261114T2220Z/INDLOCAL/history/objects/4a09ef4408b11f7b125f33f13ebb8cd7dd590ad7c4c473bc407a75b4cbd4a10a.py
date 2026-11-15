#!/usr/bin/env python3
"""Retain every checkpoint member verbatim, without duplicating identical bytes.

Run from the final frozen package before archiving. Historical versions are
content-addressed; the manifest records every original checkpoint member.
This program never modifies a checkpoint archive.
"""
from pathlib import Path
from zipfile import ZipFile
import argparse
import hashlib
import json
from archive_policy import is_source_reproduction, should_include


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint-dir", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--restore", type=int)
    parser.add_argument("--destination", type=Path)
    args = parser.parse_args()
    package = Path(__file__).resolve().parents[1]
    history = package / "history"
    manifest_path = history / "checkpoint_members.json"

    if args.verify or args.restore is not None:
        manifest = json.loads(manifest_path.read_text())
        selected = manifest["checkpoints"]
        if args.restore is not None:
            selected = [c for c in selected if c["number"] == args.restore]
            if not selected or args.destination is None:
                parser.error("--restore requires an existing number and --destination")
            if args.destination.exists():
                parser.error("the restore destination must not already exist")
            args.destination.mkdir(parents=True)
        count = 0
        for checkpoint in selected:
            for item in checkpoint["members"]:
                source = package / item["stored_at"]
                data = source.read_bytes()
                if digest(data) != item["sha256"]:
                    raise SystemExit(f"Historical content mismatch: {source}")
                if args.restore is not None:
                    target = args.destination / item["original_path"]
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                count += 1
        print(json.dumps({"verified_members": count,
                          "checkpoints": len(selected)}, indent=2))
        return

    checkpoint_dir = args.checkpoint_dir or package.parent
    archives = sorted(checkpoint_dir.glob("INDLOCAL_checkpoint_[0-9][0-9].zip"))
    if not archives:
        raise SystemExit("No checkpoint archives found")
    history.mkdir(exist_ok=True)
    objects = history / "objects"
    objects.mkdir(exist_ok=True)
    current = {}
    for path in sorted(package.rglob("*")):
        if not path.is_file() or history in path.parents:
            continue
        rel = path.relative_to(package)
        if not should_include(rel):
            continue
        current.setdefault(digest(path.read_bytes()), []).append(rel.as_posix())

    stored_objects = {}
    checkpoints = []
    omitted_members = []
    for archive in archives:
        number = int(archive.stem.rsplit("_", 1)[1])
        checkpoint = {
            "number": number,
            "archive_name": archive.name,
            "archive_sha256": digest(archive.read_bytes()),
            "members": [],
        }
        with ZipFile(archive) as original:
            for entry in original.infolist():
                if entry.is_dir():
                    continue
                data = original.read(entry)
                sha = digest(data)
                original_path = Path(entry.filename)
                if original_path.is_absolute() or ".." in original_path.parts:
                    raise SystemExit(f"Unsafe historical path: {entry.filename}")
                preferred = original_path.relative_to("INDLOCAL").as_posix()
                if is_source_reproduction(preferred):
                    omitted_members.append({
                        "checkpoint": number,
                        "original_path": entry.filename,
                        "sha256": sha,
                        "bytes": len(data),
                        "reason": "Downloaded third-party source reproduction, not authored work; the source citation and authored audit are retained."
                    })
                    continue
                if sha in current:
                    candidates = current[sha]
                    stored_at = preferred if preferred in candidates else candidates[0]
                    state = "exact_bytes_retained_in_current_tree"
                else:
                    if sha not in stored_objects:
                        path = objects / (sha + original_path.suffix)
                        if path.exists() and path.read_bytes() != data:
                            raise SystemExit(f"Content-address collision: {path}")
                        if not path.exists():
                            path.write_bytes(data)
                        stored_objects[sha] = path.relative_to(package).as_posix()
                    stored_at = stored_objects[sha]
                    state = "superseded_version_retained_verbatim"
                checkpoint["members"].append({
                    "original_path": entry.filename,
                    "sha256": sha,
                    "bytes": len(data),
                    "stored_at": stored_at,
                    "state": state,
                })
        checkpoints.append(checkpoint)
    manifest = {
        "format": "INDLOCAL checkpoint member retention v1",
        "omitted_members": omitted_members,
        "checkpoints": checkpoints,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    (history / "README.md").write_text(
        "# Exact checkpoint history\n\n"
        f"Every authored file from checkpoints {checkpoints[0]['number']:02d}--{checkpoints[-1]['number']:02d} is retained byte for byte. "
        "The current paper and results table state the final conclusions; "
        "historical versions retain the wording and state reached earlier.\n\n"
        "`checkpoint_members.json` maps each original archive path to either "
        "an identical current file or a file in `objects/`. No authored proof, "
        "note, code, log or passage has been omitted. Downloaded third-party "
        "source reproductions accidentally included in an earlier checkpoint "
        "are listed under `omitted_members`, with their reasons. The manifest records SHA-256 "
        "hashes for the original archives and for every retained member.\n\n"
        "Verify all retained members from the package root:\n\n"
        "```sh\npython3 code/preserve_checkpoint_history.py --verify\n```\n\n"
        "Restore an earlier checkpoint's complete file tree to a new directory:\n\n"
        "```sh\npython3 code/preserve_checkpoint_history.py "
        "--restore 3 --destination /tmp/INDLOCAL_checkpoint_03_restored\n```\n\n"
        "This reproduces member contents and paths. The original immutable "
        "ZIP archives retain their own compression and metadata.\n"
    )
    print(json.dumps({
        "checkpoints": len(checkpoints),
        "checkpoint_members": sum(len(c["members"]) for c in checkpoints),
        "unique_historical_objects": len(stored_objects),
        "omitted_members": len(omitted_members),
    }, indent=2))


if __name__ == "__main__":
    main()
