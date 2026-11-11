"""Build the claim register for the independently written manuscript audit."""
from pathlib import Path
import re,csv,collections

root=Path(__file__).resolve().parents[1]
source=root/'sections'/'A.tex'
claims=re.findall(r'\\begin\{claim\}\{(A\.\d+)\}\{(Proved|Refuted|Known|Open)\}\{([^\n]*)\}\s*(.*?)\\end\{claim\}',source.read_text(),re.S)
meta={
1:('direct source comparison','XVI ms.1--3','Literal absolute Loc (3) is not the adopted relative axiom.'),
2:('pullback associativity','XII ms.207--209; GALOIS D.1','No two-out-of-three needed for composition and base-change closure; retract premise explicit.'),
3:('A.2; code/a_finite_audit.py','XII ms.210,220; GALOIS A.5','Full faithfulness on coefficients need not satisfy two-out-of-three.'),
4:('A.3','XII ms.226--227,248','Raw pullback is proved homotopical only for the stated class; postcomposition works for every map.'),
5:('A.3--A.4','XII ms.222','The preliminary base-change universal quantifier is indispensable.'),
6:('elementary antitone adjunction','II ms.83--89, (6.7)','Right-hand domain requires pullback closure, not composition closure.'),
7:('A.6','II Proposition 6.1, ms.88--89','Correct composition criterion for a closed transporter pair.'),
8:('code/a_finite_audit.py','II first versions (6.2)--(6.5)','W is composition-closed but not two-out-of-three, exactly as permitted in II section 6.'),
9:('A.6--A.7; relative Theorem A','II ms.66,89; XII ms.225--226','Smooth/proper are asphericity stabilizers, not the mixed transporters into W.'),
10:('localization universal property','XII ms.215--218; XIIc B055--B065','Axiom a gives equality of strong saturations; b is equality of the original restricted classes.'),
11:('A.2; two-out-of-three','XIII ms.10--11; XVI 4.4.1','No chosen functorial factorization or terminal object needed.'),
12:('A.11; localization universal property','XII ms.217--218; XIIc B060--B065','Sufficient extra replacement hypothesis, not proof from a and b alone.'),
13:('A.10; E.12; code/a_b062_verify.py','XII ms.207,217--218; XIIc B062','Six-object finite lattice refutes a+b implies c at every-base scope; W strongly saturated; enhanced version also fails.'),
14:('A.3--A.4','XII ms.225--227','The c of ms.227 is an adjunction axiom, different from c of ms.218.'),
15:('direct source comparison','XVI ms.27--41; POLES A.5--A.6','Four fibration notions and eight reference/factorization variants kept separate.'),
16:('A.11; universal comparison maps','XVI 4.4.1,4.4.9,4.4.10; POLES A.13--A.14','Replacement transfer in B needs commuting squares; functoriality suffices.'),
17:('A.16; Brown 1973 I.4 Lemmas 1--2','XVI 4.4.3; POLES A.13','Complete relative mapping-path proof, with all terminal-map premises.'),
18:('code/a_finite_audit.py; rational averaging','I ms.117--118; GALOIS D.3','Finite covering/opfibration counterexample independently reconstructed.'),
19:('adjunction; pointwise base change; Yoneda','I ms.79--81,117--123; GALOIS D.2','Weak constant-coefficient conclusion distinguished from all local systems.'),
20:('code/a_finite_audit.py','I ms.102; Ib-C003; GALOIS D.9; STRATA D.5','Proper cosieve has comma transition empty to point.'),
21:('A.2,A.4,A.11,A.12','XII ms.241--248','Finite product universal property proved by localizing the product/diagonal adjunction.'),
22:('A.11; arrow reversal','XIII ms.7--12,27--28; PATHS D.17','Historical exactness W=TF composed TC is distinguished from one-sided equality.'),
23:('lifting adjunction','XIII ms.45--50','Presheaf variance fixes comma orientation and walking-arrow fibrancy.'),
24:('code/a_finite_audit.py','XIII ms.45--50','Ordinary limit of an objectwise weak equivalence may fail to be weak.'),
25:('Alexandrov closed sets; infinite Ramsey theorem','XIII ms.60--67','Noetherian and sober Alexandrov posets are finite; companion observation independently verified.'),
26:('finite-set product and coproduct universal properties','XIII ms.50--59; PATHS D.9','Finite intrinsic floor does not imply infinite Kan extensions.'),
27:('two lifting pairs; Riehl 2014 Lemma 11.3.3','XIII ms.27--29,57','Closedness plus exactness DOES imply both trivial-class equalities; the added premise is essential.'),
28:('A.17,A.23,A.25,A.27; Quillen 1967 I.1 Theorem 1 and I.4 Theorem 3','XIII ms.57--72','All u with existing ordinary Kan extension are admissible under the actual uniform closed exact premise.'),
29:('A.6; code/a_finite_audit.py','II section 5, ms.69--80, especially (5.20)','The final closure on the supremum and the distinction element/principal lower set are required.'),
30:('code/a_finite_audit.py','II ms.65--67','A union of composition-closed pullback-closed classes need not compose.'),
31:('direct source comparison; comma definitions','VI ms.81--84; XII ms.222--225','Higher-category 2026 claims not used as proof inputs.'),
32:('A.1; Quillen 1973 Theorem A; code/a_absolute_relative.py','XVI Loc (1,2,3)/(3 bis); POLES A.16','Component-dependent class satisfies literal moderate saturation and absolute A but fails relative A over BC2. It is not closed under all arrow retracts.'),
33:('code/a_finite_audit.py','XII ms.273--275; POLES G.17--G.18','Strongly saturated isomorphisms on finite sets refute the converse and the unqualified corollary.'),
34:('A.6; code/a_finite_audit.py','II cancelled section 4, ms.65--68','Stabilizers are not antitone for arbitrary input classes.'),
}
header=['id','statement','status','where_proved','depends_on','manuscript_rows_or_pages_settled','notes']
with (root/'A_results.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(header)
    for ident,status,title,body in claims:
        number=int(ident.split('.')[1]);deps,pages,note=meta[number]
        body=re.sub(r'\s+',' ',body).strip()
        writer.writerow([ident,title+'. '+body,status,'sections/A.tex, '+ident,deps,pages,note])
assert len(claims)==34
counts=collections.Counter(status for _,status,_,_ in claims)
log=f'Wrote {len(claims)} A claims to A_results.csv\nStatus counts: {dict(sorted(counts.items()))}\nAll rows have source locations, dependencies, and scope notes.\n'
(Path(__file__).with_suffix('.out.txt')).write_text(log)
print(log,end='')
