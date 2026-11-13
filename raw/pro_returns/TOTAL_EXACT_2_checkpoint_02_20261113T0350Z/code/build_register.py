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
    "D:known-diagram": "II ms. 36-36ter; strict first and last inclusions, middle comparison unresolved",
    "D:manuscript": "II ms. 36-36ter; XII ms. 88-89 (stated corrected implications)",
    "D:typing": "II ms. 36; XII ms. 88-89",
}
notes = {
    "A:main": "No proof or counterexample; three ordinary arrows are the least unresolved family size.",
    "A:fieldwise": "All small categories; no totality assumption. Reduction, not a decision of the main question.",
    "A:P1-torsion": "Four objects and seventeen arrows with a terminal object. Q_a(x)=Z^2 plus Z/3. Alternative modules with the same T1 are not excluded.",
    "B:P1-rational": "Four-object category with terminal object and one infinite-cyclic automorphism group. Rational obstruction and integral torsion-free strengthening; the even-power invariant includes tensor-permutation closure. Not a separator.",
    "B:lead1": "Both derivations checked, including the sign between their explicit maps.",
    "B:lead2": "The Tor formula requires augmentation zero; I is required for the criterion, connectedness is not.",
    "B:lead3": "No category hypothesis for the formulas; common successors for the equalizer criterion; k=0 included.",
    "B:lead4-scope": "Exactness is not equivalent to siftedness or injectivity of the set-to-abelian comparison.",
    "B:zero-normal-form": "Common successors suffice.",
    "B:mixed-cycle-obstruction": "A bar chain with module coefficients is intended, not nonzero H1 of BA.",
    "C:survival-question": "Universal admissible-choice survival remains unresolved. Selected sufficiently large targets have proved infinite-stage survival.",
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
    "C:selected-nontotal": "Every admissible a-sequence admits selected large targets with persistent binary H2. A deterministic countable example is specified. Decides total strictly contained in quasi-filtered, not universal C.1 or A.1.",
    "C:generic-component-warning": "Generic repaired graph gluing only; not shown to occur in C.1.",
    "C:connected-convex-warning": "Connected source and target, all old images strongly convex, point paths of size two, and numerically admissible s=45. A 46-edge path shortens to 45; no realization as actual C.1 arrows is claimed.",
    "CD:bounded-fibres": "One uniform finite size bound; unbounded fibres not covered.",
    "CD:pinning-counterexample": "An exact total category can lose an original set-colimit relation after passage to a component of elements that fixes a coefficient.",
    "CC:positive-gap": "All admissible repaired AKR categories; probability combinations have total marginal discrepancy at least one.",
    "CC:convex-counterexample": "Quasi-filtered example only; neither totality nor its failure is asserted.",
    "FT:ty": "Nonzero commutative rings only; zero ring refutes literal any-ring wording.",
    "D:undecided-inclusions": "Only exact versus total remains unresolved; total is strictly contained in quasi-filtered.",
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
("A.1", "Open", "A:main A:fieldwise", "No universal proof or separator."),
("A.2: Q", "Open", "A:coefficients A:fieldwise", "Coefficient implication not decided."),
("A.2: every F_p", "Open", "A:coefficients A:fieldwise", "With Q, equivalent to the integral question."),
("B.1: triples", "Open", "B:triple-question B:lead3", "First undecided ordinary family size."),
("B.2: Leads 1-5", "Proved / corrected", "B:lead1 B:lead2 B:lead3 B:lead4 B:lead5", "Formal claims proved; explanatory overstatements corrected."),
("C.1: AKR H_2", "Open", "C:survival-question C:fixed-path-kernel C:selected-nontotal", "Selected large choices have infinite-stage survival; the universal admissible-choice assertion remains unresolved."),
("C.2: Leads 6-9", "Proved / refuted as worded", "FT:finite-test C:link-comparison C:nonmonic-circle-counterexample FT:ty FT:minimal-family", "Corrected claims proved; literal nonmonic-circle and any-ring assertions refuted."),
("D.1: both right-hand inclusions", "Open", "D:known-diagram C:selected-nontotal D:undecided-inclusions", "Total is strictly contained in quasi-filtered. Exact versus total remains unresolved, so the combined item is unfinished."),
("D.2: manuscript corrections", "Proved within stated scope", "D:manuscript D:truncation D:typing", "Known corrections audited; an exactness replacement still depends on A.1."),
("D.3: literature record", "Recorded", "", "Opened passages and failed body retrievals are individually listed."),
("Lead 1", "Proved", "B:lead1", "Canonical isomorphism and both derivations."),
("Lead 2", "Proved", "B:lead2", "One-relator criterion and Tor formula."),
("Lead 3", "Proved", "B:lead3", "All small categories, including k=0."),
("Lead 4", "Proved; final gloss qualified", "B:lead4 B:lead4-scope", "Exactness is not siftedness or injectivity of the set-to-abelian comparison."),
("Lead 5(i)", "Proved", "B:lead5", "Membership and vanishing of the colimit class of kappa."),
("Lead 5(ii)", "Proved in stronger form", "B:zero-normal-form", "Common successors suffice."),
("Lead 5(iii)", "Proved", "B:lead5", "Affine annihilation gives a triple equalizer; joint annihilation still needed."),
("Lead 5(iv)", "Proved", "B:lead5 B:mixed-cycle-obstruction", "Kernel, Tor quotient and mixed-cycle interpretation."),
("Lead 6", "Proved", "FT:sphere-representatives FT:finite-test", "Finite-poset and sphere-face tests with explicit factorization."),
("Lead 7", "Proved conditionally; literal circle claim refuted", "C:link-comparison C:link-obstruction C:nonmonic-circle-counterexample", "The dimension consequence retains its hypothesis."),
("Lead 8", "Proved for nonzero rings; literal any-ring claim refuted", "FT:ty", "Ty^op fails I, IV and totality; zero ring exceptional."),
("Lead 9(a)", "Proved", "FT:minimal-family", "No reverse arrow q to p."),
("Lead 9(b)", "Proved", "FT:minimal-family", "Unbounded hom-sets out of p."),
("Lead 9(c)", "Proved", "FT:minimal-family", "Full cosieve remains a separator with the same minimal family size."),
("Lead 9(d)", "Proved", "FT:minimal-family", "Ordinary postcomposites remain pairwise distinct."),
]
header = ["INCOMPLETE", "",
          "| Item | State | Statements | Exact scope |",
          "|---|---|---|---|"]
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
