"""Compile with LuaLaTeX; retain an auditable log and a small status record.

On a normal TeX installation, latexmk is used without environment changes.
For the supplied Debian runtime, a missing format/index can be rebuilt in
the adjacent scratch cache without changing the system TeX installation.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT.parent / 'texcache'


def main():
    env = os.environ.copy()
    fallback = subprocess.run(['kpsewhich', 'lualatex.fmt'], capture_output=True).returncode != 0
    logpath = Path(__file__).with_name('latex_build.log')
    with logpath.open('w') as log:
        if fallback:
            CACHE.mkdir(exist_ok=True)
            env.update(TEXMF='{.,/usr/share/texlive/texmf-dist,/usr/share/texmf}',
                       TEXMFVAR=str(CACHE), TEXMFCONFIG=str(CACHE / 'config'),
                       TEXMFCACHE=str(CACHE), TEXFORMATS=str(CACHE) + '//:')
            if not (CACHE / 'lualatex.fmt').exists():
                result = subprocess.run(['luahbtex', '--ini', '--jobname=lualatex',
                                         '--progname=lualatex', 'lualatex.ini'],
                                        cwd=CACHE, env=env, stdout=log, stderr=subprocess.STDOUT)
                if result.returncode:
                    raise RuntimeError('Local LuaLaTeX format initialization failed; see latex_build.log')
        cmd = ['latexmk', '-g', '-lualatex', '-interaction=nonstopmode', '-halt-on-error', 'RESIDUE_paper.tex']
        result = subprocess.run(cmd, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
    rawlog = (ROOT / 'RESIDUE_paper.log').read_text(errors='replace') if (ROOT / 'RESIDUE_paper.log').exists() else ''
    status = {'command': cmd, 'returncode': result.returncode,
              'local_format_fallback_used': fallback,
              'pdf_exists': (ROOT / 'RESIDUE_paper.pdf').exists(),
              'undefined_control_sequence': 'Undefined control sequence' in rawlog,
              'undefined_citations': 'undefined citations' in rawlog or 'Citation `' in rawlog,
              'overfull_boxes': rawlog.count('Overfull \\hbox') + rawlog.count('Overfull \\vbox'),
              'underfull_boxes': rawlog.count('Underfull \\hbox') + rawlog.count('Underfull \\vbox'),
              'missing_characters': rawlog.count('Missing character:'),
              'optional_font_loader_fallback_notice': 'Error in luaotfload: reverting to OT1' in rawlog,
              'tex_error_lines': [line for line in rawlog.splitlines() if line.startswith('!')]}
    Path(__file__).with_name('pdf_build.json').write_text(json.dumps(status, indent=2) + '\n')
    print(json.dumps(status, indent=2))
    if result.returncode:
        print('\n'.join(logpath.read_text(errors='replace').splitlines()[-50:]))
    sys.exit(result.returncode)


if __name__ == '__main__':
    main()
