# Draft note to the author of arXiv:2610.38760 (not sent; for the user to approve)

Drafted by Claude (Fable 5.2, Anthropic), 11 November 2026, 23:58 UTC. To check before sending: the link (branch name and path), and that v1 is still the only version on arXiv (it was on 11 November 2026).

---

**To:** <e-mail> (Oren Ben-Bassat, Department of Mathematics, University of Haifa; the address printed in arXiv:2610.38760v1)

**Subject:** Conjecture 7.1 of "On a conjecture of Fiedorowicz" (arXiv:2610.38760v1): a counterexample

Dear Professor Ben-Bassat,

I am Claude, an AI model made by Anthropic, writing for an open-mathematics project that is producing a checked commentary on Grothendieck's *Les Dérivateurs*. One of our questions there was which homotopy types finite categories and finite monoids realize, and your preprint came up at once: your Theorem C is the positive answer we cite for the simply connected case.

In the same work an argument turned up that bears on your Conjecture 7.1 (every connected finite CW complex with finite fundamental group is `BM` for a finite monoid `M`). As stated in v1 it appears to be false: `RP²` is a counterexample, and more generally a finite monoid whose classifying space has the homotopy type of a finite-dimensional CW complex has trivial universal group. So among connected finite CW complexes the ones realized by finite monoids would be exactly the simply connected ones, which makes your Theorem C the complete answer.

The proof, in a few lines:

1. Let `M` be a finite monoid, `e` an idempotent of its minimal ideal, and `H = eMe`. Then `H` is a finite group, and `H → U(M) = π_1(BM)` is onto, because `η(e) = 1` and `η(eme) = η(m)` for the universal homomorphism `η`, which is onto as in your §7.
2. Your map `j_e: B(eMe) → BM` (through the Karoubi envelope, your Lemma 2.4) induces this surjection on `π_1`: with `r: 1 → e` and `s: e → 1` the two arrows given by `e`, the loop `[s][h][r]` at `1` is the class of `h` in `M`.
3. If `BM ≃ Z` with `Z` a finite-dimensional CW complex, the composite `BH → BM ≃ Z` is trivial on `π_1` by Miller's Theorem B: "Let `X` be a finite dimensional CW complex and `G` a torsion group. Then any pointed map `BG → X` induces the trivial map of fundamental groups" (H. Miller, *The Sullivan conjecture on maps from classifying spaces*, Ann. of Math. 120 (1984), 39–87; Theorem B on p. 40, proved as Theorem 10.1 on pp. 84–85 by covering spaces and K-theory). Being both trivial and onto, it forces `π_1(Z) = 1`.

The same step can be read off Atiyah's completion theorem (Publ. Math. IHES 9 (1961), Theorem (7.2) with Proposition (6.11)): a character of order `p` of a cyclic `p`-group gives a class `χ − 1` in `K⁰` of its classifying space that is not nilpotent, while it would be pulled back from a finite-dimensional complex.

Credit, so that it is clear who did what: the argument was produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode) in answer to a research prompt of the project; I checked it step by step, and read the statements of Miller and Atiyah in the published papers. Nobody here claims priority, and we have not looked exhaustively for the statement in the literature; if it is known, we would be glad of the reference. The full text is public:

https://github.com/KokunoYumeto/grothendieck-derivateurs/tree/main/raw/pro_returns/1_CATHOT

(statements G.4 and G.6 in the paper there, pp. 53–54 of the PDF). The same paper has small finite models that may interest you: a three-object, nine-arrow category of type `RP²`, which shows the obstruction is to having one object, and the smallest finite categories of types `S¹`, `S²`, `S³`; for `S²` and `S³` these are monoids, with five and seven elements.

My check of the argument, against the published papers of Miller and Atiyah, is here:

https://github.com/KokunoYumeto/grothendieck-derivateurs/blob/main/raw/reviews/1_CATHOT/REVIEW_G6.md

If I have misread the conjecture, or if a later version already changes it, I apologize for the noise. If anything further would be useful, the written-out proof or the programs, I will gladly send it.

With best regards,

Claude
(AI model by Anthropic, for the open-mathematics project)
