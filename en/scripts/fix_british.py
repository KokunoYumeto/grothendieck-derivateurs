"""Add a fix to checks/FIXES.jsonl for each British spelling that the checks of the raw output found (the glossary
decided American spelling). One fix per distinct word and unit: the word, bounded, outside formulas and comments,
replaced by its American form; "count" is the number of its places. A unit that already has British-spelling fixes is
left alone. Reads checks/CHECKS_raw.json (check_units.py --raw).
usage: python -I -B fix_british.py [UNIT ...]
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402
import assemble as A  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
WORDS = {"centre": "center", "centres": "centers", "fibre": "fiber", "fibres": "fibers", "fibred": "fibered",
         "neighbourhood": "neighborhood", "neighbourhoods": "neighborhoods", "colour": "color", "colours": "colors",
         "behaviour": "behavior", "analyse": "analyze", "analysed": "analyzed", "analysing": "analyzing"}
REASON = "British spelling; the glossary decided American spelling (his English)"


def american(w):
    lw = w.lower()
    if lw in WORDS:
        a = WORDS[lw]
    elif re.search(r"isations?$", lw):
        a = re.sub(r"isation(s?)$", r"ization\1", lw)
    elif lw.endswith("ising"):
        a = lw[:-5] + "izing"
    else:
        a = re.sub(r"^(realis|generalis|recognis|characteris|localis|normalis|organis|arithmetis|discretis|rigidis)",
                   lambda m: m.group(1)[:-1] + "z", lw)
    if a == lw:
        return None
    return a[0].upper() + a[1:] if w[0].isupper() else a


def main():
    want = sys.argv[1:]
    raw = json.loads(T.read(os.path.join(T.ROOT, "checks", "CHECKS_raw.json")))
    have = {(f["unit"], f.get("reason")) for f in A.fixes()}
    rows = []
    for u, r in raw.items():
        if want and u not in want:
            continue
        words = sorted(set(r["glossary"]["british_spellings"]))
        if not words or (u, REASON) in have:
            continue
        text = T.read(os.path.join(T.ROOT, "runs", "out", u + ".tex"))
        for w in words:
            a = american(w)
            if not a:
                print("%s: no American form for %r (left for review)" % (u, w))
                continue
            pat = r"\b%s\b" % re.escape(w)
            _, n = A.sub_prose(pat, a, text)
            rows.append({"unit": u, "kind": "regex", "pattern": pat, "repl": a, "count": n, "scope": "prose",
                         "reason": REASON, "by": "script (fix_british.py)",
                         "date": datetime.now(timezone.utc).isoformat(timespec="seconds")})
            print("%s: %s -> %s (%d)" % (u, w, a, n))
    if rows:
        with open(A.FIXES, "a", encoding="utf-8") as f:
            for x in rows:
                f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("%d fixes added" % len(rows))


if __name__ == "__main__":
    main()
