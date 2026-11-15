"""Build and check the exact one-row-per-numbered-assertion CSV register."""
from collections import Counter
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["id", "statement", "status", "where_proved", "depends_on",
          "manuscript_rows_or_pages_settled", "notes"]

# Root-owned statements. The full mathematical statement is read from TeX;
# these records supply the dependencies, manuscript locations, and scope notes.
root_data = [
("A.1", "Proved", "", "I ms.96-100,106,113; Lead1", "Definitions for a prederivator; Der1--4 and exact presheaf variance separately stated. No strongness assumed."),
("A.2", "Proved", "A.1; Cisinski2009 Cor3.8", "I ms.96-126; Lead1", "Both local (co)homological classes separately imply constant equivalence; all-derivator first inclusion."),
("A.3", "Proved", "A.1", "I ms.99; CATHOT afterword", "Corrects the reversed acyclic-group projection example for every prederivator, including the empty source."),
("A.4", "Proved", "A.1; A.5", "I ms.96-113; PartA", "Distinguishes full two-out-of-three from the single valid cancellation rule."),
("A.5", "Refuted", "A.1", "Lead1; PartB", "Complete C2 category and regular action; code/A5_finite_counterexample.py and output."),
("A.6", "Known", "Cisinski2009 Thm3.13", "I ms.99-100; PartA", "Locally constant shifted derivators; unit/counit and Der2 transfer the specified ordinary restriction to every shape."),
("A.7", "Proved", "A.2; A.6; G.2", "I ms.96-126; XVI Loc4; PartA", "Natural twisted-arrow span proves same-D opposite invariance. Finite products only; alternating fences refute infinite products. Constant class lacks reverse sum implication."),
("A.8", "Proved", "A.1; C.1", "PartsA-B; enhancement question", "Full faithfulness/equivalence of a specified adjoint restriction, not arbitrary equivalence of homotopy categories."),
("B.1", "Proved", "A.2; A.3; A.6; Cisinski2008 Prop3.7", "XVI Loc3 versus Loc3bis; PartB", "Absolute Theorem A holds for all derivators; constant class is fundamental by the checked Cisinski result."),
("B.2", "Proved", "A.8; Cisinski2008 Thm1.13", "XVI Loc3bis; PartB", "Enhanced Grothendieck homotopy-colimit proof; equivalence and fully faithful versions both proved."),
("B.3", "Proved", "A.6; Cisinski2009 Thm3.6,Lem3.9,Prop3.10,Thm3.13; Hoermann2015 Thm2.5.5", "PartB arbitrary derivator descent; D.11; Lead1", "All Der1--4 derivators. Partial LC projectors, cocartesian-compatible maps, fibrewise Kan and unit/counit detection; no enhancement or Der5."),
("B.4", "Proved", "B.1; B.2; C.2; C.4; C.7; C.11; LurieHTT5.4.6.6,5.5.7.10; LurieHA4.8.4.2", "XVI ms.75-79 Loc9; PartB", "Set generation and literal arrow-category accessibility proved for constant/LC classes of all presentable coefficients; concrete intermediate classes also accessible. Corrects subcategory-order transcription."),
("B.5", "Proved", "A.7; B.1; B.3; G.1; G.2; Cisinski2006 Cor4.2.22", "XVI Loc4,5,6a,8", "Includes arbitrary-D W1 descent and filtered-colimit closure; nonthinness is exact component criterion for W1 and constant classes."),
("B.8", "Known", "B.3; C.4; C.7; C.10; Cisinski2006 Prop9.2.17", "TOTASPH F.28; PartB", "Sphere test has no accessibility hypothesis; applied to every derivator's locally constant localizer."),
("B.9", "Proved", "HausmannHusemoller1979 Props1.2-1.4", "CATHOT E17 dependency; PartB", "Unpointed homotopy category; double homotopy pushout proves epimorphism and does not confuse it with equivalence."),
("B.10", "Proved", "HigmanNeumannNeumann1949 ThmsI-II; BaumslagDyerHeller1980 Prop4.1,Thm4.2,Cor4.5,Lem5.4,Thm5.5", "CATHOT BC B.6; cardinal Kan-Thurston lead", "Full simultaneous HNN and mitosis construction with embedding, acyclicity, simplicity, and cardinal control."),
("B.11", "Proved", "B.9; B.10; Hatcher2002 Cor4.33", "CATHOT E17 missing KT_mu; PartB", "Small CW spaces; arbitrary bound mu; aspherical replacement, local-coefficient homology isomorphism, perfect kernel, and small-group invisibility."),
("B.12", "Proved", "B.9; B.11; CATHOT C.1-C.4", "CATHOT E17; E_ind; afterword", "Every U-small filtered ind-object satisfying stated W_infinity invariance has invertible Ind(Pi1) unit. Uniform cardinal bound; canonical localization comparison; no infinite-product/pi0 swap."),
("B.13", "Open", "B.3; B.4; Cisinski2006 Scholie4.2.17", "PartB general accessibility", "Bare-derivator set-generation and literal accessibility not established; W1 accessibility also unproved here for general presentable coefficients outside the concrete families. Vopenka conditional for fundamental classes, not assumed; no explicit counterexample."),
("B.14", "Open", "B.7; C.2; C.11", "PartB Loc7a and7F general scope", "Bare-D W1 7a/factorization gap; arbitrary-spectrum LC properness criterion exact but not evaluated already for K(1). Not a literature-wide openness claim."),
("G.1", "Proved", "A.1; Der1-4", "X ms.1-5; component detection", "Nonterminal point coefficients are necessary and sufficient for Wlc subset W0; no enhancement."),
("G.2", "Proved", "A.1; Der1-4", "X ms.5; XVI Loc5", "Constant component detection iff nonthin point category. Nontrivial preorder constants detect only emptiness."),
("G.3", "Proved", "A.1; G.1", "X ms.1-5; functoriality", "Arbitrary derivator morphisms give no direction of class inclusion; equivalences and products treated separately."),
("G.4", "Proved", "A.4; G.3", "X ms.1-5; functoriality", "Pseudoretract and fully faithful coefficient comparisons; essential-image descent explicitly required for equivalences."),
("G.5", "Proved", "C.7; G.3; G.4", "X ms.1-5; scalar functoriality", "Unital associative rings; scalar extension inclusion, faithfully flat commutative reflection, and zero-ring cases."),
("G.6", "Open", "B.3; B.13; E.2; E.7; E.11", "X ms.1-5; PartsE-G", "All-bare-derivator functorial coefficient raising and iteratable enriched 2-derivator enhancement remain unspecified; accessible localized-space realization is proved."),
]
records = {r[0]: dict(id=r[0], status=r[1], depends_on=r[2],
                     manuscript_rows_or_pages_settled=r[3], notes=r[4])
           for r in root_data}
for name in ("C_results.json", "D_results.json", "EF_results.json"):
    for row in json.loads((ROOT / "research" / name).read_text()):
        assert row["id"] not in records
        records[row["id"]] = row
for row in json.loads((ROOT / "research/B_loc67_results.json").read_text())["results"]:
    records[row["id"]] = {
        "id": row["id"], "status": row["status"],
        "depends_on": "B.3; B.4; B.10; C.2; C.7; C.9; G.1; G.2; " + row.get("sources", ""),
        "manuscript_rows_or_pages_settled": "XVI ms.37-39 Loc6b,6c,7a,7b,7c,7F",
        "notes": row["statement"] + " " + row.get("remaining_exact_question", "")
    }

def expand(path):
    raw = path.read_text()
    return re.sub(r"\\input\{([^}]+)\}", lambda m: expand(ROOT/(m.group(1)+".tex")), raw)

tex = expand(ROOT / "GALOIS_paper.tex")
pat = re.compile(r"\\begin\{claim\}\{([A-G]\.\d+)\}\{(Proved|Refuted|Known|Open)\}\{")
claims = []
for m in pat.finditer(tex):
    start = m.end(); end = start; depth = 1
    while depth:
        if tex[end] == "{" and tex[end-1] != "\\": depth += 1
        if tex[end] == "}" and tex[end-1] != "\\": depth -= 1
        end += 1
    title = tex[start:end-1]
    stop = tex.index(r"\end{claim}", end)
    body = re.sub(r"\s+", " ", tex[end:stop]).strip()
    claims.append((m.group(1), m.group(2), title + ". " + body))
assert len(claims) == len({x[0] for x in claims}) == 74, len(claims)
assert set(records) == {x[0] for x in claims}, set(records) ^ {x[0] for x in claims}
aux = (ROOT / "GALOIS_paper.aux").read_text()
pages = dict(re.findall(r"\\newlabel\{([A-G]\.\d+)\}\{\{[^}]+\}\{(\d+)\}", aux))
assert set(pages) >= set(records)
rows = []
for ident, status, statement in claims:
    record = records[ident]
    assert status == record["status"], (ident, status, record["status"])
    row = {key: record.get(key, "") for key in FIELDS}
    special = {"B.3":"B_general", "B.4":"B_accessibility", "B.6":"B_loc67", "B.7":"B_loc67",
               "B.11":"B_KT", "B.12":"B_KT", "B.13":"B_KT", "B.14":"B_KT"}
    source = special.get(ident, ident[0])
    row.update(statement=statement,
               where_proved=f"GALOIS_paper.pdf, p. {pages[ident]}, statement {ident}; sections/{source}.tex")
    rows.append(row)
with (ROOT / "GALOIS_results.csv").open("w", newline="") as out:
    w = csv.DictWriter(out, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
counts = Counter(row["status"] for row in rows)
stats = {"statements": len(rows), "statuses": dict(counts),
         "open_ids": [r["id"] for r in rows if r["status"] == "Open"],
         "manuscript_audit_rows": len(list(csv.DictReader((ROOT / "research/D_audit.csv").open())))}
(ROOT / "research/release_statistics.json").write_text(json.dumps(stats, indent=2)+"\n")
print(f"PASS: exactly {len(rows)} numbered assertions, all statuses matched to the actual TeX.")
print("Status counts:", dict(counts))
print("Open assertions:", ", ".join(stats["open_ids"]))
print("PASS: every assertion has a compiled PDF page and all seven requested CSV fields.")
print("PASS: full mathematical statement bodies preserved as LaTeX in CSV; no truncated summaries.")
print(f"PASS: manuscript audit has {stats['manuscript_audit_rows']} required rows.")
