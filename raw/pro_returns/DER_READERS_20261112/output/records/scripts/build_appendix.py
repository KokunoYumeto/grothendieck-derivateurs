#!/usr/bin/env python3
"""Build the source-faithful new-results appendix and integrate the companion.

Run from the delivered records directory with --source pointing at the extracted
DER_03 archive, and --output pointing at the companion output directory. No
network call, external personal path, or unshipped research return is required.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path

SYMBOLS = {
    'Γ':r'\Gamma','Δ':r'\Delta','Λ':r'\Lambda','Π':r'\Pi','Σ':r'\Sigma','Φ':r'\Phi','Ψ':r'\Psi','Ω':r'\Omega',
    'α':r'\alpha','β':r'\beta','γ':r'\gamma','δ':r'\delta','ε':r'\varepsilon','ζ':r'\zeta','η':r'\eta',
    'θ':r'\theta','ι':r'\iota','κ':r'\kappa','λ':r'\lambda','μ':r'\mu','π':r'\pi','ρ':r'\rho','τ':r'\tau',
    'φ':r'\varphi','χ':r'\chi','ψ':r'\psi','ω':r'\omega','ℵ':r'\aleph',
    '←':r'\leftarrow','→':r'\to','↓':r'\downarrow','↔':r'\leftrightarrow','↠':r'\twoheadrightarrow',
    '↦':r'\mapsto','⇉':r'\rightrightarrows','⇐':r'\Leftarrow','⇒':r'\Rightarrow','⇔':r'\Leftrightarrow',
    '⟹':r'\Longrightarrow','∂':r'\partial','∅':r'\varnothing','∈':r'\in','∉':r'\notin','∋':r'\ni',
    '∎':r'\blacksquare','∏':r'\prod','∐':r'\coprod','−':'-','∖':r'\setminus','∘':r'\circ','∞':r'\infty',
    '∤':r'\nmid','∧':r'\wedge','∨':r'\vee','∩':r'\cap','∪':r'\cup','∫':r'\int','∼':r'\sim',
    '≃':r'\simeq','≅':r'\cong','≠':r'\ne','≡':r'\equiv','≤':r'\leq','≥':r'\geq',
    '⊂':r'\subset','⊃':r'\supset','⊄':r'\not\subset','⊆':r'\subseteq','⊊':r'\subsetneq',
    '⊔':r'\amalg','⊕':r'\oplus','⊗':r'\otimes','⊠':r'\boxtimes','⊣':r'\dashv','⋁':r'\bigvee',
    '⋂':r'\bigcap','⋃':r'\bigcup','⋆':r'\star','⋊':r'\rtimes','□':r'\square','△':r'\triangle',
    '▷':r'\triangleright','◁':r'\triangleleft','⟨':r'\langle','⟩':r'\rangle',
    '𝒞':r'\mathcal C','𝒟':r'\mathcal D','𝒢':r'\mathcal G','𝒦':r'\mathcal K','𝒩':r'\mathcal N',
    '𝒫':r'\mathcal P','𝒮':r'\mathcal S','𝒯':r'\mathcal T','𝒳':r'\mathcal X','𝒵':r'\mathcal Z',
    '𝓕':r'\mathcal F','𝔑':r'\mathfrak N','ℋ':r'\mathcal H','×':r'\times','±':r'\pm',
    '·':r'\cdot','′':r'\prime','″':r'\prime\prime',
}
SUP = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿʳˢᵏ','0123456789-nrsk'))
SUB = dict(zip('₀₁₂₃₄₅₆₇₈₉','0123456789'))
ESC = {'&':r'\&','%':r'\%','$':r'\$','#':r'\#','{':r'\{','}':r'\}',
       '\\':r'\textbackslash{}','~':r'\textasciitilde{}'}

def tex(s: str, markup: bool=True) -> str:
    """Literal prose, source Markdown emphasis, and an explicit glyph morphism.

    ASCII mathematical scripts become typographic scripts; Unicode mathematical
    characters map individually to their standard TeX glyph. No assertion,
    quantifier, index, equation, or logical connective is rewritten.
    """
    out=[];i=0
    while i < len(s):
        c=s[i]
        if markup and s.startswith('**',i):
            j=s.find('**',i+2)
            if j>=0:
                out.append(r'\textbf{'+tex(s[i+2:j])+ '}');i=j+2;continue
        if markup and c=='`':
            j=s.find('`',i+1)
            if j>=0:
                val=s[i+1:j]
                if re.search(r'\.(?:md|tex|py|out|csv|json)\b',val) or '/code/' in val:
                    out.append(r'\path{'+val.replace('\\','/')+'}')
                else:out.append(tex(val,False))
                i=j+1;continue
        if markup and c=='*' and (i==0 or s[i-1].isspace() or s[i-1]=='('):
            j=s.find('*',i+1)
            if j>=0 and '\n\n' not in s[i:j] and len(s[i:j])<200:
                out.append(r'\emph{'+tex(s[i+1:j],False)+'}');i=j+1;continue
        if c in '^_' and i+1<len(s):
            j=i+1;atom=''
            if s[j]=='{':
                depth=1;k=j+1
                while k<len(s) and depth:
                    depth+=(s[k]=='{')-(s[k]=='}');k+=1
                if depth==0:atom=s[j+1:k-1];j=k
            elif c=='_' and s[j]=='(':
                k=s.find(')',j+1)
                if k>=0:atom=s[j:k+1];j=k+1
            elif s[j].isalnum() or s[j] in '*∞αβγδεζηθικλμπρτφχψω':
                k=j+1
                if c=='_':
                    while k<len(s) and s[k].isalpha() and s[k].isascii():k+=1
                atom=s[j:k];j=k
            if atom:
                out.append(('\\textsuperscript{' if c=='^' else '\\textsubscript{')+tex(atom,False)+'}')
                i=j;continue
            out.append(r'\textasciicircum{}' if c=='^' else r'\_');i+=1;continue
        if c in SUP or c in SUB:
            table=SUP if c in SUP else SUB;j=i
            while j<len(s) and s[j] in table:j+=1
            out.append(('\\textsuperscript{' if table is SUP else '\\textsubscript{')+''.join(table[x] for x in s[i:j])+'}')
            i=j;continue
        if i+1<len(s) and s[i+1] in '\u0303\u0304\u0302':
            accent={'\u0303':'widetilde','\u0304':'overline','\u0302':'widehat'}[s[i+1]]
            base=SYMBOLS.get(c,c)
            out.append('\\ensuremath{\\'+accent+'{'+base+'}}');i+=2;continue
        if c in ['ỹ','Ū','Ỹ','Ṫ']:
            out.append({'ỹ':r'\ensuremath{\widetilde y}','Ū':r'\ensuremath{\overline U}',
                        'Ỹ':r'\ensuremath{\widetilde Y}','Ṫ':r'\ensuremath{\dot T}'}[c])
        elif c in SYMBOLS:out.append(r'\ensuremath{'+SYMBOLS[c]+'}')
        elif c=='–':out.append('--')
        elif c=='—':out.append('---')
        elif c=='…':out.append(r'\ldots{}')
        elif c=='<':out.append(r'\ensuremath{<}')
        elif c=='>':out.append(r'\ensuremath{>}')
        elif c=='^':out.append(r'\textasciicircum{}')
        elif c=='_':out.append(r'\_')
        else:out.append(ESC.get(c,c))
        i+=1
    return ''.join(out)

def md(s: str) -> str:
    """Convert the limited, explicitly inspected source Markdown grammar."""
    out=[]
    for block in re.split(r'\n\s*\n',s.strip()):
        if re.fullmatch(r'\s*[-*]{3,}\s*',block):continue
        if block.startswith('## '):
            out.append(r'\subsection*{'+tex(block.split('\n',1)[0][3:])+'}')
            if '\n' in block:out.append(md(block.split('\n',1)[1]))
        elif re.match(r'^\d+\. ',block):
            items=re.split(r'(?m)^\d+\. ',block)[1:]
            out.append('\\begin{enumerate}\n'+'\n'.join('\\item '+tex(x.strip()) for x in items)+'\n\\end{enumerate}')
        elif block.startswith('- '):
            items=re.split(r'(?m)^- ',block)[1:]
            out.append('\\begin{itemize}\n'+'\n'.join('\\item '+tex(x.strip()) for x in items)+'\n\\end{itemize}')
        elif all(x.startswith('    ') for x in block.splitlines() if x.strip()):
            out.append('\\begin{quote}\n'+tex('\n'.join(x[4:] for x in block.splitlines()))+'\n\\end{quote}')
        elif block.startswith('> '):out.append('\\begin{quote}\n'+tex(re.sub(r'(?m)^> ?','',block))+'\n\\end{quote}')
        else:out.append(tex(block.replace('\n',' ')))
    return '\n\n'.join(out)+'\n'

def take_section(s,number):
    p=re.search(r'^## '+str(number)+r'\. .+$',s,re.M)
    end=re.search(r'^## \d+\.',s[p.end():],re.M)
    return s[p.end():p.end()+end.start() if end else len(s)].strip()

READINGS={
1: r'''The argument explicitly connects the surjective group map $eMe\to U(M)$ to a map of classifying spaces through the Karoubi envelope; section~12 below reproduces that construction. The bounded-homology implication then uses the cohomological result reproduced in section~2, and the finite-generation input is supplied by the degreewise finite bar complex. The finite-complex conclusion invokes Hatcher's Proposition~4C.1; the positive realization assertion in Corollary~2.5 invokes Theorem~C of the stated, unrefereed preprint. The proof records these dependencies rather than proving them here. I found no additional missing inference in the displayed chain. In the universal-coefficient line the direct-sum decomposition is noncanonical, which does not affect the vanishing implication used. The computational observation following the source corollaries is not needed for the proof and is not reproduced here.''',
2: r'''The proof states the skeletal-filtration facts it needs and derives the character obstruction from the regular representation. The essential point in (K2) is the exactness of the skeletal relative-$K$-theory sequence: the cellular coboundary representing the relative class maps to zero in absolute $K$-theory. This establishes the filtration inclusion actually used without asserting convergence of an unrestricted Atiyah--Hirzebruch spectral sequence. The $p$-local proof reduces to finite lens-space skeleta, where the reduced $K$-groups are finite $p$-groups and localization is injective. The residual-finiteness and linearity sentence uses the stated finite-dimensional representation argument. I found no gap in these deductions from the explicitly quoted Atiyah completion and character-kernel results; those external results remain cited inputs.''',
3: r'''The source supplies the amalgamated-product construction and the factorization of every homomorphism to a smaller group. It explicitly identifies two places needing a careful independent check: the successor-step comparison with local coefficients, and the cardinal bound in the Kan--Thurston input. The cited cardinal estimate was recalled from memory, and its proof is not present in the supplied files. The construction also treats compatible classifying-space models and limit unions without spelling out their replacement maps. Thus the written argument has a specific citation and model-compatibility gap at the claimed cardinal bound and its repeated use. The deduction of Theorem~3.2 from Theorem~3.1 is written out, including the functor-category isomorphism induced by $G_c\twoheadrightarrow\pi_c$, but it also cites the return's localization results A.4, A.7 and E.17a. Corollary~3.3(b) expressly relies on the manuscript's path-category formula without re-deriving it. These are the source's dependencies; this reading does not supply missing proofs or promote its conclusion to an independently checked theorem.''',
4: r'''The infinite product is locally finite on every CW skeleton, so the weak topology of the CW complex supplies its continuity. The least differing index compares the two maps on the corresponding skeleton; the cellular representative of $s_n$ lands there, and multiplication by the inverse of the common initial product gives the stated contradiction. The Hopf-bundle lifting argument then identifies two lifts differing by a map to $S^1$, whose class vanishes by $H^1(X;\mathbb Z)=0$. I found the proof complete from the stated hypotheses and standard cellular approximation and bundle homotopy lifting. It does not construct a finite category satisfying the retract hypothesis; the unlisted speculative finite-category consequence is not added to this appendix.''',
5: r'''The bound combines the cited thirteen-point classification with a degree count that is explicitly proved. Minimality in arrow count removes degree-one beat points. A vertex-minimal full subcomplex with nonzero second mod-two homology has at least six vertices and degree at least four at each of them; the remaining comparability vertices have degree at least two. The sum gives $f_0+f_1\ge 2f_0+6\ge34$ outside the thirteen-point case. The argument is complete once the cited Cianci--Ottina object bound and classification are supplied. It proves the lower bound recorded here and does not identify the global arrow minimum.''',
6: r'''The supplied file contains the census counts and the algorithm description, but the referenced programs, enumeration certificates and output files are absent from the archive. Consequently the exhaustive lower bounds and uniqueness claims cannot be reproduced or independently certified from these attachments. The homology tests described are sufficient to exclude the listed sphere types when the enumeration is exhaustive; homology alone would not certify the positive homotopy types. The source points to separately proved models $P_2$, $P_3$ and the parallel pair for existence, but does not include an enumeration certificate in this section. The asserted ten-arrow size of Grothendieck's model is recorded by NEW\_RESULTS; this section's source statement does not give its complete composition table. This entry is therefore an exact account of a reported computational result with a missing computational proof record, not a fresh exhaustive verification.''',
7: r'''The note supplies the desuspension argument, the localizer-axiom verification and the stable-closure argument. Its decisive outside inputs are the two-local James EHP fibre sequence, Miller's theorem together with the arithmetic-square passage to two-local spheres, Kahn--Priddy in the stated space-retraction form, and Snaith's splitting. Those inputs are named but not proved here; in particular the arithmetic-square passage and the use of iterated bar constructions are compressed. I found no algebraic discrepancy in the displayed cofibre and stable-closure steps, but the precise localization and retraction formulations need independent source checking before this is described as a completed peer review. The source's accessibility discussion is expressly unproved and lies outside the recorded theorem; it is omitted rather than turned into an additional assertion. The relation between $W_S$ and $RT(W_S)$ is exhibited by the specific map $\mathbb{RP}^2\to e$ and the source's explicit construction, not inferred from a categorical label.''',
8: r'''The source's two-cone construction makes the failure concrete: both cones and their union have contractible classifying spaces, while their intersection has the specified nontrivial fundamental group. The supplied TOTASPH review gives the relation matrix and an explicit nontrivial permutation representation for an acyclic example. The suspension is simply connected and acyclic, so its contractibility follows from Hurewicz and Whitehead. This proves the counterexample to the reverse axiom once the category model of the presentation complex is supplied; the review reports that model's counts but the full attaching data are outside the cited FINDINGS paragraph. The list of later manuscript dependencies is a source attribution, not a separate proof of each later statement. The inventory adds the word ``only'' to its homology-localizer sentence; the cited FINDINGS paragraph says ``for homology localizers and not for $W_\infty$.'' The two-cone proof supplies the stated failure for $W_\infty$ but gives no classification excluding every other localizer. The inventory's stronger word is preserved in its exact statement and flagged here as unsupported by that proof.''',
9: r'''The cited FINDINGS entry gives a claim and one-line description, not a full proof. The supplied POLES review adds the trefoil outline reproduced below, including the Alexander module $\mathbb Z[t,t^{-1}]/(t^2-t+1)$. Its derivation of the fibre local system, the comparison from strict categorical base change to the stated homology calculation, and the claimed surjection are not written out. The review refers for those steps to a working note absent from the archive. Thus the direct proof as supplied has a definite missing middle step. The field-coefficient version is also asserted without its corresponding derivation. This appendix preserves that limitation and does not replace the missing proof with an invented argument.''',
10: r'''The proof is the composition of two identified manuscript facts: the endpoint functor is final for the specified simply connected target, and total asphericity passes to final images. The source identifies both manuscript locations, and the supplied review repeats the deduction. These two cited facts establish exactly the displayed implication. Their internal proofs are not reproduced in FINDINGS; this is a short proof by reference rather than a standalone construction of the endpoint category. The converse is not asserted here.''',
11: r'''The supplied text writes out the covering-space argument that converts the category-of-elements acyclicity condition into weak contractibility, and it gives the exact direct-sum functor that transfers exact colimits to categories of elements. It then supplies the polynomial affine-cone construction and the two injections which no postcomposition can equalize. The source excerpt retains two dependencies outside its boundaries: the collage model from Part~B and the affine-category exactness theorem from Part~D. The supplied review checks both and gives the short colimit relation used in the latter; its text is reproduced as an accompanying source note. I found the bridge C.5--C.6 and the displayed polynomial identities internally consistent. The theorem that the affine category of injective ordinals is filtered is credited to Isbell--Mitchell, 1973, Theorem~3, as the review requires. This is an independent written proof with recorded dependencies, not a claim of priority for that theorem.''',
12: r'''The proof specifies the exact morphism from the maximal subgroup's classifying space to that of the monoid through its Karoubi envelope, and computes the induced surjection on fundamental groups. Miller's stated theorem makes the same induced map trivial for a finite-dimensional target; the two conclusions force $U(M)=1$. The fundamental group of $\mathbb{RP}^2$ then supplies the counterexample. I found the source proof complete from Quillen's Theorem~A and Miller's stated theorem. The supplied verdict adds a $K$-theoretic verification of the latter finite-group case. The separately cited EMAIL\_CLAIMS\_CHECK file is absent, so its purported additional checks cannot be reproduced here. The refutation is tied to the conjecture as quoted in the supplied version-1 record; no assertion about a later version or publication status is added.''',
}

TITLES={1:'Finite monoids, finite dimension, and bounded homology',2:'Maps from finite-group classifying spaces under a cohomological bound',
3:'Kan--Thurston without small quotients and the ind-category statement',4:'Uncountably many homotopy classes of maps to the two-sphere',
5:'The thirty-four-arrow lower bound for the projective plane',6:'The reported census of small categories',
7:'The reversible localizer defined by two-local spheres',8:'The two-cone counterexample to the reverse axiom',
9:'The reported trefoil argument for failure of Loc (7 F)',10:'Totality and the fixed-origin path category',
11:'Exact colimits, total asphericity, and injective ordinals',12:'The projective-plane counterexample for finite monoids'}

ADDED_BIB = r'''
% References required by the new-results appendix. Existing entries are retained.
@article{Miller1984,
  author = {Miller, Haynes},
  title = {The {Sullivan} conjecture on maps from classifying spaces},
  journal = {Annals of Mathematics},
  series = {Second Series}, volume = {120}, number = {1},
  year = {1984}, pages = {39--87},
  note = {Theorem B, p. 40; Theorem 10.1 and proof, pp. 84--85. Reference as specified in the supplied CATHOT return and verdict.}
}
@misc{BenBassat2026,
  author = {Ben-Bassat, Oren},
  title = {On a Conjecture of {Fiedorowicz}},
  year = {2026}, eprint = {2610.38760}, archivePrefix = {arXiv},
  url = {https://arxiv.org/abs/2610.38760v1},
  note = {Version 1, 28 October 2026. The appendix refers specifically to Theorem C and Conjecture 7.1 as quoted in the supplied source record.}
}
@article{Isbell1974Exact,
  author = {Isbell, John}, title = {Exact colimits. {I}},
  journal = {Annals of Mathematics}, volume = {100}, number = {3},
  year = {1974}, pages = {633--637}, doi = {10.2307/1970960},
  url = {https://annals.math.princeton.edu/1974/100-3/p05},
  note = {The source return's original attribution; the supplied review identifies the earlier Isbell--Mitchell 1973 Theorem 3.}
}
@article{Husainov2002Dimension,
  author = {Husainov, Ahmet A.},
  title = {Homological dimension theory of small categories},
  journal = {Journal of Mathematical Sciences}, volume = {110}, number = {1},
  year = {2002}, pages = {2273--2321},
  note = {Bibliographic metadata checked against the author's publication list; the appendix reproduces the source return's Section 2.3 citation.}
}
@misc{OpenMaths2026Derived,
  author = {{Claude Opus 5.5}},
  title = {Derived colimits over a small category},
  howpublished = {Open Maths lesson, AI-written, CC0},
  year = {2026},
  note = {20 October 2026. Provenance reported in the supplied expert FINDINGS F2-9; the lesson itself is not among the attachments.}
}
@article{NRIsbellMitchell1973,
  author = {Isbell, John R. and Mitchell, Barry}, title = {Exact colimits},
  journal = {Bulletin of the American Mathematical Society}, volume = {79},
  year = {1973}, pages = {994--996}, doi = {10.1090/S0002-9904-1973-13296-3},
  note = {Theorem 3, as identified and checked in the supplied TOTASPH review.}
}
@article{NRHarvey1971,
  author = {Harvey, W. J.}, title = {On branch loci in {Teichm\"uller} space},
  journal = {Transactions of the American Mathematical Society}, volume = {153},
  year = {1971}, pages = {387--399}, doi = {10.1090/S0002-9947-1971-0297994-0},
  note = {Prior reference recorded by NEW\_RESULTS; the relevant proof is outside the supplied appendix source files.}
}
'''

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--records',type=Path,required=True);args=ap.parse_args()
    src=args.source;out=args.output;rec=args.records;out.mkdir(parents=True,exist_ok=True);rec.mkdir(parents=True,exist_ok=True)
    nr=(src/'NEW_RESULTS.md').read_text()
    entries={}
    for line in nr.splitlines():
        if re.match(r'\| \d+ \|',line):
            cells=[x.strip() for x in line.strip('|').split('|')]
            entries[int(cells[0])]=dict(zip(['statement','proof_source','proved_by','checked_by','bears_on'],cells[1:]))
    assert len(entries)==12
    ownpath='pro_reviews_max_20261112/1_CATHOT/OWN_RESULTS.md'
    own=(src/ownpath).read_text()
    findingpath='pro_reviews_max_20261112/DERIVATEURS_EXPERT/FINDINGS.md'
    findings=(src/findingpath).read_text()
    def finding(key):
        m=re.search(r'(?m)^- (?:\*\*)?'+re.escape(key)+r'.*?(?=\n- |\n##|\Z)',findings,re.S)
        assert m,key
        return m.group(0)[2:].strip()
    review2path='pro_reviews_max_20261112/2_TOTAL_ASPHERICITY/REVIEW.md';review2=(src/review2path).read_text()
    review3path='pro_reviews_max_20261112/3_POLES/REVIEW.md';review3=(src/review3path).read_text()
    def row(s,key):
        return next(x for x in s.splitlines() if x.startswith('| '+key+' '))
    bodies={};sources={};raw={}
    for no,section in [(1,2),(2,1),(3,3),(4,4),(5,5),(6,6)]:
        text=take_section(own,section)
        if no==1:text=text.split('\nComments.')[0]
        if no==4:text=text.split('\n**Corollary 4.2.')[0]
        if no==3:text=text.split('\n*Where an error could hide.')[0]
        raw[no]=text;sources[no]=[(ownpath,'section '+str(section))];bodies[no]=md(text)
    revpath='pro_reviews_max_20261112/DERIVATEURS_EXPERT/RESULT_REVERSIBLE_NOT_STABLE.md'
    rev=(src/revpath).read_text();text=rev[rev.index('## 1.'):rev.index('## 5.')]
    raw[7]=text;sources[7]=[(revpath,'sections 1--4')];bodies[7]=md(text)
    for no,key in [(8,'F-G1'),(9,'F3-5'),(10,'F2-11')]:
        text=finding(key);raw[no]=text;sources[no]=[(findingpath,key)]
        bodies[no]=md(text)
    supplement8='\n\n'.join(row(review2,key).split('|',3)[-1].strip(' |') for key in ['A.12','A.13'])
    bodies[8]+='\n\\subsection*{Proof details recorded in the supplied TOTASPH review}\n'+md(supplement8)
    sources[8].append((review2path,'A.12--A.13'));raw[8]+='\n\n'+supplement8
    trefoil=row(review3,'C.5');trefoil=trefoil[trefoil.index('**Independent confirmation'):].rstrip(' |')
    bodies[9]+='\n\\subsection*{The available proof sketch}\n'+md(trefoil)
    sources[9].append((review3path,'C.5'));raw[9]+='\n\n'+trefoil
    totalpath='pro_returns_cited/TOTASPH_sections_C.tex';tot=(src/totalpath).read_text();tot=tot[:tot.index('\\subsection{Monoids')]
    raw[11]=tot;sources[11]=[(totalpath,'C.1--C.10'),(review2path,'C.5--C.10')]
    # Prefix every local label. The only external reference is named explicitly.
    tot=tot.replace('\\ref{D:affine-exactness}','D.4 of the source return')
    tot=re.sub(r'\\(label|ref)\{(C:[^}]+)\}',r'\\\1{NR:\2}',tot)
    for env in ['definition','lemma','theorem','proposition']:
        tot=tot.replace('\\begin{'+env+'}',r'\begin{nr'+env+'}').replace('\\end{'+env+'}',r'\end{nr'+env+'}')
    tot=tot.replace('\\subsection{',r'\subsection*{')
    # The review identifies the earlier attribution as superseded. Keep the
    # original source paragraph intact and annotate it rather than replacing it.
    tot=tot.replace('The exact-colimit example is attributed',r'\noindent\textbf{Historical source wording.} The review corrects the attribution below to Isbell--Mitchell (1973), Theorem~3; the source wording is retained.\par\smallskip'+'\nThe exact-colimit example is attributed')
    bodies[11]=tot
    checks='\n\n'.join(row(review2,key).split('|',3)[-1].strip(' |') for key in ['C.9','C.10'])
    bodies[11]+='\n\\subsection*{The supplied reviewer on attribution and the exact-colimit step}\n'+md(checks)
    raw[11]+='\n\n'+checks
    cathpath='pro_returns_cited/CATHOT_sections_G.tex';cath=(src/cathpath).read_text()
    def claim(k):
        start=cath.index('\\begin{claim}{'+k+'}')
        end=cath.find('\\begin{claim}',start+1)
        return cath[start:end if end>=0 else len(cath)].strip()
    twelfth=claim('G.4')+'\n\n'+claim('G.6')
    raw[12]=twelfth;sources[12]=[(cathpath,'G.4 and G.6'),('pro_reviews_max_20261112/1_CATHOT/G6_VERDICT.md','theorem and verification')]
    bodies[12]=twelfth.replace('\\begin{claim}',r'\begin{nrsourceclaim}').replace('\\end{claim}',r'\end{nrsourceclaim}')
    verdict=(src/'pro_reviews_max_20261112/1_CATHOT/G6_VERDICT.md').read_text()
    extra=verdict[verdict.index('**The proof of step 4'):verdict.index('## Is the return')].strip()
    bodies[12]+='\n\\subsection*{The supplied verdict\textquotesingle s verification of the finite-group step}\n'+md(extra)
    raw[12]+='\n\n'+extra
    preamble=r'''% Source-faithful appendix generated by build_appendix.py.
% All source paths refer to members of DER_03_companion_newresults_conventions.zip.
\begingroup
\selectlanguage{english}
\providecommand{\Set}{\mathbf{Set}}
\providecommand{\Ab}{\mathbf{Ab}}
\providecommand{\Winfty}{W_\infty}
\providecommand{\Hot}{\mathbf{Hot}}
\providecommand{\Z}{\mathbb{Z}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\id}{\operatorname{id}}
\providecommand{\colim}{\mathop{\operatorname{colim}}}
\newtheorem{nrdefinition}{Source definition}
\newtheorem{nrlemma}{Source lemma}
\newtheorem{nrtheorem}{Source theorem}
\newtheorem{nrproposition}{Source proposition}
\newenvironment{nrsourceclaim}[3]{\par\medskip\noindent\textbf{Source #1. #3}\quad\textit{#2}\par\smallskip}{\par\medskip}
\dgrbackchapter{Results proved along the way that we did not find in the literature}
\markright{Appendix: results and source proofs}
'''
    framing=nr[nr.index('Some statements'):nr.index('\nStarted ')].strip()
    intro=md(framing)+r'''
\noindent\textbf{Editorial scope.} The inventory was started on 12 November 2026 by Claude Opus~5.5 (effort max). This appendix was assembled by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Each numbered section preserves the inventory statement and the available cited proof, with mathematical glyphs and scripts typeset for reading. Proofs and source comments remain attributed to their source authors. The paragraph headed ``GPT-6 Astra's reading'' is an editorial reading of the supplied argument; it is not the separate peer review requested for later work. Missing cited evidence is stated explicitly. Original source identifiers are preserved. The source extracts and the exact glyph mapping are included among the build records. No material from STRATA, PATHS, BISITE or RESIDUE is added beyond the inventory's own references.
\par\medskip
\noindent\textbf{Notation from the cited sources.} A universe $U$ is fixed; categories are small in that universe. $BX=|NX|$ denotes the classifying space, $W_\infty$ the functors inducing weak homotopy equivalences, and $\mathbf{Hot}$ the homotopy category. In $\mathrm{Cat}_{\mathrm{hot}}$, morphisms are $\pi_0\operatorname{Fun}(X,K)$. The functor $\Pi_1$ inverts every arrow, with unit $\eta_X:X\to\Pi_1X$. For a monoid $M$, $U(M)$ is its universal group. Brackets $[A,Y]$ denote free homotopy classes. Original labels such as Theorem~2.1 and G.4 refer to the cited source, not to the numbering of this appendix.
'''
    parts=[preamble,intro];evidence=[]
    for n in range(1,13):
        e=entries[n]
        parts += [r'\section*{'+str(n)+'. '+TITLES[n]+'}',r'\phantomsection\addcontentsline{toc}{section}{'+str(n)+'. '+TITLES[n]+'}',
          r'\label{nr:entry'+str(n)+'}',r'\noindent\textbf{Statement recorded in the inventory.}\par\smallskip',md(e['statement']),
          r'\noindent\textbf{Bearing on the manuscript.} '+tex(e['bears_on'])+r'\par\smallskip',
          r'\noindent\textbf{Proved by.} '+tex(e['proved_by'])+r'\par',
          r'\noindent\textbf{Checked by (inventory record).} '+tex(e['checked_by'])+r'\par\smallskip',
          r'\noindent\textbf{Cited source.} '+ '; '.join(r'\path{'+p+'}, '+tex(loc) for p,loc in sources[n])+r'\par\medskip',
          r'\subsection*{Statement and proof in the supplied source}',bodies[n],
          r'\subsection*{GPT-6 Astra\textquotesingle s reading}',READINGS[n],r'\par\bigskip']
        evidence.append({'entry':n,'title':TITLES[n],'source_members':[p for p,_ in sources[n]],'source_locations':[l for _,l in sources[n]],
                         'statement_sha256':hashlib.sha256(e['statement'].encode()).hexdigest(),'extracted_source_sha256':hashlib.sha256(raw[n].encode()).hexdigest(),
                         'statement_preserved':True,'proof_present':'reported computation without shipped programs' if n==6 else 'sketch with missing cited working note' if n==9 else 'available source text reproduced',
                         'proved_by':e['proved_by'],'checked_by':e['checked_by'],'bearing':e['bears_on']})
    ending=r'''
\section*{Statements found to be known}
\phantomsection\addcontentsline{toc}{section}{Statements found to be known}
The inventory closes by recording the following prior references, so that these statements are not presented as priority claims.
\begin{enumerate}
\item The filteredness of the affine category of injective ordinals: J.~R.~Isbell and B.~Mitchell, ``Exact colimits,'' \emph{Bulletin of the American Mathematical Society} \textbf{79} (1973), 994--996, Theorem~3. This is the prior theorem used in section~11; the bridge to total asphericity is the additional connection recorded there. The source review also identifies the intermediate CC0 Open Maths lesson, ``Derived colimits over a small category'' (20 October 2026), as the provenance of the return's polynomial proof.
\item Uniqueness in Nielsen realization: W.~J.~Harvey, ``On branch loci in Teichmüller space,'' \emph{Transactions of the American Mathematical Society} \textbf{153} (1971), 387--399. NEW\_RESULTS records that the La Longue Marche expert located this reference; its proof and precise formulation are outside the supplied new-results proof files.
\item The identification recorded as ``localiseur spécial'' and accessible fundamental localizer: D.-C.~Cisinski, \emph{Les préfaisceaux comme modèles des types d'homotopie}, Astérisque~308 (2006), Corollary~4.2.22, as cited in NEW\_RESULTS and the supplied expert FINDINGS F3-4. The exact axiom translation is not added as a new appendix theorem.
\end{enumerate}
\endgroup
'''
    parts.append(ending)
    appendix='\n\n'.join(parts)+'\n'
    assert len(re.findall(r'\\section\*\{\d+\.',appendix))==12
    assert len(re.findall(r'\\subsection\*\{GPT-6 Astra',appendix))==12
    (out/'appendix_new_results.tex').write_text(appendix)
    (rec/'APPENDIX_SOURCE_EXTRACTS.md').write_text('\n\n'.join('## Entry '+str(n)+'\n\n'+raw[n] for n in range(1,13)))
    (rec/'APPENDIX_VALIDATION.json').write_text(json.dumps({'entries':evidence,'section_count':12,'reading_count':12,
      'missing_cited_members':['pro_reviews_max_20261112/1_CATHOT/work/code/','pro_reviews_max_20261112/1_CATHOT/EMAIL_CLAIMS_CHECK.md',
      'pro_reviews_max_20261112/DERIVATEURS_EXPERT/work/checks_3/own_thoughts_before_reading.md'],
      'external_cross_reference':'D:affine-exactness rendered as D.4 of the source return; the source review identifies this theorem'},indent=2,ensure_ascii=False)+'\n')
    with (rec/'APPENDIX_TYPESETTING_MAP.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['source_glyph','tex_rendering','effect'])
        for a,b in SYMBOLS.items():w.writerow([a,r'\ensuremath{'+b+'}','same mathematical glyph'])
        for a,b in SUP.items():w.writerow([a,r'\textsuperscript{'+b+'}','same superscript'])
        for a,b in SUB.items():w.writerow([a,r'\textsubscript{'+b+'}','same subscript'])
    for p in (src/'companion/reader').iterdir():
        if p.is_dir():shutil.copytree(p,out/p.name,dirs_exist_ok=True)
        else:shutil.copy2(p,out/p.name)
    shutil.copy2(src/'companion/kit/derivateurs_companion.sty',out/'derivateurs_companion.sty')
    master=(out/'LesDerivateurs_companion.tex').read_text()
    master=master.replace('\\nocite{*}','\\input{appendix_new_results}\n\n\\nocite{*}')
    fit_preamble=r'''\providecommand{\textquotesingle}{\textquoteright}
% Fit only diagrams that exceed the available page box; preserve source tokens.
\AddToHook{env/tikzcd/before}{\begin{adjustbox}{max width=\linewidth,max totalheight=\textheight}}
\AddToHook{env/tikzcd/after}{\end{adjustbox}}
'''
    master=master.replace('\\begin{document}',fit_preamble+r'\begin{document}')
    (out/'LesDerivateurs_companion.tex').write_text(master)
    bib=out/'LesDerivateurs_companion.bib'
    bib.write_text(bib.read_text()+'\n'+ADDED_BIB)
    print(json.dumps({'sections':12,'readings':12,'appendix_bytes':len(appendix.encode()),'sources_verified':True}))

if __name__=='__main__':main()
