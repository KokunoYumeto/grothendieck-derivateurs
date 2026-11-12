# Derived from scripts/build_reader.py in DER_02_english_translation.zip.
# Original reader: Claude Opus 5.5 (Anthropic); adaptation: GPT-6 Astra (OpenAI).
import re

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

CMT = re.compile(r"(?<!\\)%.*")

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

PAGEBREAK = re.compile(r"\\(?:clearpage|newpage|cleardoublepage|pagebreak(?:\[\d\])?)(?![A-Za-z])")

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
