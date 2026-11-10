# Pages commented in two parts of the companion

The companion comments the text in parts (I-a, I-b, II-a, ...). Eight pairs of consecutive parts both contain the same
five printed pages of the Künzer–Malgoire–Maltsiniotis edition: these pages end the earlier part and open the later
one. The overlaps start and end inside manuscript pages, so they are given here by printed page and by manuscript page.

| Pair | Edition pages | Manuscript pages | Text kept | Not set in the book |
|---|---|---|---|---|
| I-a / I-b | 34–38 | 59 (end)–66 (beginning) | I-a | I-b, pp. 34–38 |
| VI-a / VI-b | 39–43 | 63 (end)–70 (beginning) | VI-a | VI-b, pp. 39–43 |
| VI-b / VI-c | 84–88 | 137 (end)–145 (beginning) | VI-b | VI-c, pp. 84–88 |
| VII-a / VII-b | 34–38 | 49′ (end)–57 (beginning) | VII-a | VII-b, pp. 34–38 |
| VII-b / VII-c | 69–73 | 108–117 (beginning) | VII-b | VII-c, pp. 69–73 |
| XIIb-a / XIIb-b | 78–82 | 114 (end)–122 (beginning) | XIIb-a | XIIb-b, pp. 78–82 |
| XIIc-a / XIIc-b | 145–149 | 228–234 (beginning) | XIIc-a | XIIc-b, pp. 145–149 |
| XIII-a / XIII-b | 29–33 | 50 (end)–60 (beginning) | XIII-a | XIII-b, pp. 29–33 |

Each overlap also contains the end of the preceding manuscript page (VII-a/VII-b: ms. 50′, written `50$'$` in VII-a;
XIIc-a/XIIc-b: only the end of footnote 124 of ms. 227).

**In the integrated book.** `kit/build_global_reader.py` has a setting `SKIP_PAGES` (printed pages per part). For the
later part of each pair it does not set the text from the line that opens the first overlapping page to the line that
opens the next five-page file (so the `\setcounter{footnote}` lines of that file are kept). It checks that the cut
meets no commentary block and leaves environments and braces balanced, and reports each cut. The files of each part
(`companion/checks/DER_<id>/`) still contain the whole part.

**Which text is kept.** The two texts of an overlap differ only where one of them corrects a reading (XIIc-a/XIIc-b also in
the layout of the diagrams; see below). In each pair the
earlier part's text is kept: it carries most of the commentary on these pages (blocks set in the overlap: I-a 6 / I-b 0;
VI-a 5 / VI-b 1; VI-b 4 / VI-c 2; VII-a 4 / VII-b 0; VII-b 11 / VII-c 4; XIIb-a 5 / XIIb-b 6; XIIc-a 6 / XIIc-b 5;
XIII-a 10 / XIII-b 7) and it ends on these pages, so one cut per pair suffices. Where the later part had the right reading, the kept text was corrected (below).

**What is carried over.** For each pair: the commentary blocks of the later part set inside the omitted pages are
copied into the kept part's `_blocks.tex` (the later part keeps its own copy), with any bibliography entry they cite
that the kept part lacks; claim rows of the later part whose assertion stands on the overlapping pages are moved to the
kept part's `_claims.csv` with their ids; correction rows of the later part on those pages are merged into the kept
part's row for the same reading (its evidence appended in brackets) or moved there with the leaf renumbered. Rows on
the edge page whose assertion lies after the overlap stay where they were (VI-b/VI-c: VI-c row on ms. 145, printed
p. 89; VII-a/VII-b: VIIb-A023, VIIb-A024 and the correction on ms. 57 zero-length propagation, printed p. 39;
VII-b/VII-c: VIIc-A028, VIIc-A029, printed p. 74; XIIb: XIIbb-A023, printed p. 83, and the preamble-wide correction of
`\intdiag`; XIIc: XIIcb-A024 and XIIcb-A025, Proposition 17, printed p. 150, and the two corrections of the TikZ code
of the whole XIIc-b text; XIII: XIIIb-Q047, item c) of the theorem-scholie, printed p. 34, and the correction of the
footnote numbering in the XIII-b preamble). The block of VII-b anchored on the last overlapping page but set after the cut ("Degreewise free is a
precise assertion") remains in the book where it is.

## The eight overlaps

### I-a / I-b — printed pp. 34–38, ms. 59 (end)–66 (beginning). Kept: I-a.

Differences, settled on the page images (I-a leaves 36–38 = printed pp. 34–36, I-b leaves 1–2 = pp. 37–38):
display (1) on ms. 61 has the tilde arrow `\isolongto` (I-a right; I-b had changed it to `\longrightarrow`);
Hom is sans-serif throughout and underlined only in Remarque 2 (I-a's `\sHom`/`\uHom` right; I-b had underlined
Hom_A(hot(X), M) in the HOT example). I-b's two wrong changes are undone in the I-b text, and its two correction rows
are not carried (listed below). I-b's `{\raggedright ...\par}` wrapper on ms. 60 is layout only.
Carried: 22 claim rows (I-b-A001–A022), 2 correction rows (the edition bracket on ms. 60; "dérivateur à gauche [plutôt
à droite]" on ms. 64), 5 corrections merged. I-b had no block on these pages; its block on ms. 67, "The conclusion
reached at the overlap", stays in I-b (retitled).

### VI-a / VI-b — printed pp. 39–43, ms. 63 (end)–70 (beginning). Kept: VI-a.

Difference: the bent identity arrow on ms. 69 (printed p. 43, VI-b leaf 5) is solid in the edition; VI-a had it dashed.
Corrected in VI-a. Carried: block "Three theories within the comparison diagram" (ms. 70); 25 claim rows
(VIb-A001–A025: all start on printed p. 43 or earlier, including footnotes 43–45 of the Théorème-Scholie); the arrow
correction; 5 corrections merged into VI-a's rows, whose intended readings were only "see recovered report" and now
state the reading.

### VI-b / VI-c — printed pp. 84–88, ms. 137 (end)–145 (beginning). Kept: VI-b.

The texts differ only in TeX comments. Carried: blocks "The replacement must be taken over the new base" (ms. 139)
and "A pullback can destroy the replacement equivalence" (ms. 142); 12 claim rows (VIc-A001–A012); 4 corrections
merged.

### VII-a / VII-b — printed pp. 34–38, ms. 49′ (end)–57 (beginning). Kept: VII-a.

Differences: "exponentation" (ms. 50′): the edition prints this spelling (VII-a leaf 36); VII-a keeps it with a
correction row, VII-b had the normalized "exponentiation". The page label is printed "[page 50′]" with a prime; VII-a's
`50$'$` renders it, VII-b's `50'` gives an apostrophe. Carried: 22 claim rows (VIIb-A001–A022); 14 corrections merged.
VII-b had no block on these pages.

### VII-b / VII-c — printed pp. 69–73, ms. 108–117 (beginning). Kept: VII-b.

Difference: VII-c set the bracketed note under the diagram on ms. 112 in `\small`; the edition prints it at normal size
(VII-b leaf 39). Carried: blocks "The total category and the telescope" (ms. 108), "What the preorder forgets about a
lift" (ms. 112), "The obstruction withdrawn in the footnote" (ms. 113) and "What the ind-object represents" (ms. 117,
placed before VII-b's own ms. 117 blocks); 27 claim rows (VIIc-A001–A027); 4 corrections merged.

### XIIb-a / XIIb-b — printed pp. 78–82, ms. 114 (end)–122 (beginning). Kept: XIIb-a.

The texts differ only in a TeX comment. Carried: six blocks (ms. 115 ×2, 119, 120 ×2, 121; "Integration as a calculus
of gluing" placed before XIIb-a's ms. 122 block), with `\Hot` written `\mathrm{Hot}` (XIIb-a does not define `\Hot`)
and four bibliography entries; 23 claim rows (XIIbb-A001–A022 and XIIbb-A044); 4 corrections merged.

### XIIc-a / XIIc-b — printed pp. 145–149, ms. 228–234 (beginning). Kept: XIIc-a.

The XIIc-b text sets every diagram of these pages with `ampersand replacement=\&` and other column and row separations
(layout only) and draws two dotted arrows differently. On ms. 229 the arrow p_f bends by 60 degrees instead of 45
(layout). On ms. 230 (printed p. 146) the edition draws the dotted arrow pr_1 from X × I down to X to the right of the
vertical arrows i_X and i_0^X, with its label on its right, as XIIc-b has it; XIIc-a had it as a loop on the left of
the diagram. Corrected in XIIc-a, with a correction row. Carried: blocks "An interval with room at both ends"
(ms. 228), "A cylinder and a circle in finite categories" and "What the appeal to Thomason supplies" (ms. 230), "Weak
equivalences between objects under a fixed base" (ms. 232) and "Comparing the two meanings of homotopy pushout"
(ms. 233), each placed in the file before the XIIc-a block that follows it in the text, with one bibliography entry;
23 claim rows (XIIcb-A001–A023); 5 corrections merged.

### XIII-a / XIII-b — printed pp. 29–33, ms. 50 (end)–60 (beginning). Kept: XIII-a.

The texts are identical. Carried: seven blocks (ms. 51, 53, 54 ×2, 55, 57, 59), placed in reading order (where a
carried block is set at the same place as an XIII-a block, the one with the earlier anchor page comes first); in the
copy of "Why uniform left structures produce right images" the block with the Brown argument is named instead of being
called "the next block", since an XIII-a block stands between them. Three bibliography entries; 46 claim rows
(XIIIb-Q001–Q046); 8 corrections merged.

## Carried material, item by item

### I-b -> I-a

- Claim rows moved from `DER_I-b_claims.csv` to `DER_I-a_claims.csv` (22, ids kept): I-b-A001 (ms. 60, sketched), I-b-A002 (ms. 60, proved), I-b-A003 (ms. 61, stated), I-b-A004 (ms. 61, stated), I-b-A005 (ms. 61–62, proved), I-b-A006 (ms. 62, proved), I-b-A007 (ms. 62, stated), I-b-A008 (ms. 62, stated), I-b-A009 (ms. 62, stated), I-b-A010 (ms. 62, proved), I-b-A011 (ms. 62, proved), I-b-A012 (ms. 62–63, stated), I-b-A013 (ms. 63–64, proved), I-b-A014 (ms. 63, stated), I-b-A015 (ms. 63, stated), I-b-A016 (ms. 63–64, stated), I-b-A017 (ms. 64, sketched), I-b-A018 (ms. 64, stated), I-b-A019 (ms. 65, stated), I-b-A020 (ms. 65, sketched), I-b-A021 (ms. 65, stated), I-b-A022 (ms. 66–67, proved).
- Correction row 4 of `DER_I-b_corrections.csv` (printed36; ms62; Proposition2: parmis -> Keep parmis; standard spelling parmi, edition_slip_kept) merged into row 34 of `DER_I-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 6 of `DER_I-b_corrections.csv` (printed37; ms63; Proposition2 last words: à gauche). -> à gauche). in upright roman; no change, doubt_resolved) merged into row 37 of `DER_I-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 8 of `DER_I-b_corrections.csv` (printed37; ms64; Proposition2prime(c): y\backslash Y est D-contractile -> Keep printed y\backslash Y; mathematically read y\backslash X, edition_slip_kept) merged into row 38 of `DER_I-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 9 of `DER_I-b_corrections.csv` (printed38; ms65; Definition3: s'appelerait -> Keep s'appelerait; standard spelling s'appellerait, edition_slip_kept) merged into row 39 of `DER_I-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 10 of `DER_I-b_corrections.csv` (printed38; ms66; Proposition4: coefficients constant -> Keep coefficients constant; grammatical form constants, edition_slip_kept) merged into row 40 of `DER_I-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 2 of `DER_I-b_corrections.csv` moved to `DER_I-a_corrections.csv` (printed34; ms60; product-square lifting category: (i_0,uprime_0)\backslash(I/iprime_0) × (j_0,vprime_0)\backslash(J/jprime_0) -> Keep original with the edition bracket: (i_0,uprime_0)\backslash(I/iprime_0) × (jprime_0\backslash J)/(j_0,vprime_0), edition_slip_kept); pdf_page official:36 renumbered 36 in the kept part's leaf numbering.
- Correction row 7 of `DER_I-b_corrections.csv` moved to `DER_I-a_corrections.csv` (printed37; ms64; Proposition2prime opening: dérivateur à gauche [plutôt à droite] -> Keep both original and editorial correction; intended right derivator, edition_slip_kept); pdf_page 1 renumbered 39 (supplement) in the kept part's leaf numbering.

### VI-b -> VI-a

- Claim rows moved from `DER_VI-b_claims.csv` to `DER_VI-a_claims.csv` (25, ids kept): VIb-A001 (ms. 64, proved), VIb-A002 (ms. 64, proved), VIb-A003 (ms. 64, stated), VIb-A004 (ms. 65, stated), VIb-A005 (ms. 65, stated), VIb-A006 (ms. 65, false), VIb-A007 (ms. 66, proved), VIb-A008 (ms. 66, proved), VIb-A009 (ms. 66, proved), VIb-A010 (ms. 67, stated), VIb-A011 (ms. 67, stated), VIb-A012 (ms. 68, proved), VIb-A013 (ms. 68, proved), VIb-A014 (ms. 68, proved), VIb-A015 (ms. 68, stated), VIb-A016 (ms. 69, proved), VIb-A017 (ms. 69, proved), VIb-A018 (ms. 70, assumed), VIb-A019 (ms. 70, proved), VIb-A020 (ms. 70, proved), VIb-A021 (ms. 70, stated), VIb-A022 (ms. 70, stated), VIb-A023 (ms. 70, proved), VIb-A024 (ms. 70, proved), VIb-A025 (ms. 70, proved).
- Correction row 2 of `DER_VI-b_corrections.csv` (ms66, paragraph beginning J'avais songé: evident -> Intended French: évident., edition_slip_kept) merged into row 34 of `DER_VI-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 3 of `DER_VI-b_corrections.csv` (ms68, last paragraph of printed41: $A\Sigma^{-1}$ -> Intended consistent notation: $\mathcal A\Sigma^{-1}$., edition_slip_kept) merged into row 35 of `DER_VI-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_VI-b_corrections.csv` (ms68, before Lemme: En d'autre termes -> Intended French: En d'autres termes., edition_slip_kept) merged into row 36 of `DER_VI-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_VI-b_corrections.csv` (ms69, last line of printed42: $C_{i(X)}$ -> Intended arrow: $C(i_X)$., edition_slip_kept) merged into row 37 of `DER_VI-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 6 of `DER_VI-b_corrections.csv` (ms69, paragraph immediately before ms70: foncteur C -> Intended typographic consistency: foncteur $C$., edition_slip_kept) merged into row 38 of `DER_VI-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 79 of `DER_VI-b_corrections.csv` moved to `DER_VI-a_corrections.csv` (ms69; curved identity arrow in the common-retraction diagram (printed p. 43): \arrow[rr, bend right=15, dashed, "\id"'] -> \arrow[rr, bend right=15, "\id"'], transcription); pdf_page 5 renumbered 45 in the kept part's leaf numbering.
- Commentary block copied into `DER_VI-a_blocks.tex`: "Three theories within the comparison diagram" (anchor `p70:J'ai envie de grouper ce qui a été prouvé`).

### VI-c -> VI-b

- Claim rows moved from `DER_VI-c_claims.csv` to `DER_VI-b_claims.csv` (12, ids kept): VIc-A001 (ms. 138, proved), VIc-A002 (ms. 138-139, proved), VIc-A003 (ms. 139, proved), VIc-A004 (ms. 140, proved), VIc-A005 (ms. 140, proved), VIc-A006 (ms. 141, proved), VIc-A007 (ms. 142, false), VIc-A008 (ms. 142, false), VIc-A009 (ms. 143, proved), VIc-A010 (ms. 143, proved), VIc-A011 (ms. 144, proved), VIc-A012 (ms. 144-146, proved).
- Correction row 2 of `DER_VI-c_corrections.csv` (ms139; original line89; unit square: \Phi_S(X'/S') -> \Phi_S(X'/S) [intended; retain printed S-prime], edition_slip_kept) merged into row 75 of `DER_VI-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 3 of `DER_VI-c_corrections.csv` (ms141; line166; diagram(**), curved arrow i_Xprime: \arrow[rr, bend left, dashed, "{i_{X'}}"] -> \arrow[rr, bend left, "{i_{X'}}"], transcription) merged into row 76 of `DER_VI-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_VI-c_corrections.csv` (ms144; line248; curved identity arrow: \arrow[rr, bend left, dashed, "{\id_{X'}}"] -> \arrow[rr, bend left, "{\id_{X'}}"], transcription) merged into row 77 of `DER_VI-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_VI-c_corrections.csv` (ms144; line253; target of i_X times id: \Phi_S(X')\times_S S' -> \Phi_S(X)\times_S S' [intended; retain printed X-prime], edition_slip_kept) merged into row 78 of `DER_VI-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Commentary block copied into `DER_VI-b_blocks.tex`: "The replacement must be taken over the new base" (anchor `p139`).
- Commentary block copied into `DER_VI-b_blocks.tex`: "A pullback can destroy the replacement equivalence" (anchor `p142`).

### VII-b -> VII-a

- Claim rows moved from `DER_VII-b_claims.csv` to `DER_VII-a_claims.csv` (22, ids kept): VIIb-A001 (ms. 50', proved), VIIb-A002 (ms. 50', proved), VIIb-A003 (ms. 50', proved), VIIb-A004 (ms. 50', proved), VIIb-A005 (ms. 50', stated), VIIb-A006 (ms. 50'–51, proved), VIIb-A007 (ms. 51, proved), VIIb-A008 (ms. 51, proved), VIIb-A009 (ms. 52, proved), VIIb-A010 (ms. 52, proved), VIIb-A011 (ms. 53, proved), VIIb-A012 (ms. 53, stated), VIIb-A013 (ms. 53, proved), VIIb-A014 (ms. 53, proved), VIIb-A015 (ms. 54–55, proved), VIIb-A016 (ms. 55, proved), VIIb-A017 (ms. 55, proved), VIIb-A018 (ms. 55, proved), VIIb-A019 (ms. 56, proved), VIIb-A020 (ms. 56, proved), VIIb-A021 (ms. 56–57, sketched), VIIb-A022 (ms. 57, stated).
- Correction row 2 of `DER_VII-b_corrections.csv` (opening before ms50': connus -> connues (agreement with applications), edition_slip_kept) merged into row 62 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 3 of `DER_VII-b_corrections.csv` (ms50', Cartesian-power parenthesis: où dans -> ou dans (conjunction), edition_slip_kept) merged into row 63 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_VII-b_corrections.csv` (ms50', degeneracy generators: corréspondant -> correspondant, edition_slip_kept) merged into row 64 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_VII-b_corrections.csv` (ms51, collapse map versus simplicial degeneracy: dégénérenscence -> dégénérescence, edition_slip_kept) merged into row 65 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 6 of `DER_VII-b_corrections.csv` (ms52, first sentence: q : y→z -> g : y→z (notation used in the surrounding argument), edition_slip_kept) merged into row 66 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 7 of `DER_VII-b_corrections.csv` (ms52, weighting Hom display: \operatorname{Hom}_{Ens}(Tr(y)) -> \operatorname{Hom}_{Ens}(Tr(y),\mathbf N), edition_slip_kept) merged into row 67 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 8 of `DER_VII-b_corrections.csv` (ms52, formula (1), first object: \Delta_{\varepsilon_1} -> \Delta_{\varepsilon_i}, edition_slip_kept) merged into row 68 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 9 of `DER_VII-b_corrections.csv` (ms52, formula (1), second arrow: g_{\varepsilon,\pi_i} -> g_{\varepsilon_i,\pi_i}, edition_slip_kept) merged into row 68 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 10 of `DER_VII-b_corrections.csv` (ms53, unique product display: f_{\varepsilon_n,l_n\pi_n} -> f_{\varepsilon_n,l_n,\pi_n}, edition_slip_kept) merged into row 69 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 11 of `DER_VII-b_corrections.csv` (ms54, g_i display: g_{\varepsilon_i,l_i} -> g_{\varepsilon_i,\pi_i}, edition_slip_kept) merged into row 70 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 12 of `DER_VII-b_corrections.csv` (ms55, first paragraph: détérminés -> déterminés, edition_slip_kept) merged into row 71 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 13 of `DER_VII-b_corrections.csv` (ms55, identity-at-source paragraph: Le f=id -> Le cas f=id, edition_slip_kept) merged into row 72 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 14 of `DER_VII-b_corrections.csv` (ms56, long(pi_{i-1}) underbrace: \sum_{j\in[1,l_i]}\pi_i(j) -> \sum_{j\in[1,l_{i-1}]}\pi_{i-1}(j), edition_slip_kept) merged into row 73 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 15 of `DER_VII-b_corrections.csv` (ms57, boxed range in (**): i\in[0,r-1] -> i\in[1,r-1]; pi_0 is governed by its separate first condition, edition_slip_kept) merged into row 84 of `DER_VII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.

### VII-c -> VII-b

- Claim rows moved from `DER_VII-c_claims.csv` to `DER_VII-b_claims.csv` (27, ids kept): VIIc-A001 (ms. 108, stated), VIIc-A002 (ms. 108, stated), VIIc-A003 (ms. 108–109, open), VIIc-A004 (ms. 109, stated), VIIc-A005 (ms. 109, proved), VIIc-A006 (ms. 109, open), VIIc-A007 (ms. 109, proved), VIIc-A008 (ms. 110, stated), VIIc-A009 (ms. 110–111, stated), VIIc-A010 (ms. 111, stated), VIIc-A011 (ms. 111–112, stated), VIIc-A012 (ms. 112, stated), VIIc-A013 (ms. 112, stated), VIIc-A014 (ms. 112, stated), VIIc-A015 (ms. 112–113, conjectured), VIIc-A016 (ms. 113, false), VIIc-A017 (ms. 113, stated), VIIc-A018 (ms. 114, stated), VIIc-A019 (ms. 114, stated), VIIc-A020 (ms. 114, false), VIIc-A021 (ms. 115, stated), VIIc-A022 (ms. 115, stated), VIIc-A023 (ms. 115–116, stated), VIIc-A024 (ms. 116, stated), VIIc-A025 (ms. 116, stated), VIIc-A026 (ms. 116–117, stated), VIIc-A027 (ms. 117, stated).
- Correction row 2 of `DER_VII-c_corrections.csv` (ms112: failed comparison: ont échoués -> ont échoué, edition_slip_kept) merged into row 70 of `DER_VII-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 3 of `DER_VII-c_corrections.csv` (ms113: footnote24: C'est un erreur -> C'est une erreur, edition_slip_kept) merged into row 71 of `DER_VII-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_VII-c_corrections.csv` (ms116: localization paragraph: celle déduit -> celle déduite, edition_slip_kept) merged into row 73 of `DER_VII-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_VII-c_corrections.csv` (ms117: displayed localization formula: H_T(a,b) \simeq \mathrm{Hom}_{X(Y)\Sigma_Y^{-1}}(a_Y,b_Y) -> H_T^Y(a,b) \simeq \mathrm{Hom}_{X(Y)\Sigma_Y^{-1}}(a_Y,b_Y), edition_slip_kept) merged into row 74 of `DER_VII-b_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Commentary block copied into `DER_VII-b_blocks.tex`: "The total category and the telescope" (anchor `p108:sur laquelle on peut se poser la question`).
- Commentary block copied into `DER_VII-b_blocks.tex`: "What the preorder forgets about a lift" (anchor `p112`).
- Commentary block copied into `DER_VII-b_blocks.tex`: "The obstruction withdrawn in the footnote" (anchor `p113:Je vais résumer les faits positifs`).
- Commentary block copied into `DER_VII-b_blocks.tex`: "What the ind-object represents" (anchor `p117:associant à tout $a \in X$`).

### XIIb-b -> XIIb-a

- Claim rows moved from `DER_XIIb-b_claims.csv` to `DER_XIIb-a_claims.csv` (23, ids kept): XIIbb-A001 (ms. 114 (continued before 115), open), XIIbb-A002 (ms. 114 (continued before 115), sketched), XIIbb-A003 (ms. 115, proved), XIIbb-A004 (ms. 115;120, proved), XIIbb-A005 (ms. 115, stated), XIIbb-A006 (ms. 115–116, assumed), XIIbb-A007 (ms. 116–117, proved), XIIbb-A008 (ms. 116;118, footnotes 81–82, stated), XIIbb-A009 (ms. 116, stated), XIIbb-A010 (ms. 116, stated), XIIbb-A011 (ms. 116, proved), XIIbb-A012 (ms. 116–117, proved), XIIbb-A013 (ms. 117, stated), XIIbb-A014 (ms. 117, stated), XIIbb-A015 (ms. 117–118, proved), XIIbb-A016 (ms. 118, proved), XIIbb-A017 (ms. 118–119, proved), XIIbb-A018 (ms. 119, sketched), XIIbb-A019 (ms. 120, proved), XIIbb-A020 (ms. 120, proved), XIIbb-A044 (ms. 120 (commentary), proved), XIIbb-A021 (ms. 121, stated), XIIbb-A022 (ms. 121–122, stated).
- Correction row 2 of `DER_XIIb-b_corrections.csv` (ms115, fibre inclusion in first paragraph: W-asphérique [plutôt W-coasphérique] -> Keep the printed phrase and editorial correction; intended classification is W-coaspherical., edition_slip_kept) merged into row 45 of `DER_XIIb-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_XIIb-b_corrections.csv` (ms119, curved natural-transformation arrow λ_α in triangle: \arrow[from=A, to=B, bend left, dashed, "\lambda_\alpha"] % ?? -> \arrow[from=A, to=B, bend left, "\lambda_\alpha"], doubt_resolved) merged into row 48 of `DER_XIIb-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_XIIb-b_corrections.csv` (ms120, deduction of Proposition11: p_{i_0\,!}(X_{i_0}) -> Intended: p_{i_0\,!}(e_{X_{i_0}}); keep p_{i_0\,!}(X_{i_0}) in the source transcription., edition_slip_kept) merged into row 50 of `DER_XIIb-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 6 of `DER_XIIb-b_corrections.csv` (ms121, phrase introducing the integral notation: signe d'integration -> Intended: signe d'intégration; keep the source spelling., edition_slip_kept) merged into row 51 of `DER_XIIb-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Commentary block copied into `DER_XIIb-a_blocks.tex`: "Why the interval test exceeds Dwyer maps" (anchor `p115:Complément : critère d'asphéricité totale`).
- Reference copied into `DER_XIIb-a_references.bib`: `Grothendieck1990XII`.
- Commentary block copied into `DER_XIIb-a_blocks.tex`: "Components of a proper family" (anchor `p115:La démonstration sera donnée plus bas`).
- Commentary block copied into `DER_XIIb-a_blocks.tex`: "The comparison map requested in footnote 83" (anchor `p119:plus de doute c'est lui!`).
- Commentary block copied into `DER_XIIb-a_blocks.tex`: "Total asphericity depends on more than homotopy type" (anchor `p120:ayant un objet final est aussi totalement`).
- Reference copied into `DER_XIIb-a_references.bib`: `Cegarra2020`.
- Commentary block copied into `DER_XIIb-a_blocks.tex`: "A span is remembered by its transition arrows" (anchor `p120`).
- Reference copied into `DER_XIIb-a_references.bib`: `Grothendieck1983`.
- Reference copied into `DER_XIIb-a_references.bib`: `Grothendieck1991Letter`.
- Commentary block copied into `DER_XIIb-a_blocks.tex`: "Integration as a calculus of gluing" (anchor `p121`).

### XIIc-b -> XIIc-a

- Text of `DER_XIIc-a_text.tex` corrected on ms. 230 (printed p. 146): `\arrow[dd, dotted, out=180, in=180, looseness=4, "\mathrm{pr}_1"']` -> `\arrow[dd, dotted, bend left=45, "\mathrm{pr}_1"{pos=.60}]`.
- Correction row added to `DER_XIIc-a_corrections.csv` (pdf_page 32; ms230; dotted arrow pr_1 in the expanded mapping-cylinder diagram (printed p. 146); transcription).
- Claim rows moved from `DER_XIIc-b_claims.csv` to `DER_XIIc-a_claims.csv` (23, ids kept): XIIcb-A001 (ms. 228, open), XIIcb-A002 (ms. 228, stated), XIIcb-A003 (ms. 228, stated), XIIcb-A004 (ms. 228, stated), XIIcb-A005 (ms. 228, stated), XIIcb-A006 (ms. 228 (continued footnote), stated), XIIcb-A007 (ms. 228 (continued footnote), stated), XIIcb-A008 (ms. 228 (continued footnote), stated), XIIcb-A009 (ms. 229, stated), XIIcb-A010 (ms. 229, stated), XIIcb-A011 (ms. 229–230, proved), XIIcb-A012 (ms. 230, stated), XIIcb-A013 (ms. 230, proved), XIIcb-A014 (ms. 230, stated), XIIcb-A015 (ms. 231–232, proved), XIIcb-A016 (ms. 231–232, proved), XIIcb-A017 (ms. 231 footnote 125; 232 NB, proved), XIIcb-A018 (ms. 232, proved), XIIcb-A019 (ms. 232–233, open), XIIcb-A020 (ms. 233, proved), XIIcb-A021 (ms. 233–234, proved), XIIcb-A022 (ms. 234, stated), XIIcb-A023 (ms. 234, proved).
- Correction row 2 of `DER_XIIc-b_corrections.csv` (ms.229, first paragraph: factoriastion -> Intended: factorisation., edition_slip_kept) merged into row 43 of `DER_XIIc-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 3 of `DER_XIIc-b_corrections.csv` (ms.230, sentence following the formula for i_f: comme composé de $Y \longrightarrow Y \amalg X$ -> Intended: comme composé de $X \longrightarrow Y \amalg X$., edition_slip_kept) merged into row 44 of `DER_XIIc-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_XIIc-b_corrections.csv` (ms.232, end of Proposition 16 proof: $Y'_0 \longrightarrow Y$ -> Intended: $Y'_0 \longrightarrow Y'$., edition_slip_kept) merged into row 45 of `DER_XIIc-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_XIIc-b_corrections.csv` (ms.232, question about a pushout: $S' \longrightarrow S$ -> Intended: $S \longrightarrow S'$., edition_slip_kept) merged into row 46 of `DER_XIIc-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 6 of `DER_XIIc-b_corrections.csv` (ms.234, first paragraph after the two-square diagram: immersions ouverts -> Intended: immersions ouvertes., edition_slip_kept) merged into row 47 of `DER_XIIc-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Reference copied into `DER_XIIc-a_references.bib`: `Grothendieck1990XIIa`.
- Commentary block copied into `DER_XIIc-a_blocks.tex`: "An interval with room at both ends" (anchor `p228:assurent que ça existe, avec`), placed before "Conservative gluing is an additional hypothesis".
- Commentary block copied into `DER_XIIc-a_blocks.tex`: "A cylinder and a circle in finite categories" (anchor `p230:donc aussi la rétraction`), placed before "The mapping cylinder, with the two endpoints distinguished".
- Commentary block copied into `DER_XIIc-a_blocks.tex`: "What the appeal to Thomason supplies" (anchor `p230:donc aussi la rétraction`), placed before "The mapping cylinder, with the two endpoints distinguished".
- Commentary block copied into `DER_XIIc-a_blocks.tex`: "Weak equivalences between objects under a fixed base" (anchor `p232:Ici, c'est un argument formel, valable`), placed before "Why Proposition 16 is a formal gluing lemma".
- Commentary block copied into `DER_XIIc-a_blocks.tex`: "Comparing the two meanings of homotopy pushout" (anchor `p233:Il faut donc vérifier :`), placed before "Completing the pasting step".

### XIII-b -> XIII-a

- Claim rows moved from `DER_XIII-b_claims.csv` to `DER_XIII-a_claims.csv` (46, ids kept): XIIIb-Q001 (ms. 50, stated), XIIIb-Q002 (ms. 50, stated), XIIIb-Q003 (ms. 50–51, stated), XIIIb-Q004 (ms. 50–51, stated), XIIIb-Q005 (ms. 51, stated), XIIIb-Q006 (ms. 51, assumed), XIIIb-Q007 (ms. 51, stated), XIIIb-Q008 (ms. 51, stated), XIIIb-Q009 (ms. 51–52, stated), XIIIb-Q010 (ms. 52, stated), XIIIb-Q011 (ms. 52, stated), XIIIb-Q012 (ms. 52, stated), XIIIb-Q013 (ms. 52, open), XIIIb-Q014 (ms. 53, stated), XIIIb-Q015 (ms. 53, false), XIIIb-Q016 (ms. 53, stated), XIIIb-Q017 (ms. 53, stated), XIIIb-Q018 (ms. 53, stated), XIIIb-Q019 (ms. 53–54, open), XIIIb-Q020 (ms. 53–54, conjectured), XIIIb-Q021 (ms. 54, open), XIIIb-Q022 (ms. 54, stated), XIIIb-Q023 (ms. 54–55, stated), XIIIb-Q024 (ms. 54 footnote32, open), XIIIb-Q025 (ms. 55, stated), XIIIb-Q026 (ms. 55, open), XIIIb-Q027 (ms. 55, stated), XIIIb-Q028 (ms. 55, sketched), XIIIb-Q029 (ms. 55, stated), XIIIb-Q030 (ms. 55–56, conjectured), XIIIb-Q031 (ms. 56, stated), XIIIb-Q032 (ms. 56, open), XIIIb-Q033 (ms. 56, stated), XIIIb-Q034 (ms. 57, stated), XIIIb-Q035 (ms. 57, stated), XIIIb-Q036 (ms. 57–58, stated), XIIIb-Q037 (ms. 58, stated), XIIIb-Q038 (ms. 58, stated), XIIIb-Q039 (ms. 59, assumed), XIIIb-Q040 (ms. 59, stated), XIIIb-Q041 (ms. 59, stated), XIIIb-Q042 (ms. 59, sketched), XIIIb-Q043 (ms. 59, stated), XIIIb-Q044 (ms. 60–65, proved), XIIIb-Q045 (ms. 60,65–66, proved), XIIIb-Q046 (ms. 60, stated).
- Correction row 3 of `DER_XIII-b_corrections.csv` (ms. 51, after Definition 2 [sic line 61]: eventuellement -> éventuellement, edition_slip_kept) merged into row 29 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 4 of `DER_XIII-b_corrections.csv` (ms. 51, Example 2 [sic line 65]: K^{\bullet}(A) -> K^{\bullet}(\mathcal A), edition_slip_kept) merged into row 28 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 5 of `DER_XIII-b_corrections.csv` (ms. 52, definition of nonnegative/nonpositive complexes: K^i=0 si i\geq0, resp. si i\leq0 -> K^i=0 si i<0, resp. si i>0, edition_slip_kept) merged into row 30 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 6 of `DER_XIII-b_corrections.csv` (ms. 53, first paragraph [sic line 80]: elle même -> elle-même, edition_slip_kept) merged into row 31 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 7 of `DER_XIII-b_corrections.csv` (ms. 55, first sentence [sic line 97]: des ces structures -> de ces structures, edition_slip_kept) merged into row 32 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 8 of `DER_XIII-b_corrections.csv` (ms. 56, paragraph before Section 6 [sic line 113]: u_{\star} -> u_* (same right direct-image functor; notation normalized only in commentary), edition_slip_kept) merged into row 33 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 9 of `DER_XIII-b_corrections.csv` (ms. 59, Theorem-scholie 1), parenthetical on finite shapes: \mathcal M étant supposée stable par \varinjlim finies -> \mathcal M étant supposée stable par \varprojlim finies, edition_slip_kept) merged into row 35 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Correction row 10 of `DER_XIII-b_corrections.csv` (ms. 60, Theorem-scholie 1)b) [sic line 155]: suite croissante de fermées -> suite croissante de fermés, edition_slip_kept) merged into row 36 of `DER_XIII-a_corrections.csv`, the same reading; its evidence is appended there in brackets.
- Commentary block copied into `DER_XIII-a_blocks.tex`: "Quillenisability and the strength of its qualifiers" (anchor `p51:En pratique, j'utiliserai cette définition`), placed before "Two meanings of a bounded diagram of complexes".
- Commentary block copied into `DER_XIII-a_blocks.tex`: "A bound on each component is not a bound on the diagram" (anchor `p53`), placed before "Unbounded resolutions remove the dimensional restriction".
- Reference copied into `DER_XIII-a_references.bib`: `Joyal1984Letter`.
- Commentary block copied into `DER_XIII-a_blocks.tex`: "An answer already present in Joyal's letter" (anchor `p54`), placed before "The two elementary derivator axioms".
- Reference copied into `DER_XIII-a_references.bib`: `Serpe2003`.
- Reference copied into `DER_XIII-a_references.bib`: `StacksKInjective079P`.
- Commentary block copied into `DER_XIII-a_blocks.tex`: "Unbounded resolutions answer the derived-image question" (anchor `p54`), placed before "The two elementary derivator axioms".
- Commentary block copied into `DER_XIII-a_blocks.tex`: "Localization axioms, stability, and locally constant coefficients" (anchor `p55`), placed before "Locally constant diagrams depend on the homotopy type".
- In the copy of "Why uniform left structures produce right images": "the general Brown argument given in the next block." -> "the general Brown argument given below, in the block ``The Brown argument makes admissibility automatic''.".
- Commentary block copied into `DER_XIII-a_blocks.tex`: "Why uniform left structures produce right images" (anchor `p57`), placed before "Closure and exactness already imply both trivial-class equalities".
- Commentary block copied into `DER_XIII-a_blocks.tex`: "The Brown argument makes admissibility automatic" (anchor `p59`), placed before "Every available right Kan extension is admissible".

### I-b: rejected


### Corrections not carried because the page image refutes them

- `DER_I-b_corrections.csv` row 3 (printed35; ms61; display(1): \Hom(q^*M, q^*N) \isolongto \Hom(p^*M, p^*N) -> \Hom(q^*M, q^*N) \longrightarrow \Hom(p^*M, p^*N), transcription). The edition (I-a PDF leaf 37, printed p. 35) prints the arrow of display (1) with a tilde: \isolongto is the right reading; the change to \longrightarrow is undone in the I-b text. The row is removed from DER_I-b_corrections.csv.
- `DER_I-b_corrections.csv` row 5 (printed36; ms62; HOT cohomology display: \Hom_{\cA}(\hot(X), M) -> \underline{\Hom}_{\cA}(\hot(X), M), transcription). The edition (I-a PDF leaf 38, printed p. 36) prints Hom_A(hot(X), M) without underline; the change to \underline{\Hom} is undone in the I-b text. The row is removed from DER_I-b_corrections.csv.
