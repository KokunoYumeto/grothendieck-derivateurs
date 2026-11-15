"""Build the bibliography from supplied metadata and this run's access record."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'code/inputs/TOTEX_references.bib'

def entries(text):
    out = {}
    for m in re.finditer(r'@(\w+)\{([^,]+),', text):
        i = m.end(); depth = 1
        while depth:
            if text[i] == '{': depth += 1
            if text[i] == '}': depth -= 1
            i += 1
        out[m.group(2)] = text[m.start():i]
    return out

base = entries(SOURCE.read_text())
selected = ['IsbellMitchell1973', 'IsbellMitchell1976',
    'AdamekReiterman1976', 'AdamekKoubekReiterman1981', 'Oberst1968',
    'Husainov2002', 'GabrielUlmer1971', 'GrothendieckDerivateurs']
notes = {
 'IsbellMitchell1973': 'Opened: complete attached primary paper; Theorems 1--3, Lemma 1, and Corollary 1 read.',
 'IsbellMitchell1976': 'Opened: complete attached primary paper, Sections 1--4. Theorem 3.1, Proposition 3.3, the coefficient-ring remark on p.296, Theorem 4.1, Corollaries 4.2--4.4, Proposition 4.5 and Corollary 4.6 used in their stated variance.',
 'AdamekReiterman1976': 'Opened: complete primary paper. Proposition I.2 read. Section II.3 repeats the false fixed-point/exact-Ab equivalence. AKR1981 A.4 explicitly corrects the earlier 1975 remark; its counterexample also refutes the assertion repeated here in II.3. No claim that A.4 explicitly cites II.3 is intended.',
 'AdamekKoubekReiterman1981': 'Opened: supplied primary scan. Constructions B.5--B.9 and C.1, and the full induction in Theorem C.2, pp.385--389, inspected. Corrections and the precise remaining homology question are recorded in this paper.',
 'GabrielUlmer1971': 'Opened: full university-hosted scan; Sections 5.2, 15.2(c), and 15.9 read for filtered and sifted colimit criteria. No claim about the unresolved totality implication is attributed to this source.',
 'GrothendieckDerivateurs': 'Opened: supplied French transcriptions, corrected 11 November 2026, of Chapters II, VII, and XII from the Kuenzer--Malgoire--Maltsiniotis edition. II manuscript pp.36--36ter, VII pp.25--32, and XII pp.88--89 inspected. No independent collation against the edition is claimed.'
}
for key,note in notes.items():
    base[key] = re.sub(r' note = \{.*?\}\s*\n\}', lambda _: ' note = {'+note+'}\n}', base[key], flags=re.S)
all_entries = {key:base[key] for key in selected}
all_entries.update(entries((ROOT/'notes/finite_references.bib').read_text()))
extra = ROOT/'notes/extra_references.bib'
if extra.exists(): all_entries.update(entries(extra.read_text()))
dest = ROOT/'TOTEX2_references.bib'
dest.write_text('% Every entry records body-access status in this run.\n\n'+'\n\n'.join(all_entries.values())+'\n')
for key,value in all_entries.items():
    assert re.search('Opened|Not opened',value), key
    print(key, 'NOT OPENED' if 'Not opened' in value else 'OPENED')
print('entries',len(all_entries))
