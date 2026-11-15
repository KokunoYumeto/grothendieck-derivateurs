"""Build the A/G claim ledger without dropping mathematical qualifiers.

Run from any directory. The only section edit is an idempotent placement of the
late-added A.19 after A.18. Other contributors' typography fixes are preserved.
"""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parents[1]
a_file = BASE / 'sections' / 'A.tex'
a_text = a_file.read_text()
start = a_text.index(r'\begin{claim}{A.19}')
end = a_text.index(r'\end{proof}', start) + len(r'\end{proof}')
block = a_text[start:end]
if a_text.find(r'\begin{claim}{A.18}') > start:
    a_text = a_text[:start] + a_text[end:]
    a_text = a_text.rstrip() + '\n\n' + block + '\n'
    a_file.write_text(a_text)

locations = {
 'A.1': 'XVI ms. 1–3; Loc (1), (1 bis), (1 ter), (2), (3), (3 bis), footnote 1',
 'A.2': 'XII ms. 75–77; W(7), W(7 bis)',
 'A.3': "XVI ms. 16′–18′; Loc (6a,b,c), (6′a,b), footnote 13",
 'A.4': 'XVI ms. 25–27; Loc (6A), (6A′), (6B), (6C); XII ms. 261–264',
 'A.5': 'XVI ms. 27–32; intrinsic, Grothendieck, weak and perfect fibrations',
 'A.6': 'XVI ms. 38–45; Loc (7a,b,c), (7D), (7F)',
 'A.7': 'XVI ms. 8, 12, 71–75; Loc (4), (5), (8), (8 bis), (9)',
 'A.8': 'XVI Lemma 3.2.1, ms. 20–22; XII footnote 136, ms. 266',
 'A.9': 'XII Proposition 16, ms. 231–232; XVI Lemma 4.4.1',
 'A.10': 'XII Proposition 6, ms. 78; XVI ms. 18′–19',
 'A.11': 'XVI Proposition 3.6, ms. 25–26, footnote 19; XII ms. 266, footnote 136',
 'A.12': 'XVI Proposition 3.3 and Corollary 3.7, ms. 22, 26–27; XII ms. 265–272',
 'A.13': 'XVI Lemmas 4.4.1 and 4.4.3, ms. 45–49',
 'A.14': 'XVI Lemma 4.4.9 and Corollary 4.4.10',
 'A.15': 'XVI ms. 45–70; 4.4.6, 4.4.13, 4.4.15, literal heading 4.16 and footnote 36',
 'A.16': 'XVI Loc (3) versus Loc (3 bis); historical eight-condition implication diagram',
 'A.17': 'XVI ms. 45–70 and 83–85; all eight fibration formulations',
 'A.18': 'XVI ms. 18′, 25, 38–45, 71–72; Loc (4a), (4b)',
 'A.19': 'XVI historical W_omega; Cisinski 2006 §§1.4.12, 6.1.12, Theorem 6.1.18',
 'G.1': 'XII ms. 76–77, 270–272; companion XIIba-A-053',
 'G.2': 'XII Theorem 2, ms. 78–80',
 'G.3': 'XII ms. 81–83, 108–109, 227–228, footnote 124',
 'G.4': 'XII ms. 85, 149–151; Proposition 7 and one-point-complement tests',
 'G.5': 'XII ms. 97–100; total-asphericity gluing argument',
 'G.6': 'XII ms. 104–107; appendix ms. 15–16; XIIba-C008,C012,C016; XIIapp-C060–065',
 'G.7': 'XII ms. 125–135; XIIbb-A028–035,A043; XIIb-b-B001,B005–006; footnote 85',
 'G.8': 'XII Theorem 4, ms. 146–149; Corollary 6, ms. 157; XIIb-b-B035–038,B042–046; XIIbb-C011–020',
 'G.9': 'XII Theorem 5, ms. 168–169; XIIbb-C048–052; footnote 111',
 'G.10': 'XII ms. 111; companion XIIba-C037–038; TOTASPH boundary-weight recognition claim',
 'G.11': 'XII ms. 114–115, 228–234; XIIc-a-C046,C050,C053,C062; footnote 124',
 'G.12': 'XII Propositions 17 and 18, ms. 234–239',
 'G.13': 'XII ms. 240–261; footnote 130',
 'G.14': 'XII Proposition 20, ms. 262–264; footnote 134; XVI footnotes 15–17, ms. 23–24',
 'G.15': 'XII ms. 265–267; reversed citation of Proposition 6 and footnote 136',
 'G.16': 'XII lemma and deployment argument, ms. 268–272',
 'G.17': 'XII theorem part 3° and Corollary 1, ms. 274; checked against supplied edition PDF',
 'G.18': 'XII Cons 2, ms. 273; checked against supplied edition PDF',
 'G.19': 'XII appendix ms. 17–18; footnotes 9 and 10; open/closed gluing entry',
 'G.20': 'XII theorem parts 1°–2°, ms. 272–274; Corollary 2, ms. 275; footnotes 137–138',
 'G.21': 'XVI §§3–4, ms. 16′–70; Propositions 3.3,3.6, Corollary 3.7, 4.4.15, footnote 36',
 'G.22': 'XVI §5, ms. 71–83; Theorem 5.4, Corollary 5.3.2, Lemma 5.5',
 'G.23': 'XVI §6, ms. 83–97; Theorem 6.1, Lemma 6.2, Corollary 6.3, 6.4(b,c)',
 'G.24': 'XVI §7, ms. 98–123, especially ms. 119–120; footnotes 55,57,58',
 'G.25': 'XII §§5–8 and appendix; XVI §§3–7; complete stated audit location register',
 'G.26': 'XII abstract theorem, ms. 272–275; square-of-cofibres lemma, ms. 268; footnotes 137–138',
}
notes = {
 'A.1': 'Relative Theorem A is printed 3 bis. Modern strong saturation is not assumed for every historical weak localizer; the historical minimum is nevertheless W_infinity by A.19.',
 'A.2': 'Exact all-small-category and strict map-of-MV-covers quantifiers, with empty pieces and intersections included.',
 'A.3': 'XII W(7) includes all three cube clauses; XVI Loc (6) excludes 6c after footnote 13.',
 'A.4': 'Intrinsic preservation definition; Dwyer means classical full sieve with right adjoint on generated cosieve; no false closure under retracts is used.',
 'A.5': 'Strict base change is distinguished from homotopy pullback and from Grothendieck fibration; variance of reindexing maps is explicit.',
 'A.6': 'The word cofibrations in the first 7F wording is a variance error; reference D_V and absolute D_W are separated.',
 'A.7': 'All filtered colimits is stronger than accessibility. The source uses a countable-cardinality convention distinct from modern finite accessibility.',
 'A.8': 'Complete typed relative Brown argument supplied; no retract closure of the cofibration class or strong saturation is needed.',
 'A.9': 'No implicit retract closure or abstract model-category lifting axiom. Exact assumptions are existence of pushouts, identities and two out of three, and intrinsic cofibration factorizations.',
 'A.10': 'Two specified degenerate cubes prove the arrows; repeated source label f_1=j_1 is corrected to f_2=j_1.',
 'A.11': 'Automatic for modern fundamental localizers, without reverse excision. Actual endpoint-product cylinder is used, not pushout-product.',
 'A.12': 'Pointed cofibers and their cone-vertex sections are retained. The wedge comparison uses e→Z_0. Object retract closure suffices for the third clause.',
 'A.13': 'Every Brown premise is stated; enough fibrations alone does not identify arbitrary weak or Grothendieck fibrations with intrinsic fibrations.',
 'A.14': 'The B transfer requires functorial replacements over the fixed base, not merely objectwise existence.',
 'A.15': 'Records the manuscript arrows separately from their modern verification. The summary uses 7F for V where the earlier proof used 7; A.17 resolves the modern case.',
 'A.16': 'Open in this audit: absolute historical Theorem A ⇒ relative Theorem A. Test base [1] is the first nonterminal instance. Not a claim of newly open literature status; minimum itself is settled.',
 'A.17': 'No accessibility hypothesis. All eight conditions imply homotopy-pullback stability, then W=W_infinity or total; cited full proof E.4–E.5.',
 'A.18': 'Includes arbitrary small indexing sets and empty summands; modern forward coproduct closure needs no extra Loc (8).',
 'A.19': 'Known separate weak-localizer theorem. Literal Loc1 cancellation implies Cisinski FS3, so the minimality theorem applies without relative Theorem A.',
 'G.1': 'Object-level intersection/union implication is true for every modern W by forward gluing and retracts; it must not be equated with the failed map-level 6c.',
 'G.2': 'Finite A with 35 objects and 159 arrows, and its two cones; acyclic-group alternative also specified.',
 'G.3': 'Reverse cancellation fails even for a genuine Dwyer cofibration; full reverse hypotheses repair the conditional claims.',
 'G.4': 'One-point complement is required to have only the identity endomorphism; the reverse assertion is conditional on full excision.',
 'G.5': 'Four objects and ten arrows give S^2; an ordinary final fork is contractible. The mono-under-right-adjoint claim about Kan extension is independently false.',
 'G.6': 'Appendix V′_0 is S^2, not S^1; its double cone is S^3. The later equivalence transfer uses forward trivial-Dwyer pushout, not reverse cancellation. Explicit finite original attachment checked.',
 'G.7': 'Forward and reverse clauses separated; no inference merely from an abstract isomorphism in the localized category.',
 'G.8': '110 objects and 1051 arrows; exceptional central lift has 107 objects and 867 arrows. All lifting categories and finite compositions checked. The conditional reverse theorem is retained.',
 'G.9': 'Exact nerve formula N(X/F)_n=disjoint_union_chains F(x_n) proves colimit/mono preservation. Counterexample uses all simplex categories of finite nerves and includes degenerate simplices.',
 'G.10': 'Two parallel arrows; universal cofibrancy proof covers every complementary base change, including the empty complement. The narrower question about trivial cofibrations is not refuted by this example.',
 'G.11': 'The actual cylinder is a product followed by pushout, n≥2. H.6 refutes the distinct endpoint pushout-product desideratum.',
 'G.12': 'Pasting cancellation concerns squares, not reflection of equivalences along a pushout. Only forward direction of the source biconditional is used.',
 'G.13': 'Loc (7F) and all-terminal-fibrant assumptions are explicit. In Cat the latter follows from product stability.',
 'G.14': 'Direction of the comparison lambda in the source is reversed; correcting the arrow preserves the proof by two out of three.',
 'G.15': 'The citation at p.265 reverses the result at p.78. Footnote136 identifies a real missing pushout comparison, now supplied without circularity.',
 'G.16': 'Fubini for pointed homotopy cofibers proves the lemma; the map-to-object reduction already used reverse cofiber detection at p.267.',
 'G.17': 'A strict finite cube satisfies every printed hypothesis and fails 6c. The PDF confirms absence of conservativity in theorem3°; adding it repairs the assertion.',
 'G.18': 'Empty strict pullback of the distinct endpoints of [1], with all three other vertices contractible; false even for W_Z. Changing Cartesian to cocartesian gives the intended statement.',
 'G.19': 'Full category-level Quillen A proof, explicit P/x contraction and typed natural transformations; includes empty sieve, complement or crossing-arrow category.',
 'G.20': 'Corrected theorem proved in modern Cat and extended to the exact arbitrary-relative-category factorization premises in G.26. The unconditional3° and literal Cartesian Cons2 remain false and are not used.',
 'G.21': 'Inventory includes the Brown premise, presheaf monos, integral models, the enough-cofibrations digression, and every fibration-arrow family.',
 'G.22': 'The full printed list is false only through reverse excision; direct countable witness construction and the combinatorial-model theorem establish accessibility without it.',
 'G.23': 'Full stability minimum is total; if containment in W_infinity is imposed there is no solution. The forward-only minimum is W_infinity.',
 'G.24': 'Accessible modern scope; Cisinski Theorem5.2.15 and Groth Proposition1.36. Explicit projective/injective model presentation and both pointwise comma formulas; no 6b,7,7D,7F assumption.',
 'G.25': 'A semantic register backed by G.1–G.24, not a claim that lexical marker search alone proves exhaustive coverage.',
 'G.26': 'Complete finite Reedy proof under a fixed least vertex. One-leg gluing, typed latching maps, common refinements, root rectification, product-colimit cofibrancy, terminal constant-span comparison, and actual cone maps are explicit. No global initial object, terminal cofibrancy, pushout-product axiom or functorial factorization is assumed. Corollary2 uses actual object retracts. Arbitrary absolute finite homotopy colimits are not asserted.',
}

rows = []
pattern = re.compile(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{([^\n]+)\}\n(.*?)\\end\{claim\}', re.S)
for section in ('A', 'G'):
    file = BASE / 'sections' / f'{section}.tex'
    text = file.read_text()
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        identifier, status, title, statement = match.groups()
        extent = text[match.start():matches[index+1].start() if index+1<len(matches) else len(text)]
        dependencies = list(dict.fromkeys(re.findall(r'\\claimref\{([^}]+)\}', extent)))
        dependencies = [d for d in dependencies if d != identifier]
        rows.append({
            'id': identifier,
            'statement': re.sub(r'\s+', ' ', title+' '+statement).strip(),
            'status': status,
            'where_proved': f'POLES_paper.tex, Part {section}, {identifier}',
            'depends_on': '; '.join(dependencies),
            'manuscript_rows_or_pages_settled': locations[identifier],
            'notes': notes[identifier],
        })
    numbers = [int(m.group(1).split('.')[1]) for m in matches]
    assert numbers == list(range(1,len(numbers)+1)), (section,numbers)
    assert len(re.findall(r'(?<!\\)\\\[', text)) == len(re.findall(r'(?<!\\)\\\]', text)), section
    assert text.count(r'\begin{proof}') == text.count(r'\end{proof}'), section
    print(section, 'claims:', len(matches), 'display and proof delimiters balanced')
assert len({r['id'] for r in rows}) == len(rows)
assert set(locations) == {r['id'] for r in rows}
out = BASE/'research'/'AG_results.json'
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
print('Rows:',len(rows))
for status in ('Proved','Refuted','Known','Open'):
    print(status+':', sum(r['status']==status for r in rows))
print('Saved:',out.relative_to(BASE))
