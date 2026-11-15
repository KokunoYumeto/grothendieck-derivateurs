# FINDINGS: running list (CATHOT review at effort max)

Kept by Claude Fable 5.2 (effort max), 12 Nov 2026, while reviewing the return CATHOT of GPT-6 Astra (effort Pro,
ChatGPT Pro mode). Every potential finding or implication goes here when noticed, small ones included. Status words:
**proved here** (my own proof, written out in the file named), **checked** (a claim of the return or of a source that I
verified, with how), **hunch** (suspected, not proved; reasons in HUNCHES.md), **question** (worth posing).
"Recent" marks results dated after mid-2026 that I could not know from memory.

## A. Finite monoids and finite categories as models (Part G, the e-mail to the author of arXiv:2610.38760v1)

F1. **(checked, with my own proof) A finite monoid whose classifying space has the homotopy type of a
finite-dimensional CW complex has trivial universal group.** Return G.4; e-mail claim (c). Proof written out in
`EMAIL_CLAIMS_CHECK.md` (c) and `G6_VERDICT.md`. The only non-elementary input is the π1-triviality of maps
BG → X (G finite, X finite-dimensional): Miller, Ann. of Math. 120 (1984), Theorem B = Theorem 10.1, or directly
Atiyah's theorem for cyclic groups (Publ. IHES 9 (1961), (8.1), (6.11)). Hence Conjecture 7.1 of arXiv:2610.38760v1
(28 Oct 2026, recent) is false as stated: RP², every lens space, every RPⁿ (n ≥ 2), and in fact every connected
finite-dimensional complex with non-trivial fundamental group is not BM for a finite monoid M.

F2. **(proved here; sharpening, not in the return) Bounded integral homology is enough.** If M is a finite monoid and
H_k(BM; Z) = 0 for all large k, then U(M) = 1. No covering space is needed: the regular representation of the finite
group U(M) gives a flat bundle V on BM; in K⁰(BM) the class [V] − rank lies in skeletal filtration ≥ 1, the
filtration quotients above the top cohomological degree vanish, so a power of it is a phantom class, and its pull-back
to BH (H the group eMe of the minimal ideal) is zero in lim K⁰ of the skeleta; by Atiyah (7.2), (6.10) the character
of the representation is then trivial on every element of prime-power order of H, hence on H, hence on U(M).
Written out in `OWN_RESULTS.md` §1.

F3. **(proved here) Characterization.** For a finite monoid M the following are equivalent: (i) BM has the homotopy
type of a finite CW complex; (ii) of a finite-dimensional CW complex; (iii) H_k(M; Z) = Tor_k^{ZM}(Z, Z) = 0 for all
large k. They imply U(M) = 1. With Theorem C of arXiv:2610.38760v1 (recent, unrefereed; I read its proof and ran
consistency tests) the homotopy types in question are exactly the simply connected finite complexes. Consequences:
(a) a "Swan theorem for finite monoids": if U(M) ≠ 1 then H_k(M; Z) ≠ 0 for infinitely many k; (b) a finite monoid of
finite left or right cohomological dimension (trivial module Z of finite projective dimension over ZM) has trivial
universal group and a classifying space of finite homotopy type. `OWN_RESULTS.md` §1.

F4. **(checked by my own exhaustive programs) The small models and their minimality.** All categories with at most 7
arrows and at least two objects, and all 208,672 labelled monoids of order 6 (1,373 classes up to isomorphism and
anti-isomorphism; orders 1–5: 1, 2, 6, 27, 156 classes) were enumerated by my own code (`work/code/`), with exact
integral H_1, H_2, H_3 of the nerve. Results: fewest arrows for S¹ is 4 (only the parallel pair), for S² is 5 (only
the monoid P_2 = 1 + 2×2 rectangular band, unique up to isomorphism), for S³ is 7, and no category with 7 arrows and
more than one object has the homology of S³ in degrees ≤ 3, so every smallest S³ is a monoid. P_2 ≃ S² and P_3 ≃ S³
re-proved by my own exact check of the two projective resolutions. R_2 (3 objects, 9 arrows) is homeomorphic to RP².
The triples (H_1, H_2, H_3) occurring for monoids of order ≤ 6 agree with the list the return quotes from Sweeney
(arXiv:2502.05276v2, 13 Jun 2026, recent).

F5. **(noticed) Categories with two objects and six arrows that have the homology of S² through degree 3** exist
(8 labelled ones). They do not beat P_2 in arrows; whether they are of type S² was not needed and not decided.

F6. **(hunch H1) Wall's finiteness obstruction of BC vanishes for every finite category C with BC finitely
dominated**, so the finite-dimensional homotopy types of finite categories would be exactly the finite complexes.
Reasons and a first reduction in `HUNCHES.md`. The return (G.1, G.17) does not pose this.

F7. **(question, open in the return as G.17) Is K(Z, 2) = CP^∞ the classifying space of a finite monoid or a finite
category?** Reformulation found here: BM ≃ CP^∞ iff U(M) = 1 and there is a 2-cocycle u: M × M → Z such that the
infinite monoid M ×_u Z has contractible classifying space (the extension gives a principal K(Z,1)-fibration
B(M ×_u Z) → BM classified by [u]). `HUNCHES.md` H2.

## B. Grothendieck's text

G1. V ms. 51–52 defines Hot_0 ("types d'homotopie de type fini (ou de présentation finie?)") as the homotopy types of
finite categories. F1–F4 and Part G of the return give the first exact information on this class: it contains all
finite complexes (finite posets), all BG for finite groups G, but a one-object finite category is of finite
homotopy type only when simply connected. VII ms. 128 ("pour X à composantes finies, le calcul des π_i devrait être
fini, ce qui n'est pourtant pas le cas") is consistent: finite categories have classifying spaces with infinitely
generated total homotopy.

G2. XIIapp ms. 8–11: Grothendieck's own small models, the parallel pair (circle) and the four-object, ten-arrow
category Z of type S² (his footnote 7), are upper bounds; the minima are 4 arrows (his parallel pair is minimal) and
5 arrows (a monoid). Checked: H_*(BZ) = H_*(S²) by my program.

G3. **(proved here; the return's E.17, left open there) V ms. 46 is true for "local".** A small ind-object K of
Cat hot has a W∞-invariant functor if and only if K is isomorphic in Ind(Cat hot) to the ind-groupoid (Π₁K_i)
(`OWN_RESULTS.md`, Theorems 3.1–3.2). The proof needs a Kan–Thurston theorem in which every homomorphism from the
group to a small group factors through π₁ of the space; I prove it cell by cell from the simple acyclic groups of
B.7. Consequence for the manuscript: asking that the path ind-categories H(a, b) be invariant on *all* small
categories (V ms. 44–46, VII ms. 129–132, test (b) of IX ms. 22) forces the Hom-functor to depend only on Π₁ of the
diagram shape. The condition is the wrong one unless the shapes are bounded (finite categories, as he proposes at
V ms. 51), where D.3 of the return shows that every homotopy type is ind-representable.

G4. E.4 of the return is a clean counterexample to V ms. 47 with every hypothesis of ms. 46–47 in force (finite,
full, local, fibrant stages; fibrant union). E.22 proves the T² = 1 that VII ms. 149–150 wanted from the (false)
faithfulness of finite tests. A finite category is not a compact test object (BZ/2), against VII ms. 121.

G5. IX ms. 23, "Je doute que ces conditions puissent être satisfaites pour M finie": as written the tests are
satisfied by a five-arrow category with discrete mapping spaces (E.14); the true obstruction for small M is G3.

## C. Further findings

F8. **(proved here)** A poset of type RP² has at least 34 arrows (the return has 28): `OWN_RESULTS.md`, 5.1.

F9. **(proved here)** If Sⁿ is a homotopy retract of X for infinitely many n with π_n(S³) ≠ 0 and H¹(X; Z) = 0, then
[X, S²] is uncountable (`OWN_RESULTS.md`, 4.1). With hunch H3 this would answer D.6 negatively.

F10. **(computed)** For the six-element monoid of Sweeney's Example 5.2 the cup products x₂², x₂x₃, x₃x₂ vanish
mod 2, 3 and 32003; S² is a retract of its classifying space. Evidence for BM ≃ ⋁_{n≥2} Sⁿ.

F11. **(noticed)** Theorem 1.1 of `OWN_RESULTS.md` weakens the hypothesis of Miller's Theorem B from "finite
dimension" to "bounded integral cohomology" when π₁ of the target is finite (or residually finite, or linear).
It is the monoid case that needs it: BM is never finite-dimensional as a complex, and families 249 and 321 of the
OpenAI collection (claimed, 2026) are reminders that cohomological and geometric dimension differ in general.

F12. **(flaw in the return)** D.9 attributes to Raptis's discussion of products a statement that passage does not
contain; the claim is true and the proof stands through Proposition 4.8 of the same paper.

F13. **(for the prompts of the other packages)** "Finite category" and "finite CW type" must be kept apart in every
prompt; "Thomason–Kan" must be read as "local" or as "fibrant" at each occurrence; nothing may be deduced from an
isomorphism of ind-objects.

F14. **(connection to recent results)** OpenAI family 317 (Thomason structures on nCat, claimed 25 Sep 2026) and
family 312 (homotopy hypothesis for coherators, claimed 24 Sep 2026) frame hunch H5: strict n-categories up to
higher transformations should represent exactly the types of strict n-groupoids, which stop being all n-types at
n = 3. Neither is used in a verdict.

F15. **(from the earlier review, checked: correct)** For a fibrant poset R of type S¹, η: R → Π₁R is a weak
equivalence between Thomason-fibrant categories that is not an isomorphism in Cat hot: π₀Fun(BZ, R) is a point and
π₀Fun(BZ, Π₁R) = Z. So "weak equivalence between Thomason–Kan categories ⇒ isomorphism in Cat hot" (V ms. 47) fails
for "fibrant". Also from there: B.4 needs only H²(G; Z/2) ≠ 0, which the spin extension gives without Schur's
computation of the multiplier.

## D. Compared with the earlier review (pro_reviews_20261110/1_CATHOT: REVIEW.md, REVIEW_author.md, REVIEW_G6.md)

Opened only after my own REVIEW.md was complete. The earlier reviews were written at effort medium.

**Where it was right.**
- Its verdicts on the 84 items labelled Proved, Refuted or Known agree with mine: none false. Its G.6 verdict
  (REVIEW_G6.md) is the same as mine, with the same proof and the same second route through Atiyah; its statements
  of Miller's Theorem B and of Atiyah (6.11), (7.2) are exact.
- Its enumeration of monoids of order 5 and 6 found the same counts (4,122 and 208,672) and the same exclusion of
  S³; "exactly the six labellings of P₂" at five arrows agrees with my uniqueness statement.
- It had the reduction of E.17 to a Kan–Thurston statement with no small quotients ("(KT_μ)"), expected the answer
  yes, and drew the consequence that test (b) cannot be asked on all shapes. I found the same reduction
  independently; its version uses only that acyclic maps are epimorphisms in Hot, which is slightly more economical
  than mine.
- Its observation that B.4 does not need Schur's computation, and its "Consequence 1" (F15 above), are correct.
- Its remark that a finite category of type CP^∞ would answer D.6 negatively (phantom maps) is correct.

**What it missed, or left weaker.**
- It left E.17 open, with (KT_μ) unproved ("should follow from Maunder's proof … I have not checked"). Proved here
  (`OWN_RESULTS.md`, 3.1), so E.17 is settled.
- G.5 (Theorem C of the preprint) was "unverified; nobody here has checked its proof". Here the proof was read in
  full, its lemmas re-derived, and Theorem A tested on five monoids.
- It did not check the 1985 correction to Miller's paper, nor Miller's K-theory computation. Both checked here.
- No sharpening of G.4: the equivalence finite ⇔ finite-dimensional ⇔ bounded homology for finite monoids and the
  Swan-type corollary (`OWN_RESULTS.md`, 2.1–2.3) are new here.
- Its enumeration stopped at 6 arrows; the 7-arrow categories with several objects (needed to say that every
  smallest S³ is a monoid) were done here. It did not state uniqueness of the smallest S¹ and S².
- D.9's cylinder argument, E.14's path-category paragraph and E.19 were "not checked" there; D.9 is checked here
  (and the wrong attribution found). The return's code was "not run or read" there; it was read here.
- Literature not opened there and opened here: Sweeney (v1, v2), Cianci–Ottina, Domínguez–Segovia (the statements
  used), Chachólski–Scherer, Hatcher 4C.1, Miller's correction, Atiyah §8.
- Not there: the bound a_pos(RP²) ≥ 34; the criterion for uncountably many maps to S²; the cup-product evidence;
  the Wall-obstruction question for finite categories (H1); the reformulation for K(Z, 2) (H2).

**Where it was wrong or too weak in wording.**
- I found no mathematical error in it.
- REVIEW.md, row G.4, says "proved, given Miller's Theorem B"; REVIEW_G6.md rightly drops "given". Row G.15 excludes
  the monoids of order 6 by mod-2 Betti numbers through degree 4; that is sufficient because none has the numbers
  of S³, and my integral computation confirms it.
- Its statement that the E.17 reduction "needs a second check" was the honest status then. The grant-evidence entry
  and the findings file can now say that E.17 is proved in this review, still unchecked by a second party.

**What it did that I did not.** It compared the return with the companion's audit rows (V-I026 …, VIIc-…, IX-…) and
wrote the table "Corrections the companion needs" and the list of changes for prompts 2–7. I did not open the
companion's row files for that; its table is consistent with my verdicts, with one amendment: at V ms. 43–46 (row
V-I052) the implication is no longer open.
