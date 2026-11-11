#!/usr/bin/env python3
"""Assemble the numbered-result ledger and a deduplicated bibliography.

This is an editorial consistency program. It checks document structure, not
the validity of mathematical proofs. Run from any directory.
"""
from __future__ import annotations

import csv
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ROOT_NOTES = {
    "B.1": ("Cisinski 2004 Theorem 2.2.11; XVI Loc (1 ter,3 bis)", "Modern relative-Theorem-A convention; no accessibility assumption."),
    "B.2": ("XII W(7) forward; XVI Loc (6 a,6 B)", "Objectwise Grothendieck-construction comparison specified; empty diagrams included."),
    "B.3": ("Lead 1; XII ms. 266–267", "Explicit functorial category K(g); A empty gives B coproduct e."),
    "B.4": ("XII ms. 228–234; XVI Loc (6 A,6 A')", "The manuscript uses products with endpoints, not pushout-products. Thomason 5.3(3) is not used."),
    "B.5": ("Lead 1; XII ms. 265–272; XVI Loc (6 b,6'b,6 C)", "Full cube and single-square versions proved equivalent; specified cone basepoints and retracts included."),
    "B.6": ("Lead 2; Lead 3 minimality", "No extra forward axiom; empty and arbitrarily disconnected sources treated."),
    "B.7": ("XII Theorem 2 ms. 78; TOTASPH A.12–A.13", "35 objects, 159 arrows; integral Smith forms and nontrivial A5 quotient checked."),
    "B.8": ("XII Theorem 2 ms. 78; XVI Theorem 5.4 ms. 79", "37-object two-cone counterexample and actual Dwyer-cylinder counterexample."),
    "B.9": ("XII ms. 85; TOTASPH A.10–A.11, B.1–B.2, F.20", "Both variances; one-point complement has only identity endomorphism."),
    "B.10": ("CATHOT B.6–B.7 input", "Mitosis independently proved; the stronger simple-group claim is unnecessary and unused."),
    "B.11": ("After CATHOT consequence for Part C", "All acyclic groups killed by every reversible localizer; nontrivial pi1 retained in source."),
    "B.12": ("CATHOT B.8", "Specified graph-of-spaces quotient is a homology equivalence; H need not be acyclic."),
    "B.13": ("Part H wording; proposed upward-closed reading of Lead 3", "W0 contains WZ but fails reverse excision; four-object circle cofiber checked."),
    "D.1": ("Lead 3", "Integral homology gives the least reversible fundamental localizer; full cube proof by chain complexes."),
    "D.2": ("Lead 3 exception; XVI Theorem 6.1", "No solution with Loc (5); total class is unique only after omitting Loc (5)."),
    "D.3": ("After TOTASPH sphere threshold; Parts C,H", "A nontotal reversible localizer kills no nonnegative-dimensional sphere."),
    "D.4": ("Lead 4; XVI ms. 87–92", "Unconstrained intersection versus an additional requested inclusion inside Winfty distinguished."),
    "D.5": ("XVI ms. 87–96; simple homotopy suggestion", "Geometric simple structures survive; ordinary localization at simple maps loses the finer classification."),
    "D.6": ("XVI ms. 95", "Finite posets P and sd(P); all monotone reverse maps have degree zero."),
    "H.1": ("Part H; Leads 1–6 placement", "Proper reversible class is not the entire interval above WZ."),
    "H.2": ("XII ms. 88–89; TOTASPH final-image criterion", "Ordinary presheaf Kan extension; finality means nonempty connected commas."),
    "H.3": ("TOTASPH C.5; Part H", "All covariant element categories and their coverings; empty case explicit."),
    "H.4": ("TOTASPH D.19; Part H", "No accessibility; final functors give pi0 bijection and pi1 surjections."),
    "H.5": ("TOTASPH F.25, F.28–F.30", "Every sieve is a cofibration iff W contains W1; four-object S2 category checked."),
    "H.6": ("XII ms. 114–115, 228–234; TOTASPH F.23–F.24,F.31", "Uniform n>=2 coend proof, complete n=2,3 computations, and arrow-retract obstruction."),
    "H.7": ("Part H stable derivators; XVI ms. 119–121", "Unpointed HOT_W is stable only for the total class, whenever its derivator structure exists."),
    "H.8": ("Parts C,D,E,H; separation of reversible excision from Loc (7 F)", "Nontotal reversible implies Loc (5) and failure of (7 F); no accessibility hypothesis."),
}


def braced(text: str, pos: int) -> tuple[str, int]:
    assert text[pos] == "{", (pos, text[pos:pos+50])
    depth = 1
    i = pos + 1
    start = i
    while depth:
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1
    return text[start:i-1], i


def claims(text: str):
    marker = r"\begin{claim}"
    pos = 0
    while (pos := text.find(marker, pos)) >= 0:
        start = pos
        pos += len(marker)
        values = []
        for _ in range(3):
            value, pos = braced(text, pos)
            values.append(value)
        end = text.index(r"\end{claim}", pos)
        nxt = text.find(marker, end)
        proof_end = len(text) if nxt < 0 else nxt
        yield values, text[pos:end].strip(), text[start:proof_end]
        pos = end + len(r"\end{claim}")


def bib_entries(text: str):
    for m in re.finditer(r"@(\w+)\s*\{", text):
        body, end = braced(text, m.end()-1)
        key = body.split(",", 1)[0].strip()
        yield key, text[m.start():end]


def field(entry: str, name: str) -> str:
    m = re.search(r"\b"+name+r"\s*=\s*\{", entry, re.I)
    return braced(entry, m.end()-1)[0] if m else ""


def merge_bibliography() -> dict[str, str]:
    sources = [ROOT / "research" / name for name in
               ("Root_references.bib", "AG_references.bib", "CE_references.bib", "F_references.bib")]
    records = {}
    identity_keys = {}
    aliases = {}
    duplicate_notes = {}
    for source in sources:
        if not source.exists():
            raise FileNotFoundError(source)
        for key, entry in bib_entries(source.read_text()):
            # Identical source URLs are reliable despite TeX accent spellings.
            url = field(entry, "url").rstrip("/")
            doi = field(entry, "doi").lower()
            if "smf_ast_308" in url or "Cisinski2006" in key:
                identity = "cisinski2006"
            elif "Cisinski2004" in key:
                identity = "cisinski2004"
            elif "Thomason1980" in key:
                identity = "thomason1980"
            elif "Hatcher2002" in key:
                identity = "hatcher2002"
            else:
                identity = doi or url or key
            if identity in identity_keys:
                canonical = identity_keys[identity]
                aliases[key] = canonical
                duplicate_notes.setdefault(canonical, []).append(field(entry, "note"))
            else:
                identity_keys[identity] = key
                records[key] = entry
    for key, notes in duplicate_notes.items():
        entry = records[key]
        m = re.search(r"\bnote\s*=\s*\{", entry, re.I)
        old, end = braced(entry, m.end()-1)
        new = old + "; additional source checks: " + "; ".join(n for n in notes if n and n != old)
        records[key] = entry[:m.end()] + new + entry[end-1:]
    # Rewrite only citation argument keys, never prose or original source files.
    citation_pattern = re.compile(r"(\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{)([^}]+)(\})")
    for source in (ROOT / "sections").glob("*.tex"):
        text = source.read_text()
        def sub(m):
            keys = [aliases.get(k.strip(), k.strip()) for k in m.group(2).split(",")]
            return m.group(1) + ",".join(keys) + m.group(3)
        source.write_text(citation_pattern.sub(sub, text))
    heading = "% POLES bibliography. Every cited item records its verification status.\n% Generated by code/assemble_deliverables.py from the authored source records.\n\n"
    (ROOT / "POLES_references.bib").write_text(heading + "\n\n".join(records.values()) + "\n")
    for key, entry in records.items():
        if not re.search(r"\b(?:verified|unverified)\b", field(entry, "note"), re.I):
            raise AssertionError(f"No verification status for {key}")
    return aliases


def assemble_results():
    fields = ["id", "statement", "status", "where_proved", "depends_on", "manuscript_rows_or_pages_settled", "notes"]
    metadata = {}
    for name in ("AG_results.json", "CE_results.json", "F_results.json"):
        rows = json.loads((ROOT / "research" / name).read_text())
        for row in rows:
            assert row["id"] not in metadata
            metadata[row["id"]] = row
    ledger = []
    identifiers = set()
    ref_targets = set()
    cites = set()
    for source in sorted((ROOT / "sections").glob("[A-H].tex")):
        text = source.read_text()
        for values, statement, block in claims(text):
            identifier, status, title = values
            assert identifier not in identifiers, identifier
            assert status in {"Proved", "Refuted", "Known", "Open"}, (identifier, status)
            identifiers.add(identifier)
            deps = sorted(set(re.findall(r"\\claimref\{([^}]+)\}", block)) - {identifier},
                          key=lambda s: (s.split(".")[0], int(s.split(".")[1])))
            old = metadata.get(identifier, {})
            pages, note = ROOT_NOTES.get(identifier, (old.get(fields[5], ""), old.get("notes", "")))
            assert pages, (identifier, "missing manuscript/lead mapping")
            ledger.append({
                "id": identifier,
                "statement": re.sub(r"\s+", " ", title + ". " + statement),
                "status": status,
                "where_proved": f"POLES_paper.tex, Part {identifier[0]}, {identifier}; sections/{identifier[0]}.tex",
                "depends_on": "; ".join(deps),
                "manuscript_rows_or_pages_settled": pages,
                "notes": note,
            })
        ref_targets.update(re.findall(r"\\claimref\{([^}]+)\}", text))
        for m in re.finditer(r"\\cite\w*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}", text):
            cites.update(k.strip() for k in m.group(1).split(","))
    assert not ref_targets - identifiers, ("missing claims", ref_targets - identifiers)
    keys = {key for key, _ in bib_entries((ROOT / "POLES_references.bib").read_text())}
    assert not cites - keys, ("missing bibliography", cites - keys)
    assert not set(metadata) - identifiers, ("stale metadata", set(metadata)-identifiers)
    with (ROOT / "POLES_results.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(ledger)
    (ROOT / "research" / "Root_results.json").write_text(json.dumps([r for r in ledger if r["id"][0] in "BDH"], indent=2, ensure_ascii=False)+"\n")
    return {
        "numbered_statements": len(ledger),
        "status_counts": {status: sum(r["status"] == status for r in ledger) for status in ["Proved", "Refuted", "Known", "Open"]},
        "statements_by_part": {part: sum(r["id"].startswith(part+".") for r in ledger) for part in "ABCDEFGH"},
        "open_statement_ids": [r["id"] for r in ledger if r["status"] == "Open"],
        "citation_keys_used": len(cites),
        "bibliography_entries": len(keys),
        "missing_cross_references": [],
        "missing_citations": [],
        "ledger_columns": fields,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bibliography-only", action="store_true")
    args = parser.parse_args()
    aliases = merge_bibliography()
    result = {"bibliography_ready": True} if args.bibliography_only else assemble_results()
    result["bibliography_aliases"] = aliases
    target = "bibliography_merge.json" if args.bibliography_only else "editorial_checks.json"
    (ROOT / "verification" / target).write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))
