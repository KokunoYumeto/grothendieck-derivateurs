"""Assemble the complete research audit and a reproducibility entry point."""
from collections import Counter
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/"BISITE_results.csv").open()))
counts=Counter(row["status"] for row in rows)
table=["| Part | Proved | Refuted | Known | Open | Total |",
       "|---|---:|---:|---:|---:|---:|"]
for part in "ABCDEFG":
    subset=[r for r in rows if r["id"].startswith(part+".")]
    c=Counter(r["status"] for r in subset)
    table.append("| "+part+" | "+" | ".join(str(c[s]) for s in
                 ("Proved","Refuted","Known","Open"))+" | "+str(len(subset))+" |")
table.append("| **Total** | "+" | ".join(str(counts[s]) for s in
             ("Proved","Refuted","Known","Open"))+" | **"+str(len(rows))+"** |")
front="""# BISITE research audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 November 2026.
No priority is claimed. The work was developed from the attached prompt,
its primary-source archive, targeted primary-literature checks, and
independent proofs and finite computations. Earlier AI-produced packages
are treated as leads, not as authorities.

## Deliverables and status conventions

The paper is BISITE_paper.tex and BISITE_paper.pdf. The complete register is
BISITE_results.csv, with exactly one row per numbered statement and the
requested seven columns. BISITE_references.bib is the unified bibliography;
each entry has an explicit verification note. The sections directory holds
the included LaTeX sources. The code directory holds programs and saved
outputs. The auxiliary part registers and reports are retained so the merge
is reproducible.

“Proved” means a proof is given here under the full hypotheses in the
statement. “Refuted” means a specified assertion is false and an explicit
counterexample is supplied. “Known” means the cited primary theorem and its
actual hypotheses were checked. “Open” records an exact task not settled by
this audit; it does not claim that the task is unresolved in the literature.
C.9 is a proved conditional implication: above dimension two its
model-structure premise is the unrefereed OpenAI claim, named in its
statement and dependency field. It is not an unconditional verification of
that claim. Bibliographic verification of the two OpenAI attachments means
that their documents and claimed statements were read, not that their
proofs or formalizations were certified.

"""
front+="\n".join(table)+"\n"
front+="""

## Main determinations

The manuscript's maximal universal testing class is identified with the
correct smooth or proper class according to comma variance. The minimal
categorical fine theories are the covariant and presheaf diagram
infinity-categories. The simplicial literal-slice recipe needs a
quasicategorical base; its corrected universal version uses the actual
covariant and contravariant model structures at every base.

The complementarity inclusion for the same fundamental localizer holds
exactly for the minimal localizer and the total class, without an
accessibility hypothesis. The truncation, homology, and local-system
examples are distinguished and checked separately. The finite central C2
extension is verified by nonabelian presentation reductions, not by
homology alone.

XIIc B062 is false. A six-element lattice satisfies fibre axioms (a) and
(b) at every base and violates (c), with explicit inverse equivalences
after both ordinary and enhanced localization. Separately, the manuscript's
literal moderately saturated absolute localizer package does not imply
relative Theorem A; a component-sensitive class and a finite groupoid
triangle give a counterexample. Its failure of full arrow-retract closure
is explicitly recorded. These conclusions supersede the temporary Open
drafts from the work process.

The abstract theorem uses explicit enhanced presentation hypotheses,
distinguished from the finite Brown floor. The derivator statements give
the precise base-change, projection and exchange maps and their canonical
mates. The correspondence construction specifies both its enhanced input
and its geometric-setup version. In the diagonally closed discrete-fibration
setup, the stable cohomologically proper maps are exactly finite discrete
bifibrations.

The geometric comparison is proved for every categorically proper map of
finite posets, including nonvertex points of the target realization. The
genus-zero forgetting functor is proper for every n≥3 and is not smooth at
n=4, with a lifting category equivalent to BZ. Its specified direct-image
and boundary comparisons are proved using the actual constructible
categories and canonical mates.

The stable finite-limit formula is a covariant spectral weight acting by a
derived coend. A pointwise twist followed by the same-base colimit is
refuted on the walking arrow. The finite-poset canonical equivalence
criterion, its upper-interval variance, and its geometric Verdier comparison
are stated with the checked Aoki hypotheses. Finite EI categories require
coefficient conditions, and ordinary Verdier duality need not preserve the
coarse minimum stratification.

## Exact remaining tasks

| ID | Remaining assertion | Smallest boundary isolated here |
|---|---|---|
| B.21 | Existence of a different strict Grothendieck bifibration representing the path local system with contractible total category | The five-element rectangular-band monoid; the given fence model's failure is proved, but it does not rule out every alternative |
| C.10 | Relative Street-nerve recognition of both strict higher fine localizations, together with the local lifting and universal Kan base-change criteria | A strict 2-category with a walking noninvertible 2-cell |
| D.12 | General locally compact Hausdorff representation of cosheaves by the unrestricted open-test localization of Top/Y, and a precise dual slice presentation of sheaves | The real line is beyond the proved finite Alexandrov construction |
| F.18 | Extension of the derivator base-change theorem to specified strict higher indexing shapes with coherent mates | Dimension two, where a higher Der 4 and a compatible lax-comma comparison must first be supplied |

Each corresponding paper statement explains the attempted reduction and
the missing comparison. No one of these tasks is silently replaced by its
proved special case.

## Reproducibility and evidence limits

The source-archive inventory and hashes are in code/00_inventory.out.txt.
The extraction programs record the supplied PDFs and text products used.
Reading an extracted section is not a claim to have checked every page of
each monograph. Exact source locations and corrections appear in the
detailed audits below and in the bibliography notes.

The finite certificate programs run with Python's standard library. They
verify complete finite category laws, pullbacks or pushouts where used,
comma categories, permutation actions, explicit localization certificates,
and exact group-presentation or linear-algebra data. In particular,
a_b062_verify.py is independent of the search and rewriting algorithm.
The search exhausted the specified naturally labelled posets through five
objects, recorded no skipped cases, and found the counterexample during a
partial six-object enumeration. No minimality theorem for arbitrary finite
categories is claimed.

The D.11 consistency check covers 50 naturally labelled posets, 1,584
monotone maps to a three-object chain, and 794 comma posets for the retained
proper-lifting cases. Its rational-homology check is distinguished from the
paper's full homotopy-initiality proof. The C2 finite-EI calculation checks
the algebra of the resolution; the paper separately proves the infinite
product-versus-sum conclusion.

The build and final validation programs record compilation, citation and
register consistency, PDF page geometry, and the reproducibility manifest.
The PDF was rendered for visual inspection. Computational checks support
the specified finite certificates and document integrity; this paper is
not a formally verified or refereed mathematical work.

"""
chunks=[front]
for path in (ROOT/"A_report.md",ROOT/"BC_report.md",
             ROOT/"sections/DG_report.md",ROOT/"EF_report.md"):
    body=path.read_text()
    body=body.replace("Root is responsible for final merged-paper compilation, cross-section numbering, bibliography merge, rendered inspection, and packaging. No external message or publication was made by this contribution.","The final compilation and validation are documented in the combined build and validation outputs.")
    shifted="\n".join("#"+line if line.startswith("#") else line for line in body.splitlines())
    chunks.append(shifted)
(ROOT/"BISITE_report.md").write_text("\n\n".join(chunks)+"\n")

readme="""# BISITE

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

Open BISITE_paper.pdf for the complete mathematics. Its source is
BISITE_paper.tex with included sections. BISITE_results.csv is the exact
statement registry; BISITE_references.bib is the unified, verified-source
bibliography. BISITE_report.md records sources, corrections, computations,
conditional dependencies and remaining tasks.

## Build

With a normal LuaLaTeX installation containing the standard mathematical
packages, fontspec, Latin Modern, apacite and BibTeX, run from this directory:

    lualatex -interaction=nonstopmode -halt-on-error BISITE_paper.tex
    bibtex BISITE_paper
    lualatex -interaction=nonstopmode -halt-on-error BISITE_paper.tex
    lualatex -interaction=nonstopmode -halt-on-error BISITE_paper.tex

Alternatively, code/build_paper.py supports the minimal TeX distribution
used during preparation and records each pass. If that distribution lacks
the Lua font loader, code/prepare_tex.py first downloads its public runtime
packages from official CTAN mirrors into a local cache. The preparation
output records exact download hashes. No system installation is modified.
The standard apacite package supplies APA author-date citations and
references; its runtime is included in the optional preparation step.

## Mathematical checks

Run the certificate suite:

    python code/validate_package.py --checks

The individual programs and their original outputs are retained in code.
The mathematical certificate programs use Python's standard library. The
combined package validator additionally uses Poppler (pdfinfo, pdftotext
and pdffonts). Rendering contact sheets uses Poppler and Pillow.
The source-extraction programs additionally need the original attached
background archive in the sibling background directory; the supplied
copyrighted papers are not duplicated in this return archive. The core
mathematical certificates do not need those source files or network access.
The search code is retained separately from its independent hand-certificate
checker; the exploratory size-six search is not a required reproduction step.

MANIFEST.json gives the SHA-256 digest and byte count of every delivered
file except itself. code/package_artifacts.py recreates the single ZIP and
checks its CRC, member paths and manifest against the actual archived bytes.

## Scope

The paper labels every statement Proved, Refuted, Known or Open. It gives
exact hypotheses, variance, localizer and coefficient conditions. The
conditional implication C.9 above dimension two is not a verification of
the unrefereed 2026 model-structure claim. The four outstanding tasks are
B.21, C.10, D.12 and F.18. All proofs and finite examples remain subject to
independent mathematical review.
"""
(ROOT/"README.md").write_text(readme)
log=f"Combined audit: {len(rows)} statements; {dict(counts)}.\n"
log+="Merged A, B/C, D/G and E/F detailed reports without omitting their corrections.\n"
log+="README includes build instructions and the exact remaining tasks.\n"
Path(__file__).with_suffix(".out.txt").write_text(log)
print(log,end="")
