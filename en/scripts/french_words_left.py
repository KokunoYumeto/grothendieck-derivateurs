"""Words of the English units that are French and not English (12 Nov 2026).

Every word of the English running text, of its footnotes, editors' notes and the text boxes of its formulas
(check_units.text_runs) is looked up in the word lists of pyspellchecker: a word known in French and unknown in English
is listed with its places, the French around it and the English. The list is read by hand: a French word left in the
English is a gap; titles, names, quotations and notation kept on purpose are not.

usage: python -I -B french_words_left.py [--en DIR]
Writes checks/completeness/FRENCH_WORDS.json.
"""
import collections
import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402
from spellchecker import SpellChecker  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
_spec = importlib.util.spec_from_file_location("completeness", os.path.join(T.HERE, "completeness.py"))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
C, K = M.C, M.K

EN_WORDS = SpellChecker(language="en")
FR_WORDS = SpellChecker(language="fr")
WORD = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+(?:['’][A-Za-zÀ-ÖØ-öø-ÿœŒ]+)?")


def texts(en):
    """The English running text with its footnotes and notes (prose), and the wording of its formulas' text boxes."""
    yield C.prose(C.strip_comments(en))
    for x in K.text_runs(en):
        yield re.sub(r"\\[A-Za-z]+\*?|[{}$]", " ", x)


def main(argv):
    en_dir = os.path.join(T.ROOT, "translation")
    if argv[:1] == ["--en"]:
        en_dir = argv[1]
    found = collections.defaultdict(list)
    for un in T.units():
        u = M.Unit(un["id"], un["folder"], en_dir)
        for t in texts(u.en):
            for m in WORD.finditer(t):
                w = m.group(0)
                lw = w.lower().replace("’", "'")
                parts = lw.split("'")
                if len(lw) < 3 and len(parts) == 1:
                    continue
                if lw in EN_WORDS or all(p in EN_WORDS for p in parts if p):
                    continue
                if lw in FR_WORDS or (len(parts) == 2 and parts[0] in ("l", "d", "qu", "j", "n", "c", "s")):
                    found[lw].append({"unit": un["id"], "context": t[max(0, m.start() - 80):m.end() + 80]})
    out = {w: {"count": len(v), "places": v[:6]} for w, v in sorted(found.items(), key=lambda kv: -len(kv[1]))}
    os.makedirs(M.OUT, exist_ok=True)
    T.write(os.path.join(M.OUT, "FRENCH_WORDS.json"), json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    for w, v in out.items():
        print("%-22s %4d  %s | %s" % (w, v["count"], v["places"][0]["unit"], v["places"][0]["context"].replace("\n", " ")[:150]))


if __name__ == "__main__":
    main(sys.argv[1:])
