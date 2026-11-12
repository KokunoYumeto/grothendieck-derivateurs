"""Build the reader: the 243 English units set as one book (12 Nov 2026).

Writes reader/LesDerivateurs_English.tex, one self-contained LaTeX file, and with --pdf compiles it with LuaLaTeX
(three runs, --no-shell-escape) and prints the page count, the LaTeX errors and the undefined references.

What the reader changes against the book of 11 Nov (scripts/build.py, which sets the units one after the other):
  - front matter: a title page, a note on the text, on how to read it and on how this book was made, the rights
    statement, and a table of contents by Grothendieck's chapters (chapter XII with its four edition files);
  - each chapter opens with a heading and has running heads; the edition file's own title page (which only repeats
    the title) is not set, and its editors' note is set under the heading, translated in full except the sentence
    that gives the editors' e-mail address;
  - the edition's table of contents (dertbmt) is set as a chapter of its own, without its title block;
  - the seams between units disappear: where a paragraph runs on from one five-page unit into the next, it is set as
    one paragraph (classify() says when);
  - the transcription's page breaks inside the text (\\clearpage, \\newpage, set where an edition page ended) end the
    paragraph but do not break the page;
  - one paragraph layout for the whole book: the \\parindent and \\parskip settings of single units' preambles are not
    applied;
  - the three LaTeX errors of the book of 11 Nov do not occur: \\mathllap is defined (Der-ChXIV-07-10-10_p011-011);
    an \\AtBeginDocument block of a preamble is set as its content (Der-ChXV-05-11-10_p031-035 and three more); the
    diagram's baseline is fixed in the unit itself (checks/FIXES.jsonl);
  - the margin marks: "p. n" where page n of the edition begins (grey), "[page n]" where page n of the manuscript
    begins (typewriter), as the units have them; the anchors of unnumbered pages print nothing;
  - a tikz-cd diagram wider than the line or taller than the page is scaled down to fit (adjustbox, through the
    environment's hooks); the others are set at their size;
  - the one e-mail address in the text (chapter V, where the editors ask a reader to write to G. Maltsiniotis) is
    replaced by "[e-mail address removed]", as in the units published in en/.
Everything else is the units' own: each unit's preamble definitions are applied in a group of their own (as the
transcription's loader does), and its body is set as it is.
usage: python -I -B build_reader.py [--pdf] [--show]
  --show: print the chapter title pages found, the editors' notes as set and the seams joined, and stop
"""
import collections
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
OUT = os.path.join(T.ROOT, "reader")
NAME = "LesDerivateurs_English"
EDITION_URL = "https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html"
REPO_URL = "https://github.com/KokunoYumeto/grothendieck-derivateurs"
DATE = "12 November 2026"

# Per edition file: heading line, title (from the English title page of the edition file), running head, kind
# ("front", "chapter" or "part": a later file of chapter XII), TOC text (None: the title).
W = "\\texorpdfstring{$W$}{W}"
CHAPTERS = {
    "dertbmt": ("", "The edition's table of contents", "The edition's table of contents", "front", None),
    "Der-ChI-234": ("Chapter I", "Generalities on (pre)derivators", "I. Generalities on (pre)derivators", "chapter",
                    None),
    "Der-ChII-234": ("Chapter II", "Cofinality (on the right and on the left)\\\\(preliminary to cohomological "
                     "cofinality)", "II. Cofinality (on the right and on the left)", "chapter",
                     "Cofinality (on the right and on the left) (preliminary to cohomological cofinality)"),
    "Der-ChIII-567": ("Chapter III", "External Hom in derivators", "III. External Hom in derivators", "chapter", None),
    "Der-ChIV-567": ("Chapter IV", "Substantial diagrams", "IV. Substantial diagrams", "chapter", None),
    "Der-ChV-234": ("Chapter V", "Categories of paths and localization", "V. Categories of paths and localization",
                    "chapter", None),
    "Der-ChVI-345": ("Chapter VI", "HOT", "VI. HOT", "chapter", None),
    "Der-ChVII-456": ("Chapter VII", "Categories of paths (2)", "VII. Categories of paths (2)", "chapter", None),
    "Der-ChVIII-567": ("Chapter VIII", "Relative homotopy 1-types: their integration\\,\\dots",
                       "VIII. Relative homotopy 1-types: their integration\\,\\dots", "chapter",
                       "Relative homotopy 1-types: their integration\\texorpdfstring{\\,\\dots}{…}"),
    "Der-ChIX-678": ("Chapter IX", "Return to the categories of fractions $\\mathcal{M}W^{-1}$,\\\\comparison with "
                     "Quillen", "IX. Return to the categories of fractions $\\mathcal{M}W^{-1}$", "chapter",
                     "Return to the categories of fractions \\texorpdfstring{$\\mathcal{M}W^{-1}$}{MW\u207b\u00b9}, "
                     "comparison with Quillen"),
    "Der-ChX-789": ("Chapter X", "Comparison of Cat with $\\boldsymbol{\\Delta}^{\\wedge}$",
                    "X. Comparison of Cat with $\\boldsymbol{\\Delta}^{\\wedge}$", "chapter",
                    "Comparison of Cat with \\texorpdfstring{$\\boldsymbol{\\Delta}^{\\wedge}$}{\u0394\\textasciicircum}"),
    "Der-ChXI-890": ("Chapter XI", "Hot-fibrations, proper functors and smooth functors etc.\\\\(in Cat)",
                     "XI. Hot-fibrations, proper functors and smooth functors", "chapter",
                     "Hot-fibrations, proper functors and smooth functors etc. (in Cat)"),
    "Der-ChXIIa-012": ("Chapter XII", "Characterization of $W_\\infty$. $W$-proper, $W$-smooth functors etc.\\\\"
                       "Amalgamated sums and $W$-cocartesian squares in Cat",
                       "XII. Characterization of $W_\\infty$, sections 1--4", "chapter",
                       "Characterization of \\texorpdfstring{$W_\\infty$}{W\u221e}. " + W + "-proper, " + W +
                       "-smooth functors etc. Amalgamated sums and " + W + "-cocartesian squares in Cat"),
    "Der-ChXIIb-012": ("Chapter XII", "Section 5", "XII. Characterization of $W_\\infty$, section 5", "part",
                       "Section 5"),
    "Der-ChXIIc-30-03-03": ("Chapter XII", "Section 6", "XII. Characterization of $W_\\infty$, section 6", "part",
                            "Section 6"),
    "Der-ChXIIapp-19-06-03": ("Chapter XII", "Appendix", "XII. Characterization of $W_\\infty$, appendix", "part",
                              "Appendix"),
    "Der-ChXIII-25-01-04": ("Chapter XIII", "Categories of models (1)", "XIII. Categories of models (1)", "chapter",
                            None),
    "Der-ChXIV-07-10-10": ("Chapter XIV", "h-cartesian and h-cocartesian squares",
                           "XIV. h-cartesian and h-cocartesian squares", "chapter", None),
    "Der-ChXV-05-11-10": ("Chapter XV", "Factorization theorems\\\\(Models (2))",
                          "XV. Factorization theorems (Models (2))", "chapter", "Factorization theorems (Models (2))"),
    "der-ch16": ("Chapter XVI", "The basic localizers", "XVI. The basic localizers", "chapter", None),
    "der-ch17": ("Chapter XVII", "Categories with fibrations and cofibrations\\\\(Models (3))",
                 "XVII. Categories with fibrations and cofibrations", "chapter",
                 "Categories with fibrations and cofibrations (Models (3))"),
    "der-ch18": ("Chapter XVIII", "Accessible categories and sets", "XVIII. Accessible categories and sets", "chapter",
                 None),
    "der-ch19": ("Chapter XIX", "Models (4)", "XIX. Models (4)", "chapter", None),
}
XII_FIRST_PART = "Sections 1--4"  # the TOC line of chapter XII's first file

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
\usepackage[a4paper,left=27mm,right=35mm,top=28mm,bottom=27mm,headsep=9mm,marginparwidth=25mm,marginparsep=5mm]{geometry}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{xurl}
\usepackage{adjustbox}
% a diagram wider than the line or taller than the page is scaled down to fit (the widest, a chart of chapter II,
% runs to more than twice the width of the line); a diagram that fits is set as it is
\AddToHook{env/tikzcd/before}{\begin{adjustbox}{max width=\linewidth,max totalheight=\textheight}}
\AddToHook{env/tikzcd/after}{\end{adjustbox}}
\usepackage[hyperfootnotes=false,bookmarksopen=true,bookmarksopenlevel=1]{hyperref}
\hypersetup{pdftitle={Les Dérivateurs (English translation)},pdfauthor={Alexander Grothendieck},
  pdfsubject={English translation of the edition by M. Künzer, J. Malgoire and G. Maltsiniotis},
  colorlinks=true,linkcolor=black,urlcolor=blue!45!black,pdfdisplaydoctitle=true}
\setlength{\emergencystretch}{2em}
\setlength{\headheight}{14pt}
\makeatletter
\newcommand{\derleqno}{\tagsleft@true}
\renewcommand*{\@pnumwidth}{2.4em}
\renewcommand*{\@tocrmarg}{3.4em}
% \mathllap, \mathrlap, \mathclap as mathtools defines them (one unit uses \mathllap)
\providecommand*{\mathllap}[1]{\mathpalette\der@mathllap{#1}}
\providecommand*{\mathrlap}[1]{\mathpalette\der@mathrlap{#1}}
\providecommand*{\mathclap}[1]{\mathpalette\der@mathclap{#1}}
\def\der@mathllap#1#2{\llap{$\m@th#1{#2}$}}
\def\der@mathrlap#1#2{\rlap{$\m@th#1{#2}$}}
\def\der@mathclap#1#2{\hb@xt@\z@{\hss$\m@th#1{#2}$\hss}}
% the margin marks: p. n where page n of the edition begins, [page n] where page n of the manuscript begins
\newcommand{\derpp}[1]{\marginpar{\raggedright\footnotesize\color{black!55}p.~#1}}
\newcommand{\dermsp}[1]{\marginpar{\raggedright\footnotesize\ttfamily[#1]}}
% the editors' note of an edition file, under the chapter heading
\newenvironment{dernote}{\par\begingroup\small\setlength{\parindent}{0pt}\setlength{\parskip}{0.6ex}}%
  {\par\endgroup\vspace{2mm}\noindent\rule{0.3\textwidth}{0.4pt}\par\vspace{5mm}\@afterheading}
% #1 heading line, #2 title, #3 running head, #4 TOC text
\newcommand{\derchapter}[4]{\clearpage\setcounter{footnote}{0}\phantomsection
  \addcontentsline{toc}{section}{#4}\markboth{#3}{#3}\thispagestyle{plain}%
  \vspace*{10mm}{\centering\ifx\relax#1\relax\else{\large\scshape #1\par}\vspace{3mm}\fi
  {\LARGE\bfseries #2\par}}\vspace{9mm}\@afterheading}
% a later edition file of chapter XII
\newcommand{\derpart}[4]{\clearpage\setcounter{footnote}{0}\phantomsection
  \addcontentsline{toc}{subsection}{#4}\markboth{#3}{#3}%
  \vspace*{4mm}{\centering{\large\scshape #1\par}\vspace{2mm}{\Large\bfseries #2\par}}\vspace{7mm}\@afterheading}
\renewcommand*{\l@section}[2]{\addpenalty{-\@highpenalty}\vskip 0.8em plus 1pt
  {\leftskip 0pt\rightskip\@tocrmarg\parfillskip -\rightskip\parindent 0pt\interlinepenalty\@M
   \leavevmode\normalsize #1\nobreak\leaders\hbox{$\m@th\mkern\@dotsep mu\hbox{.}\mkern\@dotsep mu$}\hfill
   \nobreak\hb@xt@\@pnumwidth{\hss #2}\par}}
\renewcommand*{\l@subsection}{\@dottedtocline{2}{1.5em}{0em}}
\makeatother
% two styles, each setting all its fields: the body (running head, page number at the right of the head) and plain
% (page number in the foot: front matter, chapter openings); a style set with \pagestyle{fancy} would keep the fields
% that \pagestyle{plain} cleared
\fancypagestyle{derbody}{\fancyhf{}\fancyhead[L]{\small\itshape\leftmark}\fancyhead[R]{\small\thepage}%
  \renewcommand{\headrulewidth}{0pt}}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\small\thepage}\renewcommand{\headrulewidth}{0pt}}
\pagestyle{derbody}
"""


def front_matter():
    return r"""\begin{document}
\pdfbookmark[1]{Title page}{title}
\begin{titlepage}
\centering
\vspace*{0.2\textheight}
{\Large Alexander Grothendieck\par}
\vspace{2.2em}
{\fontsize{30}{36}\selectfont\bfseries Les Dérivateurs\par}
\vspace{1.4em}
{\Large The Derivators\par}
\vspace{0.6em}
{\large English translation\par}
\vspace{3.5em}
{\normalsize of the edition by M.~Künzer, J.~Malgoire and G.~Maltsiniotis\par}
\vfill
{\small Reader of """ + DATE + r"""\par}
\end{titlepage}
\setcounter{page}{2}
\pagestyle{plain}
\pdfbookmark[1]{About this book}{about}
\noindent\textbf{The text.} Alexander Grothendieck wrote \emph{Les Dérivateurs} from October 1990 through the first
half of 1991. This
book is an English translation of the electronic edition by M.~Künzer, J.~Malgoire and G.~Maltsiniotis (Universités de
Montpellier~II et Paris~VII), \url{""" + EDITION_URL + r"""}: its table of contents and its twenty-two files, one for
each chapter and four for chapter XII. The deciphering of the manuscript, its edition and the editors' notes are
theirs. The contents give the version of each file.

\medskip
\noindent\textbf{How to read it.} In the margin, {\footnotesize\color{black!55}p.~$n$} marks where page $n$ of the
edition begins, and {\footnotesize\ttfamily[page $n$]} where page $n$ of Grothendieck's manuscript begins, as the
edition gives it. Grothendieck's page references are to the pages of his manuscript, and so are the page numbers of the
edition's table of contents and of its indexes. Words in typewriter type between square brackets are the editors':
their corrections and comments and the manuscript's page numbers; a question mark in brackets means that the editors
were not sure of the word before it. Each chapter opens with the editors' note of its edition file. The e-mail address
of G.~Maltsiniotis, which the editors give for remarks, is not reproduced. Formulas and notation are those of the edition, which differ between
chapters; only the words inside formulas and diagrams are translated (``def'' over the equality sign, for ``déf'').
Diagrams wider than the text are set smaller, to fit it.

\medskip
\noindent\textbf{How this book was made.} The French text is our LaTeX transcription of the edition, release
v2026-11-11b of \url{""" + REPO_URL + r"""}. It is AI-transcribed by Claude Opus~5.5 (Anthropic) from the pages of the
edition and carries the corrections of its critical companion, AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)
and checked against the edition by Claude Opus~5.5. The English is AI-translated by GPT-6.1 Sol (OpenAI API, reasoning
effort max), five pages of the edition at a time, with a glossary of Grothendieck's terms by Claude Fable~5.2 and
Claude Opus~5.5 (Anthropic), whose English follows his own English of \emph{Pursuing Stacks} where it has one. Every
five pages were checked by script against the French: the formulas identical, the page marks and labels in place, the
glossary's terms used, no French left. The whole translation was then compared with the French paragraph by paragraph
and sentence by sentence for anything missing or left in French, and the places found were corrected. The checks, the
corrections and this book are by Claude Opus~5.5 (Anthropic). The checks compare the English with the French; they do
not judge its prose. The sources, the checks and their records are in the directory \texttt{en/} of the repository.

\bigskip
\noindent\textbf{Rights}

\smallskip
\noindent The rights in the original work belong to its author or the author's representatives or heirs. Where we
hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the
public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we
do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will
take it down.
\clearpage
\pdfbookmark[1]{Contents}{contents}
\tableofcontents
\clearpage
\pagestyle{derbody}
"""


# ---------------------------------------------------------------- reading the units

CMT = re.compile(r"(?<!\\)%.*")
EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")


def unit_doc(u):
    s = T.read(os.path.join(T.ROOT, "translation", u["folder"], u["id"] + ".tex")).replace("\r\n", "\n")
    return T.split_doc(s)


def brace_end(s, i):
    """Index after the group that opens at s[i] == '{' (comments and escaped characters skipped)."""
    depth, k = 0, i
    while k < len(s):
        c = s[k]
        if c == "\\":
            k += 2
            continue
        if c == "%":
            k = s.find("\n", k)
            if k < 0:
                break
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return k + 1
        k += 1
    raise ValueError("unbalanced braces")


def unwrap_atbegindocument(pre):
    while True:
        m = re.search(r"\\AtBeginDocument\s*\{", pre)
        if not m:
            return pre
        a = m.end() - 1
        b = brace_end(pre, a)
        pre = pre[:m.start()] + pre[a + 1:b - 1] + pre[b:]


SKIP = re.compile(r"\s*\\(documentclass|usepackage|usetikzlibrary|frenchsetup)(?![A-Za-z])|"
                  r"\s*\\setlength\s*\{?\\(parindent|parskip)\}?")
DMO = re.compile(r"\\DeclareMathOperator(\*?)\s*\{?(\\[A-Za-z]+)\}?\s*\{([^}]*)\}")


def definitions(pre):
    """The lines of a unit's preamble set at the head of its group, each ending in % (no space, no paragraph end)."""
    out = ["\\begingroup\\makeatletter%"]
    if "leqno" in pre:
        out.append("\\derleqno%")
    if "AutoSpacePunctuation=false" in pre:
        out.append("\\NoAutoSpacing%")
    for line in unwrap_atbegindocument(pre).split("\n"):
        if not line.strip() or line.lstrip().startswith("%") or SKIP.match(line):
            continue
        line = DMO.sub(lambda m: "\\DeclareRobustCommand{%s}{\\operatorname%s{%s}}" % (m.group(2), m.group(1),
                                                                                       m.group(3)), line).rstrip()
        if not re.search(r"(?<!\\)%", line):
            line += "%"
        out.append(line)
    out.append("\\makeatother\\let\\printedpage\\derpp\\let\\msp\\dermsp%")
    return out


# ---------------------------------------------------------------- front pages of the edition files

PAGEBREAK = re.compile(r"\\(?:clearpage|newpage|cleardoublepage|pagebreak(?:\[\d\])?)(?![A-Za-z])")
NUMERIC_PP = re.compile(r"\\printedpage\{[^}]*\d[^}]*\}")


def split_front(body):
    """(front pages, rest): the front pages are the title page and the editors' note before the first numbered
    edition page; they end at the last page break before it."""
    m = NUMERIC_PP.search(body)
    if not m:
        return "", body
    breaks = list(PAGEBREAK.finditer(body, 0, m.start()))
    if not breaks:
        return "", body
    return body[:breaks[-1].end()], body[breaks[-1].end():]


def front_pages(front):
    return [p for p in PAGEBREAK.split(front) if CMT.sub("", p).strip()]


def clean_note(page):
    """The editors' note as set in the reader: its text, without the layout commands, the anchor of its unnumbered
    page and the sentence that gives the e-mail address."""
    t = "\n".join(ln for ln in page.split("\n") if not ln.lstrip().startswith("%"))
    t = CMT.sub("", t)
    t = re.sub(r"\\printedpage\{[^}]*\}", "", t)
    t = re.sub(r"\\(?:vspace|hspace)\*?\{[^}]*\}", "", t)
    t = re.sub(r"\\(?:noindent|hfill|qquad|quad|centering)(?![A-Za-z])", "", t)
    t = re.sub(r"\\(?:begin|end)\{(?:flushright|center)\}", "", t)
    t = re.sub(r"\s*Send a message to:\s*", "\n", t)
    t = re.sub(r"\\textbf\{[^{}]*@[^{}]*\}\s*(\\\\)?", "", t)
    t = re.sub(r"\\\\\s*", "\n", t)
    t = t.strip()
    sig = re.search(r"G\.\s*Maltsiniotis\s*$", t)
    if sig:
        t = t[:sig.start()].rstrip() + "\n\n\\hfill G.~Maltsiniotis"
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t).strip()
    if "@" in t:
        raise SystemExit("an e-mail address is left in an editors' note: " + t[:200])
    return "\\begin{dernote}\n" + t + "\n\\end{dernote}\n"


def title_text(page):
    t = CMT.sub("", page)
    t = re.sub(r"\\printedpage\{[^}]*\}", "", t)
    t = re.sub(r"\\(?:vspace|hspace)\*?\{[^}]*\}|\\(?:bigskip|medskip|smallskip|centering|noindent)(?![A-Za-z])", "", t)
    t = re.sub(r"\\(?:begin|end)\{center\}", "", t)
    t = re.sub(r"\\(?:Large|LARGE|large|huge|Huge|sffamily|bfseries)(?![A-Za-z])", "", t)
    t = re.sub(r"\\text(?:bf|sf)\{", "{", t)
    t = re.sub(r"[{}]", "", t)
    return re.sub(r"\s+", " ", t.replace("\\\\", " ")).strip()


# ---------------------------------------------------------------- seams between units

LEAD_TOK = r"(?:\\noindent|\\printedpage\{[^}]*\}|\\msp\{[^}]*\}|\\setcounter\{[^}]*\}\{[^}]*\}|\\sbox\{[^}]*\}\{.*\})"
LEAD = re.compile(r"^\s*(?:" + LEAD_TOK + r"\s*)+$")


def lines_nc(text):
    out = []
    for ln in text.split("\n"):
        t = CMT.sub("", ln).rstrip()
        if t.strip():
            out.append(t)
    return out


def last_text_line(body):
    """The last line of a body with text other than anchors (comments removed)."""
    ls = [ln for ln in lines_nc(body) if not LEAD.match(ln)]
    return ls[-1] if ls else ""


def classify(prev_body, body):
    """Does the body of a unit continue the paragraph with which the previous unit's body ends? (join, end, start)
    end: stop (a sentence, an ellipsis or a structure ends), display (a display ends), hyphen (a word cut by the
    edition's hyphen), open (none of these);
    start: word (a lower-case word), punct, math (an inline formula), bracket (an editors' note in brackets), display,
    upper (a capital or an opening parenthesis or quotation mark), struct (anything else: an environment, a heading,
    a label in bold, an item, spacing, a macro)."""
    last = last_text_line(prev_body)
    first, noindent = "", False
    for ln in lines_nc(body):
        if "\\noindent" in ln:
            noindent = True
        if LEAD.match(ln):
            continue
        first = re.sub(r"^\s*(?:(?:\\noindent|\\printedpage\{[^}]*\}|\\msp\{[^}]*\})\s*)+", "", ln)
        break
    if re.search(r"[A-Za-z]-\s*$", last):
        end = "hyphen"
    elif re.search(r"[.!?;:]['’”)}\]]*\s*$|(\\ldots|\\dots|…|\.\.\.)\s*\}?\s*$", last) or \
            re.search(r"\\end\{(itemize|enumerate|description|center|quote|quotation|flushleft|flushright|tabular|"
                      r"minipage)\}\s*$|\\endgroup\s*$|\\par\s*$", last):
        end = "stop"
    elif re.search(r"\\\]\s*$|\\end\{(equation|align|gather|multline|eqnarray|displaymath)\*?\}\s*$|\$\$\s*$", last):
        end = "display"
    else:
        end = "open"
    f = first.lstrip()
    if re.match(r"[a-z]|\\(textit|emph|underline|textup)\{[a-z]", f):
        start = "word"
    elif re.match(r"[,.;:)]", f):
        start = "punct"
    elif re.match(r"\$(?!\$)", f):
        start = "math"
    elif re.match(r"\\texttt\{\[", f):
        start = "bracket"
    elif re.match(r"\\\[|\$\$|\\begin\{(equation|align|gather|multline|eqnarray|displaymath)\*?\}", f):
        start = "display"
    elif re.match(r"[A-Z(`'\"“‘]|\\(textit|emph|underline|textup)\{[A-Z(]", f):
        start = "upper"
    else:
        start = "struct"
    colon = re.search(r":['’”)}]*\s*$", last) is not None
    join = start in ("word", "punct") or \
        (start in ("math", "bracket", "display") and (end != "stop" or colon)) or \
        (start == "upper" and end in ("open", "hyphen")) or (start == "upper" and end == "display" and noindent)
    if end == "hyphen" and start != "word":
        join = False
    return join, end, start, last, first


def lead_joined(body):
    """The beginning of a body that continues the previous paragraph: the blank lines before its first line of text
    are dropped, and the lines of anchors before it end in % (no space)."""
    lines = body.lstrip("\n").split("\n")
    out, k = [], 0
    while k < len(lines):
        ln = lines[k]
        bare = CMT.sub("", ln).strip()
        if not bare:
            if ln.strip():
                out.append(ln)  # a comment line
            k += 1
            continue
        if LEAD.match(CMT.sub("", ln)):
            out.append(ln if re.search(r"(?<!\\)%", ln) else ln.rstrip() + "%")
            k += 1
            continue
        break
    return "\n".join(out + lines[k:])


def end_for_join(body, first, end):
    """The end of a body whose paragraph runs on into the next unit: no blank line at its end, and exactly one space
    before the next word (none before punctuation, none inside a word cut by a hyphen, whose hyphen goes)."""
    lines = body.rstrip().split("\n")
    texts = [i for i, ln in enumerate(lines) if CMT.sub("", ln).strip() and not LEAD.match(CMT.sub("", ln))]
    k = texts[-1]
    for i in range(k + 1, len(lines)):  # anchor lines after the last text: no space of their own
        if CMT.sub("", lines[i]).strip() and not re.search(r"(?<!\\)%", lines[i]):
            lines[i] = lines[i].rstrip() + "%"
    m = re.search(r"(?<!\\)%", lines[k])
    code, comment = (lines[k][:m.start()], lines[k][m.start():]) if m else (lines[k].rstrip(), "")
    if end == "hyphen":
        lines[k] = re.sub(r"-\s*$", "", code) + "%" + comment[1:] if comment else re.sub(r"-\s*$", "", code) + "%"
    elif re.match(r"\s*[,.;:)]", first):
        lines[k] = code.rstrip() + "%" + (comment[1:] if comment else "")
    else:
        lines[k] = code.rstrip() + "\\space%" + (comment[1:] if comment else "")
    return "\n".join(lines)


# ---------------------------------------------------------------- the book

def digitless_anchors(body):
    """The anchors of unnumbered edition pages print nothing."""
    return re.sub(r"\\printedpage\{([^}]*)\}", lambda m: m.group(0) if re.search(r"\d", m.group(1)) else "\\relax",
                  body)


def build(show=False):
    units = T.units()
    parts = [PREAMBLE, front_matter()]
    notes, titles, seams = {}, {}, []
    joined = collections.Counter()
    kept = collections.Counter()
    for folder, _, _, _ in T.FILES:
        mine = [u for u in units if u["folder"] == folder]
        head, title, run, kind, toc = CHAPTERS[folder]
        toc = toc or title
        version = T.VERSIONS.get(folder, "")
        # the version is printed in the contents, not in the PDF bookmarks
        # (a control space: in the contents file a plain space after \dots, chapter VIII, would be lost)
        vtxt = "\\texorpdfstring{\\ {\\normalfont\\small (version of %s)}}{}" % version if version else ""
        if kind == "front":
            parts.append("\\derchapter{}{%s}{%s}{%s}\n" % (title, run, toc))
        elif kind == "chapter" and folder == "Der-ChXIIa-012":
            parts.append("\\derchapter{%s}{%s}{%s}{%s. %s}\n" % (head, title, run, head, toc))
            parts.append("\\phantomsection\\addcontentsline{toc}{subsection}{%s%s}\n" % (XII_FIRST_PART, vtxt))
        elif kind == "chapter":
            parts.append("\\derchapter{%s}{%s}{%s}{%s. %s%s}\n" % (head, title, run, head, toc, vtxt))
        else:
            parts.append("\\derpart{%s}{%s}{%s}{%s%s}\n" % (head, title, run, toc, vtxt))
        entries = []
        for i, u in enumerate(mine):
            pre, body = unit_doc(u)
            if folder == "dertbmt":
                body = re.sub(r"\\begin\{center\}.*?\\end\{center\}\s*\\bigskip", "", body, count=1, flags=re.S)
            if i == 0:
                front, rest = split_front(body)
                if front:
                    pages = front_pages(front)
                    note = [p for p in pages if "deciphered" in p]
                    if len(note) > 1:
                        raise SystemExit("%s: two editors' notes" % u["id"])
                    titles[folder] = [title_text(p) for p in pages if p not in note]
                    notes[folder] = clean_note(note[0]) if note else ""
                    body = (notes[folder] + "\n" + rest) if note else rest
            body = PAGEBREAK.sub(r"\\par", body)
            join, first = False, ""
            if entries:
                join, end, start, last, first = classify(entries[-1]["body"], body)
                (joined if join else kept)[(end, start)] += 1
                if join:
                    seams.append((u["id"], end, start, last[-80:], first[:80]))
                    entries[-1]["body"] = end_for_join(entries[-1]["body"], first, end)
                    entries[-1]["joins_next"] = True
                    body = lead_joined(body)
            own_fn = "\\thefootnote" in pre
            head_lines = definitions(pre)
            if own_fn:
                head_lines.append("\\edef\\derfnsaved{\\the\\value{footnote}}\\setcounter{footnote}{0}%")
            entries.append({"head": "\n".join(head_lines), "body": body, "own_fn": own_fn, "joins_next": False})
        for e in entries:
            # an e-mail address in the text (the editors ask a reader to write to G. Maltsiniotis, chapter V) is
            # not reproduced, as in the units of en/ in the repository
            body = EMAIL.sub("[e-mail address removed]", digitless_anchors(e["body"]))
            if e["joins_next"]:
                body = body.rstrip() + "\n"
            else:
                body = body.strip("\n") + "\n\n"
            tail = ("\\setcounter{footnote}{\\derfnsaved}%\n" if e["own_fn"] else "") + "\\endgroup" + \
                ("%\n" if e["joins_next"] else "\n\n")
            parts.append(e["head"] + "\n" + body.lstrip("\n") + tail)
    parts.append("\\end{document}\n")
    if show:
        for folder in T.FILES:
            f = folder[0]
            if f in titles or f in notes:
                print("=" * 20, f, "| title page:", titles.get(f))
                print(notes.get(f, ""))
        print("seams joined:", sum(joined.values()), dict(joined))
        print("seams kept as paragraph ends:", sum(kept.values()), dict(kept))
        for s in seams:
            print("  ", s)
        return None
    return "".join(parts)


def compile_pdf():
    for _ in range(3):
        subprocess.run(["lualatex", "--no-shell-escape", "-interaction=nonstopmode", "-file-line-error",
                        NAME + ".tex"], cwd=OUT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = T.read(os.path.join(OUT, NAME + ".log"))
    pages = re.search(r"Output written on .*?\((\d+) pages", log)
    # with -file-line-error an error reads "file:line: message", in the book or in a package file
    errors = re.findall(r"^.*\.(?:tex|sty|cls|def|cfg|fd|lua):\d+: .*|^! .*", log, re.M)
    undef = re.findall(r"(?:Reference|Citation) `[^']*' on page \d+ undefined|There were undefined references|"
                       r"Label\(s\) may have changed", log)
    print("%s.pdf: %s pages, %d LaTeX errors, %d undefined references or unsettled labels" % (
        NAME, pages.group(1) if pages else "?", len(errors), len(undef)))
    for e in errors[:40]:
        print("  ", e)
    for e in undef[:10]:
        print("  ", e)


def main():
    show = "--show" in sys.argv
    tex = build(show)
    if show:
        return
    os.makedirs(OUT, exist_ok=True)
    T.write(os.path.join(OUT, NAME + ".tex"), tex)
    print("%s.tex: %d characters" % (NAME, len(tex)))
    if "--pdf" in sys.argv:
        compile_pdf()


if __name__ == "__main__":
    main()
