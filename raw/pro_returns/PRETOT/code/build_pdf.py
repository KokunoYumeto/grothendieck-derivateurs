"""Build the paper with LuaLaTeX, from any working directory.

A normal TeX Live installation needs no special setup.  This workspace ships
TeX sources and Type 1 fonts but omits its generated file database, format, font
map, and OpenType loader.  The optional bootstrap below writes only under the
package's .build directory.  It builds a clearly named local Type 1 variant of
the installed LaTeX kernel, omitting its unavailable OpenType-loader startup;
the mathematical document and all other kernel startup code are unchanged.
No system installation, network fetch, or global configuration change occurs.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
import os
import subprocess
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'code' / 'outputs'
BUILD = ROOT / '.build'


def run(args, env, name, cwd=ROOT):
    p = subprocess.run(args, cwd=cwd, env=env, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, text=True)
    (OUT / name).write_text(p.stdout, encoding='utf-8')
    if p.returncode:
        print(p.stdout[-8000:])
        raise SystemExit(p.returncode)
    return p.stdout


def bootstrap(env):
    dist = Path('/usr/share/texlive/texmf-dist')
    debian = Path('/usr/share/texmf')
    if not (dist / 'tex/latex/base/latex.ltx').is_file():
        raise RuntimeError('Install a complete TeX Live distribution with LuaLaTeX.')
    tree = BUILD / 'texmf'
    kernel_dir = tree / 'tex/latex/pretot-type1'
    fmt_dir = tree / 'web2c/luahbtex'
    map_dir = tree / 'fonts/map/pdftex'
    for p in (kernel_dir, fmt_dir, map_dir, BUILD / 'cache', BUILD / 'config', BUILD / 'tmp'):
        p.mkdir(parents=True, exist_ok=True)
    (tree / 'texmf.cnf').write_text(
        f'TEXMF = {{{tree},/etc/texmf,{debian},{dist}}}\n'
        f'TEXMFVAR = {tree}\nTEXMFCONFIG = {BUILD / "config"}\n'
        f'TEXMFCACHE = {BUILD / "cache"}\n', encoding='utf-8')
    env['TEXMFCNF'] = str(tree) + ':'
    env['TMPDIR'] = str(BUILD / 'tmp')
    kernel = (dist / 'tex/latex/base/latex.ltx').read_text()
    marker = "  if xpcall(function ()%\n             require('luaotfload-main')%"
    assert marker in kernel, 'Installed kernel differs; use ordinary full TeX Live.'
    pos = kernel.index(marker)
    a = kernel.rfind('  \\directlua{%', 0, pos)
    b = kernel.index('\n  }%\n  \\let\\f@encoding\\encodingdefault', pos) + len('\n  }%')
    kernel = kernel[:a] + '  \\def\\encodingdefault{OT1}%' + kernel[b:]
    kernel = kernel.replace('  \\expandafter\\let\\csname ver@luaotfload.sty\\endcsname\\fmtversion\n', '')
    (kernel_dir / 'pretot-type1-latex.ltx').write_text(
        '% Local Type 1 variant for PRETOT; OpenType loader startup omitted.\n' + kernel)
    ini = (dist / 'tex/latex/tex-ini-files/lualatex.ini').read_text()
    ini = ini.replace('\\input latex.ltx', '\\input pretot-type1-latex.ltx')
    (kernel_dir / 'pretot-type1-lualatex.ini').write_text(ini)
    maps = [debian / 'fonts/map/dvips/lm/lm.map']
    maps += [dist / ('fonts/map/dvips/amsfonts/' + name + '.map')
             for name in ('cm', 'cmextra', 'symbols')]
    maps += [dist / 'fonts/map/dvips/rsfs/rsfs.map']
    (map_dir / 'pdftex.map').write_text('\n'.join(p.read_text() for p in maps))
    if not (fmt_dir / 'lualatex.fmt').is_file():
        run(['luahbtex', '--ini', '--interaction=nonstopmode', '--halt-on-error',
             '--jobname=lualatex', '--progname=lualatex',
             '--output-directory=' + str(fmt_dir), 'pretot-type1-lualatex.ini'],
            env, 'latex_format_bootstrap.out')
    return env


def main():
    OUT.mkdir(exist_ok=True)
    env = os.environ.copy()
    lookup = subprocess.run(['kpsewhich', 'lualatex.fmt'], env=env,
                            capture_output=True, text=True)
    used_bootstrap = not lookup.stdout.strip()
    if used_bootstrap:
        env = bootstrap(env)
    log = ''
    for n in range(1, 4):
        log = run(['lualatex', '-interaction=nonstopmode', '-halt-on-error',
                   'PRETOT_paper.tex'], env, f'latex_pass_{n}.out')
    (OUT / 'latex_final.out').write_text(log, encoding='utf-8')
    markers = ['undefined references', 'undefined citations', 'multiply defined',
               'Overfull \\hbox', 'LaTeX Error:', '! error:']
    bad = [m for m in markers if m.lower() in log.lower()]
    summary = (f'Engine: LuaLaTeX\nLocal Type 1 bootstrap: {used_bootstrap}\n'
               f'PDF: {ROOT / "PRETOT_paper.pdf"}\n'
               f'Checks: {"PASS" if not bad else "FAIL: " + ", ".join(bad)}\n')
    (OUT / 'build_pdf.out').write_text(summary)
    print(summary, end='')
    if bad:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
