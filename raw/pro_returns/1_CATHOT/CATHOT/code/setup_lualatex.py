"""Bootstrap this incomplete TeX Live installation without system writes.

Uses the installed LuaHBTeX engine, restores disk lookup in the installed TeX
trees, adds missing CTAN runtime packages to a workspace TEXMF, and generates
the genuine lualatex format.  All downloads and subprocess outputs are logged.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tarfile
import urllib.request

PAPER = Path(__file__).resolve().parents[1]
RUNTIME = PAPER.parent / 'tex_runtime'
for item in ['home', 'var', 'config', 'cache', 'downloads', 'formats']:
    (RUNTIME / item).mkdir(parents=True, exist_ok=True)


def environment():
    env = os.environ.copy()
    env.update({
        'TEXMFHOME': str(RUNTIME / 'home'),
        'TEXMFVAR': str(RUNTIME / 'var'),
        'TEXMFCONFIG': str(RUNTIME / 'config'),
        'TEXMFCACHE': str(RUNTIME / 'cache'),
        # Kpathsea's openout_any=p permits absolute cache writes beneath this
        # designated output root.  Keep that protection enabled.
        'TEXMFOUTPUT': str(RUNTIME),
        'TEXMF': '{' + ','.join([
            str(RUNTIME / 'home'), str(RUNTIME / 'var'),
            str(RUNTIME / 'config'), '/usr/share/texlive/texmf-dist',
            '/usr/share/texmf', '/etc/texmf']) + '}',
        'TEXFORMATS': str(RUNTIME / 'formats') + '//:',
    })
    return env


def run(args, name, cwd=PAPER, fail=True):
    print('COMMAND ' + repr(args), flush=True)
    p = subprocess.run(args, cwd=cwd, env=environment(), text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (PAPER / 'code' / name).write_text(p.stdout)
    print(f'  exit={p.returncode}; saved {name}; lines={len(p.stdout.splitlines())}', flush=True)
    if p.returncode and fail:
        print(p.stdout[-9000:], flush=True)
        raise SystemExit(p.returncode)
    return p


def lookup(filename):
    p = subprocess.run(['kpsewhich', filename], env=environment(), text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.stdout.strip()


def package(name, filename):
    existing = lookup(filename)
    if existing:
        print(f'FOUND {filename}: {existing}', flush=True)
        return
    archive = RUNTIME / 'downloads' / f'{name}.tar.xz'
    sources = [
        f'https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/{name}.tar.xz',
        f'https://mirrors.ctan.org/systems/texlive/tlnet/archive/{name}.tar.xz',
        f'https://ftp.fau.de/ctan/systems/texlive/tlnet/archive/{name}.tar.xz',
    ]
    for url in sources:
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read()
                final_url = response.url
            archive.write_bytes(data)
            print(f'DOWNLOAD {name}: {final_url}; bytes={len(data)}; sha256={hashlib.sha256(data).hexdigest()}', flush=True)
            break
        except Exception as exc:
            print(f'DOWNLOAD FAILED {url}: {exc}', flush=True)
    else:
        raise RuntimeError(f'Could not download package {name}')
    count = 0
    with tarfile.open(archive, 'r:xz') as tf:
        for member in tf:
            rel = Path(member.name)
            if rel.is_absolute() or '..' in rel.parts:
                raise ValueError(f'Unsafe archive member: {member.name}')
            if rel.parts and rel.parts[0] == 'texmf-dist':
                rel = Path(*rel.parts[1:])
            target = RUNTIME / 'home' / rel
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                target.parent.mkdir(parents=True, exist_ok=True)
                with tf.extractfile(member) as source:
                    target.write_bytes(source.read())
                count += 1
            else:
                raise ValueError(f'Nonregular archive member: {member.name}')
    print(f'  extracted {count} files; lookup {filename}: {lookup(filename)}', flush=True)


def font_map():
    """Supply the missing generated PDF map using installed CM/AMS/LM maps."""
    sources = [
        Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts') / n
        for n in ['cm.map', 'cmextra.map', 'symbols.map', 'euler.map', 'latxfont.map']
    ] + [Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
    lines, seen = [], set()
    for source in sources:
        for line in source.read_text().splitlines():
            if not line.strip() or line.lstrip().startswith('%'):
                continue
            key = line.split()[0]
            if key not in seen:
                seen.add(key)
                lines.append(line)
    destination = RUNTIME / 'home/fonts/map/pdftex/local/pdftex.map'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text('\n'.join(lines) + '\n')
    print(f'FONT MAP: {destination}; {len(lines)} installed CM/AMS/LM font entries', flush=True)


def main():
    print('Installed engine: /usr/bin/lualatex', flush=True)
    run(['/usr/bin/lualatex', '--version'], 'tex_engine_version.out')
    for name, filename in [
        ('lualibs', 'lualibs.lua'),
        ('luaotfload', 'luaotfload-main.lua'),
        ('luatexbase', 'luatexbase.sty'),
        ('lua-uni-algos', 'lua-uni-normalize.lua'),
        ('apacite', 'apacite.bst'),
    ]:
        package(name, filename)
    env = environment()
    keys = ['TEXMFHOME', 'TEXMFVAR', 'TEXMFCONFIG', 'TEXMFCACHE', 'TEXMFOUTPUT', 'TEXMF', 'TEXFORMATS']
    (PAPER / 'code' / 'tex_environment.json').write_text(
        json.dumps({k: env[k] for k in keys}, indent=2) + '\n')
    font_map()
    run(['/usr/bin/lualatex', '--ini', '--jobname=lualatex',
         '--progname=lualatex', '-interaction=nonstopmode',
         '-halt-on-error', 'lualatex.ini'], 'tex_format_build.out',
        cwd=RUNTIME / 'formats')
    print(f'FORMAT: {RUNTIME / "formats" / "lualatex.fmt"}', flush=True)
    print('Run builds with the environment() mapping from this module.', flush=True)


if __name__ == '__main__':
    main()
