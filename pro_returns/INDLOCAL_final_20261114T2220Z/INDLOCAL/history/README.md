# Exact checkpoint history

Every authored file from checkpoints 01--07 is retained byte for byte. The current paper and results table state the final conclusions; historical versions retain the wording and state reached earlier.

`checkpoint_members.json` maps each original archive path to either an identical current file or a file in `objects/`. No authored proof, note, code, log or passage has been omitted. Downloaded third-party source reproductions accidentally included in an earlier checkpoint are listed under `omitted_members`, with their reasons. The manifest records SHA-256 hashes for the original archives and for every retained member.

Verify all retained members from the package root:

```sh
python3 code/preserve_checkpoint_history.py --verify
```

Restore an earlier checkpoint's retained file tree to a new directory:

```sh
python3 code/preserve_checkpoint_history.py --restore 3 --destination /tmp/INDLOCAL_checkpoint_03_restored
```

This reproduces all retained member contents and paths; the two listed third-party source reproductions remain omitted. The original immutable ZIP archives retain their own compression and metadata.
