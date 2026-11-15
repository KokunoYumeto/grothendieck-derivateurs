"""Build the E/F rows for the shared GALOIS statement register."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = [
('E.1','Proved','Equivalence of local-system infinity categories is detected by maps into the coefficient core and arrow core.','C.1','Lead1; Part E','Two test objects do not alone construct a derivator.'),
('E.2','Proved','For an E-infinity ring R, the derivator of presentable R-linear stable categories realizes W_ModR^lc as its constant-coefficient class.','E.1;C.6','Lead1; Part E','Specified monoidal enhancement; all small indexing shapes; larger coefficient universes; zero ring included.'),
('E.3','Proved','The Hom-category constant tests in presentable R-linear categories yield the same class as the ordinary-derivator realization.','E.2','Part E; Di Vittorio comparison','Does not assert every HDer axiom for an enriched-shape extension.'),
('E.4','Proved','The specified second rational categorical stage detects K(Z/p,2) for every prime p and K(Z,2), and is strictly smaller than the first stage.','E.2;C.7','Lead4; Part E','Uses units in Q(zeta_p), and powers of 2 in Q.'),
('E.5','Known','The specified finite-type coefficient tower is W0 superset W1 superset ... with intersection W_infinity.','C.4','Lead4; CATHOT C.1-C.4','Does not characterize a canonical raising operation on arbitrary derivators.'),
('E.6','Known','The attached Di Vittorio accepted v2 proves HDer1-HDer4 for enriched models and leaves HDer5 as Conjecture3.2.23.','','Recent results; Part E and G','Shift invariance of all five assumed axioms is proved; enriched shapes differ from ordinary Cat.'),
('E.7','Proved','Every accessible W_D^lc is realized by the derivator of its localized spaces; this applies to every presentable infinity-category coefficient and is functorial for specified inclusions of localizers.','B.3;B.4','Part E','Uses product stability and Cisinski2006 Theorems4.2.15,1.4.3; unrestricted derivator-morphism functoriality is not asserted.'),
('E.8','Proved','The full second linear stage consists of component-bijective maps whose based-loop maps are Wlc_ModR; for Hk this is pi1/pi2 isomorphism plus k-homology equivalence of 2-connected covers.','E.1;E.2;C.7','Lead4; Part E','For Q equivalently exact pi0/pi1/pi2 and rational higher homotopy. Uses canonical free-linear-presheaf algebra map and monadicity, including disconnected loops.'),
('E.9','Proved','Every 2-connected rationally acyclic space is invisible to the specified second rational categorical stage; in particular K(Z/p,3).','E.1;E.4;E.8','Lead4; Part E','Independent Postnikov proof; both coefficient core and arrow core have rational homotopy groups above degree two.'),
('E.10','Proved','The rational loop tower is realized at all stages by ordinary localized-space coefficient derivators, with strict exact-rational stages and intersection W_infinity; the intersection conclusion extends to every accessible component-detecting initial LC class.','B.3;B.4;C.7;E.7;E.8;G.1','Lead4; Part E','Includes every nonterminal presentable initial coefficient. The first linear coefficient category may be retained; later localized-space coefficients are not asserted to be higher linear categories.'),
('E.11','Open','Functorial coefficient raising on all bare derivators and all their morphisms, and realization of the higher rational stages by higher Q-linear categories, remain unresolved.','E.2;E.7;E.8;E.10','Lead4; Part E','Full ordinary tower and its intersection are constructed; only higher linear-categorical realization remains separate.'),
('F.1','Proved','All-set local systems with their designated evaluation functors recover the fundamental groupoid, whereas finite-set Galois theory is profinite.','','Part F; SGA1 comparison','Yoneda reconstruction; empty and disconnected cases included; CATHOT reflector cited without reproof.'),
('F.2','Proved','Enhanced R-linear local systems with a coherent evaluation functor reconstruct R[Omega X] as an E1 algebra and reconstruct the many-object linear path category.','E.2','Part F','Recover the specified algebra via the evaluation monad, not only a Morita class.'),
('F.3','Proved','The enhanced infinity-topos of space-valued local systems has shape X; designated enhanced fiber functors recover X; the homotopy category plus specified constant functor recovers X in Hot.','','Part F','Known shape construction, independently proved; constant functor is additional named datum in ordinary formulation.'),
('F.4','Known','For a locally connected Grothendieck topos, locally constant sets are split representations of its fundamental pro-groupoid; the classifying topos is their filtered-colimit completion.','','Part F; Longue Marche Sections1-4','Hoyois Thm3.13 and Cor3.20; retains covering-family data; no unsupported claim LC always a topos.'),
('F.5','Known','Kaledin Cor6.1.2.5 reconstructs spaces from enhanced groupoid families; Thm7.3.1.3 is the general enhanced-category representability theorem.','','Part F; Recent results','Exact Pos and Pos+ shapes and uncountable regular size bounds retained; Chapters6-7 preliminary.'),
('F.6','Proved','Raising coefficients and varying shapes are different reconstruction procedures; Pi1 Map(BJ,X) cannot be replaced by Map(BJ,Pi1X).','E.5;F.3;F.5','Part F; CATHOT F.11 comparison','Finite tetrahedral face poset and K(Z,2) witness; exact program output attached.'),
('F.7','Proved','The recognition condition W_C^lc=W_infinity is reflection of specified map equivalences by the local-system functor; the computed positive and negative cases are listed.','E.1;C.4;C.5;C.7;C.10','Part F','General rings and E-local spectra inherit qualifications from Part C.'),
('F.8','Open','The literal bare ordinary category plus ordinary fibers is not proved here to reconstruct loop-chain E1 algebras, or spaces without additional structure.','F.2;F.3','Part F','Exact gap is recovery of coherent monad data; not presented as a counterexample.')
]
rows=[]
for i,s,t,d,p,n in data:
    rows.append(dict(id=i,statement=t,status=s,where_proved=f'GALOIS_paper.tex, Part {i[0]}, {i}',depends_on=d,manuscript_rows_or_pages_settled=p,notes=n))
out=root/'research'/'EF_results.json'
out.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print(f'{len(rows)} E/F statements registered.')
print('Status counts:',{s:sum(r['status']==s for r in rows) for s in ('Proved','Known','Open','Refuted')})
