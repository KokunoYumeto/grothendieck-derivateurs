"""Workspace-only LuaLaTeX repair and command wrapper.

The installed TeX tree contains ordinary packages but its generated ls-R,
formats and language files point into an absent /var/lib/texmf.  This script
uses disk lookup for the read-only installed trees, downloads only missing
Lua/APA support into a separate local tree, and builds lualatex.fmt locally.

Run:
    python STRATA/code/E_texenv.py --setup
    python STRATA/code/E_texenv.py --run lualatex -halt-on-error FILE.tex
The command wrapper preserves the caller's current directory.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tarfile
import urllib.request

PROJECT = Path(__file__).resolve().parents[1]
WORKSPACE = PROJECT.parent
ROOT = WORKSPACE / "STRATA_build" / "texenv"
TREE = ROOT / "texmf-local"
VAR = ROOT / "texmf-var"
CONFIG = ROOT / "texmf-config"
CACHE = ROOT / "cache"
DIST = Path("/usr/share/texlive/texmf-dist")
DEBIAN = Path("/usr/share/texmf")
PACKAGES = (
    "luaotfload", "lualibs", "lua-uni-algos", "luatexbase",
    "lualatex-math", "apacite",
)
MIRRORS = (
    "https://mirrors.mit.edu/CTAN/systems/texlive/tlnet/archive/",
    "https://mirror.math.princeton.edu/pub/CTAN/systems/texlive/tlnet/archive/",
    "https://mirrors.ctan.org/systems/texlive/tlnet/archive/",
)


def environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update({
        "TEXMFHOME": str(TREE),
        "TEXMFVAR": str(VAR),
        "TEXMFCONFIG": str(CONFIG),
        "TEXMFCACHE": str(CACHE),
        "TEXMFOUTPUT": str(ROOT),
        "TEXMF": "{" + ",".join(map(str, [CONFIG, VAR, TREE / "texmf-dist",
                                          TREE, DEBIAN, DIST])) + "}",
        "TEXMFDBS": str(TREE),
        "TEXFORMATS": str(VAR / "web2c") + "//:",
        "VARTEXFONTS": str(VAR / "fonts"),
        "MKTEXFMT": "0",
        "MKTEXPK": "0",
    })
    return env


def run(command: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    print("$ " + shlex.join(command), flush=True)
    result = subprocess.run(command, cwd=cwd, env=environment(), text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(result.stdout, end="", flush=True)
    if check and result.returncode:
        raise RuntimeError(f"Command failed with exit status {result.returncode}")
    return result


def fetch(package: str) -> tuple[str, Path, str]:
    archive = ROOT / "downloads" / (package + ".tar.xz")
    record = archive.with_suffix(archive.suffix + ".url")
    if archive.exists() and record.exists():
        return package, archive, record.read_text().strip()
    errors = []
    for mirror in MIRRORS:
        url = mirror + archive.name
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "STRATA-reproducible-build/1"})
            with urllib.request.urlopen(request, timeout=25) as response:
                data = response.read()
            if not data.startswith(b"\xfd7zXZ\x00"):
                raise ValueError("Response is not an xz archive")
            archive.write_bytes(data)
            record.write_text(url + "\n")
            return package, archive, url
        except Exception as error:
            errors.append(f"{url}: {error}")
    raise RuntimeError("\n".join(errors))


def setup() -> None:
    for directory in [TREE, VAR / "web2c" / "luahbtex", CONFIG, CACHE,
                      ROOT / "downloads", ROOT / "smoke"]:
        directory.mkdir(parents=True, exist_ok=True)
    env_record = {k: v for k, v in environment().items()
                  if k.startswith(("TEXMF", "TEXFORMATS", "VARTEX", "MKTEX"))}
    (ROOT / "environment.json").write_text(json.dumps(env_record, indent=2) + "\n")
    (ROOT / "environment.sh").write_text(
        "\n".join("export " + k + "=" + shlex.quote(v) for k, v in env_record.items()) + "\n")
    manifest = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        fetched = list(pool.map(fetch, PACKAGES))
    for package, archive, url in fetched:
        with tarfile.open(archive, "r:xz") as tf:
            tf.extractall(TREE, filter="data")
        item = {"package": package, "url": url, "bytes": archive.stat().st_size,
                "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}
        manifest.append(item)
        print(json.dumps(item), flush=True)
    (ROOT / "download_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    # Supply only generated English-language configuration; all patterns are
    # copied verbatim or referenced from the installed TeX distribution.
    language_dir = TREE / "tex" / "generic" / "config"
    language_dir.mkdir(parents=True, exist_ok=True)
    source_dir = DIST / "tex" / "generic" / "config"
    shutil.copyfile(source_dir / "language.us", language_dir / "language.dat")
    (language_dir / "language.def").write_text(
        (source_dir / "language.us.def").read_text() + "\n\\uselanguage{USenglish}\n")
    (language_dir / "language.dat.lua").write_text(
        (source_dir / "language.us.lua").read_text() + "\n}\n")

    # Provide the required outline-font maps without invoking system updmap.
    maps = sorted((DIST / "fonts" / "map" / "dvips" / "amsfonts").glob("*.map"))
    maps += [DIST / "fonts/map/dvips/rsfs/rsfs.map",
             DEBIAN / "fonts/map/dvips/lm/lm.map"]
    map_dir = TREE / "fonts" / "map" / "pdftex"
    map_dir.mkdir(parents=True, exist_ok=True)
    (map_dir / "pdftex.map").write_text(
        "\n".join(p.read_text() for p in maps if p.exists()))
    print("Generated local English language configuration and outline-font map.", flush=True)

    required = ["article.cls", "fontspec.sty", "amsmath.sty", "amssymb.sty",
                "amsthm.sty", "mathtools.sty", "mathrsfs.sty", "longtable.sty",
                "booktabs.sty", "array.sty", "enumitem.sty", "microtype.sty",
                "xcolor.sty", "natbib.sty", "hyperref.sty", "bookmark.sty",
                "needspace.sty", "apacite.sty", "apacite.bst",
                "luaotfload-main.lua", "lualatex.ini", "pdftex.map"]
    for filename in required:
        command = ["kpsewhich"]
        if filename.endswith(".lua"):
            command.append("--format=lua")
        run(command + [filename], ROOT)
    format_dir = VAR / "web2c" / "luahbtex"
    if not (format_dir / "lualatex.fmt").exists():
        run(["luahbtex", "--ini", "--interaction=nonstopmode", "--halt-on-error",
             "--jobname=lualatex", "lualatex.ini"], format_dir)
    print("Workspace LuaLaTeX format is ready.", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setup", action="store_true")
    parser.add_argument("--run", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.setup or args.run is None:
        setup()
    if args.run:
        raise SystemExit(subprocess.run(args.run, env=environment()).returncode)


if __name__ == "__main__":
    main()
