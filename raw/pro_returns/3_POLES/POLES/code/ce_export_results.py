#!/usr/bin/env python3
"""Export exact numbered C/E claim statements and their audit metadata."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
META = {
    "C.1": ("", "XVI ms. 17', 91, 119-121; Part C", "Unreduced E-homology; all small spectra, including zero and nonconnective spectra; all unital rings, not assumed commutative; n >= 0. Verified Cisinski existence theorems are used."),
    "C.2": ("C.1", "XVI Loc (4), (5), (8), (9); ms. 74-78", "Nonzero generalized homology detects the number of components without a connectivity hypothesis on E. Empty families and empty sources included."),
    "C.3": ("B.2; C.1", "XVI ms. 17'; XII W(7); Loc (6 a,b,c)", "Spectral cofiber-sequence proof for E. Finite face-poset/suspension cubes refute 6b and 6c for every finite n >= 0; executable checks n = 0,1,2,3."),
    "C.4": ("C.2", "Part C homological intrinsic fibrations", "Free-group classifying spaces are null for every E-aspherical object when E is nonzero; no hypothesis on E's homotopy degrees."),
    "C.5": ("C.4; E.2; F.8", "XVI ms. 91, 119-121; Loc (7 F) for homology", "Every nonzero spectrum fails 7F, using a non-surjective free-group endomorphism inducing the identity on stable suspension spectra. All nonzero unital coefficient rings included."),
    "C.6": ("C.2; C.5; E.4; A.13", "XVI footnote 36; ms. 68-70, 91; Loc (7), (7 D)", "Explicit perfect groupoid replacement for homology; perfect model of * -> K(Z,n+1) for truncations. Failure already at the weakest reference localizer W_infinity."),
    "C.7": ("C.1; C.2; C.3; C.5; C.6; E.2", "Part C full ten-column table; XVI ms. 17', 91, 119-121", "Homology: all columns except 7,7D,7F hold for E != 0. Truncation: 6b,6c,7,7D fail, 7F holds. The zero theory is total and fails only Loc 5."),
    "C.8": ("C.2", "XVI ms. 68-70, 91; Fib_W0", "Exact intrinsic description by connected strict fibers within each total component and existence of an arrow lift in each such component; includes empty components and endomorphisms."),
    "C.9": ("C.1; A.8; A.9", "XVI ms. 91, 119-121; Fib_Wn and Loc (7 F)", "Exact canonical truncated-pullback criterion for every base change. Cisinski Proposition 6.2.3 supplies the same criterion under the verified properness hypothesis."),
    "C.10": ("C.1; C.2; C.5; F.8", "XVI ms. 91, 119-121; bounds for Fib_WE", "Lower classes: products, component inclusions, closure operations and simplicial E-sharp nerves. Upper class Q_E tests every vertex of every finite ordinal; explicit three-sheeted cover makes the upper inclusion strict for every nonzero E. Exact set-sized testing criterion also supplied."),
    "C.11": ("B.2; B.4", "TOTASPH F.25,F.28-F.30; XII ms. 228-234; Loc (6 A)", "All functors are W0-cofibrations. For W >= W1, all object injections are W-cofibrations and enough cofibrations follow. Endpoint-product and pushout-product operations remain distinct; see H.6 for the latter's obstruction."),
    "E.1": ("C.1", "Lead 5; Part E accessible convention", "No reflector is assumed for nonaccessible classes. Local limits are ambient limits, whereas local colimits are reflected ambient colimits."),
    "E.2": ("A.8; A.9; E.1", "XVI Loc (7 F), ms. 39, 91, 119-121", "7F iff aspherical generation iff set nullification iff right proper simplicial/Thomason localization. Necessity of aspherical generation does not need accessibility."),
    "E.3": ("E.1; E.2", "Lead 5; RSS/ABFJ modality dictionary", "7F iff accessible nullification iff modality iff locally cartesian reflection iff local category is LCC, specifically for reflective subcategories of spaces. Monodromy is retained in the homotopy-limit proof. Intrinsic Cat fibrations are not identified with the modality's right class."),
    "E.4": ("A.8; A.13; B.1", "XVI ms. 28-29, 89-90; Loc (7 D_Winfty)", "Equivalence with arbitrary homotopy-pullback stability, without accessibility of W. Perfect factorization uses the accessible minimal localizer W_infinity only. Cisinski 5.3.14, 6.4.14 and 6.2.3 verify the model transfer."),
    "E.5": ("E.4; B.1; A.13; A.14", "XVI Theorem 6.1, ms. 83; section 4.4 eight variants", "All eight modern fibration variants have only W_infinity and the total class as solutions, even without accessibility. Loc 5 excludes the total class."),
    "E.6": ("E.1; E.3; E.4; E.5", "Lead 5; XVI Theorem 6.1", "7 and weakest 7D are equivalent to left exactness in the accessible setting. Spaces have exactly two reflective lex localizations. Finite truncation is modal and LCC but not lex."),
    "E.7": ("E.3; E.6", "XII ms. 178-187; footnotes 116-117; final assertion on ms. 187", "Full local-coefficient proof of a_n subset b_n subset c_n subset a_(n-1); b2=c2 corrects strictness. a_n is universal b_n and fails 2/3, so b_n defines W_n. Whitehead attaching maps prove strictness for n >= 3; finite cellular checks n = 3,...,8."),
}

rows = []
for part in ("C", "E"):
    text = (ROOT / "sections" / f"{part}.tex").read_text()
    headers = re.finditer(r"\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{", text)
    for header in headers:
        identifier, status = header.groups()
        title_start = header.end()
        depth = 1
        title_end = title_start
        while depth:
            if text[title_end] == "{":
                depth += 1
            elif text[title_end] == "}":
                depth -= 1
            title_end += 1
        title = text[title_start:title_end - 1]
        body_end = text.index(r"\end{claim}", title_end)
        body = text[title_end:body_end]
        dependencies, locations, notes = META[identifier]
        rows.append({
            "id": identifier,
            "statement": re.sub(r"\s+", " ", title + " " + body).strip(),
            "status": status,
            "where_proved": f"POLES_paper.tex, Part {part}, {identifier}",
            "depends_on": dependencies,
            "manuscript_rows_or_pages_settled": locations,
            "notes": notes,
        })
assert {r["id"] for r in rows} == set(META)
destination = ROOT / "research" / "CE_results.json"
destination.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"claims_exported": len(rows), "destination": "research/CE_results.json",
                  "claim_ids": [r["id"] for r in rows]}, indent=2))
