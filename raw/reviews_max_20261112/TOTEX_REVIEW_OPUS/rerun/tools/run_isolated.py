"""Run one copied program under python -I: put only the program's own folder on sys.path,
give it only its own name and the given flags in argv. Used for the TOTEX review reruns."""
import runpy, sys, time
from pathlib import Path
script = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(script.parent))
sys.argv = [str(script)] + sys.argv[2:]
t0 = time.time()
runpy.run_path(str(script), run_name='__main__')
sys.stderr.write(f"[run_isolated] {script.name} {' '.join(sys.argv[1:])} elapsed {time.time()-t0:.1f}s\n")
