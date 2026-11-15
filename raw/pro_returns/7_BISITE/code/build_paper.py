"""Reproducibly build the BISITE LuaLaTeX paper.

Uses the installed TeX distribution. On this workspace the user TeX tree is
empty, so we point TeX to its actual distribution and keep all generated
formats and font caches beside the sources. No network or privileged write
is needed. Individual TeX pass output is retained in code/build_*.out.txt.
"""
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".texcache"
CACHE.mkdir(exist_ok=True)
ENV = os.environ.copy()
DIST = Path("/usr/share/texlive/texmf-dist")
if DIST.exists():
    ENV["TEXMF"] = "{"+",".join(map(str,(CACHE/"texmf",DIST,Path("/usr/share/texmf"))))+"}"
for key, sub in (("TEXMFVAR","var"),("TEXMFCONFIG","config"),
                 ("TEXMFCACHE","cache")):
    path=CACHE/sub
    path.mkdir(exist_ok=True)
    ENV[key]=str(path)
ENV["TEXFORMATS"]=str(CACHE)+"//:"
ENV["TEXMFOUTPUT"]=str(ROOT)
# The minimal distribution also lacks the generated aggregate font map.
# Aggregate only the installed public maps used by this paper.
fontmap=CACHE/"texmf/fonts/map/pdftex/bisite/pdftex.map"
fontmap.parent.mkdir(parents=True,exist_ok=True)
map_sources=[
 DIST/"fonts/map/dvips/amsfonts/cm.map",
 DIST/"fonts/map/dvips/amsfonts/cmextra.map",
 DIST/"fonts/map/dvips/amsfonts/symbols.map",
 DIST/"fonts/map/dvips/amsfonts/latxfont.map",
 DIST/"fonts/map/dvips/rsfs/rsfs.map",
 Path("/usr/share/texmf/fonts/map/dvips/lm/lm.map")]
entries={}
for source in map_sources:
    if source.exists():
        for line in source.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith(("%","#")):
                entries.setdefault(line.split()[0],line)
fontmap.write_text("\n".join(entries.values())+"\n")

def run(name,args,cwd=ROOT):
    result=subprocess.run(args,cwd=cwd,env=ENV,text=True,
                          stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    path=ROOT/"code"/f"build_{name}.out.txt"
    path.write_text(result.stdout)
    print(f"{name}: exit={result.returncode}, log={path.relative_to(ROOT)}")
    if result.returncode:
        print(result.stdout[-9000:])
        raise SystemExit(result.returncode)

if not (CACHE/"lualatex.fmt").exists():
    run("format",["luahbtex","--ini","--interaction=nonstopmode",
        "--halt-on-error","--jobname=lualatex","lualatex.ini"],CACHE)
for passno in (1,2,3):
    run(f"lua{passno}",["lualatex","-interaction=nonstopmode",
        "-halt-on-error","-file-line-error","BISITE_paper.tex"])
    if passno==1:
        run("bibtex",["bibtex","BISITE_paper"])
print("PDF generated:",ROOT/"BISITE_paper.pdf")
