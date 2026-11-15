# When is each companion complete?

Claude Fable 5.2 at effort high (the intake agent of TOTAL_EXACT_2 and LM8). 13 Nov 2026, 17:13 UTC (machine clock).
Answer to the main session's consultation. One answer, no sub-agents.

**What this rests on.**
- Read by me, row by row: TOTAL_EXACT_2 (89 rows) and LM8 (167 rows), their two prompts, the two experts'
  handoffs, and today `PROGRAM_WARGAME_ROUND2_20261112.md` (Summary, 1.1, 1.2, 1.7–1.9, section 3).
- Second-hand (handoffs, prompt blocks, the war game): the content of the Dérivateurs returns 2–8 and of LM1–LM7.
- Never opened by me: the text of *Les Dérivateurs*, the text of *La Longue Marche*, any scan, any cited source.
  So the lists below are complete for the threads I read (total asphericity; §§50–53) and are a frame, to be
  filled by the field experts, for the rest. Where I name a chapter I did not read, it is marked (2nd hand).

## 0. The criterion, in one sentence

A companion is a companion to a text. It is complete when **every claim, conjecture, question and marked doubt of
that text has a final status**, and not when the mathematics those claims open has been exhausted.

Final status of one item of the text, exactly one of:
- **proved** (his form or the strongest correct form), proof read by the field expert at effort max;
- **refuted**, with the counterexample checked and the corrected statement proved;
- **known**, with the theorem cited from an opened source and the reduction written;
- **open, closed off**: the exact statement it was reduced to, every approach tried, and the reason we stop
  (stopping rule, section 3).

Plus, for the companion as a whole: the claim register covers every section of the text; every correction to the
text is checked against the scan; every return it quotes has a review at effort max; the bridges he names to
other texts are stated with their status; the PDF check passes.

"What do we really want to know" is therefore: what is true of what he wrote. New questions that the answers raise
are placed (section 2), not pursued inside the companion.

## 1. The questions each companion must answer

### 1A. Les Dérivateurs

| # | Question of the text | State after today | Counts as done when |
|---|---|---|---|
| D1 | II ms. 36–36ter: is a totally `W∞`-aspherical category filtered? Proposition 2.19 (sifted ⇒ total) | **Answered.** False; `filtered ⊊ exact ⊊ total ⊊ quasi-filtered` with `Δ_inj`, `C_δ`, `K*`; the true forms (total + sifted ⇒ filtered; the Eilenberg–MacLane test) | the expert has read TOTAL_EXACT_2 A.21, A.24, A.30–A.34, C.25–C.28 at max; the wording of 2.19 is compared with the edition. No further Pro run |
| D2 | XII ms. 88–89, 107–114 and Théorème 2: the classes W(7), W(7 bis), composition of total sieves | answered in TOTASPH (2nd hand; reviewed, 0 wrong); PRETOT C.4 at `n = 2` now refuted | DER_FOLLOWUP A.2 written out. A.3 (`n ≥ 3`) is a generalization of ours: one run, then section 3 |
| D3 | VII ms. 99–115: the comparison `C_∞ → C` over the types; what follows from the shape `Ty` | `Ty^op` is not total (C.40): nothing follows from the shape. The class of diagrams for which the comparison holds is open (2nd hand: PATHS, INDLOCAL, DER_FOLLOWUP B) | the class is determined, or closed off. This one matters: it is his claim, not ours |
| D4 | XVI: the localizer axioms, relative Theorem A, XVI 6.4 b; I ms. 79–84 and X: the classes `W_D`, the statements he gets wrong | POLES, GALOIS reviewed in part (2nd hand; GALOIS review stopped at 22 of 74 rows) | reviews finished; each false statement has its corrected form |
| D5 | Gluing along a stratification, proper and smooth functors, the six operations on Cat, open tests (chapters met by STRATA, PATHS, BISITE, RESIDUE) | 368 rows, **none reviewed at max** (war game 3.1) | reviewed. This is the largest gap of the companion and it is a reading gap, not a Pro gap |
| D6 | The chapters no return addresses (III–VI, VIII–XI, XIII–XV, XVII–XIX as far as I know: 2nd hand) | no register seen by me | a claim register exists for them, even if most rows are "definition, no claim" |

Bridges it must state (war game 1.2, 1.7): B1 and S3 (gluing is exodromy), S4 (the shapes over which colimits
are homotopy colimits: now settled on the abelian side by D1), B14 (forgetting a point is proper and not smooth:
the Cat side of hole filling in La Longue Marche), S11 with LM8 B.6, B.9 (the localizers of the Lie approximations).

Outside its scope: which Fraïssé classes are exact, amenability and Ramsey properties, `F_p`- against
`Q`-exactness (conference floor questions); strict higher categories beyond what the text states; anything about
the arithmetic of the moduli tower.

### 1B. La Longue Marche

| # | Question of the text | State after today | Counts as done when |
|---|---|---|---|
| L1 | Which group is his `Γ_{g,ν}`; is the group cut out by his loop equations (§§26–29, 46) the Galois group; his "hasty corollary" at (0,4) → (0,3) | pro-ℓ: `GT_0 ⊋ GT` at every prime (LM8 B.12, B.14d); filling is exact on the normalizer with image `GT × S_3` (B.17). Profinite `GT` against `GT_0`: open (2nd hand, LM3b F.4) | the pro-ℓ results are reviewed; the profinite question is closed off by section 3 (it is a named open problem of the field) |
| L2 | §47: does his compatibility with `C_2 * C_3` cut the group down | graded and filtered forms settled (B.26, B.27, B.30); the profinite statement open (B.28) | B.28 proved or refuted, or closed off after one push. This matters: it is the one place where his text may see more than `GT_0` |
| L3 | §50–§51: envelopes, the Fermat tower, the signed data | LM1, LM7 (2nd hand); LM8 B.24, B.31–B.35; B.24d open | LM7_PUSH intake done; B.24d closed off now (technical, his comparison is already refuted over `F_2[ε]`) |
| L4 | §52: L-groups ("∀ L-groupe … obtenu ainsi"), modular multiplicities, the Galois–Teichmüller axioms, quasi-unipotent homomorphisms, the presentations, the limiting topos | **Answered** except two: the profinite realization (A.12) and the reading of scans 242–243 (E.11) | A.12: one push through the involution of A.22, then closed off; scans 242–243 read and the correction worded for the reading he has |
| L5 | §52 "each refinement calls for a new study of splittings" (scans 173, 178) | answered to the depth he asks: thresholds for the tripod and two elliptic curves, the cusp sections separate at class 3, the `lim¹` class at class 2 (F.2–F.24) | F.16–F.18 confirmed by a second route or a second reader. F.12 (all unrestricted section sets) is not his question: closed off now |
| L6 | §53: `ST_{1,1}`, `GL(2,Z)^~`, `SN_{1,1}`, the 140-1 draft extension, germs | **Answered** (E.1–E.13) | scans checked for E.4, E.5 |
| L7 | §§1–49 as covered by LM2–LM6 (2nd hand): multi-Galois topoi, the tower, finite group actions, points as sections | LM4 running; LM5, LM6 not sent | their returns taken in; for "points as sections" the section conjecture is closed off as a named open problem, with what the 2026 results give |

Bridges it must state: to cote 149 (he says so himself, 149 scan 101; war game B13), to 142 (hole filling, B14),
to 147 (germs and the limiting topos, with LM8 E.10–E.11), to *Les Dérivateurs* (B14, S11).

Outside its scope: LM8 Part G (the CM curve): it answers cote 149 and CYCLOTOMIC_KERNEL, not a passage of
La Longue Marche; the degree-8 scalar (G.16); GT-shadows beyond the check he needs (E.14–E.17 are already more than
the text asks); the general theory of the class across the primes.

## 2. What mathematics goes where

| Destination | What goes there | From today's material |
|---|---|---|
| **The companion** | the status of each item of the text, the proof or counterexample, the corrected statement, the tables he asks for | T: A.1–A.3, A.21, A.24, A.30–A.34, C.28, C.40, D.1, D.2, D.4, and the checked Leads as lemmas. L: Parts A–F as answers to items 1–5 of its prompt; B.10–B.19 |
| **Notes of the archive edition** (by cote and scan) | results that answer a passage of an archive text | L Part G → cote 149 (§3 and scans 45, 99–103) and LM §34; L E.10–E.13 → 147 (germs, "pièces de construction"); L F.4, F.15, F.21, F.24 and the 5-descent instance of the conference (order 75) → 149 §3 on sections; L C.6 → wherever he asks about moduli over `Z` |
| **The program document** (the six books and their bridges) | statements that connect two texts | the duality "exact colimits are compact limits" as the bridge between colimits over a shape and limits over a tower; B14 with L B.17; S11 with L B.6, B.9; the Teichmüller tower as an index category (candidate P3); S4 as settled by T |
| **A separate program, placed and not judged** | lines that leave his questions | the Fraïssé line (Ramsey, amenability, Reiter, `F_p` against `Q`, rigid ages): its own note, FRAISSE_EXACT; the shape map (the first-derived class, D+1, the frameworks outside Grothendieck's texts); the Connes–Marcolli–Ramachandran link of L G.18; torsion in `GT` beyond what L1 needs (A.22 against the pentagon) once L4 is closed off |

Rule of placement: an item goes to the companion only if a passage of the text can be cited for it. A.6, A.13,
A.18–A.20 of T are an example of the other case: true, read, and belonging to the Fraïssé note, with one remark in
the companion at II ms. 36ter.

## 3. Stopping rules

**Per item.**
1. An item with a final status is not sent again.
2. An open item is sent in a push prompt with its exact reduction. After a run, it advanced only if a new
   statement toward it is proved (a reduction, a case, an obstruction as a theorem). Longer tables, restatements and
   finite checks beyond the first are not advances.
3. **Two runs without an advance: close it off.** Also close it off at once when the run reduces it to a named open
   problem of the field (profinite `GT = GT_0`, the section conjecture), or to a single number nobody asked for.
4. A question raised by a return and not by the text gets no run from the companion's budget unless its answer
   changes the wording of a corrected claim; otherwise it is placed by section 2.

**Per companion.**
5. Measure a run by the rows of the *claim register of the text* whose status changed, not by its row count.
   LM8: 167 rows, of which the items of the text it settles are about a dozen; that dozen is the yield.
6. **Stop Pro runs for a companion when a push run changes no status in that register.** What then remains is
   reading (reviews at max, scans), which no Pro run does.
7. A companion is complete when the five conditions of section 0 hold. By that test: the total-asphericity thread
   of *Les Dérivateurs* is complete but for one expert reading; *Les Dérivateurs* as a whole waits on the reviews
   of returns 4–8 and a register for the unaddressed chapters, not on mathematics; *La Longue Marche* waits on
   LM4–LM7 intakes, on B.28, A.12 and the scans, and is otherwise answered for §§50–53.

## 4. What I cannot say

Whether the claim registers of the two texts exist in full. I have seen registers of returns, not a register of
his claims by chapter. If it does not exist, building it (from the transcription notes, one pass per chapter) is
the first step, and the only one that makes "complete" checkable.
