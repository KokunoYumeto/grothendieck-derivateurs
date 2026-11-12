# Translation comparison: La Longue Marche and Les Dérivateurs into English

Runs from 2026-11-10 22:48 to 2026-11-10 23:18 (UTC). Made by Claude (Claude Code, Opus 5.5) at the user's request of 10 November 2026.

Seven configurations translated the same French with the same prompt: five pages of each work (one page of each for the reference, Claude Fable 5.2 at max). Below: what each run cost, what it would cost for the whole works, and the script checks of every output. Nothing here judges which translation is best; the blind grading (`blind/`, `key/KEY.json`) does that.

Total billed for the comparison: **$3.25** at batch and Flex prices (budget $15), 7 runs, one at a time. List price (no batch or Flex discount) is twice each figure.

## The texts

| sample | what | source file (lines) | characters |
|---|---|---|---|
| `source/LM.tex` | La Longue Marche, package LM_P049 (second pass), scans 483-487 (manuscript pages 245-247) | `user\Documents\longue_marche_pro_pilot_20261104\second_pass\LM_P049_checked.tex` (61-183) | 9,420 |
| `source/DER.tex` | Les Dérivateurs, Ch. XVIII (chunk DER_XVIII-a, corrected French of 11 Nov), edition pages 1-5 (manuscript pages 50-60) | `user\Documents\derivateurs_companion_20261109\corrected_french_20261111\DER_XVIII-a.tex` (139-394) | 14,878 |
| `source/LM_ref.tex` | La Longue Marche, package LM_P049 (second pass), scan 483 | `user\Documents\longue_marche_pro_pilot_20261104\second_pass\LM_P049_checked.tex` (61-98) | 2,188 |
| `source/DER_ref.tex` | Les Dérivateurs, Ch. XVIII (chunk DER_XVIII-a), edition page 1 | `user\Documents\derivateurs_companion_20261109\corrected_french_20261111\DER_XVIII-a.tex` (139-168) | 3,774 |

- **LM**: package LM_P049 after its second pass (`LM_P049_checked.tex`; no `_checked_fixed` exists for it), scans 483-487, consecutive: prose, 138 formulas (2 displays), 27 `\deleted`, 28 `\inserted`, 71 `\unsure` (19 bars between alternative readings), 13 `\illegible`, 6 `\margin`, 6 `\uline`, his abbreviations. The window was chosen among the five-scan windows of the second-passed packages for the number of glossary entries it contains (42) and a length near the mean (1,884 characters per scan against 1,941 over 1,314 scans).
- **DER**: `DER_XVIII-a.tex` of `corrected_french_20261111`, edition pages 1-5 (manuscript pages 50-60), consecutive: the opening of §4 (4.1 "Pseudo-topos. Problème du produit" and the start of 4.2), prose, 158 formulas (35 displays, 2 tikz-cd diagrams), 3 footnotes, 3 editors' `\texttt{[...]}` additions, 15 comments (running heads, [sic] notes). `UNEXPLAINED.md` lists no line for DER_XVIII-a (nor for DER_XIV), so no line had to be avoided.
- **Reference pages** (Fable 5.2 at max): the first page of each sample, LM scan 483 and DER page 1.
- Each source file's sha256 is in `selection/MANIFEST.json`. No source file was changed by this work. Another session rewrote the files of `corrected_french_20261111` during the runs (10 Nov, 23:16 and 23:20 UTC); `DER_XVIII-a.tex` came back byte for byte the same (its sha256 still matches), so the sample is current. Three other chunks changed a little, which moves the DER total used below by a few hundred characters.

## The prompt

One prompt per work, identical for every configuration: `prompt/system_LM.txt`, `prompt/system_DER.txt` (template `prompt/PROMPT_TEMPLATE.txt`, parts `prompt/PROMPT_PARTS.txt`, built by `scripts/prepare.py`); the user message of each request is `prompt/user_<sample>.txt` (for DER it also lists the chunk's macro definitions used on the pages, for reference). It asks for a faithful English in his voice and register (his own English of *Pursuing Stacks* as the model, American spelling); every macro, page anchor and comment line kept, the words inside the text-carrying macros translated (`\deleted` included; both readings of `\unsure{A|B}` when they are words); formulas copied character for character, only French in `\text{...}` translated; paragraphs kept; only the translated LaTeX returned.

The terms are the glossary entries (`translation_glossary_20261110`, decision files `scripts/entries_*.txt`) whose French occurs on the pages, found with the glossary's own regular expressions (`scripts/list_hits.py`, `selection/HITS_*.json`): 42 entries for LM, 23 for DER, written compactly (one line each, related entries sometimes joined). Of the notation and typesetting decisions, the prompt carries those that act on the prose: his abbreviations written out, quotation marks ``...'', the editors' brackets translated, `\uline` kept, the apparatus of the transcription. Those that would change a formula are left out, because the formulas must come back unchanged; on these pages they are: LM `\boldsymbol{\Gamma}` as one macro for the doubled Gamma, `(1)\qquad` as `\tag{1}`, `\mathrm{Norm}` as `\operatorname{Norm}`, `\longrightarrow` in running text as `\to`; DER `\mathcal{U}` as `\mathfrak{U}`, `\mathrm{Hom}` as `\operatorname{Hom}`, (Ens) as (Sets), "déf" as "def" over the equality sign, `\longrightarrow` in running text as `\to`. They are mechanical and can be applied by script after the translation (for DER the macros `\Hom`, `\uHom`, `\Ens`, `\defeq` carry four of them, so the English preamble does it); the two pending decisions (natural or sharp, Fraktur S or calligraphic S) are copied as read. Two lines of the prompt go slightly beyond the glossary: "likewise pseudo-topoi" (from topos, plural topoi) and "bi-contrafoncteur → bi-contrafunctor" (from contrafoncteur).

## Configurations and cost

Prices per million tokens, input/output: Opus 5.5 $2/$10, Fable 5.2 $4/$20, Sonnet 5.5 $1/$5 (Message Batches API, half the list price); GPT-6.1 Sol $1/$5 (Flex tier). Output tokens include the thinking (Anthropic) or the reasoning tokens (OpenAI); "thinking" below is the output minus the visible translation, which was counted with the token-counting endpoint (Anthropic) or reported by the API (OpenAI). All requests: adaptive thinking, output cap 128,000 tokens, no prompt caching.

| configuration | tokens in (LM + DER) | tokens out (LM + DER) | of which thinking | billed | $ per page LM | $ per page DER | minutes |
|---|---|---|---|---|---|---|---|
| Claude Opus 5.5, effort high, Message Batches API | 6,685 + 10,350 | 9,508 + 12,054 | 4,987 + 4,121 | $0.250 | $0.022 | $0.028 | 3.2 |
| Claude Fable 5.2, effort medium, Message Batches API | 6,685 + 10,350 | 9,150 + 8,699 | 4,626 + 749 | $0.425 | $0.042 | $0.043 | 2.2 |
| Claude Opus 5.5, effort max, Message Batches API | 6,685 + 10,350 | 52,645 + 57,526 | 48,120 + 49,585 | $1.14 | $0.108 | $0.119 | 6.9 |
| Claude Fable 5.2, effort high, Message Batches API | 6,685 + 10,350 | 14,022 + 14,738 | 9,497 + 6,803 | $0.643 | $0.061 | $0.067 | 2.9 |
| Claude Sonnet 5.5, effort high, Message Batches API | 6,685 + 10,350 | 4,478 + 7,950 | ≈0 + ≈0 | $0.079 | $0.006 | $0.010 | 2.2 |
| GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier | 4,327 + 6,789 | 6,400 + 6,422 | 3,449 + 1,034 | $0.075 | $0.007 | $0.008 | 4.1 |
| Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work) | 2,921 + 3,468 | 8,987 + 21,859 | 7,895 + 20,084 | $0.642 | $0.191 | $0.451 | 4.3 |

The three Anthropic models share a tokenizer, so their input counts are the same; GPT-6.1 Sol's tokenizer counts about two thirds as many tokens for the same text. "≈0": Sonnet 5.5 at effort high chose not to think (its output equals the counted translation within the counting error). The visible translation itself is about 4,500 (LM) and 7,900 (DER) tokens for the Anthropic models.

Batch IDs, stop reasons and per-request figures: `runs/RUNS.jsonl`, `runs/<configuration>/<sample>_result.json`; one ledger row per run in `compute_cost_ledger/LEDGER.jsonl` (ids `trcmp-<configuration>`).

## Extrapolation to the whole works

Two estimates per work: the cost per page times the pages, and the cost per character of French times the characters of the whole work (which corrects for the samples being a little shorter or longer than the average page). LM: about 1,500 scan pages at 1,941 characters each (the mean over the 1,314 second-passed scans); DER: the 1,171 pages of the corrected French, 3,400,778 characters in all (2,904 per page). Same prompt, five pages per request, batch or Flex prices, no caching.

| configuration | LM, 1,500 pages: per page | by length | DER, 1,171 pages: per page | by length | both works (by length) | against Opus 5.5 high |
|---|---|---|---|---|---|---|
| Claude Opus 5.5, effort high, Message Batches API | $32.54 | $33.53 | $33.08 | $32.28 | $65.81 | 1.00× |
| Claude Fable 5.2, effort medium, Message Batches API | $62.92 | $64.84 | $50.44 | $49.23 | $114.07 | 1.73× |
| Claude Opus 5.5, effort max, Message Batches API | $161.95 | $166.88 | $139.57 | $136.22 | $303.10 | 4.61× |
| Claude Fable 5.2, effort high, Message Batches API | $92.15 | $94.96 | $78.73 | $76.84 | $171.80 | 2.61× |
| Claude Sonnet 5.5, effort high, Message Batches API | $8.72 | $8.99 | $11.73 | $11.45 | $20.44 | 0.31× |
| GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier | $10.90 | $11.23 | $9.11 | $8.89 | $20.12 | 0.31× |
| Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work) * | $287.14 | $254.77 | $528.18 | $406.45 | $661.22 | 10.05× |

\* The reference translated one page per request, so its fixed share of the prompt per page is five times that of the others; its figures are an upper bound for five-page requests.

## Script checks

`scripts/checks.py`, on every full output against its French (`checks/CHECKS.json`; one detail file per output in `checks/`, with every changed formula, every flagged sentence and every missing term).

1. **Formulas and macros back unchanged.** Every formula (inline, display, math environments) compared in order with the French after masking the words inside `\text{...}`: identical / identical up to spacing / changed / missing / added. Page anchors (`\scanpage`, `\mspage`, `\printedpage`, `\msp`) in order; the comment lines; the count of every macro outside formulas; the bars of `\unsure{A|B}`.
2. **No French left.** French function words (le, la, des, que, qui, dans, ...) and elisions (l', d', qu') in the running text, and sentences with several of them; accented words other than étale, dévissage and names; and French left in the wording of `\text{...}` boxes inside formulas (masked in check 1, to be translated).
3. **Paragraph lengths.** Paragraphs split at blank lines and paired in order; the running text (formulas and macro names removed) English/French; flagged below 0.7 or above 1.5.
4. **Glossary.** For each glossary entry on a French page, whether its English form occurs on the same page of the output ("entry-pages"), and occurrences covered; British spellings (the glossary decided American).

### LM

| configuration | stop | only LaTeX | formulas: identical / spacing / changed / missing / added (of French) | anchors in order | comments | macro counts differing | French words / flagged sentences / elisions / French \text{} boxes in formulas | paragraphs EN/FR, median ratio (min-max), flagged | glossary entry-pages, occurrences | British |
|---|---|---|---|---|---|---|---|---|---|---|
| Claude Opus 5.5, effort high, Message Batches API | end_turn | yes | 138 / 0 / 0 / 0 / 0 (138) | yes | all | none | 0 / 0 / 0 / 0 of 1 | 19/19, 1.012 (0.922-1.056), 0 | 70/70, 105/105 | 0 |
| Claude Fable 5.2, effort medium, Message Batches API | end_turn | yes | 138 / 0 / 0 / 0 / 0 (138) | yes | all | none | 0 / 0 / 0 / 0 of 1 | 19/19, 1.0 (0.945-1.062), 0 | 70/70, 105/105 | 0 |
| Claude Opus 5.5, effort max, Message Batches API | end_turn | yes | 138 / 0 / 0 / 0 / 0 (138) | yes | all | none | 0 / 0 / 0 / 0 of 1 | 19/19, 1.0 (0.908-1.102), 0 | 70/70, 105/105 | 0 |
| Claude Fable 5.2, effort high, Message Batches API | end_turn | yes | 138 / 0 / 0 / 0 / 0 (138) | yes | all | none | 0 / 0 / 0 / 0 of 1 | 19/19, 1.002 (0.908-1.095), 0 | 70/70, 105/105 | 0 |
| Claude Sonnet 5.5, effort high, Message Batches API | end_turn | yes | 137 / 0 / 1 / 0 / 0 (138) | yes | all | deleted 27→26, illegible 13→12, unsure 55→53 | 0 / 0 / 0 / 1 of 1 | 19/19, 0.98 (0.892-1.062), 0 | 70/70, 105/105 | 0 |
| GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier | completed | yes | 138 / 0 / 0 / 0 / 0 (138) | yes | all | none | 0 / 0 / 0 / 0 of 1 | 19/19, 1.011 (0.892-1.095), 0 | 70/70, 105/105 | 0 |
| Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work) | end_turn | yes | 38 / 0 / 0 / 0 / 0 (38) | yes | all | none | 0 / 0 / 0 / 0 of 1 | 3/3, 0.962 (0.936-0.997), 0 | 15/15, 26/26 | 0 |

### DER

| configuration | stop | only LaTeX | formulas: identical / spacing / changed / missing / added (of French) | anchors in order | comments | macro counts differing | French words / flagged sentences / elisions / French \text{} boxes in formulas | paragraphs EN/FR, median ratio (min-max), flagged | glossary entry-pages, occurrences | British |
|---|---|---|---|---|---|---|---|---|---|---|
| Claude Opus 5.5, effort high, Message Batches API | end_turn | yes | 158 / 0 / 0 / 0 / 0 (158) | yes | all | none | 0 / 0 / 0 / 0 of 9 | 22/22, 0.956 (0.896-1.079), 0 | 42/42, 87/87 | 0 |
| Claude Fable 5.2, effort medium, Message Batches API | end_turn | yes | 158 / 0 / 0 / 0 / 0 (158) | yes | all | none | 0 / 0 / 0 / 0 of 9 | 22/22, 0.986 (0.903-1.079), 0 | 42/42, 87/87 | 0 |
| Claude Opus 5.5, effort max, Message Batches API | end_turn | yes | 158 / 0 / 0 / 0 / 0 (158) | yes | all | none | 0 / 0 / 0 / 0 of 9 | 22/22, 0.969 (0.898-1.079), 0 | 42/42, 87/87 | 0 |
| Claude Fable 5.2, effort high, Message Batches API | end_turn | yes | 158 / 0 / 0 / 0 / 0 (158) | yes | all | none | 0 / 0 / 0 / 0 of 9 | 22/22, 0.969 (0.886-1.079), 0 | 42/42, 87/87 | 0 |
| Claude Sonnet 5.5, effort high, Message Batches API | end_turn | yes | 158 / 0 / 0 / 0 / 0 (158) | yes | all | none | 0 / 0 / 0 / 6 of 9 | 22/22, 0.961 (0.855-1.184), 0 | 42/42, 84/87 | 0 |
| GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier | completed | yes | 158 / 0 / 0 / 0 / 0 (158) | yes | all | none | 0 / 0 / 0 / 0 of 9 | 22/22, 0.956 (0.886-1.076), 0 | 42/42, 87/87 | 0 |
| Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work) | end_turn | yes | 54 / 0 / 0 / 0 / 0 (54) | yes | all | none | 0 / 0 / 0 / 0 of 0 | 8/8, 1.0 (0.932-1.079), 0 | 15/15, 36/36 | 0 |

Details that the tables compress (from the detail files):

- **Claude Opus 5.5, effort high, Message Batches API, LM**: nothing to report
- **Claude Opus 5.5, effort high, Message Batches API, DER**: nothing to report
- **Claude Fable 5.2, effort medium, Message Batches API, LM**: nothing to report
- **Claude Fable 5.2, effort medium, Message Batches API, DER**: nothing to report
- **Claude Opus 5.5, effort max, Message Batches API, LM**: nothing to report
- **Claude Opus 5.5, effort max, Message Batches API, DER**: nothing to report
- **Claude Fable 5.2, effort high, Message Batches API, LM**: nothing to report
- **Claude Fable 5.2, effort high, Message Batches API, DER**: nothing to report
- **Claude Sonnet 5.5, effort high, Message Batches API, LM**: changed `$\unsure{\mathrm{Centre}}(\pi)=1$` → `$\unsure{\mathrm{Center}}(\pi)=1$`; marks lost or added, by page: 483 deleted 4→3, 483 illegible 1→0, 484 unsure 9→8, 487 unsure 18→17; French left in \text{} of formulas: "ou"
- **Claude Sonnet 5.5, effort high, Message Batches API, DER**: French left in \text{} of formulas: "pl. fid.", "pl. fid.", "pl. fid.", "pleinement fidèle", "pleinement fidèle", "pleinement fidèle"; terms found fewer times than their French: pleinement fidèle (page 5: 7 in the French, 4 in the English)
- **GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier, LM**: nothing to report
- **GPT-6.1 Sol, reasoning effort high, OpenAI Responses API, Flex tier, DER**: nothing to report
- **Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work), LM_ref**: nothing to report
- **Claude Fable 5.2, effort max, Message Batches API (reference: one page of each work), DER_ref**: nothing to report

Limits of the checks: they test form, not sense. A formula can be right and the sentence around it wrong; a term can be present on the page and still be used in the wrong place; the French-word list catches untranslated sentences, not mistranslated ones; paragraph ratios catch omissions and additions of some size only.

## The blind set

`blind/<work>_<letter>.tex`: each full output, byte for byte, letters assigned at random per work (`scripts/blind.py`, random.SystemRandom); the letter-to-configuration mapping in `key/KEY.json`; the French in `source/` (`LM.tex`, `DER.tex`, and `LM_ref.tex`, `DER_ref.tex` for the one-page reference). No blind file names a model or a provider (checked by script). The grader should read only `blind/`, `source/` and `prompt/`; `runs/`, `checks/`, `key/` and this file name the configurations, and `selection/` holds how the pages were chosen (hashes, glossary hits). In each work one blind file covers only the first page: it translates `source/LM_ref.tex` or `source/DER_ref.tex`.

## Files

`scripts/`: `common_tc.py` (samples, glossary machinery), `list_hits.py`, `prepare.py`, `run.py` (one run at a time, budget and one-batch-at-a-time checks, ledger rows), `checks.py`, `blind.py`, `report.py`. Keys were read only through `claude_tools/run_with_note_key.py` (Anthropic, account B, `Untitled 1939.md`) and `enr_pilot.call` (OpenAI, `Untitled 1936.md`); none was printed or stored.

## Blind grading and the decision (11 Nov 2026)

GPT-6.1 Sol at reasoning effort max was added at the user's request ("what about Sol Max?"); it passed every script
check (formulas 296/296 identical, anchors, no French left, glossary 112/112). The eight outputs were re-lettered at
random (`key/KEY.json`; the seven-run letters kept as `key/KEY_7runs_20261111.json`, `blind_7runs_20261111/`) and graded
blind and independently by two subscription agents, Claude Fable 5.2 (g1) and Claude Opus 5.5 (g2), from
`grading/GRADING_BRIEF.md`: `grading/GRADE_g1.*`, `grading/GRADE_g2.*`.

| Configuration | LM fidelity / English | DER fidelity / English | Mean fidelity | Minor slips (both graders) | Both works |
|---|---|---|---|---|---|
| Sol 6.1, max (Flex) | 9.50 / 8.25 | 9.50 / 9.00 | 9.50 | 4 | $81 |
| Fable 5.2, max (one page each) | 9.25 / 8.50 | 9.50 / 9.00 | 9.38 | 1 | $661 |
| Fable 5.2, high | 9.25 / 8.50 | 9.50 / 8.25 | 9.38 | 6 | $172 |
| Fable 5.2, medium | 9.25 / 8.50 | 9.25 / 7.75 | 9.25 | 8 | $114 |
| Opus 5.5, max | 9.25 / 8.50 | 9.25 / 8.75 | 9.25 | 6 | $303 |
| Sol 6.1, high (Flex) | 9.25 / 8.50 | 8.75 / 8.75 | 9.00 | 7 | $20 |
| Opus 5.5, high | 8.50 / 8.50 | 8.25 / 8.25 | 8.38 | 15 | $66 |
| Sonnet 5.5, high | 6.50 / 8.00 | 7.00 / 7.75 | 6.75 | 49 | $20 |

No configuration made a major error. **Decision (Claude, 11 Nov): GPT-6.1 Sol, effort max, Flex, for both works**
(about $81 for about 2,700 pages, on the OpenAI key); the user's rule was quality first, cheaper only without loss.
Two slips shared by most versions go into the glossary before the bulk run: "action effective" (as against
"extérieure") is "actual action" (in English an effective action is a faithful one); "sans doute" is "probably", not
"no doubt". Cost of the comparison: $3.25 + $0.30 (Sol max); the grading ran on the subscription.
