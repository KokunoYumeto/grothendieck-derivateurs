"""Print the status of a batch's responses that have not finished (no output is saved; the batch's own process
collects them). usage: python -I -B peek.py BATCH"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402
import run  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
name = sys.argv[1]
state = json.loads(T.read(os.path.join(run.R, "state_%s.json" % name)))
log = T.read(os.path.join(run.R, name + ".log"))
done = {ln.split()[1] for ln in log.splitlines() if " completed " in ln or " incomplete " in ln}
P = run.openai_mod()
for u in state["units"]:
    if u in done:
        continue
    rid = state["ids"][u][-1]
    code, r = run.api(P, "GET", "%s/%s" % (P.API, rid))
    print(u, code, r.get("status"), r.get("service_tier"), json.dumps(r.get("usage") or {})[:200],
          json.dumps(r.get("error"))[:200])
