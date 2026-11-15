"""Run a command with the isolated genuine LuaLaTeX runtime environment."""
import subprocess
import sys
import json
import shutil
from setup_lualatex import PAPER, RUNTIME, environment, font_map

if not (RUNTIME / 'formats/lualatex.fmt').exists():
    raise SystemExit('Run python CATHOT/code/setup_lualatex.py first.')
font_map()
command = sys.argv[1:] or [sys.executable, str(PAPER / 'code/build.py')]
env = environment()
(PAPER / 'code/tex_environment.json').write_text(json.dumps(
    {k: v for k, v in env.items() if k.startswith('TEXMF') or k == 'TEXFORMATS'},
    indent=2) + '\n')
if not sys.argv[1:]:
    history = PAPER / 'code/build_history'
    history.mkdir(exist_ok=True)
    archive = history / f'prior_{len(list(history.iterdir())) + 1:02d}'
    archive.mkdir()
    for source in list((PAPER / 'code').glob('build_pass_*.out')) + [PAPER / 'CATHOT_paper.log']:
        if source.exists():
            shutil.copy2(source, archive / source.name)
print('WORKSPACE TEX COMMAND: ' + repr(command), flush=True)
raise SystemExit(subprocess.run(command, env=env).returncode)
