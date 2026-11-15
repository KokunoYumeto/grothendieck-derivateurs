# Decisions on the unlisted changes in the checked texts

Each part of the companion was checked by GPT-6 Astra (OpenAI, ChatGPT Pro mode), which returned the part's text with
its corrections. The corrections it lists in the part's table (`companion/checks/DER_<part>/DER_<part>_corrections.csv`,
kinds `transcription` and `doubt_resolved`) are applied as listed, except five that the edition's pages overrule
(below); slips of the edition (`edition_slip_kept`) stay as printed. The returned texts also contain 435 changes that no row of those tables lists. Each of them was checked by
Claude Opus 5.5 (Anthropic) against the edition's page (the editors' PDF, rendered at 200 dpi, at 400–600 dpi where a glyph or a
line style had to be told apart) and decided as follows.

- **KEEP**: the new text matches the edition.
- **REVERT**: the old text matched the edition; the change is wrong.
- **STRIP**: a layout addition of the returned text, not the edition's text (wrappers, forced breaks, page breaks,
  small type); the old text is restored.
- **TECHNICAL**: a LaTeX change that prints the same text, arrows and labels (syntax repairs, spacing inside a
  diagram, a stray page break removed); it stays.

The transcription in this folder and the texts of the companion (`DER_<part>_text.tex`) carry the listed corrections and
the KEEP and TECHNICAL changes; the REVERT and STRIP changes are undone. Where a part has a `DER_<part>_text_pro.tex`,
that file is its returned text before the REVERT and STRIP decisions were applied.

`DECISIONS.json` has one entry per change: `hunk` (its number), `chunk` (the part), `package_line` and
`returned_line` (the line of the text's body, after `\begin{document}`, in the part's text as given for the check, that
is its five-page files of this transcription merged in order, and in the returned text), `decision`,
`edition_page` (chapter and printed page), `ms_page`, `pdf_leaf` (the leaf of the part's PDF that was looked at),
`reason`, `file` (the five-page file of this transcription concerned), `package_text` and `returned_text` (the lines
before and after the change), and for change 225 a `note`. In the reasons, "Pro" is GPT-6 Astra (ChatGPT Pro mode), and "the package" is the text
as given for the check.

## Counts

| Decision | Changes |
|---|---|
| KEEP | 69 |
| REVERT | 9 |
| STRIP | 227 |
| TECHNICAL | 130 |
| **Total** | **435** |

| Part | KEEP | REVERT | STRIP | TECHNICAL | Total |
|---|---|---|---|---|---|
| I-a | 9 | 0 | 0 | 0 | 9 |
| I-b | 0 | 0 | 5 | 1 | 6 |
| II-a | 5 | 0 | 3 | 0 | 8 |
| II-b | 0 | 5 | 186 | 4 | 195 |
| III-V | 10 | 0 | 2 | 0 | 12 |
| VI-a | 9 | 0 | 0 | 0 | 9 |
| VI-b | 1 | 0 | 0 | 0 | 1 |
| VI-c | 2 | 0 | 2 | 0 | 4 |
| VII-a | 9 | 1 | 2 | 1 | 13 |
| VII-b | 4 | 1 | 0 | 2 | 7 |
| VII-c | 3 | 0 | 4 | 0 | 7 |
| VIII-X | 0 | 0 | 4 | 0 | 4 |
| XI-XIIa | 0 | 0 | 2 | 1 | 3 |
| XIIapp | 0 | 0 | 0 | 2 | 2 |
| XIIb-a | 0 | 0 | 1 | 5 | 6 |
| XIIb-b | 1 | 0 | 3 | 2 | 6 |
| XIIc-a | 4 | 0 | 0 | 3 | 7 |
| XIIc-b | 1 | 0 | 2 | 90 | 93 |
| XIII-a | 0 | 0 | 3 | 0 | 3 |
| XIII-b | 3 | 0 | 0 | 0 | 3 |
| XIX | 2 | 0 | 0 | 0 | 2 |
| XV-b | 0 | 0 | 0 | 7 | 7 |
| XVI | 0 | 1 | 0 | 2 | 3 |
| XVII-a | 0 | 0 | 0 | 3 | 3 |
| XVII-b | 6 | 0 | 0 | 0 | 6 |
| XVIII-c | 0 | 1 | 0 | 1 | 2 |
| XVIII-d | 0 | 0 | 0 | 2 | 2 |
| XVIII-e | 0 | 0 | 8 | 4 | 12 |

The other parts have no unlisted change.

## Every REVERT

| Change | Part | Edition page | Why |
|---|---|---|---|
| 62 | VII-a | VII p. 30 | 'Ob (Ty/τ′) = ensemble des couples': the edition prints Ty without underline here; the old plain Ty was right |
| 63 | VII-b | VII p. 34 | the label is printed [page 50′] with a math prime, which `50$'$` renders; `50'` prints an apostrophe |
| 213 | XVI | XVI p. 9 | the edition prints the solid top arrow Hom(X, I_H) → Hom(π₀(X), I); the returned text deleted it |
| 226 | XVIII-c | XVIII p. 97 | the edition prints t_α(μλ) on the right of the steep arrow (tikz-cd's default side); `swap` moves it to the left. Its place, about three quarters down, matches `pos=.72`, which could be kept without `swap` |
| 427 | II-b | II p. 51 | a comment only: the returned text resolves the doubt '% ?? italic s or upright s' before R(L) as the italic s (corrections row 45); the edition prints an upright s here, at ms. 70 and on p. 53, so the '% ??' comes back |
| 432 | II-b | II p. 60 | a facsimile panel of ms. 97 (an image of the leaf) in place of the diagram; the diagram as transcribed draws the page |
| 433 | II-b | II p. 61 | a facsimile panel of ms. 98 in place of the first diagram; the diagram as transcribed draws the page but for one arrow, which corrections row 70 corrects (`rrd` → `rrdd`) |
| 434 | II-b | II p. 61 | the second diagram of ms. 98 and footnote 68, deleted for the same panel; the diagram as transcribed draws the page but for one arrow, which row 71 corrects (`rrd` → `rrdd`) |
| 435 | II-b | II p. 62 | a facsimile panel of ms. 99 in place of both diagrams and of 'et dualement on a'; the diagrams as transcribed draw the page but for one arrow, which row 75 corrects (`dr` → `ddr`) |

## Corrections of macro definitions

Ten rows of the tables of corrections (row n is the n-th row of the part's `corrections.csv` after its header)
correct a definition in a preamble rather than the text. Each was checked against the edition's page by Claude Opus 5.5
(Anthropic); the five-page files that carry the definition take the eight that the page confirms.

| Part, row | Correction | Edition page | Decision |
|---|---|---|---|
| I-a 1 | `\Del`: `\mathbf{\Delta}` → `\boldsymbol{\Delta}` | I p. 7 | applied (Der-ChI-234_p006-010): the edition prints a bold Δ, which `\mathbf` loses under fontspec |
| II-a 21 | `\sX`: `\mathscr{X}` → `\mathcal{X}` | II p. 11 | applied (Der-ChII-234_p011-015): the topos letter is the calligraphic X, not the script one |
| II-a 22 | `\X`: `\mathscr{X}` → `\mathcal{X}` | II p. 14 | applied (Der-ChII-234_p016-020), as row 21 |
| VI-a 58 | `\usepackage[no-math]{fontspec}` | VI p. 1 | applied in the nine files of VI-a (Der-ChVI-345_p001-005 to p041-045): the edition prints the bold Δ¹ that fontspec loses without the option |
| XIX 1–3 | `\rcl`: `\neg` → `\bar{}` | XIX p. 1 | applied (der-ch19_p001-005): the right Q-closure mark is a horizontal bar, not a negation sign |
| XIX 44 | `\harp` with the lower-left and upper-right half-heads | XIX p. 23 | applied (der-ch19_p021-025, whose definition had the upper-left and lower-right ones) |
| XVII-b 21 | `\postilde`, `\cl`, `\tl` as `^{\sim}` | XVII pp. 36, 49 | not applied: at (4.5.2) and (6.1.7) the edition prints the small accent tilde of the files' definitions, not the relation tilde `\sim` |
| XVII-b 39 | `^{\sim}` in (6.1.7) | XVII p. 49 | not applied, as row 21 |

The three other listed corrections that are not applied, VII-a 99, XVI 13 and II-b 45, are the changes 62, 213 and
427 above.

## The 195 changes of II-b

182 of them (241–422) are listed in the order of the part's text. 168 of these only add the returned text's layout: a
`\dcfit{...}` wrapper (its opening, its closing brace or both, with the `ampersand replacement=\&` that tikz-cd needs
inside it) or `\dcjoinedprintedpage` in place of `\printedpage`. Each was checked by a script: with the wrapper removed
by brace matching, the option and `\&` undone and the page macro mapped back, the lines equal the text as given for the
check up to spacing, comments included; they are STRIP. Two (244, 304) only add `ampersand replacement=\&` to inline
diagrams in running text: TECHNICAL, as in XIIc-b. The other twelve were checked on their pages and are STRIP (wrappers;
in 309 the returned text also bent an arrow that the edition draws straight). The remaining 13 (423–435) are the
facsimile panels that replace the diagrams of ms. 97–99, with the deletion that goes with the ms. 98 panel, six more
`\dcfit` wrappers and three resolved `% ??` comments, decided by the same rules.

## How the classes were applied

- Macro changes are content. Each was read with the macro definitions of its own part's text, which differ by part (in
  I-a the text's `\Hom` printed an underlined Hom; in VII-b `\Ty` is underlined, in VII-a it is not; in III-V `\Ch` is
  already underlined, so `\underline{\Ch}` printed two lines).
- Layout additions are STRIP when the edition does not show them: raggedright, small-type groups, resizebox, adjustbox
  and `\dcfit` wrappers, `\Needspace`, `\nopagebreak`, forced line breaks and paragraph splits, and the page breaks and
  running-head macro added before chapter covers. Layout changes that reproduce the edition are KEEP: the bars in the
  left margin (XIIc-a, ms. 206 and 227) and the ragged column of the W₀/W₁ lists (XIIc-a, ms. 171).
- Spacing inside a diagram or array (column or row separation, bend angle, label position along the same side,
  invisible spacers) is TECHNICAL, as are repairs that make the intended diagram compile (ampersand replacement inside
  macro arguments, empty nodes as arrow targets) and the removal of three stray `\newpage`/`\clearpage` at the end of
  full pages (VII-a, XIIc-a, XVI).

## The 93 TikZ changes of XIIc-b

84 of them differ from the text as given only by `ampersand replacement=\&` and `\&` for `&` (checked mechanically on
every one). 29 of these were compared with the pages (changes 108–119, 121–125, 140, 148–150, 158, 165, 168, 176–180,
on printed pp. 147–170): in each the diagram's objects, arrows, labels and sides match the edition and the change prints
nothing different; all are TECHNICAL. The other 55 were classed TECHNICAL by the same rule without a page check. Three
of the 84 (158, 165, 168) repair inline diagrams whose code already used `\&` without the option, so they printed
literal ampersands. The 9 changes with further differences were each checked on their page: 105, 106, 107, 188, 192,
193 TECHNICAL (spacing, bends, label positions as printed, empty target nodes); 120 KEEP (α drawn as a short dotted
2-cell between i_Y and i, as printed); 138–139 STRIP (resizebox wrapper).

## Notes

- Pairs that open and close a wrapper have the same decision (10/11, 14/15, 17/18, 48/49, 64/65, 75/76, 78/79,
  138/139, 207/208).
- 63 (REVERT): the scripts in `kit/` read the manuscript page `50$'$` as 50′.
- 226 (REVERT): only the `swap` is wrong; `pos=.72` puts the label where the edition has it.
- 204 (KEEP): the mark is a tilde, not a breve; the edition's glyph is the small accent tilde that Chapter XIX writes
  `^{\tld}` elsewhere, whereas `^{\sim}` draws the relation tilde.
- 219–224 (KEEP): the text now uses `\cl`, defined as `^{\tilde{}}`, which gives the printed glyph (the returned text's
  own preamble redefines it as `^{\sim}`).
- 203 (KEEP): the reset of the footnote counter and the switch to `\fnsymbol` before the Glossaire (Chapter XIII,
  p. 58) give the edition's * and † (p. 61) with arabic numbers for the main text, which is how the five-page files
  of Chapter XIII number their footnotes.
- 98–99 and 101–102 (KEEP) need the packages array, ragged2e and marginnote, which the files concerned and the
  transcription's master now load; 225 (TECHNICAL) fills the boxes for the circled τ labels of ms. 318 (Chapter XVIII,
  p. 120), which were changed under a correction row, and goes with them.
- Some changes lie on pages that two consecutive parts both contain (see `companion/reader/OVERLAPS.md`): 10–11 (I-b
  p. 34), 45 (VI-b p. 43), 46–47 (VI-c pp. 86, 88), 63 (VII-b p. 34), 70 (VII-c p. 72), 92 (XIIb-b p. 81), 105–115
  (XIIc-b pp. 145–149). Their decisions apply to those parts' own texts; the transcription takes these pages from the
  earlier part.
- 432–435 (REVERT): the ms. 97 diagram is right as transcribed. After the revert of 433–435, corrections rows 70, 71
  and 75 of II-b are applied: the arrow from the class 'X cofiltrante' ends at the class 'X localement cofiltrante'
  (`rrdd`, `ddr`), as on the edition's pp. 61–62, not at the example box below it.
- 425 and 427: the edition prints the raised s of ˢR upright (II pp. 43, 51 and 53). The texts and the preamble's `\sR`
  write the italic `{}^{s}`; the upright `{}^{\mathrm{s}}` is not set yet.
- 278 (STRIP) restores the `% ??` of the transcription on the underbrace of ms. 55; its resolution, corrections row 12
  of II-b, is right.
- 283 and 284 are one change: the items of the ms. 57 list are paired across the two. The 41 wrappers of II-b whose
  ends lie in different changes have the same decision on both.
- 241–270 and 423 lie on pp. 29–33 of Chapter II, which II-a also contains (`Der-ChII-234_p031-035.tex`); the
  transcription takes these pages from II-a.
