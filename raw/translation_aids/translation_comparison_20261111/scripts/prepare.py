"""Cut the two French samples, render the one translation prompt per work, and write the request texts.

Writes (only inside translation_comparison_20261111):
  source/LM.tex, source/DER.tex          the five pages of each work, exactly as in the final files
  source/LM_ref.tex, source/DER_ref.tex  the one page of each work translated by the reference configuration
  selection/MANIFEST.json                file, line range and sha256 of each sample's source file
  prompt/system_LM.txt, prompt/system_DER.txt   the system prompt (identical for every configuration)
  prompt/user_<sample>.txt               the user message of each request
usage: python -I -B prepare.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_tc as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
P = os.path.join(T.ROOT, "prompt")
S = os.path.join(T.ROOT, "source")

TEMPLATE = open(os.path.join(P, "PROMPT_TEMPLATE.txt"), encoding="utf-8").read()


def parts():
    """PROMPT_PARTS.txt: sections headed '@@ <WORK> <PLACEHOLDER>'; the text up to the next header fills it."""
    out, cur = {}, None
    for line in open(os.path.join(P, "PROMPT_PARTS.txt"), encoding="utf-8").read().split("\n"):
        m = re.match(r"@@ (LM|DER) ([A-Z_]+)\s*$", line)
        if m:
            cur = out.setdefault(m.group(1), {}).setdefault(m.group(2), [])
            continue
        if cur is not None:
            cur.append(line)
    return {w: {k: "\n".join(v).strip("\n") for k, v in d.items()} for w, d in out.items()}


PARTS = parts()


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def macro_block(text):
    """The \\newcommand lines of the DER chunk's preamble whose macro is used in the text."""
    pre = T.read(T.DER_FILE)
    pre = pre[:pre.index("\\begin{document}")]
    lines = []
    for line in pre.splitlines():
        m = re.match(r"\\newcommand\{(\\[A-Za-z]+)\}", line)
        if m and re.search(re.escape(m.group(1)) + r"(?![A-Za-z])", text):
            lines.append(line)
    return "\n".join(lines)


manifest = {}
for name, spec in list(T.SAMPLES.items()) + [(k + "_ref", v) for k, v in T.REF.items()]:
    work = name.split("_")[0]
    text, a, z = T.cut(spec)
    write(os.path.join(S, name + ".tex"), text)
    manifest[name] = {"source_file": spec["file"], "lines": [a, z], "sha256_of_source_file": T.sha256(spec["file"]),
                      "pages": spec["pages"], "chars": len(text), "what": spec["what"],
                      "anchors": [p[0] for p in T.split_pages(text, work)]}
    head = "Translate this LaTeX into English (%s; %d page%s)." % (spec["head"], spec["pages"],
                                                                   "s" if spec["pages"] > 1 else "")
    if work == "DER":
        user = ("The edition's macros used on these pages, for reference (do not translate or return them):\n"
                + macro_block(text) + "\n\n" + head + "\n\n" + text)
    else:
        user = head + "\n\n" + text
    write(os.path.join(P, "user_%s.txt" % name), user)
    print(name, "lines %d-%d" % (a, z), "chars", len(text), "anchors", manifest[name]["anchors"])

for work in ("LM", "DER"):
    d = PARTS[work]
    sysp = TEMPLATE
    for k, v in d.items():
        sysp = sysp.replace("{" + k + "}", v.rstrip("\n"))
    assert "{" + "WORK" not in sysp and not re.search(r"\{[A-Z_]{4,}\}", sysp), "unfilled placeholder"
    write(os.path.join(P, "system_%s.txt" % work), sysp)
    print("system_%s.txt" % work, len(sysp), "chars")

write(os.path.join(T.ROOT, "selection", "MANIFEST.json"), json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")
