"""Write the English units: translation/<folder>/<unit>.tex, each a complete LaTeX document like its French.

An English unit is the French file's preamble, with babel's main language English (\\usepackage[french]{babel}
becomes \\usepackage[french,english]{babel}; French stays loaded for the \\frenchsetup lines of some preambles) and the
few macros that print French words in English (common_dt.MACRO_EN: \\pl prints "[rather", \\defeq and its variants
"def", \\cardred, \\red, \\redop "red"), and as its body the translation that came back (runs/out/<unit>.tex), with the fixes of checks/FIXES.jsonl for
that unit applied in order, and the page anchors whose argument is French in English (common_dt.ANCHOR_EN: "page 68
vide" becomes "page 68 blank"). Nothing else is changed.

checks/FIXES.jsonl, one fix per line:
  {"unit": U, "kind": "replace", "old": "...", "new": "...", "count": n, "reason": "...", "by": "...", "date": "..."}
  {"unit": U, "kind": "regex", "pattern": "...", "repl": "...", "count": n, "scope": "prose"|"all", ...}
"count" is the number of places the fix must find (the script stops if it finds another number); "scope": "prose"
applies a regex outside formulas and comment lines only.
usage: python -I -B assemble.py [UNIT ...]
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
FIXES = os.path.join(T.ROOT, "checks", "FIXES.jsonl")
BABEL_FR, BABEL_EN = "\\usepackage[french]{babel}", "\\usepackage[french,english]{babel}"
SEG = re.compile(r"(?<!\\)%[^\n]*|\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\begin\{(" +
                 T.GC.MATH_ENVS + r")\}.*?\\end\{\1\}", re.S)


def fixes():
    if not os.path.exists(FIXES):
        return []
    return [json.loads(x) for x in T.read(FIXES).splitlines() if x.strip()]


def sub_prose(pattern, repl, text):
    """re.subn outside formulas and comments."""
    out, i, n = [], 0, 0
    for m in SEG.finditer(text):
        s, k = re.subn(pattern, repl, text[i:m.start()])
        out += [s, m.group(0)]
        n += k
        i = m.end()
    s, k = re.subn(pattern, repl, text[i:])
    out.append(s)
    return "".join(out), n + k


def apply(unit, text, fx):
    for f in fx:
        if f["kind"] == "replace":
            n = text.count(f["old"])
            if n != f.get("count", 1):
                raise SystemExit("%s: fix finds %d places, not %d: %r" % (unit, n, f.get("count", 1), f["old"][:80]))
            text = text.replace(f["old"], f["new"])
        elif f["kind"] == "regex":
            if f.get("scope") == "prose":
                text, n = sub_prose(f["pattern"], f["repl"], text)
            else:
                text, n = re.subn(f["pattern"], f["repl"], text)
            if n != f["count"]:
                raise SystemExit("%s: fix finds %d places, not %d: %r" % (unit, n, f["count"], f["pattern"]))
        else:
            raise SystemExit("unknown fix kind %r" % f["kind"])
    return text


def english_doc(unit, body):
    pre = T.split_doc(T.read(os.path.join(T.ROOT, "source", unit + ".tex")))[0]
    try:
        pre = T.english_preamble(pre)
    except ValueError as e:
        raise SystemExit("%s: %s" % (unit, e))
    left = [ln for ln in pre.split("\n") if T.DEFLINE.match(ln) and re.search(r"déf|plutôt|réd|r\\acute\{e\}d", ln)]
    if left:
        raise SystemExit("%s: a macro still prints French: %s" % (unit, left[0][:120]))
    return pre + T.BD + "\n\n" + body.strip("\n") + "\n\n" + T.ED + "\n"


def main():
    want = sys.argv[1:]
    fx = fixes()
    n = nf = 0
    for u in T.units():
        if want and u["id"] not in want:
            continue
        raw = os.path.join(T.ROOT, "runs", "out", u["id"] + ".tex")
        if not os.path.exists(raw):
            continue
        mine = [f for f in fx if f["unit"] == u["id"]]
        body = T.english_anchors(apply(u["id"], T.read(raw), mine))
        T.write(os.path.join(T.ROOT, "translation", u["folder"], u["id"] + ".tex"), english_doc(u["id"], body))
        n += 1
        nf += len(mine)
    print("%d English units written (%d fixes applied)" % (n, nf))


if __name__ == "__main__":
    main()
