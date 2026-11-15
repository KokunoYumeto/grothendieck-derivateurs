"""Run one configuration of the translation comparison (one run at a time; the budget is checked before each).

Configurations (the same prompt for all: prompt/system_<work>.txt with prompt/user_<sample>.txt):
  opus55-high     Claude Opus 5.5 (claude-opus-5-5), effort high, Message Batches API          LM, DER (5 pages each)
  opus55-max      Claude Opus 5.5, effort max, Message Batches API                              LM, DER
  fable52-medium  Claude Fable 5.2 (claude-fable-5-2), effort medium, Message Batches API       LM, DER
  fable52-high    Claude Fable 5.2, effort high, Message Batches API                            LM, DER
  sonnet55-high   Claude Sonnet 5.5 (claude-sonnet-5-5), effort high, Message Batches API       LM, DER
  sol61-high      GPT-6.1 Sol (gpt-6.1-sol), reasoning effort high, OpenAI Responses API, Flex  LM, DER
  sol61-max       GPT-6.1 Sol, reasoning effort max, OpenAI Responses API, Flex (user, 11 Nov)   LM, DER
  fable52-max     Claude Fable 5.2, effort max, Message Batches API: the reference, on one page of each work
                  (LM_ref = scan 483, DER_ref = edition page 1)

Before a run: the dollars of the finished runs plus the worst case of the new run (its input tokens at the run's price
plus every request's output cap at the output price) must stay within the budget (its figure is withheld from this public copy). An Anthropic batch is
submitted only when no other batch of the account is in progress (one batch at a time). Each run is logged in
runs/RUNS.jsonl and in C:\\Users\\user\\Documents\\compute_cost_ledger\\LEDGER.jsonl.

Keys: Anthropic through C:\\Users\\user\\Documents\\claude_tools\\run_with_note_key.py (KEY_NOTE = account B's note);
OpenAI through enr_pilot.call (enriques_api_pilot_20261106), as sga_scan_check_20261105 does. No key is printed or
stored.

usage:
  set KEY_NOTE, then: python -I ...\\claude_tools\\run_with_note_key.py ...\\scripts\\run.py run opus55-high
  python -I -B ...\\scripts\\run.py run sol61-high
  ... run.py collect CONFIG     (resume waiting for a submitted run)
  ... run.py plan               (worst cases, no API call)
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_tc as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.join(T.ROOT, "runs")
RUNS = os.path.join(R, "RUNS.jsonl")
BUDGET = None  # dollars; withheld from this public copy
MAX_OUT = 128000
A = "https://api.anthropic.com/v1"
CONFIGS = {  # price: billed per million tokens (batch or Flex price); list: list price; both withheld from this public copy
    "opus55-high": dict(provider="anthropic", model="claude-opus-5-5", effort="high", price=None,
                        list=None, name="Claude Opus 5.5, effort high, Message Batches API"),
    "fable52-medium": dict(provider="anthropic", model="claude-fable-5-2", effort="medium", price=None,
                           list=None, name="Claude Fable 5.2, effort medium, Message Batches API"),
    "opus55-max": dict(provider="anthropic", model="claude-opus-5-5", effort="max", price=None,
                       list=None, name="Claude Opus 5.5, effort max, Message Batches API"),
    "fable52-high": dict(provider="anthropic", model="claude-fable-5-2", effort="high", price=None,
                         list=None, name="Claude Fable 5.2, effort high, Message Batches API"),
    "sonnet55-high": dict(provider="anthropic", model="claude-sonnet-5-5", effort="high", price=None,
                          list=None, name="Claude Sonnet 5.5, effort high, Message Batches API"),
    "sol61-high": dict(provider="openai", model="gpt-6.1-sol", effort="high", price=None, list=None,
                       name="GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier"),
    "sol61-max": dict(provider="openai", model="gpt-6.1-sol", effort="max", price=None, list=None,
                      name="GPT-6.1 Sol, reasoning effort max, OpenAI Responses API, Flex tier (added 11 Nov at the user's request)"),
    "fable52-max": dict(provider="anthropic", model="claude-fable-5-2", effort="max", price=None,
                        list=None, samples=["LM_ref", "DER_ref"],
                        name="Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work)"),
}
for _c in CONFIGS.values():
    _c.setdefault("samples", ["LM", "DER"])
PAGES = {"LM": 5, "DER": 5, "LM_ref": 1, "DER_ref": 1}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def rd(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def system_for(sample):
    return rd(os.path.join(T.ROOT, "prompt", "system_%s.txt" % sample.split("_")[0]))


def user_for(sample):
    return rd(os.path.join(T.ROOT, "prompt", "user_%s.txt" % sample))


def runs():
    if not os.path.exists(RUNS):
        return []
    return [json.loads(x) for x in rd(RUNS).splitlines() if x.strip()]


def log_run(rec):
    os.makedirs(R, exist_ok=True)
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def committed():
    """Dollars of finished runs plus the worst case of runs submitted and not yet collected."""
    rs = runs()
    done = {r["run"] for r in rs if r["event"] == "done"}
    total = sum(r["billed_usd"] for r in rs if r["event"] == "done")
    total += sum(r["worst_case_usd"] for r in rs if r["event"] == "submitted" and r["run"] not in done)
    return total


def save_output(cfg_name, sample, text, meta):
    d = os.path.join(R, cfg_name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, sample + ".tex"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(os.path.join(d, sample + "_result.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)


def ledger_row(cfg_name, cfg, rec):
    in_t, out_t = rec["input_tokens"], rec["output_tokens"]
    pages = sum(PAGES[s] for s in cfg["samples"])
    lp = (in_t * cfg["list"][0] + out_t * cfg["list"][1]) / 1e6
    ok = [r for r in rec["requests"] if r.get("text_chars")]
    row = {"id": "trcmp-" + cfg_name, "date": rec["ended"][:10],
           "project": "Translation model comparison: Grothendieck, La Longue Marche and Les Dérivateurs into English",
           "work": ("one page of each work (LM scan 483, DER Ch. XVIII p. 1), the reference" if cfg_name == "fable52-max"
                    else "five pages of each work (LM scans 483-487 of package LM_P049; DER Ch. XVIII pp. 1-5)"),
           "method": ("Message Batches API" if cfg["provider"] == "anthropic" else "Responses API, Flex tier, background")
           + ", translation_comparison_20261111/scripts/run.py",
           "model": cfg["model"] if cfg["provider"] == "anthropic" else "GPT-6.1 Sol (OpenAI)", "effort": cfg["effort"],
           "requests": len(rec["requests"]), "pages": pages, "input_tokens": in_t, "output_tokens": out_t,
           "usd_batch_price": round(rec["billed_usd"], 4), "list_price_usd": round(lp, 4),
           "per_page_billed_usd": round(rec["billed_usd"] / pages, 4),
           "key": "account B (key in Untitled 1939.md)" if cfg["provider"] == "anthropic"
           else "OpenAI project key (Untitled 1936.md)",
           "basis": "measured: usage of each answer; price %s/%s per million (%s)" % (
               cfg["price"][0], cfg["price"][1], "batch" if cfg["provider"] == "anthropic" else "Flex"),
           "wall_minutes": rec["wall_minutes"],
           "result": "%d of %d translations returned (stop reasons: %s); outputs in translation_comparison_20261111/runs/%s"
                     % (len(ok), len(rec["requests"]), ", ".join(str(r.get("stop_reason")) for r in rec["requests"]),
                        cfg_name)}
    if rec.get("batch"):
        row["batch"] = rec["batch"]
    with open(T.LEDGER, "rb") as f:
        f.seek(0, 2)
        lead = ""
        if f.tell():
            f.seek(-1, 2)
            lead = "" if f.read(1) == b"\n" else "\n"
    with open(T.LEDGER, "a", encoding="utf-8") as f:
        f.write(lead + json.dumps(row, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- Anthropic (Message Batches)

def a_api(method, url, body=None):
    h = {"x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01",
         "content-type": "application/json"}
    data = json.dumps(body).encode("utf-8") if body is not None else None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h, method=method),
                                        timeout=600) as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and attempt < 5:
                time.sleep(20 * (attempt + 1))
                continue
            return e.code, e.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            if attempt < 5:
                time.sleep(20 * (attempt + 1))
                continue
            return 0, str(e)
    return 0, "no answer"


def params(cfg, sample):
    return {"model": cfg["model"], "max_tokens": MAX_OUT, "thinking": {"type": "adaptive"},
            "output_config": {"effort": cfg["effort"]}, "system": system_for(sample),
            "messages": [{"role": "user", "content": [{"type": "text", "text": user_for(sample)}]}]}


def count_tokens(model, system, messages):
    body = {"model": model, "messages": messages, "thinking": {"type": "adaptive"}}
    if system:
        body["system"] = system
    code, r = a_api("POST", A + "/messages/count_tokens", body)
    if code != 200:
        raise SystemExit("count_tokens %d: %s" % (code, r[:300]))
    return json.loads(r)["input_tokens"]


def text_tokens(model, text):
    """Approximate token count of a text (the visible translation): a user message with the text minus one with 'x'."""
    if not text:
        return 0
    return (count_tokens(model, None, [{"role": "user", "content": text}])
            - count_tokens(model, None, [{"role": "user", "content": "x"}]) + 1)


def batches_in_progress():
    code, r = a_api("GET", A + "/messages/batches?limit=20")
    if code != 200:
        raise SystemExit("batch list %d: %s" % (code, r[:300]))
    return [b["id"] for b in json.loads(r).get("data", []) if b.get("processing_status") in ("in_progress", "canceling")]


def anthropic_run(cfg_name, cfg, budget):
    assert os.environ.get("ANTHROPIC_API_KEY"), "run through run_with_note_key.py"
    reqs, in_tokens = [], 0
    for sample in cfg["samples"]:
        p = params(cfg, sample)
        in_tokens += count_tokens(p["model"], p["system"], p["messages"])
        reqs.append({"custom_id": sample, "params": p})
    worst = in_tokens * cfg["price"][0] / 1e6 + len(reqs) * MAX_OUT * cfg["price"][1] / 1e6
    spent = committed()
    print("%s: %d requests, input %d tokens (counted), worst case $%.2f; committed so far $%.2f; budget $%.2f"
          % (cfg_name, len(reqs), in_tokens, worst, spent, budget), flush=True)
    if spent + worst > budget:
        raise SystemExit("worst case over the budget: not submitted")
    while True:
        busy = batches_in_progress()
        if not busy:
            break
        print(time.strftime("%H:%M:%S"), "another batch is in progress (%s); waiting" % ", ".join(busy), flush=True)
        time.sleep(120)
    code, r = a_api("POST", A + "/messages/batches", {"requests": reqs})
    if code != 200:
        raise SystemExit("batch submit %d: %s" % (code, r[:500]))
    bt = json.loads(r)
    log_run({"event": "submitted", "run": cfg_name, "provider": "anthropic", "model": cfg["model"],
             "effort": cfg["effort"], "batch": bt["id"], "created": bt.get("created_at"), "submitted": now(),
             "samples": cfg["samples"], "max_tokens": MAX_OUT, "input_tokens_counted": in_tokens,
             "worst_case_usd": round(worst, 4), "committed_before_usd": round(spent, 4), "budget_usd": budget})
    print("batch", bt["id"], flush=True)
    anthropic_collect(cfg_name, cfg, bt["id"])


def anthropic_collect(cfg_name, cfg, bid):
    while True:
        code, r = a_api("GET", A + "/messages/batches/" + bid)
        if code != 200:
            print(time.strftime("%H:%M:%S"), "status", code, r[:200], flush=True)
            time.sleep(120)
            continue
        s = json.loads(r)
        print(time.strftime("%H:%M:%S"), s["processing_status"], json.dumps(s["request_counts"]), flush=True)
        if s["processing_status"] == "ended":
            break
        time.sleep(60)
    code, body = a_api("GET", s["results_url"])
    assert code == 200, (code, body[:300])
    reqs, tin, tout, billed = [], 0, 0, 0.0
    for line in body.splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        sample = x["custom_id"]
        if x["result"]["type"] != "succeeded":
            reqs.append({"sample": sample, "result": x["result"]["type"], "detail": json.dumps(x["result"])[:500]})
            print(sample, x["result"]["type"], json.dumps(x["result"])[:300], flush=True)
            continue
        m = x["result"]["message"]
        u = m.get("usage") or {}
        i_plain = u.get("input_tokens") or 0
        i_cw = u.get("cache_creation_input_tokens") or 0
        i_cr = u.get("cache_read_input_tokens") or 0
        o_t = u.get("output_tokens") or 0
        cost = (i_plain + 1.25 * i_cw + 0.1 * i_cr) * cfg["price"][0] / 1e6 + o_t * cfg["price"][1] / 1e6
        tin += i_plain + i_cw + i_cr
        tout += o_t
        billed += cost
        text = "".join(c.get("text", "") for c in m["content"] if c.get("type") == "text")
        vis = text_tokens(cfg["model"], text)
        meta = {"sample": sample, "config": cfg_name, "model": m.get("model"), "effort": cfg["effort"],
                "stop_reason": m.get("stop_reason"), "stop_details": m.get("stop_details"), "usage": u,
                "input_tokens": i_plain + i_cw + i_cr, "output_tokens": o_t, "visible_output_tokens_counted": vis,
                "thinking_tokens_estimated": max(o_t - vis, 0), "billed_usd": round(cost, 6),
                "content_types": [c.get("type") for c in m["content"]], "text_chars": len(text), "batch": bid}
        save_output(cfg_name, sample, text, meta)
        reqs.append({k: meta[k] for k in ("sample", "stop_reason", "input_tokens", "output_tokens",
                                          "visible_output_tokens_counted", "thinking_tokens_estimated", "billed_usd",
                                          "text_chars")})
        print(sample, m.get("stop_reason"), "in", i_plain + i_cw + i_cr, "out", o_t, "(visible about %d)" % vis,
              "$%.4f" % cost, flush=True)
    t0 = datetime.fromisoformat(s["created_at"].replace("Z", "+00:00"))
    t1 = datetime.fromisoformat(s["ended_at"].replace("Z", "+00:00"))
    rec = {"event": "done", "run": cfg_name, "provider": "anthropic", "model": cfg["model"], "effort": cfg["effort"],
           "batch": bid, "ended": s["ended_at"], "wall_minutes": round((t1 - t0).total_seconds() / 60, 1),
           "input_tokens": tin, "output_tokens": tout, "billed_usd": round(billed, 6), "requests": reqs}
    log_run(rec)
    ledger_row(cfg_name, cfg, rec)
    print("%s: tokens in %d, out %d, $%.4f at batch price, %.1f min" % (cfg_name, tin, tout, billed,
                                                                      rec["wall_minutes"]), flush=True)


# ---------------------------------------------------------------- OpenAI (Responses API, Flex tier)

def openai_mod():
    sys.path.insert(0, r"C:\Users\user\Documents\enriques_api_pilot_20261106")
    import enr_pilot  # noqa: E402  (call(): the key is read from the user's note at each call, never printed)
    return enr_pilot


def openai_body(cfg, sample):
    return {"model": cfg["model"], "instructions": system_for(sample),
            "input": [{"role": "user", "content": [{"type": "input_text", "text": user_for(sample)}]}],
            "reasoning": {"effort": cfg["effort"]}, "max_output_tokens": MAX_OUT, "background": True,
            "service_tier": "flex"}


def openai_run(cfg_name, cfg, budget):
    P = openai_mod()
    bodies, est = {}, 0
    for sample in cfg["samples"]:
        b = openai_body(cfg, sample)
        est += (len(b["instructions"]) + len(b["input"][0]["content"][0]["text"])) // 3
        bodies[sample] = b
    worst = est * cfg["price"][0] / 1e6 + len(bodies) * MAX_OUT * cfg["price"][1] / 1e6
    spent = committed()
    print("%s: %d requests, input about %d tokens (estimated), worst case $%.2f; committed so far $%.2f; budget $%.2f"
          % (cfg_name, len(bodies), est, worst, spent, budget), flush=True)
    if spent + worst > budget:
        raise SystemExit("worst case over the budget: not submitted")
    ids = {}
    t_start = time.time()
    for sample, body in bodies.items():
        for attempt in range(6):
            code, r = P.call("POST", P.API, body)
            if code < 300 and r.get("id"):
                ids[sample] = r["id"]
                print(sample, "submitted", r["id"], r.get("status"), flush=True)
                break
            print(sample, "submit failed", code, json.dumps(r.get("error"))[:300], flush=True)
            if code == 400:
                raise SystemExit("request rejected")
            time.sleep(60)
        else:
            raise SystemExit("could not submit " + sample)
    log_run({"event": "submitted", "run": cfg_name, "provider": "openai", "model": cfg["model"], "effort": cfg["effort"],
             "submitted": now(), "t_start": t_start, "response_ids": ids, "samples": cfg["samples"],
             "max_output_tokens": MAX_OUT, "input_tokens_estimated": est, "worst_case_usd": round(worst, 4),
             "committed_before_usd": round(spent, 4), "budget_usd": budget})
    openai_collect(cfg_name, cfg, ids, t_start)


def openai_collect(cfg_name, cfg, ids, t_start):
    P = openai_mod()
    done, t_end = {}, {}
    while len(done) < len(ids):
        time.sleep(30)
        for sample, rid in ids.items():
            if sample in done:
                continue
            code, r = P.call("GET", "%s/%s" % (P.API, rid))
            st = r.get("status")
            if code >= 500 or st in ("queued", "in_progress"):
                continue
            done[sample] = r
            t_end[sample] = time.time()
            print(sample, st, "service_tier", r.get("service_tier"), json.dumps(r.get("usage") or {})[:300], flush=True)
    reqs, tin, tout, billed = [], 0, 0, 0.0
    for sample in cfg["samples"]:
        r = done[sample]
        u = r.get("usage") or {}
        i_t, o_t = u.get("input_tokens") or 0, u.get("output_tokens") or 0
        cost = (i_t * cfg["price"][0] + o_t * cfg["price"][1]) / 1e6
        tin += i_t
        tout += o_t
        billed += cost
        text = "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                       for c in o.get("content", []) if c.get("type") == "output_text")
        reasoning = (u.get("output_tokens_details") or {}).get("reasoning_tokens")
        meta = {"sample": sample, "config": cfg_name, "model": r.get("model"), "effort": cfg["effort"],
                "stop_reason": r.get("status"), "incomplete_details": r.get("incomplete_details"),
                "service_tier": r.get("service_tier"), "usage": u, "input_tokens": i_t, "output_tokens": o_t,
                "reasoning_tokens": reasoning,
                "visible_output_tokens": (o_t - reasoning) if reasoning is not None else None,
                "billed_usd": round(cost, 6), "text_chars": len(text), "response_id": r.get("id"),
                "minutes": round((t_end[sample] - t_start) / 60, 1)}
        save_output(cfg_name, sample, text, meta)
        reqs.append({k: meta[k] for k in ("sample", "stop_reason", "input_tokens", "output_tokens", "reasoning_tokens",
                                          "visible_output_tokens", "billed_usd", "text_chars")})
        print(sample, r.get("status"), "in", i_t, "out", o_t, "(reasoning %s)" % reasoning, "$%.4f" % cost, flush=True)
    rec = {"event": "done", "run": cfg_name, "provider": "openai", "model": cfg["model"], "effort": cfg["effort"],
           "ended": now(), "wall_minutes": round((max(t_end.values()) - t_start) / 60, 1), "input_tokens": tin,
           "output_tokens": tout, "billed_usd": round(billed, 6), "requests": reqs}
    log_run(rec)
    ledger_row(cfg_name, cfg, rec)
    print("%s: tokens in %d, out %d, $%.4f at the Flex price, %.1f min" % (cfg_name, tin, tout, billed,
                                                                         rec["wall_minutes"]), flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    budget = float(args[args.index("--budget") + 1]) if "--budget" in args else BUDGET
    if args[0] == "plan":
        for n, c in CONFIGS.items():
            print("%-15s %-18s %-6s samples %-18s output cap worst $%.2f" % (
                n, c["model"], c["effort"], ",".join(c["samples"]), len(c["samples"]) * MAX_OUT * c["price"][1] / 1e6))
        print("committed so far $%.4f of $%.2f" % (committed(), budget))
    elif args[0] == "run":
        name = args[1]
        cfg = CONFIGS[name]
        if any(r["run"] == name and r["event"] in ("done", "submitted") for r in runs()):
            raise SystemExit(name + " was already submitted (use collect)")
        (anthropic_run if cfg["provider"] == "anthropic" else openai_run)(name, cfg, budget)
    elif args[0] == "collect":
        name = args[1]
        cfg = CONFIGS[name]
        sub = [r for r in runs() if r["run"] == name and r["event"] == "submitted"]
        if any(r["run"] == name and r["event"] == "done" for r in runs()):
            raise SystemExit(name + " is already collected")
        if cfg["provider"] == "anthropic":
            anthropic_collect(name, cfg, sub[-1]["batch"])
        else:
            openai_collect(name, cfg, sub[-1]["response_ids"], sub[-1]["t_start"])
