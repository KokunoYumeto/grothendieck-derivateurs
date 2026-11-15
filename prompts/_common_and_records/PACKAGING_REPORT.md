# Packaging report: six Dérivateurs prompts for GPT-6 Astra (ChatGPT Pro mode)

Claude Opus 5.5 (Anthropic), effort max, 12 Nov 2026, finished 17:17 WEST. Nothing was sent or published. The
expert's folders (`pro_reviews_max_20261112\DERIVATEURS_EXPERT\PRO_PROMPTS\`, `pro_reviews_max_20261112\1_CATHOT\PRO_PROMPTS\`
and `1_CATHOT\PRO_PROMPT_EMAIL_CLAIMS*`) were only read; no file there is newer than the start of this work.

## Verdicts

| Prompt | Upload folder `pro_prompts_max_20261112\<NAME>\` | Verdict |
|---|---|---|
| TOTAL_EXACT | `PROMPT.md` 13,894 B; `TOTAL_EXACT_background.zip` 8,198,994 B (21 files) | ready |
| PRESHEAF_TOTALITY | `PROMPT.md` 13,273 B; `PRESHEAF_TOTALITY_background.zip` 6,095,540 B (37 files) | ready |
| REVERSIBLE_LOCALIZERS | `PROMPT.md` 15,512 B; `REVERSIBLE_LOCALIZERS_background.zip` 31,805,467 B (37 files) | ready; first decide its overlap with the planned H6 prompt |
| FINMON | `PROMPT.md` 20,393 B; `FINMON_background.zip` 33,679,765 B (51 files) | ready |
| INDLOCAL | `PROMPT.md` 15,767 B; `INDLOCAL_background_1.zip` 21,846,832 B (32 files); `INDLOCAL_background_2.zip` 21,782,932 B (1 file) | ready; first decide its overlap with the planned H5/H6 prompts |
| S2COUNT | `PROMPT.md` 11,154 B; `S2COUNT_background.zip` 27,942,437 B (36 files) | ready |

File counts leave out `MANIFEST.tsv`. Each upload folder is flat and holds 2 or 3 files. `1_CATHOT\PRO_PROMPT_EMAIL_CLAIMS.md`
is byte-identical to FINMON's `PROMPT.md` (checked with `cmp`) and was packaged once, as FINMON. The two overlaps come from
the expert's `CHANGES_20261112.md`: the coordinator's planned prompt for hunch H6 overlaps Parts E.1–E.2 of
REVERSIBLE_LOCALIZERS ("keep one of the two"), and planned prompts for H5 and H6, if they are the CATHOT expert's, overlap
Parts E and C4 of INDLOCAL. They are scheduling decisions, not packaging defects.

## Common to all six

**Layout.** Every zip is flat. `MANIFEST.tsv` sits at the root with the columns `path_in_zip`, `source_path`, `bytes`,
`sha256` and `why_included`. INDLOCAL's two zips each carry the full manifest, with an extra column `in_zip`. Source paths
start with `%USERPROFILE%` in place of the home folder, so the first name does not appear. Rows the expert listed keep the
expert's reason, with two exceptions: three page ranges are corrected (see TOTAL_EXACT and PRESHEAF_TOTALITY), and
redacted copies say so. Rows I added start with "added:".

**Checks.** `verify_packages.py` (in the work folder) reopens every zip and runs the CRC test. It checks every member's
size and sha256 against the manifest and against its source file. Each redacted copy (see Privacy) must equal its source
with only the e-mail addresses replaced. All checks passed. All zips are under 40 MB. INDLOCAL in one zip would be about
43.6 MB, so Hausmann–Husemoller 1979 (a 24.8 MB scan) has a zip of its own.

**Effort-max material only.** None of the six lists cites, and no zip holds, a file of `pro_reviews_20261110\`. All reviews
come from `pro_reviews_max_20261112\`. The returns are the GPT-6 Astra returns in `pro_returns_20261110\`. `_COMMON_BLOCK.md`,
`TOTASPH_PROMPT.md` and `POLES_PROMPT.md` are the earlier prompts in `pro_prompts_20261110\`, as the expert listed them.

**Grothendieck's text.** It comes from `corrected_french_20261111\DER_<id>.tex`, one file per part, which are the names
the prompts use. `derivateurs_publish_20261111\repo\transcription\` holds the same corrected French split into five-page
files, plus a second pass on macro typography (accents, underlines; `TRANSCRIPTION_UPDATE_20261111.md`). That pass changes
no mathematics. I read the page ranges in the manifests and in the new prompt paragraphs from the files' `\msp{page N}` marks.

**PROMPT.md.** Only the statements of attached material were changed:
1. In all six headers, "The files to attach are listed in `ZIP_LIST.tsv`." now names `MANIFEST.tsv` in the zip. `ZIP_LIST.tsv`
   does not travel with the prompt.
2. The three Dérivateurs-expert prompts had no other statement of attached material. Each gets one paragraph,
   "Attached in that zip …", right after the header.
3. In the three CATHOT prompts, the "What is attached" paragraph is corrected.

The mathematics, the R-lists, the Parts and the rules are untouched. The expert's text is kept as `PROMPT_from_expert.md`
in each work folder. Two provenance references stay in the headers and are not attached, because no Part uses them:
`PROMPT_before_results_20261112.md` (all six) and `PUSH_STANDARD_AND_AUDIT_20261111.md` (FINMON, our audit standard).

**The two items the expert could not list.**
- *TeX source of arXiv:2610.38760v1.* It is on disk:
  `pro_reviews_max_20261112\1_CATHOT\work\lit\benbassat\src\Fiedorowicz2.tex` (80,867 B). It is the arXiv e-print of v1:
  its `00README.json` names it as the top-level file, it is dated 28 Oct 2026, and v1 is the only version. It is included
  next to the PDF in FINMON (Part B; `EMAIL_CLAIMS_CHECK.md` cites its line numbers) and in S2COUNT (Part A3, the monoids
  M(Y, f)), as `BenBassat_2610.38760v1.tex`.
- *Source of the Open Maths lesson "Derived colimits over a small category".* The only copy under `Documents` is inside
  `pro_batch_20261022_open_questions\Q13-derived-colimits-injective-ordinals\SOURCES.zip`
  (`lessons/cotangent-complexes-and-deformations-in-ringed-topoi/derived-colimits-over-a-small-category.md`, 18,270 B,
  sha256 156dad72…, packed 22 Oct 2026). It is older than the page TOTASPH read. Its § 4 holds only Exercises 4.1–4.2, and it
  has no interpolation or gap-polynomial construction. TOTASPH cites "sections 4.1–4.8" and that construction. **Not attached.**
  The new paragraph of TOTAL_EXACT gives the lesson's address and points to TOTASPH C.9–C.10, which write the construction
  out in full (`TOTASPH_C.tex`: "interpolation on coordinate hyperplanes", the gap bijection). So R3 can be checked without
  the lesson.
  - Where I looked: `derivateurs_companion_20261109`, `pro_batch_20261022_open_questions` (with `answers`),
    `pro_batch_20261023_lesson_questions`, `pro_batch_20261024_math_map`, `pro_batch_20261025_followups`,
    `pro_batch_20261108_lessons`, `math` (timed out), `Codex\2026-10-19`, `Codex\2026-10-20`,
    `Codex\course-current-edition-20261003` (by file name), the `openmaths_*` folders, `claude-notes`, `results`, `outputs`,
    `reports_20261112`, `state_of_work_20261108`, `raw_publish_20261111`, `pro_index_20261005`, `math-agent-logbooks`,
    `Free or receipted\free\lesson-sources`, and the day's logbooks. Outside `Documents` I tested one known path, the
    open-courses staging tree on F:. It stops at 30 Sep and has no such course.
  - The current source is presumably on the openmaths.org server or in Codex's site tree. The 22 Oct copy is kept in
    `work\TOTAL_EXACT\extracted_lesson\` for the record.

**Privacy and safety.** The scan covered every text file in the zips (`.md .tex .csv .tsv .py .out .json .bbl`), each
`MANIFEST.tsv` and each `PROMPT.md`. It looked for e-mail addresses, API-key patterns, the words password, passphrase,
api key, access/auth token, bearer and token, Obsidian or "Untitled 19xx" notes, the first name, and local user paths
(`work\<NAME>\PRIVACY_SCAN.tsv`).
- *Hits in the source files.* Only printed e-mail addresses:
  - G. Maltsiniotis's contact address in the edition's notes: `DER_II-a.tex` 1, `DER_VII-a.tex` 1, `DER_XIII-a.tex` 1,
    `DER_III-V.tex` 4, `DER_VIII-X.tex` 3, `DER_XVI.tex` 1.
  - Authors' `\email` lines: `HORR_2205.02353.tex` 4, `Groth2013_derivators_1112.3840.tex` 1,
    `HoveyPalmieri1999_Bousfield_lattice_math9801103.tex` 2, `Fiedorowicz2002_math0202260.tex` 1,
    `BarmakMinian_math0611156.tex` 2, `BenBassat_2610.38760v1.tex` 2 (one address, twice).
- *Action.* In the zipped copies each address is replaced by `[e-mail address removed]`. Nothing else changes, and line
  numbers are kept. The copies are in `work\<NAME>\redacted\`. Their manifest rows say so and give the source's sha256.
- *After redaction.* There are no hits in any zipped text file, manifest or prompt: no address, key, password, token,
  Obsidian note, first name or local user path.
- *PDFs.* PDFs were not altered. Their text was extracted with `pdftotext` and scanned (`work\PDF_SCAN.tsv`). No first name,
  local path, key or Obsidian note was found. Our own PDFs carry no address: the CATHOT, TOTASPH, POLES and GALOIS papers
  and the OpenAI manuscript.
- *Addresses left in published PDFs.* The published papers print their authors' addresses: Ben-Bassat, Carcacía-Campos,
  Cianci–Ottina, Martinian–Steinberg, Chachólski–Scherer, Cisinski (1999, 2004, Astérisque 308),
  May–Stephan–Zakharevich, Palmer–Wu, Raptis, Shoikhet, Berrick–Casacuberta, Rezk and Cegarra. Adámek–Rosický–Vitale
  prints the TAC editorial board's addresses, and the Miller 1984/1985 JSTOR cover pages carry JSTOR's support address.
  These are left as published. If no address may appear even there, those papers have to come out.
- *Image-only scans.* Adámek–Koubek–Reiterman 1981 has almost no text layer, so it could not be text-scanned.

**Work folder** `pro_prompts_max_20261112_work\`:
- One folder per prompt with `MANIFEST.tsv` (identical to the zipped one), `PROMPT_from_expert.md`, `PRIVACY_SCAN.tsv`,
  `build_log.json` and `redacted\`.
- At the root: `build_packages.py` (all decisions are in it, so a rebuild reproduces the folders), `verify_packages.py`,
  `scan_pdfs.py`, `PDF_SCAN.tsv` and this report.
- `CATHOT_01_FINMON\`, `CATHOT_02_INDLOCAL\` and `unwrap_check.py` were there before (15:17, another session) and are untouched.

## TOTAL_EXACT

**Folder.** `PROMPT.md` 13,894 B; `TOTAL_EXACT_background.zip` 8,198,994 B (9,083,300 B unpacked, 21 files + manifest).

**Zip.**
- *Notes (5):* `_COMMON_BLOCK.md`, `2_TOTAL_ASPHERICITY_REVIEW.md`, `RESULT_FILTERED_BY_ONE_TYPES.md`, `HUNCHES.md`, `FINDINGS.md`.
- *Return TOTASPH (9):* `TOTASPH_PROMPT.md`, `_paper.pdf`, `_results.csv`, `_report.md`, `_C.tex`, `_D.tex`,
  `_D_followup.tex`, `_D_general.tex`, `_CD_report.md`.
- *Grothendieck's text (2):* `DER_II-a.tex` (II ms. 1–53; 1 address removed), `DER_XIIb-a.tex` (XII ms. 59–122).
- *Literature (5):* `IsbellMitchell1973.pdf`, `AdamekKoubekReiterman1981.pdf`, `AdamekRosickyVitale2010_sifted.pdf`,
  `Lurie_HTT.pdf`, `Cegarra2020_hocolim.pdf`.

**Against ZIP_LIST.tsv (18 rows).**
- *Kept:* all 18.
- *Added 3:* the sources that Part D.1 names and that are on disk.
  - Adámek–Rosický–Vitale, *What are sifted colimits?* (TAC 23, 2010).
  - Lurie, *Higher Topos Theory* (HTT 5.3 is named; TOTASPH C/D also cite it).
  - Cegarra, *Cohomology of homotopy colimits of simplicial sets and small categories* (Mathematics 8, 2020): the "work
    on homotopy colimits in Cat".
- *Not on disk:* Gabriel–Ulmer, Isbell–Mitchell 1976, Oberst 1968, Adámek–Reiterman 1976, Husainov 2002. A search of the
  literature corpus and the free shelf found none of them. The prompt asks Pro to open them itself.
- *Not attached:* the old lesson copy (see above).
- *Corrected:* the manifest reason for `DER_XIIb-a.tex` gives the true range, XII ms. 59–122. The expert wrote 87–103; the
  ms. 112 of R9 is in this file.
- *Found and not added:* `pro_batch_20261022_open_questions\answers\Q13-solution.md` (GPT-6 Astra, 23 Oct 2026). It is a
  separate proof that colimits over Δ_inj are exact (a signed-equalizer lemma via Ramsey theory), so a third proof of R3.
  The prompt does not use it; add it only if a third proof is wanted.
- *Left alone in the prompt:* R3 says that the lesson's address is in `TOTASPH_CD_report.md`. That file names the lesson but
  gives no address; the address is in `TOTASPH_references.bib`. R3 is outside the attached-material statement, so it was not
  edited; the new paragraph supplies the address.

**PROMPT.md.** Line 6 was "TOTASPH (return 2). The files to attach are listed in `ZIP_LIST.tsv`." It is now "TOTASPH
(return 2). The attached files are listed in `MANIFEST.tsv` at the root of `TOTAL_EXACT_background.zip`." It is followed
by this new paragraph:

> Attached in that zip, besides the files named below: the return TOTASPH (paper, results table, report, the TeX of Parts
> C and D, the prompt it answered); Isbell–Mitchell 1973 and Adámek–Koubek–Reiterman 1981; three of the sources named in
> D.1 (Adámek–Rosický–Vitale 2010 on sifted colimits, `AdamekRosickyVitale2010_sifted.pdf`; Lurie, *Higher Topos Theory*,
> `Lurie_HTT.pdf`; Cegarra 2020 on homotopy colimits of small categories, `Cegarra2020_hocolim.pdf`); Grothendieck's text
> in `DER_II-a.tex` (II ms. 1–53) and `DER_XIIb-a.tex` (XII ms. 59–122): the French transcription corrected on 11 Nov
> 2026, AI-made from the edition of Künzer, Malgoire and Maltsiniotis, manuscript pages marked `\msp{page N}`; where a
> formula looks wrong, say so and reason from the mathematics. Of `_COMMON_BLOCK.md` only the conventions, the rules of
> proof and the form of the deliverables apply; its paragraph "WHAT IS ATTACHED" describes the zip of an earlier prompt.
> The Open Maths lesson of R3 is not attached; it is online at
> https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/derived-colimits-over-a-small-category.html,
> and the construction R3 uses is written out in TOTASPH C.9, C.10 (`TOTASPH_C.tex`).

The sentence on `_COMMON_BLOCK.md` is needed because its "WHAT IS ATTACHED" paragraph names `DER_<id>_text.tex`, companion
files and `FABLE_PILOT_OVERVIEW_20261110.md`, none of which is in these zips. The same sentence is in the other two
Dérivateurs-expert prompts.

**Verdict:** ready to send.

## PRESHEAF_TOTALITY

**Folder.** `PROMPT.md` 13,273 B; `PRESHEAF_TOTALITY_background.zip` 6,095,540 B (7,475,774 B unpacked, 37 files).

**Zip.**
- *Notes (7):* `_COMMON_BLOCK.md`, `2_TOTAL_ASPHERICITY_REVIEW.md`, `3_POLES_REVIEW.md`, `RESULT_FILTERED_BY_ONE_TYPES.md`,
  `HUNCHES.md`, `FINDINGS.md`, `CATHOT_OWN_RESULTS.md`.
- *Returns (11):* `TOTASPH_PROMPT.md`, `TOTASPH_paper.pdf`, `_results.csv`, `_A.tex`, `_C.tex`, `_E.tex`, `_F.tex`,
  `_F_followup.tex`, `_G.tex`; `POLES_paper.pdf`, `POLES_results.csv`.
- *Grothendieck's text (8):* `DER_II-a.tex`, `DER_VII-a.tex`, `DER_VII-b.tex`, `DER_XIIb-a.tex`, `DER_XIIb-b.tex`,
  `DER_XIIapp.tex`, `DER_XIII-a.tex`, `DER_XIII-b.tex`. One address was removed from each of II-a, VII-a and XIII-a.
- *Programs (7):* `catlib.py`, `enum_monoids.py`, `enum_cats.py`, `enum_monoids_upto6.out`, `enum_cats_upto7.out`,
  `enum_monoids_upto6.json`, `enum_cats_upto7.json`.
- *Literature (4):* `HORR_2205.02353.tex` (4 addresses removed), `Cisinski1999_Dwyer.pdf`, `Cisinski_Asterisque308.pdf`,
  `Thomason1980.pdf`.

**Against ZIP_LIST.tsv (32 rows).**
- *Kept:* all 32.
- *Added 5:*
  - `DER_XIII-a.tex` and `DER_XIII-b.tex` (XIII ms. 1–98). Part D asks Pro to "locate that use in XII §3 and XIII", and
    chapter XIII was not in the list.
  - `Thomason1980.pdf`: the origin of Dwyer maps, cited in TOTASPH F (R2–R5) and the subject of Parts B–D.
  - The two census JSON files, which are the data outputs, with example composition tables, of the programs Part A.3
    offers. `enum_cats_upto7.json` contains the ≤ 6 run, so `enum_cats_upto6.json` was left out as a subset.
    `enum_cats_upto6.keep.json` is a byte duplicate and was left out.
- *Corrected:* manifest reasons for two files whose ranges the expert placed wrongly. `DER_XIIb-a.tex` covers XII
  ms. 59–122 and contains the Dwyer-type immersions of ms. 107–114. `DER_XIIb-b.tex` covers ms. 115–169 (XII § 3,
  continued), not "104–169 (ms. 107–114 …)".

**PROMPT.md.** Line 6 was "TOTASPH (return 2), Parts E–G. The files to attach are listed in `ZIP_LIST.tsv`." It is now
"TOTASPH (return 2), Parts E–G. The attached files are listed in `MANIFEST.tsv` at the root of
`PRESHEAF_TOTALITY_background.zip`." It is followed by this new paragraph:

> Attached in that zip, besides the files named below: the returns TOTASPH (paper, results table, the TeX of the sections
> cited, the prompt it answered) and POLES (paper, results table); `HUNCHES.md` (H3, behind Part A); Grothendieck's text
> in the `DER_*.tex` files (II ms. 1–53; VII ms. 1–117; XII ms. 59–169, where XII §3 begins at the end of `DER_XIIb-a.tex`
> and continues in `DER_XIIb-b.tex`; the appendix to XII; XIII ms. 1–98, for Part D): the French transcription corrected
> on 11 Nov 2026, AI-made from the edition of Künzer, Malgoire and Maltsiniotis, manuscript pages marked `\msp{page N}`;
> where a formula looks wrong, say so and reason from the mathematics. The zip also holds Thomason 1980 (Dwyer maps),
> Cisinski 1999, Cisinski's Astérisque 308, Hackney–Ozornova–Riehl–Rovelli (TeX) and the outputs of the census programs.
> Of `_COMMON_BLOCK.md` only the conventions, the rules of proof and the form of the deliverables apply; its paragraph
> "WHAT IS ATTACHED" describes the zip of an earlier prompt.

**Verdict:** ready to send.

## REVERSIBLE_LOCALIZERS

**Folder.** `PROMPT.md` 15,512 B; `REVERSIBLE_LOCALIZERS_background.zip` 31,805,467 B (36,443,866 B unpacked, 37 files).

**Zip.**
- *Notes (8):* `_COMMON_BLOCK.md`, `3_POLES_REVIEW.md`, `4_GALOIS_REVIEW.md`, `RESULT_REVERSIBLE_NOT_STABLE.md`,
  `HUNCHES.md`, `FINDINGS.md`, `CATHOT_OWN_RESULTS.md`, `CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`.
- *Returns (16):*
  - POLES: `POLES_PROMPT.md`, `POLES_paper.pdf`, `_results.csv`, `_report.md`, `_conventions.tex`, `_B.tex`, `_C.tex`,
    `_D.tex`, `_E.tex`, `_F.tex`, `_H.tex`.
  - GALOIS: `GALOIS_paper.pdf`, `_results.csv`, `_conventions.tex`, `_B_loc67.tex`, `_B_KT.tex`.
- *Grothendieck's text (4):* `DER_I-b.tex` (I ms. 60–126), `DER_XIIb-a.tex`, `DER_XIIc-b.tex` (XII ms. 228–275),
  `DER_XVI.tex` (1 address removed).
- *Literature (9):*
  - `Cisinski_Asterisque308.pdf`, `Cisinski2004_minimal.pdf`, `HausmannHusemoller1979.pdf`, `BerrickCasacuberta1999.pdf`,
    `Miller1984.pdf`.
  - `Groth2013_derivators_1112.3840.tex` (1 address removed) and its `.bbl`.
  - `HoveyPalmieri1999_Bousfield_lattice_math9801103.tex` (2 addresses removed).
  - `Rezk_sharp_maps.pdf`.

**Against ZIP_LIST.tsv (33 rows).**
- *Kept:* all 33. Hausmann–Husemoller is not named in the prompt, but GALOIS B_KT.tex (attached, B.14) and the GALOIS
  review cite it. Berrick–Casacuberta is cited in POLES F (R2) and in the POLES review.
- *Added 4:* each is cited by an attached proof and needed by a Part.
  - Groth, *Derivators, pointed derivators, and stable derivators* (arXiv:1112.3840v2), TeX with bibliography. It is cited
    in POLES A–H, GALOIS B.6–B.7, the POLES review and `RESULT_REVERSIBLE_NOT_STABLE.md`, and it defines the strong stable
    derivators of Part G.
  - Hovey–Palmieri, *The structure of the Bousfield lattice* (arXiv:math/9801103), TeX. It is cited in POLES F (R2) and
    is "what is known" for Part D.3.
  - Rezk's paper on sharp maps. It is cited in GALOIS B_loc67 (R9), and sharp maps are the `Fib_W` of Part E.
- *Not added:*
  - Hatcher: cited four times in the POLES sections for textbook facts. It would take the zip past 40 MB.
  - Brown 1973 and Rijke–Shulman–Spitters: peripheral citations.
  - James, Kahn–Priddy, Snaith, Toda, Bousfield 1994/1997, Bousfield's K(n) paper, Dror Farjoun, Berger–Ratković and
    Casacuberta–Scevenels–Smith: not on disk (corpus and free shelf searched). The prompt asks Pro to open the sources.

**PROMPT.md.** Line 6 was "POLES (return 3). The files to attach are listed in `ZIP_LIST.tsv`." It is now "POLES
(return 3). The attached files are listed in `MANIFEST.tsv` at the root of `REVERSIBLE_LOCALIZERS_background.zip`." It is
followed by this new paragraph:

> Attached in that zip, besides the files named below: the returns POLES and GALOIS (papers, results tables, the POLES
> report, the TeX of the sections cited) and the prompt POLES answered; Grothendieck's text in `DER_I-b.tex` (I ms.
> 60–126), `DER_XIIb-a.tex` (XII ms. 59–122), `DER_XIIc-b.tex` (XII ms. 228–275) and `DER_XVI.tex` (XVI in full): the
> French transcription corrected on 11 Nov 2026, AI-made from the edition of Künzer, Malgoire and Maltsiniotis,
> manuscript pages marked `\msp{page N}`; where a formula looks wrong, say so and reason from the mathematics. Of the
> literature the attached proofs cite, the zip also holds Cisinski, Astérisque 308 and *Le localisateur fondamental
> minimal* (2004); Groth 2013 on derivators (Part G); Hovey–Palmieri 1999 on the Bousfield lattice (R2, Part D.3); Rezk
> on sharp maps (R9, Part E); Hausmann–Husemoller 1979; Berrick–Casacuberta 1999; Miller 1984. Of `_COMMON_BLOCK.md`
> only the conventions (with the change stated at the end of this prompt), the rules of proof and the form of the
> deliverables apply; its paragraph "WHAT IS ATTACHED" describes the zip of an earlier prompt.

**Verdict:** ready to send. Before sending, decide between Parts E.1–E.2 here and the coordinator's planned H6 prompt.

## FINMON

**Folder.** `PROMPT.md` 20,393 B; `FINMON_background.zip` 33,679,765 B (37,261,127 B unpacked, 51 files).

**Zip.**
- *Notes (8):* `OWN_RESULTS.md`, `HUNCHES.md`, `CATHOT_REVIEW.md`, `CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`,
  `G6_VERDICT.md`, `EMAIL_CLAIMS_CHECK.md`, `CATHOT_FINDINGS.md`, `DERIVATEURS_FINDINGS.md`.
- *Return CATHOT (3):* `CATHOT_paper.pdf`, `CATHOT_results.csv`, `CATHOT_G.tex`.
- *Grothendieck's text (4):* `DER_III-V.tex` (4 addresses removed), `DER_VII-c.tex`, `DER_VIII-X.tex` (3 removed),
  `DER_XIIapp.tex`.
- *Programs (23):*
  - Census: `catlib.py`, `enum_monoids.py` + `_upto6.out`/`.json`, `enum_cats.py` + `_upto6.out`, `_upto7.out`, `_upto7.json`.
  - Mod-p homology: `higher_homology.py` + `_order5.out`, `_order6.out`, with `dump_classes.py`,
    `monoid_classes_order5.npy`, `monoid_classes_order6.npy`.
  - Checks: `models_check.py`/`.out`, `models_check_tables.py`, `resolution_check.py`/`.out`, `theoremA_test.py`/`.out`,
    `cup_products.py`/`.out`.
- *Literature (13):*
  - `BenBassat_2610.38760v1.pdf` and `.tex` (2 removed); `Miller1984.pdf`, `Miller1985_correction.pdf`, `Atiyah1961.pdf`.
  - `Sweeney_2502.05276v2.pdf`, `Fiedorowicz2002_math0202260.tex` (1 removed), `MartinianSteinberg_2511.12657v1.pdf`,
    `CarcaciaCampos_2611.09718v1.pdf`, `CianciOttina_1512.06088v1.pdf`, `BarmakMinian_math0611156.tex` (2 removed).
  - `Hatcher_AT.pdf`, `Quillen_KtheoryI.pdf`.

**Against ZIP_LIST.tsv (45 rows).**
- *Kept:* 44.
- *Left out:* `CATHOT_report.md`. No R-item and no Part cites it, and the prompt's own list names only the paper, Part G
  and the results table.
- *Kept although the prompt did not name it:* `CATHOT_FINDINGS.md`. Its G1–G5 are the CATHOT expert's notes on exactly the
  pages of Part F (V ms. 51–52, VII ms. 121 and 128, IX ms. 23, XII app. ms. 8–11), so the attached-material paragraph now
  names it.
- *Added 7:*
  - The TeX source of arXiv:2610.38760v1.
  - `models_check_tables.py`, imported by `resolution_check.py`, which does not run without it.
  - `dump_classes.py` and the two `.npy` inputs that `higher_homology.py` reads.
  - The census JSON outputs behind R7 (Part C1), with example tables. The upto6 JSON of categories is a subset of the
    upto7 one, and the `.keep.json` is a byte duplicate.
- *Not on disk:* Putcha 1998, Jardine, Geoghegan, Thomason 1979, Fiedorowicz 1984, McDuff 1979. The prompt already marks
  them as "Not attached". Steinberg's *Representation Theory of Finite Monoids* is in the corpus, but no Part names it.
- *Dangling pointer, harmless:* `EMAIL_CLAIMS_CHECK.md` refers to the CATHOT expert's `READING_BASE.md` for exact reading
  locations. That file is not attached, because the prompt does not use it.

**PROMPT.md.**
- *Line 8.* It was "… construction or a computation. The files to attach are listed in `ZIP_LIST.tsv`." It now ends "…
  The attached files are listed in `MANIFEST.tsv` at the root of `FINMON_background.zip`."
- *"What is attached", start.* "The files of `ZIP_LIST.tsv`, under the names of its second column (`MANIFEST` in the zip
  lists every file with its origin):" became "The files of `FINMON_background.zip`, listed with their origins in
  `MANIFEST.tsv` at its root:".
- *After `DERIVATEURS_FINDINGS.md`)*, this was added: "and `CATHOT_FINDINGS.md` (the CATHOT expert's running list of
  findings; G1–G5 concern the pages of Part F)".
- *Programs.* "the census programs and their outputs" became "the programs and their outputs (census, mod-p homology,
  small models, projective resolutions, tests of Theorem A, cup products)".
- *Preprint.* "arXiv:2610.38760v1" became "arXiv:2610.38760v1 (PDF and TeX source)".
- The rest of the paragraph is unchanged and rewrapped.

**Verdict:** ready to send.

## INDLOCAL

**Folder.** `PROMPT.md` 15,767 B; `INDLOCAL_background_1.zip` 21,846,832 B (32 files); `INDLOCAL_background_2.zip`
21,782,932 B (`HausmannHusemoller1979.pdf` only). Together 49,633,166 B unpacked; a single zip would be about 43.6 MB.

**Zips.**
- *Notes (6):* `OWN_RESULTS.md`, `HUNCHES.md`, `CATHOT_REVIEW.md`, `CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`,
  `GALOIS_REVIEW.md`, `RESULT_FILTERED_BY_ONE_TYPES.md`.
- *Returns (13):*
  - CATHOT: `CATHOT_paper.pdf`, `_results.csv`, `_report.md`, `_BC.tex`, `_D.tex`, `_E.tex`, `_E_ind.tex`, `_E_path.tex`.
  - GALOIS: `GALOIS_paper.pdf`, `_results.csv`, `_conventions.tex`, `_B.tex`, `_B_KT.tex`.
- *Grothendieck's text (4):* `DER_III-V.tex` (4 removed), `DER_VII-b.tex`, `DER_VII-c.tex`, `DER_VIII-X.tex` (3 removed).
- *Literature (10):* `Thomason1980.pdf`, `Cisinski1999_Dwyer.pdf`, `Raptis2010.pdf`, `MayStephanZakharevich2017.pdf`,
  `Quillen_KtheoryI.pdf`, `HausmannHusemoller1979.pdf` (zip 2), `PalmerWu_2510.16879v1.pdf`,
  `Shoikhet_1412.0317v4.pdf`, `ChacholskiScherer_math0110316v1.pdf`, `OpenAI_317_Thomason_nCat.pdf`.

**Against ZIP_LIST.tsv (32 rows).**
- *Kept:* all 32. `CATHOT_BC.tex` (B.7, C.1–C.6, used by R1) and `GALOIS_conventions.tex` were in the list but not in the
  prompt's paragraph, so the paragraph now names them.
- *Added 1:* Cisinski 1999 on Dwyer and pseudo-Dwyer morphisms. R4 (H4) turns on "not a pseudo-Dwyer morphism", and Part D
  is about Thomason cofibrations.
- *Not found on disk:* Kan–Thurston 1976, Baumslag–Dyer–Heller 1980, Maunder 1981, Dwyer–Kan 1980 and Leary 2013 (corpus
  queries; Hausmann 1986 was not queried). The prompt already marks them as not attached, or as searches for Pro.

**PROMPT.md.**
- *Line 7.* "The files to attach are listed in `ZIP_LIST.tsv`." became "The attached files are listed in `MANIFEST.tsv` at
  the root of each of the two zips."
- *"What is attached", start.* It now reads "The files of `INDLOCAL_background_1.zip` and `INDLOCAL_background_2.zip` (the
  second holds only Hausmann–Husemoller 1979), listed with their origins in `MANIFEST.tsv` at the root of each:".
- *CATHOT parts.* "report and Parts D, E" became "report and Parts B, C, D, E".
- *GALOIS.* "results table and the sections with B.9–B.12" became "results table, conventions and the sections with
  B.9–B.12".
- *Literature.* "Thomason 1980; Raptis 2010;" became "Thomason 1980; Cisinski 1999 (Dwyer and pseudo-Dwyer morphisms,
  Part D); Raptis 2010;".
- The rest is unchanged and rewrapped.

**Verdict:** ready to send; attach both zips. Before sending, decide between Parts E and C4 here and the coordinator's
planned H5/H6 prompts.

## S2COUNT

**Folder.** `PROMPT.md` 11,154 B; `S2COUNT_background.zip` 27,942,437 B (31,085,083 B unpacked, 36 files).

**Zip.**
- *Notes (4):* `OWN_RESULTS.md`, `HUNCHES.md`, `CATHOT_REVIEW.md`, `CHECK_OF_CATHOT_OWN_RESULTS_20261112.md`.
- *Return CATHOT (5):* `CATHOT_paper.pdf`, `_results.csv`, `_report.md`, `_D.tex`, `_E.tex`.
- *Grothendieck's text (2):* `DER_III-V.tex` (4 removed), `DER_VII-c.tex`.
- *Programs (19):*
  - `cup_products.py`/`.out`, `catlib.py`.
  - `higher_homology.py` + `_order6.out`, with `dump_classes.py` and `monoid_classes_order6.npy`.
  - `resolution_check.py`/`.out` with `models_check_tables.py`; `models_check.py`/`.out`.
  - `enum_monoids.py` + `_upto6.out`/`.json`; `enum_cats.py` + `_upto6.out`, `_upto7.out`, `_upto7.json`.
- *Literature (6):* `Sweeney_2502.05276v2.pdf`, `BenBassat_2610.38760v1.pdf` and `.tex` (2 removed), `Miller1984.pdf`,
  `Hatcher_AT.pdf`, `Quillen_KtheoryI.pdf`.

**Against ZIP_LIST.tsv (22 rows).**
- *Kept:* all 22.
- *Added 14:*
  - The census programs and their outputs (`enum_*`, 7 files). R4 rests on `OWN_RESULTS.md` 6.1 ("P₂ is the only smallest
    category of type S²"), and Part B3 asks for a lower bound on arrows. The prompt's paragraph already promises "the
    programs and outputs for R3 and R4".
  - `models_check.py`/`.out` (P₂ of type S²).
  - `models_check_tables.py`, without which `resolution_check.py` does not run.
  - `dump_classes.py` and `monoid_classes_order6.npy`, the input of `higher_homology.py`.
  - The TeX source of arXiv:2610.38760v1 (Definition 3.3, Part A3).
  - Quillen, *Higher algebraic K-theory I*. Part A3 names Theorems A and B; it is the same file FINMON and INDLOCAL carry
    for those theorems, and the zip stays under 40 MB.

**PROMPT.md.**
- *Line 7.* It now ends "The attached files are listed in `MANIFEST.tsv` at the root of `S2COUNT_background.zip`."
- *"What is attached", start.* It now reads "The files of `S2COUNT_background.zip`, listed with their origins in
  `MANIFEST.tsv` at its root:".
- *Programs.* "the programs and outputs for R3 and R4" became "… for R3 and R4 (with the census of `OWN_RESULTS.md` 6.1)".
- *Preprint.* "arXiv:2610.38760v1" became "arXiv:2610.38760v1 (PDF and TeX source)".
- *Quillen.* "Quillen, *Higher algebraic K-theory I* (Theorems A and B, Part A3);" was added after Hatcher.
- The rest is unchanged and rewrapped.

**Verdict:** ready to send.
