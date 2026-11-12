"""Which glossary, notation and typesetting entries occur in the two samples (prints; writes selection/HITS_<work>.json).
usage: python -I -B list_hits.py"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_tc as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def forms(spec):
    """'name := regex || name := regex' -> [(name, regex)]"""
    out = []
    for part in spec.split(" || "):
        if " := " in part:
            n, r = part.split(" := ", 1)
            out.append((n.strip(), r.strip()))
    return out


for work in ("LM", "DER"):
    s, a, z = T.cut(T.SAMPLES[work])
    raw = T.GC.expand(T.GC.strip_comments(s), T.der_macros() if work == "DER" else {})
    t = T.running_text(s, work)
    res = {"glossary": [], "notation": [], "typesetting": []}
    print("=" * 30, work, "lines %d-%d, %d chars" % (a, z, len(s)))
    for fr, rx, en, src, note in T.glossary(work):
        if rx == "-":
            continue
        ms = [m.group(0) for m in re.finditer(rx, t, re.I)]
        if ms:
            res["glossary"].append({"french": fr, "regex": rx, "english": en, "note": note, "found": ms})
            print("G  %-45s -> %-50s %s" % (fr, en[:50], sorted(set(x.lower() for x in ms))[:6]))
    for obj, spec, en, note in T.decision_lines("notation_%s.txt" % work):
        hits = {n: len(re.findall(r, raw)) for n, r in forms(spec)}
        hits = {k: v for k, v in hits.items() if v}
        if hits:
            res["notation"].append({"object": obj, "english": en, "note": note, "found": hits})
            print("N  %-45s -> %-40s %s" % (obj, en[:40], hits))
    for row in T.decision_lines("typesetting.txt"):
        if row[0] != work or len(row) < 5:
            continue
        _, wf, spec, uni, note = row[:5]
        if spec == "-":
            continue
        hits = {n: len(re.findall(r, raw)) for n, r in forms(spec)}
        hits = {k: v for k, v in hits.items() if v}
        if hits:
            res["typesetting"].append({"written_form": wf, "unified": uni, "note": note, "found": hits})
            print("T  %-45s -> %-40s %s" % (wf, uni[:40], hits))
    with open(os.path.join(T.ROOT, "selection", "HITS_%s.json" % work), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
