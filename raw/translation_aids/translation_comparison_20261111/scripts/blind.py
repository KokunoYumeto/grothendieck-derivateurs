"""The blind set for the grading: each full output copied to blind/<work>_<letter>.tex, the letters assigned at random
per work (random.SystemRandom), the mapping in key/KEY.json. The French is in source/. Refuses to write a blind file
that names a model or a provider.
usage: python -I -B blind.py          (once, after every run is collected)
"""
import json
import os
import random
import re
import shutil
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_tc as T  # noqa: E402
import run as RUN  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
NAMES = re.compile(r"claude|anthropic|opus|fable|sonnet|haiku|mythos|gpt|openai|chatgpt|codex|\bsol\b|astra|gemini|"
                   r"llama|mistral|\bmodel name\b", re.I)
B = os.path.join(T.ROOT, "blind")
K = os.path.join(T.ROOT, "key", "KEY.json")

if os.path.exists(K):
    raise SystemExit("key/KEY.json exists already: the letters are assigned once")
rng = random.SystemRandom()
key = {"assigned": datetime.now(timezone.utc).isoformat(timespec="seconds"),
       "method": "letters A, B, ... shuffled per work with random.SystemRandom; each blind file is the configuration's "
                 "full output, byte for byte", "LM": {}, "DER": {}}
for work in ("LM", "DER"):
    items = []
    for cfg_name, cfg in RUN.CONFIGS.items():
        for sample in cfg["samples"]:
            if sample.split("_")[0] == work and os.path.exists(os.path.join(T.ROOT, "runs", cfg_name, sample + ".tex")):
                items.append((cfg_name, cfg, sample))
    letters = [chr(ord("A") + i) for i in range(len(items))]
    rng.shuffle(letters)
    for (cfg_name, cfg, sample), letter in sorted(zip(items, letters), key=lambda x: x[1]):
        src = os.path.join(T.ROOT, "runs", cfg_name, sample + ".tex")
        text = T.read(src)
        hit = NAMES.findall(text)
        if hit:
            raise SystemExit("%s names %s: not copied" % (src, sorted(set(hit))))
        dst = os.path.join(B, "%s_%s.tex" % (work, letter))
        shutil.copyfile(src, dst)
        key[work][letter] = {"config": cfg_name, "configuration": cfg["name"], "model": cfg["model"],
                             "effort": cfg["effort"], "source": "source/%s.tex" % sample,
                             "pages": RUN.PAGES[sample], "output": "runs/%s/%s.tex" % (cfg_name, sample),
                             "sha256": T.sha256(dst)}
        print(work, letter, cfg_name, sample)
os.makedirs(os.path.dirname(K), exist_ok=True)
with open(K, "w", encoding="utf-8") as f:
    json.dump(key, f, ensure_ascii=False, indent=1)
print("key written:", K)
