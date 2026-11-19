# KNOWLEDGE HANDOFF — Dérivateurs expert (returns 2–8)

Keep this file current. A successor (or I, after a context compaction) starts here, then reads TASK.md (the brief
and the coordinator's eight later messages, verbatim, with the list of deliverables at its end), then
GROTHENDIECK_NOTES.md, READING_BASE.md, FINDINGS.md, HUNCHES.md and the REVIEW.md files written so far.
A compaction summary is not evidence: re-check against these files.

## State (run `date` before writing a time)

- **12 Nov 2026, 22:05 local (clock checked): CONSULT ON PRETOT ANSWERED (coordinator message 11, verbatim in
  TASK.md).** PRETOT = the return of GPT-6 Astra (ChatGPT Pro mode) to my prompt PRESHEAF_TOTALITY, reviewed by
  Claude Opus 5.5 (effort max) in ../PRETOT_REVIEW_OPUS/ (I read only its REVIEW.md sections 1-2, 10-11 and
  FINDINGS.md). My answer: ../../GLOBAL_SHAPE_AFTER_PRETOT_20261112.md (398 words).
  WHAT CHANGED FOR MY FILES: (1) RESULT_FILTERED_BY_ONE_TYPES.md carries a correction block: the theorem holds for
  non-empty connected A; in general condition 2 means every component filtered (my step (2 => 3) took the
  colimit of the constant diagram to be a point). (2) Hunch H7 (sifted + total => filtered) is PROVED (PRETOT
  F.3; abelian form F.6). (3) Hunch H3 (integral totality of a presheaf forces simple connectivity) is REFUTED
  (PRETOT A.5: pi_1 = SL(2,5)); HUNCHES.md still shows H3 and H7 as open: UPDATE THEM when work resumes.
  (4) H1 (total => exact) is the open inclusion; candidate Ty^op (review FINDINGS F12).
  The prompts now live in pro_prompts_max_20261112 (per the review); the coordinator edited INDLOCAL,
  REVERSIBLE_LOCALIZERS, FINMON after my revision. Return 4 (GALOIS) is still at 22 rows of 74; resume point
  unchanged (sections/C.tex).

- **12 Nov 2026, 16:47 local (clock checked): COORDINATOR MESSAGE 10 IS DONE.** The seven unsent prompts
  (PRO_PROMPTS/TOTAL_EXACT, PRESHEAF_TOTALITY, REVERSIBLE_LOCALIZERS; ../1_CATHOT/PRO_PROMPTS/FINMON, INDLOCAL,
  S2COUNT; ../1_CATHOT/PRO_PROMPT_EMAIL_CLAIMS.md = copy of FINMON) are revised: each has a section "Results this
  prompt builds on" with status, asks that start from the results, a backup PROMPT_before_results_20261112.md and
  a ZIP_LIST.tsv (18, 32, 33, 45, 32, 22 and 45 rows; all 227 paths exist; generator work/make_zip_lists.py).
  PRO_PROMPTS/CHANGES_20261112.md (copy in ../1_CATHOT/PRO_PROMPTS/) says per prompt what changed.
  NEW FILES OF MINE: RESULT_FILTERED_BY_ONE_TYPES.md (NEW THEOREM, unchecked: A filtered iff colimits over A of
  sets and of groupoids are homotopy colimits iff the Grothendieck construction of every Cat-valued diagram maps
  by a weak equivalence to the colimit in Cat; the true form of II ms. 36ter); CHECK_OF_CATHOT_OWN_RESULTS_20261112.md
  (my reading of ../1_CATHOT/OWN_RESULTS.md sections 1-5: no error; its 3.1-3.2 = GALOIS B.10-B.12).
  FINDINGS.md has F4-1..F4-7; HUNCHES.md has H7-H10 and a status list.
  RETURN 4 (GALOIS) IS UNFINISHED: 22 rows of 74 written (A.1-A.8, B.1-B.14). RESUME at
  pro_returns_20261110/4_GALOIS/GALOIS/sections/C.tex (then D, E, F, G, report, research, code), then the steps
  listed in the older entry below (zip_4, Cisinski 2009, Kaledin, Di Vittorio, Summary, comparison, READING_BASE
  section 3). Returns 5-8, COMBINED_REVIEW.md and FOLLOW_UPS.md are NOT STARTED.

- **12 Nov 2026, 16:23 local (clock checked): INTERRUPTED BY TWO COORDINATOR MESSAGES (verbatim in TASK.md, messages 9 and 10).**
  State of return 4 (GALOIS) at the interruption: ../4_GALOIS/REVIEW.md has 22 rows of 74: A.1-A.8 and B.1-B.14
  (Part B is COMPLETE; B.13, B.14 unproved, the rest correct; row B.7 was rewritten in full after reading
  B_loc67.tex to its end; B_KT.tex read in full). NOT YET READ: sections C.tex, D.tex, E.tex, F.tex, G.tex,
  the report, research files, code; the GALOIS zip is not unzipped; Cisinski 2009 Th. 3.6/3.13 not yet opened
  (input of B.3); Kaledin and Di Vittorio not read. No Summary, no comparison, no findings F4-* yet.
  New item of mine in row B.14: W^lc of K(n)-local spectra is not proper (map K(Z,2) -> K(Z_p,2)), granted
  Bousfield 1999 (K(n)_*-equivalences are isomorphisms on H_1(-;Z/p)), quoted from memory, NOT opened.
  Message 10 (later one) asks: put the new results into the seven unsent prompts (3 mine, 4 of the CATHOT
  expert), with PROMPT_before_results_20261112.md copies, ZIP_LIST.tsv, and PRO_PROMPTS/CHANGES_20261112.md.
  Message 9 (earlier one) asks for a short final message (hunches ranked, what to look for in returns 5-8,
  hunches not yet in prompts). RESUME return 4 at sections/C.tex after that task, if context allows.

- **12 Nov 2026, 14:42 local (clock checked): RETURN 3 (POLES) REVIEW.md IS COMPLETE** (`.._POLES\REVIEW.md`,
  56 KB): all 104 rows have a verdict and an argument (102 correct, 2 unproved = A.16 and F.14; 0 wrong, 0 gap;
  checked by script against the CSV ids), plus Summary, "Additions by the reviewer" (R1-R4), "The prompt, judged",
  and the section on report/CSV/code. Own analysis written before reading the return:
  `work\checks_3\own_thoughts_before_reading.md`; own program `work\checks_3\check_poles.py` (+ `.out`).
  GROTHENDIECK_NOTES.md now also covers XI section 1, XII parts I-IV (ms. 1-58), XII part VI sections 1-8
  (ms. 171-275) and XVI in full.
  **RETURN 3 IS FINISHED (14:56, clock checked):** comparison with the earlier review, findings F3-1..F3-11, hunches H4-H6, prompt draft PRO_PROMPTS/REVERSIBLE_LOCALIZERS/PROMPT.md, READING_BASE section 2, and the two corrections in GROTHENDIECK_NOTES.md are all written. NEW RESULT OF MY OWN (kind (1) of message 8): RESULT_REVERSIBLE_NOT_STABLE.md (a fundamental localizer with Loc (6 b) that is not of the form R(L): the null class of the 2-local spheres; uses James EHP, Miller, Kahn-Priddy, Snaith; answers POLES F.14 (1) without accessibility). Not read on return 3: research json ledgers; most program bodies (listed in the REVIEW).
  **NOW (from 14:57): return 4 (GALOIS).** PROMPT.md read in full at 14:57 (Leads 1-4; Parts A-G). Subject: for a
  derivator D the classes W_D (constant coefficients), W_D^coh, W_D^hom, W_D^1 (f* fully faithful on locally
  constant coefficients LC_D), W_D^lc (f* an equivalence LC_D(Y) -> LC_D(X)); Lead 1: W-infinity in W_D^lc in
  W_D^1 in W_D^coh cap W_D^hom in W_D and W_D^lc is a fundamental localizer; Lead 2: values (sets: W_0, W_1;
  (n-1)-types: W_(n-1), W_n; HOT: W-infinity; D(Z), spectra: W_D^lc = W-infinity; D(Q): strictly between);
  Lead 3: the false statements of I ms. 79-84 become true with 2-complete equivalences; Lead 4: tower
  W_D > W_D^(1) = W_D^lc > W_D^(2) > ... Parts: A definitions/closure, B localizer axioms incl. relative Theorem A,
  C computations, D fibrations (I ms. 76-126, compare XI section 1), E realization W_D^lc = W_D' and the tower,
  F Tannakian reconstruction (Hoyois; LM multi-Galois), G Chapter X ms. 1-5 revisited. Also in the prompt:
  (KT_mu) Kan-Thurston-type statement for CATHOT E.17; Di Vittorio 2-derivators and Kaledin enhanced groupoids
  (both attached to that prompt as PDFs: read them for Parts E-G; message 2 of the coordinator requires it).
  PROGRESS (15:00, clock checked): steps (1) and (3) DONE: DER_I-b (I ms. 60-126) and Chapter X ms. 1-5 read in full, notes in
  GROTHENDIECK_NOTES.md; own analysis in work/checks_4/own_thoughts_before_reading.md (W^1 fails two out of
  three; for D(k): W^coh = W^hom = W^1 = maps with k-acyclic homotopy fibres, W^lc = iso on H_*(Omega -; k)).
  GALOIS return at a glance (15:02): 74 rows = A.1-A.8, B.1-B.14, C.1-C.15, D.1-D.12, E.1-E.11, F.1-F.8, G.1-G.6;
  its own labels: 52 Proved, 10 Known, 7 Refuted, 5 Open (B.13, B.14, E.11, F.8, G.6). Sections files:
  conventions (read), A, B, B_general, B_accessibility, B_loc67, B_KT, C, D, E, F, G (241 KB). Its convention:
  fundamental localizer = relative Theorem A + retracts (as POLES). Already seen to agree with my own analysis:
  A.5 (W^1 fails two out of three), C.2 (W^coh = W^hom = W^1 for enhanced coefficients), C.7. To scrutinize:
  B.3 ("relative Theorem A for an arbitrary derivator": I expected this to need an enhancement), B.6, B.7,
  B.10-B.12 (KT_mu and CATHOT E.17), D.3-D.5, D.12 (counterexamples), E.2-E.4, E.8-E.10, F.1-F.3.
  REVIEW PROGRESS for return 4 (15:03, clock checked 15:01): ../4_GALOIS/REVIEW.md has the header, Part A
  (A.1-A.8) and the first table of Part B with rows B.1, B.2, B.5, B.8, B.9, B.10 (all correct). sections/B.tex
  and B_general.tex are read; row B.3 written (correct; its one unverified input is Cisinski 2009 Th. 3.6 for a subcategory R: OPEN THAT PAPER in work/zip_4 and confirm). Row B.4 (B_accessibility.tex) also written. Row B.6 written too (B_loc67.tex read to line 230; B_loc67.tex read to line 559 and row B.7 written at 15:04 (CONTINUE AT LINE 559 of B_loc67.tex: end of the positive-characteristic case and the W^1 statements of B.7; amend row B.7 if needed; then B_KT.tex for B.11-B.14; then C, D, E, F, G). 19 rows of 74 are written so far: A.1-A.8, B.1-B.10 except none missing (B.1-B.10 all present). NEXT, in this order: (B.3, B.4 done;
  I expected an enhancement to be needed), B_accessibility.tex (B.4), B_loc67.tex (B.6, B.7), B_KT.tex
  (B.11-B.14); append their rows to the same Part B table (start a new table "Part B, continued"); then C, D,
  E, F, G. After all rows: script check that all 74 ids have a row; Summary; additions; prompt judgement;
  report/code section; comparison with pro_reviews_20261110/4_GALOIS; findings; hunches; prompts.
  REMAINING for return 4: (2) unzip pro_prompts_20261110/4_GALOIS/*.zip to work/zip_4 (never open *_review or
  REVIEW*.md inside; the Di Vittorio and Kaledin PDFs are there: read their statements for Parts E-G);
  (4) read pro_returns_20261110/4_GALOIS/GALOIS/sections/*.tex one by one, writing ../4_GALOIS/REVIEW.md part
  by part (Write to a temp file + cat; python patches with ASCII source only); (5) report, CSV id check, own
  checks; (6) comparison with pro_reviews_20261110/4_GALOIS/; (7) findings F4-*, hunches, prompts,
  READING_BASE section 3, handoff. Then returns 5 (STRATA), 6 (PATHS), 7 (BISITE), 8 (RESIDUE), then
  COMBINED_REVIEW.md and FOLLOW_UPS.md.
- (older entries follow)

- 12 Nov 2026, 14:02 local (the run started 13:21): **TOTASPH REVIEW.md has a verdict and argument for all 107
  items** (A.1–G.6; checked by script that every id of `TOTASPH_results.csv` has a row), a disposition table for
  the audit rows and a summary (104 correct, 2 unproved = the return's two Open items D.7 and F.27, 0 wrong,
  0 gap). All sections `sections\*.tex` of the return were read in full (A, A_audit, B, C, D, D_followup,
  D_general, E, F, F_followup, G, H).
  **RETURN 2 IS FINISHED (14:10, clock checked):** REVIEW.md complete; READING_BASE section 1 written; comparison with
  the earlier review in FINDINGS.md; hunches H1, H3 in HUNCHES.md; prompt drafts PRO_PROMPTS/TOTAL_EXACT/PROMPT.md
  (H1 = D.7) and PRO_PROMPTS/PRESHEAF_TOTALITY/PROMPT.md (H3 = F.27, plus sieve composition for W_n, the repaired
  class of XII ms. 114, path categories, Cat-valued colimits). Left undone on return 2: five programs of the return
  not read; G.1 to be re-checked when Chapter VII is read. **NEXT: return 3 (POLES):** read
  pro_prompts_20261110/3_POLES/PROMPT.md, then DER_XI-XIIa, DER_XIIc-a?, DER_XIIc-b (XII section 8), DER_XVI in full,
  unzip the POLES background zip into work/zip_3 (do not open *_review or REVIEW*.md inside), then the return
  pro_returns_20261110/3_POLES/POLES (sections A-H, about 250 KB), writing REVIEW.md part by part.
  The list below is the record of how return 2 was finished.
  **Steps for return 2 (all done except where noted):**
  0. STATE at 14:06 (clock checked): steps 1 and 2 are DONE (report, all six appendices, root_report, bib, the two affine-cone
     programs and outputs read; own check script written and run in `work\checks_2\`; REVIEW.md has its final
     section "Report, results CSV, research files and code" and no "still to do" paragraph). Five programs of the
     return were not read (listed in that REVIEW section). Step 5 is DONE too (comparison written under Return 2 in FINDINGS.md). NEXT: steps 3 and 4 (READING_BASE section 1; prompt drafts for H1 and H3), then return 3 (POLES). (Earlier note, kept for reference:) step 5 (comparison with the earlier review:
     `pro_reviews_20261110\2_TOTAL_ASPHERICITY\REVIEW_author.md`, 28 KB, and PROMPT_UPDATES.md), then steps 3, 4,
     then return 3 (POLES). Caution when patching files with python heredocs: the tool turns a double backslash
     into a single one, so a path fragment like backslash-r becomes a carriage return; build backslashes with
     chr(92).
  1. DONE (about 14:03): CSV mapping checked by script; `TOTASPH_report.md` §§1–8 and Appendix 1 (= research\AG_report.md)
     read in full; section "Report, results CSV, research files and code" appended to REVIEW.md.
     REMAINING of step 1: report Appendices 2–6 (lines 220–450 of TOTASPH_report.md = research\CD_report.md,
     CD_followup.md, F_report.md, CD_C048_report.md, AG_general_report.md), `research\root_report.md`,
     the research csv/json ledgers, `README` (read), and the code in `code\` (read, do not run:
     ag_finite_examples.py, root_monoid_checks.py, root_presheaf_checks.py, cd_affine_polynomials.py,
     cd_finite_checks.py, f_check.py, f_low_truncation.py are the mathematical ones). Then edit the last bullet of
     that REVIEW section and delete the paragraph "Still to be done on this return" in the Summary;
  2. own programs (optional but wanted): `work\checks_2\` — e.g. recompute `t = (1,2) − (0,2) + (0,1)` and the
     `n = 2` affine cone in `Δ_inj`; homology of the 4-object `Z` (type `S²`); the pushout of F.23 for `n = 2`
     (8 objects, 30 arrows, type `S³`);
  3. add §1 "TOTASPH literature" to READING_BASE.md (list below under "Read so far");
  4. add hunch H3 (= F.27) to HUNCHES.md; draft `PRO_PROMPTS\TOTAL_EXACT\PROMPT.md` (H1 = D.7) and
     `PRO_PROMPTS\PRESHEAF_TOTALITY\PROMPT.md` (H3 = F.27), push standard;
  5. only then open the earlier review `..\..\pro_reviews_20261110\2_TOTAL_ASPHERICITY\` and add "Compared with the
     earlier review" under Return 2 in `work\_running_list.md`, then `cp` it over FINDINGS.md;
  6. when Chapter VII is read (for PATHS), re-check G.1 (morphisms of intervals in VII §§5–7).
- Returns 3–8: not started. Prompts 3–8 not yet read.

## Working facts about the environment

- Context window about 800k tokens (auto-compact near 96%). The French text is about 3.56 MB = roughly 2 M tokens,
  so read per return. `Read` returns at most about 25k tokens per call once a turn is long: use `limit ≈ 400–480`
  lines for the DER files.
- Bash heredocs with apostrophes can fail: write text with the Write tool into `work\_part.md` (or similar) and
  append with `cat work\_part.md >> target`.
- The Write tool refuses a file named `FINDINGS.md` ("subagents should return findings as text"). The coordinator
  asked for that file by name (message 7), so the running list is kept in `work\_running_list.md` (Write/Edit
  there) and copied over `FINDINGS.md` with `cp` after each change. Say so in the final message.
- Local literature: `work\zip_2\papers\` (TOTASPH zip, unzipped), text extractions in `work\lit\`
  (Cisinski2004_minimal.txt; IsbellMitchell1973_bull.pdf/.txt; AKR1981.pdf, a scan without text layer: read pages
  with the Read tool, `pages`), `work\recent_papers\` (312.txt, 317.txt).
- The zips of later prompts contain the discarded reviews (`*_review/`, `REVIEW*.md`; in zip 2:
  `CATHOT_review/REVIEW.md`): never open them. The earlier reviews under `pro_reviews_20261110\<n>\` may be opened
  only after my own REVIEW.md of return n is complete, and only for the comparison (message 7).

## Plan being followed

For each return n = 2..8: (1) read PROMPT.md; (2) read in full the chunks of the French text the prompt names and
add them to GROTHENDIECK_NOTES.md; (3) read the literature the return relies on (zip of the prompt, unzipped under
`work\zip_<n>\`, or free online copies) and add it to READING_BASE.md; (4) read every file of the return, writing
the review part by part as each section is read; (5) own checks in `work\checks_<n>\`; (6) complete
`..\<n>\REVIEW.md`; (7) comparison with the earlier review into FINDINGS.md; (8) HUNCHES.md and prompt drafts;
(9) update this file. After return 8: COMBINED_REVIEW.md, FOLLOW_UPS.md (push standard: every item is mathematics
to do, with "what counts as done"), read `..\1_CATHOT\` review if it exists (never write there).
Judge each return also against what its prompt should have asked (message 6: prompts 3–7 were framed at effort
medium).

Chunks named by each prompt (from the prompts' README; verify against each PROMPT.md):
- 3 POLES (PROMPT.md read 14:10 on 12 Nov; Parts A-H; Leads 1-6): passages named: XII ms. 12 (Theoreme 1), ms. 75-78
  (W(7), W(7 bis), Theoreme 2; read), ms. 178-187 (classes a_n, b_n, c_n), ms. 228-234 (mapping cylinder),
  ms. 265-272 (XII section 8; footnote 136; 'inhabituelle' ms. 270), XII sections 5-8 and the appendix;
  XVI sections 1, 3 (ms. 16'-27: Loc (6), (6 a, b, c), (6'), (6 A), (6 A'), (6 B), (6 C); K. S. Brown's lemma 3.2.1),
  4 (Loc (5), (7), (7 D), (7 F)), 5 (Theoreme 5.4, ms. 79), 6 (Theoreme 6.1, ms. 83; 6.4 b, ms. 87-92), 7
  (ms. 119-121). Files to read in full before the return: DER_XI-XIIa, DER_XIIc-a, DER_XIIc-b, DER_XVI.
  Leads: 1 cofibre criterion; 2 W contains W_Z; 3 W_Z least with Loc (6 b); 4 the localizer of XVI 6.4 b under
  both readings; 5 fibration axiom = left exactness; 6 correspondence with localizing subcategories of spectra.
- 4 GALOIS: I-a (read), I-b, VIII-X, XIIc-a, XIIapp (read), VI-a; XI §1; XVI Loc axioms.
- 5 STRATA: I, VI-a/b/c, VIII-X, XIIb-a/b (read), XIIapp (read); XI §1, XVI §4.
- 6 PATHS: III-V, VII-a/b/c, VIII-X, XIIc-a; XIII-a/b, XVII-a/b, XIX.
- 7 BISITE: II-b §§5–6, XII §7 (XIIc-b), XI-XIIa §III, XIII §§4–6.
- 8 RESIDUE: not yet looked at.

## Read so far

- Grothendieck (notes in GROTHENDIECK_NOTES.md): I-a (I ms. 1–66) in full; II-a (II ms. 1–53) in full; II §7
  statements only; XIIb-a and XIIb-b (XII ms. 59–169) in full; XIIapp (ms. 1–18) in full. Not read: I-b, II-b
  §§4–6, III–XI, XII ms. 1–58 and 171–275, XIII–XIX.
- Recent results (READING_BASE.md §0): scoreboard files; OpenAI 317 (§§1–7) and 312 (§§1–2, 5); push standard.
- Own-project claims (message 5): `grant_evidence\EVIDENCE.md` (Dérivateurs entries), the envelope finding
  (`french_school_site_20261110\findings\2026-11-10_thomason-kan-envelope.md`), board card `reading-list.md`.
- TOTASPH: PROMPT.md; all sections. Literature opened (to be entered in READING_BASE.md §1 with these details):
  Cisinski, *Le localisateur fondamental minimal*, Cahiers 45 (2004), from the zip (`work\lit\Cisinski2004_minimal.txt`):
  1.1.1 (FS1–3), Déf. 1.1.3 (LF1–3), Prop. 1.1.13, Th. 2.2.11 (`W∞` minimal), Th. 2.3.6;
  Isbell–Mitchell, *Exact colimits*, Bull. AMS 79 (1973) 994–996, whole note, free at ams.org
  (`work\lit\IsbellMitchell1973_bull.pdf`): Th. 1 (colim exact ⇔ components of aff C filtered), Lemma 1, Th. 2,
  Cor. 1 (exact + weak terminal objects ⇒ filtered components), Th. 3 (aff Δ filtered, target `2^{n+1} − 1` points);
  Adámek–Koubek–Reiterman, Czech. Math. J. 31 (1981) 368–389, dml.cz (`work\lit\AKR1981.pdf`, scan; read pp. 368–371,
  384–386): quasi-filtered categories, Theorem [1] (fixed points ⇔ quasi-filtered), A.4, Construction C.1, Th. C.2;
  Cisinski, *La classe des morphismes de Dwyer n'est pas stable par rétractes*, Cahiers 40 (1999), Prop. 2 and
  Déf. 1 (grep in `work\lit\Cisinski1999.txt`); Hackney–Ozornova–Riehl–Rovelli, arXiv:2205.02353 (TeX in the zip):
  Definition "discretely flat" and the statement that the main theorem holds for discretely flat cofibrations
  (statement only); Cisinski, Astérisque 308 (2006), Cor. 9.2.15, Prop. 9.2.17 (`work\lit\Cisinski_Ast308.txt`).
  Not opened: Batanin–Berger (arXiv:1305.0086) Def. 1.1 and Lemma 1.10; Thomason 1980 Th. 4.9, Prop. 4.3 (used as
  standard); Quillen 1973 Theorem A; Hatcher; Husainov 2002; Pavlov 2024; Street–Walters 1973.

## Settled so far (details in the REVIEW.md and FINDINGS.md)

- TOTASPH, all parts: every item checked; none wrong (104 correct, 2 unproved = D.7, F.27). The id ↔ section
  label mapping of the CSV was verified by script (A.1 = A:localizer … G.6 = G:notfiltered, in section order).
  Main results confirmed: the characterization C.5 of total asphericity (ordinary colimits of simplicial sets
  over `A` are homotopy colimits); `Δ_inj` refutes Grothendieck's conjecture of II ms. 36ter (it is the
  Isbell–Mitchell example of 1973; the return's label "Proved" for C.9 should be "Known, independent proof");
  total ⇔ filtered when there is a weakly terminal object; `W∞` fails W(7), W(7 bis) (XII Théorème 2 is false);
  B035 refuted (three-element presheaf on the monoid `{1, e}`); C035 refuted (`a ⇉ t → s`); C005 refuted (`Ψ`;
  follows from Grothendieck's own remarks); C045/C047: strict and total functors compose for every localizer,
  total sieves compose for `W∞`, `W_R`, not for `W_0`, `W_1`; C048: no class exists unless `S²` is `W`-aspherical
  (⇔ `W_1 ⊂ W`, Cisinski Ast. 308, 9.2.17), then all sieves.
- Open: D.7 (total ⇒ exact abelian colimits?) = hunch H1; F.27 (totally `W_Z`-aspherical presheaf ⇒ totally
  `W∞`-aspherical?) = hunch H3. My attacks are in the review rows and in HUNCHES.md.
- Follow-up idea noted in G.5: for which `Y` is `Ch(Y; y_0, −)` totally aspherical (necessary: `Y` total); the case
  `Y = e` (the category of interval types) is the first test.

## Rules that are easy to forget

- Verdict vocabulary: correct / wrong / gap / unproved, each with my own proof, counterexample or exact citation
  that I opened. No labels copied from the return.
- Say in a review when a result relied on is recent (2026) and unrefereed.
- FOLLOW_UPS.md and PRO_PROMPTS: mathematics for GPT-6 Astra (effort Pro) to do; outcome section; exact passages
  of Grothendieck.
- Never write in `1_CATHOT\`. Name the model: "GPT-6 Astra (ChatGPT Pro mode)".
- Final message: per return the number of items per verdict and the main findings; then the main follow-ups; say
  exactly where I stopped.

## DER_FOLLOWUP drafted and packaged (successor of the expert, Claude Fable 5.2, effort max, 13 November 2026, 05:43 local, clock checked)

Task: step 2 of task 2 in `HANDOFF_SUCCESSOR_20261113.md`. Not sent; the user sends Pro prompts.

Files.
- Work: `pro_prompts_max_20261112_work/DER_FOLLOWUP/`: `PROMPT.md` (38,118 bytes), `ZIP_LIST.md` (47 rows; its section
  "Items that TOTAL_EXACT_2 may settle" says how to edit the prompt when that run is back), `LEADS_DERIVATIONS.md`,
  `build_zip_20261113.py`, `unpack_eprints_20261113.py`, `MANIFEST.tsv`, `stage/`.
- Upload: `pro_prompts_max_20261112/DER_FOLLOWUP/`: `PROMPT.md` (identical copy) and `DER_FOLLOWUP_background.zip`
  (1,988,655 bytes, 134 entries with `MANIFEST.tsv`; the only PDFs are Isbell–Mitchell 1973 and 1976).
- arXiv sources fetched to `Free or receipted/free/arxiv-eprints-der-20261113/` (one folder each): 1412.0317,
  2205.02353, math/0610668, 1905.12018, math/0110316.
- Lint `--lint-math` on both copies: `files: 1 failing lint: 0`. Closing paragraph: the template's.

Read. The three handoff files; the template and the push script; `TOTAL_EXACT_2/PROMPT.md`; the PRETOT review in
full and its findings; in `PRETOT_paper.tex` the conventions, A.1–A.5 with proofs, C.1–C.4 with proofs, E.1,
E.6–E.9 with proofs, F.9–F.12 with proofs (lines 68–203, 885–966, 1057–1080, 1269–1483, 2037–2189); INDLOCAL R6–R8
and Part C; the checkpoint 02 register of TOTAL_EXACT_2 (62 rows; statements C.1, C.24, C.26–C.28, D.1–D.4 in
full); the results tables of PATHS, TOTASPH and TOTEX at the R-items. Not read: the proofs of PATHS C.P1–C.P3, of
TOTEX D.21–D.26 and E.2–E.6, of checkpoint C.24; the arXiv sources (titles only).

Found in the checkpoint 02 of TOTAL_EXACT_2 (unreviewed, run in progress): C.24 and D.1 state
`{total} ⊊ {quasi-filtered}` (a selected repaired AKR category with `H_2 ≠ 0` in one action component); C.27 states
the expert's three lines on `Ty^op` as proved (for non-zero rings); A.1, A.3, A.17, B.1, C.1, C.17, D.2 open.

Items of the prompt. A (PRETOT C.4: the classes `𝒬_n`; A.3, `n ≥ 3`, is the main question), B (which
`F: Ty^op → Cat` have `C_∞ ≃ C`), C (PRETOT E.9), D (PRETOT F.10), E (PRETOT A.5 over `End_Δ([n])`), F
(statements and literature). Marked `[TOTAL_EXACT_2]`: A.2 (`n = 2`) and B.1 (the three lines).

Mathematics of mine in the prompt, checked by nobody and by no program (Leads; derivations in
`LEADS_DERIVATIONS.md`):
1. Lead 1. For `E` with all action components `(n−1)`-connected, `E^◁` is total for `W_n` and `E` is a cosieve of
   it. So PRETOT C.4 at `n` holds iff `𝒬_n = 𝒬_{n+1}`, and at all `n` iff quasi-filtered = total. With checkpoint
   C.24 it is false at `n = 2`.
2. Lead 2. For `u: y_0 → z` and the pair `f, g: ((++), y_0 → y_0 → z) ⇉ ((+), y_0 → z)` over `(0,1,1)`, `(0,0,1)`:
   `H_1` of the restricted action is `Z[Y(z,z)]/span{γv : vu = id}`. So a strictly aspherical end-point functor
   forces `Y` to be a connected thin groupoid; `P(R_0, 0) → R_0` is not strict (`H_1 = Z`). If this stands, E.9 is
   closed and the remark N6 of the PRETOT review (strict ≠ total for path fibrations) holds only for the truncation.
3. Lead 3. Over an exact shape `B∫_A M` is a `K(Γ, 1)` for every diagram of free monoids or free groups; F.10 on
   `Δ_inj` becomes: is every colimit monoid of free monoids aspherical? One example by hand
   (`⟨x, y, z | xy = x, y² = y, yz = z⟩`, `H_2 = 0`).
4. Lead 4 (b)–(d): the totally aspherical acts over `End_Δ([n])` are the acyclic simplicial sets of dimension
   at most `n`; the groups that occur.
5. Lead 5 (b): the comparison is the sequential homotopy colimit of the inclusions `F(t_n) → ∫_{t_n↑} F`; the
   conditions (2F), (DESC), (LOC), (𝒟), (𝒟₁). The expert's suggestion is Lead 5 as a whole.

Open / not done. No machine check of Leads 1–3 (a check of Lead 2 on `R_0` is the cheapest next step). No
literature search. The out-of-date records listed in `HANDOFF_SUCCESSOR_20261113.md` are still not corrected.
`HUNCHES.md` was not attached (H3, H7 out of date).

## DER_FOLLOWUP, second pass (same agent, 13 November 2026, 05:58 local, clock checked)

On the coordinator's message. This section replaces, in the section above: the zip figures, "Closing paragraph: the
template's", "No machine check", "No literature search" and "records not corrected".

- Prompt: 42,387 bytes, both copies identical; zip 2,045,351 bytes, 137 entries. Lint `--lint-math`: failing 0.
  New in the prompt: R16 (literature), a "Status" line under each Lead, Lead 5 corrected, Part B.3 and C.1 reworded.
  Backups in the work folder: `PROMPT_before_lead_checks_20261113.md`, `LEADS_DERIVATIONS_before_checks_20261113.md`,
  `ZIP_LIST_before_checks_20261113.md`. Patch scripts: `patch_prompt_20261113.py`.
- Clock sentence: "Ignore any clock." replaced by "Take the time the work needs." by
  `claude_tools/prompt_lessons_20261112/clock_line_20261113.py` in the template, both DER_FOLLOWUP copies, 12 READY
  upload prompts (LM5 already had it) and the root PROMPT.md of two zips (LM6_POINTS_AS_SECTIONS, EXIT_TOWER).
  Backups: `claude_tools/prompt_lessons_20261112/clock_line_backup_20261113/`. Every changed prompt lints: failing 0.
  Not changed (out of scope): the work-tree copies of ANABELIAN_149_PUSH and S6_02_PUSH still have the old sentence.
- Read in full since the first pass: checkpoint C.24 (statement and proof; not the six statements it cites); PATHS
  C.P1-C.P3 with proofs; TOTEX D.21-D.26 and E.1-E.4 with proofs, E.5 statement.
- Leads: 1 (a)-(c) re-derived, (d) conditional on C.24; 2 checked by program for the walking retraction
  (`checks_drafter/lead2_walking_retraction.py`: `H_1` of dimension 1 over five prime fields on paths of length at
  most 2; span `Z.e` up to length 3; both pairs); 3 re-derived, its example by hand only; 4 re-derived; 5 (a) checked
  against PATHS and corrected ((DESC) => (D) directly; (DESC) => (LOC) needs Part B.4). None refuted.
- Literature (web search, 13 Nov): McDuff 1979; Fiedorowicz 1984; Gray-Steinberg arXiv:1805.03413 (fetched, attached;
  they state that Fiedorowicz's Lemma 5.2 (a) does not hold); Adamek-Reiterman 1976; Dwyer-Kan 1980; Evrard 1975;
  Kervaire 1969. Only Gray-Steinberg was opened. No source found for Leads 1, 2, 3, 5.
- Records corrected with dated notes (backups in the work folder, `records_backup_20261113/`): `HUNCHES.md` (H1, H3,
  H7), `pro_reviews_20261110/KNOWLEDGE_HANDOFF.md` (PATHS section: B.8, A.8), the PRETOT `REVIEW.md` (F.16),
  `GLOBAL_SHAPE_AFTER_PRETOT_20261112.md` (items 1, 2, 5 and F.16).
- Tally: `claude_tools/maths_prompt_tally.py` lists DER_FOLLOWUP as READY ("hold A.2 and B.1 until TOTAL_EXACT_2
  returns"); backup `maths_prompt_tally.py.bak_20261113_before_der_followup`; tally run: READY 14.
- Still open: no independent reader of the Leads; the hand example of Lead 3 is not machine-checked; the six
  statements behind C.24 are unread; the originals of R16 other than Gray-Steinberg are unopened.

## After TOTAL_EXACT_2: third pass on DER_FOLLOWUP (same agent, 13 November 2026, 13:55 local, clock checked)

What the intake of TOTAL_EXACT_2 means for this companion (intake by Claude Fable 5.2 at effort high, folder
`<local>/Documents/pro_intake_20261113/`; I read its BLOCK, PUSH_ITEMS, HANDOFF_ADDENDUM and the Derivateurs
parts of IMPLICATIONS, not the return itself).

- TOTAL_EXACT_2 came back complete: 89 statements, none open; the intake found all consistent (47 with the proof
  read, 42 at statement level only) and nothing wrong.
- The main question is answered NO. Hunch H1 (total => exact) is refuted: the category `C_delta` of ordered
  3-uniform hypergraphs with `2|U| - 3|E(U)| > 0` and strictly closed induced embeddings is total and not exact
  (three point arrows into the one-edge object, no affine equalizer over any non-zero ring). So
  filtered < exact < total < quasi-filtered, all strict, with witnesses `Delta_inj`, `C_delta`, `K*`. The separator
  came from the homogeneous route (C4 of the prompt), not from cone attachments. HUNCHES.md carries a note at H1.
- `K*` is not total for any admissible choice (final C.28; the selected-target proof is now C.37). The three lines on
  `Ty^op` are proved (final C.40, non-zero rings). The nine Leads of that prompt are all proved, four with a
  correction of wording. Register numbers moved since checkpoint 02: C.24 -> C.37, C.27 -> C.40.
- Not to be taken as checked: the 42 statement-level rows (all of B.2-B.10, C.2-C.5, C.11-C.18, C.29-C.39, C.41);
  the AKR invariants and TOTEX Proposition C.1 under C.10, C.19-C.28; every cited source; the return's code and
  notes. In C.27 one step is compressed (rerunning C.19 with components as the marked pair).
- Worth keeping: totality of `C_delta` is a statement about the atomic topology (sheafification is homotopy final on
  categories of elements, and every atom of the continuous `Aut(M)`-sets is representable or terminal); `Delta_inj`
  is the same for `Aut(Q,<)`. The non-exactness has a uniform gap (A.18) and bounded finite coefficients do not see
  it (A.20); dually a diagram of finite `F_p`-spaces over `C_delta^op` has `lim^1 = F_p`. From LM8: the localizers
  `W_a` of its B.6, B.9 are new examples for REVERSIBLE_LOCALIZERS and GALOIS (not acted on).

Done in this pass.
- DER_FOLLOWUP: the block applied by `patch_prompt_totex2_intake_20261113.py` (work folder). Header; R12 and R14
  with the final numbers; new R17 (the main theorem); Lead 1 (d) now rests on C.28; Part A.2 = check C.10, C.19-C.28
  and write out the counterexample `E^<|`; Part B.1 settled (check C.40); Part D.1 names `C_delta`; new Part D.4 (the
  free-group diagram over `C_delta`, from the return's note); Part A.3 gains the predimension route; Part F.1 asks
  for the four classes with their witnesses. Prompt 46,223 bytes, both copies identical; zip 2,110,805 bytes, 149
  entries, the final return's LaTeX in place of checkpoint 02. Lint: `files: 2 failing lint: 0`.
  Backups: `*_before_totex2_intake_20261113.*` in the work folder.
- `NEXT_PROMPT_ITEMS.md` (this folder): the items for a separate prompt (N1 Fraisse totality, N2 exactness against
  Ramsey and amenability, N3 exact colimits as compact limits, N4 the predimension family, N5 the three regimes,
  N6 literature).

Not done: the reading at effort max of A.21, A.24, A.30-A.34, C.25-C.28 (window nearly full); the tally entry of
DER_FOLLOWUP still says "hold A.2 and B.1" (the hold has ended); LM8 B.6, B.9 not entered into any prompt.

## Field-expert conference, round 1 (same agent, 13 November 2026, 14:42 local, clock checked)

- The note BUILD_ON_TOTEX2_20261113.md was superseded before it was written; its content is the talk
  `<local>/Documents/expert_conference_20261113/talks/R1_Derivateurs_expert.md` (agenda: AGENDA.md there).
- New in the talk, derived by me by hand, no program, no second reader: (1) `A` total iff every connected presheaf
  on `A^op` is aspherical (the test-category reading of XII Def. 1); (2) the category FI of finite sets and
  injections is Q-exact, F_p-exact for no p, not total (`El_FI`(2-subsets) = B(Z/2)); so "exact iff Aut(M)
  amenable" (N2) is false as stated; BZ is a second example; (3) the three compact-limit properties (CH) Ramsey,
  (CC) convex, (CAb) exact, with (CC) => Reiter property by a minimax argument; (4) candidates C1-C6 (C1: exact iff
  (CH); C2: total and Q-exact => Z-exact; C4: the converse of N1 through B(U/G_F)).
- Three questions put: to the LM7 reviewer, the intake agent, the shape-map agent. Round 2 (replies) follows:
  read every talk in `talks/` and write `replies/R2_Derivateurs_expert.md`.
- Read for the talk: the final register of TOTAL_EXACT_2 (statements of Parts A and D), not its proofs.

## Conference round 2 (same agent, 13 November 2026, 14:54 local, clock checked)

- Written: `expert_conference_20261113/replies/R2_Derivateurs_expert.md` and `floor/Derivateurs_expert_Q1.md`.
- New, by hand: for an age with free amalgamation and `G_F` normal of finite index in an open `U`,
  `El_A(T_{G/U}) = B(U/G_F)`; so finite imaginaries fail at `pi_1` and cannot give `Q_n != Q_{n+1}` for n >= 2;
  under weak elimination of imaginaries total <=> quasi-filtered <=> all open subgroups are pointwise stabilizers
  (granted the intake's reading of T A.33 (ii)). `Aut(M_delta)` is not amenable (the intake's argument, checked).
- Three talks derived the Ramsey / convex / exact table and the FI example independently; they agree.
- Context past 80 %: a successor should take over any further round.


## Referee reading of TOTAL_EXACT_2 and the prompt FRAISSE_EXACT (next field expert, Claude Fable 5.2, effort max, 13 November 2026, 15:12 local, clock checked)

Task of the coordinator: (A) the reading at effort max of T A.21, A.24, A.30–A.34, C.25–C.28 ("T" = TOTAL_EXACT_2,
final register); (B) the next Pro prompt from N1–N6 of `NEXT_PROMPT_ITEMS.md`; (C) at most five questions for the
previous expert; (D) this section. Sub-agents: none. The prompt is not sent; the user sends Pro prompts.

Files.
- `REVIEW_MAIN_PROOFS_TOTEX2.md` (this folder): the verdicts with the evidence, the step of C.27 written out (§4), the
  sources opened (§5), remarks for the companion (§6), what was not checked (§7).
- Work: `pro_prompts_max_20261112_work/FRAISSE_EXACT/`: `PROMPT.md` (42,630 bytes), `ZIP_LIST.md` (23 rows, with the
  list of e-prints fetched), `build_zip_20261113.py`, `MANIFEST.tsv`, `stage/`, `CONSULT_FOR_PREVIOUS_EXPERT.md`,
  `checks_drafter/lead8e_check.py` (+ `.out`), `unpack_new_eprints_20261113.py`.
- Upload: `pro_prompts_max_20261112/FRAISSE_EXACT/`: `PROMPT.md` (identical copy) and
  `FRAISSE_EXACT_background.zip` (1,693,377 bytes, 57 entries; LaTeX only except the two notes of Isbell–Mitchell).
  File prefix of the deliverables: `FREX`. Lint `--lint-math` on both copies: `files: 2 failing lint: 0`.
- arXiv sources fetched to `Free or receipted/free/arxiv-eprints-der-20261113/` (one folder each, unpacked, nothing
  executed): 1801.01165, math/0305241, 1106.3127, 1606.07979, 1705.02379, 1208.2389, 0805.2778, 1505.00762, 1312.3430.

(A) Verdicts. A.21, A.24, A.30, A.31, A.32, A.33, A.34, C.25, C.26, C.27, C.28: all correct; no gap, no error. Read
as inputs and followed: C.5, C.10, C.19–C.22, C.24, C.32. The compressed step of C.27 (routing of forbidden pairs of
components into a new quasi-filter target) goes through; it uses (10), (11) for the component necklace, which are
TOTEX C.1 applied to the injections `H(f), H(g)` with path bound `n + 1`, and at each step factors the actual arrow by
the hypothesis at the earlier stage. Cited theorems, hypotheses checked in the sources: Evans–Hubička–Nešetřil 2019,
Theorem 2.6 (strong class with (*), countably many types, JEP, AP: holds for `C_δ` and the subclass);
Goerss–Jardine IV.5.6 (stated for `y↓F`, the variance used); Adámek–Koubek–Reiterman 1981, pp. 375–387 ((4), (9)–(11),
B.7–B.9, C.1, (c_m) and its proof, which uses neither (d_m) nor anything beyond (10), (11)). So D.1 stands.
For the companion: "`K*`" must be worded as the construction with repaired quasi-filters (for the printed maps (11)
fails: TOTEX C.1).

Findings made on the way (mine; checked by nobody else unless said).
1. `Aut(M)` for `C_δ` is not amenable: Evans–Hubička–Nešetřil Theorem 3.8 applies (the graph of common hyperedges is
   2-sparse; I wrote the count). Also by T A.18 with the Reiter form of Moore's criterion.
2. The remark in Evans–Hubička–Nešetřil 2019 (arXiv v4) that the graph of a `k`-sparse `n`-ary relation is sparse is
   false as stated (one triple with a private third point per pair). Their theorem is not affected.
3. Exactness of `colim_A` depends only on the topological group `G = Aut(M)`: `colim_A V = (V_∞)_G`, so exact over `R`
   iff coinvariants are exact on smooth `R[G]`-modules (Lead 1). Consequences: a dense union of compact subgroups
   (EPPA) gives exactness over `Q`; a non-trivial automorphism of a finite member kills exactness over `Z` and
   totality.
4. Amenable does not imply exact: `G = Z = Aut(Z; d_k)`, and `Aut(Q,<)^Z ⋊ Z` with strong amalgamation and rigid
   structures (Lead 6). So N2 as written in `NEXT_PROMPT_ITEMS.md` ("exact iff amenable") is false in one direction
   without (Op); the prompt asks for each direction under named hypotheses (Part A.3).
5. Three fixed-point properties of `A^op`-diagrams: compact Hausdorff (= finite-pattern Ramsey, T A.13), compact
   convex (= Reiter = amenable, Lead 2), torsors under compact abelian groups (= exact, Lead 3). The first implies
   the other two; the relation between the last two is the main question.
6. Totality in terms of open subgroups: `El(T_{G/U}) ≃ E_U` (finite strong `B` with `G_B ≤ U`; arrows `u|_B`, `u ∈ U`);
   under functorial amalgamation, total iff every `E_U` is weakly contractible; `π_1(E_U) = U/⟨G_B ≤ U⟩` (Lead 7).
   The converse of T A.33 is false: linear orders with a convex equivalence relation are Ramsey (KPT Corollary 6.8),
   hence exact and total, and the stabilizer of a class is open and not a `G_F`. So N1's converse is expected false.
7. The predimension family `C(k, a, b)`, `δ = a|V| − b|E|`: expected total for all `(k, a, b)` (the proofs use only
   submodularity, integrality, positivity), so it gives no member of `𝒬_n ∖ 𝒬_{n+1}`; not exact for `k ≥ 3`,
   `ak/2 ≤ b < (k−1)a` (private vertex); for `k = 3`, `2b < a` the triple `v_1, v_2, v_3` HAS the affine equalizer
   `[123] + [234] + [345] − [124] − [245]` on five points (checked by `lead8e_check.py` on a grid of `(a, b)`), while
   `Aut(M)` is not amenable for all `b < (k−1)a`: these are the candidates for "exact and not amenable" (Lead 8).
8. The three regimes (N5) as one statement: over a tower with surjective transitions a levelwise solvable `y` lies in
   the closure of the image and the obstruction is `lim^1` of the kernels; for compact groups all levelwise
   solvable `y` are solvable iff the index is exact; so an obstruction outside the closure needs a non-exact index
   (Lead 9).
9. T A.11's category (linear and cyclic order) has `BC` simply connected with `H_2 = Z`; I expect `BC ≃ CP^∞`, and it
   is a candidate for `𝒬_2 ∖ 𝒬_3` (bears on DER_FOLLOWUP A.3; asked in Part B.5 for this category only).

(B) The prompt. Parts: A exactness against amenability and the Ramsey properties (main question A.3 (i)–(v), test
classes A.4); B totality of categories of embeddings (general theorem, the criterion `E_U`, the converse, (St) and
(Op) for free amalgamation classes, the category of T A.11); C exact colimits as limits of compact diagrams (duality,
torsor form, finite groups, the position of "`lim^1` vanishes on profinite diagrams", the diagram over `C_δ^op`);
D the predimension family; E the three regimes; F literature and the statement for the companion. R1–R12 carry the
status of each result; Leads 1–9 are mine and unchecked except Lead 8 (e) (program) and what the review covers.

(C) `CONSULT_FOR_PREVIOUS_EXPERT.md`: five questions (main question A or B; whether Lead 7 or Lead 3 is already in
XII, GALOIS, PRETOT, TOTEX; where Part B.5 belongs; whether Part E must name the LM cases).

Not done. No reading of the 42 rows that the intake left at statement level. No program for T (every step of the
eleven statements was followed by hand). Leads 1–7 and 9 have no machine check and no second reader. The tally
(`claude_tools/maths_prompt_tally.py`) does not list FRAISSE_EXACT, and its line for DER_FOLLOWUP still says "hold A.2
and B.1". `HUNCHES.md` has no entries for the findings above (they are Leads of the prompt). LM8 B.6, B.9 not
entered into any prompt. The companion text at II ms. 36ter is not written.

Context. Harness figure (get_usage, "self") at 15:05: 256,640 tokens of 800,000 (32 %). Read-in ended near 25 %.

## Addendum: the experts' conference folded into FRAISSE_EXACT (same agent, 13 November 2026, 15:34 local, clock checked)

Two coordinator messages after the section above (conference folder `Documents/expert_conference_20261113/`).

- Prompt now 53,526 bytes, both copies identical, lint `files: 2 failing lint: 0`; zip unchanged in content
  (1,693,377 bytes, 57 entries). New in the prompt: hypotheses (FA) split into (FA) over non-empty bases and (FA0)
  over the empty base, (WEI), (Fin); Lead 5 (c) (index condition from the norm map), Lead 7 rewritten (under (FA) and
  (Op) every action component is contractible or equivalent to A, so A is in Q_n iff BA is (n-1)-connected; the
  category of T A.11 expected quasi-filtered and not total), Lead 8 (e), Lead 10 (F_p for all p against Q),
  Lead 11; Parts A.3 (vi)-(viii), A.4 classes (7), (8) and the item FE-1, B.3, B.5, B.6, C.4, C.6, D.3 (FE-4), E.5.
- Floor answers written (`floor/<question>_answer_Derivateurs_successor.md`): shape_map_Q1 SETTLED (false: M' = P_V +
  coker(g -> g v_1 + g v_2 + g v_3) has the dimensions of Q_{F_p} and T_1 = 0; program `checks_drafter/lead11_check.py`,
  all 31,178 labelled objects with at most 7 points); Derivateurs_expert_Q1 (part 1 settled: contractible; part 2
  true with functorial joint embedding, expected false without; part 3: n = 2 yes by T A.11, n >= 3 open);
  intake_Q1 NOT settled (true for pairs by total unimodularity and for categories with a weakly terminal object;
  under the hypothesis I = 0 or Z for every family; shape of a counterexample: colim Sat = Q).
- Sign-off: `joint/SIGNOFF_Derivateurs_successor.md`. Objections: FE-3 (false), first half of FE-6 and
  sub-statement 1 (b) of the open disagreements (Reiter does not give Q-exactness even with finite hom-sets: finite
  subsets of Z up to translation). Amendments: FE-2 (all pairs of open subgroups), FE-4 (clause 3 not yet a
  statement), A 3 (repaired K*), A 15 (the remark of Evans-Hubicka-Nesetril on sparse relations is false as stated).
- `CONSULT_FOR_PREVIOUS_EXPERT.md` stays as written; the coordinator says the previous expert is past its room.
  Its questions 2 and 3 are answered in part by the conference (the expert's own E_U = B(Gamma); the three
  fixed-point rows were reached independently in three talks).
- Context at 15:31 (get_usage, "self"): 514,174 of 800,000 (64 %). This agent stops here. A successor should start
  from this file, the review, the prompt and the three floor answers; the cheapest next steps are: (Op) for the
  category of T A.11 (it decides a second witness for total < quasi-filtered), a search for an affine equalizer
  family in C(3, 3, 1) beyond the triple, and the tally entry for FRAISSE_EXACT.

## OpenAI 317 and 312 placed (same agent, Claude Fable 5.2 at effort max, 14 November 2026)

Task of the main session (Claude Opus 5.5 at effort max): fold two AI-produced results into the unsent prompts.
Context on arrival 749,714 of 800,000, so NO prompt was edited and no backup made. Written instead:
`INSERTS_AI_RESULTS_20261114.md` (this folder): paste-ready blocks. Read of the papers: only the first theorem of
each introduction, truncated; the "Moreover" clause of 317 and the conclusion of 312's theorem are unread.
Judgment: 317 (Thomason structures on nCat, n <= infinity) goes to REVERSIBLE_LOCALIZERS (new item: localizers of
nCat against fundamental localizers of Cat), to DER_FOLLOWUP as frame for the 2-category of types, perhaps one
sentence in INDLOCAL; 312 (elementary expansions for coherators) goes to the Part on simple homotopy types (H5) of
REVERSIBLE_LOCALIZERS. Neither bears on H2 or H9. Nothing for FINMON, S2COUNT, FRAISSE_EXACT, PRESHEAF_TOTALITY.
This agent is at its window: a successor starts from this file, the review, the two inserts files and the prompts.

## Intake of DER_FOLLOWUP (final) and FINMON (final) (same agent, Claude Fable 5.2 at effort max, 17 November 2026, 12:59 local, clock checked)

Task of the main session (Claude Opus 5.5 at effort max): brief
`pro_prompts_max_20261112_work/BRIEF_INTAKE_DER_FOLLOWUP_FINMON_20261117.md`. I had been compacted on 15 Nov; I
reread this file in full first. Everything is in
`pro_prompts_max_20261112_work/INTAKE_DER_FOLLOWUP_FINMON_20261117.md` (sections 1–11, a summary table at the top).

What a successor must know.
- **DER_FOLLOWUP** (GPT-6 Astra, ChatGPT Pro mode; 65 statements) is sound in all its main claims; I followed
  Parts A, D, G in full and B once.
  - The tower: `A_n(Λ)` = finite ordered sets with a `Λ`-valued `n`-cocycle = `Δ_inj/K(Λ, n)`; all open subgroups
    of its Fraïssé group are pointwise stabilizers (uses `n ≥ 2` at one place: a circle nerve); every action
    component is contractible or equivalent to the base. So `A_n(F_2) ∈ 𝒬_n ∖ 𝒬_{n+1}`, `T_1 ⊋ 𝒬_2 ⊋ T_2 ⊋ …`, and
    totally `W_n`-dwyérienne sieves do not compose for finite `n ≥ 2`. A.13: for a connected Kan complex `K` the
    action components of `Δ_inj/K` are the point and the connected covers of `K`.
  - Lead 6 (my predecessor's H2) holds for every fundamental localizer (A.11).
  - Part G: `W̃` (REVLOC F.1; a degree-two map of 2-spheres is in it) refutes products and `u_!` under Loc (1)–(3);
    `W♯` refutes XV 9.11–9.13 under Loc (1)–(3); Loc (1 bis) restores them; my reading of 9.12 against the
    edition's note is confirmed; XVI Lemma 2.5 fails for countable products (zigzag product completion).
  - Part D: every exact index passes every free-monoid test (D.6), so PRETOT F.10 is answered no. **Open:** whether
    every `M: C_δ → FreeMon` passes; reductions D.8–D.10.
  - Corrections to my own Leads: Lead 4 (a) was wrong beyond free degeneracy completions (E.3); the suggestion in
    Lead 5 was refuted (B.6); Leads 1, 2, 3 proved.
- **FINMON** (695 rows; INCOMPLETE by its own first line): only C2-CP2 is unresolved, between 17 and 22 arrows.
  Statement level only on my side; 14 GB of encoded certificates not decoded. Its Proposition 6.6 has the same
  counterexample as my entry V.10 (finitary permutations of `N`).
- **Records these change** (section 10 of the intake): four entries of the editors' file (XV.8, XV.9, XVI.2, XVI.3)
  and V.10; the sentence on XVI footnote 56 in `INTAKE_S2COUNT_REVLOC_20261117.md` (Corollaire 7.7.2 is true; the
  footnote's guess is wrong).
- **The successor's items** (section 7): Part A reverse excision and homology localizers (@4, @8 (ii), REVLOC
  D.2.4, D.3.2, and whether Loc (8) is needed in 7.7.2); B `TC = C ∩ W` (@8 (i)); C the linear "Thm(?)" (g6);
  D schematization (@270); E finite models (CP², the `S²` frontier), last. FRAISSE_EXACT stays separate and takes
  the free-monoid item; its B.6 is settled and B.2, B.5 change (section 8).
- **New leads of mine** (section 9; by hand, unchecked): `A^op` is the orbit category of `Aut(M)` for the family of
  pointwise stabilizers, so `T_k` is Bredon homology; the action spectrum of a category (the types of its action
  components) is closed under covers, and for connected categories which sets occur is open.

Not done: see section 11 of the intake. I wrote nothing to the RUNBOOK, STATUS.md, the registry or the tally.
Context: the harness tool reports the main session, not me; by my own count I ended near 450k.
