"""Install missing public LuaLaTeX runtime files into a local TeX tree.

The workspace's TeX installation omits texlive-luatex's font loader. This
script only fills the local cache from the official CTAN TeX Live archive.
It never writes the system installation. A normal full TeX Live installation
does not require this preparation. Download hashes are recorded below.
"""
from concurrent.futures import ThreadPoolExecutor
import hashlib
from pathlib import Path
import tarfile
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/".texcache"
TREE=CACHE/"texmf"
TREE.mkdir(parents=True,exist_ok=True)
PACKAGES=("lualibs","luaotfload","lua-uni-algos","luatexbase","apacite")

def fetch(package):
    url=f"https://mirrors.ctan.org/systems/texlive/tlnet/archive/{package}.tar.xz"
    dest=CACHE/f"{package}.tar.xz"
    if not dest.exists():
        with urllib.request.urlopen(url,timeout=40) as response:
            data=response.read()
        dest.write_bytes(data)
    data=dest.read_bytes()
    count=0
    with tarfile.open(dest) as archive:
        for member in archive.getmembers():
            name=member.name
            if not member.isfile() or name.startswith("tlpkg/"):
                continue
            if name.startswith("texmf-dist/"):
                name=name[len("texmf-dist/"):]
            target=(TREE/name).resolve()
            if not target.is_relative_to(TREE.resolve()):
                raise ValueError(f"Unsafe archive member: {name}")
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(archive.extractfile(member).read())
            count+=1
    return f"{package}: {count} files; {len(data)} bytes; SHA256 {hashlib.sha256(data).hexdigest()}; {url}"

with ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,PACKAGES))
text="\n".join(results)+"\n"
Path(__file__).with_suffix(".out.txt").write_text(text)
print(text,end="")
