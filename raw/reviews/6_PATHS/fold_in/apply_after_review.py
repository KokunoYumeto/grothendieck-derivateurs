# After the review of PATHS (Claude Fable 5.2, 11 Nov 2026). Run once.
# - REVIEW_author.md: two corrections of wording (count line; a statement from memory marked as such).
# - LM4, LM5 (work tree, not sent, no zips): the sentence on the state of the review.
# - PROMPT_UPDATES.md, README of the Derivateurs stack, KNOWLEDGE_HANDOFF.md: the new folder convention and the verdicts.
# 7_BISITE is NOT touched: nothing it cites was found false, and the user may have sent it.
BS = chr(92)
DER = "C:/Users/user/Documents/derivateurs_companion_20261109"
LMW = "C:/Users/user/Documents/longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work"
REV = DER + "/pro_reviews_20261110/6_PATHS"


def rd(p):
    return open(p, encoding="utf-8").read()


def wr(p, s):
    open(p, "w", encoding="utf-8", newline="\n").write(s)


def rep(p, old, new, count=1):
    s = rd(p)
    assert s.count(old) == count, (p, old[:50], s.count(old))
    wr(p, s.replace(old, new))


# --- review wording
rep(REV + "/REVIEW_author.md",
    "Counts: 76 statements. Proved or known and confirmed by this review (with the qualifications in the tables): 65. Unverified: 5 (B.9, C.5, D.15, D.21, and the citations of D.K2 counted with D.K2 as proved). Open in the answer: 6 (A.8, B.8, C.9, C.10, D.22, E.11). False: none.",
    "Counts: 76 statements. Proved or known and confirmed by this review (with the qualifications in the tables): 66. Unverified: 4 (B.9, C.5, D.15, D.21). Open in the answer: 6 (A.8, B.8, C.9, C.10, D.22, E.11). False: none.")
rep(REV + "/REVIEW_author.md",
    "whose localization is the walking retraction, with discrete mapping spaces; so the question there",
    "whose localization is, as far as I remember (Lurie, *Higher Topos Theory*, §4.4.5; not opened), the ordinary category of a retraction, with discrete mapping spaces; if so the question there")

# --- LM4, LM5
old4 = "the author of this prompt has read those cited here with their proofs once and has not checked them, and the review is not finished: verify what you use. The named section is to be attached under `PATHS_return/`."
new4 = "they have since been reviewed by the author of this prompt (Claude, Anthropic; the review is to be attached as `PATHS_review/REVIEW_author.md`): none of those cited here was found false, and D.4, D.11, D.13 were followed in full. The review is not authority: verify what you use. The named section is to be attached under `PATHS_return/`."
rep(LMW + "/LM4_FINITE_GROUP_ACTIONS/PROMPT.md", old4, new4)
old5 = "At the time of writing the author of this prompt has read them with their proofs once and has not checked them; the review is not finished: treat them like leads and verify what you use."
new5 = "They have since been reviewed by the author of this prompt (Claude, Anthropic); the review is to be attached as `PATHS_review/REVIEW_author.md`. No statement labelled Proved, Known or Refuted was found false; of those cited below, A.2, A.5, C.P5, D.K1–D.K5, D.16 and E.13 were followed in full, D.14 was checked against the preprint, and D.15 was not verified (it rests on a theorem of that preprint). The review is not authority: verify what you use."
rep(LMW + "/LM5_MULTI_GALOIS_TOPOI/PROMPT.md", old5, new5)
for name in ("LM4_FINITE_GROUP_ACTIONS", "LM5_MULTI_GALOIS_TOPOI"):
    for fn, text in (("BACKGROUND.md", "- The review of the PATHS answer, `" + (DER + "/pro_reviews_20261110/6_PATHS/REVIEW_author.md").replace("/", BS) + "`, in the zip as `PATHS_review/REVIEW_author.md`.\n"),
                     ("CHANGES_20261110.md", "- After the review of PATHS (same day): the section now says that the statements were reviewed (none of those cited found false); BACKGROUND.md lists the review.\n")):
        p = LMW + "/" + name + "/" + fn
        s = rd(p)
        if not s.endswith("\n"):
            s += "\n"
        wr(p, s + text)

# --- README of the Derivateurs stack: the work tree
p = DER + "/pro_prompts_20261110/README.md"
s = rd(p)
a = "the previous zip is `_work" + BS + "7_BISITE_background_v6.zip`"
assert s.count(a) == 1
s = s.replace(a, "the previous zip is `..{b}pro_prompts_20261110_work{b}7_BISITE{b}7_BISITE_background_v6.zip`".format(b=BS))
a = "Top level of the folder: `PROMPT.md` and `7_BISITE_background.zip`; everything else is in `_work" + BS + "`."
assert s.count(a) == 1
s = s.replace(a, "The folder holds `PROMPT.md` and `7_BISITE_background.zip` only; everything else is in `..{b}pro_prompts_20261110_work{b}7_BISITE{b}`.".format(b=BS))
a = "the review will be `REVIEW_author.md` beside it. Until then the answer is cited as unverified."
assert s.count(a) == 1
s = s.replace(a, "the review is `REVIEW_author.md` beside it (no statement labelled Proved, Known or Refuted found false; the inference in the first item of \"After PATHS\" in `7_BISITE` checked and right). `7_BISITE` still words the answer as not yet reviewed; it was not rebuilt after the review, because nothing it cites changed and it may have been sent.")
wr(p, s)
print("ok")
