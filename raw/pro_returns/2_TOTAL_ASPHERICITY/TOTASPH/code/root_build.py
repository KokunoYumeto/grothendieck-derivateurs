#!/usr/bin/env python3
"""Build with LuaLaTeX, using workspace-local formats/caches if needed.

The supplied environment has TeX Live files but dangling system database
symlinks. Removing the database-only !! prefixes lets kpathsea read the
installed files; this changes no global configuration or permission.
On a normal TeX Live installation, latexmk -lualatex TOTASPH_paper.tex also works.
"""
from pathlib import Path
import os
import shutil
import subprocess

root=Path(__file__).resolve().parents[1]
build=root/'build'
build.mkdir(exist_ok=True)
env=dict(os.environ)
trees=[str(build/'texmf/texmf-dist'),str(build/'texmf'),'/usr/share/texlive/texmf-dist','/usr/share/texmf']
env['TEXMF']='{'+','.join(trees)+'}'
env['TEXMFVAR']=str(build/'texmf-var')
env['TEXMFCONFIG']=str(build/'texmf-config')
env['TEXMFCACHE']='build/texmf-cache'
env['TEXFORMATS']=str(build)+':'+env.get('TEXFORMATS','')
for k in ['TEXMFVAR','TEXMFCONFIG']:
    Path(env[k]).mkdir(exist_ok=True)
(build/'texmf-cache').mkdir(exist_ok=True)
# The host has font files but no generated pdftex.map. Supply a private map.
map_dir=build/'texmf/fonts/map/pdftex/local'
map_dir.mkdir(parents=True,exist_ok=True)
map_sources=[Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts')/n
             for n in ['cm.map','cmextra.map','symbols.map','euler.map','latxfont.map']]
map_sources += [Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
(map_dir/'pdftex.map').write_text('\n'.join(p.read_text() for p in map_sources if p.exists()))
format_file=build/'lualatex.fmt'
if not format_file.exists():
    ini=subprocess.check_output(['kpsewhich','lualatex.ini'],env=env,text=True).strip()
    args=['luahbtex','--ini','--jobname=lualatex','--interaction=nonstopmode',
          '--halt-on-error',f'--output-directory={build}',ini]
    with (build/'format-build.out.txt').open('w') as log:
        completed=subprocess.run(args,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
    print('LuaLaTeX format build exit:',completed.returncode,flush=True)
    completed.check_returncode()
with (build/'compile.out.txt').open('w') as log:
    args=['latexmk','-g','-lualatex','-interaction=nonstopmode','-halt-on-error',
          '-outdir=build','TOTASPH_paper.tex']
    completed=subprocess.run(args,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
print('LuaLaTeX paper build exit:',completed.returncode,flush=True)
completed.check_returncode()
shutil.copy2(build/'TOTASPH_paper.pdf',root/'TOTASPH_paper.pdf')
shutil.copy2(build/'TOTASPH_paper.log',root/'code/root_compile.log')
if (build/'TOTASPH_paper.blg').exists():
    shutil.copy2(build/'TOTASPH_paper.blg',root/'code/root_bibliography.log')
print('Output:',root/'TOTASPH_paper.pdf',flush=True)
