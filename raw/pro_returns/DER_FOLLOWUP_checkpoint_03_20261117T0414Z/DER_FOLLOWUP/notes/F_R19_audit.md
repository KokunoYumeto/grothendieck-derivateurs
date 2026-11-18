# R19 primary-source audit: cotes 104 and 106

Audit date: 17 November 2026. This note records source inspection and an independent mathematical reading of the relevant proof terms. **No Lean compiler or Lake build was run in this audit.** Consequently “inspected Lean proof” below does not mean “executed locally.”

## 1. Sources actually obtained, provenance, and reproducibility

The primary source is Michel Hua's `Commutator-IO/grothendieck-project`, pinned here to commit

`08e7d549678e7434e4d21d95a2cefa8e74fd2acf`

(commit date `2026-11-16T20:59:20Z`). Public raw files and GitHub API metadata were fetched without credentials. The reproducible commands are `python code/F_source_fetch.py` for the original discovery and `python code/F_R19_fetch.py` for the now-pinned proof-source fetch. Their detailed HTTP, size, and hash records are `code/outputs/F_source_fetch.json` and `code/outputs/F_R19_fetch.json`. The latter checks each repository file's Git blob hash against the downloaded recursive tree; all twelve repository-file checks succeeded. The four additional API/fork-file fetches also succeeded. Sources are retained under `notes/R19_public_sources/`.

| Source opened | Exact use in this audit |
|---|---|
| `README.md`, especially “Transcription” and “The Lean appendix” | Project provenance and the distinction between verification of a reading and fidelity to a manuscript |
| `RIGHTS.md`, `LICENSE` | Project's stated separation of its code from manuscript transcriptions; no inference that a manuscript transcription is CC0 |
| `lean/README.md`, introduction and rows 104 and 106 | Project's precise advertised scope and limitations of these two formalizations |
| `lean/lean-toolchain`, `lean/lakefile.toml`, `lean/lake-manifest.json` | Compiler and Mathlib pins and build options |
| `.github/workflows/lean.yml` | Actual configured build and axiom-audit workflow, distinguished from evidence that a particular run succeeded |
| `lean/Grothendieck/Folder104.lean`, directness section and the semisimplex declarations | Exact hypotheses and proof of the c104 statement used here |
| `lean/Grothendieck/Upstream/SemiSimplexCategoryReedy.lean` in full | The local dependency implementing the directness theorem; it is not an accepted upstream Mathlib theorem |
| `lean/Grothendieck/Folder106.lean` in full | Exact cofibration axioms, span relation, quotient, composition, Brown comparison, inverse functor, and final statements |
| `docs/lean/sections/104.tex`, `docs/lean/sections/106.tex` | Written exposition associated with the code; the mathematical conclusions below were checked against the actual Lean statements |
| `src/content/findings.ts` (saved as `findings.ts`), relevant entries only | c106's evolving finding and the project's warning that its reading and literature comparison are separate questions |
| Mathlib PR 44731 metadata, files, comments, and its exact `Direct.lean` | Status of the upstream proposal and the proof actually proposed |

Stable public entry points:

- [Pinned Folder104.lean](https://github.com/Commutator-IO/grothendieck-project/blob/08e7d549678e7434e4d21d95a2cefa8e74fd2acf/lean/Grothendieck/Folder104.lean).
- [Pinned Folder106.lean](https://github.com/Commutator-IO/grothendieck-project/blob/08e7d549678e7434e4d21d95a2cefa8e74fd2acf/lean/Grothendieck/Folder106.lean).
- [Pinned local Reedy dependency](https://github.com/Commutator-IO/grothendieck-project/blob/08e7d549678e7434e4d21d95a2cefa8e74fd2acf/lean/Grothendieck/Upstream/SemiSimplexCategoryReedy.lean).
- [Mathlib PR 44731](https://github.com/leanprover-community/mathlib4/pull/44731), proposed file at fork commit `a38dc275ef15bfa207bd9cb3ac0f18fce7725c7c`.

### Verification and authorship boundaries

The checked source pins Lean to `leanprover/lean4:v4.35.0-rc4` and Mathlib to `715a03a90adf491de40fbec8b456c179a623435f`. Its configuration sets `warningAsError = true`; the workflow invokes `leanprover/lean-action@v1` with `axiom-audit: true`. The workflow comments identify the permitted axioms as `propext`, `Classical.choice`, and `Quot.sound`, and say that an independent `leanchecker` recheck is omitted. These are **configuration facts**, not a local build result or proof that the current commit completed that workflow.

A literal search of both proof files, the local Reedy dependency, and PR 44731's proposed file found none of the tokens `sorry`, `admit`, `axiom`, `unsafe`, or `native_decide`. This is a limited textual check; it is not a substitute for compiling or inspecting the complete transitive dependency closure. The mathematical arguments needed here are also set out and audited below.

The README says that transcription skills have used Opus 5.5 since 19 October 2026, with earlier Fable/Opus passes, and that transcription headers record their own provenance. It does **not** establish the precise model or effort level that wrote each line of these two Lean files. PR 44731 explicitly discloses AI assistance by a Claude model under Michel Hua's direction; its description does not specify a model version or reasoning effort. We do not silently transfer the transcription provenance to every proof file.

The project's own scope warning is important: verifying the formalized reading does not verify that this is exactly what Grothendieck wrote. We have not independently collated cotes 104 and 106 against manuscript images for this audit. Page references in the project use its numbering; the user's R19 convention gives the project page as scan page plus one. None of the conclusions here rests on a new attribution of priority to a manuscript.

### Correction to “Mathlib #44731”

PR 44731 was opened on 11 October 2026 and **closed, unmerged, the same day** (`state = closed`, `merged = false`, `merged_at = null`). The reviewer asked for closure because obtaining a good direct-category API would require substantial work. The inspected comment does not allege a mathematical error. Thus it is appropriate to cite a proposed and inspected Lean proof; it is inaccurate to call this an accepted Mathlib result.

There is a public bot comment reporting a post-build, Lean-aware environment diff at the proposed commit, with four new declarations: `ofWellFounded`, `wellFounded`, `eq_id_of_endo`, and the unique identity/all-morphisms factorization instance. This is reported upstream build evidence for that proposal, not our own execution and not evidence of merger. The local project explicitly vendors the declarations in `Grothendieck.Upstream.SemiSimplexCategoryReedy`; that file says its branch was closed upstream. The proofs needed by Folder104 therefore remain available locally regardless of PR status.

## 2. Cote 104: exact statement and mathematical audit

The relevant namespace is `Grothendieck.Folder104`. The source defines

\[
\operatorname{Strict}(X,Y)\iff
  \operatorname{Hom}(X,Y)\ne\varnothing
  \quad\text{and}\quad
  \operatorname{Hom}(Y,X)=\varnothing.
\]

The declarations used are:

| Declaration | Source location | Exact role |
|---|---:|---|
| `Strict` | Folder104, line 165 | The preceding strict relation |
| `strict_of_not_isIso` | 169 | Identity endomorphisms imply a noninvertible arrow has no reverse arrow |
| `strict_of_not_identities` | 175 | Adds skeletality to turn a nonidentity arrow into a strict pair |
| `reedyDirecte` | 187 | With identity endomorphisms, skeletality, and well-founded `Strict`, constructs `ReedyStructure (identities M) ⊤ Ordinal` |
| `wf_of_degre` | 194 | Any degree into a well-founded preorder that strictly raises every nonidentity arrow makes `Strict` well founded |
| `entiers_relatifs_non_directe` | 203 | The ordered set of integers has monic arrows and only identity endomorphisms, but is not direct |
| `deltaInj_skeletal`, `deltaInj_lt`, `deltaInjReedy` | 277, 285, 299 | The category of nonempty finite ordinals and order embeddings is skeletal and direct |

The local dependency proves the more general theorem in namespace `HomotopicalAlgebra.ReedyStructure`: the relation

\[
R(X,Y)\iff\exists f:X\longrightarrow Y\text{ that is not an identity}
\]

is well founded if and only if the category admits a degree that strictly raises nonidentity arrows, with the existence direction taking ordinal rank. Its factorization condition is elementary: the only factorization with first factor an identity is the identity followed by the given arrow. In the converse direction, `R` is a subrelation of the pullback of the well-founded strict degree order. This is exactly what `ofWellFounded` and `wellFounded` implement. The PR's proposed proof and the local dependency agree on this argument.

Here is the bridge to the manuscript's stricter relation. If `f:X→Y` has a reverse arrow `g`, both `gf` and `fg` are endomorphisms, hence identities. Thus `f` is invertible. If the category is skeletal, then `X=Y`, and the identity-endomorphism hypothesis makes `f` an identity. Therefore every nonidentity arrow is strict, and ordinal rank of `Strict` supplies the degree. Conversely any strict pair has a nonidentity arrow and so strictly raises degree. These implications check the advertised iff. The assertion that every arrow is monic is **unused** in this directness argument.

“Direct” here allows an ordinal-valued degree. An arbitrary ordinal-ranked direct category need not admit a natural-number-valued degree. For the finite posets occurring in our paper there is no such distinction: the degree of an element can be the maximum length of a strict chain ending there, a natural number. Every strict arrow raises that degree. For a face poset, face cardinality minus one is an even more explicit choice. The semisimplex category has degree the ordinal's length. Thus these constructions satisfy the source's exact hypotheses without an extra finiteness inference.

The integers counterexample is material: monicity and identity endomorphisms alone do not imply directness. Nor does directness imply filteredness, totality, or asphericity; the statement is solely about a degree structure.

**Audit conclusion:** the c104 directness claim is mathematically correct under the stated skeletality and well-foundedness conditions, and the exact Lean proof and its custom dependency were inspected. It can be cited as an independently checked proof source, with PR status corrected as above.

## 3. Cote 106: exact axioms, quotient, and proof

### 3.1 Hypotheses actually formalized

In `Grothendieck.Folder106`, the class `CategorieACofibrations W cof` is a proposition on a category with an initial object. Its fields explicitly impose:

1. Isomorphisms lie in `W` and in `cof`; cofibrations are closed under composition; `W` satisfies all three clauses of two out of three.
2. Pushouts along cofibrations exist. In a pushout of `c:b→a` and `u:b→y`, with `c` a cofibration, the map `y→a∐_b y` is a cofibration, and is in `W` if `c` is in `W`; the other map `a→a∐_b y` is in `W` if `u` is in `W`.
3. Every map factors as a cofibration followed by a member of `W`.

An object is cofibrant when its initial map is a cofibration. The full span theorem additionally assumes **every object is cofibrant**, through the explicit parameter `hcof`. These are the source's precise version of the named C1–C3 axioms. This audit does not identify them with every convention called “Baues C1–C3” in the literature without writing them out.

The proof's initial Brown factorization and inversion lemmas need less of C2. The span composition uses the clause that pushing a weak equivalence along a cofibration gives a weak equivalence. The other clause, `pushout_W_of_W`, is not used anywhere in this file. Its presence in the statement is harmless and must not be confused with an extra, unstated assumption.

### 3.2 The localization Hom description

From here the namespace is `Grothendieck.Folder106.CategorieACofibrations`. `Span W cof x y` consists of diagrams

\[
x\xrightarrow{f}z\xleftarrow{i}y,
\qquad f\in\mathrm{cof},\quad i\in W.
\]

`Span.Arrow s t` means the existence of an apex map `u:z→z'` commuting with both legs. No cofibration condition is imposed on `u`. It is automatically a weak equivalence by two out of three applied to the two denominators. The formal `Pi0` is `Quot Span.Arrow`, that is, the quotient by the equivalence relation generated by the arrow-existence relation. It correctly gives connected components of the ordinary category of such spans, not just isomorphism classes, direct refinements, or a quotient under an additional homotopy relation.

Composition pushes out the first denominator against the second numerator, a cofibration. The numerator of the composite is a composite of cofibrations and the denominator is a composite of weak equivalences, by precisely the C2 clause just identified. The proof verifies that maps of spans act on this construction, and verifies units and associativity in the quotient. This defines the category `Rect W cof` with the same objects as the original category and these quotient Hom sets.

`qbar` takes the component of a span to `[i]^{-1}[f]` in Mathlib's explicitly constructed localization. The main declarations are:

| Declaration | Source line | Content |
|---|---:|---|
| `factorisationDeBrown_general` | 213 | For any map between cofibrant objects, a Brown factorization with a weak-equivalence retraction and a trivial-cofibration section |
| `factorisationDeBrown` | 226 | If the map is in `W`, both resulting cofibrations are in `W` |
| `inverse_W_of_inverse_W₀` | 237 | A functor inverting `W∩cof` inverts `W`, when all objects are cofibrant |
| `localisation_W₀_iso_localisation_W` | 254 | Strict inverse functors between the two specified localization constructions |
| `Span`, `Span.Arrow`, `Pi0` | 288, 305, 443 | The exact span data, arrow relation, and component quotient |
| `Critere` | 460 | The manuscript's condition (**), expressed by `Relation.EqvGen Span.Arrow` |
| `arrow_brown` | 543 | Common-successor comparison for a span equipped with a specified retraction |
| `phi`, `phi_inverts`, `phiBar` | 584, 644, 673 | The Brown-span functor, inversion of `W`, and its lift from the localization |
| `phiBar_frac` | 684 | The lift recovers the component of every span from its fraction |
| `fidele` | 699 | `qbar` is injective |
| `critere` | 710 | Condition (**) always holds under `hcof` |
| `fidele_iff_critere` | 716 | The advertised equivalence, with both sides already proved |
| `qFunctor_iso` | 723 | `qFunctor` and `phiBar` compose to the identity in both orders |
| `plein` | 747 | `qbar` is surjective |

Thus the exact mathematical conclusion is the canonical bijection

\[
\operatorname{Hom}_{C[W^{-1}]}(x,y)
\cong\pi_0\{x\overset{\mathrm{cof}}\longrightarrow z
                    \overset{W}\longleftarrow y\}.
\]

For the particular object-preserving localization constructed in the file, this gives an isomorphism of categories with literal inverse functors. For an arbitrary equivalent localization model the invariant conclusion is the corresponding categorical equivalence and Hom bijections.

### 3.3 Independent audit of the key proof

For `F:x→y`, form the coproduct `x∐y` using initial maps and factor `(F,id_y)` as a cofibration `c:x∐y→b` followed by `α:b→y` in `W`. The induced maps `j_x:x→b` and `j_y:y→b` are cofibrations, `αj_x=F`, and `αj_y=id_y`. Hence `j_y∈W`; if `F∈W`, also `j_x∈W`. This is the Brown span of `F` and proves that inverting trivial cofibrations already inverts all weak equivalences.

The potentially delicate comparison lemma is `arrow_brown`. Suppose a span `s=(f,i)` has a map `ψ:z→y` with `ψi=id_y` and `ψf=F`. Push out the Brown cofibration `c:x∐y→b` along `(f,i):x∐y→z`. The pushout maps to `y` through the compatible pair `(α,ψ)`. Factor that map as a cofibration `κ` followed by a weak equivalence `β`. The resulting span is a common successor of `s` and the Brown span. Its numerator is a composite of cofibrations. Its denominator followed by `β` is `id_y`, so it is a weak equivalence by two out of three. This establishes all span-membership conditions, not merely the commutative diagram.

The same comparison proves independence of a chosen Brown factorization, the identity law, and compatibility with composition: the pushout composite of Brown spans has the required retraction to the final target. One obtains a functor `φ:C→Rect`. For a cofibration, `φ(f)` is the class of `(f,id)`. For a trivial cofibration, `(id,f)` is its inverse. Brown factorization then shows that `φ` inverts every member of `W`, so it descends to `φ̄:C[W^{-1}]→Rect`.

Finally every span is the composite of `(f,id)` and `(id,i)`. The latter is the inverse of `φ(i)`, so `φ̄q` recovers every span component. Conversely `qφ` is the localization functor, since a Brown span has the specified weak-equivalence retraction. The localization universal property gives the other composite identity. This proves the asserted bijection without assuming condition (**). Applying injectivity to the two sections of a weak equivalence yields (**).

There is no circular use of the manuscript's unproved section criterion in this argument. There is also no functorial factorization assumption: choices occur in the Brown construction, and the component comparison supplies the needed independence.

**Audit conclusion:** the strong c106 statement, including automatic (**), is correct under the explicit axioms above. The source contains a complete proof of this statement. Its role is a formalization of the project's completed reading, not a certification of a manuscript transcription or a claim that the complete argument is new.

## 4. Safe uses in the paper

Suggested finite-poset addition, using bibliography key `FR19Hua104`:

```tex
The finite posets used here are also direct categories.  Indeed, the
maximum length of a strict chain ending at an object defines a
natural-number degree raised by every nonidentity map; for a face
poset one may use face dimension.  This is the finite case of the
well-foundedness criterion formalized in R19, cote~104,
\texttt{reedyDirecte} and \texttt{wf\_of\_degre}
\cite{FR19Hua104}.  The criterion concerns directness alone and
places no filteredness hypothesis on these examples.
```

Suggested addition near G.13, using key `FR19Hua106`:

```tex
A related fraction description is available in the all-cofibrant
setting of R19, cote~106.  Under the explicit C1--C3 cofibration
axioms recorded there, the localization Hom set is the set of
connected components of spans
$x\xrightarrow{\mathrm{cof}}z\xleftarrow{W}y$;
the declarations \texttt{qFunctor\_iso}, \texttt{fidele}, and
\texttt{plein} prove the description, and \texttt{critere} proves
the manuscript's condition~$(**)$ automatically \cite{FR19Hua106}.
This gives length-two representatives.  Its equality relation is
connectivity in a span category, so an application to arbitrary
products still needs the common-refinement or uniform homotopy
argument used in \ref{G:fractions-products} and
\ref{G:model-products}.
```

The c106 theorem by itself does not assert the ordinary Ore calculus of G.13: its quotient is generated by arbitrary finite zigzags of span maps. In particular one must not interchange `π0` with an arbitrary infinite product merely from this statement, or infer a uniform bound on equality witnesses. G.13's actual common-refinement proof and G.14's model-category homotopy proof remain the reasons their product conclusions hold.

## 5. Scope of the rest of R19

The audit above settles the two Lean statements specifically assigned to this note. R19's cote-105 open-sieve assertion was independently proved and its fixed-derivator details audited in `notes/C8_independent_audit.md`; that proof does not treat an uninspected Lean claim as a premise. The correction records for cotes 114 and 118 were read in `findings.ts`, but their manuscript accuracy and complete formal files were not re-audited here. Their mathematical effects belong to the separate Part G/source audit. Nothing in this note retracts those corrections or promotes the false implications mentioned in the prompt.

The bibliography fragment `notes/F_R19_refs.bib` supplies distinct, commit-pinned entries for the two formal files, the local Reedy dependency, the project provenance, and the unmerged upstream proposal.
