"""Build the Part E statement register from the explicit audited claim metadata."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
rows = [
('E.1','A Grothendieck fibration is an opfibration iff every transport has a left adjoint; its transports are weak equivalences; bifibrations are properly contained in proper-and-smooth functors.','Proved','sections/E.tex, E.1','Part D lifting-category criteria and diamond counterexample','VI ms.186–187; VIc-C008','Extra weak-equivalence hypothesis on bifibration transports is redundant.'),
('E.2','Cisinski functorial proper-and-smooth replacement is fibrewise equivalent on locally constant Grothendieck-fibration input.','Known','Cisinski 2006 Theorem 5.3.14 and Corollaries 6.4.8,6.4.16; sections/E.tex, E.2','Quillen Theorem B','VIc-C008 (perfect comparison only)','Does not supply strict universal lifts.'),
('E.3','Alternating comma replacement gives a functorial proper-and-smooth replacement, total weakly equivalent always and fibrewise weakly equivalent on weak fibrations.','Proved','sections/E.tex, E.3','Quillen Theorem B; filtered-colimit finite-data argument','VI ms.192–195; VIc-C022–C031,C036','No inference of strict bifibrancy.'),
('E.4','Filtered colimits of strict bifibrations under arbitrary maps over a fixed base remain strict bifibrations.','Refuted','sections/E.tex, E.4; code/E_finite_checks.py','E.1','VI ms.192–195 (limit-method boundary)','Finite initial chains with growing maxima converge to N without maximum; base [1].'),
('E.5','For infinite lambda bounding Y, the contractible-patch category K_lambda(Y) has classifying space weakly equivalent to Y, naturally.','Proved','sections/E.tex, E.5','Quillen Theorem A; category-of-simplices comparison','CATHOT follow-up lead in STRATA prompt','No Kan hypothesis needed; includes empty Y.'),
('E.6','Integrating K_lambda of a covariant local system represents it; trivial-Kan-fibration transitions give a bifibration. Contravariant models require opposite patch categories.','Proved','sections/E.tex, E.6','E.1; E.5; Thomason homotopy-colimit comparison','CATHOT patch-construction follow-up','E.10 now supplies the transition hypothesis on all-mono or all-epi bases.'),
('E.7','Postcomposition on contractible patches along a weak equivalence between Kan complexes necessarily has adjoints.','Refuted','sections/E.tex, E.7; code/E_finite_checks.py','Two-object contractible groupoid nerve','CATHOT patch-enlargement follow-up','Inclusion of vertex 0; patch at vertex 1 has no maps either way to the image. Does not refute existence of another bifibration representative.'),
('E.8','Every locally constant space-valued diagram with 1-truncated values has a strict-bifibration representative over every small base.','Proved','sections/E.tex, E.8','E.1; fundamental groupoids','VIc-C008 (1-truncated values)','Functorial on strict simplicial-presheaf models.'),
('E.9','Every locally constant space-valued object over S has a strict-bifibration representative when BS is a 1-type.','Proved','sections/E.tex, E.9','E.5; local-system invariance under B-equivalence; strict diagram models','VIc-C008 (1-type bases)','Includes weakly contractible, initial, terminal, and groupoid bases; coherent equivalence versus strict functoriality distinguished.'),
('E.10','Every local system over a small category with all arrows monic or all arrows epic has a strict-bifibration representative; in particular every small poset base is affirmative.','Proved','sections/E.tex, E.10; Lurie HTT A.2.8.2 and A.3.3.4','E.5–E.6; injective fibrant replacement; representable monomorphisms','VIc-C008 for all posets and all-mono/all-epi bases','Functorial on models with a uniform replacement-size bound; the six-element sphere path local system is settled affirmatively.'),
('E.11','Every locally constant object over every small category admits a small ordinary strict-bifibration representative, functorially; and strict bifibrations give the claimed fine-localization equivalence.','Open','sections/E.tex, E.11; code/E_finite_checks.py','E.1–E.10; Fiedorowicz 2002 unnumbered Lemma pp.33–34','VIc-C008 in full generality','Exact remaining test: path local system of *->BM for the one-object five-arrow rectangular-band monoid with BM~S2. One object is minimal; no minimality in number of arrows is claimed.'),
('E.12','XI §1 and XVI §4 do not assert strict-bifibration replacement; two ill-typed displayed terms have the stated corrections.','Proved','sections/E.tex, E.12; supplied source transcriptions','Typed source diagrams; E.1–E.4','XI ms.127–132; XVI ms.41–43,58–60','XI fibre map X_s-prime->X_s; XVI Lemma 4.4.1 output factor p in F, not f in F.')
]
path = root / 'audit' / 'E_results.csv'
with path.open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['id','statement','status','where_proved','depends_on','manuscript_rows_or_pages_settled','notes'])
    w.writerows(rows)
print(f'Wrote {len(rows)} rows to {path.name}')
print('Statuses:', {s: sum(r[2] == s for r in rows) for s in ['Proved','Known','Refuted','Open']})
