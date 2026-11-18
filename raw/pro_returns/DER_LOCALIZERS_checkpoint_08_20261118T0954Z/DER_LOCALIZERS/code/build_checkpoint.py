#!/usr/bin/env python3
"""Build this paper with retained per-pass logs in the available TeX runtime.

The sibling tex-support directory is a scratch-only repair for this container's
missing TeX indexes and Lua font-loader installation. A normal TeX installation
uses code/build_paper.sh directly. No third-party runtime files are redistributed.
"""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
build = root / 'build'
build.mkdir(exist_ok=True)
number = int(sys.argv[1])
env = os.environ.copy()
support = root.parent / 'tex-support' / 'texmf'
dist = Path('/usr/share/texlive/texmf-dist')
if (build / 'lualatex.fmt').exists():
    env['TEXFORMATS'] = str(build) + ':'
if support.exists():
    env['TEXMFHOME'] = str(support)
    env['TEXMF'] = '{' + str(support) + ',' + str(dist) + ',/usr/share/texmf}'
    env['TEXINPUTS'] = '.:' + str(dist / 'tex') + '//:'
    env['LUAINPUTS'] = str(support / 'tex') + '//:' + str(dist / 'tex') + '//:'
    env['TEXFONTMAPS'] = str(support / 'fonts/map') + '//:' + str(dist / 'fonts/map') + '//:'
    env['TFMFONTS'] = str(dist / 'fonts/tfm') + '//:/usr/share/texmf/fonts/tfm//:'
    env['VFFONTS'] = str(dist / 'fonts/vf') + '//:/usr/share/texmf/fonts/vf//:'
    env['T1FONTS'] = str(dist / 'fonts/type1') + '//:/usr/share/texmf/fonts/type1//:'
    env['OPENTYPEFONTS'] = str(dist / 'fonts/opentype') + '//:/usr/share/texmf/fonts/opentype//:'
    env['TTFONTS'] = str(dist / 'fonts/truetype') + '//:/usr/share/texmf/fonts/truetype//:'
    env['BIBINPUTS'] = '.:' + str(dist / 'bibtex/bib') + '//:'
    env['BSTINPUTS'] = '.:' + str(dist / 'bibtex/bst') + '//:'

latex = ['lualatex', '-interaction=nonstopmode', '-halt-on-error',
         '-output-directory=build', 'DER_LOCALIZERS_paper.tex']
steps = [(f'checkpoint{number}_pass3.stdout', latex),
         ('checkpoint_bibtex.stdout', ['bibtex', 'build/DER_LOCALIZERS_paper']),
         (f'checkpoint{number}_pass4.stdout', latex),
         (f'checkpoint{number}_pass5.stdout', latex)]
for name, command in steps:
    with (build / name).open('w') as output:
        result = subprocess.run(command, cwd=root, env=env,
                                stdout=output, stderr=subprocess.STDOUT)
    print(json.dumps({'log': name, 'exit_code': result.returncode}), flush=True)
    if result.returncode:
        print('\n'.join((build / name).read_text().splitlines()[-30:]), flush=True)
        raise SystemExit(result.returncode)

final_log = build / f'checkpoint{number}_pass5.stdout'
shutil.copy2(final_log, build / 'checkpoint_pass4.stdout')
shutil.copy2(build / 'DER_LOCALIZERS_paper.pdf', root / 'DER_LOCALIZERS_paper.pdf')
text = final_log.read_text()
print(json.dumps({'final_diagnostics': re.findall(
    r'^.*(?:Overfull|Missing character|Warning|undefined).*$', text, re.M),
    'underfull_boxes': len(re.findall(r'^Underfull', text, re.M))}, indent=2))
