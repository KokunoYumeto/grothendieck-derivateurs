"""Build one chunk's reader of the Les Dérivateurs companion: set the commentary blocks of DER_<id>_blocks.tex into the
text DER_<id>_text.tex at their anchors, check every file of the chunk (column headers, anchors, citations), and write DER_<id>_reader.tex.
usage: python build_reader.py DER_<id> [DIR]      (exit status 1 if a check fails; every problem is printed)"""
import csv
import pathlib
import re
import sys

TAG = sys.argv[1]
D = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(".")
KINDS = {"exposition", "context", "later", "examples", "status", "development"}
errors = []


def read(name):
    p = D / f"{TAG}_{name}"
    if not p.exists():
        errors.append(f"missing {p.name}")
        return ""
    return p.read_text(encoding="utf-8")


text, blocks_src = read("text.tex"), read("blocks.tex")
overview, bib = read("overview.tex"), read("references.bib")
for name, cols in (("claims.csv", "id,ms_page,statement,kind,proof_status,gap_or_error,repair,references,notes"),
                   ("corrections.csv", "pdf_page,place,transcription_reads,should_read,kind,evidence")):
    p = D / f"{TAG}_{name}"
    if not p.exists():
        errors.append(f"missing {p.name}")
        continue
    head = next(csv.reader(p.open(encoding="utf-8")), [])
    if [h.strip() for h in head] != cols.split(","):
        errors.append(f"{name}: header must be {cols}")
if "\\begin{document}" not in text:
    errors.append("text.tex: not a complete document")
pre, body = text.split("\\begin{document}", 1) if "\\begin{document}" in text else ("", text)
body = body.rsplit("\\end{document}", 1)[0]
MS = re.compile(r"\\msp(?:in)?\{(?:page\s*)?(\d+(?:bis|ter|quater|'|\$'\$)?)\}")   # 36, 36bis, 12'  ($'$ = math prime, 11 Nov)
marks = [(m.group(1).replace("$'$", "'"), m.start()) for m in MS.finditer(body)]
pos_of = {}
for n, k in marks:
    pos_of.setdefault(n, k)
BLOCK = re.compile(r"\\begin\{dcomment\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{dcomment\}", re.S)
blocks = list(BLOCK.finditer(blocks_src))
if not blocks:
    errors.append("blocks.tex: no dcomment block")
inserts = []
for idx, b in enumerate(blocks):
    kind, anchor, title = b.group(1).strip(), b.group(2).strip(), b.group(3).strip()
    if kind not in KINDS:
        errors.append(f"block '{title}': kind {kind!r} not one of {sorted(KINDS)}")
    if "\\ours" in b.group(4) and kind != "development":
        errors.append(f"block '{title}': \\ours outside a development block")
    m = re.fullmatch(r"p(\d+(?:bis|ter|quater|')?)(?::(.+))?", anchor, re.S)
    if not m:
        errors.append(f"block '{title}': anchor {anchor!r} is not p<N> or p<N>:<words>")
        continue
    n, words = m.group(1), m.group(2)
    if words and len(words.strip()) < 20:
        errors.append(f"block '{title}': anchor words '{words.strip()}' shorter than 20 characters")
    if n not in pos_of:
        errors.append(f"block '{title}': no manuscript page {n} in this chunk")
        continue
    # a chunk of several chapters has each manuscript page number once per chapter: search every page so numbered
    spans = []
    for p, k in marks:   # p<N> also covers N bis, N ter, N' (earlier packages anchored them under N)
        if p == n or (n.isdigit() and re.fullmatch(re.escape(n) + r"(?:bis|ter|quater|')", p)):
            spans.append((k, min([q for _, q in marks if q > k] + [len(body)])))
    if words:
        hits = [s + h.start() for s, e in spans for h in re.finditer(re.escape(words.strip()), body[s:e])]
        if len(hits) != 1:
            errors.append(f"block '{title}': '{words.strip()[:40]}' occurs {len(hits)} times on ms. page {n}"
                          + (f" (the chunk has {len(spans)} pages {n})" if len(spans) > 1 else ""))
            continue
        at = hits[0]
    else:
        if len({s for s, _ in spans}) > 1:
            errors.append(f"block '{title}': the chunk has {len(spans)} manuscript pages {n}; give anchor words")
            continue
        at = spans[0][1]
    brk = body.find("\n\n", at)
    inserts.append((len(body) if brk < 0 else brk, idx, b.group(0)))
# values of the two registers
ENUMS = {"claims.csv": {"kind": {"definition", "axiom", "proposition", "claim", "conjecture", "question", "remark"},
                        "proof_status": {"proved", "sketched", "stated", "assumed", "conjectured", "false", "open"}},
         "corrections.csv": {"kind": {"transcription", "edition_slip_kept", "doubt_resolved"}}}
for name, cols in ENUMS.items():
    p = D / f"{TAG}_{name}"
    if not p.exists():
        continue
    rows = list(csv.DictReader(p.open(encoding="utf-8")))
    for i, r in enumerate(rows, 2):
        for col, allowed in cols.items():
            if (r.get(col) or "").strip() not in allowed:
                errors.append(f"{name} line {i}: {col} {r.get(col)!r} not one of {sorted(allowed)}")
    if name == "claims.csv":
        ids = [(r.get("id") or "").strip() for r in rows]
        dup = sorted({x for x in ids if ids.count(x) > 1})
        if dup:
            errors.append(f"claims.csv: duplicate ids {dup[:10]}")
keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))
for src in (blocks_src, overview):
    for group in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", src):
        for k in group.split(","):
            if k.strip() and k.strip() not in keys:
                errors.append(f"\\cite key {k.strip()} not in references.bib")
for k, v in ((k, v) for k, v in re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", bib, re.S)):
    if not re.search(r"\b(url|doi)\s*=", v):
        errors.append(f"reference {k}: no url or doi")
if errors:
    print("\n".join("ERROR: " + e for e in errors))
    sys.exit(1)
for at, _, blk in sorted(inserts, reverse=True):   # blocks at the same place keep their file order
    body = body[:at] + "\n\n" + blk + "\n" + body[at:]
# a package's own layout file (\input{reader_layout.tex} and the like) is not used: the kit sets the layout, and
# derivateurs_companion.sty supplies the macros such files defined for the text (\dcfit, the zigzag arrow style)
for line in re.findall(r"^[ \t]*\\input\{[^}]*\}[ \t]*$", pre, re.M):
    print(f"note: dropped {line.strip()} from the preamble (the package's own layout; the kit sets the layout)")
pre = re.sub(r"^[ \t]*\\input\{[^}]*\}[ \t]*\n?", "", pre, flags=re.M)
pre = pre.replace("\\documentclass[11pt]{article}", "\\documentclass[11pt]{article}\n\\usepackage{derivateurs_companion}", 1)
if "derivateurs_companion" not in pre:
    pre = pre + "\n\\usepackage{derivateurs_companion}\n"
out = (pre + "\\begin{document}\n" + body + "\n\\clearpage\n\\section*{Overview of these pages}\n" + overview +
       f"\n\\bibliographystyle{{plainnat}}\n\\bibliography{{{TAG}_references}}\n\\end{{document}}\n")
(D / f"{TAG}_reader.tex").write_text(out, encoding="utf-8")
print(f"{TAG}: {len(blocks)} blocks set in ({', '.join(sorted({b.group(1).strip() for b in blocks}))}), "
      f"{len(keys)} references -> {TAG}_reader.tex")
