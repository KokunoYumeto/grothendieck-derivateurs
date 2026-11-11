"""Build the E/F registry from the exact final statement text and audit data."""
import csv
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIELDS=("id","statement","status","where_proved","depends_on",
        "manuscript_rows_or_pages_settled","notes")
DATA={
"E.1":("A.3;A.4","XII ms.207–208, 216–218, 226","Raw slice adjunction only along the testing class; all postcomposition functors descend."),
"E.2":("E.1;B.1","XII ms.226; Lead 3","Exact endpoint counterexample; ef_finite_checks.py."),
"E.3":("","VI ms.108–113; XII ms.225–227","Enhanced compact-projective presentation is an explicit extra hypothesis; it is not inferred from enough intrinsic fibrations."),
"E.4":("E.3;F.2","VI ms.138–169; XII ms.226","Presentable coefficient version; canonical mates and exact comma comparisons."),
"E.5":("E.3;B.3;B.8;D.2;EFCisinski2009","VI ms.81–84, 108–113","Coarse equals locally constant only after the extra coarse comparison."),
"E.6":("B.1","VI ms.108–113; arbitrary-W lead","BC2 with component equivalences; fine local systems retain a regular action lost by total localization."),
"E.7":("A.2;EFCisinski2019","XII ms.240–261; XIII ms.7–12; PATHS D.8,D.17,D.18","Brown finite floor; no all-small strict diagram rectification."),
"E.8":("E.7;EFCisinski2006;B.11","XVI Loc (7 F); POLES E.2–E.3","Necessity of aspherical generation does not use accessibility; model equivalences do."),
"E.9":("B.19;E.7","XVI Loc (7 F); PATHS E.5","Universal source evaluation is required for the indicated mapping-path transfer."),
"E.10":("","VI ms.83–84; OpenAI family 312 lead","Proved ordinary-groupoid test; no dependence on the unrefereed globular model claim."),
"E.11":("A.12","XII ms.217–218; XIIc B062","Functorial coaugmented W-replacement proves the stronger intermediate assertion."),
"E.12":("A.10","XII ms.217–218; XIIc B062","Six-element lattice counterexample; both ordinary and enhanced localizations; a_b062_verify.py."),
"E.13":("","PATHS D.20; STRATA C.7","Coherent arrow category differs from arrows in the homotopy category; derived integer-coefficient example."),
"E.14":("E.8;EFRijkeShulmanSpitters2020","POLES E.2–E.3 modality/LCC comparison","Accessible localizations of spaces; explicit proof of the LCC converse using point diagrams."),
"F.1":("EFGroth2013;EFGPS2014a;EFMaltsiniotis2012","I; VI ms.138–169","Der 1–4 and canonical mate pasting; no strongness assumed."),
"F.2":("F.1;B.5;EFGPS2014a","VI ms.138–169; STRATA D.4","Converse tests terminal coefficients on the left adjoint mate, not on the original right comparison."),
"F.3":("F.1","Lead 3","Empty endpoint pullbacks; exact finite checks and nonzero stable version."),
"F.4":("F.2;EFGPS2014b","Lead 3; VI projection formulas","Internal formula for smooth maps or locally constant second coefficient; external formula for all maps."),
"F.5":("F.4","Lead 3","Monoidality alone is insufficient for the internal projection formula; finite endpoint check."),
"F.6":("F.2;G.1","Lead 3","Global dualizability or pointwise preservation of fibre limits is stated explicitly."),
"F.7":("F.2;F.4","VI exchange formulas","Closed exchange and right-adjoint mates; all source and target functors specified."),
"F.8":("F.1;B.5;EFGPS2014b","VI ms.84","Both coefficient opposition and base opposition are needed to reverse adjunctions."),
"F.9":("EFGroth2013","I; VI open–closed formulas","Coherent sequences without Der5; strongness only for triangulated recollement."),
"F.10":("F.2;F.4;EFMann2022","Lead 3; Mann correspondence question","Base is nerve of ordinary Cat with strict pullbacks; enhancement and separate cocontinuity explicit."),
"F.11":("F.10;F.6;G.8","Lead 3 terminology","Kan exceptional inverse image is restriction; Grothendieck properness does not make left and right Kan functors equal."),
"F.12":("F.10;EFHeyerMann2024","Mann versus later geometric-setup conventions","All-smooth class fails diagonal closure; discrete fibrations give a precise smaller setup."),
"F.13":("EFHormann2017","Hörmann comparison","Theorem 6.12 is used with its actual pre-multiderivator hypotheses; no enhancement is manufactured."),
"F.14":("F.2;EFAnelWeinberger2025","Anel–Weinberger comparison","Indexed presheaf calibration over the ordinary base Cat, not an unstated Cat-infinity pullback theorem."),
"F.15":("EFJansen2023;EFKentLeiningerSchleimer2009","STRATA genus-zero comparison","Explicit mapping-class quotient category; stability range and coefficient hypotheses fixed."),
"F.16":("F.15;B.5;EFKentLeiningerSchleimer2009","STRATA forgetting-mark question","Proper for every n>=3; at n=4 an incoming lifting category is BZ, so not smooth."),
"F.17":("F.15;F.16;D.6;EFKeel1992","STRATA geometric direct image and boundary base change","Constructibility checked; fibre exit categories and replete boundary cosieves identify the canonical comparisons."),
"F.18":("C.10","Strict nCat-indexing question","No proof depends on OpenAI 2026; first undecided case n=2 needs a higher Der4 and mate compatibility."),
"F.19":("F.2;F.12;EFHeyerMann2024","Mann proper-class question","Exact cohomological properness classification for discrete fibrations with spectra or nonzero commutative-ring coefficients; canonical norm only after checking diagonal properness."),
}
rows=[]
for path in (ROOT/"sections/E.tex",ROOT/"sections/E_b062.tex",ROOT/"sections/F.tex"):
    text=path.read_text()
    for match in re.finditer(r"\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{",text):
        start=match.end(); depth=1; i=start
        while depth:
            if text[i]=="{" and (i==0 or text[i-1]!="\\"): depth+=1
            if text[i]=="}" and (i==0 or text[i-1]!="\\"): depth-=1
            i+=1
        title=text[start:i-1]
        end=text.index(r"\end{claim}",i)
        ident,status=match.group(1,2)
        dependencies,pages,notes=DATA[ident]
        statement=re.sub(r"\s+"," ",title+". "+text[i:end]).strip()
        rows.append(dict(zip(FIELDS,(ident,statement,status,
             f"BISITE_paper.tex, Part {ident[0]}, statement {ident} and its proof ({path.relative_to(ROOT)})",
             dependencies,pages,notes))))
rows.sort(key=lambda row:(row["id"][0],int(row["id"].split(".")[1])))
assert len(rows)==33 and len({r["id"] for r in rows})==33
with (ROOT/"EF_results.csv").open("w",newline="") as stream:
    writer=csv.DictWriter(stream,fieldnames=FIELDS);writer.writeheader();writer.writerows(rows)
from collections import Counter
log=f"Registered {len(rows)} exact E/F statements.\nStatuses: {dict(Counter(r['status'] for r in rows))}\n"
Path(__file__).with_suffix(".out.txt").write_text(log)
print(log,end="")
