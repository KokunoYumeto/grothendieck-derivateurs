#!/usr/bin/env python3
"""Rebuild and verify the Part F result register (standard library only)."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_rows_or_pages_settled', 'notes']
ROWS = [{'id': 'F.1', 'statement': 'Cross-ratio model of X4 and injective peripheral cyclic subgroups', 'status': 'Known', 'where_proved': 'sections/F.tex, F.1', 'depends_on': '', 'manuscript_rows_or_pages_settled': 'Part F(i)', 'notes': 'Keel Catalogue Facts 1-2; normalization proof'}, {'id': 'F.2', 'statement': 'Complete four-object skeleton of Exit X4 with coset exit bimodules', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.2', 'depends_on': 'F.1', 'manuscript_rows_or_pages_settled': 'Part F(i)', 'notes': 'T04 is the opposite; all composition specified'}, {'id': 'F.3', 'statement': 'Aspherical strata force an ordinary exit infinity-category', 'status': 'Refuted', 'where_proved': 'sections/F.tex, F.3', 'depends_on': '', 'manuscript_rows_or_pages_settled': 'Part F rationale', 'notes': 'S2 stratified by a point and R2; mapping space S1'}, {'id': 'F.4', 'statement': 'Twenty-six strata of X5 and all their automorphism groups', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.4', 'depends_on': 'F.7', 'manuscript_rows_or_pages_settled': 'Part F(i)', 'notes': '1 open; 10 divisors; 15 points; P4/full twist'}, {'id': 'F.5', 'statement': 'Transporter and Dehn-twist quotient model specifies all C5 arrows', 'status': 'Known', 'where_proved': 'sections/F.tex, F.5', 'depends_on': 'F.4;F.7', 'manuscript_rows_or_pages_settled': 'Part F(i)', 'notes': 'Jansen 3.18 and 6.6; all bimodules reduced explicitly'}, {'id': 'F.6', 'statement': 'Composition formula and product-asphericity of all genus-zero strata', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.6', 'depends_on': 'F.1;F.5', 'manuscript_rows_or_pages_settled': 'Part F(i)', 'notes': 'Includes Fadell-Neuwirth induction and quotient independence'}, {'id': 'F.7', 'statement': 'Ordinary EI exit model for all stable labelled genus-zero moduli', 'status': 'Known', 'where_proved': 'sections/F.tex, F.7', 'depends_on': '', 'manuscript_rows_or_pages_settled': 'Part F(i)', 'notes': 'Jansen Corollary 6.6; original Charney-Lee category is opposite'}, {'id': 'F.8', 'statement': 'Constructible coefficients agree with HOT of entrance category', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.8', 'depends_on': 'F.7', 'manuscript_rows_or_pages_settled': 'Part F(ii)', 'notes': 'Compactly generated coefficients; bare derivator limitation explicit'}, {'id': 'F.9', 'statement': 'Filling punctures and stabilizing define actual forgetful functors', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.9', 'depends_on': 'F.7', 'manuscript_rows_or_pages_settled': 'Part F(ii),(iv)', 'notes': 'Forgetting strict on fixed surface models; relabelling coherent by lift comparisons'}, {'id': 'F.10', 'statement': 'Full-model entrance forgetful functors are W-infinity-proper', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.10', 'depends_on': 'F.9;D proper lifting criterion', 'manuscript_rows_or_pages_settled': 'Part F(ii); I ms.49-56', 'notes': 'Lift categories equivalent to relative multicurve posets; Bass-Serre trees with leaves'}, {'id': 'F.11', 'statement': 'Forgetting a marking is always W-infinity-smooth', 'status': 'Refuted', 'where_proved': 'sections/F.tex, F.11', 'depends_on': 'F.9', 'manuscript_rows_or_pages_settled': 'Part F(ii)', 'notes': 'Five-to-four test groupoid is BZ; smallest in forgetful sequence'}, {'id': 'F.12', 'statement': 'Clutching is represented by a replete full cosieve in entrance variance', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.12', 'depends_on': 'F.7', 'manuscript_rows_or_pages_settled': 'Part F(ii)', 'notes': 'Replete cosieve proper; fixed-curve product inclusion not strict proper'}, {'id': 'F.13', 'statement': 'Strict categorical fibres of forgetting model geometric curve fibres', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.13', 'depends_on': 'F.9;F.6', 'manuscript_rows_or_pages_settled': 'Part F(ii)', 'notes': 'All hom-sets/actions checked; S2 versus S2 wedge S2 excludes fibre bundle'}, {'id': 'F.14', 'statement': 'Right Kan extensions and proper base change for the stated moduli maps', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.14', 'depends_on': 'F.8;F.10;F.12;F.13;D proper BC', 'manuscript_rows_or_pages_settled': 'Part F(ii)', 'notes': 'Compactly generated coefficients; locally compact Hausdorff geometric BC; strict proper models and pullback comparison qualified'}, {'id': 'F.15', 'statement': 'Complete five-to-four object and coset arrow map', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.15', 'depends_on': 'F.4;F.9', 'manuscript_rows_or_pages_settled': 'Part F(ii)', 'notes': 'All 26 object types checked by program'}, {'id': 'F.16', 'statement': 'Exact tower definitions and label/orientation restrictions in Longue Marche', 'status': 'Known', 'where_proved': 'sections/F.tex, F.16', 'depends_on': '', 'manuscript_rows_or_pages_settled': 'Part F(iv); LM19 ms.102; LM27 ms.172-173', 'notes': 'Missing start of LM26 obtained from public primary transcription'}, {'id': 'F.17', 'statement': 'Teichmuller groupoid is the open subgroupoid, with Lego presentation', 'status': 'Proved', 'where_proved': 'sections/F.tex, F.17', 'depends_on': 'F.6;F.7;F.16', 'manuscript_rows_or_pages_settled': 'Part F(iii),(iv); Esquisse section2', 'notes': 'Equivariant marking-path groupoid required; whole EI category not a groupoid; no arithmetic claims'}]


def main():
    path = ROOT / "audit" / "F_results.csv"
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(ROWS)
    ids = [row["id"] for row in ROWS]
    assert len(ids) == len(set(ids)) == 17
    text = (ROOT / "sections" / "F.tex").read_text()
    statements = re.findall(r"\\begin\{statement\}\{(F\.\d+)\}\{(Known|Proved|Refuted|Open)\}", text)
    assert statements == [(row["id"], row["status"]) for row in ROWS], statements
    graph = {row["id"]: re.findall(r"F\.\d+", row["depends_on"]) for row in ROWS}
    done = set()
    def visit(node, active):
        assert node not in active, ("dependency cycle", active, node)
        if node in done:
            return
        for dependency in graph[node]:
            assert dependency in graph, dependency
            visit(dependency, active | {node})
        done.add(node)
    for node in graph:
        visit(node, set())
    print("Rebuilt audit/F_results.csv: 17 result rows.")
    print("Statement identifiers and statuses agree with sections/F.tex.")
    print("All internal dependencies exist; the dependency graph is acyclic.")

if __name__ == "__main__":
    main()
