"""Regenerate BC's statement register and update its explicit historical audit.

This is metadata maintenance only; mathematical verification is in
verify_counterexamples.py.
"""
from pathlib import Path
import csv
import json
import re
from collections import Counter

root = Path(__file__).resolve().parents[2]
sections = root / "sections"
tex = (sections / "BC_agent.tex").read_text()
register_path = sections / "BC_agent_results.json"
previous = {r["id"]: r for r in json.loads(register_path.read_text())}
extra = {
    "B.11": ("", "XVI ms.9, Corollary2.2 parenthesis",
             "Counterexample W_ne is strongly saturated and relative; finite pullback checked."),
    "B.12": ("", "XVI2.1,2.2 principal clause,2.5 finite intended version,2.6; XV9.4 formal equivalences,9.5,9.6",
             "Identities are required in the finite localization lemma. Earlier-axiom deductions in XV9.4 are not certified."),
    "B.13": ("B.5,B.12; Cisinski2006 1.4.12,4.1.29,6.1.18",
             "XVI second2.8,second2.9,2.11–2.14",
             "Arbitrary small sets included; no infinite-coproduct preservation assumed."),
    "B.14": ("", "XVI3.1, ms.18′",
             "Formal cube implications; third vertex of second cube is f2=j1."),
    "B.15": ("B.12", "XVI2.5 arbitrary-W literal wording",
             "Four-object diamond, W={a→1,id_1}; all products of W-arrows lie in W, but not all identities belong to W. Complete finite verification."),
    "B.16": ("", "XVI/XV literal absolute package",
             "All small categories. Explicit infinite counterexample; symbolic affine-tail certificate."),
    "B.17": ("B.12,B.16", "XVI2.7; XV9.9,9.10,9.12,9.13",
             "Finite-coproduct closure does not repair the collapse claim. Relative corrected proof supplied."),
}
claims = re.findall(
    r"\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\s*(.*?)\\end\{claim\}",
    tex, re.S)
rows = []
for ident, status, title, statement in claims:
    row = previous.get(ident, {
        "id": ident, "statement": "", "status": status,
        "where_proved": "sections/BC_agent.tex", "depends_on": "",
        "manuscript_rows_or_pages_settled": "", "notes": ""})
    row["statement"] = title + " — " + " ".join(statement.split())
    row["status"] = status
    if ident in extra:
        row["depends_on"], row["manuscript_rows_or_pages_settled"], row["notes"] = extra[ident]
    rows.append(row)
register_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")

audit_path = sections / "BC_historical_audit.csv"
with audit_path.open(newline="") as stream:
    reader = csv.DictReader(stream)
    fields = reader.fieldnames
    audit = list(reader)
for row in audit:
    chap, name, page = row["chapter"], row["manuscript_statement"], row["manuscript_page"]
    key = (chap, name)
    if key in {
        ("XVI", "Proposition 2.1"), ("XVI", "Lemme 2.6"),
        ("XV9", "Corollaire 9.5"), ("XV9", "Corollaire 9.6"),
    } or (chap == "XVI" and name == "Corollaire 2.9" and page == "13"):
        row.update(status="Proved", proof_in_RESIDUE="B.12",
                   notes="Formal statement proved under its explicit hypotheses; relative Theorem A is unnecessary.")
    if key == ("XVI", "Corollaire 2.2"):
        row.update(status="Refuted", proof_in_RESIDUE="B.11,B.12",
                   notes="Principal equivalence proved. Parenthetical upgrade to full Loc(4) is false; replace it by Loc(4a), or retain Loc(4b).")
    if key == ("XVI", "Lemme 2.5"):
        row.update(status="Refuted", proof_in_RESIDUE="B.12,B.15",
                   notes="Literal arbitrary W is false even for binary products. With identities, finite assertions are proved; arbitrary infinite products remain Open here.")
    if key == ("XV9", "Proposition 9.4"):
        row.update(status="Open", proof_in_RESIDUE="B.12",
                   notes="All formal equivalences and finite/filtered reductions proved. Parenthetical implication from Loc(1,2,3,4,6c′) remains unaudited here.")
    if (chap == "XVI" and name in {"Proposition 2.8", "Corollaire 2.11",
                                  "Corollaire 2.12", "Corollaire 2.13", "Lemme 2.14"}
            or (chap == "XVI" and name == "Corollaire 2.9" and page == "15")):
        row.update(status="Known", proof_in_RESIDUE="B.13",
                   notes="Literal axioms plus the stated component-bijection premise suffice. Both discrete-set adjunctions proved for arbitrary small sets.")
    if key == ("XVI", "Proposition 3.1"):
        row.update(status="Proved", proof_in_RESIDUE="B.14",
                   notes="Both degenerate cubes checked; transcription's repeated f1 corrected to f2=j1.")
    if key in {
        ("XVI", "Proposition 2.7"), ("XV9", "Proposition 9.9"),
        ("XV9", "Lemme 9.10"), ("XV9", "Proposition 9.12"),
        ("XV9", "Corollaire 9.13"),
    }:
        row.update(status="Refuted", proof_in_RESIDUE="B.16,B.17",
                   notes="W_nb satisfies all literal axioms, also finite-coproduct closure. Its localization is nonthin despite component-changing weak arrows. Relative corrected proof supplied.")
    if key == ("XVI", "Corollaire 2.11"):
        row["manuscript_page"] = "17"
    if key == ("XVI", "Corollaire 2.12"):
        row["manuscript_page"] = "18"
    if key == ("XVI", "Corollaire 2.13"):
        row["manuscript_page"] = "18 / 13′"
    if key == ("XVI", "Lemme 2.14"):
        row["manuscript_page"] = "13′–15′"
    if key == ("XVI", "Proposition 3.1"):
        row["manuscript_page"] = "18′"
with audit_path.open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(audit)
print(json.dumps({"numbered_statements": len(rows),
                  "statement_statuses": dict(Counter(r["status"] for r in rows)),
                  "historical_rows": len(audit),
                  "historical_statuses": dict(Counter(r["status"] for r in audit))},
                 ensure_ascii=False, indent=2))
