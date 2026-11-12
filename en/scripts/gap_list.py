"""Write the gap list of the completeness check of 12 Nov 2026: COMPLETENESS_20261112.csv.

One row per place:
  - every place that a fix of 12 Nov 2026 in checks/FIXES.jsonl changes (status "fixed"): the places are found by
    applying the unit's fixes in order to runs/out/<unit>.tex, as assemble.py does;
  - every place where French stays in the English on purpose, or where the source itself has a gap (status "stays"):
    the editors' gloss of AQT, the journal names of the bibliography, the words the editors could not read.
Columns: unit, edition_page (the edition's printed page), manuscript_page (the last manuscript page mark before the
place), kind, french, english_before, english_now, status, reason. The flags of completeness.py that are not gaps
(read by hand) are in checks/completeness/FLAGS.jsonl and are not repeated here.
usage: python -I -B gap_list.py
"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402
import assemble as A  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
DATE = "2026-11-12"
OUT = os.path.join(T.ROOT, "COMPLETENESS_20261112.csv")
FIXED = "fixed (checks/FIXES.jsonl, 12 Nov 2026)"
CMT = re.compile(r"(?<!\\)%[^\n]*")
HOT_FR = re.compile(r"(?<![A-Za-z\\])hot(?=-|\s+(?:é|e)quivalence)")


def flat(s):
    return re.sub(r"\s+", " ", s).strip()


def around(text, a, b, w=80):
    return flat(text[max(0, a - w):a] + text[a:b] + text[b:b + w])


def where(text, pos):
    before = T.english_anchors(text[:pos])
    p = re.findall(r"\\printedpage\{([^}]*)\}", before)
    m = re.findall(r"\\msp\{([^}]*)\}", before)
    return (p[-1] if p else ""), (m[-1] if m else "")


def places(fix, text):
    """[(start, end, replacement)] of a fix in text, as assemble.apply finds them."""
    if fix["kind"] == "replace":
        out, i = [], text.find(fix["old"])
        while i >= 0:
            out.append((i, i + len(fix["old"]), fix["new"]))
            i = text.find(fix["old"], i + len(fix["old"]))
        return out
    rx = re.compile(fix["pattern"])
    if fix.get("scope") != "prose":
        return [(m.start(), m.end(), m.expand(fix["repl"])) for m in rx.finditer(text)]
    out, i = [], 0
    segs = list(A.SEG.finditer(text)) + [None]
    for s in segs:
        j = s.start() if s else len(text)
        for m in rx.finditer(text, i, j):
            out.append((m.start(), m.end(), m.expand(fix["repl"])))
        i = s.end() if s else j
    return out


def french_body(unit):
    return T.body_text(T.read(os.path.join(T.ROOT, "source", unit + ".tex")).replace("\r\n", "\n"))


def english_body(unit, folder):
    return T.body_text(T.read(os.path.join(T.ROOT, "translation", folder, unit + ".tex")).replace("\r\n", "\n"))


def nocomment_finditer(rx, text):
    """Matches of rx outside comments (the line break \\\\ read as two spaces, so that a word after it is found)."""
    masked = CMT.sub(lambda m: " " * len(m.group(0)), text).replace("\\\\", "  ")
    return list(rx.finditer(masked))


FR_KEYS = {  # the French of the places of the other fixes: a string to find in the French unit
    "\\textit{0-connexe}": "\\textit{0-connexe}",
    "W(7 bis) or W(7 bis faible) on": "W(7 bis faible)",
    "``On the derived categories of abelian categories''": "Des catégories dérivées",
    "``Theory of Topoi and Étale Cohomology of Schemes''": "Théorie des Topos",
    "baseline=(\\tikzcdmatrixname-2-1.base)]\nT_0 \\arrow[rr]": "baseline=(\\tikzcdmatrixname-2-1.base)]",
    "(and even an imm-": "(et même une imm-",
    "open ersion of Dwyer), and $p_f \\in W$.": "ersion ouverte de Dwyer)",
}
KINDS = {
    "hot": "capital Hot- for the French lower-case hot-",
    "0-connexe": "French word left in a formula",
    "7 bis faible": "French word left in a footnote",
    "Des catégories": "title of a published work translated",
    "Théorie des Topos": "title of a published work translated",
    "tikzcdmatrixname": "LaTeX error in a diagram (no text missing)",
    "imm-": "word cut by the edition's hyphen at a page end, rendered as a broken word",
    "ersion of Dwyer": "word cut by the edition's hyphen at a page end, rendered as a broken word",
}


def kind_of(fix):
    key = fix.get("old", "") + fix.get("pattern", "")
    for k, v in KINDS.items():
        if k.lower() in key.lower() or (k == "hot" and "Hot" in key):
            return v
    for k, v in KINDS.items():
        if k in fix.get("new", ""):
            return v
    return "other"


def fixed_rows():
    rows = []
    fx = A.fixes()
    um = T.unit_map()
    for unit in dict.fromkeys(f["unit"] for f in fx if f.get("date") == DATE):
        mine = [f for f in fx if f["unit"] == unit]
        k = next(i for i, f in enumerate(mine) if f.get("date") == DATE)
        text = A.apply(unit, T.read(os.path.join(T.ROOT, "runs", "out", unit + ".tex")), mine[:k])
        fr = french_body(unit)
        hot_rows, seen = [], {}
        for f in mine[k:]:
            for a, b, new in places(f, text):
                page, ms = where(text, a)
                kind = kind_of(f)
                row = {"unit": unit, "edition_page": page, "manuscript_page": ms, "kind": kind, "french": "",
                       "english_before": around(text, a, b), "english_now": flat(text[max(0, a - 80):a] + new +
                                                                                  text[b:b + 80]),
                       "status": FIXED, "reason": f["reason"], "_pos": a}
                if kind.startswith("capital Hot"):
                    hot_rows.append(row)
                else:
                    key = next((v for o, v in FR_KEYS.items() if o in f.get("old", "") or f.get("old", "") in o), "")
                    i = fr.find(key) if key else -1
                    for _ in range(seen.get(key, 0)):  # the k-th place of the same fix: the k-th in the French
                        i = fr.find(key, i + 1) if i >= 0 else -1
                    seen[key] = seen.get(key, 0) + 1
                    row["french"] = around(fr, i, i + len(key)) if i >= 0 else ""
                rows.append(row)
            text = A.apply(unit, text, [f])
        if hot_rows:
            frm = nocomment_finditer(HOT_FR, fr)
            hot_rows.sort(key=lambda r: r["_pos"])
            if len(frm) == len(hot_rows):
                for r, m in zip(hot_rows, frm):
                    r["french"] = around(fr, m.start(), m.end())
            else:
                raise SystemExit("%s: %d French hot-, %d places fixed" % (unit, len(frm), len(hot_rows)))
    for r in rows:
        r.pop("_pos")
        r["unit_order"] = list(um).index(r["unit"])
    return rows


def stays_rows():
    rows = []
    um = T.unit_map()
    specs = [
        (re.compile(r"\[âne qui trotte\]"), re.compile(r"\[âne qui trotte: at a donkey's trot, i\.e\. by routine "
                                                        r"verification\]"),
         "editors' gloss kept in French",
         "AQT is Grothendieck's abbreviation of 'âne qui trotte'; the editors' gloss gives the French words, which the "
         "English keeps with their sense (glossary entry 'AQT, âne qui trotte': the abbreviation is his, the gloss "
         "the editors')"),
        (re.compile(r"\[(?:mots?\(?s?\)? illisibles?(?:\(s\))?|ou \$X_a\$, indice illisible)\]"),
         re.compile(r"\[(?:illegible words?(?:\(s\))?|or \$X_a\$, illegible subscript)\]"),
         "illegible in the source",
         "the editors could not read the manuscript here and say so in their note; the note is translated, the word "
         "itself is lost in the source"),
    ]
    for un in T.units():
        fr = french_body(un["id"])
        en = english_body(un["id"], un["folder"])
        for rf, re_, kind, reason in specs:
            mf, me = nocomment_finditer(rf, fr), nocomment_finditer(re_, en)
            if len(mf) != len(me):
                raise SystemExit("%s: %s: %d French, %d English" % (un["id"], kind, len(mf), len(me)))
            for a, b in zip(mf, me):
                page, ms = where(en, b.start())
                snip = around(en, b.start(), b.end())
                rows.append({"unit": un["id"], "edition_page": page, "manuscript_page": ms, "kind": kind,
                             "french": around(fr, a.start(), a.end()), "english_before": snip, "english_now": snip,
                             "status": "stays", "reason": reason, "unit_order": list(um).index(un["id"])})
    u = "Der-ChXIII-25-01-04_p066-066"
    fr, en = french_body(u), english_body(u, "Der-ChXIII-25-01-04")
    for name in ("Cahiers de Topologie et Géométrie Différentielle", "Astérisque"):
        i, j = fr.find(name), en.find(name)
        page, ms = where(en, j)
        snip = around(en, j, j + len(name))
        rows.append({"unit": u, "edition_page": page, "manuscript_page": ms, "kind": "journal name kept in French",
                     "french": around(fr, i, i + len(name)), "english_before": snip, "english_now": snip,
                     "status": "stays", "reason": "bibliography: the name of a journal or series is not translated",
                     "unit_order": list(um).index(u)})
    return rows


def main():
    rows = fixed_rows() + stays_rows()
    rows.sort(key=lambda r: (r["unit_order"], r["status"] != FIXED))
    cols = ["unit", "edition_page", "manuscript_page", "kind", "french", "english_before", "english_now", "status",
            "reason"]
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    from collections import Counter
    print("%s: %d rows" % (os.path.basename(OUT), len(rows)))
    for (k, s), n in sorted(Counter((r["kind"], r["status"]) for r in rows).items()):
        print("  %3d  %-45s %s" % (n, k, s))


if __name__ == "__main__":
    main()
