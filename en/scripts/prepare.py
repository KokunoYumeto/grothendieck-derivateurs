"""Copy the French of every unit and render its prompt (no API call).

For each five-page file of the transcription (the source of record: derivateurs_publish_20261111/repo/transcription,
release v2026-11-11b, commit f42cfdd), writes, inside derivateurs_translation_20261111 only:
  source/<unit>.tex            the file, byte for byte
  source/MANIFEST.json         per unit: its path in the repository, sha256, pages, the request line, the terms
  prompt/system/<unit>.txt     the system prompt: prompt/PROMPT_TEMPLATE.txt (the comparison's, byte for byte) with the
                               DER parts of prompt/PROMPT_PARTS_DER.txt, the slots filled for the unit
  prompt/user/<unit>.txt       the user message: the unit's macros used on its pages (for reference), the request line,
                               the text (the body of the file, between \\begin{document} and \\end{document})
Adapted from translation_comparison_20261111/scripts/prepare.py: the same template, the same parts and the same user
message; what the whole book needs beyond its five pages is listed in PROMPT_PARTS_DER.txt.
usage: python -I -B prepare.py
"""
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
P = os.path.join(T.ROOT, "prompt")
S = os.path.join(T.ROOT, "source")
TEMPLATE = T.read(os.path.join(P, "PROMPT_TEMPLATE.txt"))
MATH = re.compile(r"\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\begin\{(" + T.GC.MATH_ENVS +
                  r")\}.*?\\end\{\1\}", re.S)
# Text-carrying macros beyond the comparison's list, named in the prompt where the unit has them.
MORE_TEXT = ["\\footnotetext", "\\textsc", "\\textsf", "\\textup", "\\textmd", "\\textrm", "\\textsl", "\\emph",
             "\\underline", "\\mbox", "\\hbox", "\\fbox", "\\marginpar", "\\item"]
LABEL_RX = re.compile(r"\bDer ?\(?\d|\bDér ?\(?\d|\bLoc ?\(?\d|\bPS ?\d|\bW\(\d|\bL ?\d\b")
ABBR = ["fcg", "fcga", "LLP", "RLP"]
NUM = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}


def parts():
    """PROMPT_PARTS_DER.txt: sections headed '@@ DER <PLACEHOLDER>'; the text up to the next header fills it."""
    out, cur = {}, None
    for line in T.read(os.path.join(P, "PROMPT_PARTS_DER.txt")).split("\n"):
        m = re.match(r"@@ DER ([A-Z_]+)\s*$", line)
        if m:
            cur = out.setdefault(m.group(1), [])
            continue
        if cur is not None:
            cur.append(line)
    return {k: "\n".join(v).strip("\n") for k, v in out.items()}


PARTS = parts()


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def definitions(pre):
    """[(name, block)] of the preamble's macro definitions; a block runs over lines until its braces balance."""
    lines = pre.split("\n")
    out, i = [], 0
    head = re.compile(r"\s*\\(?:(?:re|provide)?newcommand\*?\s*\{?(\\[A-Za-z@]+)|DeclareMathOperator\*?\s*\{?"
                      r"(\\[A-Za-z@]+)|DeclareRobustCommand\*?\s*\{?(\\[A-Za-z@]+)|def\s*(\\[A-Za-z@]+)|"
                      r"let\s*(\\[A-Za-z@]+)|newsavebox\s*\{(\\[A-Za-z@]+)\}|sbox\s*\{?(\\[A-Za-z@]+)\}?)")
    while i < len(lines):
        m = head.match(lines[i])
        if not m:
            i += 1
            continue
        name = next(g for g in m.groups() if g)
        block, depth, j = [], 0, i
        while j < len(lines):
            ln = lines[j]
            block.append(ln)
            t = strip_comments(ln)
            depth += len(re.findall(r"(?<!\\)\{", t)) - len(re.findall(r"(?<!\\)\}", t))
            j += 1
            if depth <= 0:
                break
        out.append((name, "\n".join(block)))
        i = j
    return out


def used(name, text):
    return re.search(re.escape(name) + r"(?![A-Za-z@])", text) is not None


def macro_block(pre, body):
    defs = definitions(pre)
    keep = [(n, b) for n, b in defs if used(n, body)]
    names = {n for n, _ in keep}
    for n, b in defs:  # one level of dependency: a definition used by a kept one
        if n not in names and any(used(n, kb) for _, kb in keep):
            keep.append((n, b))
            names.add(n)
    order = {b: k for k, (_, b) in enumerate(defs)}
    return "\n".join(b for _, b in sorted(keep, key=lambda x: order[x[1]]))


def ranges(nums):
    nums = sorted(set(nums))
    out, a = [], None
    for k, n in enumerate(nums):
        if a is None:
            a = n
        if k + 1 == len(nums) or nums[k + 1] != n + 1:
            out.append(str(a) if a == n else "%d-%d" % (a, n))
            a = None
    return ", ".join(out)


def request_line(u, body):
    b = strip_comments(body)
    args = re.findall(r"\\printedpage\{([^}]*)\}", b)
    numbered = [int(a) for a in args if re.fullmatch(r"\d+", a.strip())]
    unnumbered = len(args) - len(numbered)
    bits = []
    if numbered:
        bits.append("edition page%s %s" % ("s" if len(numbered) > 1 else "", ranges(numbered)))
        if unnumbered:
            bits[-1] += " and %s unnumbered page%s" % (NUM.get(unnumbered, unnumbered), "s" if unnumbered > 1 else "")
    elif unnumbered:
        bits.append("%s unnumbered edition page%s" % (NUM.get(unnumbered, unnumbered), "s" if unnumbered > 1 else ""))
    ms = [int(x) for x in re.findall(r"\\msp\{(?:pages? )?(\d+)", b)]
    if ms:
        lo, hi = min(ms), max(ms)
        bits.append("manuscript page %d" % lo if lo == hi else "manuscript pages %d-%d" % (lo, hi))
    n = len(args)
    return ("Translate this LaTeX into English (Les Dérivateurs, %s, %s; %d page%s)."
            % (u["phrase"], ", ".join(bits), n, "s" if n != 1 else ""), n)


def quotes_line(body):
    b = strip_comments(body)
    forms = []
    if "\u201c" in b or "\u201d" in b:
        forms.append("\u201c...\u201d")
    if "\u2018" in b:
        forms.append("\u2018...\u2019")
    if re.search(r"(?<![`\\])`(?!`)", b):
        forms.append("`...'")
    if "\u00ab" in b:
        forms.append("\u00ab...\u00bb")
    if not forms:
        forms = ["\u201c...\u201d"]
    lst = forms[0] if len(forms) == 1 else ", ".join(forms[:-1]) + " and " + forms[-1]
    return "- Quotation marks %s are written ``...''." % lst


def system_prompt(u, body, hits):
    b = strip_comments(body)
    prose = MATH.sub(" ", b)
    more_text = [m for m in MORE_TEXT if used(m, b if m in ("\\mbox", "\\hbox", "\\textup", "\\textrm") else prose)]
    labels = LABEL_RX.findall(prose)
    abbr = [a for a in ABBR if re.search(r"\b%s\b" % a, prose)]
    tl = T.terms()
    term_lines = ["- " + tl[fr][0] for fr in hits] or ["- (none of the glossary's terms occur on these pages)"]
    sysp = TEMPLATE
    for k, v in PARTS.items():
        sysp = sysp.replace("{" + k + "}", v.rstrip("\n"))
    sysp = sysp.replace("{TERMS}", "\n".join(term_lines))
    sysp = sysp.replace("<<CHAPTER>>", u["phrase"])
    sysp = sysp.replace("<<MORE_TEXT_MACROS>>", "".join(", " + m for m in more_text))
    sysp = sysp.replace("<<MORE_ANCHORS>>", ", \\clearpage" if used("\\clearpage", b) else "")
    sysp = sysp.replace("<<QUOTES>>", quotes_line(body))
    lab = ""
    if labels:
        lab = "- Labels of axioms and conditions are names and stay as they are (Der 1, Loc (6 b), PS 2, W(4b))"
        lab += "; \"Dér\" is written \"Der\"." if any(x.startswith("Dér") for x in labels) else "."
    sysp = sysp.replace("\n<<LABELS>>", ("\n" + lab) if lab else "")
    sysp = sysp.replace("\n<<ABBREVIATIONS>>", ("\n- His abbreviations %s are kept as he writes them."
                                                % ", ".join(abbr)) if abbr else "")
    assert not re.search(r"\{[A-Z_]{4,}\}|<<|>>", sysp), "unfilled placeholder in " + u["id"]
    return sysp


def hits_of(body, macros):
    t = T.running_text(body, macros)
    out = []
    for fr, rx, en, src, note in T.glossary():
        if rx != "-" and re.search(rx, t, re.I):
            out.append(fr)
    return out


def main():
    os.makedirs(os.path.join(P, "system"), exist_ok=True)
    os.makedirs(os.path.join(P, "user"), exist_ok=True)
    os.makedirs(S, exist_ok=True)
    man = {"release": T.RELEASE, "commit": T.COMMIT, "repository": T.REPO, "units": {}}
    tot_pages = tot_chars = 0
    for u in T.units():
        raw = T.read(u["src"])
        pre, body = T.split_doc(raw)
        text = T.body_text(raw)
        hits = hits_of(text, T.macros_of(pre))
        line, npages = request_line(u, text)
        mb = macro_block(pre, text)
        user = ("The edition's macros used on these pages, for reference (do not translate or return them):\n" + mb +
                "\n\n" if mb else "") + line + "\n\n" + text
        sysp = system_prompt(u, text, hits)
        shutil.copyfile(u["src"], os.path.join(S, u["id"] + ".tex"))
        T.write(os.path.join(P, "system", u["id"] + ".txt"), sysp)
        T.write(os.path.join(P, "user", u["id"] + ".txt"), user)
        man["units"][u["id"]] = {"folder": u["folder"], "repo_path": os.path.relpath(u["src"], T.REPO).replace("\\", "/"),
                                 "sha256": T.sha256(u["src"]), "pages": npages, "chars_text": len(text),
                                 "request": line, "terms": hits, "system_chars": len(sysp), "user_chars": len(user)}
        tot_pages += npages
        tot_chars += len(text)
    T.write(os.path.join(S, "MANIFEST.json"), json.dumps(man, ensure_ascii=False, indent=1) + "\n")
    us = man["units"]
    print("%d units, %d edition pages, %d characters of text; terms per unit: min %d, median %d, max %d"
          % (len(us), tot_pages, tot_chars, min(len(v["terms"]) for v in us.values()),
             sorted(len(v["terms"]) for v in us.values())[len(us) // 2], max(len(v["terms"]) for v in us.values())))
    print("system prompt chars: min %d, max %d; user message chars: min %d, max %d" % (
        min(v["system_chars"] for v in us.values()), max(v["system_chars"] for v in us.values()),
        min(v["user_chars"] for v in us.values()), max(v["user_chars"] for v in us.values())))


if __name__ == "__main__":
    main()
