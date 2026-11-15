#!/usr/bin/env python3
"""Build the paper with LuaLaTeX/BibTeX, preserving command output.

On an ordinary TeX Live installation this uses the normal configuration.
The optional --local-tex-runtime reconstructs the missing format/database
configuration of the supplied container inside the writable package folder;
it does not install packages or modify the system TeX tree.
"""
from pathlib import Path
import argparse
import os
import subprocess

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--local-tex-runtime', action='store_true')
args = parser.parse_args()
env = dict(os.environ)
audit = root / 'audit'
audit.mkdir(exist_ok=True)

def run(command, name, cwd=root):
    with (audit/name).open('w') as out:
        out.write('COMMAND: '+' '.join(map(str,command))+'\n')
        out.flush()
        done = subprocess.run(list(map(str,command)), cwd=cwd, env=env,
                              stdout=out, stderr=subprocess.STDOUT)
    if done.returncode:
        print((audit/name).read_text()[-5000:])
        raise SystemExit(done.returncode)
    print(name, 'PASS', flush=True)

if args.local_tex_runtime:
    runtime = root / '.build' / 'tex-runtime'
    runtime.mkdir(parents=True, exist_ok=True)
    trees = [Path('/usr/share/texlive/texmf-dist'), Path('/usr/share/texmf')]
    env.update(TEXMF='{'+','.join(map(str,[runtime]+trees))+'}',
               TEXMFVAR=str(runtime), TEXMFCONFIG=str(runtime),
               TEXMFCACHE=str(runtime), TEXFORMATS=str(runtime)+'//:')
    # The container supplies the LuaHBTeX engine and Type 1 fonts, but not
    # luaotfload. This paper deliberately uses fontenc/lmodern Type 1 fonts.
    # Configure a local LaTeX format to select its documented OT1 fallback
    # directly, avoiding an attempted load of the absent OpenType loader.
    # No system file is edited; a normal installation needs no such option.
    base = trees[0]/'tex/latex/base/latex.ltx'
    local_base = runtime/'tex/latex/base/latex.ltx'
    source = base.read_text()
    start = source.index('  \\directlua{%\n  if xpcall(function ()%')
    end = source.index('  \\let\\f@encoding\\encodingdefault', start)
    local_source = source[:start]+'  \\def\\encodingdefault{OT1}%\n'+source[end:]
    local_base.parent.mkdir(parents=True,exist_ok=True)
    changed = not local_base.exists() or local_base.read_text() != local_source
    if changed:
        local_base.write_text(local_source)
    maps = list((trees[0]/'fonts/map/dvips/amsfonts').glob('*.map'))
    maps += [trees[0]/'fonts/map/dvips/rsfs/rsfs.map',
             trees[1]/'fonts/map/dvips/lm/lm.map']
    dest = runtime/'fonts/map/pdftex/updmap/pdftex.map'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text('\n'.join(p.read_text() for p in maps if p.is_file()))
    if changed or not (runtime/'lualatex.fmt').is_file():
        run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
             '--jobname=lualatex','--progname=lualatex',
             '--output-directory='+str(runtime),'lualatex.ini'],
             'format_initialization.txt')

run(['lualatex','-interaction=nonstopmode','-halt-on-error','PATHS_paper.tex'], 'lualatex_pass1.txt')
run(['bibtex','PATHS_paper'], 'bibtex.txt')
run(['lualatex','-interaction=nonstopmode','-halt-on-error','PATHS_paper.tex'], 'lualatex_pass2.txt')
run(['lualatex','-interaction=nonstopmode','-halt-on-error','PATHS_paper.tex'], 'lualatex_pass3.txt')
print('Built', root/'PATHS_paper.pdf', flush=True)
