"""Prepare missing TeX support in this workspace without changing system files.

The deliverable itself is ordinary LuaLaTeX. This helper addresses the
execution image's missing filename database, Lua font loader, and formats.
Downloaded upstream packages are unmodified and are temporary build inputs.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tarfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "tmp" / "tex_runtime"
RUNTIME.mkdir(parents=True, exist_ok=True)
packages = {
    "luaotfload": "https://tex.org.uk/macros/luatex/generic/luaotfload.zip",
    "lualibs": "https://tex.org.uk/systems/texlive/tlnet/archive/lualibs.tar.xz",
    "apacite": "https://tex.org.uk/systems/texlive/tlnet/archive/apacite.tar.xz",
    "lua-uni-algos": "https://tex.org.uk/systems/texlive/tlnet/archive/lua-uni-algos.tar.xz",
}
manifest = []
for name, url in packages.items():
    archive = RUNTIME / (name + (".tar.xz" if url.endswith(".tar.xz") else ".zip"))
    if not archive.exists():
        with urllib.request.urlopen(url, timeout=60) as response:
            archive.write_bytes(response.read())
    data = archive.read_bytes()
    destination = RUNTIME / name
    destination.mkdir(exist_ok=True)
    if url.endswith(".tar.xz"):
        with tarfile.open(archive) as bundle:
            bundle.extractall(destination, filter="data")
    else:
        with zipfile.ZipFile(archive) as bundle:
            for item in bundle.infolist():
                target = (destination / item.filename).resolve()
                if not target.is_relative_to(destination.resolve()):
                    raise ValueError("Unsafe upstream archive member")
            bundle.extractall(destination)
    manifest.append({"package": name, "url": url, "bytes": len(data),
                     "sha256": hashlib.sha256(data).hexdigest()})
    print(f"Prepared {name}: {len(data)} bytes", flush=True)

env = os.environ.copy()
system = [Path("/usr/share/texlive/texmf-dist"), Path("/usr/share/texmf")]
env["TEXINPUTS"] = ".:" + ":".join(str(p / "tex") + "//" for p in system) + ":" + str(RUNTIME) + "//:"
env["LUAINPUTS"] = env["TEXINPUTS"]
env["BSTINPUTS"] = ".:" + ":".join(str(p / "bibtex" / "bst") + "//" for p in system) + ":" + str(RUNTIME) + "//:"
env["BIBINPUTS"] = ".:"
for variable, sub in (("TFMFONTS", "tfm"), ("VFFONTS", "vf"),
                      ("T1FONTS", "type1"), ("TTFONTS", "truetype"),
                      ("OPENTYPEFONTS", "opentype"), ("ENCFONTS", "enc"),
                      ("TEXFONTMAPS", "map")):
    env[variable] = ":".join(str(p / "fonts" / sub) + "//" for p in system) + ":"
fontmaps = Path("/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts")
(RUNTIME / "pdftex.map").write_text("\n".join(
    (fontmaps / name).read_text() for name in
    ("cm.map", "cmextra.map", "symbols.map", "latxfont.map")))
env["TEXFONTMAPS"] = str(RUNTIME) + "//:" + env["TEXFONTMAPS"]
for variable, directory in (("TEXMFVAR", "var"), ("TEXMFCONFIG", "config"),
                            ("TEXMFCACHE", "cache")):
    path = ROOT / "GALOIS" / ("tex-" + directory)
    path.mkdir(exist_ok=True)
    env[variable] = "tex-" + directory
env["TEXFORMATS"] = str(RUNTIME) + "//:"
# Persist only the TeX-specific overrides, never a copy of the shell environment.
tex_keys = {"TEXINPUTS", "LUAINPUTS", "BSTINPUTS", "BIBINPUTS", "TFMFONTS",
            "VFFONTS", "T1FONTS", "TTFONTS", "OPENTYPEFONTS", "ENCFONTS",
            "TEXFONTMAPS", "TEXMFVAR", "TEXMFCONFIG", "TEXMFCACHE", "TEXFORMATS"}
(RUNTIME / "environment.json").write_text(json.dumps({k: env[k] for k in sorted(tex_keys)}, indent=2))
(RUNTIME / "upstream_packages.json").write_text(json.dumps(manifest, indent=2))
if not (RUNTIME / "lualatex.fmt").exists():
    result = subprocess.run(
        ["luahbtex", "--ini", "--interaction=nonstopmode", "--halt-on-error",
         "--jobname=lualatex", "lualatex.ini"],
        cwd=RUNTIME, env=env, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    (RUNTIME / "format_build.out").write_text(result.stdout)
    print(result.stdout[-4500:])
    if result.returncode:
        raise SystemExit(result.returncode)
print("LuaLaTeX workspace runtime prepared.")
