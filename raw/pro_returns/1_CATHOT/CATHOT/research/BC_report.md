# Parts B and C research and audit report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. The section's 17 numbered statements are all recorded in `BC_results.csv`.

## Material inspected

Read the attached prompt, the pilot overview's envelope lead, and the V manuscript passages at ms.37--49 defining and invoking the right adjoint. The prior companion and leads were treated as claims to check, not authorities.

Primary sources opened and relevant passages inspected:

- Higman, Neumann, and Neumann (1949), *Embedding Theorems for Groups*, publisher PDF, Theorems I and II. Theorem II permits simultaneous conjugation of an arbitrary family of isomorphic subgroups while retaining the base group.
- Baumslag, Dyer, and Heller (1980), *The topology of discrete groups*, complete 47-page primary-source PDF at the University of Chicago archive. Inspected Proposition 4.1, Theorem 4.2, Corollary 4.5, Lemmas 5.1--5.4, and Theorem 5.5. The previously missing background paper was found freely available at `https://math.uchicago.edu/~shmuel/lg-readings/Baumslag-Dyer-Heller.pdf`. Theorem 5.5 explicitly states a same-cardinality acyclic embedding for infinite groups.
- Domínguez and Segovia, arXiv:2012.02464v2, *Extending free group action on surfaces*, equation (35), Proposition 20, and Corollary 21. These record the finite alternating-group multiplier and a compatible torus generator. The journal version is entitled *Extending free actions of finite groups on surfaces* (2022); its corresponding numbering is equation (34), Proposition 21, Corollary 22. The paper consistently cites the inspected arXiv numbering.
- Lawson, *An introduction to Bousfield localization*, author PDF dated March 11, 2019, Example 9.2 and Examples 9.5--9.6. Example 9.2 confirms that simply connected spaces are local with respect to integral homology equivalences; the section gives the complete Postnikov mapping-space argument needed here.
- Löh, *A note on bounded-cohomological dimension of discrete groups*, author PDF dated September 8, 2015, Corollary 1.3. This independently records same-cardinality mitotic embeddings. It was useful as a search lead but is not needed in the final proof.
- Palmer and Wu, *Embedding groups into acyclic groups*, arXiv:2510.16879v1, introduction. This supplied current bibliographic cross-checks for Kan--Thurston and BDH; none of its stronger finite-generation theorems is used.

Schur's 1911 article bibliographic record was opened, but its original full text could not be accessed through the available reader. Its bibliography entry is explicitly marked **unverified**. No proof depends on an uninspected theorem number in it. The finite multiplier calculation is instead an explicitly identified **Known** input verified in the Domínguez--Segovia primary research paper. Its upper-bound proof is not independently reproduced; the infinite-cardinal calculation and all required transition maps are proved in full from that finite input.

## Search record and claims of novelty

Searches included `finitary alternating group Schur multiplier infinite set Z/2`, `simple groups prescribed homology`, `simple Kan-Thurston groups homology`, `every group simple group same cardinality`, `acyclic simple every group embed`, `mitotic acyclic Baumslag Dyer Heller`, `Schur multipliers alternating groups n 8 theorem proof pdf`, and `homology equivalence simply connected mapping spaces integral`. Searches about categorical homotopy, natural transformations, local objects, and 1-types did not locate the precise full classification stated here. This is not a novelty claim; the argument is assembled from standard group embeddings, amalgams, Postnikov towers, and the nerve of a groupoid.

The alternating-union construction of a simple acyclic envelope was also encountered in a MathOverflow discussion of arbitrarily large acyclic simple groups. That forum was used only as a search lead and cross-check. The paper proves the observation, the cardinal bounds, and all subsequent consequences independently from the verified primary ingredients.

## Corrections and settled leads

Lead 1 is correct. The cardinal argument must remain within the fixed universe, and the infinite homology calculation requires checking the maps in the directed system, not just the abstract finite Schur multipliers. The section does both. Evaluation `Fun(BG,K) -> K` is a strict category isomorphism under the small-quotient hypothesis, including categories with nontrivial endomorphisms and idempotents.

The argument is strengthened to **every non-1-type**, including arbitrary disconnected types and arbitrary actions of a nontrivial fundamental group. Finitary alternating groups alone were not assumed to provide the required essential maps to spheres. Instead, for each infinite cardinal lambda, simple and acyclic embeddings are alternated to build an acyclic simple group of size lambda containing a prescribed group. Amalgamated doubles of such envelopes, iterated from Z, produce perfect groups G of size lambda with no nontrivial homomorphisms to any smaller group and homology equivalences `BG -> S^n` for every n >= 2. Mapping into simply connected universal covers turns nonzero higher homotopy elements into essential unpointed maps. The resulting groups G need not be simple; the exact small-quotient property requested in the prompt is proved.

Lead 2 is fully settled affirmatively: representable homotopy types are exactly 1-types, and local categories are exactly those isomorphic in Cat hot to groupoids. The canonical groupoidification unit is the relevant isomorphism. Having a 1-type nerve alone is not sufficient: the infinite fence has contractible nerve and is not local.

The local subcategory is reflective, with reflector Pi_1. It is **not coreflective**. The reflector inverts 1-equivalences, a larger class than W_infty, so this does not restore the nonexistent right adjoint to Cat hot -> Hot. The right adjoint asserted at V ms.37 is false, rather than merely unproved. Thomason fibrancy is also insufficient to imply localness; a Thomason fibrant replacement of a category of type S^2 is already a counterexample.

## Computations

`code/bc_checks.py` uses exact permutation operations, rational Clifford algebra, free-product normal forms, and finite graph distances. Its deterministic output is `code/bc_checks_output.json`.

It verifies the fresh-point commutator producing a 3-cycle; verifies that spin lifts of the two Klein-four generators square to -1 and anticommute; checks the simple-envelope word for all 1,360 choices of nonidentity g and arbitrary h in cyclic groups of orders 2 through 16; and verifies finite fence truncations with 3, 5, 9, 17, 33, and 65 objects, with endpoint distances 2, 4, 8, 16, 32, and 64. These finite checks supplement the general proofs and are not presented as proof of an infinite assertion or as a recomputation of the full finite Schur multiplier.

`code/bc_write_metadata.py` produces the 17-row results ledger; its output is retained in `code/bc_write_metadata_output.txt`.

## Remaining questions in Parts B and C

None of the requested classification or representability questions in Parts B and C remains open in this treatment. The proof uses the stated classical finite Schur-multiplier theorem as a Known ingredient. Whether some of the explicit large groups can additionally be required to be simple while retaining the exact sphere-plus type is neither needed nor asserted. The central classification proof does not depend on the alternating-group calculation at all; it also independently refutes the proposed right adjoint.

No transcription correction was needed for the mathematical formulas used from V; the correction is to the asserted adjoint itself.
