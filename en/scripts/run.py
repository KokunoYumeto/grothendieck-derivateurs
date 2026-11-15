"""Translate the units of Les Dérivateurs, one batch at a time (budget checked before each batch).

Model: GPT-6.1 Sol (gpt-6.1-sol), reasoning effort max, OpenAI Responses API, Flex tier (service_tier "flex"),
background mode, max_output_tokens 128,000, no tools; the prompt of prepare.py (prompt/system/<unit>.txt as the
instructions, prompt/user/<unit>.txt as the user message). The key is read only by enr_pilot.call
(enriques_api_pilot_20261106), from the user's note, at each call; it is never printed or stored.

Adapted from translation_comparison_20261111/scripts/run.py (its OpenAI part: the same request body, the same
price arithmetic, a row per run in the cost ledger). What scale changed:
  - a batch is a set of units submitted together and collected before the next batch is submitted;
  - before a batch: no other batch in flight; the units' files in the repository still have the sha256 of
    source/MANIFEST.json; the dollars billed so far plus the batch's worst case (estimated input at the input price
    plus 128,000 output tokens per request at the output price) stay within CAP (the user's stop line); and the
    measured cost per edition page so far is at most twice the comparison's (Sol max on its five DER pages);
  - each submitted response id is written at once to runs/state_<batch>.json, so that a stopped run can be collected;
  - network errors and Flex refusals are retried; a response that fails is resubmitted up to twice in its batch;
    since batch b04, a Flex "server_is_overloaded" refusal (nothing billed) is resubmitted up to 8 times, after 4, 8,
    16 and then 30 minutes, and a batch's "pages" are the pages translated ("pages_requested": all its pages).

usage (from scripts/):
  python -I -B run.py plan
  python -I -B run.py batch NAME --next N            the next N units (book order) without a translation
  python -I -B run.py batch NAME --units U1 U2 ...   these units (a unit already translated is re-run; its earlier
                                                     output goes to runs/out/attempts/)
  python -I -B run.py collect NAME                   wait for and collect a batch whose submitter stopped
"""
import json
import os
import shutil
import sys
import time
import urllib.error
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.join(T.ROOT, "runs")
OUT = os.path.join(R, "out")
RUNS = os.path.join(R, "RUNS.jsonl")
MODEL, EFFORT, TIER = "gpt-6.1-sol", "max", "flex"
NAME = "GPT-6.1 Sol, reasoning effort max, OpenAI Responses API, Flex tier"
MAX_OUT = 128000
PRICE = None  # billed per million tokens in/out at the Flex price; withheld from this public copy
LIST = None  # list price per million tokens; withheld from this public copy
CAP = None  # the user's stop line in dollars; the figure is withheld from this public copy
REF_PER_PAGE = None  # the comparison's cost per page (translation_comparison_20261111, sol61-max, DER); withheld from this public copy
FINAL = ("completed", "incomplete", "failed", "cancelled")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def manifest():
    return json.loads(T.read(os.path.join(T.ROOT, "source", "MANIFEST.json")))["units"]


def runs():
    if not os.path.exists(RUNS):
        return []
    return [json.loads(x) for x in T.read(RUNS).splitlines() if x.strip()]


def log_run(rec):
    os.makedirs(R, exist_ok=True)
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def spent():
    return sum(r["billed_usd"] for r in runs() if r["event"] == "done")


def in_flight():
    rs = runs()
    done = {r["batch"] for r in rs if r["event"] == "done"}
    return [r for r in rs if r["event"] == "submitted" and r["batch"] not in done]


def translated():
    return {u for r in runs() if r["event"] == "done" for u, q in r["units"].items() if q.get("text_chars")}


def pages_done():
    """Edition pages translated so far (units whose answer has text; a refused request translated nothing)."""
    m = manifest()
    return sum(m[u["unit"]]["pages"] for r in runs() if r["event"] == "done" for u in r["requests"]
               if u.get("text_chars"))


def openai_mod():
    sys.path.insert(0, r"C:\Users\user\Documents\enriques_api_pilot_20261106")
    import enr_pilot  # noqa: E402  (call(): the key is read from the user's note at each call, never printed)
    return enr_pilot


def api(P, method, url, body=None, tries=8):
    """enr_pilot.call with retries on network errors, unreadable answers and server errors."""
    for k in range(tries):
        try:
            code, r = P.call(method, url, body)
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError, ValueError) as e:
            print(time.strftime("%H:%M:%S"), "network error (%s), retry" % type(e).__name__, flush=True)
            time.sleep(min(30 * (k + 1), 300))
            continue
        if code >= 500 and k < tries - 1:
            print(time.strftime("%H:%M:%S"), "HTTP %d, retry" % code, flush=True)
            time.sleep(min(30 * (k + 1), 300))
            continue
        return code, r
    return 0, {"error": {"message": "no answer after %d tries" % tries}}


def body_for(unit):
    return {"model": MODEL, "instructions": T.read(os.path.join(T.ROOT, "prompt", "system", unit + ".txt")),
            "input": [{"role": "user", "content": [{"type": "input_text",
                                                    "text": T.read(os.path.join(T.ROOT, "prompt", "user",
                                                                                unit + ".txt"))}]}],
            "reasoning": {"effort": EFFORT}, "max_output_tokens": MAX_OUT, "background": True, "service_tier": TIER}


def est_input(body):
    return (len(body["instructions"]) + len(body["input"][0]["content"][0]["text"])) // 3


def worst_case(units):
    return sum(est_input(body_for(u)) * PRICE[0] / 1e6 + MAX_OUT * PRICE[1] / 1e6 for u in units)


def submit(P, unit, state, state_path):
    body = body_for(unit)
    for k in range(12):
        code, r = api(P, "POST", P.API, body)
        if code < 300 and r.get("id"):
            state["ids"].setdefault(unit, []).append(r["id"])
            T.write(state_path, json.dumps(state, ensure_ascii=False, indent=1))
            print(time.strftime("%H:%M:%S"), unit, "submitted", r["id"], r.get("status"), flush=True)
            return r["id"]
        err = json.dumps(r.get("error"))[:300]
        print(time.strftime("%H:%M:%S"), unit, "submit refused", code, err, flush=True)
        if code == 400:
            raise SystemExit("request rejected (400): " + err)
        time.sleep(min(60 * (k + 1), 600))
    raise SystemExit("could not submit " + unit)


def cmd_batch(name, units, force=False):
    if any(r["batch"] == name for r in runs()):
        raise SystemExit("batch %s exists (use collect)" % name)
    if in_flight():
        raise SystemExit("another batch is in flight: %s" % in_flight()[0]["batch"])
    m = manifest()
    for u in units:
        if u not in m:
            raise SystemExit("unknown unit " + u)
        src = os.path.join(T.REPO, m[u]["repo_path"])
        if T.sha256(src) != m[u]["sha256"]:
            raise SystemExit("%s changed in the repository since prepare.py: check the source of record" % u)
    s, w = spent(), worst_case(units)
    pages = sum(m[u]["pages"] for u in units)
    pd = pages_done()
    per_page = s / pd if pd else None
    print("%s: %d units, %d pages; worst case $%.2f; billed so far $%.4f for %d pages%s; cap $%.2f" % (
        name, len(units), pages, w, s, pd, (" ($%.4f a page)" % per_page) if per_page else "", CAP), flush=True)
    if s + w > CAP:
        raise SystemExit("billed so far plus the worst case of this batch would pass $%.2f: not submitted" % CAP)
    if per_page and per_page > 2 * REF_PER_PAGE and not force:
        raise SystemExit("cost per page $%.4f is more than twice the comparison's $%.4f: stop and report" % (
            per_page, REF_PER_PAGE))
    P = openai_mod()
    state_path = os.path.join(R, "state_%s.json" % name)
    state = {"batch": name, "units": units, "ids": {}, "t_start": time.time()}
    T.write(state_path, json.dumps(state, ensure_ascii=False, indent=1))
    log_run({"event": "submitted", "batch": name, "model": MODEL, "effort": EFFORT, "tier": TIER,
             "submitted": now(), "t_start": state["t_start"], "units": units, "pages": pages,
             "max_output_tokens": MAX_OUT, "worst_case_usd": round(w, 4), "billed_before_usd": round(s, 4),
             "cap_usd": CAP, "state": os.path.basename(state_path)})
    for u in units:
        submit(P, u, state, state_path)
    collect(name, P)


def save_attempt(unit):
    """Move an earlier output of the unit to runs/out/attempts/<unit>_a<k>.*"""
    a = os.path.join(OUT, "attempts")
    os.makedirs(a, exist_ok=True)
    k = 1
    while os.path.exists(os.path.join(a, "%s_a%d_result.json" % (unit, k))):
        k += 1
    for ext in (".tex", "_result.json"):
        p = os.path.join(OUT, unit + ext)
        if os.path.exists(p):
            shutil.move(p, os.path.join(a, "%s_a%d%s" % (unit, k, ext)))


def usage_cost(r):
    u = r.get("usage") or {}
    i_t, o_t = u.get("input_tokens") or 0, u.get("output_tokens") or 0
    return i_t, o_t, (i_t * PRICE[0] + o_t * PRICE[1]) / 1e6


def collect(name, P=None):
    P = P or openai_mod()
    state_path = os.path.join(R, "state_%s.json" % name)
    state = json.loads(T.read(state_path))
    units, t_start = state["units"], state["t_start"]
    for u in units:  # units whose submission was cut off by a stop
        if u not in state["ids"]:
            submit(P, u, state, state_path)
    final, t_end, failed_attempts, resubmits, retry_at = {}, {}, [], {}, {}
    last_note = 0
    while len(final) < len(units):
        time.sleep(60)
        for u in units:
            if u in final:
                continue
            if u in retry_at:  # a Flex refusal waiting for its resubmission
                if time.time() < retry_at[u]:
                    continue
                del retry_at[u]
                submit(P, u, state, state_path)
                continue
            rid = state["ids"][u][-1]
            code, r = api(P, "GET", "%s/%s" % (P.API, rid))
            st = r.get("status")
            if code != 200 or st not in FINAL:
                continue
            i_t, o_t, c = usage_cost(r)
            # Flex "server_is_overloaded" (nothing billed): resubmitted up to 8 times, after 4, 8, 16, 30 minutes;
            # any other failure: resubmitted at once, up to twice (added after batch b03, 11 Nov).
            overload = st == "failed" and (r.get("error") or {}).get("code") == "server_is_overloaded" and not o_t
            limit = 8 if overload else 2
            if st in ("failed", "cancelled") and resubmits.get(u, 0) < limit:
                failed_attempts.append({"unit": u, "response_id": rid, "status": st, "error": r.get("error"),
                                        "input_tokens": i_t, "output_tokens": o_t, "billed_usd": round(c, 6)})
                k = resubmits.get(u, 0)
                resubmits[u] = k + 1
                if overload:
                    wait = min(240 * 2 ** k, 1800)
                    retry_at[u] = time.time() + wait
                    print(time.strftime("%H:%M:%S"), u, st, json.dumps(r.get("error"))[:200],
                          "-> resubmitted in %d min" % (wait // 60), flush=True)
                    continue
                print(time.strftime("%H:%M:%S"), u, st, json.dumps(r.get("error"))[:300], "-> resubmitted",
                      flush=True)
                submit(P, u, state, state_path)
                continue
            final[u] = r
            t_end[u] = time.time()
            i_t, o_t, c = usage_cost(r)
            print(time.strftime("%H:%M:%S"), u, st, "tier", r.get("service_tier"), "in", i_t, "out", o_t,
                  "$%.4f" % c, "(%d of %d done)" % (len(final), len(units)), flush=True)
        if time.time() - last_note > 900:
            last_note = time.time()
            print(time.strftime("%H:%M:%S"), "%d of %d done, %.0f min" % (len(final), len(units),
                                                                       (time.time() - t_start) / 60), flush=True)
    os.makedirs(OUT, exist_ok=True)
    m = manifest()
    reqs, tin, tout, treas, billed = [], 0, 0, 0, 0.0
    for u in units:
        r = final[u]
        i_t, o_t, c = usage_cost(r)
        u_ = r.get("usage") or {}
        reasoning = (u_.get("output_tokens_details") or {}).get("reasoning_tokens")
        text = "".join(cc.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                       for cc in o.get("content", []) if cc.get("type") == "output_text")
        if os.path.exists(os.path.join(OUT, u + "_result.json")):
            save_attempt(u)
        meta = {"unit": u, "batch": name, "model": r.get("model"), "effort": EFFORT, "status": r.get("status"),
                "incomplete_details": r.get("incomplete_details"), "error": r.get("error"),
                "service_tier": r.get("service_tier"), "usage": u_, "input_tokens": i_t, "output_tokens": o_t,
                "reasoning_tokens": reasoning,
                "visible_output_tokens": (o_t - reasoning) if reasoning is not None else None,
                "billed_usd": round(c, 6), "text_chars": len(text), "response_id": r.get("id"),
                "pages": m[u]["pages"], "minutes": round((t_end[u] - t_start) / 60, 1),
                "system_sha256": T.sha256(os.path.join(T.ROOT, "prompt", "system", u + ".txt")),
                "user_sha256": T.sha256(os.path.join(T.ROOT, "prompt", "user", u + ".txt")),
                "source_sha256": m[u]["sha256"]}
        if text:
            T.write(os.path.join(OUT, u + ".tex"), text)
        T.write(os.path.join(OUT, u + "_result.json"), json.dumps(meta, ensure_ascii=False, indent=1))
        tin += i_t
        tout += o_t
        treas += reasoning or 0
        billed += c
        reqs.append({k: meta[k] for k in ("unit", "status", "input_tokens", "output_tokens", "reasoning_tokens",
                                          "billed_usd", "text_chars", "pages", "minutes")})
    for fa in failed_attempts:
        tin += fa["input_tokens"]
        tout += fa["output_tokens"]
        billed += fa["billed_usd"]
    pages = sum(m[q["unit"]]["pages"] for q in reqs if q["text_chars"])  # pages translated (since b04)
    rec = {"event": "done", "batch": name, "model": MODEL, "effort": EFFORT, "tier": TIER, "ended": now(),
           "wall_minutes": round((max(t_end.values()) - t_start) / 60, 1), "pages": pages,
           "pages_requested": sum(m[u]["pages"] for u in units), "input_tokens": tin,
           "output_tokens": tout, "reasoning_tokens": treas, "billed_usd": round(billed, 6),
           "list_price_usd": round((tin * LIST[0] + tout * LIST[1]) / 1e6, 6),
           "per_page_billed_usd": round(billed / pages, 6) if pages else None, "requests": reqs,
           "failed_attempts": failed_attempts,
           "units": {q["unit"]: {"status": q["status"], "text_chars": q["text_chars"]} for q in reqs}}
    log_run(rec)
    ledger_row(rec)
    print("%s: %d units, %d pages translated; tokens in %d, out %d (reasoning %d); $%.4f at the Flex price ($%.4f a "
          "page); %.1f min" % (name, len(units), pages, tin, tout, treas, billed, billed / pages if pages else 0,
                               rec["wall_minutes"]), flush=True)
    print("billed in all so far $%.4f" % spent(), flush=True)


def ledger_row(rec):
    ok = sum(1 for q in rec["requests"] if q["status"] == "completed" and q["text_chars"])
    row = {"id": "dertr-" + rec["batch"], "date": rec["ended"][:10],
           "project": "English translation of Grothendieck, Les Dérivateurs (transcription release v2026-11-11b)",
           "work": "%d units (five-page files of the transcription), %d edition pages: %s" % (
               len(rec["requests"]), rec["pages"], ", ".join(q["unit"] for q in rec["requests"])),
           "method": "Responses API, Flex tier, background, derivateurs_translation_20261111/scripts/run.py",
           "model": "GPT-6.1 Sol (OpenAI)", "effort": EFFORT, "tier": TIER, "requests": len(rec["requests"]),
           "pages": rec["pages"], "input_tokens": rec["input_tokens"], "output_tokens": rec["output_tokens"],
           "reasoning_tokens": rec["reasoning_tokens"], "usd_batch_price": round(rec["billed_usd"], 4),
           "list_price_usd": round(rec["list_price_usd"], 4),
           "per_page_billed_usd": round(rec["per_page_billed_usd"], 4) if rec["per_page_billed_usd"] else None,
           "key": "OpenAI project key (Untitled 1936.md)",
           "basis": "measured: usage of each answer; price %s/%s per million (Flex)" % PRICE,
           "wall_minutes": rec["wall_minutes"],
           "result": "%d of %d translations completed%s; outputs in derivateurs_translation_20261111/runs/out" % (
               ok, len(rec["requests"]),
               (", %d failed attempts resubmitted" % len(rec["failed_attempts"])) if rec["failed_attempts"] else "")}
    with open(T.LEDGER, "rb") as f:
        f.seek(0, 2)
        lead = ""
        if f.tell():
            f.seek(-1, 2)
            lead = "" if f.read(1) == b"\n" else "\n"
    with open(T.LEDGER, "a", encoding="utf-8") as f:
        f.write(lead + json.dumps(row, ensure_ascii=False) + "\n")


def cmd_plan():
    m = manifest()
    done = translated()
    todo = [u for u in m if u not in done]
    s, pd = spent(), pages_done()
    print("units %d, translated %d, to do %d (%d pages)" % (len(m), len(done), len(todo),
                                                          sum(m[u]["pages"] for u in todo)))
    print("billed so far $%.4f for %d pages%s; cap $%.2f; in flight: %s" % (
        s, pd, (" ($%.4f a page)" % (s / pd)) if pd else "", CAP, [r["batch"] for r in in_flight()] or "none"))
    if todo:
        n = 0  # the next units in order, each with its own worst case (its input differs)
        while n < len(todo) and s + worst_case(todo[:n + 1]) <= CAP:
            n += 1
        print("worst case of one more unit $%.3f; units that fit under the cap now: %d" % (
            worst_case(todo[:1]), n))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "plan":
        cmd_plan()
    elif a[0] == "batch":
        name = a[1]
        if "--next" in a:
            n = int(a[a.index("--next") + 1])
            done = translated()
            units = [u for u in manifest() if u not in done][:n]
        else:
            units = a[a.index("--units") + 1:]
            units = [u for u in units if not u.startswith("--")]
        cmd_batch(name, units, force="--force" in a)
    elif a[0] == "collect":
        collect(a[1])
