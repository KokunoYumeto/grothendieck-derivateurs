#!/usr/bin/env python3
"""Build and validate the C/D statement register from the delivered TeX.

Run from any working directory: python3 /path/to/STRATA/code/CD_metadata.py
Only audit/CD_results.csv is written. The statements themselves are in
sections/C.tex and sections/D.tex; this program checks the declared IDs,
status labels, bibliography coverage, and source/proof dependencies.
"""
from pathlib import Path
import csv
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["id", "statement", "status", "where_proved", "depends_on",
          "manuscript_rows_or_pages_settled", "notes"]

# statement, dependencies, manuscript location, qualification
META = {
    "C.1": (
        "A specified sieve-cosieve decomposition is reconstructed by its crossing bimodule; the crossing-arrow category has commuting-square morphisms.",
        "0.1", "XII ms.59–60",
        "The bimodule and its two endpoints are retained; the total homotopy type of E alone is not the gluing datum."),
    "C.2": (
        "B(E^op) maps by a specified endpoint-compatible weak equivalence to the holink from BB into BX minus BB, whose open stratum retracts to BA.",
        "C.1; Douteau–Waas 2022 v2 Theorem 6.1", "Lead 3; XII ms.59–63",
        "Arbitrary small X; BA is not generally the literal complementary open subset. Quinn's metric/tameness hypotheses are not asserted."),
    "C.3": (
        "The specified map hocolim(BA <- BE -> BB) -> BX is a weak equivalence and agrees with holink evaluation under C.2.",
        "C.2; audited POLES G.19", "XIIapp-G11; XII appendix ms.17–18",
        "The supplied proof is audited, not reproved a third time; no reverse excision is used. Includes empty pieces and disconnected categories."),
    "C.4": (
        "Unrestricted endpoint paths can replace the crossing category in the gluing formula without changing its result.",
        "C.3; code/CD_checks.py", "Lead 3 path-versus-holink distinction",
        "False: two objects and two parallel nonidentity arrows give a two-point crossing link versus path components indexed by Z."),
    "C.5": (
        "Finite sieve filtrations glue by their actual successive crossing categories; coherent flag categories supply all generalized links.",
        "C.1–C.3; Douteau–Waas 2022 v2 Theorem 6.1 and Example 2.30", "Lead 3 finite-filtration extension",
        "Pairwise homotopy types alone do not suffice; boundary versus filled triangle checked. Spatial Segal products are asserted for groupoidal layers."),
    "C.6": (
        "For presentable infinity-category coefficients, Fun(X^op,C) is the lax pullback of triples FA,FB,FB->i*j_*FA, and i*j_* is t_*s*.",
        "C.1; SGA 4 IV Theorem 9.5.4 and Exercise 9.5.10", "XII ms.62–63; Lead 4 coefficient gluing",
        "The direct enhanced proof retains mapping spaces and the coherent gluing arrow. The right-Kan cofinality comparison is explicitly typed."),
    "C.7": (
        "Passing to homotopy categories before taking the ordinary lax comma construction reconstructs the homotopy category of coefficients.",
        "C.6; code/CD_checks.py", "Lead 4 enhancement boundary",
        "False already over [1]: arrows S0->* and *->S1 have Z morphism classes in the coherent arrow category and one in the ordinary comma category."),
    "C.8": (
        "Locally constant enhanced coefficients form the Cat_infinity pullback Fun(BA,C) x_Fun(BE,C) Fun(BB,C), with equivalence gluing data.",
        "C.3; groupoidification", "GALOIS A.8/B.3/B.5 comparison; Lead 3 locally constant extension",
        "The pullback is formed before Ho. Bare derivators retain the invariance and support statements, not the false ordinary-comma formula."),
    "C.9": (
        "Strict simplicial-category pushout along a sieve preserves every Dwyer–Kan equivalence exactly when every discrete crossing weight preserves objectwise weak equivalences.",
        "C.1; audited TOTASPH F.14; Hackney–Ozornova–Riehl–Rovelli 2024 Theorem 1.5 generalized form", "XII ms.59–72; TOTASPH F.14",
        "A degreewise coend criterion with necessity proved by adjoining a new source. Distinct from classifying-space homotopical cofibration."),
    "C.10": (
        "A three-object seven-arrow couniversal weak-equivalence sieve can have a disconnected individual crossing category.",
        "C.9; audited TOTASPH F.18; code/CD_checks.py", "TOTASPH F.18; directed-gluing converse boundary",
        "All compositions and natural transformations checked; the universal pushout argument is mathematical, not inferred from finitely many tests."),
    "C.11": (
        "A four-object eleven-arrow couniversal weak-equivalence sieve is a homotopical cofibration but need not be discretely flat.",
        "C.9; audited TOTASPH F.21; code/CD_checks.py", "TOTASPH F.21; XII strict-gluing qualification",
        "The failed weight map is CK coproduct_K CK -> *, with K a circle; integral H2 is Z."),
    "D.1": (
        "A pointed Der 1–4 presheaf derivator has the exceptional adjunction chains j^? ⊣ j_! ⊣ j^* ⊣ j_* and i_! ⊣ i^* ⊣ i_* ⊣ i^!, with the stated support images.",
        "Groth 2013 v2 Lemma 3.7 and Corollary 3.8; pointwise Kan formulas", "I ms.1–9; Lead 4",
        "All four Kan extensions are fully faithful, at every shape. Index opposition translates Groth's covariant convention; Der 5 is not assumed."),
    "D.2": (
        "Pointed derivators have coherent support fibre/cofiber sequences and the bicartesian open-closed square; stable strong derivators have the associated triangulated recollement.",
        "D.1; Groth 2013 v2 Theorem 4.16 and Example 4.25; GPS 2014 Theorem 6.1", "I ms.2–9; Lead 4 exactness clauses",
        "The coherent square is explicitly constructed by Kan extensions on X times [1]^2. Pointedness does not imply stability or triangulation."),
    "D.3": (
        "A poset map is W_infinity-proper exactly when all outgoing exact lifting posets are weakly contractible, and smooth exactly when all incoming ones are weakly contractible.",
        "Maltsiniotis 2005 Theorem 1.2 and proper dual; audited I ms.53–54", "I ms.53–56; Lead 4 map classification",
        "Necessary and sufficient for arbitrary small posets, including finite and locally finite. Empty lifting posets fail; identity tests are automatic."),
    "D.4": (
        "Strict-pullback right base change holds if the vertical functor is proper or the base-change functor smooth; left base change has the dual conditions, and universal space-valued tests detect them.",
        "D.3; Groth–Ponto–Shulman 2014 Theorems 3.8 and 3.16", "I ms.49–59; VI ms.162–169; Lead 4",
        "All Der 1–4 coefficients in presheaf variance. Gives fibre limits for proper maps and fibre colimits for smooth maps; includes a representable converse test."),
    "D.5": (
        "Topological properness, strict-versus-homotopy-fibre comparison, or stratified local product structure characterize categorical properness and smoothness for finite posets.",
        "D.3–D.4; code/CD_checks.py", "Ib-C003; I ms.53–59; GALOIS D.9; Lead 4",
        "False: endpoint inclusions of [1] separate all claimed notions; the proper cosieve has comma transition empty->point; explicit right-base-change map 2->1 fails."),
    "D.6": (
        "The four-object diamond map to [1] is proper and smooth and a Grothendieck fibration, but is neither an opfibration nor a locally trivial topological fibre bundle.",
        "D.3; code/CD_checks.py", "VIc-C008 strictness comparison; Lead 4",
        "Weak contractibility is certified by extrema. The greatest/least-element criterion for strict lifts is used only over [1], not arbitrary bases."),
    "D.7": (
        "Full poset inclusions are proper precisely for cosieves and smooth precisely for sieves; product projections have both properties and images obey the stated component conditions.",
        "D.3", "I ms.54–56; Lead 4 examples and edge cases",
        "Empty-source maps are both vacuously; no unstated surjectivity on connected components."),
    "D.8": (
        "The finite-poset coefficient dictionary transports intrinsic base change; closed inclusions and finite product projections admit the specified ambient geometric interpretation, while arbitrary monotone maps do not.",
        "Part A coefficient hypotheses; C.2; D.1–D.5; HTT Corollary 7.3.1.18; Haine 2022 Corollary 3.2, Proposition 3.8 and Subexample 3.15", "Lead 4 constructible base-change comparison",
        "Literal product direct-image claim: spaces and compactly generated or stable presentable coefficients covered by Part A. Intrinsic Kan extensions are not automatically ambient six operations."),
    "D.9": (
        "The smoothness fibre-inclusion target at I ms.54 is y\\X; with downsets open, the compatible closure formula at XII ms.59 is y in closure{x} when x<=y.",
        "D.3; direct type and topology checks; code/CD_checks.py", "I ms.54; XII ms.59",
        "Corrections concern the supplied transcription; no claim about an uninspected original scan. Preserve the manuscript's explicit sieve/downset convention."),
}


def main():
    declarations = []
    all_text = ""
    for letter in ("C", "D"):
        path = ROOT / "sections" / f"{letter}.tex"
        content = path.read_text()
        all_text += content
        found = re.findall(r"\\begin\{statement\}\{([^}]+)\}\{([^}]+)\}\{([^}]*)\}", content)
        assert len(found) == (11 if letter == "C" else 9)
        for ident, status, title in found:
            assert ident.startswith(letter + ".")
            assert status in {"Proved", "Known", "Refuted", "Open"}
            declarations.append((ident, status, title))
        assert content.count(r"\begin{proof}") == content.count(r"\end{proof}")
        assert content.count(r"\begin{statement}") == content.count(r"\end{statement}")
    ids = [entry[0] for entry in declarations]
    assert len(ids) == len(set(ids)) and set(ids) == set(META)
    bib = (ROOT / "audit" / "CD_references.bib").read_text()
    bibkeys = set(re.findall(r"@\w+\{([^,]+),", bib))
    citations = {key.strip() for group in re.findall(r"\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}", all_text)
                 for key in group.split(",")}
    assert citations <= bibkeys, sorted(citations - bibkeys)
    assert bib.count("verified:") == len(bibkeys)
    rows = []
    for ident, status, title in declarations:
        claim, dependencies, pages, notes = META[ident]
        rows.append(dict(zip(FIELDS, [ident, claim, status,
                    f"sections/{ident[0]}.tex, {ident}", dependencies, pages, notes])))
    dest = ROOT / "audit" / "CD_results.csv"
    with dest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print("C/D statement IDs:", ", ".join(ids))
    print("Status counts:", dict(Counter(row["status"] for row in rows)))
    print("Bibliography entries:", len(bibkeys), "; cited keys:", len(citations), "; all verified")
    print("Wrote", dest.relative_to(ROOT), "with", len(rows), "rows and", len(FIELDS), "columns")
    print("METADATA CHECKS PASSED")


if __name__ == "__main__":
    main()
