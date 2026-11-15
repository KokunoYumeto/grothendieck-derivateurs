"""Build the A/KT contribution to the result register from explicit metadata."""
from pathlib import Path
import json

rows = [
    ("A.1", "The fibred and opfibred Grothendieck constructions give the specified span C <- C_u -> C_infinity; no general direct C -> C_infinity functor is supplied.", "Proved", "", "VII ms.99-110; VIIb-C026", "Variance and map directions fixed explicitly."),
    ("A.2", "For every filtered indexing category A and every D:A->Cat, the canonical Grothendieck-total-category to Cat-colimit functor is a weak equivalence; the sequential fibred version follows by opposites.", "Proved", "A.1", "VII ms.108-109; VIIb-C026", "No full-faithfulness, injectivity, or fibrancy of transition functors. Componentwise extension includes empty A."),
    ("A.3", "A base functor u:J->T induces weak equivalences of fibred total categories for every strict F:T^op->Cat iff every u/t is weakly contractible.", "Proved", "A.1; A.2", "VII ms.99-110; VIIb-C026", "Necessity is for all F, not for a specified diagram or the restricted homotopy-hypothesis class."),
    ("A.4", "Preorder cofinality plus homotopy of parallel reindexing maps does not imply the total/sequential comparison is a weak equivalence.", "Refuted", "A.1", "VII ms.99-109; VIIb-C026", "T=B C2, constant terminal fibre, constant identity sequence. The manuscript already identifies this obstruction. Full finite check attached."),
    ("A.5", "Total W_infinity-asphericity of A does not make every Cat-valued colimit homotopically correct: for Delta_inj and D([n])=B N^(n+1), the total category has integral H_k=Z in every degree whereas the Cat colimit has type S1.", "Refuted", "A.6", "After TOTASPH correction; VIIb-C026", "Positive-degree homology diagrams are projective representables; no need to assume general exactness to calculate total homology."),
    ("A.6", "Delta_inj has exact abelian-group-valued colimits and is totally W_infinity-aspherical but is not filtered.", "Proved", "", "TOTASPH C.7-C.10 verification", "Full independent recheck of the integral affine-cone argument supplied."),
    ("A.7", "For nonempty connected shapes, filtered categories are contained in the universally correct Cat-colimit shapes, which are strictly contained in the totally W_infinity-aspherical shapes.", "Proved", "A.2; A.5; A.6", "Part A; VIIb-C026", "Discrete diagrams prove the necessary upper bound. Property is componentwise for disconnected A."),
    ("A.8", "An exact intrinsic classification of universally correct Cat-colimit shapes, including whether all connected such shapes are filtered, remains unresolved here.", "Open", "A.7", "Part A", "Exact gap and residual infinite-with-no-weakly-terminal scope recorded; no claim of literature-wide openness."),
    ("A.9", "The last-element map sd P->P for the six-face triangle-boundary poset is a weak equivalence with no inverse modulo zigzags of natural transformations; all 456 reverse monotone maps have degree zero.", "Proved", "", "POLES D.6 verification; VIIc-A046; V-I066", "Full finite enumeration and output attached. Does not itself decide the particular path map q_L."),
    ("D.K1", "An acyclic map of small CW spaces is an epimorphism in the unpointed homotopy category, with weakly equivalent double-pushout codiagonal.", "Proved", "", "GALOIS B.9 verification; CATHOT E.17 reduction", "Classical claim with checked primary citations and complete proof."),
    ("D.K2", "Every small group embeds in a simple nonabelian integrally acyclic group of any prescribed infinite small cardinality at least its size.", "Proved", "", "GALOIS B.10 verification; KT_mu", "Simultaneous HNN and mitosis construction, including cardinal control, independently checked."),
    ("D.K3", "KT_mu holds: every connected small CW complex has an acyclic BG presentation whose perfect kernel is killed by every homomorphism to any group of size at most mu.", "Proved", "D.K2", "GALOIS B.11 verification; KT_mu; CATHOT E.17", "Subcomplex injectivity induction, twisted homology, kernel description, and all universe bounds verified."),
    ("D.K4", "If a presheaf ind-represented by a nonempty small filtered system of categories modulo natural transformations inverts W_infinity on all small shapes, it inverts W_1 and the specified groupoid-completion unit is an ind-isomorphism with the same indexing category.", "Proved", "D.K1; D.K3", "GALOIS B.12 verification; CATHOT E.17", "No space representability premise. Empty test shapes, arbitrary components, and noninvertible endomorphisms included."),
    ("D.K5", "All-small-shape homotopy invariance of the constant-to-constant localization Hom functor for a small relative category forces factorization through Pi_1; if represented by a space, that space is a 1-type.", "Proved", "D.K4", "V ms.44-46; Lead 3 size correction; CATHOT E.17", "The countable path system satisfies the small-index hypothesis. Bounded shape classes do not support this conclusion."),
]
out = []
for ident, statement, status, depends, pages, notes in rows:
    section = "sections/D_kt.tex" if ident.startswith("D.") else "sections/A_colimits.tex"
    out.append(dict(id=ident, statement=statement, status=status,
                    where_proved=f"{section}, {ident}", depends_on=depends,
                    manuscript_rows_or_pages_settled=pages, notes=notes))
dest = Path(__file__).resolve().parents[1] / "research/A_results.json"
dest.write_text(json.dumps(out, indent=2) + "\n")
print(f"Wrote {len(out)} entries to {dest.name}.")
print({s: sum(r['status'] == s for r in out)
       for s in ['Proved', 'Refuted', 'Known', 'Open']})
