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
