"""Run one program of the PRETOT return from the copied code folder.

Usage (always with the interpreter in isolated mode):
    python -I run_isolated.py <copied_code_dir> <script.py> <log_dir>

Isolated mode puts neither the current directory nor this script's directory on
sys.path.  Only <copied_code_dir> is APPENDED to sys.path (after the standard
library), because appendix_gluing_check.py imports path_checks from its own folder.
The program runs as __main__ via runpy; stdout and stderr go to
<log_dir>/<script>.stdout and .stderr; exit status and wall time to <script>.status.
Written by Claude Opus 5.5 for the PRETOT review, 12 Nov 2026.
"""
import contextlib
import io
import runpy
import sys
import time
import traceback
from pathlib import Path


def main():
    code_dir = Path(sys.argv[1]).resolve()
    script = code_dir / sys.argv[2]
    log_dir = Path(sys.argv[3]).resolve()
    log_dir.mkdir(parents=True, exist_ok=True)
    assert script.is_file() and script.parent == code_dir
    sys.path.append(str(code_dir))
    # the program sees only its own name in argv (two programs read an optional argv[1])
    sys.argv = [str(script)]
    out, err = io.StringIO(), io.StringIO()
    status = 0
    t0 = time.perf_counter()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            runpy.run_path(str(script), run_name='__main__')
        except SystemExit as e:
            status = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
        except BaseException:
            traceback.print_exc()
            status = 1
    elapsed = time.perf_counter() - t0
    stem = script.stem
    (log_dir / f'{stem}.stdout').write_text(out.getvalue(), encoding='utf-8')
    (log_dir / f'{stem}.stderr').write_text(err.getvalue(), encoding='utf-8')
    (log_dir / f'{stem}.status').write_text(
        f'exit={status}\nseconds={elapsed:.2f}\npython={sys.version.split()[0]}\n', encoding='utf-8')
    print(f'{stem}: exit={status} seconds={elapsed:.2f}')
    sys.exit(status)


if __name__ == '__main__':
    main()
