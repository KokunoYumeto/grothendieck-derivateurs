# After the review of STRATA (Claude Fable 5.2, 11 Nov 2026): the "After STRATA" sections now say
# that the statements were reviewed, the review is added to the three zips, one row label is corrected.
# Run once, after apply_fold_in.py. The zips were not sent in between, so no new _vN copy is made.
import hashlib, os, zipfile

DER = r"C:\Users\user\Documents\derivateurs_companion_20261109"
LM = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111"
REVIEW = DER + r"\pro_reviews_20261110\5_STRATA\REVIEW_author.md"
NOTE = "review of the STRATA answer by Claude (Fable 5.2), added 11 Nov 2026"

def rd(p):
    return open(p, encoding="utf-8").read()

def wr(p, s):
    open(p, "w", encoding="utf-8", newline="\n").write(s)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def sub(p, old, new):
    s = rd(p)
    assert s.count(old) == 1, (p, old[:50], s.count(old))
    wr(p, s.replace(old, new))

def append(p, text):
    s = rd(p)
    if not s.endswith("\n"):
        s += "\n"
    wr(p, s + text)

def add_review(folder, zipname, unz=False):
    zp = os.path.join(folder, zipname)
    b = open(REVIEW, "rb").read()
    name = "STRATA_review/REVIEW_author.md"
    with zipfile.ZipFile(zp, "a", zipfile.ZIP_DEFLATED) as z:
        assert name not in z.namelist()
        z.writestr(name, b)
    z = zipfile.ZipFile(zp)
    assert z.testzip() is None
    n = len(z.namelist())
    total = sum(i.file_size for i in z.infolist())
    z.close()
    size = os.path.getsize(zp)
    h = sha(open(zp, "rb").read())
    mp = os.path.join(folder, "MANIFEST.tsv")
    lines = rd(mp).split("\n")
    lines[0] = "# MANIFEST of %s (%d files, %d bytes zipped%s)" % (zipname, n, size, (", %d bytes unzipped" % total) if unz else "")
    lines[1] = "# zip SHA-256: " + h
    at = [i for i, l in enumerate(lines) if l.startswith("# UNRESOLVED OR MISSING")]
    at = at[0] if at else len(lines)
    lines[at:at] = ["\t".join([name, REVIEW, sha(b), str(len(b)), NOTE])]
    wr(mp, "\n".join(lines))
    return n, size, h

REV = ("They have since been reviewed by the author of this prompt (Claude, Anthropic); the review is attached as "
       "`STRATA_review/REVIEW_author.md`. No statement labelled Proved, Known or Refuted was found false; the review says for each "
       "statement whether its proof was followed and which cited sources were opened. Not verified there: %s. "
       "The review is not authority: verify what you use.")
ROW = (" Where that answer writes \"row VIc-C008\" it means the question at VI ms. 186 whether every locally constant object is represented "
       "by a functor that is both a fibration and an opfibration; in the companion's current register that question is row VIc-C022.")

out = {}

f = DER + r"\pro_prompts_20261110\7_BISITE"
sub(f + r"\PROMPT.md",
    "At the time of writing the author of this prompt has read them, the proofs of Parts C, D, E in outline, and has checked none: treat them like leads and verify what you use.",
    REV % "the step of A.4 and B.3 that passes from the stratification by simplices to the coarser one (taken there from two sources that were not opened), A.5, the extension of D.8 beyond space-valued coefficients, the general case of the contractibility argument in F.10, and the geometric halves of F.13–F.14" + ROW)
out["7_BISITE"] = add_review(f, "7_BISITE_background.zip")
append(f + r"\BACKGROUND.md", "- `STRATA_review/REVIEW_author.md` (review of the STRATA answer, `pro_reviews_20261110\\5_STRATA\\REVIEW_author.md`)\n")
append(f + r"\CHANGES_20261110.md", "- After the review of STRATA (same day): the section now says that the statements were reviewed (none found false) and names what was not verified; a note on the row label (\"VIc-C008\" in the STRATA files is row VIc-C022 of the current register); `STRATA_review/REVIEW_author.md` added to the zip (no new `_vN`: the zip had not been sent in between).\n")

f = DER + r"\pro_prompts_20261110\6_PATHS"
sub(f + r"\PROMPT.md",
    "At the time of writing the author of this prompt has read them, the proofs of Parts C and E in outline, and has checked none: treat them like leads and verify what you use.",
    REV % "the step of A.4, A.12 and B.3 that passes from the stratification by simplices to the coarser one (taken there from two sources that were not opened), and the citation behind B.8" + ROW)
out["6_PATHS"] = add_review(f, "6_PATHS_background.zip")
append(f + r"\BACKGROUND.md", "- `STRATA_review/REVIEW_author.md` (review of the STRATA answer, `pro_reviews_20261110\\5_STRATA\\REVIEW_author.md`)\n")
append(f + r"\CHANGES_20261110.md", "- After the review of STRATA (same day): the section now says that the statements were reviewed (none found false) and names what was not verified; a note on the row label (\"VIc-C008\" in the STRATA files is row VIc-C022 of the current register); `STRATA_review/REVIEW_author.md` added to the zip (no new `_vN`: the zip had not been sent in between).\n")

f = LM + r"\LM3_TEICHMULLER_TOWER"
sub(f + r"\PROMPT.md",
    "At the time of writing the author of this prompt has read Part F in full and the rest in statement, and has checked no proof: treat every statement like a lead and verify what you use.",
    REV % "the general case of the contractibility argument in F.10 (the case of the empty multicurve was checked against Kent–Leininger–Schleimer, Theorem 7.1), the comparison of the functors with the geometric maps in F.9, F.13 and F.14, and Bakalov–Kirillov's theorem used in F.17; Jansen's Construction 3.18, Proposition 3.23, Corollary 6.6 and Theorem 6.7 were opened and say what F.5, F.7 and F.8 take from them; the definitions quoted in F.16 agree with the attached transcription")
sub(f + r"\PROMPT.md",
    "not opened by the author of this prompt). F.11 (Refuted there)",
    "opened by the author of this prompt). F.11 (Refuted there; recomputed by the author of this prompt)")
out["LM3"] = add_review(f, "LM3_TEICHMULLER_TOWER_background.zip", True)
n, size, h = out["LM3"]
append(f + r"\BACKGROUND_ADD.md", "- `STRATA_review/REVIEW_author.md` (review of the STRATA answer by Claude; source `C:\\Users\\user\\Documents\\derivateurs_companion_20261109\\pro_reviews_20261110\\5_STRATA\\REVIEW_author.md`)\n")
append(f + r"\CHANGES_20261110.md", "- After the review of STRATA (same day): the section now says that the statements were reviewed (none found false), names what was not verified and what was checked against sources; `STRATA_review/REVIEW_author.md` added to the zip (no new `_vN`: the zip had not been sent in between).\n")
a = rd(f + r"\ASSEMBLY.md")
first = a.split("\n")[2]
assert first.startswith("262 files")
newfirst = ("%d files, %s bytes zipped" % (n, format(size, ","))) + first[first.index(" (hash and per-file"):] + " The review of that answer (`STRATA_review/REVIEW_author.md`) was added afterwards, the same day."
wr(f + r"\ASSEMBLY.md", a.replace(first, newfirst))

f = LM + r"\LM5_MULTI_GALOIS_TOPOI"
sub(f + r"\PROMPT.md",
    "At the time of writing the author of this prompt has read them in statement, Parts C and F in full, and has checked no proof: treat them like leads and verify what you use.",
    (REV % "part of the contractibility argument in F.10 and the comparison with the geometric maps in F.13; the statements of Parts A and C cited below were followed and their sources opened").replace("is attached as", "is to be attached as"))
append(f + r"\BACKGROUND.md", "- The review of the STRATA answer, `C:\\Users\\user\\Documents\\derivateurs_companion_20261109\\pro_reviews_20261110\\5_STRATA\\REVIEW_author.md`, in the zip as `STRATA_review/REVIEW_author.md`.\n")
append(f + r"\CHANGES_20261110.md", "- After the review of STRATA (same day): the section now says that the statements were reviewed (none found false) and names what was not verified; BACKGROUND.md lists the review.\n")

f = LM + r"\LM4_FINITE_GROUP_ACTIONS"
sub(f + r"\PROMPT.md",
    "the author of this prompt has read them in statement, Part F in full, and has checked no proof: verify what you use. The named sections are to be attached under `STRATA_return/`.",
    "they have since been reviewed by the author of this prompt (Claude, Anthropic; the review is to be attached as `STRATA_review/REVIEW_author.md`): none of those cited here was found false, and B.1, F.1–F.3, F.16 were followed in full; F.13 in outline only. The review is not authority: verify what you use. The named sections are to be attached under `STRATA_return/`.")
append(f + r"\BACKGROUND.md", "- The review of the STRATA answer, `C:\\Users\\user\\Documents\\derivateurs_companion_20261109\\pro_reviews_20261110\\5_STRATA\\REVIEW_author.md`, in the zip as `STRATA_review/REVIEW_author.md`.\n")
append(f + r"\CHANGES_20261110.md", "- After the review of STRATA (same day): the section now says that the statements were reviewed (none of those cited found false); BACKGROUND.md lists the review.\n")

for k, v in out.items():
    print(k, v)
