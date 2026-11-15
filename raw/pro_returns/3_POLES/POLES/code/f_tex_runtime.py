"""Repair this workspace's incomplete TeX Live installation without system writes.

The container supplies LuaHBTeX and TeX macro trees, but omits generated lookup
databases/formats and some Lua font packages.  This module installs only five
explicit public CTAN packages under tmp/tex, copies the shipped English language
configuration, composes the existing font maps, and builds lualatex.fmt locally.
It never changes HOME or a system directory.  A normal complete TeX installation
does not require this repair; build_lualatex.py can use it with --system-tex.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT.parent / "tmp" / "tex"
DIST = Path("/usr/share/texlive/texmf-dist")
SYSTEM_TEXMF = Path("/usr/share/texmf")
PACKAGES = {
    "luaotfload": "https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaotfload.tar.xz",
    "lualibs": "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lualibs.tar.xz",
    "lua-uni-algos": "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-uni-algos.tar.xz",
    "lua-alt-getopt": "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/lua-alt-getopt.tar.xz",
    "tex-gyre": "https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/tex-gyre.tar.xz",
}


def _install_packages() -> None:
    downloads = RUNTIME / "downloads"
    local = RUNTIME / "texmf"
    manifest_path = ROOT / "code" / "f_tex_dependencies.json"
    previous = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest = {}
    for name, url in PACKAGES.items():
        archive = downloads / (name + ".tar.xz")
        if not archive.exists():
            print(f"Downloading explicit dependency {name} from {url}", flush=True)
            request = urllib.request.Request(url, headers={"User-Agent": "POLES-reproducible-LuaLaTeX-build/1.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
            archive.write_bytes(data)
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        expected = previous.get(name, {}).get("sha256")
        if expected is not None and digest != expected:
            raise RuntimeError(f"{name}: CTAN archive changed; inspect/update the dependency lock deliberately")
        manifest[name] = {"url": url, "sha256": digest, "bytes": archive.stat().st_size}
        marker = local / ".installed" / f"{name}-{digest}"
        if marker.exists():
            continue
        with tarfile.open(archive, "r:xz") as tar:
            for member in tar.getmembers():
                path = PurePosixPath(member.name)
                if path.is_absolute() or ".." in path.parts:
                    raise RuntimeError(f"Unsafe archive path: {member.name}")
                parts = path.parts
                if parts and parts[0] == "texmf-dist":
                    parts = parts[1:]
                # TeX Live metadata is retained in the download, not mixed into TEXMF.
                if not parts or parts[0] == "tlpkg":
                    continue
                target = local.joinpath(*parts)
                if member.isdir():
                    target.mkdir(parents=True, exist_ok=True)
                elif member.isfile():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with tar.extractfile(member) as source, target.open("wb") as dest:
                        shutil.copyfileobj(source, dest)
                else:
                    raise RuntimeError(f"Unexpected non-regular archive entry: {member.name}")
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(digest + "\n")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")


def _generated_configuration() -> None:
    config = RUNTIME / "texmf" / "tex" / "generic" / "config"
    config.mkdir(parents=True, exist_ok=True)
    source = DIST / "tex" / "generic" / "config"
    (config / "language.dat").write_text((source / "language.us").read_text())
    (config / "language.def").write_text((source / "language.us.def").read_text() + "\\uselanguage {USenglish}\n")
    (config / "language.dat.lua").write_text((source / "language.us.lua").read_text() + "}\n")
    maps = [
        *sorted((DIST / "fonts/map/dvips/amsfonts").glob("*.map")),
        DIST / "fonts/map/dvips/rsfs/rsfs.map",
        SYSTEM_TEXMF / "fonts/map/dvips/lm/lm.map",
    ]
    lines = []
    seen = set()
    for path in maps:
        for line in path.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith(("%", "#")):
                continue
            font = line.split()[0]
            if font not in seen:
                lines.append(line)
                seen.add(font)
    mapdir = RUNTIME / "texmf" / "fonts" / "map" / "pdftex" / "poles"
    mapdir.mkdir(parents=True, exist_ok=True)
    (mapdir / "pdftex.map").write_text("% Composed from installed AMS/CM, RSFS and LM maps.\n" + "\n".join(lines) + "\n")


def tex_environment(prepare: bool = True) -> dict[str, str]:
    """Return the inherited environment with only TeX-specific variables changed."""
    for directory in ("downloads", "texmf", "texmf-var", "texmf-config", "cache", "formats", "fonts"):
        (RUNTIME / directory).mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    overrides = {
        "TEXMF": "{" + ",".join(map(str, [RUNTIME / "texmf", RUNTIME / "texmf-var", DIST, SYSTEM_TEXMF, Path("/etc/texmf")])) + "}",
        "TEXMFCNF": str(DIST / "web2c"),
        "TEXMFVAR": str(RUNTIME / "texmf-var"),
        "TEXMFCONFIG": str(RUNTIME / "texmf-config"),
        "TEXMFCACHE": str(RUNTIME / "cache"),
        # Permit Lua's font cache writes in this one workspace output tree while
        # retaining TeX's default paranoid openout_any=p restriction.
        "TEXMFOUTPUT": str(RUNTIME),
        "TEXFORMATS": str(RUNTIME / "formats") + ":",
        "VARTEXFONTS": str(RUNTIME / "fonts"),
    }
    env.update(overrides)
    if prepare:
        _install_packages()
        _generated_configuration()
        (ROOT / "code" / "f_tex_environment.json").write_text(json.dumps(overrides, indent=2) + "\n")
        fmt = RUNTIME / "formats" / "lualatex.fmt"
        if not fmt.exists():
            command = ["luahbtex", "--ini", "--jobname=lualatex", "--progname=lualatex", "--interaction=nonstopmode", "--halt-on-error", "lualatex.ini"]
            print("Building workspace-local LuaLaTeX format", flush=True)
            result = subprocess.run(command, cwd=fmt.parent, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (ROOT / "code" / "f_tex_format_output.txt").write_text(result.stdout)
            if result.returncode:
                print(result.stdout, flush=True)
                raise RuntimeError(f"LuaLaTeX format build failed with code {result.returncode}")
            print(f"Built {fmt}", flush=True)
    return env


if __name__ == "__main__":
    tex_environment()
    print("Workspace-local TeX runtime prepared successfully.")
