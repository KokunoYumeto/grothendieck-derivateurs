#!/usr/bin/env python3
"""Retrieve the absent LuaTeX font packages into a private TeX tree.

This is environment repair only; nothing is installed globally. Package archives
are obtained from a CTAN mirror and SHA-256 digests are printed for provenance.
"""
from pathlib import Path
import hashlib
import tarfile
import urllib.request

root=Path(__file__).resolve().parents[1]
destination=root/'build/texmf'
archive_dir=root/'build/tex-packages'
destination.mkdir(exist_ok=True)
archive_dir.mkdir(exist_ok=True)
base='https://mirror.apps.cam.ac.uk/pub/tex-archive/systems/texlive/tlnet/archive/'
for name in ['luaotfload','lualibs','luatexbase','lua-uni-algos']:
    archive=archive_dir/(name+'.tar.xz')
    if not archive.exists():
        with urllib.request.urlopen(base+archive.name,timeout=45) as response:
            archive.write_bytes(response.read())
    print(name,archive.stat().st_size,hashlib.sha256(archive.read_bytes()).hexdigest(),flush=True)
    with tarfile.open(archive,'r:xz') as t:
        for member in t.getmembers():
            path=(destination/member.name).resolve()
            if not path.is_relative_to(destination.resolve()):
                raise ValueError(member.name)
        t.extractall(destination,filter='data')
print('Workspace LuaTeX font dependencies ready.',flush=True)
