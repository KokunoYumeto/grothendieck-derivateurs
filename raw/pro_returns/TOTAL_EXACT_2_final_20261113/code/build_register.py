"""Build the statement CSV and report from the compiled LaTeX labels.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
Missing labels, duplicate numbers and unclassified statuses are errors.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
aux = (ROOT / "TOTEX2_paper.aux").read_text()
labels = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]+)\}", aux))
ENV = "theorem|proposition|lemma|corollary|definition|remark|obstruction|example"
pattern = re.compile(
    r"\\begin\{(" + ENV + r")\}\[([^\]]*)\](.*?)\\end\{\1\}", re.S)

def ref(label):
    if label not in labels:
        raise ValueError("Uncompiled label: " + label)
    return labels[label]

main = (ROOT / "TOTEX2_paper.tex").read_text()
paths = [ROOT / (p + ".tex") for p in re.findall(r"\\input\{([^}]+)\}", main)]
pages = {
    "FT:ty": "VII ms. 25-32",
    "A:main": "II ms. 36-36ter; XII ms. 88-89 (totality does not imply exactness)",
    "D:known-diagram": "II ms. 36-36ter; all three inclusions strict",
    "D:manuscript": "II ms. 36-36ter; XII ms. 88-89 (stated corrected implications)",
    "D:typing": "II ms. 36; XII ms. 88-89",
}
notes = {
    "A:main": "Explicit small category of positive ordered 3-uniform hypergraphs and strict closed embeddings. All covariant set actions are covered; the named triple has no affine equalizer.",
    "A:coefficients": "One total category and one triple work over every nonzero unital ring, in particular Q and every F_p. The column cokernel has projective dimension exactly one and T1=R.",
    "A:fieldwise": "All small categories; no totality assumption. Reduction, not a decision of the main question.",
    "A:uniform-finite-coefficients": "A single uniform bound on the cardinalities is essential. Quasi-filteredness gives T1 vanishing; totality gives all positive degrees. Unbounded finite-valued diagrams are not covered.",
    "A:predimension-amalgam": "Finite ordered simple 3-uniform hypergraphs, delta=2|V|-3|E|, strict d-closed induced embeddings. Closure, composition and free amalgamation proved directly.",
    "A:predimension-necklace": "Explicit bound s>(2n-2)(delta(T)+2|S|); proof counts first-appearance indices, and proves inducedness and strict relative positivity for every subset.",
    "A:predimension-quasi": "Both the full positive-predimension category and its full point-and-edge-closed subcategory; all parallel pairs.",
    "A:predimension-triple": "Actual representable arrows only, arbitrary nonzero unital coefficient rings. The column is injective and T1 of its cokernel equals the coefficient ring.",
    "A:predimension-alternating-bridge": "Finite explicit bridge for arbitrary closed endpoint embeddings agreeing on B intersection C; all-subset predimension and order bounds proved, including degenerate bases.",
    "A:predimension-stabilizers": "The generated subgroup of pointwise stabilizers of B and C equals the pointwise stabilizer of their intersection.",
    "A:predimension-open-subgroups": "Every open subgroup is the pointwise stabilizer of a finite closed set, possibly empty; finite order eliminates the setwise/pointwise ambiguity.",
    "A:predimension-stabilizer-criterion": "Arbitrary set actions: eventual-equality quotient and smooth-action saturation are homotopy final. No finiteness or injectivity restriction remains.",
    "A:predimension-total": "Both full ordered positive-predimension categories are total and nonexact over every nonzero unital ring. Complete separator theorem; independently audited.",
    "A:P1-torsion": "Four objects and seventeen arrows with a terminal object. Q_a(x)=Z^2 plus Z/3. Alternative modules with the same T1 are not excluded.",
    "B:P1-rational": "Four-object category with terminal object and one infinite-cyclic automorphism group. Rational obstruction and integral torsion-free strengthening; the even-power invariant includes tensor-permutation closure. Not a separator.",
    "B:lead1": "Both derivations checked, including the sign between their explicit maps.",
    "B:triple-question": "Refuted by the same total category and its three closed point arrows. Three is the smallest possible obstructing ordinary family size.",
    "B:lead2": "The Tor formula requires augmentation zero; I is required for the criterion, connectedness is not.",
    "B:lead3": "No category hypothesis for the formulas; common successors for the equalizer criterion; k=0 included.",
    "B:lead4-scope": "Exactness is not equivalent to siftedness or injectivity of the set-to-abelian comparison.",
    "B:zero-normal-form": "Common successors suffice.",
    "B:mixed-cycle-obstruction": "A bar chain with module coefficients is intended, not nonzero H1 of BA.",
    "C:survival-question": "Every admissible repaired C.1 construction. Every attachment preserves the old binary cycle colimit; the first-stage H2 generator survives the infinite union.",
    "C:component-two-intersection": "The intersection is represented by an actual commuting span; at least two components are essential to avoid the singleton point-lifting defect.",
    "C:component-path-inflation": "Simultaneous source induction: no component cycles and L_H(f,g) <= L_U(f,g)+1, with exact path vertex counts.",
    "C:universal-components": "Every admissible C.1 choice; s>=15n and k>=n+1 suffice. No selected size, convexity or ordering bound is added.",
    "C:universal-nontotal": "Nonzero binary H2 in the infinite union for every admissible repaired construction. Three independent mathematical audits passed.",
    "C:akr-all-rings": "Every admissible repaired construction, arbitrary abelian-group coefficients.",
    "C:nonmonic-circle-counterexample": "Three objects, eight arrows; comma graph H1=Z^6.",
    "C:split-monic-counterexample": "Quasi-filtered AKR, finite free values, split injections, T1=Z; totality not asserted.",
    "C:protected-cycles": "All-stage pointwise and relative result; not injectivity after taking colimit.",
    "C:freefactor-nerve": "Finite parallel-pair index, not quasi-filtered. Free values and free-factor transitions do not make the ordinary nerve colimit aspherical.",
    "C:fixed-path-kernel": "Every repaired attachment with prescribed covered target. Exact kernel formula; no all-stage vanishing inferred.",
    "C:beta-fixed-subsets": "Exact prefix/suffix classification for every actual point path size and k at least the common bound; at most 2L-1 subsets.",
    "C:beta-small-overlap": "Component injections and point-image overlap at most one imply the stated next-copy fixed-set criterion.",
    "C:protected-nonadjacent": "All admissible stages: a proper protected-circle overlap is empty, a vertex, or one edge.",
    "C:protected-two-images": "Objectwise two-image saturation over every abelian coefficient group; no colimit saturation inferred.",
    "C:large-target-convexity": "Strong geodesic convexity follows from the explicit strict diameter/visibility bound; component injection is proved separately.",
    "C:ordered-necklace": "All sufficiently large k, with a terminating finite choice procedure; no assertion at every smaller admissible k.",
    "C:ordered-necklace-short-warning": "Increasing maps with point paths of size two can force an order cycle at numerically admissible n=3, k=11. The pair is not shown to occur among actual generated C.1 arrows.",
    "C:local-convexity": "All actual C.1 arrows, all admissible choices. An outside simple excursion of length r satisfies (2-a_m)r>=1; in particular all images are two-convex.",
    "C:small-diameter-source": "Source component diameters at most the explicit local radius suffice; no component-injectivity hypothesis is used.",
    "C:first-stage-safe-sources": "Every later attachment from a source already in K1 preserves the old binary cycle colimit. The separate universal component theorem extends preservation to all later-born sources.",
    "C:selected-nontotal": "Every admissible a-sequence admits selected large targets with persistent binary H2. A deterministic countable example is specified. This earlier geometric proof is retained separately from the universal component proof.",
    "C:generic-component-warning": "Generic repaired graph gluing only; not shown to occur in C.1.",
    "C:connected-convex-warning": "Connected source and target, all old images strongly convex, point paths of size two, and numerically admissible s=45. A 46-edge path shortens to 45; no realization as actual C.1 arrows is claimed.",
    "CD:bounded-fibres": "One uniform finite size bound; unbounded fibres not covered.",
    "CD:pinning-counterexample": "An exact total category can lose an original set-colimit relation after passage to a component of elements that fixes a coefficient.",
    "CC:positive-gap": "All admissible repaired AKR categories and the total predimension category; probability combinations have total marginal discrepancy at least one.",
    "CC:convex-counterexample": "The predimension example is total. Nonempty finite-dimensional compact convex potential sets can have empty strict inverse limit even under totality.",
    "CD:unresolved": "The former missing implication is false: total C_delta is nonexact and therefore cannot satisfy the equivalent compact/Ramsey conditions.",
    "FT:ty": "Every nonzero unital ring; zero ring refutes literal any-ring wording.",
    "D:typing": "Mathematical correction to supplied transcription; no new editorial collation.",
}
rows = []
for path in paths:
    tex = path.read_text()
    matches = list(pattern.finditer(tex))
    for i, match in enumerate(matches):
        env, heading, body = match.groups()
        found = re.findall(r"\\label\{([^}]+)\}", body)
        if not found:
            raise ValueError("Numbered statement without label: " + heading)
        label = found[0]
        status = next((s for s in ("Open", "Proved", "Refuted", "Known")
                       if heading.startswith(s)), None)
        if status is None:
            raise ValueError("Unclassified statement: " + heading)
        end = matches[i+1].start() if i+1 < len(matches) else len(tex)
        following = tex[match.end():end]
        deps = sorted(set(re.findall(r"\\ref\{([^}]+)\}", body + following)) - {label})
        cites = sorted(set(re.findall(
            r"\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}", body + following)))
        statement = re.sub(r"\\label\{[^}]+\}", "", body).strip()
        statement = re.sub(r"[ \t]+", " ", statement)
        rows.append({
            "id": ref(label),
            "statement": statement,
            "status": status,
            "where_proved": ("Not proved; " if status == "Open" else "")
                + str(path.relative_to(ROOT)) + " [" + label + "]",
            "depends_on": "; ".join(
                [ref(x) + " [" + x + "]" for x in deps] + ["Source: " + c for c in cites]),
            "manuscript_pages_settled": pages.get(label, ""),
            "notes": notes.get(label, heading) + " Stable label: " + label,
        })
assert len({r["id"] for r in rows}) == len(rows), "Duplicate statement number"
fields = ["id", "statement", "status", "where_proved", "depends_on",
          "manuscript_pages_settled", "notes"]
with (ROOT / "TOTEX2_results.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

outcomes = [
("A.1", "Refuted", "A:main A:predimension-total", "Explicit total ordered predimension category with a triple having no affine equalizer."),
("A.2: Q", "Refuted", "A:coefficients A:predimension-triple", "The same separator has a projective-dimension-one rational diagram with T1=Q."),
("A.2: every F_p", "Refuted for each prime", "A:coefficients A:predimension-triple", "The same category and triple work simultaneously for every prime, with T1=F_p."),
("B.1: triples", "Refuted", "B:triple-question B:lead3", "The three point arrows into one hyperedge are the smallest possible obstructing ordinary family."),
("B.2: Leads 1-5", "Proved / corrected", "B:lead1 B:lead2 B:lead3 B:lead4 B:lead5", "Formal claims proved; explanatory overstatements corrected."),
("C.1: AKR H_2", "Proved", "C:survival-question C:universal-components C:universal-nontotal", "Every admissible repaired construction preserves the first-stage binary H2 class through the infinite union."),
("C.2: Leads 6-9", "Proved / refuted as worded", "FT:finite-test C:link-comparison C:nonmonic-circle-counterexample FT:ty FT:minimal-family", "Corrected claims proved; literal nonmonic-circle and any-ring assertions refuted."),
("D.1: both right-hand inclusions", "Proved strict", "D:known-diagram A:predimension-total C:selected-nontotal", "All three inclusions are strict, with explicit witnesses."),
("D.2: manuscript corrections", "Proved / conjectures refuted", "D:manuscript D:truncation D:typing", "The filteredness conjecture and its exactness replacement are false; corrected added-hypothesis criteria and typing repairs are given."),
("D.3: literature record", "Completed", "", "Verified opened passages, exact theorem locations, failed body retrievals and main-question searches are individually listed."),
("Lead 1", "Proved", "B:lead1", "Canonical isomorphism and both derivations."),
("Lead 2", "Proved", "B:lead2", "One-relator criterion and Tor formula."),
("Lead 3", "Proved", "B:lead3", "All small categories, including k=0."),
("Lead 4", "Proved; final gloss qualified", "B:lead4 B:lead4-scope", "Exactness is not siftedness or injectivity of the set-to-abelian comparison."),
("Lead 5(i)", "Proved", "B:lead5", "Membership and vanishing of the colimit class of kappa."),
("Lead 5(ii)", "Proved in stronger form", "B:zero-normal-form", "Common successors suffice."),
("Lead 5(iii)", "Proved", "B:lead5", "Affine annihilation gives a triple equalizer; a common affine equalizer of the displayed finite pairs suffices, and one pair suffices by IV."),
("Lead 5(iv)", "Proved", "B:lead5 B:mixed-cycle-obstruction", "Kernel, Tor quotient and mixed-cycle interpretation."),
("Lead 6", "Proved", "FT:sphere-representatives FT:finite-test", "Finite-poset and sphere-face tests with explicit factorization."),
("Lead 7", "Proved with its stated hypothesis; literal circle claim refuted", "C:link-comparison C:link-obstruction C:nonmonic-circle-counterexample", "The comparison and dimension consequence are proved in full under the specified comma-contractibility hypothesis."),
("Lead 8", "Proved for nonzero rings; literal any-ring claim refuted", "FT:ty", "Ty^op fails I, IV and totality; zero ring exceptional."),
("Lead 9(a)", "Proved", "FT:minimal-family", "No reverse arrow q to p."),
("Lead 9(b)", "Proved", "FT:minimal-family", "Unbounded hom-sets out of p."),
("Lead 9(c)", "Proved", "FT:minimal-family", "Full cosieve remains a separator with the same minimal family size."),
("Lead 9(d)", "Proved", "FT:minimal-family", "Ordinary postcomposites remain pairwise distinct."),
]
header = ["| Item | State | Statements | Exact scope |",
          "|---|---|---|---|"]
if any(row["status"] == "Open" for row in rows):
    header = ["INCOMPLETE", ""] + header
for item, state, ls, scope in outcomes:
    nums = ", ".join(ref(x) for x in ls.split()) or "Access table"
    header.append("| " + " | ".join((item, state, nums, scope)) + " |")
report = "\n".join(header) + "\n\n" + (ROOT/"notes/report_body.md").read_text()
report += "\n\n" + (ROOT/"notes/literature.md").read_text()
(ROOT / "TOTEX2_report.md").write_text(report, encoding="utf-8")
print("Statement rows:", len(rows))
print("Statuses:", {s: sum(r["status"] == s for r in rows)
                    for s in ("Proved", "Refuted", "Known", "Open")})
with (ROOT/"TOTEX2_results.csv").open() as f:
    print("CSV readback rows:", len(list(csv.DictReader(f))))
print("Report first line:", report.splitlines()[0])
print("Outcome rows:", len(outcomes))
