"""Build the integrated reader of the Les Dérivateurs companion: one book holding every returned chunk in manuscript
order under its chapter, with one table of contents (which also names the parts the book does not contain yet), PDF
bookmarks, a register of the claims, the counts of the transcription corrections and one bibliography.

Each chunk is read from its checked files: checks/DER_<id>/DER_<id>_reader.tex (the text with the commentary blocks set
in, built by kit/build_reader.py), _overview.tex, _references.bib, _claims.csv and _corrections.csv. A chunk whose checked
reader is not there yet is absent, and the contents say so.

Locality: every chunk is set inside a group that applies the definitions of its own preamble (\\newcommand, \\def,
\\DeclareMathOperator and the like, written to reader/parts/DER_<id>_defs.tex), so that macros of the same name defined
differently by different chunks never meet; the packages of all the chunks are loaded once, in the global preamble,
with their options united (clashes resolved below, see BOOK_OPTIONS). Labels are qualified by the chunk ("DER_I-a:x").
The chunks' bibliographies are merged into one (the first entry of a key wins; a later entry of the same key that
differs in anything but its note is reported). Edition pages that two chunks both transcribe are set once (SKIP_PAGES).

Writes  reader/LesDerivateurs_companion.tex, reader/LesDerivateurs_companion.bib, reader/parts/DER_<id>.tex and
        reader/parts/DER_<id>_defs.tex; with --pdf also reader/LesDerivateurs_companion.pdf (LuaLaTeX, BibTeX,
        LuaLaTeX, LuaLaTeX, and LuaLaTeX again while the log asks for a rerun) and a report of pages, LaTeX errors,
        undefined references and multiply defined labels.
usage: python -I kit/build_global_reader.py [--pdf]   (paths: companion/checks, companion/reader)"""
import collections
import csv
import os
import pathlib
import re
import subprocess
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
KIT = pathlib.Path(__file__).resolve().parent
ROOT = KIT.parent / "companion"
CHECKS = ROOT / "checks"
OUT = ROOT / "reader"
NAME = "LesDerivateurs_companion"

# ------------------------------------------------------------------------------------------------------------------
# The work. Chapters in order: key, numeral in the contents, heading line, title (the edition's).
CHAPTERS = [
    ("I", "I", "Chapter I", "Généralités sur les (pré)dérivateurs"),
    ("II", "II", "Chapter II", "Cofinalité (à droite et à gauche) (préliminaire à la cofinalité cohomologique)"),
    ("III", "III", "Chapter III", "Hom externes dans les dérivateurs"),
    ("IV", "IV", "Chapter IV", "Diagrammes substantiels"),
    ("V", "V", "Chapter V", "Catégories de chemins et localisation"),
    ("VI", "VI", "Chapter VI", "HOT"),
    ("VII", "VII", "Chapter VII", "Catégories de chemins (2)"),
    ("VIII", "VIII", "Chapter VIII", "1-types d'homotopie relatifs : leur intégration\\,\\dots"),
    ("IX", "IX", "Chapter IX", "Retour sur les catégories de fractions $\\mathcal{M}W^{-1}$, comparaison avec Quillen"),
    ("X", "X", "Chapter X", "Comparaison de Cat avec $\\boldsymbol{\\Delta}^{\\wedge}$"),
    ("XI", "XI", "Chapter XI", "Hot-fibrations, foncteurs propres et foncteurs lisses etc. (dans Cat)"),
    ("XII", "XII", "Chapter XII", "Caractérisation de $W_\\infty$. Foncteurs $W$-propres, $W$-lisses etc. Sommes "
                                  "amalgamées et carrés $W$-cocartésiens dans Cat"),
    ("XIIapp", "", "Chapter XII, appendix", "Appendice au chapitre XII"),
    ("XIII", "XIII", "Chapter XIII", "Catégories de modèles (1)"),
    ("XIV", "XIV", "Chapter XIV", "Carrés h-cartésiens et h-cocartésiens"),
    ("XV", "XV", "Chapter XV", "Théorèmes de factorisation (Modèles (2))"),
    ("XVI", "XVI", "Chapter XVI", "Les localiseurs fondamentaux"),
    ("XVII", "XVII", "Chapter XVII", "Catégories à fibrations et à cofibrations (Modèles (3))"),
    ("XVIII", "XVIII", "Chapter XVIII", "Catégories et ensembles accessibles"),
    ("XIX", "XIX", "Chapter XIX", "Modèles (4)"),
]
CHAPTER = {k: (num, head, title) for k, num, head, title in CHAPTERS}
CHAPTER_ORDER = [k for k, *_ in CHAPTERS]
# The 32 chunks in manuscript order (make_package.py --list) and the chapters each covers, with the part it is of each
# (empty: the whole chapter).
CHUNKS = [
    ("DER_I-a", [("I", "part 1 of 2")]), ("DER_I-b", [("I", "part 2 of 2")]),
    ("DER_II-a", [("II", "part 1 of 2")]), ("DER_II-b", [("II", "part 2 of 2")]),
    ("DER_III-V", [("III", ""), ("IV", ""), ("V", "")]),
    ("DER_VI-a", [("VI", "part 1 of 3")]), ("DER_VI-b", [("VI", "part 2 of 3")]), ("DER_VI-c", [("VI", "part 3 of 3")]),
    ("DER_VII-a", [("VII", "part 1 of 3")]), ("DER_VII-b", [("VII", "part 2 of 3")]),
    ("DER_VII-c", [("VII", "part 3 of 3")]),
    ("DER_VIII-X", [("VIII", ""), ("IX", ""), ("X", "")]),
    ("DER_XI-XIIa", [("XI", ""), ("XII", "sections 1--4")]),
    ("DER_XIIb-a", [("XII", "section 5, part 1 of 2")]), ("DER_XIIb-b", [("XII", "section 5, part 2 of 2")]),
    ("DER_XIIc-a", [("XII", "section 6, part 1 of 2")]), ("DER_XIIc-b", [("XII", "section 6, part 2 of 2")]),
    ("DER_XIIapp", [("XIIapp", "")]),
    ("DER_XIII-a", [("XIII", "part 1 of 2")]), ("DER_XIII-b", [("XIII", "part 2 of 2")]),
    ("DER_XIV", [("XIV", "")]),
    ("DER_XV-a", [("XV", "part 1 of 2")]), ("DER_XV-b", [("XV", "part 2 of 2")]),
    ("DER_XVI", [("XVI", "")]),
    ("DER_XVII-a", [("XVII", "part 1 of 2")]), ("DER_XVII-b", [("XVII", "part 2 of 2")]),
    ("DER_XVIII-a", [("XVIII", "part 1 of 5")]), ("DER_XVIII-b", [("XVIII", "part 2 of 5")]),
    ("DER_XVIII-c", [("XVIII", "part 3 of 5")]), ("DER_XVIII-d", [("XVIII", "part 4 of 5")]),
    ("DER_XVIII-e", [("XVIII", "part 5 of 5")]),
    ("DER_XIX", [("XIX", "")]),
]
# Overlaps: eight pairs of chunks transcribe the same five edition pages (one part file of the transcription). The book
# sets those pages once, from the earlier chunk of the pair, which also holds the commentary blocks, claims and
# corrections of the other chunk on them (reader/OVERLAPS.md). For the chunk named here, the edition pages (printed
# page numbers, \printedpage) from..to are not set: the cut runs from the part-file line that opens page `from` to the
# part-file line that opens the next part (or to \printedpage{to+1}). Manuscript pages in the comments.
SKIP_PAGES = {
    "DER_I-b": (34, 38),      # ms. 59 (end)-66 (beginning), set from DER_I-a
    "DER_VI-b": (39, 43),     # ms. 63 (end)-70 (beginning), set from DER_VI-a
    "DER_VI-c": (84, 88),     # ms. 137 (end)-145 (beginning), set from DER_VI-b
    "DER_VII-b": (34, 38),    # ms. 49' (end)-57 (beginning), set from DER_VII-a
    "DER_VII-c": (69, 73),    # ms. 108-117 (beginning), set from DER_VII-b
    "DER_XIIb-b": (78, 82),   # ms. 114 (end)-122 (beginning), set from DER_XIIb-a
    "DER_XIIc-b": (145, 149), # ms. 228-234 (beginning), set from DER_XIIc-a
    "DER_XIII-b": (29, 33),   # ms. 50 (end)-60 (beginning), set from DER_XIII-a
}
STATUSES = ["proved", "sketched", "stated", "assumed", "conjectured", "false", "open"]
LISTED = ("false", "open", "conjectured")
CORRECTION_KINDS = [("transcription", "transcription"), ("edition_slip_kept", "edition slip kept"),
                    ("doubt_resolved", "doubt resolved")]

# The global layout: the options the book sets itself for these packages (a chunk's own options are not used), and
# options of other packages that are dropped from the union.
BOOK_OPTIONS = {"geometry": ["a4paper", "left=25mm", "right=30mm", "top=24mm", "bottom=26mm", "headheight=14pt",
                             "marginparwidth=21mm", "marginparsep=4mm"],
                "microtype": []}
DROP_OPTIONS = {"fontspec": {"no-math"}}           # the transcription's own setting: fontspec sets the math fonts too
KIT_PACKAGES = {"framed", "xcolor", "natbib", "hyperref", "graphicx"}    # loaded by derivateurs_companion.sty
HYPERREF_OPTIONS = ["hyperfootnotes=false", "bookmarksnumbered=true", "bookmarksopen=true", "bookmarksopenlevel=0"]

# ------------------------------------------------------------------------------------------------------------------
# Reading TeX: groups, comments, statements.


def skip_ws(t, i):
    while i < len(t) and t[i] in " \t\r\n":
        i += 1
    return i


def read_group(t, i, open_="{", close="}"):
    """The balanced group starting at t[i] (which must be open_): (content, index after it); escaped braces skipped."""
    assert t[i] == open_
    depth, j = 0, i
    while j < len(t):
        c = t[j]
        if c == "\\":
            j += 2
            continue
        if c == "%":
            j = t.find("\n", j)
            if j < 0:
                break
            continue
        if c == open_:
            depth += 1
        elif c == close:
            depth -= 1
            if depth == 0:
                return t[i + 1:j], j + 1
        j += 1
    raise ValueError(f"unbalanced {open_}{close} at {t[i:i + 60]!r}")


def comment_mask(t):
    """A list of booleans: True where t[k] is inside a comment."""
    mask, i, n = [False] * len(t), 0, len(t)
    while i < n:
        c = t[i]
        if c == "\\":
            i += 2
            continue
        if c == "%":
            j = t.find("\n", i)
            j = n if j < 0 else j
            for k in range(i, j):
                mask[k] = True
            i = j
            continue
        i += 1
    return mask


PACKAGE_CMDS = {"usepackage", "RequirePackage"}
CLASS_CMDS = {"documentclass"}
PASS_CMDS = {"PassOptionsToPackage"}
TIKZ_CMDS = {"usetikzlibrary", "usepgflibrary"}
DEFINE_CMDS = {"newcommand", "renewcommand", "providecommand", "DeclareRobustCommand", "def", "edef", "gdef", "xdef",
               "let", "DeclareMathOperator", "newenvironment", "renewenvironment", "NewDocumentCommand",
               "RenewDocumentCommand", "ProvideDocumentCommand", "DeclareDocumentCommand", "NewDocumentEnvironment",
               "RenewDocumentEnvironment", "newif", "newcounter", "newlength", "newsavebox", "newtoks", "newcount",
               "newdimen", "newskip", "newcolumntype", "tikzset", "tikzcdset", "pgfkeys", "definecolor", "colorlet",
               "newtheorem", "theoremstyle", "mathchardef", "chardef", "newfontfamily", "newfontface",
               "makeatletter", "makeatother", "catcode", "DeclarePairedDelimiter"}
GLOBAL_DEFINE_CMDS = {"DeclareMathAlphabet", "DeclareSymbolFont", "DeclareSymbolFontAlphabet", "SetMathAlphabet",
                      "SetSymbolFont", "DeclareMathSymbol", "DeclareMathDelimiter", "DeclareMathAccent",
                      "DeclareMathRadical", "DeclareFontFamily", "DeclareFontShape", "setmathfont"}
# layout, typography and the per-chunk reader's own settings: the book sets its own
DROP_CMDS = {"setlength", "addtolength", "emergencystretch", "raggedbottom", "flushbottom", "frenchsetup",
             "setmainfont", "setmonofont", "setsansfont", "geometry", "hypersetup", "AtBeginDocument", "AtEndDocument",
             "AddToHook", "AddToHookNext", "AtBeginEnvironment", "AtEndEnvironment", "BeforeBeginEnvironment",
             "AfterEndEnvironment", "pagestyle", "thispagestyle", "pagenumbering", "pdfextension", "pdfvariable",
             "pdfcompresslevel", "pdfobjcompresslevel", "tracinglostchars", "clubpenalty", "widowpenalty",
             "displaywidowpenalty", "brokenpenalty", "interlinepenalty", "allowdisplaybreaks", "setlist", "setcounter",
             "input", "include", "includeonly", "linespread", "parindent", "parskip", "marginparpush",
             "marginparwidth", "marginparsep", "microtypesetup", "sloppy", "fussy", "urlstyle", "bibliographystyle",
             "title", "author", "date", "selectlanguage", "hyphenation", "tolerance", "pretolerance", "hbadness",
             "vbadness", "hfuzz", "vfuzz", "DocumentMetadata", "frenchbsetup", "babelprovide", "nocite",
             "IfFileExists", "InputIfFileExists", "listfiles", "graphicspath", "pdfstringdefDisableCommands"}
STARTERS = PACKAGE_CMDS | CLASS_CMDS | PASS_CMDS | TIKZ_CMDS | DEFINE_CMDS | GLOBAL_DEFINE_CMDS | DROP_CMDS | {"global"}
CS = re.compile(r"\\([A-Za-z@]+)")


def statements(pre):
    """Split a preamble into its top-level statements, comments kept: a statement begins at a known command or at
    any command opening a line, outside braces and comments."""
    mask, starts, depth, i = comment_mask(pre), [], 0, 0
    while i < len(pre):
        if mask[i]:
            i += 1
            continue
        c = pre[i]
        if c == "\\":
            m = CS.match(pre, i)
            if m:
                line_start = pre.rfind("\n", 0, i) + 1
                if depth == 0 and (m.group(1) in STARTERS or not pre[line_start:i].strip()):
                    starts.append(i)
                i = m.end()
            else:
                i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    return [pre[a:b] for a, b in zip(starts, starts[1:] + [len(pre)])]


def options(s):
    """Split an option list at top-level commas."""
    out, depth, cur = [], 0, ""
    for c in s:
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        if c == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += c
    if cur.strip():
        out.append(cur.strip())
    return [o for o in (re.sub(r"\s+", " ", x) for x in out) if o]


def strip_comments(s):
    mask = comment_mask(s)
    return "".join(c for c, m in zip(s, mask) if not m)


def define(stmt):
    """A definition statement made local-safe: a \\newcommand (or the like) of a macro another chunk or a package may
    already define replaces it inside the group; \\renewcommand of a macro the global context lacks still works;
    \\DeclareMathOperator (preamble only) becomes a \\newcommand; global definitions become local ones."""
    s = re.sub(r"\\gdef(?![A-Za-z])", r"\\def", stmt)
    s = re.sub(r"\\xdef(?![A-Za-z])", r"\\edef", s)
    name = r"\s*(?:\{\s*(\\[A-Za-z@]+)\s*\}|(\\[A-Za-z@]+))"

    def let_relax(m):
        cs = m.group(1) or m.group(2)
        return f"\\let{cs}\\relax{m.group(0)}"

    s = re.sub(r"\\(?:newcommand|NewDocumentCommand|newlength|newsavebox|newtoks|newcount|newdimen|newskip)\*?"
               + name, let_relax, s)
    s = re.sub(r"\\renewcommand\*?" + name, lambda m: f"\\providecommand{m.group(1) or m.group(2)}{{}}{m.group(0)}", s)

    def env_relax(m):
        e = m.group(1).strip()
        return (f"\\expandafter\\let\\csname {e}\\endcsname\\relax\\expandafter\\let\\csname end{e}\\endcsname\\relax"
                + m.group(0))

    s = re.sub(r"\\(?:newenvironment|NewDocumentEnvironment)\*?\s*\{([^}]*)\}", env_relax, s)
    s = re.sub(r"\\(?:renewenvironment|RenewDocumentEnvironment)\*?\s*\{([^}]*)\}",
               lambda m: (f"\\expandafter\\providecommand\\csname {m.group(1).strip()}\\endcsname{{}}"
                          f"\\expandafter\\providecommand\\csname end{m.group(1).strip()}\\endcsname{{}}{m.group(0)}"), s)
    s = re.sub(r"\\newcounter\s*\{([^}]*)\}",
               lambda m: f"\\expandafter\\let\\csname c@{m.group(1).strip()}\\endcsname\\relax{m.group(0)}", s)
    s = re.sub(r"\\newtheorem\*?\s*\{([^}]*)\}",
               lambda m: "".join(f"\\expandafter\\let\\csname {p}{m.group(1).strip()}\\endcsname\\relax"
                                 for p in ("", "end", "c@")) + m.group(0), s)
    out, i = "", 0
    for m in re.finditer(r"\\DeclareMathOperator(\*?)", s):
        if m.start() < i:
            continue
        j = skip_ws(s, m.end())
        if j < len(s) and s[j] == "{":
            cs, j = read_group(s, j)
        else:
            cs = CS.match(s, j).group(0)
            j += len(cs)
        j = skip_ws(s, j)
        body, j = read_group(s, j)
        cs = cs.strip()
        out += s[i:m.start()] + f"\\let{cs}\\relax\\newcommand{{{cs}}}{{\\operatorname{m.group(1)}{{{body}}}}}"
        i = j
    return out + s[i:]


def parse_preamble(cid, pre):
    """(packages [(name, [options])], passed options {pkg: [opts]}, class options, tikz libraries, definitions text,
    global definitions, notes)."""
    pkgs, passed, cls_opts, libs, defs, gdefs, notes = [], collections.defaultdict(list), [], [], [], [], []
    unused = collections.Counter()
    for st in statements(pre):
        body = strip_comments(st).strip()
        m = CS.match(body)
        if not m:
            continue
        cmd = m.group(1)
        if cmd == "global":
            st = re.sub(r"^\s*\\global\s*", "", st, count=1)
            body = strip_comments(st).strip()
            m = CS.match(body)
            if not m:
                continue
            cmd = m.group(1)
        rest = body[m.end():]
        if cmd in PACKAGE_CMDS or cmd in CLASS_CMDS:
            j, opts = skip_ws(rest, 0), []
            if j < len(rest) and rest[j] == "[":
                o, j = read_group(rest, j, "[", "]")
                opts = options(o)
            j = skip_ws(rest, j)
            names, j = read_group(rest, j)
            if cmd in CLASS_CMDS:
                cls_opts = opts
            else:
                for n in options(names):
                    pkgs.append((n, opts))
            if rest[j:].strip():
                notes.append(f"{cid}: text after \\{cmd} kept as a definition: {rest[j:].strip()[:60]}")
                defs.append(rest[j:])
        elif cmd in PASS_CMDS:
            j = skip_ws(rest, 0)
            o, j = read_group(rest, j)
            j = skip_ws(rest, j)
            names, j = read_group(rest, j)
            for n in options(names):
                passed[n] += options(o)
        elif cmd in TIKZ_CMDS:
            libs += options(read_group(rest, skip_ws(rest, 0))[0])
        elif cmd in GLOBAL_DEFINE_CMDS:
            gdefs.append(st.strip())
        elif cmd in DEFINE_CMDS:
            defs.append(define(st))
        elif cmd in DROP_CMDS:
            unused[cmd] += 1
        else:
            notes.append(f"{cid}: preamble command \\{cmd} kept, local to the chunk")
            defs.append(define(st))
    if unused:
        notes.append(f"{cid}: preamble settings not used (the book sets its own layout): "
                     + ", ".join(f"\\{k}" + (f" x{n}" if n > 1 else "") for k, n in unused.items()))
    return pkgs, passed, cls_opts, libs, defs, gdefs, notes


TEXT_ONLY = re.compile(r"\$|\\\(|\\\[|\\par(?![A-Za-z])|\\marginpar|\\marginnote|\\begin\{|\\section|\\footnote")


def defined_macros(defs_text):
    """{macro name: (argument pattern, whether it can be set inside math)} for the macros of a chunk's definitions."""
    out = {}

    def group_at(j, open_="{", close="}"):
        j = skip_ws(defs_text, j)
        if defs_text.startswith(open_, j):
            try:
                return read_group(defs_text, j, open_, close)
            except ValueError:
                pass
        return None, j

    for m in re.finditer(r"\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?\s*"
                         r"(?:\{\s*\\([A-Za-z@]+)\s*\}|\\([A-Za-z@]+))", defs_text):
        n, j = group_at(m.end(), "[", "]")
        n = int(n.strip()) if n and n.strip().isdigit() else 0
        default, j = group_at(j, "[", "]")
        body, _ = group_at(j)
        pattern = ("o" + "m" * (n - 1)) if default is not None and n else "m" * n
        out[m.group(1) or m.group(2)] = (pattern, not TEXT_ONLY.search(body or ""))
    for m in re.finditer(r"\\(?:def|edef)\s*\\([A-Za-z@]+)((?:[^{\\]|\\(?![A-Za-z]))*)", defs_text):
        if m.group(1) not in out:
            body, _ = group_at(m.end())
            out[m.group(1)] = ("m" * m.group(2).count("#"), not TEXT_ONLY.search(body or ""))
    for m in re.finditer(r"\\let\s*\\([A-Za-z@]+)\s*=?\s*\\([A-Za-z@]+)", defs_text):
        if m.group(2) != "relax":
            out.setdefault(m.group(1), ("", True))
    for m in re.finditer(r"\\DeclareMathOperator\*?\s*\{?\s*\\([A-Za-z@]+)", defs_text):
        out[m.group(1)] = ("", True)
    return out


# ------------------------------------------------------------------------------------------------------------------
# A chunk: its text with the commentary set in, split at chapter boundaries.
SEPARATOR = "\n\\clearpage\n\\section*{Overview of these pages}\n"
MS = re.compile(r"\\msp(?:in)?\{(?:page\s*)?(\d+(?:bis|ter|quater|')?)\}")      # as kit/build_reader.py
BLOCK = re.compile(r"\\begin\{dcomment\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{dcomment\}", re.S)
MARK = re.compile(r"^% ---- from (\S+)[ \t]*$", re.M)
CREDIT = re.compile(r"GPT-6|OpenAI|ChatGPT|Anthropic|AI-produced|AI-written|AI-assisted")
READER_NOTE = re.compile(r"GPT-6|OpenAI|ChatGPT|Anthropic|AI-produced|AI-written|[Aa]nnotated reader|\breader\b|"
                         r"\battachment\b|\bpackage\b")
STRUCTURAL = re.compile(r"\\(?:begingroup|endgroup|selectlanguage\{\w+\}|begin\{otherlanguage\*?\}\{\w+\}|"
                        r"end\{otherlanguage\*?\})")


def chapter_of(part_file):
    """The chapter key of a transcription part file named in a '% ---- from' line."""
    if part_file.startswith("der1_"):
        return "I"
    m = re.match(r"Der-Ch([IVX]+?)(a|b|c|app)?-", part_file)
    if m:
        return m.group(1) + ("app" if m.group(2) == "app" else "")
    m = re.match(r"der-ch(\d+)_", part_file)
    if m:
        n = int(m.group(1))
        return ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV",
                "XVI", "XVII", "XVIII", "XIX"][n]
    return None


def spans(pattern, t):
    return [(m.start(), m.end()) for m in pattern.finditer(t)]


def inside(pos, sp):
    return any(a <= pos < b for a, b in sp)


def clean_body(cid, body, notes):
    """Remove what the chunk's own reader put around the text: title pages and page numbering of that reader, and its
    notes about the reader in English (credits, scope of the package); Grothendieck's text is untouched."""
    blocks = spans(BLOCK, body)
    out, i = [], 0
    pat = re.compile(r"\\begin\{titlepage\}.*?\\end\{titlepage\}|\\pagenumbering\{[^}]*\}|\\maketitle\b|"
                     r"\\tableofcontents\b|\\begin\{otherlanguage\}\{english\}.*?\\end\{otherlanguage\}", re.S)
    for m in pat.finditer(body):
        if inside(m.start(), blocks):
            continue
        g = m.group(0)
        if g.startswith("\\begin{otherlanguage}") and not READER_NOTE.search(g):
            continue
        flat = strip_comments(g)
        if len(re.findall(r"\\begin\{", flat)) != len(re.findall(r"\\end\{", flat)) or \
                flat.count("{") - flat.count("\\{") != flat.count("}") - flat.count("\\}"):
            notes.append(f"{cid}: WARNING reader front matter not removed (unbalanced): {flat[:80]!r}")
            continue
        out.append(body[i:m.start()])
        i = m.end()
        flat = re.sub(r"\s+", " ", g)[:90]
        notes.append(f"{cid}: not set (the chunk reader's own front matter): {flat!r}")
    out.append(body[i:])
    return "".join(out)


def skip_pages(cid, body, notes):
    """The body without the edition pages SKIP_PAGES[cid] (set from the other chunk of the overlap)."""
    if cid not in SKIP_PAGES:
        return body
    lo, hi = SKIP_PAGES[cid]
    first = re.search(r"\\printedpage\{%d\}" % lo, body)
    after = re.search(r"\\printedpage\{%d\}" % (hi + 1), body)
    if not first:
        notes.append(f"{cid}: WARNING edition page {lo} not found; overlap not cut")
        return body
    line = body.rfind("\n", 0, first.start()) + 1
    prev = body.rfind("\n", 0, max(line - 1, 0)) + 1
    start = prev if body[prev:line].startswith("% ---- from ") else line
    if after:
        last = body.rfind("\\printedpage{%d}" % hi, 0, after.start())
        froms = [m.start() for m in re.finditer(r"^% ---- from \S+[ \t]*$", body[last:after.start()], re.M)]
        end = last + froms[-1] if froms else body.rfind("\n", 0, after.start()) + 1
    else:
        end = len(body)
    cut = body[start:end]
    flat = strip_comments(cut)
    bad = [b for b in BLOCK.finditer(body) if b.start() < start < b.end() or b.start() < end < b.end()]
    envs = collections.Counter(re.findall(r"\\begin\{([^}]*)\}", flat))
    envs.subtract(collections.Counter(re.findall(r"\\end\{([^}]*)\}", flat)))
    if bad or any(envs.values()) or flat.count("{") - flat.count("\\{") != flat.count("}") - flat.count("\\}"):
        notes.append(f"{cid}: WARNING the cut at edition pages {lo}-{hi} is not clean; overlap not cut")
        return body
    ms = MS.findall(cut)
    notes.append(f"{cid}: edition pages {lo}-{hi} (ms. {ms[0] if ms else '?'}-{ms[-1] if ms else '?'}) not set: "
                 f"the book sets them from the other chunk of the overlap ({len(BLOCK.findall(cut))} blocks of this "
                 f"chunk there, carried over in its source)")
    return body[:start] + body[end:]


def clean_overview(cid, text, notes):
    """Drop the credit lines of a chunk's overview (the book's credits page gives the credits); structural lines of such
    a paragraph (groups, language switches) are kept."""
    paras = re.split(r"(\n[ \t]*\n)", text)
    for k in range(0, len(paras), 2):
        p = paras[k]
        lines = p.split("\n")
        live = "\n".join(l for l in lines if not l.lstrip().startswith("%"))
        if not CREDIT.search(live):
            continue
        keep = [l for l in lines if STRUCTURAL.fullmatch(l.strip()) or l.lstrip().startswith("%")]
        dropped = "\n".join(l for l in lines if l not in keep)
        flat = strip_comments(dropped)
        if (flat.count("{") - flat.count("\\{")) != (flat.count("}") - flat.count("\\}")) or \
                re.search(r"\\(?:begin|end)\{|\\(?:begin|end)group", flat):
            notes.append(f"{cid}: WARNING a credit line of the overview could not be separated and is kept: "
                         f"{flat.strip()[:80]!r}")
            continue
        paras[k] = "\n".join(keep)
        flat = re.sub(r"\s+", " ", flat).strip()[:90]
        notes.append(f"{cid}: overview credit line not set (the credits page gives the credits): {flat!r}")
    return "".join(paras)


def qualify_labels(cid, t):
    t = re.sub(r"\\label\{([^}]*)\}", lambda m: f"\\label{{{cid}:{m.group(1)}}}", t)
    t = re.sub(r"\\(ref|eqref|pageref|autoref|nameref|vref|cref|Cref|labelcref)(\*?)\{([^}]*)\}",
               lambda m: f"\\{m.group(1)}{m.group(2)}{{" + ",".join(f"{cid}:{x.strip()}" for x in m.group(3).split(","))
               + "}", t)
    t = re.sub(r"\\hyperref\[([^\]]*)\]", lambda m: f"\\hyperref[{cid}:{m.group(1)}]", t)
    t = re.sub(r"\\(hyperlink|hypertarget)\{([^}]*)\}", lambda m: f"\\{m.group(1)}{{{cid}:{m.group(2)}}}", t)
    return t


def ms_range(t):
    labels = MS.findall(t)
    return (labels[0], labels[-1]) if labels else None


def ms_tex(label):
    return label.replace("'", "\\texorpdfstring{$'$}{′}")


def split_pieces(cid, body, expected, notes):
    """[(chapter key, text)] in order: the body cut where the transcription's part files change chapter. A block set in
    a later chapter than its anchor (the anchor on the last page of a chapter) is moved to the end of its chapter."""
    marks = [(m.start(), chapter_of(m.group(1))) for m in MARK.finditer(body)]
    cuts = []
    for pos, ch in marks:
        if ch is None:
            continue
        if not cuts or cuts[-1][1] != ch:
            cuts.append((pos, ch))
    found = [ch for _, ch in cuts]
    if found != expected:
        if len(expected) == 1 or not found:
            if found and found != expected:
                notes.append(f"{cid}: WARNING part files name chapters {found}, expected {expected}; set as one piece")
            return [(expected[0], body)]
        notes.append(f"{cid}: WARNING part files name chapters {found}, expected {expected}")
    cuts[0] = (0, cuts[0][1])
    pieces = [[ch, body[a:b]] for (a, ch), (b, _) in zip(cuts, cuts[1:] + [(len(body), None)])]
    if len(pieces) > 1:   # a block whose anchor lies only in an earlier piece goes back to the end of that piece
        for k in range(1, len(pieces)):
            for b in list(BLOCK.finditer(pieces[k][1])):
                m = re.fullmatch(r"p(\d+(?:bis|ter|quater|')?)(?::(.+))?", b.group(2).strip(), re.S)
                if not m:
                    continue
                n, words = m.group(1), m.group(2)
                homes = [j for j, (_, t) in enumerate(pieces)
                         if (words and words.strip() in BLOCK.sub("", t)) or (not words and n in MS.findall(t))]
                if k in homes or len(homes) != 1 or homes[0] > k:
                    continue
                home = homes[0]
                pieces[k][1] = pieces[k][1].replace(b.group(0), "", 1)
                pieces[home][1] = pieces[home][1].rstrip() + "\n\n" + b.group(0) + "\n"
                notes.append(f"{cid}: block {b.group(3)!r} moved back to chapter {pieces[home][0]}, where its anchor is")
    return [tuple(p) for p in pieces]


# ------------------------------------------------------------------------------------------------------------------
# Plain text for PDF bookmarks, and table cells (CSV statements) made safe for LaTeX.
UNI = {  # Unicode symbol -> LaTeX math
    "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "δ": r"\delta", "ε": r"\varepsilon", "ϵ": r"\epsilon",
    "ζ": r"\zeta", "η": r"\eta", "θ": r"\theta", "ϑ": r"\vartheta", "ι": r"\iota", "κ": r"\kappa", "λ": r"\lambda",
    "μ": r"\mu", "ν": r"\nu", "ξ": r"\xi", "π": r"\pi", "ϖ": r"\varpi", "ρ": r"\rho", "ϱ": r"\varrho", "σ": r"\sigma",
    "ς": r"\varsigma", "τ": r"\tau", "υ": r"\upsilon", "φ": r"\varphi", "ϕ": r"\phi", "χ": r"\chi", "ψ": r"\psi",
    "ω": r"\omega", "Γ": r"\Gamma", "Δ": r"\Delta", "Θ": r"\Theta", "Λ": r"\Lambda", "Ξ": r"\Xi", "Π": r"\Pi",
    "Σ": r"\Sigma", "Υ": r"\Upsilon", "Φ": r"\Phi", "Ψ": r"\Psi", "Ω": r"\Omega",
    "→": r"\to", "←": r"\leftarrow", "↔": r"\leftrightarrow", "⇒": r"\Rightarrow", "⇐": r"\Leftarrow",
    "⇔": r"\Leftrightarrow", "↦": r"\mapsto", "↪": r"\hookrightarrow", "↩": r"\hookleftarrow",
    "⇉": r"\rightrightarrows", "⇇": r"\leftleftarrows", "⇄": r"\rightleftarrows", "⇆": r"\leftrightarrows",
    "↠": r"\twoheadrightarrow", "⟶": r"\longrightarrow", "⟵": r"\longleftarrow", "⟹": r"\Longrightarrow",
    "⟸": r"\Longleftarrow", "⟺": r"\Longleftrightarrow", "⟼": r"\longmapsto", "↑": r"\uparrow", "↓": r"\downarrow",
    "⇝": r"\rightsquigarrow", "↝": r"\rightsquigarrow", "⇢": r"\dashrightarrow",
    "≃": r"\simeq", "≅": r"\cong", "≈": r"\approx", "∼": r"\sim", "≡": r"\equiv", "≠": r"\neq", "≤": r"\leq",
    "≥": r"\geq", "⩽": r"\leqslant", "⩾": r"\geqslant", "≪": r"\ll", "≫": r"\gg", "≺": r"\prec", "≻": r"\succ",
    "⪯": r"\preceq", "⪰": r"\succeq", "∈": r"\in", "∉": r"\notin", "∋": r"\ni", "⊂": r"\subset", "⊃": r"\supset",
    "⊆": r"\subseteq", "⊇": r"\supseteq", "⊊": r"\subsetneq", "⊋": r"\supsetneq", "⊄": r"\not\subset",
    "∩": r"\cap", "∪": r"\cup", "⊔": r"\sqcup", "∐": r"\amalg", "⨿": r"\amalg", "∏": r"\prod", "∑": r"\sum", "∘": r"\circ",
    "⋅": r"\cdot", "∙": r"\bullet", "∗": r"\ast", "⋆": r"\star", "∞": r"\infty", "∅": r"\emptyset",
    "∀": r"\forall", "∃": r"\exists", "∄": r"\nexists", "∧": r"\wedge", "∨": r"\vee", "⊗": r"\otimes",
    "⊕": r"\oplus", "⊠": r"\boxtimes", "∂": r"\partial", "∇": r"\nabla", "⊥": r"\perp", "⊤": r"\top",
    "⊢": r"\vdash", "⊣": r"\dashv", "∖": r"\setminus", "∣": r"\mid", "∥": r"\parallel", "′": "'", "″": "''",
    "‴": "'''", "−": "-", "∓": r"\mp", "ℓ": r"\ell", "ℕ": r"\mathbb{N}", "ℤ": r"\mathbb{Z}", "ℚ": r"\mathbb{Q}",
    "ℝ": r"\mathbb{R}", "ℂ": r"\mathbb{C}", "∫": r"\int", "√": r"\surd", "⟨": r"\langle", "⟩": r"\rangle",
    "⌊": r"\lfloor", "⌋": r"\rfloor", "⌈": r"\lceil", "⌉": r"\rceil", "□": r"\square", "■": r"\blacksquare",
    "◇": r"\Diamond", "♮": r"\natural", "♯": r"\sharp", "♭": r"\flat", "ℵ": r"\aleph", "⋯": r"\cdots",
    "⋮": r"\vdots", "⋱": r"\ddots", "∠": r"\angle", "≔": r"\mathrel{:=}", "⊲": r"\lhd", "⊳": r"\rhd",
    "≀": r"\wr", "∝": r"\propto", "≲": r"\lesssim", "≳": r"\gtrsim", "↯": r"\lightning", "⊞": r"\boxplus",
    "⋉": r"\ltimes", "⋊": r"\rtimes", "∡": r"\measuredangle", "∮": r"\oint", "⊸": r"\multimap",
    "×": r"\times", "±": r"\pm", "·": r"\cdot", "¬": r"\neg", "÷": r"\div",
    "₀": "_0", "₁": "_1", "₂": "_2", "₃": "_3", "₄": "_4", "₅": "_5", "₆": "_6", "₇": "_7", "₈": "_8", "₉": "_9",
    "₊": "_+", "₋": "_-", "ₙ": "_n", "ᵢ": "_i", "ⱼ": "_j", "ₖ": "_k", "ₘ": "_m", "ₚ": "_p", "ₓ": "_x",
    "⁰": "^0", "¹": "^1", "²": "^2", "³": "^3", "⁴": "^4", "⁵": "^5", "⁶": "^6", "⁷": "^7", "⁸": "^8", "⁹": "^9",
    "⁺": "^+", "⁻": "^-", "ⁿ": "^n", "ᵒ": "^o", "ᵖ": "^p", "ᵢ": "_i",
}
TEXT_KEEP = set("×±·¬¹²³°§¶«»¿¡") | {chr(c) for c in range(0xC0, 0x250)} | set("–—‘’‚“”„†‡•…‹›€‰")
COMBINING = {"\u0304": r"\bar", "\u0305": r"\overline", "\u0303": r"\tilde", "\u0302": r"\hat", "\u0301": r"\acute",
             "\u0300": r"\grave", "\u0306": r"\breve", "\u030c": r"\check", "\u0307": r"\dot", "\u0308": r"\ddot",
             "\u20d7": r"\vec", "\u0332": r"\underline"}
MATH_ALPHA = (("BOLD SCRIPT", "mathcal"), ("SCRIPT", "mathcal"), ("BOLD FRAKTUR", "mathfrak"), ("FRAKTUR", "mathfrak"),
              ("DOUBLE-STRUCK", "mathbb"), ("BOLD ITALIC", "boldsymbol"), ("BOLD", "mathbf"),
              ("SANS-SERIF", "mathsf"), ("MONOSPACE", "mathtt"), ("ITALIC", ""))


def uni_math(ch):
    """LaTeX math for a Unicode symbol, or None."""
    if ch in UNI:
        return UNI[ch]
    if 0x1D400 <= ord(ch) <= 0x1D7FF:
        name = unicodedata.name(ch, "")
        m = re.search(r"(CAPITAL|SMALL) ([A-Z])$", name)
        if m:
            letter = m.group(2) if m.group(1) == "CAPITAL" else m.group(2).lower()
            for key, cmd in MATH_ALPHA:
                if key in name:
                    return f"\\{cmd}{{{letter}}}" if cmd else letter
    return None


TEXT_CMDS = {"emph", "textit", "textbf", "textsc", "textrm", "textsf", "texttt", "textup", "textsl", "textmd",
             "textnormal", "underline", "mbox", "S", "P", "dag", "ddag", "ldots", "dots", "textellipsis", "oe", "OE",
             "ae", "AE", "aa", "AA", "o", "O", "l", "L", "ss", "i", "j", "textbackslash", "textasciitilde",
             "textasciicircum", "textunderscore", "textbar", "textless", "textgreater", "textendash", "textemdash",
             "textquoteleft", "textquoteright", "textquotedblleft", "textquotedblright", "guillemotleft",
             "guillemotright", "og", "fg", "quad", "qquad", "enspace", "thinspace", "enskip", "nobreakspace", "u",
             "v", "H", "c", "d", "b", "t", "r", "k", "textdegree", "LaTeX", "TeX",
             "textperiodcentered", "textsuperscript", "textsubscript", "nobreak", "slash", "ours"}
CITE_CMDS = {"cite", "citet", "citep", "citealt", "citealp", "citeauthor", "citeyear", "citeyearpar", "Citet", "Citep"}
MATH_CMDS = {  # name: argument pattern ('m' mandatory, 'o' optional)
    **{g: "" for g in ("alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi "
                       "pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta "
                       "Lambda Xi Pi Sigma Upsilon Phi Psi Omega varGamma varDelta varTheta varLambda varXi varPi "
                       "varSigma varUpsilon varPhi varPsi varOmega").split()},
    **{a: "" for a in ("to gets leftarrow rightarrow Leftarrow Rightarrow leftrightarrow Leftrightarrow longrightarrow "
                       "longleftarrow Longrightarrow Longleftarrow longleftrightarrow Longleftrightarrow mapsto "
                       "longmapsto hookrightarrow hookleftarrow rightrightarrows leftleftarrows rightleftarrows "
                       "leftrightarrows twoheadrightarrow twoheadleftarrow rightarrowtail leftarrowtail uparrow "
                       "downarrow Uparrow Downarrow nearrow searrow swarrow nwarrow iff implies impliedby "
                       "rightsquigarrow leadsto dashrightarrow dashleftarrow circlearrowleft circlearrowright "
                       "curvearrowright curvearrowleft upharpoonright leftharpoonup rightharpoonup").split()},
    **{r: "" for r in ("simeq cong approx sim equiv neq ne leq le geq ge leqslant geqslant ll gg prec succ preceq "
                       "succeq in notin ni subset supset subseteq supseteq subsetneq supsetneq nsubseteq cap cup "
                       "bigcap bigcup sqcup bigsqcup amalg coprod prod sum times otimes oplus bigotimes bigoplus "
                       "boxtimes circ cdot cdots ldots vdots ddots bullet star ast infty emptyset varnothing forall "
                       "exists nexists neg lnot wedge vee land lor setminus backslash partial nabla prime dagger perp "
                       "vdash dashv models mid nmid parallel ell hbar Re Im aleph top bot angle triangle square Box "
                       "Diamond lozenge blacksquare natural sharp flat colon lim liminf limsup varinjlim varprojlim "
                       "sup inf max min det dim ker deg hom log exp sin cos injlim projlim wr pm mp div propto "
                       "lesssim gtrsim lhd rhd unlhd unrhd triangleleft triangleright vartriangleleft "
                       "vartriangleright lbrace rbrace langle rangle lfloor rfloor lceil rceil vert Vert quad qquad "
                       "int oint surd multimap ltimes rtimes smile frown simeq circledast odot ominus oslash "
                       "lightning measuredangle boxplus not neq lneq gneq nsim ncong").split()},
    **{f: "m" for f in ("mathrm mathit mathbf mathsf mathtt mathcal mathscr mathbb mathfrak boldsymbol text "
                        "bar overline underline tilde widetilde hat widehat check breve dot ddot vec acute grave "
                        "underbrace overbrace substack mathring").split()},
    "operatorname": "m", "ensuremath": "m", "frac": "mm", "dfrac": "mm", "tfrac": "mm", "binom": "mm", "overset": "mm",
    "underset": "mm", "stackrel": "mm", "sqrt": "om", "xrightarrow": "om", "xleftarrow": "om",
}
MATH_ONLY = {"left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl", "Bigr", "middle", "limits",
             "nolimits", "displaystyle", "textstyle", "scriptstyle", "mathop", "mathrel", "mathbin", "mathord",
             "phantom", "hphantom", "vphantom", "smash", "joinrel", "relbar", "lhook", "rhook", "mathclap", "cdotp",
             "lbrack", "rbrack", "overrightarrow", "overleftarrow", "underrightarrow", "xmapsto", "mathstrut",
             "scriptscriptstyle", "nonscript", "mkern", "mskip", "kern", "hskip", "Bbbk", "imath", "jmath",
             "ulcorner", "urcorner", "llcorner", "lrcorner", "uplus", "bigvee", "bigwedge", "bigodot", "bigcirc",
             "diamond", "bowtie", "Join", "colim", "operatorname", "mathstrut", "text", "mbox", "hbox",
             "rm", "bf", "it", "sf", "tt", "cal", "mit", "sl", "em", "quad", "qquad", "prime"}


def pdf_text(s):
    """A plain-text form of a LaTeX string, for PDF bookmarks."""
    inverse = {v.lstrip("\\"): k for k, v in UNI.items() if v.startswith("\\") and v[1:].isalpha()}
    s = re.sub(r"\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}", r"\2", s)
    s = re.sub(r"\\([A-Za-z]+)\s*", lambda m: inverse.get(m.group(1), " " if m.group(1) in ("quad", "qquad") else ""), s)
    s = s.replace("--", "–").replace("~", " ")
    s = re.sub(r"\\.", "", s)
    s = re.sub(r"[{}$^_]", "", s)
    return re.sub(r"\s+", " ", s).strip() or "?"


def find_math_end(s, i):
    """The index after the math segment starting at s[i] ($, $$, \\( or \\[), or None if it is not closed."""
    if s.startswith("$$", i):
        j = s.find("$$", i + 2)
        return None if j < 0 else j + 2
    if s[i] == "$":
        j = i + 1
        while j < len(s):
            if s[j] == "\\":
                j += 2
                continue
            if s[j] == "$":
                return j + 1
            j += 1
        return None
    close = "\\)" if s.startswith("\\(", i) else "\\]"
    j = s.find(close, i + 2)
    return None if j < 0 else j + 2


def take_args(s, j, pattern):
    """The arguments of a command following s[j]: (raw argument text, new index)."""
    start = j
    for p in pattern:
        k = skip_ws(s, j)
        if p == "o":
            if k < len(s) and s[k] == "[":
                _, j = read_group(s, k, "[", "]")
            continue
        if k >= len(s):
            break
        if s[k] == "{":
            try:
                _, j = read_group(s, k)
            except ValueError:
                break
        elif s[k] == "\\":
            m = CS.match(s, k)
            j = m.end() if m else min(len(s), k + 2)
        else:
            j = k + 1
    return s[start:j], j


class Cell:
    """Typesets a CSV cell (LaTeX allowed, but often plain text with _ ^ and Unicode symbols) without errors."""

    def __init__(self, macros, bibkeys, report):
        self.macros, self.bibkeys, self.report = macros, bibkeys, report

    def math(self, seg):
        """A math segment, delimiters included, as inline math."""
        if seg.startswith("$$"):
            inner = seg[2:-2]
        elif seg.startswith("$"):
            inner = seg[1:-1]
        else:
            inner = seg[2:-2]
        out, i = [], 0
        while i < len(inner):
            c = inner[i]
            if c == "\\":
                m = CS.match(inner, i)
                if not m:
                    out.append(" " if inner.startswith("\\\\", i) else inner[i:i + 2])
                    i += 2
                    continue
                name = m.group(1)
                if name in MATH_CMDS or name in MATH_ONLY or name in self.macros or name in TEXT_CMDS:
                    out.append(m.group(0))
                else:
                    self.report[f"unknown math command \\{name}"] += 1
                    out.append(f"\\backslash\\mathrm{{{name}}}")
                i = m.end()
                continue
            if c in "#%&":
                out.append("\\" + c)
            elif ord(c) > 127:
                if c in COMBINING:
                    out.append("")       # combining marks inside math: dropped (rare)
                else:
                    u = uni_math(c)
                    if u is None:
                        self.report[f"unmapped character {c!r} in math"] += 1
                        out.append(c)
                    else:
                        out.append(u + (" " if re.search(r"\\[A-Za-z]+$", u) else ""))
            else:
                out.append(c)
            i += 1
        inner = "".join(out)
        for sign in ("^", "_"):        # a double superscript (subscript) such as c^{\prime}^{\prime}: one group
            pat = re.compile(re.escape(sign) + r"\{([^{}]*)\}\s*" + re.escape(sign) + r"\{([^{}]*)\}")
            while pat.search(inner):
                inner = pat.sub(lambda m: f"{sign}{{{m.group(1)}{m.group(2)}}}", inner)
        flat = re.sub(r"\\.", "", inner)
        if flat.count("{") != flat.count("}"):
            self.report["math segment with unbalanced braces set as text"] += 1
            return self.text(inner.replace("$", ""), plain=True)
        return "$" + inner + "$"

    def text(self, s, plain=False):
        s = unicodedata.normalize("NFC", s).replace("\u00a0", "~")
        out, i, stack, prev = [], 0, [], "other"
        while i < len(s):
            c = s[i]
            if not plain and (c == "$" or s.startswith("\\(", i) or s.startswith("\\[", i)):
                end = find_math_end(s, i)
                if end is not None:
                    out.append(self.math(s[i:end]))
                    i, prev = end, "other"
                    continue
                out.append("\\$" if c == "$" else "\\textbackslash{}")
                i += 1
                prev = "other"
                continue
            if c == "\\" and not plain:
                if s.startswith("\\\\", i):
                    out.append("\\textbackslash{}")
                    i += 2
                    prev = "other"
                    continue
                m = CS.match(s, i)
                if not m:
                    nxt = s[i + 1:i + 2]
                    if nxt in "{}_&%$#,;:! '`^\"~=.-":
                        out.append(s[i:i + 2])
                        i += 2
                        prev = "cmd" if nxt in "'`^\"~=." else "other"
                    else:
                        out.append("\\textbackslash{}")
                        i += 1
                        prev = "other"
                    continue
                name = m.group(1)
                if name in CITE_CMDS:
                    args, j = take_args(s, m.end(), "oom")
                    keys = re.search(r"\{([^}]*)\}\s*$", args)
                    if keys and all(k.strip() in self.bibkeys for k in keys.group(1).split(",")):
                        out.append(m.group(0) + args)
                    else:
                        self.report["citation of a key not in the bibliography set as text"] += 1
                        out.append("[" + self.text((keys.group(1) if keys else ""), plain=True) + "]")
                    i, prev = j, "other"
                    continue
                if name in TEXT_CMDS:
                    out.append(m.group(0))
                    i, prev = m.end(), "cmd"
                    continue
                if name in MATH_CMDS or name in self.macros:
                    pattern, mathok = self.macros.get(name) or (MATH_CMDS[name], True)
                    args, j = take_args(s, m.end(), pattern)
                    if not mathok:                       # a text macro of the chunk: as it is
                        out.append(m.group(0) + args)
                    else:
                        math = self.math("$" + m.group(0) + args + "$")
                        out.append("\\ensuremath{" + math[1:-1] + "}" if math.startswith("$") else math)
                    i, prev = j, "other"
                    continue
                self.report[f"unknown command \\{name} set as text"] += 1
                out.append("\\textbackslash{}" + name)
                i, prev = m.end(), "other"
                continue
            if c == "{":
                kind = "arg" if (not plain and (prev in ("cmd", "argclose") or s.startswith("{\\", i))) else "lit"
                stack.append(kind)
                out.append("{" if kind == "arg" else "\\{")
                i += 1
                prev = "other"
                continue
            if c == "}":
                kind = stack.pop() if stack else "lit"
                out.append("}" if kind == "arg" else "\\}")
                i += 1
                prev = "argclose" if kind == "arg" else "other"
                continue
            if c in " \t\n":
                out.append(c)
                i += 1
                continue
            prev = "other"
            if c == "_":
                out.append("\\_")
            elif c == "^":
                out.append("\\textasciicircum{}")
            elif c in "&%#":
                out.append("\\" + c)
            elif c == "$":
                out.append("\\$")
            elif c == "\\":
                out.append("\\textbackslash{}")
            elif c == "~" and plain:
                out.append("\\textasciitilde{}")
            elif ord(c) > 127 and c not in TEXT_KEEP:
                if c in COMBINING and out:
                    base = out.pop()
                    out.append(f"\\ensuremath{{{COMBINING[c]}{{{base}}}}}")
                else:
                    u = uni_math(c)
                    if u is None:
                        self.report[f"unmapped character {c!r}"] += 1
                        out.append(c)
                    else:
                        out.append(f"\\ensuremath{{{u}}}")
            else:
                out.append(c)
            i += 1
        out += ["}" for k in stack if k == "arg"]
        return "".join(out)


# ------------------------------------------------------------------------------------------------------------------
# Bibliography: the chunks' .bib files merged.
BIBENTRY = re.compile(r"^[ \t]*@(\w+)\s*([{(])", re.M)


def bib_entries(text):
    """[(type, key, full entry text)] of a .bib file."""
    out = []
    for m in BIBENTRY.finditer(text):
        typ = m.group(1).lower()
        try:
            body, end = read_group(text, m.end() - 1, m.group(2), "}" if m.group(2) == "{" else ")")
        except ValueError:
            continue
        key = body.split(",", 1)[0].strip() if typ not in ("string", "preamble", "comment") else ""
        out.append((typ, key, text[m.start():end].strip()))
    return out


def bib_fields(entry):
    body = entry[entry.index(",") + 1:] if "," in entry else ""
    out, i, n = {}, 0, len(body)
    field = re.compile(r"\s*,?\s*([A-Za-z][\w:-]*)\s*=\s*")
    while i < n:
        m = field.match(body, i)
        if not m:
            break
        name, i = m.group(1).lower(), m.end()
        if i < n and body[i] == "{":
            val, i = read_group(body, i)
        elif i < n and body[i] == '"':
            j = body.index('"', i + 1)
            val, i = body[i + 1:j], j + 1
        else:
            m2 = re.compile(r"[^,}\s]+").match(body, i)
            if not m2:
                break
            val, i = m2.group(0), m2.end()
        out[name] = re.sub(r"\s+", " ", val).strip()
    return out


def merge_bibs(chunk_bibs):
    """One bibliography; returns (text, keys, messages)."""
    first, order, strings, messages = {}, [], {}, []
    note_only, differs = collections.defaultdict(list), collections.defaultdict(list)
    for cid, text in chunk_bibs:
        for typ, key, entry in bib_entries(text):
            if typ == "comment":
                continue
            if typ in ("string", "preamble"):
                strings.setdefault(entry, cid)
                continue
            k = key.lower()
            if k not in first:
                first[k] = (cid, key, typ, entry)
                order.append(k)
                continue
            fcid, fkey, ftyp, fentry = first[k]
            if key != fkey:
                messages.append(f"bibliography: key {key} ({cid}) differs in case from {fkey} ({fcid}); {fkey} kept")
            a, b = bib_fields(fentry), bib_fields(entry)
            diff = sorted(f for f in (set(a) | set(b)) - {"note"} if a.get(f) != b.get(f))
            if ftyp != typ:
                diff.insert(0, f"type {ftyp}/{typ}")
            if diff:
                differs[fkey].append(f"{cid[4:]} ({', '.join(diff)})")
            elif a.get("note") != b.get("note"):
                note_only[fkey].append(cid)
    for key, where in differs.items():
        messages.append(f"bibliography: WARNING {key}: entry kept from {first[key.lower()][0][4:]}; it differs in "
                        f"{'; '.join(where)}")
    if note_only:
        messages.append(f"bibliography: {len(note_only)} further keys recur with only their verification note "
                        f"different (the first chunk's note is kept)")
    text = "\n\n".join(list(strings) + [first[k][3] for k in order]) + "\n"
    return text, {first[k][1] for k in order}, messages


# ------------------------------------------------------------------------------------------------------------------
# The book.
PREAMBLE_MACROS = r"""
\frenchsetup{AutoSpacePunctuation=false}
\setlength{\emergencystretch}{2em}
\hypersetup{pdftitle={Les Dérivateurs: an integrated reader, with commentary},pdfauthor={Alexander Grothendieck},
  colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue!45!black,pdfdisplaydoctitle=true}
\makeatletter
% counters as in the chunks' own readers (article class): equations by chunk, with unique PDF anchors
\newcounter{dgrchunk}
\renewcommand{\theequation}{\arabic{equation}}
\renewcommand{\thesection}{\arabic{section}}
\renewcommand{\thefigure}{\arabic{figure}}
\renewcommand{\thetable}{\arabic{table}}
\renewcommand{\theHequation}{\arabic{dgrchunk}.\arabic{equation}}
\renewcommand{\theHsection}{\arabic{dgrchunk}.\arabic{section}}
\renewcommand{\theHfigure}{\arabic{dgrchunk}.\arabic{figure}}
\renewcommand{\theHtable}{\arabic{dgrchunk}.\arabic{table}}
% running heads
\def\ps@dgr{\let\@mkboth\@gobbletwo
  \def\@oddhead{\footnotesize\scshape\rightmark\hfil\upshape\thepage}\let\@evenhead\@oddhead
  \def\@oddfoot{}\let\@evenfoot\@oddfoot}
\pagestyle{dgr}
% the contents: wider boxes for the chapter numerals, the labels of the parts and three-digit page numbers
\renewcommand*{\@pnumwidth}{2.2em}
\renewcommand*{\@tocrmarg}{3.2em}
\renewcommand*{\l@chapter}[2]{%
  \ifnum\c@tocdepth>\m@ne
    \addpenalty{-\@highpenalty}\vskip 1.0em \@plus\p@
    \setlength\@tempdima{3.8em}%
    \begingroup
      \parindent\z@ \rightskip\@pnumwidth \parfillskip -\@pnumwidth
      \leavevmode\bfseries \advance\leftskip\@tempdima \hskip -\leftskip
      #1\nobreak\hfil\nobreak\hb@xt@\@pnumwidth{\hss #2\kern-\p@\kern\p@}\par
      \penalty\@highpenalty
    \endgroup
  \fi}
\renewcommand*{\l@section}{\@dottedtocline{1}{1.5em}{4.6em}}
\renewcommand*{\l@subsection}{\@dottedtocline{2}{6.1em}{3.2em}}
% a chapter, or a part of one, that this book does not contain: a line of the contents without page number
\newcommand*{\dgrtocmissingchapter}[2]{%
  \addpenalty{-\@highpenalty}\vskip 1.0em \@plus\p@
  \begingroup\parindent\z@\leftskip 3.8em\rightskip\@tocrmarg plus 1fil\hskip-3.8em
  \hb@xt@ 3.8em{\bfseries #1\hfil}\textit{#2}\enspace\textendash\enspace\textit{not included}\par\endgroup}
\newcommand*{\dgrtocmissing}[2]{%
  \begingroup\parindent\z@\leftskip 6.1em\rightskip\@tocrmarg plus 1fil\hskip-4.6em
  \hb@xt@ 4.6em{#1\hfil}\textit{#2}\enspace\textendash\enspace\textit{not included}\par\endgroup}
% a chapter of the work: #1 numeral (contents), #2 heading line, #3 title; without numeral the contents keep the
% numeral's place empty, and the bookmark has no number
\DeclareRobustCommand{\dgrnonumber}{\numberline{}}
\pdfstringdefDisableCommands{\def\dgrnonumber{}}
\newcommand{\dgrchapter}[3]{%
  \clearpage\thispagestyle{plain}%
  \phantomsection
  \if\relax\detokenize{#1}\relax\addcontentsline{toc}{chapter}{\protect\dgrnonumber #3}%
  \else\addcontentsline{toc}{chapter}{\protect\numberline{#1}#3}\fi
  \markright{#2}%
  \begingroup\centering
    \vspace*{2\baselineskip}{\large\scshape #2\par}\bigskip{\LARGE\bfseries #3\par}\vspace{2\baselineskip}%
  \endgroup}
% a chunk (or its part in one chapter): #1 1 = on a new page, #2 label, #3 contents line, #4 heading, #5 running head
\newcommand{\dgrpart}[5]{%
  \ifnum#1=1 \clearpage\fi
  \phantomsection\addcontentsline{toc}{section}{\protect\numberline{#2}#3}%
  \markright{#5}%
  \par\begingroup\centering\sffamily\small #4\par\endgroup
  \smallskip\hrule\bigskip}
\newcommand{\dgroverview}[2]{%
  \clearpage
  \phantomsection\addcontentsline{toc}{subsection}{Overview}%
  \markright{#2}%
  \section*{Overview \textperiodcentered\ #1}}
\newcommand{\dgrblock}[2]{\pdfbookmark[2]{#2}{#1}}
% a chunk: its group, language and counters
\newcommand{\dgrchunkbegin}{\begingroup\stepcounter{dgrchunk}\selectlanguage{french}%
  \setcounter{footnote}{0}\setcounter{equation}{0}\setcounter{section}{0}\setcounter{figure}{0}\setcounter{table}{0}}
\newcommand{\dgrchunkend}{\par\endgroup}
% the back matter
\newcommand{\dgrbackchapter}[1]{\chapter*{#1}\phantomsection\addcontentsline{toc}{chapter}{#1}\markright{#1}}
\renewcommand{\bibsection}{\dgrbackchapter{\bibname}}
\newcommand{\dgrclaim}[4]{\par\noindent\hangindent=2.5em\hangafter=1
  \textbf{ms.~#2}\enspace\textsc{#1}\enspace{\footnotesize #3}\enspace\textendash\enspace#4\par\smallskip}
\makeatother
"""

TITLE_PAGE = r"""\begin{titlepage}
\centering
\vspace*{0.24\textheight}
{\Large Alexander Grothendieck\par}
\vspace{2.2em}
{\Huge\bfseries Les Dérivateurs\par}
\vspace{2.2em}
{\Large an integrated reader, with commentary\par}
\vfill
\end{titlepage}
\setcounter{page}{2}
\thispagestyle{empty}
\noindent The text is Alexander Grothendieck's, from the edition of \emph{Les Dérivateurs} by M.~Künzer,
J.~Malgoire and G.~Maltsiniotis (Universités de Montpellier~II et Paris~VII),
\url{https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html}. The \LaTeX{} transcription of that
edition is AI-transcribed (Claude Opus~5.5, Anthropic). The commentary, the register of claims and the corrections
are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checked and integrated by Claude (Anthropic).

\bigskip
\noindent\textbf{Rights}

\smallskip
\noindent The rights in the original work belong to its author or the author's representatives or heirs. Where we
hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the
public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we
do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will
take it down.

\smallskip
\begin{otherlanguage}{french}
\noindent Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Là
où nous détenons des droits, sur la transcription, la traduction, les corrections et la composition produites par IA,
ils sont dédiés au domaine public sous CC0 1.0. Cette édition est publiée à des fins pédagogiques et non lucratives, et
nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez
à sa publication ici, ouvrez une issue sur GitHub et nous la retirerons.
\end{otherlanguage}
\clearpage
"""


def tex_title(title):
    """A title with a plain-text form for the PDF bookmarks when it holds any TeX."""
    return f"\\texorpdfstring{{{title}}}{{{pdf_text(title)}}}" if re.search(r"[\\$^_{}~]", title) else title


def drop_nocite_all(cid, text, notes):
    """The book lists the whole merged bibliography once: a chunk's \\nocite{*} would repeat it (a BibTeX error)."""
    new, n = re.subn(r"\\nocite\{\s*\*\s*\}", "", text)
    if n:
        notes.append(f"{cid}: \\nocite{{*}} not repeated (the book lists the whole bibliography once)")
    return new


def drop_contents_lines(cid, text, notes):
    """The book writes its own contents and bookmarks: a chunk's \\addcontentsline, \\addtocontents or \\pdfbookmark
    is not used."""
    arg = r"\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\}"
    new, n = re.subn(r"(?:\\phantomsection\s*)?\\addcontentsline\s*" + arg + r"\s*" + arg + r"\s*" + arg +
                     r"|\\addtocontents\s*" + arg + r"\s*" + arg +
                     r"|\\pdfbookmark\s*(?:\[[^\]]*\])?\s*" + arg + r"\s*" + arg, "", text)
    if n:
        notes.append(f"{cid}: {n} contents line(s) or bookmark(s) of the chunk's own reader not used (the book writes "
                     f"its contents and bookmarks)")
    return new


def load_chunk(cid, notes):
    d = CHECKS / cid
    files = {k: d / f"{cid}_{k}" for k in ("reader.tex", "overview.tex", "references.bib", "claims.csv",
                                           "corrections.csv")}
    if not files["reader.tex"].exists():
        return None
    missing = [k for k, p in files.items() if not p.exists()]
    if missing:
        notes.append(f"{cid}: WARNING not included, missing {', '.join(missing)}")
        return None
    reader = files["reader.tex"].read_text(encoding="utf-8")
    if "\\begin{document}" not in reader or reader.count(SEPARATOR) != 1:
        notes.append(f"{cid}: WARNING not included, its reader does not have the form build_reader.py writes")
        return None
    pre, rest = reader.split("\\begin{document}", 1)
    body = rest.split(SEPARATOR, 1)[0]
    rows = lambda p: list(csv.DictReader(p.open(encoding="utf-8-sig", newline="")))
    return {"pre": pre, "body": body, "overview": files["overview.tex"].read_text(encoding="utf-8"),
            "bib": files["references.bib"].read_text(encoding="utf-8"), "claims": rows(files["claims.csv"]),
            "corrections": rows(files["corrections.csv"])}


def union_packages(chunks, notes):
    """The packages of all chunks, in order of first appearance, with their options united; options passed with
    \\PassOptionsToPackage; TikZ libraries; global definitions (preamble-only commands)."""
    pkg_opts, pkg_order, passed, libs, gdefs = {}, [], collections.defaultdict(list), [], []
    for cid, _ in CHUNKS:
        if cid not in chunks:
            continue
        c = chunks[cid]
        pkgs, pas, cls_opts, lb, defs, gd, nts = parse_preamble(cid, c["pre"])
        notes += nts
        c["leqno"] = "leqno" in cls_opts
        for o in cls_opts:
            if o not in ("leqno", "a4paper", "10pt", "11pt", "12pt", "oneside", "twoside", "final", "draft"):
                notes.append(f"{cid}: class option {o} not used")
        c["defs"] = defs
        for name, opts in pkgs:
            if name == "derivateurs_companion":
                continue
            if name not in pkg_opts:
                pkg_opts[name] = []
                pkg_order.append(name)
            for o in opts:
                if o in DROP_OPTIONS.get(name, ()) or name in BOOK_OPTIONS:
                    continue
                key = o.split("=", 1)[0].strip()
                same = [x for x in pkg_opts[name] if x.split("=", 1)[0].strip() == key]
                if same and o not in same:
                    notes.append(f"options: {name} [{o}] of {cid} clashes with [{same[0]}]; [{same[0]}] kept")
                elif o not in pkg_opts[name]:
                    pkg_opts[name].append(o)
        for p, os_ in pas.items():
            passed[p] += [o for o in os_ if o not in passed[p]]
        libs += [lib for lib in lb if lib not in libs]
        gdefs += [g for g in gd if g not in gdefs]
    return pkg_opts, pkg_order, passed, libs, gdefs


def global_preamble(pkg_opts, pkg_order, passed, libs, gdefs):
    langs = []
    for o in pkg_opts.get("babel", []) + ["english", "french"]:
        if "=" not in o and o not in langs:
            langs.append(o)
    langs = [lang for lang in langs if lang != "french"] + ["french"]     # the text is French: the main language
    hyper = HYPERREF_OPTIONS + [o for o in passed.pop("hyperref", []) + pkg_opts.get("hyperref", [])
                                if o not in HYPERREF_OPTIONS]
    pre = [f"\\PassOptionsToPackage{{{','.join(hyper)}}}{{hyperref}}", "\\documentclass[11pt,oneside]{book}"]
    for p, os_ in passed.items():
        pre.append(f"\\PassOptionsToPackage{{{','.join(os_)}}}{{{p}}}")
    for name in pkg_order:
        if name in KIT_PACKAGES:
            if pkg_opts[name] and name != "hyperref":
                pre.append(f"\\PassOptionsToPackage{{{','.join(pkg_opts[name])}}}{{{name}}}")
            continue
        if name == "babel":
            opts = [o for o in pkg_opts[name] if "=" in o] + langs
        else:
            opts = BOOK_OPTIONS.get(name, pkg_opts[name])
        pre.append(f"\\usepackage[{','.join(opts)}]{{{name}}}" if opts else f"\\usepackage{{{name}}}")
    if "babel" not in pkg_order:
        pre.append(f"\\usepackage[{','.join(langs)}]{{babel}}")
    if "geometry" not in pkg_order:
        pre.append(f"\\usepackage[{','.join(BOOK_OPTIONS['geometry'])}]{{geometry}}")
    pre += ["\\usepackage{booktabs}", "\\usepackage{derivateurs_companion}"]
    if libs:
        pre.append(f"\\usetikzlibrary{{{','.join(libs)}}}")
    return pre + gdefs + [PREAMBLE_MACROS.strip()]


def capital(s):
    return s[:1].upper() + s[1:]


def main():
    notes = []
    (OUT / "parts").mkdir(parents=True, exist_ok=True)
    known = {c for c, _ in CHUNKS}
    for d in sorted(CHECKS.glob("DER_*")):
        if d.is_dir() and d.name not in known:
            notes.append(f"{d.name}: not a chunk of the work, ignored")
    chunks = {}
    for cid, _ in CHUNKS:
        c = load_chunk(cid, notes)
        if c:
            chunks[cid] = c
    if not chunks:
        sys.exit("no checked chunk")
    present = [cid for cid, _ in CHUNKS if cid in chunks]
    pre = global_preamble(*union_packages(chunks, notes))
    bibtext, bibkeys, bibmsgs = merge_bibs([(cid, chunks[cid]["bib"]) for cid in present])
    (OUT / f"{NAME}.bib").write_text(bibtext, encoding="utf-8")

    # the sequence of the book: chapter headings, chunks, and contents lines for what is absent
    has_content = {ch: any(cid in chunks for cid, parts in CHUNKS for k, _ in parts if k == ch) for ch in CHAPTER_ORDER}
    state = {"current": None, "listed": set(), "blocks": 0, "fresh": False}

    def chapter_heading(ch):
        num, head, title = CHAPTER[ch]
        return f"\\dgrchapter{{{num}}}{{{head}}}{{{tex_title(title)}}}"

    def absent_chapters_up_to(ch, inclusive):
        """Contents lines for the chapters without any chunk, from the current chapter on, up to ch."""
        lines = []
        cur = state["current"]
        start = CHAPTER_ORDER.index(cur) + 1 if cur else 0
        stop = CHAPTER_ORDER.index(ch) + (1 if inclusive else 0)
        for k in CHAPTER_ORDER[start:stop]:
            if not has_content[k] and k not in state["listed"]:
                num, head, title = CHAPTER[k]
                lines.append(f"\\addtocontents{{toc}}{{\\protect\\dgrtocmissingchapter{{{num}}}{{{tex_title(title)}}}}}")
                state["listed"].add(k)
        return lines

    def enter(ch):
        """Lines that open chapter ch if it is not the current one."""
        if ch == state["current"]:
            return []
        lines = absent_chapters_up_to(ch, False) + [chapter_heading(ch)]
        state["current"], state["fresh"] = ch, True       # fresh: nothing set under the heading yet
        return lines

    def bookmark(m):
        state["blocks"] += 1
        return f"\\dgrblock{{dgrb{state['blocks']}}}{{{pdf_text(m.group(3))}}}\n{m.group(0)}"

    seq, summary, register_heads = [], [], {}
    for cid, parts in CHUNKS:
        label = cid[4:]
        descs = dict(parts)
        if cid not in chunks:
            for ch, desc in parts:
                if not has_content[ch]:
                    seq += absent_chapters_up_to(ch, True)
                    continue
                seq += enter(ch)
                seq.append(f"\\addtocontents{{toc}}{{\\protect\\dgrtocmissing{{{label}}}"
                           f"{{{capital(desc) if desc else 'The whole chapter'}}}}}")
            continue
        c = chunks[cid]
        body = qualify_labels(cid, skip_pages(cid, clean_body(cid, c["body"], notes), notes))
        overview = qualify_labels(cid, clean_overview(cid, c["overview"], notes))
        body, overview = (drop_contents_lines(cid, drop_nocite_all(cid, t, notes), notes) for t in (body, overview))
        pieces = split_pieces(cid, body, [ch for ch, _ in parts], notes)
        out = [f"% {cid}: Grothendieck's text with the commentary set in, then the overview, inside a group that "
               f"applies the chunk's own definitions"]
        heads = []
        for k, (ch, text) in enumerate(pieces):
            r = ms_range(text)
            rng = f"manuscript pages {ms_tex(r[0])}--{ms_tex(r[1])}" if r else "manuscript pages"
            desc = descs.get(ch, "")
            toc = f"{capital(desc)}, {rng}" if desc else capital(rng)
            dot = "\\enspace\\textperiodcentered\\enspace "
            head = f"{label}{dot}{CHAPTER[ch][1]}" + (f", {desc}" if desc else "") + f"{dot}{rng}"
            mark = f"{CHAPTER[ch][1]} \\textperiodcentered\\ \\textup{{{label}}}"
            opening = enter(ch)
            part = f"\\dgrpart{{{0 if state['fresh'] else 1}}}{{{label}}}{{{toc}}}{{{head}}}{{{mark}}}"
            state["fresh"] = False
            text = BLOCK.sub(bookmark, text).strip("\n")
            if k == 0:
                out += opening + [part, "\\dgrchunkbegin", f"\\input{{parts/{cid}_defs}}", text]
            else:
                out += opening + [part, text]
            heads.append(f"{CHAPTER[ch][1]}" + (f", {desc}" if desc else "") + f", {rng}")
        out += ["\\begin{otherlanguage}{english}",
                f"\\dgroverview{{{label}}}{{{CHAPTER[state['current']][1]} \\textperiodcentered\\ \\textup{{{label}}} "
                f"\\textperiodcentered\\ Overview}}", overview.strip("\n"), "\\end{otherlanguage}", "\\dgrchunkend", ""]
        defs = [f"% {cid}: the definitions of the chunk's preamble, applied inside its group"]
        if c["leqno"]:
            defs.append("\\csname tagsleft@true\\endcsname")
        defs += [d.rstrip() for d in c["defs"]]
        (OUT / "parts" / f"{cid}_defs.tex").write_text("\n".join(defs) + "\n", encoding="utf-8")
        (OUT / "parts" / f"{cid}.tex").write_text("\n".join(out), encoding="utf-8")
        seq.append(f"\\input{{parts/{cid}}}")
        c["macros"] = defined_macros("\n".join(c["defs"]))
        register_heads[cid] = "; ".join(heads)
        summary.append(f"{cid}: {len(pieces)} chapter piece(s), {len(BLOCK.findall(c['body']))} blocks, "
                       f"{len(c['claims'])} claims, {len(c['corrections'])} corrections, "
                       f"{len(bib_entries(c['bib']))} references")
    seq += absent_chapters_up_to(CHAPTER_ORDER[-1], True)

    back, cellreport = back_matter(chunks, present, register_heads, bibkeys, notes)
    doc = pre + ["\\begin{document}", "\\selectlanguage{english}", "\\frontmatter", TITLE_PAGE.strip(),
                 "\\tableofcontents", "\\mainmatter"] + seq + ["\\backmatter"] + back + \
          ["\\nocite{*}", "\\bibliographystyle{plainnat}", f"\\bibliography{{{NAME}}}", "\\end{document}", ""]
    (OUT / f"{NAME}.tex").write_text("\n".join(doc), encoding="utf-8")

    absent = [cid[4:] for cid, _ in CHUNKS if cid not in chunks]
    listed = sum(1 for c in present for r in chunks[c]["claims"] if (r.get("proof_status") or "").strip() in LISTED)
    print(f"{NAME}.tex: {len(present)} of {len(CHUNKS)} chunks ({', '.join(c[4:] for c in present)}); "
          f"absent: {', '.join(absent) or 'none'}")
    print("\n".join("  " + s for s in summary))
    print(f"  {sum(len(chunks[c]['claims']) for c in present)} claims, {listed} listed in the register; "
          f"{state['blocks']} commentary blocks; {len(bibkeys)} references in the merged bibliography")
    for n in notes + bibmsgs:
        print("  " + n)
    for k, n in sorted(cellreport.items()):
        print(f"  register cells: {k}: {n}")
    if "--pdf" in sys.argv:
        sys.exit(compile_pdf())


def back_matter(chunks, present, register_heads, bibkeys, notes):
    """The register of the claims and the counts of the corrections."""
    cellreport = collections.Counter()
    back = ["\\dgrbackchapter{Register of claims}",
            "The audit of each part records the definitions, axioms, propositions, claims, conjectures and questions "
            "of the text, each with the status the text gives it: proved, sketched, stated, assumed, conjectured, "
            "false (the assertion, or the inference as written, is false) or open. The table counts the entries of "
            "each part by status; the list after it gives every entry whose status is false, open or conjectured, "
            "with its manuscript page and its identifier in the audit.",
            "", "\\begin{center}\\small", "\\begin{tabular}{l" + "r" * (len(STATUSES) + 1) + "}", "\\toprule",
            "Part & " + " & ".join(STATUSES) + " & total \\\\", "\\midrule"]
    totals = collections.Counter()
    for cid in present:
        st = collections.Counter((r.get("proof_status") or "").strip() for r in chunks[cid]["claims"])
        other = sum(n for s, n in st.items() if s not in STATUSES)
        if other:
            notes.append(f"{cid}: WARNING {other} claims with a status outside {STATUSES}")
        totals.update(st)
        back.append(f"{cid[4:]} & " + " & ".join(str(st[s]) for s in STATUSES) + f" & {sum(st.values())} \\\\")
    back += ["\\midrule", "total & " + " & ".join(str(totals[s]) for s in STATUSES) + f" & {sum(totals.values())} \\\\",
             "\\bottomrule", "\\end{tabular}", "\\end{center}", ""]
    for cid in present:
        c = chunks[cid]
        listed = [r for r in c["claims"] if (r.get("proof_status") or "").strip() in LISTED]
        cell = Cell(c["macros"], bibkeys, cellreport)
        back += [f"\\section*{{{cid[4:]} \\textperiodcentered\\ {register_heads[cid]}}}",
                 f"\\pdfbookmark[1]{{{cid[4:]}}}{{dgrclaims.{cid[4:]}}}",
                 "\\begingroup\\raggedright", f"\\input{{parts/{cid}_defs}}"]
        if not listed:
            back.append("No entry is false, open or conjectured.")
        for r in listed:
            fields = [r["proof_status"].strip()] + [cell.text((r.get(f) or "").strip())
                                                     for f in ("ms_page", "id", "statement")]
            back.append("\\dgrclaim" + "".join(f"{{{x}}}" for x in fields))
        back += ["\\par\\endgroup", ""]
    back += ["\\dgrbackchapter{Transcription corrections}",
             "The corrections to the transcription, counted by kind for each part: readings of the transcription "
             "corrected against the edition (transcription), slips of the edition kept in the text with their "
             "intended reading recorded (edition slip kept), and doubtful readings settled against the edition "
             "(doubt resolved).", "", "\\begin{center}\\small",
             "\\begin{tabular}{l" + "r" * (len(CORRECTION_KINDS) + 1) + "}", "\\toprule",
             "Part & " + " & ".join(t for _, t in CORRECTION_KINDS) + " & total \\\\", "\\midrule"]
    ctot = collections.Counter()
    for cid in present:
        kc = collections.Counter((r.get("kind") or "").strip() for r in chunks[cid]["corrections"])
        other = sum(n for s, n in kc.items() if s not in dict(CORRECTION_KINDS))
        if other:
            notes.append(f"{cid}: WARNING {other} corrections of another kind")
        ctot.update(kc)
        back.append(f"{cid[4:]} & " + " & ".join(str(kc[k]) for k, _ in CORRECTION_KINDS) +
                    f" & {sum(kc.values())} \\\\")
    back += ["\\midrule", "total & " + " & ".join(str(ctot[k]) for k, _ in CORRECTION_KINDS) +
             f" & {sum(ctot.values())} \\\\", "\\bottomrule", "\\end{tabular}", "\\end{center}", ""]
    return back, cellreport


def compile_pdf():
    """LuaLaTeX, BibTeX, LuaLaTeX, LuaLaTeX; then LuaLaTeX again while the log asks for a rerun (the citations resolved
    in the third pass move page breaks after the contents were written), at most twice."""
    env = dict(os.environ, TEXINPUTS=f".{os.pathsep}{KIT}{os.pathsep}")
    latex = ["lualatex", "-interaction=nonstopmode", f"{NAME}.tex"]
    toc = OUT / f"{NAME}.toc"
    state = {"runs": 0, "toc_changed": False}

    def run(cmd):
        before = toc.read_bytes() if toc.exists() else b""
        subprocess.run(cmd, cwd=OUT, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if cmd is latex:
            state["runs"] += 1
            state["toc_changed"] = (toc.read_bytes() if toc.exists() else b"") != before

    for s in (latex, ["bibtex", NAME], latex, latex):
        run(s)
    rerun = re.compile(r"Rerun to get|may have changed\. Rerun|Rerun LaTeX")
    # the contents printed come from the previous pass: a pass that changed them (LaTeX does not warn) needs another
    while state["runs"] < 5 and (state["toc_changed"] or rerun.search(
            (OUT / f"{NAME}.log").read_text(encoding="utf-8", errors="replace").replace("\n", ""))):
        run(latex)
    runs = state["runs"]
    log = (OUT / f"{NAME}.log").read_text(encoding="utf-8", errors="replace")
    flat = log.replace("\n", "")          # the log wraps its lines; warnings are counted on the joined text
    blg = (OUT / f"{NAME}.blg").read_text(encoding="utf-8", errors="replace") if (OUT / f"{NAME}.blg").exists() else ""
    pages = re.search(r"Output written on .*?\((\d+) pages", flat)
    errors = re.findall(r"^! .*$", log, re.M)
    undefined = len(re.findall(r"(?:Reference|Citation) `[^']*' on page \S+ undefined", flat))
    multiply = len(re.findall(r"(?:Label|Citation) `[^']*' multiply defined", flat))
    missing = len(re.findall(r"Missing character", flat))
    overfull = len(re.findall(r"^Overfull \\hbox", log, re.M))
    bibwarn = len(re.findall(r"^Warning--", blg, re.M))
    biberr = re.search(r"\(There (?:was|were) (\d+) error", blg)
    settled = "settled" if not (rerun.search(flat) or state["toc_changed"]) else \
        "NOT settled (the contents or the log still ask for a rerun)"
    print(f"{NAME}.pdf: {pages.group(1) if pages else '?'} pages | LaTeX errors {len(errors)} | undefined references "
          f"{undefined} | multiply defined labels {multiply} | missing characters {missing} | overfull hboxes "
          f"{overfull} | BibTeX warnings {bibwarn}, errors {biberr.group(1) if biberr else 0} | {runs} LuaLaTeX runs, "
          f"cross-references {settled}")
    for e in errors[:40]:
        print("  " + e[:150])
    return 1 if errors or undefined or multiply or not pages else 0


if __name__ == "__main__":
    main()
