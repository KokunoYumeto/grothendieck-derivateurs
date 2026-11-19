# Brief: intake of S2COUNT (final) and REVLOC (checkpoint 17, stalled = final), folded into FRAISSE_EXACT and DER_FOLLOWUP (17 Nov 2026)

To: a5ead5c6fd26104b9, Claude Fable 5.2 (launched at effort high), the Derivateurs intake agent. You folded the INDLOCAL
final into the five Derivateurs prompts on 15 Nov 2026, 00:2x UTC. From: the main session (Claude Opus 5.5 at effort
max), 17 Nov 2026 ~00:5x UTC.

## The user's word (17 Nov 00:4x UTC)

"Since S2 count final is final, taking that one in may be smart. Finmon is still running. Revlog is also final because
that one I think is stalled ... So you could take the Revlog and S2 count as the ones that we have ... If there are
other prompts that need to be written that genuinely just don't fall in that based on S2 count, Revlog, and the other
stuff, so be it. There's no prohibition on writing more prompts. Just being parsimonious with the amount of them, not
necessarily with the mathematics that ends up being requested as part of them."

## What changed since your last turn

- 04_FRAISSE_EXACT and 05_DER_FOLLOWUP are still unsent, in
  `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112\`.
- The main session changed them on 17 Nov. Backups are in `pro_prompts_max_20261112_work\DER_FOLLOWUP\backup_fold_20261117\`.
- **DER_FOLLOWUP:**
  - **R19:** findings from Michel Hua's project on cotes 104, 105, 106, 114 and 118, including Cisinski 4.3.2
    (g) ⇒ (c), which needs a hypothesis.
  - **R20 and a new Part G:** the Derivateurs field expert's answers on the weak localization axiom. Do 9.11–9.13,
    finite products and `u_!` hold under Loc (1)–(3) alone? And a second reading of Prop. 9.12.
  - **New attachments:** `chapters_XV_XVI/DER_XV-b.tex`, `chapters_XV_XVI/DER_XVI.tex` and `R20_expert_XV_XVI.md`.
  - **A line on the edition's notes:** they are cited when used.
- **FRAISSE_EXACT:** the same citation line only.
- **The edition's notes stay in attachments.** The user, 17 Nov: reading by a model is fine, only publishing is not.
  Do not strip them.
- **Where the two prompts go:** both will be sent on the Pro account that has one or two maths slots left. Keep the zips
  lean: each added file must earn its place.

## The task, the whole of it

1. **Read the two returns.**
   - S2COUNT final:
     `derivateurs_companion_20261109\pro_prompts_max_20261112_work\S2COUNT\S2COUNT_final_20261116T0841Z_unzipped\S2COUNT\`.
     Read `S2COUNT_results.csv` (22 KB) and `S2COUNT_report.md` (20 KB) whole; read `notes/` and the sections only for
     the rows you weigh.
   - REVLOC checkpoint 17, its last return (the run stalled):
     `...\REVERSIBLE_LOCALIZERS\REVLOC_checkpoint_17_20261116T0257Z_unzipped\REVLOC\`.
     Read `REVLOC_results.csv` (80 KB) whole. Read `REVLOC_report.md` (141 KB) only for its summary, what is open and
     what is refuted. Read the sections only for the rows you weigh.
2. **Write the intake:** `derivateurs_companion_20261109\pro_prompts_max_20261112_work\INTAKE_S2COUNT_REVLOC_20261117.md`.
   - Verdicts on sense for the rows that matter.
   - What is new, and what is open.
   - What each result implies for FRAISSE_EXACT and DER_FOLLOWUP: for example REVLOC H.4, the truncation localizers,
     against DER_FOLLOWUP Part A; the S2 frontier against both.
   - Check what you use, and name every step you doubt.
3. **Fold the results into the two prompts**, as you did with INDLOCAL:
   - R-entries in "Results this prompt builds on", with status (unrefereed GPT-6 Astra, ChatGPT Pro mode) and with
     the rule that the run checks what it uses;
   - items or narrowed items in the Parts where a result changes a question;
   - the attachments: the registers and only the sections that are used, with MANIFEST rows;
   - first a backup of each PROMPT.md and zip, in `backup_s2count_revloc_intake_20261117/` in each work folder, and a
     `ZIP_ADD_S2COUNT_REVLOC_20261117.md` listing what was added.
4. **A new prompt, only if needed.** If the results raise questions that fit neither prompt, draft the items of ONE
   new prompt for that cluster, the whole mathematics of it (items, leads, background files) in
   `pro_prompts_max_20261112_work\NEW_PROMPT_ITEMS_20261117.md`. The main session builds its procedure.
5. **Lint:** `python -I -B <local>/Documents/claude_tools/push_rule_pro_prompts.py --lint-math <PROMPT.md>`
   must pass for both prompts.

## Bounds and rules

- Stop by about 935k of context. Your context is about 857k now, so about 75k of room: read the registers and the
  report summaries first, and only the sections you need.
- No sub-agents. No Grep or Glob over Documents or other big trees: name the exact folders.
- Name every model with its effort.
- Do not stop for context. If your context starts with a summary, you were compacted: reread this brief and your
  files, then go on.
- Reply to me in at most ten lines: what is new, what you folded where, whether a new prompt is needed, and the lint
  results.
