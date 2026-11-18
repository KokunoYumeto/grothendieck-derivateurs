from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
rows=[
('D.1','All weighted positive k-uniform ordered predimension classes satisfy closure restriction/intersection/transitivity, S, Rig, SA, FA and FA-empty.','Proved','sections/D.tex D:closure','','II 36ter','Every k>=2 and a,b>=1; empty bases included.'),
('D.2','All C(k,a,b) satisfy St and Op and are total, hence quasi-filtered.','Proved','sections/D.tex D:total','D.1; T A.30-A.34','II 36ter; XII 88-89','The long-circle loss is am and the bound s>3(delta(E)+am).'),
('D.3','For b<(k-1)a an explicit finite atom W has a<delta(W)<=a|W|/2 and only singleton proper nonempty strong subsets.','Proved','sections/D.tex D:atom','','II 36ter','Four constructions: cycles, truncated cliques in two ranges, core-petal hypergraphs.'),
('D.4','For b<(k-1)a C(k,a,b) is not exact over any nonzero ring; D_W is injective and T1(coker D_W)=R.','Proved','sections/D.tex D:nonexact','D.1; D.3','II 36ter','Includes C(2,2,1), C(3,3,1); all finite parallel families need not be checked because this named family fails.'),
('D.5','For b>=(k-1)a C(k,a,b) is Ramsey and exact over every ring, with extremely amenable limit group; b>=ka gives Delta_inj.','Proved','sections/D.tex D:high','D-EHN2021 Theorem 1.3; D-EHN2019 Theorem 2.13; T A.6','II 36ter','At b=(k-1)a components have unbounded finite size; unary set-valued functions are explicitly allowed.'),
('D.6','The ordered limit group is amenable iff extremely amenable iff b>=(k-1)a; unordered low-range groups are nonamenable.','Proved','sections/D.tex D:amenability','D.1; D.5; D-EHN2019 Theorem 3.8 proof','II 36ter','Hall matching and the hyperedge-assignment compact flow prove the negative range directly.'),
('D.7','The Cdelta shadow is 2-sparse; general shadow sparsity holds iff b>a(k-2); the unqualified sparse-relation claim EHN Remark 3.2 is false.','Refuted','sections/D.tex D:shadow','D.1; D.6','II 36ter','Refines Lead 4(a) and confirms Lead 8(c) caveat. Explicit 36-vertex ternary counterexample with K8 shadow.'),
('D.8','For b<(k-1)a the ordered limit has no co-precompact extremely amenable subgroup and no precompact strong Ramsey expansion.','Proved','sections/D.tex D:no-precompact','D.6; D-EHN2019 Theorem 3.16(1) proof','II 36ter','Bounded forward balls plus arbitrarily long monotone directed paths whose distant endpoint pairs are strong.'),
('D.9','The complete parameter table: no filtered examples; all total/quasi-filtered; exactness over every nonzero ring, Ramsey, and amenability agree with b>=(k-1)a.','Proved','sections/D.tex D:table','D.2; D.4; D.5; D.6','II 36ter','No parameter in this family gives a counterexample to A.3(i) or A.3(iv).'),
('D.10','The five-edge signed formula in Lead 8(e) works for a>2b; its target is positive iff a>b and all listed edges are closed iff a>2b.','Proved','sections/D.tex D:five-edge','D.4','II 36ter','A support in which every vertex occurs exactly twice cannot have affine augmentation; individual triple solvability does not imply exactness.'),
('D.11','The unordered Cdelta initial triple is rationally equalizable but the category is not exact over any nonzero ring.','Proved','sections/D.tex D:unordered','D.1; D.4','II 36ter','Explicit rigid 18-point 11-triple atom from an asymmetric cubic graph; all subsets and all graph automorphisms checked.'),
('D.12','For a Ramsey expansion u:A*->Cdelta the source is exact and u is not homotopy final; the proposed comma-H1 edge-map description of T1(Q_R) is false.','Refuted','sections/D.tex D:expansion','D.4; T A.6','II 36ter','Correct spectral sequence has E2_1,0=T1(u_!F)=0 for all F; Q_R cannot be any u_!F.')
]
with (root/'results_D.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']);w.writerows(rows)
events=[]
def add(i,typ,outcome):events.append([i,'2026-11-18','GPT-6 Astra (OpenAI), Pro, FREX/predimension',typ,outcome])
for row in rows:add(row[0],'independent re-proof','Proof written and internally checked in '+row[3])
for i in ['D.3','D.7','D.10','D.11']:add(i,'computation or formal certificate','D_certificates.py completed successfully; full output D_certificates.out.')
for i,detail in [
('T A.21','Submodularity, free amalgamation, closure restriction and intersections re-derived for general a,b,k.'),
('T A.24','Private-vertex coefficient argument re-derived; extended to macro-atoms and all nonzero rings.'),
('T A.30','Long-circle visibility and order interpolation read in full and re-derived with cut loss am.'),
('T A.31','Alternating restrictions give algebraic stabilizer generation; extensions and telescoping checked.'),
('T A.32','Minimal finite support plus ordered rigidity checked, including empty support.'),
('T A.33','Both action comparisons and comma-cosieve contractions read and checked; empty-base contraction retained.'),
('T A.34','Totality conclusion read and used after rechecking the preceding reductions.'),
('T A.6','Circle-functional Ramsey-to-integral-equalizer argument read and checked, including d=0 and coefficient transport.'),
('T A.18','Threshold-support layer-cake inequality and finite-dimensional separation read in full and re-derived; global strong-point potential space constructed.'),
('R8','Uniform positive gap re-derived and used in direct potential G-space.'),
('R12(i)','Strong-class KPT statement opened as EHN Theorem 2.13, not erroneously Theorem 2.21.'),
('R12(iii)','EHN Theorem 3.8 proof opened and adapted directly to hyperedge assignments.'),
('Lead 4(a)','Cdelta shadow edge count and infinite stabilizer orbits independently proved.'),
('Lead 4(b)','Follows from rechecked R8 plus Lead 2; Part A owns the latter correspondence.'),
('Lead 4(c)','Global pair of bounded potentials on the strong-point orbit is a nonempty compact convex G-space with no fixed point; finite consistency checked by separation.'),
('Lead 8(a)','Proved for all parameters as D.1-D.2.'),
('Lead 8(b)','Proved and extended to all b<(k-1)a as D.4; high range D.5.'),
('Lead 8(c)','Hypergraph Hall-assignment proof confirmed; shadow caveat confirmed by D.7.'),
('Lead 8(d)','The six-labelling rational average checked; full unordered exactness is nevertheless refuted by D.11.'),
('Lead 8(e)','Five signed marginal identities, positivity and closedness threshold checked; candidate exactness rejected by D.4.'),
('FE-4','First two clauses proved; third clause refuted by D.12 and the position of E2_1,0.'),
('EHN2019 Remark 3.2','Refuted by D.7: 28 private ternary tuples give a 1-sparse relation whose shadow contains K8.')]:
 add(i,'used and rechecked in this run' if not i.startswith('Lead') and i!='FE-4' and 'Remark' not in i else 'targeted proof check',detail)
add('FE-4','refuted, with the refined statement\'s id','D.12 corrects the spectral sequence and proves T1(u_!F)=0.')
add('EHN2019 Remark 3.2','refuted, with the refined statement\'s id','D.7 gives the valid shadow threshold and direct hypergraph replacement.')
with (root/'CHECK_EVENTS_D.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print('Wrote',len(rows),'result rows and',len(events),'check events.')
