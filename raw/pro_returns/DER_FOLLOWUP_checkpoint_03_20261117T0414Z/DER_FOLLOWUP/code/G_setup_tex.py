#!/usr/bin/env python3
"""Create a workspace-local LuaLaTeX format when distro caches are absent."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
base = root / "build/tex_runtime"
for sub in ("formats", "texmfvar", "texmfconfig", "texmfcache", "texmf"):
    (base / sub).mkdir(parents=True, exist_ok=True)
archives = {
    "luaotfload.zip": (
        "https://tex.org.uk/macros/luatex/generic/luaotfload.zip",
        "21e08eef057c9e2e52767aaf7f7d8d80a8d9a278346a2067b5cba07f0c4256da"),
    "lualibs.zip": (
        "https://tex.org.uk/macros/luatex/generic/lualibs.zip",
        "f6e59d4455b3af2bcee2fa4ae35f3a56d7247351852b9d1880cba4e5bff271e3"),
    "lualibs.tds.zip": (
        "https://tex.org.uk/install/macros/luatex/generic/lualibs.tds.zip",
        "49f28367ad39f643192f016ce89a47b11241ac78c20f76e8947807282423556e"),
    "lua-uni-algos.zip": (
        "https://tex.org.uk/macros/luatex/generic/lua-uni-algos.zip",
        "664c5eb615ec5f05678fdc5bc37483a8f6df5c9ec8b0e9adabbbfb8f42a92418"),
}
manifest = []
for name, (url, digest) in archives.items():
    archive = base / name
    if not archive.exists():
        subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error",
                        "--max-time", "60", url, "--output", str(archive)], check=True)
    actual = hashlib.sha256(archive.read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f"Archive {name} changed upstream; expected {digest}, got {actual}.")
    manifest.append({"archive": name, "url": url, "sha256": digest,
                     "bytes": archive.stat().st_size})
(base / "archives.json").write_text(json.dumps(manifest, indent=2) + "\n")
fontmaps = [Path("/usr/share/texmf/fonts/map/dvips/lm/lm.map")]
fontmaps += sorted(Path("/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts").glob("*.map"))
fontmaps += sorted(Path("/usr/share/texlive/texmf-dist/fonts/map/dvips/rsfs").glob("*.map"))
mapdir = base / "texmf/fonts/map/pdftex/workspace"
mapdir.mkdir(parents=True, exist_ok=True)
(mapdir / "pdftex.map").write_text("\n".join(p.read_text() for p in fontmaps))
for package in ("luaotfload", "lualibs", "lua-uni-algos"):
    archive = base / (package + ".zip")
    if not archive.exists():
        continue
    luadir = base / "texmf/tex/luatex" / package
    docdir = base / "texmf/doc/luatex" / package
    luadir.mkdir(parents=True, exist_ok=True)
    docdir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        for entry in z.infolist():
            name = Path(entry.filename).name
            if entry.is_dir():
                continue
            if name.endswith((".lua", ".sty", ".cnf")):
                (luadir / name).write_bytes(z.read(entry))
            elif name in ("COPYING", "LICENSE", "README.md", "NEWS"):
                (docdir / name).write_bytes(z.read(entry))
for archive in base.glob("*.tds.zip"):
    with zipfile.ZipFile(archive) as z:
        for entry in z.infolist():
            parts = Path(entry.filename).parts
            if entry.is_dir() or not parts or ".." in parts or Path(entry.filename).is_absolute():
                continue
            target = base / "texmf" / entry.filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(entry))
overrides = {
    "TEXMF": "{" + str(base / "texmf") + ",/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}",
    "TEXMFVAR": str(base / "texmfvar"),
    "TEXMFCONFIG": str(base / "texmfconfig"),
    # LuaTeX's restricted file writer rejects absolute cache paths.  Builds
    # run with cwd=root, so this workspace-relative path keeps the normal
    # openout policy intact and permits luaotfload's ordinary cache writes.
    "TEXMFCACHE": "build/tex_runtime/texmfcache",
    "TEXFORMATS": str(base / "formats") + "//",
}
(base / "environment.json").write_text(json.dumps(overrides, indent=2) + "\n")
env = os.environ.copy()
env.update(overrides)
fmt = base / "formats/lualatex.fmt"
if not fmt.exists():
    cmd = ["luahbtex", "--ini", "--progname=lualatex", "--interaction=nonstopmode", "--halt-on-error", "--jobname=lualatex", "--output-directory=" + str(base / "formats"), "lualatex.ini"]
    run = subprocess.run(cmd, cwd=root, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    (base / "format_build.txt").write_text(run.stdout)
    if run.returncode:
        print(run.stdout[-8000:])
        raise SystemExit(run.returncode)
print(json.dumps({"format": str(fmt), "bytes": fmt.stat().st_size, "environment_file": str(base / "environment.json")}, indent=2))
