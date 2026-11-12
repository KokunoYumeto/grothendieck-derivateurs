# *Les Dérivateurs*: French and English readers and the companion's appendix of new results, raw build of 12 November 2026

This folder holds the readers build of Grothendieck's *Les Dérivateurs* as it came back: six books (French and English,
each in three forms) made from one annotated master per language, the companion book rebuilt with a new appendix of
results proved along the way, and the build records. Nothing in the returned files has been changed.

## What each file is

| File | What it is |
|---|---|
| `output/FR/DER_FR_diplomatique.tex`, `.pdf` | French, diplomatic: the edition as printed, its slips kept, the editors' notes kept and marked as theirs, edition and manuscript pages in the margin (915 pages) |
| `output/FR/DER_FR_corrige_apparat.tex`, `.pdf` | French, corrected with apparatus: the slips of the edition corrected, each place linked to an apparatus entry giving the printed reading, the correction and its source (1,082 pages) |
| `output/FR/DER_FR_texte_de_lecture.tex`, `.pdf` | French, plain reading text: the corrected text without apparatus and without the editors' notes, a neutral sign `[…]` where text is missing or illegible, page numbers in the margin, a preface saying what was left out (899 pages) |
| `output/EN/DER_EN_diplomatic.tex`, `.pdf` | English, diplomatic: the published English translation, which follows the French as printed (915 pages) |
| `output/EN/DER_EN_corrected_apparatus.tex`, `.pdf` | English, corrected with apparatus: the same corrections wherever they change the English, and the glossary, notation and typesetting decisions (1,061 pages) |
| `output/EN/DER_EN_reading.tex`, `.pdf` | English, plain reading text (902 pages) |
| `output/FR/DER_FR_annotated_master.tex`, `output/EN/DER_EN_annotated_master.tex` | The annotated masters from which the three forms of each language are generated (`\DERform` 0, 1, 2); each PDF beside them is the master's default (diplomatic) form, 915 pages |
| `output/companion/` | The companion book with the new chapter `appendix_new_results.tex` ("Results proved along the way that we did not find in the literature", 12 entries), its master `LesDerivateurs_companion.tex`, bibliography, style, the 32 parts as shipped in release v2026-11-11b, and the rebuilt `LesDerivateurs_companion.pdf` (1,906 pages; the appendix is on pages 1,862–1,882) |
| `output/records/` | The build records: change logs (`CHANGES_FR.tsv`, `CHANGES_EN.tsv`), correction decisions (`CORRECTIONS_DECIDED.tsv`), flagged glossary entries (`GLOSSARY_FLAGGED.tsv`), apparatus counts, the omissions of the reading texts (`EDITORIAL_NOTES_*.tsv`), page-anchor checks, validation reports, compile logs and the build scripts. Start with `output/records/README.md`, the build's own README |
| `PROMPT.md` | The prompt as sent |

The three delivered archives (`DER_READERS_FR.zip`, `DER_READERS_EN.zip`, `DER_READERS_RECORDS.zip`) each carried a copy
of the build's README at their root; the three copies are identical to `output/records/README.md` and are kept once.
The scripts in `output/records/scripts/` are published as returned; we have not run them.

## Who made it

The readers, their apparatus, the annotated masters, the appendix and the records are AI-produced by GPT-6 Astra
(OpenAI, ChatGPT Pro mode), 12 November 2026, from our transcription at release v2026-11-11b (commit `f42cfdd`), the
published English translation (`en/`, tag en-2026-11-12), the companion's tables of corrections, the companion book at
`f42cfdd`, `NEW_RESULTS.md` with the proof files it cites, and the glossary, notation and typesetting tables. The text is
that of the edition by M. Künzer, J. Malgoire and G. Maltsiniotis. The three input archives (SHA-256 `13c6ef40…`,
`d64e2184…`, `b1c3a262…`) were built from those sources; the build verified all 721 of their members.

## Credits

- **Author:** Alexander Grothendieck, *Les Dérivateurs* (1990–1991).
- **Edition transcribed:** the electronic edition by M. Künzer, J. Malgoire and G. Maltsiniotis (Universités de
  Montpellier II et Paris VII), <https://webusers.imj-prg.fr/~georges.maltsiniotis/groth/Derivateurs.html>. The
  deciphering of the manuscript, its edition and the editors' notes are theirs.
- **Transcription:** AI-transcribed (Claude Opus 5.5, Anthropic).
- **Companion:** commentary, register of claims and corrections AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode),
  checked and integrated by Claude Opus 5.5 (Anthropic); the commentary from reviewed answers as credited in the
  repository README.
- **English translation:** AI-translated by GPT-6.1 Sol (OpenAI API, reasoning effort max); glossary by Claude Fable 5.2
  and Claude Opus 5.5; prompt, checks, fixes, completeness comparison and the English book by Claude Opus 5.5
  (Anthropic).
- **This build:** reader construction, AI-produced corrections and apparatus, audits and the assembly of the appendix
  by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Each appendix entry keeps its own "proved by" and "checked by" lines.
- **Check and publication of this folder:** Claude Opus 5.5 (Anthropic).

Each reader's front matter carries these credits and the rights statement in its own language.

**Credit correction for the appendix.** The appendix was built from `NEW_RESULTS.md` as it stood before the credit
correction of 12 November (commit `38b5740`). Its "Proved by" and "Checked by" lines for entries 1, 3, 6, 8, 11 and 12
are superseded by the corrected credits, which add the earlier work at other effort settings:
entry 1, the finite-dimensional case is G.4 of the CATHOT return (GPT-6 Astra) and its K-theoretic proof was first
written for this problem by Claude Fable 5.2 (effort medium), 11 Nov; entry 3, the reduction of E.17 was first found by
Claude Fable 5.2 (effort medium), 10 Nov, and (KT_μ) and E.17 for small filtered index categories were first proved by
GPT-6 Astra in the GALOIS return, B.10–B.12, 11 Nov; entry 6, the question was posed by Claude Fable 5.2 (effort high),
the minima came from the CATHOT return G.14–G.15, and were first proved without citation by Claude Fable 5.2 (effort
medium), 10 Nov; entry 8, first in the companion's commentary on XII and TOTASPH A.13 (GPT-6 Astra), found again independently by
Claude Fable 5.2 (effort max), 12 Nov, and also checked by Claude Fable 5.2 (effort medium), 10–11 Nov; entry 11, checked
by Claude Fable 5.2 at effort medium (10–11 Nov) and then at effort max (12 Nov); entry 12, proved by GPT-6 Astra (G.4 and G.6) answering a question set by Claude Fable 5.2 (effort high), 10 Nov,
checked by Claude Fable 5.2
(effort medium) on 10 Nov, completed and checked on 11 Nov, and re-checked at effort max on 12 Nov. The re-proofs at effort
max of 12 Nov stand as stated in the appendix.

## The build's own counts

From `output/records/README.md` and its validation files:

- 1,879 correction rows of kind `edition_slip_kept`: 1,707 applied, 79 merged with another row at the same place,
  64 without effect on the text, 29 rejected with a reason (`CORRECTIONS_DECIDED.tsv`, 95 decisions). They give
  1,982 French variants; each has one apparatus entry in the corrected form and none in the other two forms.
- English: 1,623 variants (1,388 from the edition's slips, 226 typesetting, 9 glossary); every French variant has a
  recorded English outcome (1,464 applied, 518 without effect on the English).
- Conventions: 223 entries audited (171 glossary, 26 notation, 26 typesetting); 17 not applied, with reasons
  (`GLOSSARY_FLAGGED.tsv`).
- Reading texts: 977 logged omission operations per language (910 bracketed editors' notes among them); 11 neutral
  signs per language; no struck-out words reconstructed.
- Page anchors: 1,176 edition anchors and 2,023 manuscript anchors per language, the same in every form.
- The three known LaTeX errors of the transcription (XIIc p. 61–64, XIV p. 11, XV p. 31–35) are fixed in every form.
- Compilation (the build's records): all six readers, both masters and the companion with 0 errors, 0 missing glyphs,
  0 undefined references; one package warning each (epstopdf: shell escape off).
- The build's privacy scan of all nine PDFs (9,510 pages), their metadata and links, and every text file: 0 findings.
- Appendix: 12 entries, each with statement, proof as supplied, bearing on the manuscript, provenance, and a paragraph
  "GPT-6 Astra's reading". Three cited files were not in the build's input (see Status).

## Our check (Claude Opus 5.5, 12 November 2026)

- **Archives.** The three delivered archives match the build's receipt (bytes and SHA-256); all 216 members match it
  byte for byte. The three input archives the build lists are the ones we sent.
- **Page counts** of the delivered PDFs: French 915 (diplomatic), 1,082 (corrected with apparatus), 899 (reading),
  915 (master); English 915, 1,061, 902, 915; companion 1,906 with the appendix on pages 1,862–1,882. All as the
  build states.
- **Compilation.** We compiled the six readers and the companion from their `.tex` with LuaLaTeX (MiKTeX, LuaHBTeX
  1.25.7, LaTeX 2025-11-01), shell escape off; readers in two passes, the companion in four with BibTeX. Result for
  all seven: 0 errors, 0 missing glyphs, 0 undefined references or citations, no rerun request. Overfull boxes
  (horizontal/vertical) as the build reports: French 31/1, 36/1, 27/1; English 29/0, 32/1, 26/2;
  companion 15/7. Pages: all as delivered except the English diplomatic text, 916 pages here (one page more, from
  Chapter XIV on), a difference of TeX installation. Besides the build's one warning (epstopdf: shell escape off),
  each of the six readers here also warns once that Latin Modern has no bold small caps (bold upright used instead).
- **Privacy.** Every file in this folder and the full text, metadata, outlines and links of all nine PDFs (9,510
  pages): no personal name, no local path, no e-mail address (the editors' addresses stay "[e-mail address removed]"),
  no key or token. The build's README links a checkpoint in the ChatGPT library of the account that ran it; the link
  opens nothing for anyone else.
- **Credits and rights.** All six readers carry, in their language: Grothendieck as author; the edition by M. Künzer,
  J. Malgoire and G. Maltsiniotis as the edition transcribed, with "the deciphering, edition and editors' notes are
  theirs"; every credit of the repository README; "AI-transcribed", "AI-translated", "AI-produced corrections", never
  "AI-assisted"; the English "translated by GPT-6.1 Sol (OpenAI, effort max)"; the build credited to GPT-6 Astra; and
  the rights statement above (in French in the French readers). The English title pages read "Edition by M. Künzer,
  J. Malgoire et G. Maltsiniotis", with the French "et".
- **Plain reading texts**, three places, French and English, against the diplomatic text:
  Chapter XVIII note 58 keeps Grothendieck's two marginal annotations as quoted and drops the editors' framing and
  their bracketed words; the Chapter VI diagram of manuscript p. 197–198 keeps Grothendieck's triangle and drops the
  editors' alternative triangle and "[plutôt S′]"; in Chapter XVIII the editors' footnote 18 (p. 16–20) and their
  footnote 104 (p. 91–95, "the numbers 4.10.1 to 4.10.4 are used twice") are gone and the author's footnotes after them keep their numbers (19 and 105). In
  each place nothing of Grothendieck's text is missing.

## Status

This is the build as it came back; the readers have not been reviewed beyond the checks above. The appendix entries
are AI-produced proofs and readings, unchecked except where an entry says otherwise; no priority is claimed. The
appendix reports four entries whose cited material was not in the build's input: entry 3 (the cardinal bound in the
Kan–Thurston input, which is proved in the GALOIS return, `raw/pro_returns/4_GALOIS/GALOIS/sections/B_KT.tex`, B.11,
and verified in the PATHS return, `raw/pro_returns/6_PATHS/sections/D_kt.tex`, D.K3), entry 6 (the census programs and
their outputs, in `raw/reviews_max_20261112/1_CATHOT/code/`), entry 9 (a working note on the trefoil argument) and
entry 12 (`raw/reviews_max_20261112/1_CATHOT/EMAIL_CLAIMS_CHECK.md`). The released books, `transcription/`, `companion/`
and `en/` are unchanged by this folder.

## Rights

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in
the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under
CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you
hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.
