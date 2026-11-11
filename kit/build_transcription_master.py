"""Write the master of the transcription, transcription/LesDerivateurs_transcription.tex, and one file per edition file,
transcription/<edition file>/<edition file>.tex, which sets that file's five-page parts in page order (through
transcription/derivateurs_parts.lua). With --pdf, also compile it with LuaLaTeX (three runs, for the contents and the
bookmarks) and print the page count and the LaTeX errors.
usage: python -I kit/build_transcription_master.py [--pdf]"""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent / "transcription"
NAME = "LesDerivateurs_transcription"

# The edition's files in order: folder (= the edition's PDF name), heading, title (as in the edition), version (footer
# of the edition file).
FILES = [
    ("dertbmt", "Table des matières", "", ""),
    ("Der-ChI-234", "Chapitre I", "Généralités sur les (pré)dérivateurs", "8 juillet 2001"),
    ("Der-ChII-234", "Chapitre II",
     "Cofinalité (à droite et à gauche) (préliminaire à la cofinalité cohomologique)", "8 juillet 2001"),
    ("Der-ChIII-567", "Chapitre III", "Hom externes dans les dérivateurs", "2 février 2002"),
    ("Der-ChIV-567", "Chapitre IV", "Diagrammes substantiels", "2 février 2002"),
    ("Der-ChV-234", "Chapitre V", "Catégories de chemins et localisation", "9 septembre 2001"),
    ("Der-ChVI-345", "Chapitre VI", "HOT", "9 novembre 2001"),
    ("Der-ChVII-456", "Chapitre VII", "Catégories de chemins (2)", "22 décembre 2001"),
    ("Der-ChVIII-567", "Chapitre VIII", "1-types d'homotopie relatifs : leur intégration\\,\\dots", "2 février 2002"),
    ("Der-ChIX-678", "Chapitre IX",
     "Retour sur les catégories de fractions $\\mathcal{M}W^{-1}$, comparaison avec Quillen", "12 mars 2002"),
    ("Der-ChX-789", "Chapitre X", "Comparaison de Cat avec $\\boldsymbol{\\Delta}^{\\wedge}$", "9 avril 2002"),
    ("Der-ChXI-890", "Chapitre XI", "Hot-fibrations, foncteurs propres et foncteurs lisses etc. (dans Cat)",
     "28 mai 2002"),
    ("Der-ChXIIa-012", "Chapitre XII, sections 1--4",
     "Caractérisation de $W_\\infty$. Foncteurs $W$-propres, $W$-lisses etc. Sommes amalgamées et carrés "
     "$W$-cocartésiens dans Cat", "7 décembre 2002"),
    ("Der-ChXIIb-012", "Chapitre XII, section 5", "", "7 décembre 2002"),
    ("Der-ChXIIc-30-03-03", "Chapitre XII, section 6", "", "30 mars 2003"),
    ("Der-ChXIIapp-19-06-03", "Appendice au chapitre XII", "", "20 juin 2003"),
    ("Der-ChXIII-25-01-04", "Chapitre XIII", "Catégories de modèles (1)", "25 janvier 2004"),
    ("Der-ChXIV-07-10-10", "Chapitre XIV", "Carrés h-cartésiens et h-cocartésiens", "7 octobre 2010"),
    ("Der-ChXV-05-11-10", "Chapitre XV", "Théorèmes de factorisation (Modèles (2))", "5 novembre 2010"),
    ("der-ch16", "Chapitre XVI", "Les localiseurs fondamentaux", "18 mars 2019"),
    ("der-ch17", "Chapitre XVII", "Catégories à fibrations et à cofibrations (Modèles (3))", "9 février 2019"),
    ("der-ch18", "Chapitre XVIII", "Catégories et ensembles accessibles", "17 décembre 2025"),
    ("der-ch19", "Chapitre XIX", "Modèles (4)", "11 février 2019"),
]
URL = "https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html"


def plain(s):
    """A title for the PDF bookmarks."""
    s = s.replace("$\\mathcal{M}W^{-1}$", "MW⁻¹").replace("$\\boldsymbol{\\Delta}^{\\wedge}$", "Δ^")
    s = s.replace("$W_\\infty$", "W∞").replace("\\,\\dots", "…").replace("--", "–")
    return s.replace("$", "")


PREAMBLE = r"""\documentclass[11pt,oneside]{article}
\usepackage{fontspec}
\usepackage[english,french]{babel}
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
\hypersetup{pdftitle={Les Dérivateurs: LaTeX transcription of the edition by Künzer, Malgoire and Maltsiniotis},
  pdfauthor={Alexandre Grothendieck},colorlinks=true,linkcolor=black,urlcolor=blue!45!black,pdfdisplaydoctitle=true}
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
{\Large Alexandre Grothendieck\par}
\vspace{2em}
{\Huge\bfseries Les Dérivateurs\par}
\vspace{2em}
{\large Transcription \LaTeX{} de l'édition de M.~Künzer, J.~Malgoire et G.~Maltsiniotis\par}
\vfill
\end{titlepage}
\begin{otherlanguage}{english}
\noindent\textbf{The text.} Alexander Grothendieck, \emph{Les Dérivateurs}, written from October 1990 through the
first half of 1991. Electronic edition by M.~Künzer, J.~Malgoire and G.~Maltsiniotis (Universités de Montpellier~II et
Paris~VII), \url{""" + URL + r"""}: a table of contents and twenty-two chapter files, 1,176 typeset pages; the version
of each file is given in the contents below and at the foot of its pages. The edition's own conventions are kept:
the manuscript's page numbers and the editors' notes in typewriter type between square brackets.

\medskip
\noindent\textbf{This transcription.} AI-transcribed (Claude Opus~5.5, Anthropic) from the edition's PDF files. The
source has one file for every five pages (\texttt{transcription/<edition file>/}). The edition's printed pages are
marked in the margin (p.~$n$), the manuscript's pages in brackets. Running heads and footers are kept as \TeX{}
comments in the source files; slips of the edition are kept as printed, flagged \texttt{\%~[sic]} in the source, and
doubtful readings are flagged \texttt{\%~??}; where the check of the companion resolved a doubt, the comment gives the
resolution. The text carries the corrections made in that check, for every part of the companion: the
transcription errors and resolved doubts listed in each part's table of corrections (five that the check against
the edition's pages overruled are not applied), and those other changes of the checked text that agree with the
edition's pages (the decisions are in \texttt{transcription/DECISIONS.md}).
These corrections are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); the corrections of macro definitions
and the changes the tables do not list were compared with the edition's pages by Claude Opus~5.5 (Anthropic).

\bigskip
\noindent\textbf{Rights}

\smallskip
\noindent The rights in the original work belong to its author or the author's representatives or heirs. Where we
hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the
public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we
do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will
take it down.
\end{otherlanguage}

\smallskip
\noindent Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Là
où nous détenons des droits, sur la transcription, la traduction, les corrections et la composition produites par IA,
ils sont dédiés au domaine public sous CC0 1.0. Cette édition est publiée à des fins pédagogiques et non lucratives, et
nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez
à sa publication ici, ouvrez une issue sur GitHub et nous la retirerons.
\clearpage
\tableofcontents
"""


def main():
    master = [PREAMBLE, FRONT]
    total = 0
    for folder, head, title, version in FILES:
        d = ROOT / folder
        parts = sorted(d.glob(f"{folder}_p*.tex"), key=lambda p: int(re.search(r"_p(\d+)-", p.name).group(1)))
        assert parts, folder
        total += len(parts)
        toc = head + (f" : {title}" if title else "") + (f" {{\\normalfont\\footnotesize (version du {version})}}"
                                                          if version else "")
        lines = [f"% {head}{' : ' + title if title else ''} -- edition file {folder}.pdf"
                 + (f", version du {version}" if version else ""),
                 f"\\derfile{{{folder}}}{{{toc}}}{{{plain(head + (' : ' + title if title else ''))}}}"]
        lines += [f"\\derpart{{{folder}/{p.name}}}" for p in parts]
        (d / f"{folder}.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
        master.append(f"\\input{{{folder}/{folder}}}\n")
    master.append("\\end{document}\n")
    (ROOT / f"{NAME}.tex").write_text("".join(master), encoding="utf-8")
    print(f"{NAME}.tex: {len(FILES)} edition files, {total} parts")
    if "--pdf" in sys.argv:
        for _ in range(3):
            subprocess.run(["lualatex", "-interaction=nonstopmode", f"{NAME}.tex"], cwd=ROOT,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log = (ROOT / f"{NAME}.log").read_text(encoding="utf-8", errors="replace")
        pages = re.search(r"Output written on .*?\((\d+) pages", log)
        errors = re.findall(r"^! .*", log, re.M)
        print(f"{NAME}.pdf: {pages.group(1) if pages else '?'} pages, {len(errors)} LaTeX errors")
        for e in errors[:40]:
            print("  ", e)


main()
