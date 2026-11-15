# Intake of the return PATHS (package 6, Les Dérivateurs)

Reviewer: Claude Fable 5.2 (Anthropic), effort high, no sub-agents, 12 November 2026. Return: GPT-6 Astra (OpenAI,
ChatGPT Pro mode), 11 November 2026; 76 statements (40 Proved, 19 Refuted, 11 Known, 6 Open by its own labels).
Replaces the review of 11 November (void; not read, nor anything in `pro_reviews_20261110/6_PATHS/`). The agent could
not write its files (harness guard); the main session saved the texts. Findings are numbered in FINDINGS.md.

## What was read

- The prompt `pro_prompts_20261110/6_PATHS/PROMPT.md`, in full.
- The return, unpacked to `work/PATHS_unzipped/PATHS/`: all of `sections/*.tex` (A_definitions, A_colimits, B,
  C_paths, C, D, D_kt, E, F_audit), `PATHS_results.csv`, `code/README.md`, the program outputs; of `research/` and
  `PATHS_report.md` only the parts on Part B and the literature searches.
- `KNOWLEDGE_HANDOFF.md`: the sections on STRATA and PATHS (the latter summarizes the void review; nothing was taken
  from it).
- PRETOT: `FINDINGS.md` of its review (F16, F17) and the paper, §"The shapes actually used in VII" (F.12–F.16) and
  the diagram theorem (F.1–F.6).
- INDLOCAL `PROMPT.md`, lines 1–140.
- Grothendieck (transcription in the PATHS background zip): VII ms. 99–103, 108–115; IX ms. 21–24. Companion: the
  claim rows IX-037, 080, 081, 088 and the location of the block at IX ms. 23.
- Arakawa–Cnossen, arXiv:2608.19870 (supplied LaTeX): introduction, §4 statements and proofs of 4.7, 4.8, 4.16.

## Programs

Rerun of the return's programs (`work/rerun/`, `python -I`): all outputs identical to the delivered ones (F7).
Own programs (`work/scratch/`, with `.out` files): `posethom.py` (poset homology), `test_cp1.py` (C.P1),
`test_s2.py` (the F.16 instance), `test_chain3.py`, `test_more.py`, `test_s2cyl.py` (F2), `test_misc.py` (D.5, A.6).

## 1. A.P2, C.P1–C.P4 against PRETOT F.16

They prove what F.16 leaves open; every step was followed and holds. Details in FINDINGS F1. E.26 (1)–(3) and E.27
(blocks with both signs) are proved for every wide `Σ`.

## 2. What INDLOCAL C1–C4 and the companion's VII blocks use

| Use | PATHS statement | Verdict |
|---|---|---|
| INDLOCAL C1: the formula of V ms. 44–45 | D.K5 (two proofs: by words, and by C.P3 applied to `(M^X, Σ_X)`) | correct |
| INDLOCAL C2: invariance forces `Π_1` | D.K1–D.K4 (= GALOIS B.9–B.12) | correct |
| INDLOCAL C3: `C_∞ → Ch_Σ` | A.P2, C.P1–C.P3 | correct |
| INDLOCAL C3: "Thomason–Kan" at V ms. 46, VII ms. 129–132, IX ms. 22–23 | D.1, D.5, D.K4, D.K5 | correct |
| INDLOCAL C4: E.26, E.27, all `Σ` | C.P3, C.P4 | correct; E.27 only for blocks with both signs |
| INDLOCAL C4: comparison with the hammock localization | B.2 (known), B.6 (gap), B.8 (open in the return) | settled by FINDINGS F2, F3, unverified by others |
| VII ms. 65–70 (`π_0`) | A.P1 | correct |
| VII ms. 99–110, row VIIb-C026 | A.1–A.4, C.P3 | correct |
| VII ms. 112–115 (composition on `C_∞`) | C.P4, E.2 | correct |
| rows VIIc-A046, V-I066 (`Cat hot`) | C.P5, A.9 | correct |
| rows VIIc-C004, C005 | E.1 (known), E.3, E.4, E.13 | correct |
| VII ms. 161–166 (smoothness) | E.3–E.5, E.9 | correct |

## 3. All statements

Verdicts: C = correct; G = correct with a gap; K = known (citation checked / not opened); O = open as stated.

| ID | Return | Verdict | Note |
|---|---|---|---|
| A.P1 | Proved | C | universal property followed |
| A.P2 | Proved | C | rests on C.P3 |
| A.1 | Proved | C | |
| A.2 | Proved | C | `q_D/z` filtered; Theorem A |
| A.3 | Proved | C | |
| A.4 | Refuted | C | = VII ms. 109 = PRETOT F.14; text read |
| A.5 | Refuted | C | colimit and spectral sequence followed |
| A.6 | Proved | C | polynomial lemma followed; `n = 2` checked by computation |
| A.7 | Proved | C | |
| A.8 | Open | O | closed since by PRETOT F.6 (F4) |
| A.9 | Proved | C | rerun: 456 maps, degree 0 |
| B.1 | Proved | C | |
| B.2 | Known | K, checked | Arakawa–Cnossen source read; Dwyer–Kan 2.1, 5.5 via that source |
| B.3 | Refuted | C | |
| B.4 | Proved | C | the zigzag `1 ⇐ pad ⇐ T ⇒ ie` followed |
| B.5 | Known | K, not opened | the two-out-of-three remark is correct |
| B.6 | Proved | G | cocone and compatibilities described, not constructed; conclusion holds by F2, F3 |
| B.7 | Proved | C | |
| B.8 | Open | O | settled by F2, F3 of this intake (unverified by others) |
| B.9 | Proved | C | rerun identical (132 comparisons) |
| C.P1 | Proved | C | and enumeration (11,369 cases) |
| C.P2 | Proved | C | Dwyer–Kan step verified in model-category form; Kerodon numbers not opened |
| C.P3 | Proved | C | |
| C.P4 | Proved | C | |
| C.P5 | Refuted | C | |
| C.1 | Proved | C | |
| C.2 | Known | K, not opened | |
| C.3 | Proved | C | |
| C.4 | Proved | C | |
| C.5 | Known | K, not opened | Quillen, Dwyer–Kan numbers |
| C.6 | Proved | C | Groth's numbers not opened |
| C.7 | Refuted | C | |
| C.8 | Proved | C | |
| C.9 | Open | O | |
| C.10 | Open | O | the unpointed comparison it waits for is F2 |
| D.1 | Proved | C | IX ms. 21–23 read |
| D.2 | Refuted | C | |
| D.3 | Proved | C | |
| D.4 | Proved | C | |
| D.5 | Refuted | C | own computation: `b_1(X^Y) = 1` |
| D.6 | Proved | C | |
| D.7 | Known | K, not opened | Cisinski 2019, 2010, 2003; Lenz |
| D.8 | Proved | C | CF3 followed; uses D.7 |
| D.9 | Refuted | C | rerun |
| D.10 | Refuted | C | rerun: 234 maps, degrees 3/228/3 |
| D.11 | Proved | C | Meier 4.13 not opened |
| D.12 | Refuted | C | `(N_ξ F)_0 = Ex² NF` taken from Meier, not opened |
| D.13 | Refuted | C | |
| D.14 | Known | K, not opened | Kaledin v3 |
| D.15 | Known | K, not opened | formal consequence of Kaledin 7.3.1.3 (preprint) |
| D.16 | Proved | C | given Kaledin's Definition 7.1.4.6 |
| D.17 | Proved | C | deductions followed; XIII, XVII, XIX pages not re-read |
| D.18 | Known | K, not opened | the Brown argument for the converse followed |
| D.19 | Refuted | C | |
| D.20 | Known | K, not opened | the example (arrows `S⁰ → *`, `* → S¹`) is correct |
| D.21 | Proved | C | given D.15 |
| D.22 | Open | O | six items |
| D.23 | Proved | C | the word `y x y x⁻¹ y⁻¹` and the `S_3` image checked |
| D.K1 | Proved | C | |
| D.K2 | Proved | C | group-theory sources not opened; = GALOIS B.10 |
| D.K3 | Proved | C | = GALOIS B.11 |
| D.K4 | Proved | C | = GALOIS B.12 |
| D.K5 | Proved | C | |
| E.1 | Known | K, not opened | CATHOT E.20–E.25, reviewed elsewhere |
| E.2 | Proved | C | |
| E.3 | Refuted | C | |
| E.4 | Refuted | C | |
| E.5 | Proved | C | Shoikhet's number not opened |
| E.6 | Refuted | C | rerun |
| E.7 | Refuted | C | rerun: Betti (1,0,0,1,0) for `n = 1, 2, 3` |
| E.8 | Proved | C | |
| E.9 | Refuted | C | |
| E.10 | Refuted | C | |
| E.11 | Open | O | BISITE B.21 bears on it (not read here) |
| E.12 | Known | K, not opened | TOTASPH G.1–G.6, reviewed elsewhere |
| E.13 | Refuted | C | the conjugation identity checked |

Counts: 58 correct, 1 correct with a gap, 11 known (1 checked, 10 not opened), 6 open as stated, 0 wrong.

## 4. Not checked

Kerodon; Dwyer–Kan's two papers beyond 2.1 and 5.5; Cisinski 2003, 2006, 2010, 2019; Lenz; Szumiło; Rădulescu-Banu;
Meier; Kaledin; Quillen; Groth; Keller; Dugger–Shipley; Arlin; Fuentes-Keuthan–Kędziorek–Rovelli;
Baumslag–Dyer–Heller; Higman–Neumann–Neumann; Hausmann–Husemoller; Hatcher 2C.5; Fiedorowicz; Shoikhet;
Maltsiniotis; Chachólski–Scherer; Cegarra. The manuscript at XIII ms. 7–10, 50–53, XVII ms. 39–40, XIX ms. 33–48
(D.17). The proofs of CATHOT E.20–E.25 and TOTASPH G.1–G.6 (E.1, E.12). The companion blocks at VII ms. 164–169.
BISITE. No literature search was made for FINDINGS F2.
