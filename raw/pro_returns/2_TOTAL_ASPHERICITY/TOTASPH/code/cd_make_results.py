"""Create the statement ledger for Parts C and D from audited summaries."""
from pathlib import Path
import csv
rows=[
('C:action-definition','Definition of P_R and P_infinity for covariant Set-valued action categories','Proved','','','Exact variance and empty-element-category convention'),
('C:homology-A','A functor with R-acyclic final comma categories induces an R-homology isomorphism; truncated version included','Proved','','','Bisimplicial-chain proof'),
('C:inherit-elements','P_R and P_infinity pass to connected components of covariant categories of elements','Proved','C:action-definition','','Explicit coproduct-over-fibres comparison isomorphism'),
('C:cyclic-covers','P_Z equals P_infinity for all small categories','Proved','C:inherit-elements','','Cyclic-subgroup covering test and Hurewicz'),
('C:classification','Total W_infinity equals total W_Z and equals nonempty connected plus P_infinity','Proved','C:cyclic-covers;C:homology-A','II-C-003;XII ms.88-89','Complete characterization with covariant set-valued tests'),
('C:exact-sufficient','Nonempty connected plus exact integral colimits implies total W_infinity','Proved','C:classification','','Direct sums over element fibres preserve exactness'),
('C:delta-definition','Delta_inj consists of nonempty finite ordinals and increasing injections','Proved','','','Countable small category'),
('C:interpolation','Compatible integral polynomials on coordinate hyperplanes admit homogeneous interpolation','Proved','','','Explicit inclusion-exclusion formula'),
('C:affine-cones','Every finite ordinal admits an integral augmentation-one affine cone equalizing all incoming injections','Proved','C:interpolation','','Explicit polynomial construction; exact computational checks through dimension 3'),
('C:counterexample','Every totally W_infinity-aspherical category is filtered','Refuted','C:affine-cones;D:affine-exactness;C:exact-sufficient','II-C-003;Lead 4','Counterexample Delta_inj completely specified and verified'),
('B:lead2','H1 of the representable quotient in Lead 2 is Z modulo the subgroup of affine-relation weights','Proved','','Lead 2','No asphericity assumption on the base required'),
('C:directed-affine','Total W_infinity implies common successors and affine equalizers of original parallel pairs','Proved','C:classification;B:lead2','II ms.36','Finite target consolidation proved'),
('C:monoid-lemma','Augmentation-one affine annihilators of x-xa in a monoid imply genuine filteredness','Proved','','','Finite invariant signed measures and minimal period descent'),
('C:weak-terminal','Total W_infinity iff filtered for weakly terminal categories, monoids, and finite-object categories','Proved','C:directed-affine;C:monoid-lemma','II-C-003','Includes all finite-arrow categories; does not extend by an unsupported infinite-limit argument'),
('C:not-sifted','Delta_inj is not sifted despite total W_infinity-asphericity','Proved','C:counterexample','','Its two-point cospan category has exactly three components'),
('D:homology-localizer','R-homology equivalences form a fundamental localizer for nonzero commutative unital R','Proved','','','Relative Theorem A established by the slice Grothendieck constructions'),
('D:R-action','Total W_R iff nonempty connected and P_R','Proved','C:homology-A;C:action-definition','Lead 4','Exact coefficient-ring scope'),
('D:aff-definition','Affine R-linearization has finite R-combinations of augmentation one as arrows','Proved','','','Ordinary category; commutative unital nonzero coefficient ring'),
('D:affine-exactness','Exact R-module colimits iff the components of Aff_R(A) are filtered','Proved','D:aff-definition','Lead 4','Self-contained proof of the precise affine condition'),
('D:exact-R-sufficient','Nonempty connected exact R-colimits imply total W_R','Proved','D:R-action;C:exact-sufficient','Lead 4','Integral conclusion strengthens to W_infinity'),
('D:disconnected-counterexample','Exact integral colimits alone imply total W_Z-asphericity without connectedness assumptions','Refuted','','Lead 4','Discrete two-object and empty categories; finite check attached'),
('D:exact-converse-open','Connected total W_infinity implies exact integral colimits; analogous connected W_R necessity','Open','C:classification;D:affine-exactness','Lead 4','Unresolved in this work; no claim of literature-open status; gap and first unhandled size stated'),
('D:group-criterion','A group is total W_R iff every subgroup is R-acyclic; finite groups iff order is invertible in R','Proved','D:R-action;D:exact-R-sufficient','','C2 separates W_Q from W_infinity; code attached'),
('D:n-convention','W_n denotes isomorphisms on pi0 through pi_n and is a fundamental localizer','Proved','D:homology-localizer','','Truncation adjunction cited at exact proposition'),
('D:final-pi1','Ordinary final functors induce bijections on components and epimorphisms of fundamental groups','Proved','','','Explicit edge-path lift'),
('D:zero-one','Total W0 iff nonempty connected; total W1 iff nonempty simply connected','Proved','D:final-pi1','','Identity proves necessity'),
('D:truncated-classification','For n>=2 total Wn iff BA n-connected and every connected action element category (n-1)-connected','Proved','C:homology-A;C:inherit-elements;C:cyclic-covers;D:final-pi1','','Truncated collage test, covers, and Hurewicz'),
('D:truncated-finite','For n>=2 total Wn iff filtered in weakly terminal and finite-object cases','Proved','D:truncated-classification;B:lead2;C:weak-terminal','','W1 exception supplied by right-zero monoid'),
('D:general-localizer','Totality is monotone in the localizer and total W_infinity is not weak-homotopy invariant','Proved','C:classification','XII ms.120','Uses fundamental-localizer minimality and explicit right-zero monoid'),
('D:zero-ring','For the zero coefficient ring every category is total and every module-colimit functor exact','Proved','','','Explains the nonzero hypothesis')]
out=Path(__file__).resolve().parents[1]/'research'/'CD_results.csv'
with out.open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_rows_or_pages_settled','notes'])
 for id,st,status,dep,pages,notes in rows:w.writerow([id,st,status,'sections/'+id[0]+'.tex; label '+id,dep,pages,notes])
print(f'{len(rows)} rows written to research/CD_results.csv')
