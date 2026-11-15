"""How well does completeness.py find an omission? (12 Nov 2026)

Deletes one sentence, or one clause between commas, at a random place of a copy of a random English unit, runs the
completeness check on that unit and counts whether a new flag appears. Two kinds of trial:
  sentence: a whole sentence of 25-400 characters (capital to full stop) is deleted;
  clause:   a clause of 20-200 characters between two commas is deleted.
Lines with a comment are not used. The units themselves are not changed: the copies go to TMP and are removed.
usage: python -I -B completeness_validation.py TMP [SEED ...]
Writes checks/completeness/VALIDATION.json.
"""
import importlib.util
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
_spec = importlib.util.spec_from_file_location("completeness", os.path.join(T.HERE, "completeness.py"))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
NL = "\n"


def trials(seed, mode, tmp, units, P, n=150):
    random.seed(seed)
    res = []
    for _ in range(n):
        un = random.choice(units)
        p = os.path.join(T.ROOT, "translation", un["folder"], un["id"] + ".tex")
        s = T.read(p).replace("\r\n", "\n")
        pre, body = s.split(T.BD, 1)
        if mode == "sentence":
            cands = list(re.finditer(r"(?<=[.!?] )[A-Z][^.!?$\\{}%\n]{25,400}[.!?](?= )", body))
        else:
            cands = list(re.finditer(r"(?<=, )[a-z][^.!?$\\{}%\n,;]{20,200},(?= )", body))
        cands = [m for m in cands if "%" not in body[body.rfind(NL, 0, m.start()) + 1:body.find(NL, m.end())]]
        if not cands:
            continue
        m = random.choice(cands)
        d = os.path.join(tmp, un["folder"])
        os.makedirs(d, exist_ok=True)
        q = os.path.join(d, un["id"] + ".tex")
        T.write(q, pre + T.BD + body[:m.start()] + body[m.end() + 1:])
        u = M.check_unit(un["id"], un["folder"], tmp, P)
        base = M.check_unit(un["id"], un["folder"], os.path.join(T.ROOT, "translation"), P)
        new = [f for f in u.flags if f not in base.flags]
        res.append({"unit": un["id"], "chars": len(m.group(0)), "flagged": bool(new),
                    "by": [f["kind"] for f in new][:3], "deleted": m.group(0)[:120]})
        os.remove(q)
    return res


def main(argv):
    tmp, seeds = argv[0], [int(x) for x in argv[1:]] or [1, 2]
    units = T.units()
    P = M.calibrate(units, os.path.join(T.ROOT, "translation"))
    out = {"seeds": seeds, "modes": {}}
    for mode in ("sentence", "clause"):
        res = []
        for seed in seeds:
            res += trials(seed, mode, tmp, units, P)
        by_len = {}
        for L in (20, 30, 60, 100):
            sub = [r for r in res if r["chars"] >= L]
            by_len[">=%d" % L] = [sum(r["flagged"] for r in sub), len(sub)]
        out["modes"][mode] = {"trials": len(res), "flagged": sum(r["flagged"] for r in res), "by_length": by_len,
                              "missed": [r for r in res if not r["flagged"]]}
        print("%s: %d of %d flagged; %s" % (mode, out["modes"][mode]["flagged"], len(res), by_len))
    T.write(os.path.join(M.OUT, "VALIDATION.json"), json.dumps(out, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
