"""Write the Part C contribution to the master statement register."""
import json
from pathlib import Path
rows=[
('C.1','For locally small complete infinity coefficients, full faithfulness/equivalence of the specified restriction is detected by its homotopy-category restriction.','Proved','','I ms.99-100; Part B enhancement question','Cotensors by all small spaces supply the required mapping-space tests.'),
('C.2','For complete and cocomplete enhanced coefficients, cohomological, homological, and 1-complete equivalences coincide and are precisely maps with coefficient-acyclic homotopy fibers.','Proved','C.1','I ms.106,113; Lead1','Uses groupoid Kan formulas; does not silently assert the same for arbitrary derivators.'),
('C.3','Constant coefficient equivalences are exactly the maps whose tensor with every coefficient object is an equivalence.','Proved','','I ms.60-66; X ms.1-5','Includes empty and infinitely disconnected indexing spaces.'),
('C.4','For r-types, W=W_r; the middle class is pi0 bijective, pi_i iso through r, and pi_(r+1) onto; Wlc=W_(r+1).','Proved','C.1;C.2;C.3','Lead2; Parts C and F','Sets and groupoids are r=0 and r=1. CATHOT reflector statement cited without reproof.'),
('C.5','Finite truncation stages have both strict inclusions and W1 fails two-out-of-three; for spaces all classes equal W_infinity.','Proved','C.4','Lead1; Lead2; Part B','Explicit maps * -> K(A,r+1) -> *.'),
('C.6','For a connected pointed space, local systems of k-modules are modules over chains on its based loop space; restriction is along the specified loop-algebra map.','Known','LurieHA4.7.3.5;SchwedeShipley5.1.6;RiveraZeinalian9.2','Part C; Part F','No finite type, nilpotence, or simply connected restriction.'),
('C.7','For any nonzero associative unital ring: constants test k-homology, middle classes test k-acyclic homotopy fibers, and Wlc tests pi0/pi1 plus universal-cover k-homology.','Proved','C.2;C.3;C.6','Lead2; Part C','Loop-algebra proof; integral bar/cobar followed by scalar extension; zero ring handled separately.'),
('C.8','W1 is the homological-epimorphism condition B tensor_A B -> B; for every prederivator W and W1 coincide on maps to the point.','Proved','C.6','CATHOT addendum; I ms.99-100','Refutes the prompt assertion that BA -> * for acyclic A is not 1-complete; reversing the map gives the intended separation.'),
('C.9','Ring homology tests are detected by rational homology when characteristic zero and mod-p homology for primes not inverted in k; Wlc_k=W_infinity iff no prime is invertible.','Proved','C.7','Lead2; Part C; Part F','Includes all nonzero associative unital rings; integral Whitehead proof supplied.'),
('C.10','For spectra: constants are integral homology equivalences, middle classes have integral-acyclic fibers, and Wlc=W_infinity.','Proved','C.2;C.3;C.6;C.7;C.9','Lead2; Part C; Part F','Uses bounded-below stable Hurewicz detection only where it applies.'),
('C.11','For E-local spectra: constants are E-homology equivalences, middle classes have E-acyclic fibers, and Wlc is component bijection plus E-homology equivalence of based loops.','Proved','C.2;C.3;C.6','Part C; Part F','Nonzero E; zero E separately. For Morava K(n), Wlc strictly exceeds weak equivalences. No unsupported replacement of loop tests by cover tests.'),
('C.12','The Wlc < W1 < W inclusions are strict for every nonzero ring, spectra, and nonzero E-local spectra; rational and mod-p Wlc also strictly exceed W_infinity.','Proved','C.7;C.8;C.10;C.11;B.10','Lead2; CATHOT addendum','Explicit acyclic presentation CW complex, finite A5 quotient, code/output, and corrected acyclic-group examples.'),
('C.13','Wlc_D(Q) is the established pi1-rational/fiberwise-rational equivalence class, with GHT finite-type algebraic models where applicable.','Known','C.7;RiveraWierstraZeinalian2021Theorem3;GHT2000Theorems5.10,5.11,6.2,6.4','Lead2; Part C','Finite-type condition belongs to GHT models, not to the equivalence-class calculation.'),
('C.14','Rational Wlc implies Toën schematization equivalence, strictly; the discrete pi1 test is stronger than proalgebraic pi1 plus finite-dimensional cohomology.','Proved','C.2;C.7;B.10;Toen2006Lemma3.3.2,Theorem3.3.4','Part C','Uncountable acyclic simple group supplies strictness; reverses a typo after Toën Definition3.1.1.'),
('C.15','The full coefficient table and empty/disconnected/idempotent edge cases follow from the preceding exact calculations.','Proved','C.4;C.5;C.7;C.10;C.11','Part C','All requested coefficient cases included with the exact middle class.')]
fields=('id','statement','status','depends_on','manuscript_rows_or_pages_settled','notes')
data=[]
for row in rows:
 d=dict(zip(fields,row));d['where_proved']='GALOIS_paper.tex, Part C, '+d['id'];data.append(d)
out=Path('GALOIS/research/C_results.json');out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(data),'numbered Part C result records to',out)
