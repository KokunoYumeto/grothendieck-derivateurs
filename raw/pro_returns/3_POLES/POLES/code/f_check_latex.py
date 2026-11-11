"""Compile Part F alone using the shared preamble; preserve all compiler output."""
from pathlib import Path
import subprocess
from f_tex_runtime import tex_environment

root=Path(__file__).resolve().parents[1]
environment=tex_environment()
main=(root/'POLES_paper.tex').read_text()
preamble=main.split(r'\begin{document}',1)[0]
bibliography='POLES_references' if (root/'POLES_references.bib').exists() else 'research/F_references'
wrapper=preamble+r'''
\begin{document}
\setcounter{section}{5}
\input{sections/F.tex}
\bibliographystyle{apalike}
\bibliography{BIBLIOGRAPHY_PLACEHOLDER}
\end{document}
'''
wrapper=wrapper.replace('BIBLIOGRAPHY_PLACEHOLDER',bibliography)
(root/'verification/F_check.tex').write_text(wrapper)
commands=[
 ['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=verification','verification/F_check.tex'],
 ['bibtex','verification/F_check'],
 ['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=verification','verification/F_check.tex'],
 ['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=verification','verification/F_check.tex'],
]
for command in commands:
    print('COMMAND:', ' '.join(command), flush=True)
    run=subprocess.run(command,cwd=root,env=environment,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(run.stdout,flush=True)
    if run.returncode:
        raise SystemExit(run.returncode)
print('Part F compiled successfully.')
