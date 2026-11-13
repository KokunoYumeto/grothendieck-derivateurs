<!-- Final answer of TOTAL_EXACT_2 (GPT-6 Astra, ChatGPT Pro mode, account 1), pasted by the user 13 Nov 2026 ~11:55 UTC; saved verbatim from the session transcript. -->

**All requested Parts and every lettered Lead are now proved or refuted. Total asphericity does not imply exactness of abelian colimits.** One explicit countable category refutes the integral implication, the rational implication, the implication over every prime field, and the triple assertion. Separately, the repaired Adámek–Koubek–Reiterman construction has nonzero binary \(H_2\) for **every admissible choice** of its parameters and targets.

## Completed deliverable

[**TOTEX2_checkpoint_03.zip**](https://chatgpt.com/library?file_id=libfile_fde3_f-199c01ed485881918fae119691c9aabf_c6789dc4b4d481919ad633aabe6d84d0&account_id=personal) — **56.5 MB**

The ZIP contains the complete **78-page LuaLaTeX paper**, its source, the results CSV, annotated bibliography, outcome report, all mathematical programs and retained outputs, exact certificates, and independent proof-audit records. Earlier checkpoints are preserved unchanged as historical records.

The current paper has **89 numbered statements: 74 Proved, 13 Refuted, 2 Known, and none Open**. All statement numbers below refer to that paper.

| Requested item | Outcome | Principal statements |
|---|---|---|
| A.1: totality implies integral exactness | **Refuted** | A.1, A.24, A.34 |
| A.2: rational exactness | **Refuted** | A.3, A.24 |
| A.2: exactness over every \(\mathbb F_p\) | **Refuted for each prime**, using the same category and triple | A.3, A.24 |
| B.1: affine equalization of triples | **Refuted** | B.1 |
| B.2: Leads 1–5 | Formal assertions proved; explanatory overstatements corrected | B.3–B.10 |
| C.1: universal repaired-AKR binary \(H_2\) survival | **Proved for every admissible construction** | C.1, C.19–C.28 |
| C.2: Leads 6–9 | Proved with the stated corrections to literal overstatements | C.2–C.6, C.38–C.41 |
| D.1: both right-hand inclusions | **Both strict** | D.1 |
| D.2: manuscript corrections | Completed, including refutation of the proposed exactness replacement | D.2–D.4 |
| D.3: literature record | Completed, distinguishing opened bodies from unsuccessful retrievals | Report access table and bibliography |

## 1. The explicit total, nonexact category

Let \(\mathcal C_\delta\) have as objects all nonempty finite linearly ordered simple \(3\)-uniform hypergraphs \(X\) satisfying

\[
\delta_X(U)=2|U|-3|E_X(U)|>0
\qquad
\text{for every nonempty }U\subseteq X.
\]

Here \(E_X(U)\) is the set of hyperedges contained in \(U\). A completely specified small skeleton uses underlying ordered sets

\[
[n]=\{1<\cdots<n\},\qquad n\geq1.
\]

An arrow \(f:X\to Y\) is a strictly increasing induced hypergraph embedding whose image is **strictly \(d\)-closed**, meaning

\[
\delta_Y(U)>\delta_Y(fX)
\qquad
\text{whenever }fX\subsetneq U\subseteq Y.
\]

Identities and composition are ordinary identities and composition of functions. Lemma A.21 proves the closure calculus needed for composition, restriction and intersections, and proves free amalgamation. In particular, the category is small, nonempty and connected.

The conclusion is:

\[
\boxed{\mathcal C_\delta\text{ is total but is not exact over any nonzero unital ring.}}
\]

Theorem A.34 also proves the same assertion for its full subcategory consisting of objects whose individual points and hyperedges are all \(d\)-closed.

### The named triple

Take \(V\) to be the one-point object and \(W\) to be the ordered three-point object with its unique three-element subset as a hyperedge. Let

\[
v_1,v_2,v_3:V\longrightarrow W
\]

select the first, second and third vertices.

These are arrows: a singleton has predimension \(2\), while its proper extensions inside \(W\) have predimension \(4\) or \(3\), both strictly greater than \(2\).

For a nonzero unital coefficient ring \(R\), define the natural map

\[
D_R:R[\mathcal C_\delta(W,-)]
   \longrightarrow
   R[\mathcal C_\delta(V,-)]^2
\]

by

\[
D_R(g)=\bigl(gv_2-gv_1,\;gv_3-gv_1\bigr).
\]

**Proposition A.24 proves that \(D_R\) is objectwise injective for every such \(R\).**

The argument is independent of the characteristic. Suppose a nonzero coefficient vector has support consisting of \(r\) distinct arrows \(g:W\to X\). Increasing embeddings of \(W\) with the same image are equal, so these arrows determine \(r\) distinct hyperedges. If their vertex union has \(u\) vertices, positivity gives

\[
2u>3|E_X(U)|\geq3r.
\]

There are \(3r\) incidences between the selected edges and their vertices. Therefore some vertex belongs to exactly one selected edge. Otherwise every vertex would have at least two incidences, giving \(2u\leq3r\).

If the coefficient of that unique edge is \(c\neq0\), its contribution at the private vertex is one of

\[
(-c,-c),\qquad(c,0),\qquad(0,c).
\]

It cannot cancel. This proves injectivity over an arbitrary nonzero unital ring, including rings with torsion or zero divisors.

An affine equalizer \(t\) of \(v_1,v_2,v_3\) would satisfy \(D_R(t)=0\) and \(\operatorname{aug}(t)=1\). Injectivity excludes it.

### The derived-colimit obstruction is explicit

Put \(Q_R=\operatorname{coker}D_R\). We obtain an exact projective presentation

\[
0\longrightarrow R[\mathcal C_\delta(W,-)]
 \xrightarrow{D_R}
 R[\mathcal C_\delta(V,-)]^2
 \longrightarrow Q_R
 \longrightarrow0.
\]

The colimits of the two projective terms are \(R\) and \(R^2\), and the induced map between them is zero: every displayed difference has augmentation zero. Consequently,

\[
\boxed{T_1^{\mathcal C_\delta}(Q_R)\cong R\neq0.}
\]

Moreover,

\[
\operatorname{pd}_{R\mathcal C_\delta}(Q_R)=1,
\qquad
T_i^{\mathcal C_\delta}(Q_R)=0\quad(i\geq2).
\]

Thus the failure of exactness already occurs on a diagram of projective dimension one. The same presentation works for

\[
R=\mathbb Z,\qquad R=\mathbb Q,\qquad R=\mathbb F_p
\]

for every prime \(p\).

This also establishes that **three ordinary arrows are the smallest possible obstructing family**: total categories satisfy the ordinary-pair affine-equalization condition IV, while this triple fails simultaneous equalization. The relevant classical distinctions between conditions I, III and IV are retained from the opened Isbell–Mitchell results, with their precise hypotheses (Isbell & Mitchell, 1976, Proposition 2.3, Theorem 3.1, and Proposition 3.3).

## 2. Why totality holds for every set-valued action

The totality theorem covers

\[
\forall H:\mathcal C_\delta\longrightarrow\mathbf{Set},
\]

including infinite actions, noninjective transition maps and empty values. It is established by a finite amalgamation argument followed by two explicit homotopy-final comparisons.

### Finite bridges give the stabilizer identity

Let \(M\) be the countable rich homogeneous limit of the strong amalgamation class and let

\[
G=\operatorname{Aut}(M)
\]

with its topology of pointwise convergence. For a finite closed substructure \(B\subseteq M\), write

\[
G_B=\{g\in G:g|_B=\operatorname{id}_B\}.
\]

The strong-limit construction is covered by Evans, Hubička, and Nešetřil (2019, Theorem 2.6); the required weighted hypergraph closure and bridge estimates are proved directly in the present paper.

The decisive finite result is Lemma A.30. Given closed \(B,C\subseteq D\), and two prescribed closed embeddings of \(D\) into a finite ambient object \(E\) agreeing on \(B\cap C\), it constructs a finite chain of copies of \(D\) joining those embeddings, with successive copies agreeing alternately on \(B\) and on \(C\).

The proof checks every subset of the resulting amalgam. Nonfixed vertex fibers occupy at most three consecutive copy indices. Cutting the cyclic construction produces a linear free amalgam; restoring the cut loses at most \(2m\) in predimension, where

\[
m=\max(|B|,|C|).
\]

When the proper visibility intervals cover all indices, the first-appearance count supplies at least one positive integral predimension increment per relevant index. Choosing the bridge sufficiently long makes this dominate both the cut loss and the ambient predimension. A separate coordinate-interpolation argument gives a linear order extending all prescribed orders.

This proves, algebraically rather than merely after taking topological closure,

\[
\boxed{\langle G_B,G_C\rangle=G_{B\cap C}.}
\]

Now let \(U\leq G\) be open. Choose a finite closed \(B\) of minimal cardinality with \(G_B\subseteq U\). For \(u\in U\), the stabilizer identity gives

\[
G_{B\cap uB}\subseteq U.
\]

Minimality forces \(uB=B\). Since an increasing permutation of a finite linear order is the identity, every \(u\in U\) fixes \(B\) pointwise. Hence

\[
\boxed{U=G_B.}
\]

The empty support is allowed, yielding \(U=G\). This is the complete open-subgroup classification in A.32.

### Contractible cosieves provide the comparison mechanism

Work in the equivalent category \(A_M\) of nonempty finite closed substructures of \(M\), with **all** increasing closed embeddings as arrows.

Every nonempty full cosieve in a slice \(P/A_M\) is contractible. Given an object \(P\to Z\) of the cosieve, freely amalgamating with \(Z\) over \(P\) defines a functor with natural transformations

\[
\operatorname{id}\longrightarrow F
\longleftarrow\operatorname{const}_{P\to Z}.
\]

The order is chosen functorially, gap by gap over \(P\). The image remains in the cosieve. The analogous disjoint-union construction contracts \(BA_M\).

These contractions identify the comma categories needed below. The homotopy-finality criterion is used in its covariant-comma convention; it is also the contractible-comma case of Goerss and Jardine (2009, Theorem IV.5.6).

### First comparison: remove noninjective transitions

For arbitrary \(H:A_M\to\mathbf{Set}\), define

\[
h\sim h'
\quad\Longleftrightarrow\quad
H(f)h=H(f)h'
\text{ for some arrow }f\text{ out of their object}.
\]

Amalgamation proves transitivity and functoriality. The quotient \(H^{\mathrm{inj}}\) has injective transition maps.

The induced functor

\[
\operatorname{El}(H)\longrightarrow
\operatorname{El}(H^{\mathrm{inj}})
\]

is homotopy final. Its comma categories are reduced explicitly to nonempty full cosieves in slices, which are contractible by the preceding construction. Therefore

\[
B\operatorname{El}(H)\simeq
B\operatorname{El}(H^{\mathrm{inj}}).
\]

This establishes the reduction for noninjective actions, rather than imposing injectivity as an additional hypothesis.

### Second comparison: saturate an injective action

For an injective action \(H\), take its directed colimit over the finite closed substructures of \(M\), using inclusion maps:

\[
S=\operatorname{colim}_{B\subseteq M}H(B).
\]

The canonical maps into \(S\) are injective, and homogeneity gives \(S\) a continuous discrete \(G\)-action. Define the saturated action

\[
T_S(B)=S^{G_B}.
\]

For a closed embedding \(f:B\to C\), extend \(f\) to an automorphism of \(M\) and use its action on \(S\). This is independent of the extension because two extensions differ by an element fixing \(B\).

There is a natural inclusion

\[
H\hookrightarrow T_S.
\]

The comma category of an object of \(\operatorname{El}(T_S)\) under this inclusion is again exactly a nonempty full cosieve in a slice. Thus

\[
B\operatorname{El}(H)\simeq B\operatorname{El}(T_S).
\]

Finally, decompose \(S\) into \(G\)-orbits. Every orbit is \(G/G_F\) for a finite closed \(F\), by the open-subgroup classification. The identity

\[
\operatorname{Fix}_M(G_B)=B
\]

then yields, for \(F\neq\varnothing\),

\[
T_{G/G_F}(B)\cong A_M(F,B).
\]

Its category of elements has an initial object. For \(F=\varnothing\), the saturated action is constant one, whose category of elements is the already contractible \(A_M\).

Every component of every saturated category of elements is therefore contractible. The two proved comparisons transfer weak contractibility back to the original arbitrary action \(H\). This completes Theorem A.34.

## 3. Universal survival in the repaired AKR construction

Part C.1 is proved with its original universal quantifier:

\[
\boxed{
H_2\!\left(
B\operatorname{El}_{K^*}
\bigl(h_V/(cv_1\sim cv_2)\bigr);
\mathbb Z
\right)\neq0
}
\]

for **every admissible sequence \((a_m)\)** and **every admissible repaired target choice**.

The older selected-large-target argument remains in the paper as an independent special-case proof. The universal proof uses the actual generating covers and source histories of the construction; it does not add the selected proof’s diameter or ordering bounds.

### The central component-path estimate

Let \(G_X\) be the binary graph at an object \(X\), and put

\[
H(X)=\pi_0G_X.
\]

For an actual parallel pair \(f,g:S\rightrightarrows T\), let \(L_U(f,g)\) denote the maximum number of vertices in a nonconstant point-transition path, and define \(L_H\) analogously for component transitions.

Theorem C.27 proves both that every generated arrow is injective on binary components and that

\[
\boxed{L_H(f,g)\leq L_U(f,g)+1,}
\]

with no nontrivial component-transition cycles.

The proof is a simultaneous induction on construction stage and source generation rank. Its essential steps are:

1. The generating cover at an object’s birth has a short-interval Helly property. A pair lying in no single birth copy forces routing of the **whole actual source arrow** through a comparison image containing that pair.
2. Descent through the birth cover represents every nonempty pointwise equalizer by an actual earlier arrow image.
3. On component sets, an intersection containing at least two components is represented by an actual commuting span
   \[
   fu=gv,\qquad u,v:R\rightrightarrows S.
   \]
   For distinct \(f,g\), the source \(R\) is strictly older.
4. A component path with \(r\) vertices for \((f,g)\) becomes one with \(r-1\) vertices for the reduced pair \((v,u)\). A nontrivial component cycle becomes a cycle of the same length.
5. Every nonconstant point path for \((v,u)\) extends to a point path for \((f,g)\) with one additional distinct vertex. Source induction gives the displayed bound and excludes component cycles.

The restriction to intersections of at least two components is essential: it avoids inferring equality of underlying points from equality of a single graph component.

At a new attachment, the prescribed point-path bound is \(n\). The original C.1 inequalities give

\[
s=4k+1\geq15n,
\qquad
k\geq n+1.
\]

Therefore the component paths fit the repaired necklace construction. Its component-copy maps are injective, and proper component visibility intervals have width at most

\[
2n<s/3.
\]

That extends the routing and Helly hypotheses to the next stage, closing the induction without circularity.

### The exact attachment kernel is zero

For one repaired attachment of \(f,g:S\rightrightarrows T\), Proposition C.10 identifies the old cycle-colimit kernel as generated by classes

\[
[(g_\#-f_\#)\sigma],
\]

where \(\sigma\) joins two fixed vertices lying in one component of \(G_S\).

The fixed subgraph is the induced image of an actual old arrow. Universal component injectivity makes that fixed subgraph connected within each source component it meets. A path between the two fixed vertices can consequently be chosen inside the fixed subgraph, where \(f_\#=g_\#\). Changing the path changes the displayed expression only by the difference of the images of an old source cycle, which is already zero in the old colimit.

Thus **every attachment kernel vanishes**.

At the first stage, the two protected cycle generators give the augmentation map

\[
\mathbb Z^2\longrightarrow\mathbb Z,
\qquad
(a,b)\longmapsto a+b.
\]

Its kernel is generated by

\[
\kappa_+-\kappa_-.
\]

Every later stage preserves that class. Every finite nerve chain in the union occurs in a finite stage, so it also survives the infinite union. Corollary C.28 proves the required universal nonvanishing.

This argument proves zero attachment kernels directly. It does not require the stronger auxiliary assertion that every individual attachment link has vanishing \(H_2\).

## 4. The algebraic Leads and their precise corrections

The algebraic part retains the distinction that drives the counterexample:

\[
\text{row kernel }K
\qquad\text{versus}\qquad
\text{simultaneous annihilator }L=\bigcap_iK_i.
\]

Totality controls the row presentation. The separator realizes a nonzero obstruction in the column presentation.

| Lead | Established result |
|---|---|
| **1** | For total \(A\), the former surjection is the canonical isomorphism \(\displaystyle T_1(P_q/(K_1+K_2))\cong\mathbb Z/\varepsilon(K_1\cap K_2)\). Both derivations and their sign relation are checked. |
| **2** | Under I, exactness is equivalent to affine annihilation of every augmentation-zero \(z\). The formula \(\displaystyle T_1(P_p/P_rz)\cong\mathbb Z/\varepsilon(\operatorname{ann}z)\) is proved. Connectedness is unnecessary. |
| **3** | The column formulas hold for every small category, including \(k=0\); common successors are needed for the stated affine-equalizer criterion. |
| **4** | Both affine-equalization assertions are proved. The explanatory conclusion is qualified: exactness is not equivalent to siftedness or to injectivity of the set-to-abelian colimit comparison. |
| **5(i)** | The specified \(\kappa\) belongs to \(K\), has augmentation pair zero, and dies in \(\operatorname{colim}K\) under totality. |
| **5(ii)** | The zero-class normal form is proved under the weaker hypothesis of common successors. |
| **5(iii)** | An affine annihilator of \(\kappa\) gives a triple equalizer. A common affine equalizer of the displayed finite pairs suffices; one pair suffices by IV. |
| **5(iv)** | The kernel of \(\psi\), the derived-colimit quotient formula, and the mixed-cycle interpretation are proved. The final “1-cycle” language refers to a bar chain with module coefficients, not to nonzero ordinary \(H_1(BA)\). |

In particular, for Lead 3, with \(Q_a=\operatorname{coker}d^T\) and \(L=\ker d^T\),

\[
T_1(Q_a)\cong\mathbb Z/\varepsilon(L),
\]

\[
T_2(Q_a)\cong
\ker\!\left(\operatorname{colim}L\longrightarrow\mathbb Z\right),
\]

and

\[
T_i(Q_a)\cong T_{i-2}(L)\qquad(i\geq3).
\]

The separator clarifies the role of the expert’s class \(\kappa\). Pairwise affine equalizers exist and can be transported to a common target, so \(\kappa\) is defined. Its colimit class is zero by totality. Nevertheless, it cannot have an affine annihilator, because Lead 5(iii) would then produce the triple equalizer already excluded by A.24. Thus a zero-class normal form cannot generally be compressed into the proposed single affine annihilation.

For the remaining Leads:

- **Lead 6 is proved:** finite-poset tests, and specifically face-poset tests for triangulated spheres, characterize totality through the stated comprehensive factorization. The factorization of an arbitrary map into a category of elements is explicit.
- **Lead 7 is proved with its stated comma-contractibility hypothesis.** The dimension consequence retains that hypothesis. The unrestricted literal circle claim is false without monomorphisms; the paper supplies a completely specified three-object, eight-arrow counterexample whose relevant comma graph has \(H_1\cong\mathbb Z^6\). The monic case and the actual AKR exception are treated separately.
- **Lead 8 is proved for every nonzero unital ring.** The interval-type variance is established, \(W_2\) is explicitly identified with the wide injective-map subcategory, and the named pair fails I and affine equalization. An explicit quotient action has \(H_1\cong\mathbb Z\). The literal phrase “any ring” requires the zero-ring exception.
- **All four clauses of Lead 9 are proved:** no reverse arrow \(q\to p\), unbounded hom-sets out of \(p\), preservation of the separator and its minimal bad-family size on the full cosieve, and pairwise distinctness of ordinary postcomposites.

## 5. The strict class diagram and manuscript conclusions

The completed diagram is

\[
\boxed{
\{\text{filtered}\}
\subsetneq
\{\text{exact}\}
\subsetneq
\{\text{total}\}
\subsetneq
\{\text{quasi-filtered}\}.
}
\]

The witnesses are:

| Strict inclusion | Witness |
|---|---|
| Filtered \(\subsetneq\) exact | \(\Delta_{\mathrm{inj}}\), with the audited exactness proof and its unequalizable ordinary point pair |
| Exact \(\subsetneq\) total | The explicit ordered predimension category \(\mathcal C_\delta\) |
| Total \(\subsetneq\) quasi-filtered | A repaired AKR category; the universal theorem now covers every admissible choice |

The first example is the one announced by Isbell and Mitchell (1973, Theorem 3). The paper distinguishes that announcement from Isbell’s 1974 proof, whose original body was not obtained, and records the independent supplied proof that was actually audited.

For the manuscript:

\[
\text{totalement }W_\infty\text{-asphérique}
\Longrightarrow
\text{filtrante}
\]

is false, and **replacing “filtered” by “exact” does not repair the implication**.

The corrected additional-hypothesis statements remain

\[
A\text{ filtered}
\iff
A\text{ total and sifted},
\]

and, for every fixed \(n\geq1\),

\[
A\text{ filtered}
\iff
\left[
\begin{array}{l}
A\text{ is total, and}\\
\operatorname{hocolim}_A K(M(a),n)
\text{ is }n\text{-truncated for every }M:A\to\mathbf{Ab}.
\end{array}
\right]
\]

The finite-cocone criterion is audited against the opened Gabriel–Ulmer passages, and the earlier PRETOT/TOTEX credits are retained (Gabriel & Ulmer, 1971, §§15.2(c), 15.9).

The two specified typing corrections are also retained:

- **II ms. 36:** finality of \(f:X\to Y\) requires \(y\backslash X\). The printed \(y\backslash Y\) has the initial object \(\operatorname{id}_y\).
- **XII ms. 88:** since \(H'\) is a presheaf on \(U'\), the correctly typed element-category expression is \(U'/H'\).

The paper states the variance translation and distinguishes mathematical correction of the supplied transcription from an independent editorial collation.

## 6. Literature audit and verification

The report gives the requested source-by-source record, including precise inspected locations and unsuccessful access attempts.

| Source | Recorded access and relevant locations |
|---|---|
| Isbell–Mitchell, 1973 | Opened; Theorems 1–3 and Lemma 1 |
| Isbell–Mitchell, 1976 | Opened; §§1–4, particularly Proposition 2.3, Theorem 3.1, Proposition 3.3, the coefficient remark on p. 296, and the §4 exclusions |
| Isbell, 1968 | Opened; the unnumbered theorems in §§1–2 |
| Isbell, 1974 | Original body not obtained; publisher and JSTOR metadata inspected |
| Oberst, 1968 | Original body not obtained; publisher metadata and subscription preview inspected |
| Adámek–Reiterman, 1975 | Original body not obtained; attempted official endpoints and failures recorded |
| Adámek–Koubek–Reiterman, 1981 | Opened; B.5–B.9, C.1, and the complete C.2 induction |
| Husainov, 2002 | Opened; Theorems 2.4–2.7 and Problem 2.5 inspected |
| Gabriel–Ulmer, 1971 | Opened; §§5.2, 15.2(c), 15.9 |
| Flatness of monoid acts | Opened Hemelaer–Rogers and Laan passages; distinct meanings of flatness kept separate |
| Predimension and homotopy comparisons | Opened Evans–Hubička–Nešetřil and Goerss–Jardine passages, with exact theorem-level use recorded |

The final metadata checks preserve the unopened-body status of Isbell (1974) and Oberst (1968); they do not turn bibliographic access into theorem verification. [Annals of Mathematics](https://annals.math.princeton.edu/1974/100-3/p05?utm_source=chatgpt.com)

The proof audits and computations have explicitly different scopes. The finite bridge certificates check positivity and strict closure by exact integer min-cut calculations, including crossing endpoint images and degenerate bases. The cone certificates check the relative path inequalities, actual embeddings, composition and naturality. Those finite checks supplement the universal proofs; the all-action and all-stage quantifiers are established in the mathematical arguments.

The final document checks passed:

- LuaLaTeX compilation with **no warnings**, overfull boxes, missing characters, undefined references or citations, or duplicate labels.
- All **78 pages visually reviewed**, with additional full-page reviews of the central proofs and the final editorial changes.
- CSV readback and statement-number consistency: **89 rows**, no Open status.
- ZIP CRC and every packaged manifest hash verified.
- Both earlier checkpoint archives preserved with their original SHA-256 values.

The completed ZIP’s SHA-256 is:

```text
4865d491966465ccc8f8e0f34c7d0eff666dc2a20c0ff4ec0114796f55cfb24a
```

### Selected references

Adámek, J., Koubek, V., & Reiterman, J. (1981). Embeddings into categories with fixed points in representations. *Czechoslovak Mathematical Journal, 31*(3), 368–389. [Primary record](https://dml.cz/dmlcz/101753)

Evans, D. M., Hubička, J., & Nešetřil, J. (2019). Automorphism groups and Ramsey properties of sparse graphs. *Proceedings of the London Mathematical Society, 119*(2), 515–546. [https://doi.org/10.1112/plms.12238](https://doi.org/10.1112/plms.12238)

Gabriel, P., & Ulmer, F. (1971). *Lokal präsentierbare Kategorien* (Lecture Notes in Mathematics, Vol. 221). Springer. [https://doi.org/10.1007/BFb0059396](https://doi.org/10.1007/BFb0059396)

Goerss, P. G., & Jardine, J. F. (2009). *Simplicial homotopy theory*. Birkhäuser. [https://doi.org/10.1007/978-3-0346-0189-4](https://doi.org/10.1007/978-3-0346-0189-4)

Isbell, J. R., & Mitchell, B. (1973). Exact colimits. *Bulletin of the American Mathematical Society, 79*(5), 994–996. [https://doi.org/10.1090/S0002-9904-1973-13296-3](https://doi.org/10.1090/S0002-9904-1973-13296-3)

Isbell, J. R., & Mitchell, B. (1976). Exact colimits and fixed points. *Transactions of the American Mathematical Society, 220*, 289–298. [https://doi.org/10.1090/S0002-9947-1976-0404377-3](https://doi.org/10.1090/S0002-9947-1976-0404377-3)

*AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.*
