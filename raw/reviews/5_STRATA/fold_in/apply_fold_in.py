# Fold the STRATA answer into the prompts not yet sent (Claude Fable 5.2, 11 Nov 2026).
# Run once. Inserts the "After STRATA" sections, keeps the previous zips as _vN,
# appends the STRATA files to the zips, updates MANIFEST.tsv.
import hashlib, io, os, re, shutil, sys, zipfile

DER = r"C:\Users\user\Documents\derivateurs_companion_20261109"
LM = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111"
RET = DER + r"\pro_returns_20261110\5_STRATA\STRATA"
HERE = DER + r"\pro_reviews_20261110\5_STRATA\fold_in"
JANSEN = DER + r"\pro_reviews_20261110\5_STRATA\sources_opened\2308.09551v2\paper.pdf"
NOTE = "STRATA answer (GPT-6 Astra, ChatGPT Pro mode), added 11 Nov 2026"

def rd(p):
    return open(p, encoding="utf-8").read()

def wr(p, s):
    open(p, "w", encoding="utf-8", newline="\n").write(s)

def sha(b):
    return hashlib.sha256(b).hexdigest()

COMMON = ["STRATA_report.md", "STRATA_results.csv", "STRATA_paper.pdf", "STRATA_paper.tex",
          "STRATA_references.bib", "sections/00_conventions.tex"]

def strata_files(sections):
    out = []
    for rel in COMMON + ["sections/%s.tex" % s for s in sections]:
        src = os.path.join(RET, rel.replace("/", "\\"))
        out.append(("STRATA_return/" + rel, src, open(src, "rb").read(), NOTE))
    return out

def jansen():
    return [("papers/2308.09551/2308.09551v2.pdf", "https://arxiv.org/pdf/2308.09551v2",
             open(JANSEN, "rb").read(),
             "M. Orsnes Jansen, Moduli stack of stable curves from a stratified homotopy viewpoint (cited in STRATA F.7, F.8); added 11 Nov 2026")]

def bgh():
    z = zipfile.ZipFile(DER + r"\pro_prompts_20261110\5_STRATA\5_STRATA_background.zip")
    rows = {}
    for line in rd(DER + r"\pro_prompts_20261110\5_STRATA\MANIFEST.tsv").splitlines():
        if line.startswith("papers/1807.03281/"):
            f = line.split("\t")
            rows[f[0]] = f
    out = []
    for name in z.namelist():
        if name.startswith("papers/1807.03281/") and not name.endswith("/"):
            b = z.read(name)
            assert rows[name][2] == sha(b), name
            out.append((name, rows[name][1], b, "Barwick, Glasman, Haine, Exodromy (for Part F: Gal(X)); added 11 Nov 2026"))
    return out

def insert_before(prompt, marker, section):
    s = rd(prompt)
    assert "After STRATA (added" not in s, prompt + " already has the section"
    assert s.count(marker) == 1, (prompt, marker, s.count(marker))
    s = s.replace(marker, section.rstrip("\n") + "\n\n" + marker)
    wr(prompt, s)

def rebuild(folder, zipname, vname, files, manifest_has_unzipped=False):
    zp = os.path.join(folder, zipname)
    vp = os.path.join(folder, vname)
    assert not os.path.exists(vp), vp
    shutil.copy2(zp, vp)
    with zipfile.ZipFile(zp, "a", zipfile.ZIP_DEFLATED) as z:
        have = set(z.namelist())
        for name, src, b, note in files:
            assert name not in have, name
            z.writestr(name, b)
    z = zipfile.ZipFile(zp)
    assert z.testzip() is None
    n = len([x for x in z.namelist() if not x.endswith("/")])
    unz = sum(i.file_size for i in z.infolist())
    z.close()
    size = os.path.getsize(zp)
    h = sha(open(zp, "rb").read())
    mp = os.path.join(folder, "MANIFEST.tsv")
    lines = rd(mp).split("\n")
    if manifest_has_unzipped:
        lines[0] = "# MANIFEST of %s (%d files, %d bytes zipped, %d bytes unzipped)" % (zipname, n, size, unz)
    else:
        lines[0] = "# MANIFEST of %s (%d files, %d bytes zipped)" % (zipname, n, size)
    assert lines[1].startswith("# zip SHA-256:")
    lines[1] = "# zip SHA-256: " + h
    idx = [i for i, l in enumerate(lines) if l.startswith("# UNRESOLVED OR MISSING")]
    at = idx[0] if idx else len(lines)
    new = ["\t".join([name, src, sha(b), str(len(b)), note]) for name, src, b, note in files]
    lines[at:at] = new
    wr(mp, "\n".join(lines))
    return n, size, h, vname

def append(p, text):
    s = rd(p)
    if not s.endswith("\n"):
        s += "\n"
    wr(p, s + text)

def listing(files):
    return "\n".join("- `%s` (%s)" % (name, "STRATA answer" if name.startswith("STRATA_return") else note.split(";")[0]) for name, src, b, note in files)

report = {}

# ---------------- 7_BISITE
f = DER + r"\pro_prompts_20261110\7_BISITE"
files = strata_files("ABCDEFG") + jansen()
insert_before(f + r"\PROMPT.md", "## Recent results (state: 10 Nov 2026)", rd(HERE + r"\BISITE_section.md"))
report["7_BISITE"] = rebuild(f, "7_BISITE_background.zip", "7_BISITE_background_v5.zip", files)
append(f + r"\BACKGROUND.md", "\n## Added 11 Nov 2026 (after the STRATA answer)\n\nFrom `pro_returns_20261110\\5_STRATA\\STRATA` (nothing from its `code\\` or `audit\\` folders):\n" + listing(files) + "\n")
append(f + r"\CHANGES_20261110.md", """
## After the STRATA answer (11 November 2026)

- PROMPT.md: section "After STRATA" added before "Recent results". For Parts A and B: the lifting-category tests for proper and smooth functors with the converse by universal base change (STRATA D.3, D.4), D.7, two transcription corrections to check (D.9). For Part B and Part E: bifibration against `Liss ∩ Prop` against `Fib_W` (E.1, D.5, D.6, E.2–E.4), the bifibration results E.8–E.10 with E.11 open; for a general `W`: G.3–G.5. For Part B, the two fine theories and the duality: G.1. For Part D (Lead 2): the poset dictionary with its hypotheses (A.1, A.2, A.4–A.6, A.12, B.3, B.7) and the difference between the Kan extensions and the topological direct images (D.5, D.8). For Part E: A.9, the lax-pullback gluing and its failure on homotopy categories (C.6–C.8). For Part F: D.1–D.2 and the moduli example F.7, F.10–F.14. For Part G: the finite-poset dictionary A.4–A.5 and what it does not supply (G.1, G.7, D.8). The STRATA statements are cited as unverified. No lead changed.
- Zip rebuilt: `STRATA_return/` with `STRATA_report.md`, `STRATA_results.csv`, `STRATA_paper.pdf`, `STRATA_paper.tex`, `STRATA_references.bib`, `sections/00_conventions.tex`, `sections/A.tex` to `G.tex` (nothing from `code\\` or `audit\\`), and Jansen's paper (arXiv:2308.09551v2) under `papers/2308.09551/`. Previous zip kept as `7_BISITE_background_v5.zip`: that is the zip of the prompt as made ready at 01:48 UTC on 11 November (with the companion files of II-b, XI-XIIa, XIIc-b, XIII-a, XIII-b and without STRATA). The current `7_BISITE_background.zip` goes with the current PROMPT.md. MANIFEST.tsv and BACKGROUND.md updated.
""")

# ---------------- 6_PATHS
f = DER + r"\pro_prompts_20261110\6_PATHS"
files = strata_files("ABCDEG")
insert_before(f + r"\PROMPT.md", "## Recent results (state: 10 Nov 2026)", rd(HERE + r"\PATHS_section.md"))
report["6_PATHS"] = rebuild(f, "6_PATHS_background.zip", "6_PATHS_background_v9.zip", files)
append(f + r"\BACKGROUND.md", "\n## Added 11 Nov 2026 (after the STRATA answer)\n\nFrom `pro_returns_20261110\\5_STRATA\\STRATA` (nothing from its `code\\` or `audit\\` folders):\n" + listing(files) + "\n")
append(f + r"\CHANGES_20261110.md", """
## After the STRATA answer (11 November 2026)

- This prompt had not been sent (confirmed by the user through the coordinator on 11 November).
- PROMPT.md: section "After STRATA" added before "Recent results". Directed paths against all paths: exit paths of `|NS|` (STRATA A.4, A.12, B.3), the crossing category as homotopy link (C.2), the failure with unrestricted paths (C.4), as the geometric form of Lead 2 and of the comparison `J`. For Part D: relative posets present every small category (B.8, B.6, B.7); homotopy categories of diagrams do not glue (C.6, C.7; B.12 open). For Parts C and E: the weight test for strict pushouts along sieves (C.9–C.11). For the first item of "After TOTASPH": G.2 (simplicial sets only), A.10, and filtered colimits of proper, smooth and fibred functors (E.3, E.4). For Part E: the strict path bifibration over posets and cancellative bases (E.5, E.6, E.10; E.7 refuted, E.11 open) to compare with `Ch(X) → X × X`; D.3–D.5, D.6, E.1, G.3. The STRATA statements are cited as unverified. No lead changed.
- Zip rebuilt: `STRATA_return/` with `STRATA_report.md`, `STRATA_results.csv`, `STRATA_paper.pdf`, `STRATA_paper.tex`, `STRATA_references.bib`, `sections/00_conventions.tex`, `sections/A.tex`, `B.tex`, `C.tex`, `D.tex`, `E.tex`, `G.tex` (nothing from `code\\` or `audit\\`); previous zip kept as `6_PATHS_background_v9.zip`. MANIFEST.tsv and BACKGROUND.md updated.
""")

# ---------------- LM3
f = LM + r"\LM3_TEICHMULLER_TOWER"
files = strata_files("BCDF") + jansen() + bgh()
insert_before(f + r"\PROMPT.md", "## Recent results (state: 10 Nov 2026)", rd(HERE + r"\LM3_section.md"))
s = rd(f + r"\PROMPT.md")
old = "Package STRATA of the companion work on *Les Dérivateurs* (if its output is attached, use it; otherwise define what you need) describes"
new = "Package STRATA of the companion work on *Les Dérivateurs* (its answer is attached under `STRATA_return/`; see \"After STRATA\" above, and verify what you use) describes"
assert s.count(old) == 1
wr(f + r"\PROMPT.md", s.replace(old, new))
report["LM3"] = rebuild(f, "LM3_TEICHMULLER_TOWER_background.zip", "LM3_TEICHMULLER_TOWER_background_v2.zip", files, True)
n, size, h, _ = report["LM3"]
append(f + r"\BACKGROUND_ADD.md", "\n## Added 11 Nov 2026 (after the STRATA answer of the Dérivateurs series)\n\nSource root `C:\\Users\\user\\Documents\\derivateurs_companion_20261109\\pro_returns_20261110\\5_STRATA\\STRATA\\`; in the zip under `STRATA_return/` with the same relative paths; nothing from its `code\\` or `audit\\` folders. Jansen's paper from arXiv (PDF of v2); *Exodromy* (arXiv source, 25 files) copied from the zip of the Dérivateurs prompt `5_STRATA`.\n" + listing(files) + "\n")
append(f + r"\CHANGES_20261110.md", """
## After the STRATA answer of the Dérivateurs series (11 November 2026)

- PROMPT.md: section "After STRATA" added before "Recent results"; the sentence of Part F that said "if its output is attached" now says that it is. Content of the section: the category (STRATA F.7: the Charney–Lee category by transporters of multicurves modulo Dehn twists; exit and entrance variance, F.8; Jansen's theorem covers all genera); the cases `n = 4, 5` (F.1–F.6; F.3); his groups in his notation (F.16) and the request to read the definition of the modular topos in the attached transcription of scans 321–330; the functors (F.9, F.12, F.13, F.15) with properness (F.10), failure of smoothness (F.11) and base change (F.14); what it says about the tower (F.17) and what it leaves to this prompt; five suggestions for Part F marked as unverified inferences (a completion by transporters in the profinite group; the profinite category `Gal(X)` of Barwick–Glasman–Haine as a geometric definition; the action as outer actions compatible with inertia bimodules and the functors, on levels 4 and 5; the element `t_1 t_2^{-1}`; relabelling as a pseudo-action); from Parts B, C, D: B.1, B.6, B.10, B.12, C.5–C.6, D.3–D.4. Cited as unverified. No lead changed.
- Zip rebuilt: `STRATA_return/` with `STRATA_report.md`, `STRATA_results.csv`, `STRATA_paper.pdf`, `STRATA_paper.tex`, `STRATA_references.bib`, `sections/00_conventions.tex`, `sections/B.tex`, `C.tex`, `D.tex`, `F.tex` (nothing from `code\\` or `audit\\`); `papers/2308.09551/2308.09551v2.pdf` (Jansen); `papers/1807.03281/` (Barwick–Glasman–Haine, arXiv source). Previous zip kept as `LM3_TEICHMULLER_TOWER_background_v2.zip`. MANIFEST.tsv, ASSEMBLY.md and BACKGROUND_ADD.md updated.
""")
a = rd(f + r"\ASSEMBLY.md")
first = a.split("\n")[2]
assert first.startswith("226 files")
newfirst = ("%d files, %s bytes zipped (hash and per-file SHA-256 in `MANIFEST.tsv`). " % (n, format(size, ","))) + first.split("). ", 1)[1] + " Rebuilt again 11 Nov 2026 after the STRATA answer of the Dérivateurs series (36 files added: 10 under `STRATA_return/`, Jansen's paper, the 25 files of the arXiv source of *Exodromy*); the previous zip is `LM3_TEICHMULLER_TOWER_background_v2.zip`."
a = a.replace(first, newfirst)
old = "- `proof_packs/` (18 files)"
assert a.count(old) == 1
a = a.replace(old, "- `STRATA_return/`: `STRATA_report.md`, `STRATA_results.csv`, `STRATA_paper.pdf`, `STRATA_paper.tex`, `STRATA_references.bib`, `sections/00_conventions.tex`, `sections/B.tex`, `sections/C.tex`, `sections/D.tex`, `sections/F.tex` (the answer of GPT-6 Astra, ChatGPT Pro mode, to the Dérivateurs prompt `5_STRATA`; nothing from its `code\\` or `audit\\` folders). For Part F.\n" + old)
old = "- The output of the Derivateurs prompt `5_STRATA` (Part F): does not exist yet.\n"
assert a.count(old) == 1
a = a.replace(old, "")
old = "- `papers/` (30 files):"
assert a.count(old) == 1
a = a.replace(old, "- `papers/` (56 files; the 26 added on 11 Nov after STRATA are `papers/2308.09551/2308.09551v2.pdf`, M. Ørsnes Jansen, *Moduli stack of stable curves from a stratified homotopy viewpoint*, and `papers/1807.03281/`, the arXiv source of Barwick–Glasman–Haine, *Exodromy*); the other 30:")
wr(f + r"\ASSEMBLY.md", a)

# ---------------- LM4, LM5 (no zips)
f = LM + r"\LM4_FINITE_GROUP_ACTIONS"
insert_before(f + r"\PROMPT.md", "## Parts", rd(HERE + r"\LM4_section.md"))
append(f + r"\BACKGROUND.md", "\n## Added 11 Nov 2026 (after the STRATA answer of the Dérivateurs series)\n\n- From `C:\\Users\\user\\Documents\\derivateurs_companion_20261109\\pro_returns_20261110\\5_STRATA\\STRATA\\` (nothing from its `code\\` or `audit\\` folders), in the zip under `STRATA_return/`: `sections/00_conventions.tex`, `sections/B.tex`, `sections/F.tex`, `STRATA_paper.tex` (the macros), `STRATA_results.csv`, `STRATA_report.md`.\n- M. Ørsnes Jansen, *Moduli stack of stable curves from a stratified homotopy viewpoint*, arXiv:2308.09551v2 (a copy is in `LM3_TEICHMULLER_TOWER_background.zip` under `papers/2308.09551/`).\n")
append(f + r"\CHANGES_20261110.md", "\n## After the STRATA answer of the Dérivateurs series (11 November 2026)\n\n- PROMPT.md: short section \"After STRATA\" added before the Parts: a group with loops as an EI category (STRATA B.1, F.1–F.3, F.13), with an inference marked unverified on the 2-category of Part C (exit-path categories of the surface with its marked points, and of the quotient orbifold for a finite group acting); his groups of §19 as read in STRATA F.16 and the functoriality of filling a puncture and of relabelling (F.9). Cited as unverified. No lead changed.\n- BACKGROUND.md: the files to attach are listed. No zip exists for this prompt.\n")

f = LM + r"\LM5_MULTI_GALOIS_TOPOI"
insert_before(f + r"\PROMPT.md", "## Parts", rd(HERE + r"\LM5_section.md"))
append(f + r"\BACKGROUND.md", "\n## Added 11 Nov 2026 (after the STRATA answer of the Dérivateurs series)\n\n- From `C:\\Users\\user\\Documents\\derivateurs_companion_20261109\\pro_returns_20261110\\5_STRATA\\STRATA\\` (nothing from its `code\\` or `audit\\` folders), in the zip under `STRATA_return/` with the same relative paths: `STRATA_report.md`, `STRATA_results.csv`, `STRATA_paper.pdf`, `STRATA_paper.tex`, `STRATA_references.bib`, `sections/00_conventions.tex`, `sections/A.tex`, `sections/B.tex`, `sections/C.tex`, `sections/F.tex`.\n- M. Ørsnes Jansen, arXiv:2308.09551v2, and S. Douteau, L. Waas, *From homotopy links to stratified homotopy theories*, arXiv:2112.02394v2 (copies: `LM3_TEICHMULLER_TOWER_background.zip`, `papers/2308.09551/`; the zip of the Dérivateurs prompt `5_STRATA`, `papers/2112.02394/`).\n")
append(f + r"\CHANGES_20261110.md", "\n## After the STRATA answer of the Dérivateurs series (11 November 2026)\n\n- PROMPT.md: section \"After STRATA\" added before the Parts: gluing a presheaf topos from an open part, a closed part and the link (STRATA C.1–C.4, C.6, C.8) as instances Part C's van Kampen theorem should contain; the exit-path category of `P¹` with three marked points (F.1–F.2, F.8) and, as an inference marked unverified, two candidate comparisons for `B_{X,U}` in Part B (the constructible topos; the topos with each missing point replaced by its link, which is the shape of Lead 2); the forgetful functor and its fibres for §32 (F.9–F.11, F.13); for Part E, three more places where level 1 behaves better (A.1–A.2, B.10, B.12, B.6). Cited as unverified. No lead changed.\n- BACKGROUND.md: the files to attach are listed. No zip exists for this prompt.\n")

for k, v in report.items():
    print(k, v)
