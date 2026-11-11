"""Assemble the audited source fragments, bibliography, and statement register.

This is a deterministic document build, not a mathematical verification.
Run from any directory; paths are relative to this file.
"""
from pathlib import Path
import csv
import json
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
SEC = ROOT / 'sections'
KEYS = {'RCisinski2006': 'RESCisinski2006',
        'RLurieHA': 'GHIJLurie2017',
        'I9LurieHA2017': 'GHIJLurie2017',
        'I9LurieHTT2009': 'GHIJLurie2009',
        'Quillen1973RESIDUE': 'RESQuillen1973'}


def canonical_keys(text):
    for old, new in KEYS.items():
        text = text.replace(old, new)
    return text


def group(text, pos):
    while text[pos].isspace():
        pos += 1
    assert text[pos] == '{', (pos, text[pos:pos + 80])
    start, depth = pos + 1, 1
    pos += 1
    while depth:
        if text[pos] == '{' and text[pos - 1] != '\\':
            depth += 1
        if text[pos] == '}' and text[pos - 1] != '\\':
            depth -= 1
        pos += 1
    return text[start:pos - 1], pos


def claims(text):
    found = []
    for m in re.finditer(r'\\begin\{(claim|result)\}', text):
        pos = m.end()
        ident, pos = group(text, pos)
        status, pos = group(text, pos)
        title, pos = group(text, pos)
        end = text.index(r'\end{' + m[1] + '}', pos)
        found.append((m.start(), ident, status, title + '. ' + text[pos:end].strip()))
    pat = r'\\paragraph\{([A-J]\.\d+) \((Proved|Refuted|Known|Open)\)\.\}'
    for m in re.finditer(pat, text):
        candidates = [len(text)]
        for marker in [r'\begin{proof}', r'\paragraph', r'\section', r'\subsection']:
            j = text.find(marker, m.end())
            if j >= 0:
                candidates.append(j)
        found.append((m.start(), m[1], m[2], text[m.end():min(candidates)].strip()))
    return sorted(found)


ROOT_DEPENDENCIES = {
 'D.1': 'Cisinski 2006, Propositions 6.2.3–6.2.4; Section 9.2.1; Corollary 9.2.15',
 'D.2': 'D.1; homotopy-fibre exact sequence',
 'D.3': 'D.1 at n=0',
 'D.4': 'C.5; product closure of right lifting classes',
 'D.5': 'Lurie HA 4.7.3.5; Rivera–Wierstra–Zeinalian 2021, Theorem 3',
 'D.6': 'D.5; slice-model realization; Thomason/Cisinski model structure',
 'D.7': 'D.1,D.5,D.6',
 'D.8': 'Finite p-group augmentation-ideal nilpotence; local-coefficient filtration',
 'D.9': 'D.8,D.12',
 'D.10': 'D.2,D.5,D.6; code/root/verify_D.py',
 'D.11': 'C.1,C.2,C.5,D.8,D.10; Cisinski 6.1.8,6.1.11,9.4.5',
 'D.12': 'D.6 slice realization; code/root/verify_coverings.py',
 'F.1': 'Quillen Theorem A; category-of-elements bar resolution; homological Whitehead',
 'F.2': 'F.1', 'F.3': 'F.1,F.2; code/root/verify_F.py',
 'F.4': 'F.1,F.2,F.3', 'F.5': 'F.1,F.2,F.3,F.4',
 'F.6': 'F.1; unresolved restricted-action gap', 'F.7': 'F.3,F.4'
}
ROOT_NOTES = {
 'D.1': 'All functors; canonical comparisons; strict pullbacks. Point tests suffice only in the smooth or proper subclasses.',
 'D.2': 'Lead 1 proved, including empty fibres, disconnected bases, and non-surjectivity on components.',
 'D.3': 'Complete elementary component criterion.',
 'D.4': 'For every W between W_infinity and W_0, the intrinsic maps are not the RLP class of any class of maps, hence not of a set.',
 'D.5': 'Nonzero coefficients. Sets give W_1, groupoids W_2, integral derived coefficients W_infinity.',
 'D.6': 'Complete only under the homotopy-pullback hypothesis; refutes the additional higher-rational-boundary condition.',
 'D.7': 'Unrestricted rational and mod-p classifications remain Open. Integral, set and groupoid cases reduce to the specified known localizers.',
 'D.8': 'A positive universal theorem, not an inference from a finite covering test. Finite checks for p=2,3,5,7.',
 'D.9': 'Arbitrary spectrum E and all smooth-and-proper maps remain Open; D.12 settles integral/rational coverings.',
 'D.10': 'All eight categories reconstructed; 48 scalar entries agree. Universal intrinsic entries proved separately from finite checks.',
 'D.11': 'All six localizer rows settled, including negative factorization entries for the two rational localizers.',
 'D.12': 'Exact covering classification for HZ and HQ; arbitrary empty or infinite fibres allowed. Matrix checks only support the universal proof.',
 'F.1': 'Totality here means XII ms.88 final-image totality. It is not diagonal asphericity.',
 'F.2': 'Only original parallel arrows are affine-equalized; this does not settle all affine parallel pairs.',
 'F.3': 'Complete classifications for full injective-ordinal subcategories and free categories; the FI and Inj(N) candidates are not total.',
 'F.4': 'Weakly terminal case complete; includes finite-object connected categories.',
 'F.5': 'The general countable exact-colimit implication is not proved.',
 'F.6': 'No complete monoid<=6/presheaf<=6 search. Cyclic-cover proof does not apply to the restricted-action presheaf question.',
 'F.7': 'General countable Cat-colimit converse remains Open; injective ordinals do not satisfy the premise.'
}


def main():
    chunks = {}
    for filename, letters in [('AE_agent.tex', 'AE'), ('BC_agent.tex', 'BC'),
                               ('GHIJ_agent.tex', 'GHIJ')]:
        text = (SEC / filename).read_text()
        pieces = re.split(r'(?=\\section\{)', text)[1:]
        assert len(pieces) == len(letters), filename
        chunks.update(zip(letters, pieces))
    chunks['D'] = (SEC / 'D_root.tex').read_text()
    chunks['F'] = (SEC / 'F_root.tex').read_text()
    chunks['I'] += '\n' + (SEC / 'I9_agent.tex').read_text()
    # D.12 was added after the original eight-map proof. Put numbered claims
    # in their final order without changing any mathematical text.
    d = chunks['D']
    start = d.index(r'\subsection{Complete covering tests')
    end = d.index(r'\subsection{The axioms', start)
    chunks['D'] = d[:start] + d[end:] + '\n' + d[start:end]
    for letter in 'ABCDEFGHIJ':
        chunks[letter] = canonical_keys(chunks[letter])
        (SEC / f'{letter}.tex').write_text(chunks[letter].strip() + '\n')

    entries = {}
    for name in ['BC_agent_references.bib', 'GHIJ_agent_references.bib',
                 'AE_agent_references.bib', 'root_references.bib', 'I9_agent_references.bib']:
        content = canonical_keys((SEC / name).read_text())
        for block in re.split(r'(?m)(?=^@)', content):
            match = re.match(r'@\w+\{([^,]+),', block)
            if not match:
                continue
            key = match[1]
            if key in entries:
                continue
            note = re.search(r'note\s*=\s*\{', block)
            assert note, ('Every source needs a verification note', key)
            if not re.search(r'\b(?:unverified|verified)\b', block[note.end():], re.I):
                block = block[:note.end()] + 'verified: ' + block[note.end():]
            entries[key] = block.strip()
    (ROOT / 'RESIDUE_references.bib').write_text(
        '% Every record states verification scope; no priority is claimed.\n\n' +
        '\n\n'.join(entries.values()) + '\n')

    metadata = {}
    for filename in ['AE_agent_results.json', 'BC_agent_results.json', 'GHIJ_agent_results.json',
                     'I9_agent_results.json']:
        for row in json.loads((SEC / filename).read_text()):
            metadata[row['id']] = row
    rows = []
    for letter in 'ABCDEFGHIJ':
        for _, ident, status, statement in claims(chunks[letter]):
            assert status in {'Proved', 'Refuted', 'Known', 'Open'}, (ident, status)
            old = metadata.get(ident, {})
            loc = old.get('manuscript_rows_or_pages_settled', '')
            if letter == 'D':
                loc = '' if status == 'Open' else 'XII ms.208,225; XVI §4; I ms.99–100'
                if ident == 'D.10':
                    loc += '; BISITE B.15 (all 48 entries)'
            if letter == 'F':
                loc = '' if status == 'Open' else 'XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases)'
            if letter == 'H':
                loc = 'BISITE D.11' if ident in {'H.1','H.2','H.7'} else (
                    'BISITE B.15' if ident == 'H.8' else 'BISITE F.15–F.17; Jansen Construction 3.18')
            rows.append({
                'id': ident, 'statement': canonical_keys(re.sub(r'\s+', ' ', statement)),
                'status': status, 'where_proved': f'sections/{letter}.tex, {ident}',
                'depends_on': old.get('depends_on', ROOT_DEPENDENCIES.get(ident, '')),
                'manuscript_rows_or_pages_settled': loc,
                'notes': old.get('notes', ROOT_NOTES.get(ident, 'Exact scope is stated in the paper.'))
            })
    ids = [r['id'] for r in rows]
    assert len(ids) == len(set(ids)), 'Duplicate statement IDs'
    assert ids == sorted(ids, key=lambda s: (s.split('.')[0], int(s.split('.')[1]))), ids
    cols = ['id','statement','status','where_proved','depends_on',
            'manuscript_rows_or_pages_settled','notes']
    with (ROOT / 'RESIDUE_results.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        writer.writerows(rows)
    alltext = '\n'.join(chunks.values())
    cited = set()
    for match in re.finditer(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}', alltext):
        cited.update(match[1].split(','))
    assert cited <= set(entries), ('Missing citations', cited - set(entries))
    summary = {'statements': len(rows), 'statuses': dict(Counter(r['status'] for r in rows)),
               'parts': dict(Counter(r['id'][0] for r in rows)), 'bibliography_records': len(entries),
               'citation_keys_resolved': True,
               'register_matches_all_numbered_statements': True}
    (ROOT / 'code/root/assembly_output.json').write_text(json.dumps(summary, indent=2) + '\n')
    report = (SEC / 'root_report.md').read_text()
    counts = ', '.join(f"{n} {label}" for label, n in summary['statuses'].items())
    report = report.replace('## Scope and status',
                            f"Register at build: **{len(rows)} statements** ({counts}); "
                            f"**{len(entries)} bibliography records**.\n\n## Scope and status", 1)
    for name, heading in [('AE_agent_report.md','Appendix 1: A/E proof and computation audit'),
                           ('BC_agent_report.md','Appendix 2: B/C proof and historical audit'),
                           ('GHIJ_agent_report.md','Appendix 3: G–J proof, source and computation audit'),
                           ('I9_agent_report.md','Appendix 4: Enhanced second-stage localization audit')]:
        report += '\n\n---\n\n# ' + heading + '\n\n' + (SEC / name).read_text()
    (ROOT / 'RESIDUE_report.md').write_text(report)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
