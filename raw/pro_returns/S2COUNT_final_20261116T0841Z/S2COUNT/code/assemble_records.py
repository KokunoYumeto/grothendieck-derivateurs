#!/usr/bin/env python3
"""Merge the independently maintained proof ledgers and bibliography.

This writes only the top-level register and bibliography in the package.
It is deliberately separate from mathematical verification programs.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['id', 'statement', 'status', 'where_proved', 'depends_on',
          'manuscript_pages_settled', 'notes']

def row(ident, statement, status, where, depends='', pages='', notes=''):
    return dict(zip(FIELDS, (ident, statement, status, where, depends, pages, notes)))

rows = []
for filename in ['A_results.csv', 'CD_results.csv', 'E_results.csv']:
    path = ROOT / 'notes' / filename
    if path.exists():
        with path.open(newline='') as source:
            for entry in csv.DictReader(source):
                entry['status'] = entry['status'].lower()
                rows.append(entry)

rows.extend([
    row('B:spherecriterion', 'Ordered sphere products give continuum many maps; nonzero return degrees acting nontrivially on the selected homotopy elements suffice', 'proved', 'sections/B_root.tex:B:spherecriterion', 'Pointed cellular approximation; Hopf principal bundle', 'V43–46', 'Independent audit of R2, including the requested coprime-degree extension'),
    row('B:finitedomination', 'Finite domination implies countably many classes into any target with countably many components and countable homotopy groups', 'proved', 'sections/B_root.tex:B:finitedomination', 'Finite CW obstruction count', 'V43–46', 'Verifies the explicitly unreviewed remark in R4'),
    row('B:main', 'The six-arrow monoid has exactly continuum many maps to S2 and S3, and six is optimal', 'proved', 'sections/B_root.tex:B:main', 'A.M1; B:smallcategories; Serre1953', 'V43–46;V51–52', 'The main universal countability claim is false; no sequential finite-category representation of F_S2'),
    row('B:smallmonoids', 'Every monoid of order at most five has finite-group classifying-space type or is the five-arrow sphere monoid', 'proved', 'sections/B_root.tex:B:smallmonoids', 'Minimal-ideal Rees structure; explicit Karoubi contraction; A.M1 at r=0', '', 'Independent enumeration in code/B_small_categories.cpp checks all labelled tables'),
    row('B:smallcategories', 'Every category with at most five arrows has countably many S2-valued homotopy classes', 'proved', 'sections/B_root.tex:B:smallcategories', 'B:smallmonoids; Miller Theorem A with correction; two-object classification', 'V43–46', 'Includes disconnected categories; source/target-normalized exhaustive enumeration agrees'),
])

task_rows = [
 ('A1','Check the six-element monoid and all used R3 assertions','proved','A.M2–A.M8','code/A_monoid_verify.py; all-degree proofs'),
 ('A2','Identify BM and compute its ring, Steenrod operations and first Massey products','proved','A.M1;A.M5–A.M8','BM is a wedge with one sphere in every degree at least two; all positive operations and triple Massey products vanish'),
 ('A3','Give a structural two-object categorical model','proved','A.M9','The specified Karoubi subcategory and actual Quillen-A comparison are supplied'),
 ('A4','Do the same for Sweeney Example 5.3','proved','A.M1–A.M9','There are 2^(n−2) sphere summands in degree n'),
 ('B1','Verify R2 and its degree variant','proved','B:spherecriterion;B:finitedomination','All stated comparison maps and homotopies are typed'),
 ('B2','Decide countability of maps from BM to S3 and S2','proved','B:main','Both sets have cardinality 2^aleph0'),
 ('B3','Decide the universal question and minimize the arrow count','refuted','B:main;B:smallcategories','Universal countability is false; optimal counterexample has six arrows'),
 ('C1','Classify the requested targets and arbitrary finite CW targets','proved','CD:targetlist;CD:countabletargets','Exact criterion for countable CW targets: each component is a Postnikov piece'),
 ('C2','Classify countable locally finite and finite representatives','proved','CD:alltargets;CD:sequential;CD:finiterepresentative','Finite representatives are exactly finite groupoid types; arbitrary-target countable criterion stated without a countable-pi1 assumption'),
 ('C3','Produce comparison failure with finite stages and S2 colimit for every specified source','proved','CD:comparisonfailure;CD:surjectivity','Failure is noninjectivity; the comparison is always onto when the colimit has finite CW type'),
 ('D','Give corrected statements at all specified manuscript pages','proved','CD:manuscript;CD:boundedtests','Includes explicit failure of set-valued finite-test conservativity'),
 ('E1','Audit INDLOCAL A.19,A.20,A.10,A.13,A.16,A.27–A.31','proved','sections/E_agent.tex:E.1–E.7','Exact nonsingular-equation theorem checked from the complete source; scope and remaining gaps retained'),
 ('E2','Decide existence of an aleph0-resolution of S2 in dimension two','undecided','sections/E_agent.tex:E.8 and research notes','Neither a no-countable-image construction nor a universal countable-quotient theorem has been proved'),
 ('E3','Determine all bounds aleph0≤mu<continuum for S2 in ZFC','undecided','sections/E_agent.tex:E.8','The whole stated interval remains unsettled here; CH makes the interval contain only aleph0 but does not decide it'),
 ('E4','Determine all dimension-two resolution bounds for every rank kappa','undecided','sections/E_agent.tex:E.3–E.5,E.8','Rank0 all bounds; positive finite rank: finite bounds yes, mu≥continuum no; infinite rank: mu<kappa yes, mu≥kappa^aleph0 no; intervening ranges unresolved'),
 ('E5','State the implications for bounded tests and two-dimensional test groups','proved','sections/E_agent.tex:E.9;CD:boundedtests','Two-dimensional group tests cannot replace the full tests for arbitrary targets at any bound, since they cannot detect S3; the S2-only refinement inherits E2–E4 gaps'),
]
for ident, statement, status, where, notes in task_rows:
    rows.append(row('TASK.'+ident, statement, status, where, '', '', notes))

seen = set()
for entry in rows:
    if entry['id'] in seen:
        raise ValueError('duplicate result id: '+entry['id'])
    seen.add(entry['id'])
with (ROOT/'S2COUNT_results.csv').open('w', newline='') as target:
    writer = csv.DictWriter(target, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)

parts = []
for filename in ['A_references.bib', 'B_references.bib', 'CD_references.bib', 'E_references.bib']:
    path = ROOT/'notes'/filename
    if path.exists():
        parts.append(path.read_text())
bib = '\n\n'.join(parts)
keys = re.findall(r'@\w+\{([^,]+),', bib)
if len(keys) != len(set(keys)):
    raise ValueError('duplicate bibliography key')
(ROOT/'S2COUNT_references.bib').write_text(bib)
print(f'Merged {len(rows)} result rows and {len(keys)} bibliography entries.')
