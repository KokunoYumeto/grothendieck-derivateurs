"""Build the English book from the English units, as the transcription's book is built from the French ones.

Writes, in translation/ (the layout of the repository's transcription/):
  derivateurs_parts.lua                the transcription's loader, byte for byte (each unit's preamble applied in a
                                       group, its body set; package lines left to the master)
  <folder>/<folder>.tex                per edition file: its heading in the contents and its units in page order
  LesDerivateurs_translation.tex       the master: the transcription master's preamble with English as the main
                                       language, an English front matter, the edition files in order
and with --pdf compiles it with LuaLaTeX (three runs, --no-shell-escape) and prints the page count and the LaTeX errors.
Before compiling, every unit's body is checked again for control sequences that its French does not have and that
could act outside the page (check_units.DANGER); if one is found, nothing is compiled.
Adapted from kit/build_transcription_master.py of the repository (derivateurs_publish_20261111/repo).
usage: python -I -B build.py [--pdf]
"""
import collections
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402
import check_units as K  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
OUT = os.path.join(T.ROOT, "translation")
NAME = "LesDerivateurs_translation"
URL = "https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html"

PREAMBLE = r"""\documentclass[11pt,oneside]{article}
\usepackage{fontspec}
\usepackage[french,english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathrsfs}
\usepackage{tikz-cd}
\usepackage{enumitem}
\usepackage{array}
\usepackage{ragged2e}
\usepackage{marginnote}
\usepackage{lmodern}
\usetikzlibrary{babel,arrows.meta,decorations.markings,decorations.pathreplacing}
\usepackage[a4paper,left=25mm,right=32mm,top=25mm,bottom=25mm,marginparwidth=24mm,marginparsep=4mm]{geometry}
\usepackage{luacode}
\usepackage{xurl}
\usepackage[hyperfootnotes=false,bookmarksopen=true,bookmarksopenlevel=0]{hyperref}
\hypersetup{pdftitle={Les Dérivateurs: English translation of the transcription of the edition by Künzer, Malgoire and Maltsiniotis},
  pdfauthor={Alexander Grothendieck},colorlinks=true,linkcolor=black,urlcolor=blue!45!black,pdfdisplaydoctitle=true}
\setlength{\emergencystretch}{2em}
\makeatletter
\newcommand{\derleqno}{\tagsleft@true}
\renewcommand*{\@pnumwidth}{2.4em}
\renewcommand*{\@tocrmarg}{3.4em}
\makeatother
\newcommand{\derpartstart}[1]{\typeout{[part #1]}}
\directlua{derparts = dofile("derivateurs_parts.lua")}
\newcommand{\derpart}[1]{\directlua{derparts.part("\luaescapestring{#1}")}}
\newcommand{\derfile}[3]{\clearpage\setcounter{footnote}{0}\phantomsection
  \addcontentsline{toc}{section}{#2}\pdfbookmark[0]{#3}{#1}}
"""

FRONT = r"""\begin{document}
\pagestyle{plain}
\begin{titlepage}
\centering
\vspace*{0.22\textheight}
{\Large Alexander Grothendieck\par}
\vspace{2em}
{\Huge\bfseries Les Dérivateurs\par}
\vspace{1em}
{\Large Derivators\par}
\vspace{2em}
{\large English translation of the transcription of the edition by M.~Künzer, J.~Malgoire and G.~Maltsiniotis\par}
\vfill
\end{titlepage}
\noindent\textbf{The text.} Alexander Grothendieck, \emph{Les Dérivateurs}, written from October 1990 through the
first half of 1991. Electronic edition by M.~Künzer, J.~Malgoire and G.~Maltsiniotis (Universités de Montpellier~II et
Paris~VII), \url{""" + URL + r"""}: a table of contents and twenty-two chapter files, 1,176 typeset pages; the version
of each file is given in the contents below and at the foot of its pages. The deciphering of the manuscript, its edition
and the editors' notes are theirs. The edition's own conventions are kept: the manuscript's page numbers and the
editors' notes in typewriter type between square brackets.

\medskip
\noindent\textbf{This translation.} AI-translated by GPT-6.1 Sol (OpenAI; Responses API, reasoning effort max, Flex
tier) from our LaTeX transcription of the edition (release v2026-11-11b of
\url{https://github.com/KokunoYumeto/grothendieck-derivateurs}), which is AI-transcribed (Claude Opus~5.5, Anthropic)
and carries the corrections of its critical companion (AI-produced by GPT-6 Astra, OpenAI, ChatGPT Pro mode; checked
by Claude Opus~5.5). The translation was made five pages at a time, with a glossary of his terms whose English follows
his own English of \emph{Pursuing Stacks} where it has one; every five pages were checked by script against the French
(formulas identical, page anchors and labels in place, no French left, the glossary's terms used). Formulas are as in
the transcription, and so is the notation, which differs between chapters of the edition; only the words set in text
inside formulas and diagrams are translated (``def'' over the equality sign, for ``déf''). The edition's printed pages
are marked in the margin (p.~$n$), the manuscript's pages in brackets; running heads and footers and the transcription's
notes (\texttt{\%~[sic]}, \texttt{\%~??}) are kept, in French, as \TeX{} comments in the source files. The
translation, the checks and the build were run by Claude Opus~5.5 (Anthropic). The headings of the contents and this
front matter are by Claude Opus~5.5.

\bigskip
\noindent\textbf{Rights}

\smallskip
\noindent The rights in the original work belong to its author or the author's representatives or heirs. Where we
hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the
public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we
do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will
take it down.
\clearpage
\tableofcontents
"""


def plain(s):
    s = s.replace("$\\mathcal{M}W^{-1}$", "MW⁻¹").replace("$\\boldsymbol{\\Delta}^{\\wedge}$", "Δ^")
    s = s.replace("$W_\\infty$", "W∞").replace("\\,\\dots", "…").replace("--", "–")
    return s.replace("$", "")


def safety():
    """Control sequences of the English bodies that the French does not have and that could act outside the page."""
    bad = []
    for u in T.units():
        p = os.path.join(OUT, u["folder"], u["id"] + ".tex")
        if not os.path.exists(p):
            continue
        en = T.body_text(T.read(p))
        fr = T.body_text(T.read(os.path.join(T.ROOT, "source", u["id"] + ".tex")))
        (csf, envf), (cse, enve) = K.control_sequences(fr), K.control_sequences(en)
        d = sorted((set(cse) - set(csf)) & K.DANGER) + sorted((set(enve) - set(envf)) & K.DANGER_ENV)
        # comments are not set; but a body must not end a comment's line early or hide a macro in one
        if d:
            bad.append((u["id"], d))
    return bad


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(T.SRC, "derivateurs_parts.lua"), os.path.join(OUT, "derivateurs_parts.lua"))
    master = [PREAMBLE, FRONT]
    total, missing = 0, []
    for folder, phrase, head, title in T.FILES:
        d = os.path.join(OUT, folder)
        units = [u for u in T.units() if u["folder"] == folder]
        have = [u for u in units if os.path.exists(os.path.join(d, u["id"] + ".tex"))]
        missing += [u["id"] for u in units if u not in have]
        if not have:
            continue
        total += len(have)
        version = T.VERSIONS.get(folder, "")
        toc = head + (": " + title if title else "") + (
            " {\\normalfont\\footnotesize (version of %s)}" % version if version else "")
        lines = ["%% %s%s -- edition file %s.pdf%s" % (head, ": " + title if title else "", folder,
                                                        ", version of " + version if version else ""),
                 "\\derfile{%s}{%s}{%s}" % (folder, toc, plain(head + (": " + title if title else "")))]
        lines += ["\\derpart{%s/%s.tex}" % (folder, u["id"]) for u in have]
        T.write(os.path.join(d, folder + ".tex"), "\n".join(lines) + "\n")
        master.append("\\input{%s/%s}\n" % (folder, folder))
    master.append("\\end{document}\n")
    T.write(os.path.join(OUT, NAME + ".tex"), "".join(master))
    print("%s.tex: %d units%s" % (NAME, total, ("; not yet translated: %d" % len(missing)) if missing else ""))
    if "--pdf" in sys.argv:
        bad = safety()
        if bad:
            for u, d in bad:
                print("  NOT COMPILED: %s has %s" % (u, d))
            raise SystemExit("unsafe control sequences: not compiled")
        for k in range(3):
            subprocess.run(["lualatex", "--no-shell-escape", "-interaction=nonstopmode", NAME + ".tex"], cwd=OUT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log = T.read(os.path.join(OUT, NAME + ".log")) if os.path.exists(os.path.join(OUT, NAME + ".log")) else ""
        pages = re.search(r"Output written on .*?\((\d+) pages", log)
        errors = re.findall(r"^! .*", log, re.M)
        where = collections.Counter()
        part = None
        for line in log.splitlines():
            m = re.match(r"\[part (.*?)\]", line)
            if m:
                part = m.group(1)
            if line.startswith("! "):
                where[part] += 1
        print("%s.pdf: %s pages, %d LaTeX errors" % (NAME, pages.group(1) if pages else "?", len(errors)))
        for p, n in where.most_common():
            print("   %d in %s" % (n, p))
        for e in errors[:40]:
            print("  ", e)


if __name__ == "__main__":
    main()
