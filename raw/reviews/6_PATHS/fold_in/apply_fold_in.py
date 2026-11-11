# Fold the PATHS answer (GPT-6 Astra, ChatGPT Pro mode) into the prompts not yet sent.
# Claude Fable 5.2, 11 Nov 2026. Run once.
# 7_BISITE: section "After PATHS", two stale sentences on audited chunks corrected, zip rebuilt
# (previous zip moved to _work/7_BISITE_background_v6.zip), _work/MANIFEST.tsv, BACKGROUND.md, CHANGES.
# LM4, LM5: sections "After PATHS"; BACKGROUND.md and CHANGES (no zips exist).
import hashlib, os, shutil, zipfile

DER = "C:/Users/user/Documents/derivateurs_companion_20261109"
LM = "C:/Users/user/Documents/longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111"
RET = DER + "/pro_returns_20261110/6_PATHS"
HERE = DER + "/pro_reviews_20261110/6_PATHS/fold_in"
NOTE = "PATHS answer (GPT-6 Astra, ChatGPT Pro mode), added 11 Nov 2026"


def rd(p):
    return open(p, encoding="utf-8").read()


def wr(p, s):
    open(p, "w", encoding="utf-8", newline="\n").write(s)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def win(p):
    return p.replace("/", chr(92))


def paths_files(rels):
    out = []
    for rel in rels:
        src = RET + "/" + rel
        out.append(("PATHS_return/" + rel, win(src), open(src, "rb").read(), NOTE))
    return out


def from_paths_zip(names):
    # files that prompt 6_PATHS already carried: copied from its zip, checked against its manifest
    z = zipfile.ZipFile(DER + "/pro_prompts_20261110/6_PATHS/6_PATHS_background.zip")
    rows = {}
    for line in rd(DER + "/pro_prompts_20261110/6_PATHS/MANIFEST.tsv").splitlines():
        f = line.split("\t")
        if len(f) >= 4:
            rows[f[0]] = f
    out = []
    for name in names:
        b = z.read(name)
        assert rows[name][2] == sha(b), name
        out.append((name, rows[name][1], b,
                    "needed to check PATHS Part E (which cites CATHOT E.20-E.25 and the companion at VII ms. 161-169); copied from the zip of prompt 6_PATHS; added 11 Nov 2026"))
    return out


def insert_before(prompt, marker, section):
    s = rd(prompt)
    assert "After PATHS (added" not in s, prompt
    assert s.count(marker) == 1, (prompt, marker, s.count(marker))
    wr(prompt, s.replace(marker, section.rstrip("\n") + "\n\n" + marker))


def replace_once(prompt, old, new):
    s = rd(prompt)
    assert s.count(old) == 1, (prompt, old[:40], s.count(old))
    wr(prompt, s.replace(old, new))


def append(p, text):
    s = rd(p)
    if not s.endswith("\n"):
        s += "\n"
    wr(p, s + text)


# ---------------- 7_BISITE
f = DER + "/pro_prompts_20261110/7_BISITE"
work = f + "/_work"
files = paths_files(["PATHS_report.md", "PATHS_results.csv", "PATHS_paper.pdf", "PATHS_paper.tex",
                     "PATHS_references.bib", "sections/00_conventions.tex", "sections/A_definitions.tex",
                     "sections/D.tex", "sections/E.tex"])
files += from_paths_zip(["CATHOT_return/sections/E_path.tex", "CATHOT_review/REVIEW.md",
                         "grothendieck/DER_VII-c/DER_VII-c_text.tex",
                         "companion/DER_VII-c/DER_VII-c_overview.tex", "companion/DER_VII-c/DER_VII-c_blocks.tex",
                         "companion/DER_VII-c/DER_VII-c_claims.csv", "companion/DER_VII-c/DER_VII-c_references.bib",
                         "companion/DER_VII-c/derivateurs_companion.sty"])

zp = f + "/7_BISITE_background.zip"
vp = work + "/7_BISITE_background_v6.zip"
assert not os.path.exists(vp)
assert sorted(os.listdir(f)) == ["7_BISITE_background.zip", "PROMPT.md", "_work"], os.listdir(f)

insert_before(f + "/PROMPT.md", "## Recent results (state: 10 Nov 2026)", rd(HERE + "/BISITE_section.md"))
replace_once(f + "/PROMPT.md", "XII §7 and XIII §§4–6 continue it. None of those three is audited yet.",
             "XII §7 and XIII §§4–6 continue it. The companion's audits of these three are attached (see Part A).")
replace_once(f + "/PROMPT.md",
             "The companion's audit of XII ms. 207–227 is attached; II-b, XII §7 and XIII are not audited, so there you audit as you go.",
             "The companion's audits of XII ms. 207–227, of II-b, of XII §7 and of XIII are attached: they are a colleague's draft, so check them against the text as you go.")

shutil.copy2(zp, vp)
with zipfile.ZipFile(zp, "a", zipfile.ZIP_DEFLATED) as z:
    have = set(z.namelist())
    for name, src, b, note in files:
        assert name not in have, name
        z.writestr(name, b)
z = zipfile.ZipFile(zp)
assert z.testzip() is None
n = len([x for x in z.namelist() if not x.endswith("/")])
z.close()
size = os.path.getsize(zp)
h = sha(open(zp, "rb").read())
mp = work + "/MANIFEST.tsv"
lines = rd(mp).split("\n")
assert lines[0].startswith("# MANIFEST of 7_BISITE_background.zip")
lines[0] = "# MANIFEST of 7_BISITE_background.zip (%d files, %d bytes zipped)" % (n, size)
assert lines[1].startswith("# zip SHA-256:")
lines[1] = "# zip SHA-256: " + h
idx = [i for i, l in enumerate(lines) if l.startswith("# UNRESOLVED OR MISSING")]
at = idx[0] if idx else len(lines)
lines[at:at] = ["\t".join([name, src, sha(b), str(len(b)), note]) for name, src, b, note in files]
wr(mp, "\n".join(lines))

listing = "\n".join("- `%s` (%s)" % (name, "PATHS answer" if name.startswith("PATHS_return") else "from the zip of prompt `6_PATHS`") for name, src, b, note in files)
append(work + "/BACKGROUND.md", "\n## Added 11 Nov 2026 (after the PATHS answer)\n\nFrom `pro_returns_20261110/6_PATHS` (nothing from its `code/`, `audit/` or `research/` folders), and, because Part E of that answer cites CATHOT E.20–E.25 and the companion's blocks at VII ms. 161–169, eight files that prompt `6_PATHS` carried:\n" + listing + "\n")
append(work + "/CHANGES_20261110.md", """
## After the PATHS answer (11 November 2026)

- PROMPT.md: section "After PATHS" added before "Recent results" (by Claude Fable 5.2; the answer is by GPT-6 Astra, ChatGPT Pro mode). For Part B (`Liss ∩ Prop ⊂ Fib_W`): PATHS E.9 (the path functor over the group `C_2` is `W∞`-smooth and proper and does not preserve rational homology equivalences under base change), with an inference marked unverified that `W∞`-smooth and proper maps are `W`-smooth and proper for every `W`, so that the inclusion fails for rational homology, for `W_0` (STRATA G.3) and for homology localizers (POLES C.10): the prompt asks to decide it. For Parts B and E: the path functors as maps in `Liss ∩ Prop` that are not bifibrations (E.3, E.4, E.6, E.11 open), the functorial factorization E.5, the cotensor E.8. For Part E: D.8, D.9 (enough intrinsic cofibrations give the finite precofibration axioms), D.17 (XIII, XVII, XIX), D.18, D.23; D.10, D.13, D.15, D.16, D.20 on what needs an enhancement; E.7 on intervals. The PATHS statements are cited as unverified (report, register, Part E and six statements of Part D read; D.8 and E.9 followed). No lead changed.
- PROMPT.md, two stale sentences corrected: the second paragraph said of II §§5–6, XII §7 and XIII §§4–6 "None of those three is audited yet", and Part A ended "II-b, XII §7 and XIII are not audited, so there you audit as you go", while the companion files of II-b, XI-XIIa, XIIc-b, XIII-a and XIII-b have been in the zip since the entry "Runnable" above. Both now say that the audits are attached.
- Zip rebuilt: `PATHS_return/` with `PATHS_report.md`, `PATHS_results.csv`, `PATHS_paper.pdf`, `PATHS_paper.tex`, `PATHS_references.bib`, `sections/00_conventions.tex`, `sections/A_definitions.tex`, `sections/D.tex`, `sections/E.tex` (nothing from `code/`, `audit/` or `research/`); and, copied from the zip of prompt `6_PATHS`, `CATHOT_return/sections/E_path.tex`, `CATHOT_review/REVIEW.md`, `grothendieck/DER_VII-c/DER_VII-c_text.tex` and the five companion files of DER_VII-c. Previous zip moved to `_work/7_BISITE_background_v6.zip` (278 files; the zip that went with the prompt of 10:08 local time on 11 November, with STRATA and its review, without PATHS); that prompt text is `pro_reviews_20261110/6_PATHS/fold_in/before/7_BISITE/PROMPT.md`. MANIFEST.tsv and BACKGROUND.md updated.
""")
assert sorted(os.listdir(f)) == ["7_BISITE_background.zip", "PROMPT.md", "_work"], os.listdir(f)
print("7_BISITE", n, size, h)

# ---------------- LM4, LM5 (no zips)
PR = "C:/Users/user/Documents/derivateurs_companion_20261109/pro_returns_20261110/6_PATHS/"
f = LM + "/LM4_FINITE_GROUP_ACTIONS"
insert_before(f + "/PROMPT.md", "## Parts", rd(HERE + "/LM4_section.md"))
append(f + "/BACKGROUND.md", "\n## Added 11 Nov 2026 (after the PATHS answer of the Dérivateurs series)\n\n- From `" + win(PR) + "` (nothing from its `code`, `audit` or `research` folders), in the zip under `PATHS_return/`: `sections/00_conventions.tex`, `sections/D.tex`, `PATHS_paper.tex` (the macros), `PATHS_results.csv`, `PATHS_report.md`.\n")
append(f + "/CHANGES_20261110.md", "\n## After the PATHS answer of the Dérivateurs series (11 November 2026)\n\n- PROMPT.md: short section \"After PATHS\" added before the Parts: strict against homotopy-coherent diagrams (PATHS D.1, D.4, D.11, D.13) and, as an inference marked unverified, a reading of his essential-surjectivity problem in three layers (outer action to coherent action; coherent action to a strict action on some model; strict action on the surface itself). Cited as unverified. No lead changed.\n- BACKGROUND.md: the files to attach are listed. No zip exists for this prompt.\n")

f = LM + "/LM5_MULTI_GALOIS_TOPOI"
insert_before(f + "/PROMPT.md", "## Parts", rd(HERE + "/LM5_section.md"))
append(f + "/BACKGROUND.md", "\n## Added 11 Nov 2026 (after the PATHS answer of the Dérivateurs series)\n\n- From `" + win(PR) + "` (nothing from its `code`, `audit` or `research` folders), in the zip under `PATHS_return/` with the same relative paths: `PATHS_report.md`, `PATHS_results.csv`, `PATHS_paper.pdf`, `PATHS_paper.tex`, `PATHS_references.bib`, `sections/00_conventions.tex`, `sections/A_colimits.tex`, `sections/C_paths.tex`, `sections/D.tex`, `sections/D_kt.tex`, `sections/E.tex`.\n")
append(f + "/CHANGES_20261110.md", "\n## After the PATHS answer of the Dérivateurs series (11 November 2026)\n\n- PROMPT.md: section \"After PATHS\" added before the Parts: the second proof of GALOIS B.11–B.12 (PATHS D.K1–D.K5; the sentence of \"After GALOIS\" that the Kan–Thurston step was unchecked is answered there, not edited) and C.P5; E.13 (finite tests do not determine a morphism of classifying topoi), with an inference marked unverified on multi-Galois topoi and profinite completions; the shapes of Kaledin's theorem (D.14–D.16); filtered colimits of categories (A.2, A.5–A.7). Cited as unverified. No lead changed.\n- BACKGROUND.md: the files to attach are listed. No zip exists for this prompt.\n")
print("LM4, LM5 done")
