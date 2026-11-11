"""Figures of the run for the README: batches and costs (runs/RUNS.jsonl), check results of the raw output and of the
English units (checks/CHECKS_raw.json, checks/CHECKS.json), fixes (checks/FIXES.jsonl), waivers (checks/WAIVERS.jsonl),
re-runs. Writes checks/REPORT.md and prints it.

Pages are counted from the units whose answer has text: a request that Flex refused ("server_is_overloaded", nothing
billed) translated nothing, and its unit went into a later batch.
usage: python -I -B report.py
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def load(p):
    p = os.path.join(T.ROOT, p)
    return json.loads(T.read(p)) if os.path.exists(p) else {}


def jsonl(p):
    p = os.path.join(T.ROOT, p)
    return [json.loads(x) for x in T.read(p).splitlines() if x.strip()] if os.path.exists(p) else []


def main():
    runs = jsonl(os.path.join("runs", "RUNS.jsonl"))
    done = [r for r in runs if r["event"] == "done"]
    man = json.loads(T.read(os.path.join(T.ROOT, "source", "MANIFEST.json")))["units"]
    L = ["# Run report", "", "## Batches (GPT-6.1 Sol, reasoning effort max, OpenAI Responses API, Flex tier)", "",
         "| batch | requests | translated | refused by Flex | edition pages translated | tokens in | "
         "tokens out (reasoning) | billed (Flex) | $ per page | minutes |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    tin = tout = treas = 0
    billed = 0.0
    pages = 0
    for r in done:
        ok = [q for q in r["requests"] if q["text_chars"]]
        pg = sum(man[q["unit"]]["pages"] for q in ok)
        refused = sum(1 for fa in r.get("failed_attempts", []) if (fa.get("error") or {}).get("code") ==
                      "server_is_overloaded") + sum(1 for q in r["requests"] if not q["text_chars"])
        L.append("| %s | %d | %d | %d | %d | %s | %s (%s) | $%.4f | $%.4f | %.1f |" % (
            r["batch"], len(r["requests"]), len(ok), refused, pg, format(r["input_tokens"], ","),
            format(r["output_tokens"], ","), format(r["reasoning_tokens"], ","), r["billed_usd"],
            r["billed_usd"] / pg if pg else 0, r["wall_minutes"]))
        tin += r["input_tokens"]
        tout += r["output_tokens"]
        treas += r["reasoning_tokens"]
        billed += r["billed_usd"]
        pages += pg
    L.append("| all | %d | %d | | %d | %s | %s (%s) | $%.4f | $%.4f | |" % (
        sum(len(r["requests"]) for r in done), sum(1 for r in done for q in r["requests"] if q["text_chars"]), pages,
        format(tin, ","), format(tout, ","), format(treas, ","), billed, billed / pages if pages else 0))
    have = collections.Counter(q["unit"] for r in done for q in r["requests"] if q["text_chars"])
    rr = {u: n - 1 for u, n in have.items() if n > 1}
    todo = [u for u in man if u not in have]
    L += ["", "Edition pages translated (each unit counted once): %d of %d; units %d of %d; units translated twice "
              "(re-run after a check): %d%s; not translated: %d%s." % (
                  sum(man[u]["pages"] for u in have), sum(v["pages"] for v in man.values()), len(have), len(man),
                  sum(rr.values()), (" (%s)" % ", ".join(sorted(rr))) if rr else "", len(todo),
                  (" (%s)" % ", ".join(todo)) if todo else ""),
          "",
          "Cost per page: the dollars billed in all (refused requests cost nothing; an answer that was replaced still "
          "counts) over the pages translated. List price (no Flex discount) is twice the billed figure: $%.4f." % (
              2 * billed)]
    raw, fin = load(os.path.join("checks", "CHECKS_raw.json")), load(os.path.join("checks", "CHECKS.json"))
    for title, ck in (("raw output, as it came back", raw), ("English units (raw output plus fixes)", fin)):
        if not ck:
            continue
        cats = collections.Counter()
        for r in ck.values():
            for f in r["fail"]:
                cats[re.sub(r"[:(].*", "", f).strip()] += 1
        npass = sum(1 for r in ck.values() if r["verdict"] == "PASS")
        L += ["", "## Checks of the %s" % title, "",
              "%d units checked: %d pass, %d fail." % (len(ck), npass, len(ck) - npass)]
        L += ["- %s: %d units" % kv for kv in cats.most_common()]
        fo = sum(r["formulas"]["french"] for r in ck.values())
        fi = sum(r["formulas"]["identical"] + r["formulas"]["spacing_only"] for r in ck.values())
        ft = sum(len(r["formulas"].get("text_only", [])) for r in ck.values())
        fm = sum(len(r["formulas"].get("moved", [])) for r in ck.values())
        gp = sum(r["glossary"]["present"] for r in ck.values())
        ge = sum(r["glossary"]["entry_pages"] for r in ck.values())
        L += ["- formulas identical (or up to spacing): %d of %d; changed only in the wording of text-mode boxes: %d; "
              "moved: %d; glossary entry-pages with the English form: %d of %d" % (fi, fo, ft, fm, gp, ge)]
    fx = jsonl(os.path.join("checks", "FIXES.jsonl"))
    if fx:
        L += ["", "## Fixes (checks/FIXES.jsonl)", "", "%d fixes in %d units:" % (len(fx), len({f["unit"] for f in fx}))]
        L += ["- %s: %s" % (f["unit"], f["reason"]) for f in fx]
    wv = jsonl(os.path.join("checks", "WAIVERS.jsonl"))
    if wv:
        L += ["", "## Waivers (checks/WAIVERS.jsonl: a check that misfired on a correct translation)", "",
              "%d waivers in %d units:" % (len(wv), len({w["unit"] for w in wv}))]
        L += ["- %s, %s: %s" % (w["unit"], ("glossary entry '%s', page %s" % (w["entry"], w["page"])) if "entry" in w
                                else (w.get("fail") or w.get("fail_prefix")), w["reason"]) for w in wv]
    out = "\n".join(L) + "\n"
    T.write(os.path.join(T.ROOT, "checks", "REPORT.md"), out)
    print(out)


if __name__ == "__main__":
    main()
