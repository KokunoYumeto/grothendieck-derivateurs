"""The initial standalone literature-fragment compilation attempt.

This is a toolchain check, not a mathematical certificate. The installed
XeLaTeX had no format; the recovery build later used a separate local
LuaLaTeX bootstrap. Run from any directory.
"""
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[1]
source = (root / 'TOTEX2_paper.tex').read_text()
preamble = source.split(r'\begin{document}', 1)[0]
body = r'''\begin{document}
\section{Manuscript and literature fragments}
\input{work/manuscript_audit.tex}
\input{work/ramsey_exact.tex}
\input{work/source_audit.tex}
\bibliographystyle{plainnat}
\bibliography{work/literature_references}
\end{document}
'''
(root / 'work/literature_harness.tex').write_text(preamble + body)
commands = [
    ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
     '-output-directory=work', 'work/literature_harness.tex'],
    ['bibtex', 'work/literature_harness'],
    ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
     '-output-directory=work', 'work/literature_harness.tex'],
    ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
     '-output-directory=work', 'work/literature_harness.tex'],
]
for command in commands:
    result = subprocess.run(command, cwd=root, text=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    print(command[0], result.returncode)
    if result.returncode:
        print(result.stdout[-5000:])
        break
else:
    for line in (root / 'work/literature_harness.log').read_text().splitlines():
        if 'Warning' in line or 'Overfull' in line:
            print(line)
