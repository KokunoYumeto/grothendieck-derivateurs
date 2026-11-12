# TASK (verbatim brief received 12 Nov 2026, 13:21 local) — durable record

Kept so that the exact instructions survive any context loss. This is the launching agent's brief, word for word.

---

You are Claude Fable 5.2, running at effort max, as the field expert for Grothendieck's *Les Dérivateurs* and seven research returns of GPT-6 Astra (effort Pro, ChatGPT Pro mode) on it: 2_TOTAL_ASPHERICITY (TOTASPH), 3_POLES, 4_GALOIS, 5_STRATA, 6_PATHS, 7_BISITE, 8_RESIDUE. Earlier reviews of these returns were discarded unread; you start from nothing. A separate expert handles 1_CATHOT.

The method, in the user's words: "they will read the appropriate literature before making comments, and then they will be asked to think about it at max effort. And they will also have to reread every single one of those returns and consider them." And: "an agent should read the rest of the math. After contextualizing its understanding by first reading relevant Grothendieck passages. Remember how the first one read the entirety of the Long March transcription before starting ... Read the math, then work on the topic. Not YOLO."

Base folder: C:\Users\user\Documents\derivateurs_companion_20261109
Write only in pro_reviews_max_20261112\<return folder> (one per return: 2_TOTAL_ASPHERICITY ... 8_RESIDUE) and pro_reviews_max_20261112\DERIVATEURS_EXPERT\ (your notes, combined reading, handoff; scratch work in its work\ subfolder). Create them.

1. Grothendieck first. Our checked French transcription is corrected_french_20261111\DER_*.tex. Read it in order and in full as far as your context allows; at the very least, before each return, read in full every part of the text its prompt names or quotes. Write DERIVATEURS_EXPERT\GROTHENDIECK_NOTES.md as you go: the structure of the text, its definitions, results and open questions, with locations.

2. Literature. The primary sources the returns rely on (each return's .bib and research files list them) and the standard literature of the field (Grothendieck's Pursuing Stacks; Heller; Franke; Maltsiniotis; Cisinski; Groth; Quillen; Thomason; others as needed). Read the primary texts themselves. Freely accessible copies only (arXiv, authors' pages, Numdam, EuDML, open archives); no paywalled or pirated copies. For web access load WebSearch / WebFetch with ToolSearch, or use the web-fetch agent. Write DERIVATEURS_EXPERT\READING_BASE.md: each source, its location, the statements you rely on with their full hypotheses, and what you could not obtain.

3. Then the returns, in order 2 to 8, each in full: its prompt (pro_prompts_20261110\<n>\PROMPT.md and its background ZIP, unzipped into your work folder) and every file of the return (pro_returns_20261110\<n>\...: paper, report, results CSV, sections, research, audit; read the code but do not run it; write and run your own checks in your work folder). For each return, every item (every results row and every claim in the paper) gets a verdict (correct / wrong / gap / unproved) with your own proof, counterexample or exact citation. Where the return leaves something open, attack it: try to prove or refute it. Record anything new. Write pro_reviews_max_20261112\<n>\REVIEW.md for a return before moving to the next.

4. Then read the eight returns together (the new CATHOT review will be in pro_reviews_max_20261112\1_CATHOT\ when it exists: read it, never write there): what they establish jointly, any contradictions, and the follow-up questions worth a further prompt to GPT-6 Astra (effort Pro). Write DERIVATEURS_EXPERT\COMBINED_REVIEW.md and FOLLOW_UPS.md.

5. Keep DERIVATEURS_EXPERT\KNOWLEDGE_HANDOFF.md current after each return, so that a successor at effort max can continue if your context runs out: what you read, what you settled, what is open.

Do not open (discarded work): anything under pro_reviews_20261110\, integration_20261111\, checks_first_returns\, returns\, returns_second\; any KNOWLEDGE_HANDOFF.md other than your own; any REVIEW*.md outside pro_reviews_max_20261112.

Done when each of returns 2-8 has its REVIEW.md with a verdict and an argument for every item, and COMBINED_REVIEW.md, FOLLOW_UPS.md, READING_BASE.md, GROTHENDIECK_NOTES.md and KNOWLEDGE_HANDOFF.md exist. Unacceptable: a verdict without an argument; "cite or prove"; labels copied from the returns; taking a return's word for what a source says without reading the source; reviewing a return before reading the Grothendieck passages it concerns. If your context runs low, finish the return in hand, update the handoff, and say in your final message exactly where you stopped.

Final message: for each return, the number of items per verdict and the most important findings; then the main follow-ups.

---

## Standing notes for myself (not part of the brief)

- The background zips of later prompts (5-8) contain copies of the discarded reviews (`*_review/`, `REVIEW_author.md`). Do not open those files. The prompts' "After X" sections and the prompts' README repeat conclusions of the discarded reviews: treat as unverified hearsay.
- `checks\` (the companion audit) was edited on 11 Nov with material from the discarded reviews (METHODOLOGY.md). Prefer the companion files as shipped inside each prompt's zip; treat every companion row as a colleague's draft.
- Tools: python at effort of own checks only; never run the returns' code.

---

## Mid-task messages from the coordinator (received 12 Nov 2026, while reading Chapter I; verbatim)

### Message 1
Addition to your reading list, from the user: many conjectures pertinent to this work have been resolved recently, a good part of it by OpenAI's models, after your training cutoff, so you cannot know from memory what is still open. Before calling anything open or known, read C:\Users\user\Documents\recent_results_20261110\SCOREBOARD.md, RECENT_RESULTS.md, BRIEF_FOR_PROMPTS.md and OPENAI_MATH_INVENTORY.md (the inventory of OpenAI's announced results; skip the .json; do not open proof_packs\ or any .lean file), and search arXiv and the announcements for 2026 results in your field yourself, since that scoreboard dates from 10 Nov. Add everything you use to your READING_BASE.md with its date and location, and say in your reviews when a result you rely on or check against is recent.

### Message 2
Required reading for you, in the papers themselves (OpenAI's manuscripts, github.com/openai/math: CONTENTS.md and lean/docs/<family>.md lead to them; read the mathematics, not the Lean): family 317, Thomason model structures on strict n-categories (the Ara–Maltsiniotis conjecture, claimed 25 Sep 2026; the n = 2 case uses the Grothendieck–Cisinski theory of basic localizers), and family 312, Grothendieck's homotopy hypothesis for coherators in the Ara–Henry convention (claimed 24 Sep 2026). RECENT_RESULTS.md (links L4, L4q, L5) says how they bear on Les Dérivateurs and Pursuing Stacks. Also Kaledin, "Enhancement for categories and homotopical algebra" (arXiv:2409.17489, v3 Feb 2026) and Di Vittorio on 2-derivators (arXiv:2309.05216). Treat the OpenAI results as claimed and unrefereed; check what you use, and take them into account in every verdict and follow-up.

Status of these two messages: see READING_BASE.md, section "Recent results (2026)".

### Message 3 (same day, shortly after)
The papers are already downloaded; read them from disk: C:\Users\user\Documents\recent_results_20261110\papers\317_Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026.pdf and papers\312_The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026.pdf (the folder has 44 such PDFs; take any other that bears on your returns). Do not open recent_results_20261110\proof_packs\.

### Message 4 (same day)
From the user: "Make sure to check the prompting too. For requesting that ProMode push the math, not just comment on the math. That was a previous error." So every item in your FOLLOW_UPS.md is written as mathematics for GPT-6 Astra (effort Pro) to do — a statement to prove or refute, a construction or computation to carry out, an open question with a stated target — never a request to comment, summarize or assign a status. The standard is C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111_work\PUSH_STANDARD_AND_AUDIT_20261111.md.

### Message 5 (same day)
Required reading from the user: our own project has also resolved conjectures, and you must know them while reading, as claims to check. Read C:\Users\user\Documents\grant_evidence\EVIDENCE.md (the Les Dérivateurs entries: the Thomason–Kan envelope, TOTASPH) and C:\Users\user\Documents\french_school_site_20261110\findings\2026-11-10_thomason-kan-envelope.md (Grothendieck asserts at V ms. 37 a fully faithful right adjoint Cat_hot → Hot; the finding is that none exists, that categories up to natural transformation give exactly the 1-types, and that a bounded envelope exists). Check this finding as part of your work where your returns touch it. The full list of required reading is the board card C:\Users\user\Documents\braindump_board\cards\reading-list.md.

### Message 6 (same day)
Note on the recent-results files: RECENT_RESULTS.md and BRIEF_FOR_PROMPTS.md (and the scoreboard's "bears on our work" column) were written by a Claude Fable 5.2 agent at effort medium. Use them only as pointers to the papers; read the papers themselves (recent_results_20261110\papers\) and form your own view. The Dérivateurs prompts 3-7 were also framed by medium-effort agents, so judge each return against what its prompt should have asked as well as what it did ask; the returns themselves are GPT-6 Astra's work at effort Pro.

### Message 7 (same day)
One more step, from the user: none of the earlier review work ran at max effort, so things may have been missed. Throughout, keep a running list DERIVATEURS_EXPERT\FINDINGS.md of every potential finding and implication you notice (new results, sharpenings, consequences for Grothendieck's text, connections between returns or to recent results), even small ones. Only after your own REVIEW.md for a return is complete, open the earlier review of that return (C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\<n>\, written at effort medium) and add to FINDINGS.md, under that return, "Compared with the earlier review": what it missed, where it was wrong or too weak, and where it was right. This lifts the earlier ban only for that comparison, and only after your own review of the return is done.

### Message 8 (same day)
The purpose of your work, from the user: build mathematics prompts for GPT-6 Astra (effort Pro) on the basis of what you read and find. Two kinds: (1) a result you prove yourself outright: write it up fully and draft a prompt asking GPT-6 Astra to check it and push it further; (2) hunches: things you suspect but cannot prove. Hunches are especially interesting; record each in DERIVATEURS_EXPERT\HUNCHES.md with your reasons, and draft prompts asking GPT-6 Astra to prove, refute or develop them. Put each draft in DERIVATEURS_EXPERT\PRO_PROMPTS\<short-name>\PROMPT.md. Every prompt pushes the math (the push standard), states exactly what counts as done for each item, what is unacceptable, and when it is finished, and points to the exact passages of Grothendieck's text it concerns. Later, when all three experts (CATHOT, Les Dérivateurs, La Longue Marche) have finished, each will read the others' notes to look for implications of the combined work; so keep your notes readable to another expert.

## Deliverables list as it now stands (brief + messages 1-8)
In `pro_reviews_max_20261112\<n>\`: REVIEW.md for n = 2..8.
In `DERIVATEURS_EXPERT\`: GROTHENDIECK_NOTES.md, READING_BASE.md, KNOWLEDGE_HANDOFF.md, COMBINED_REVIEW.md,
FOLLOW_UPS.md (every item mathematics to do, push standard), FINDINGS.md (running; plus per return "Compared with
the earlier review", written only after my own REVIEW.md of that return), HUNCHES.md, PRO_PROMPTS\<short-name>\PROMPT.md.
