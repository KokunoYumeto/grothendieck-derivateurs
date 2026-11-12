#!/usr/bin/env python3
"""Independent exact-body replay of reader notes and annotated projections.

Does not import the reader builder or its note parser. Sources are the verified
unit files, canonical JSON master payloads, and the logged omission records.
"""
from pathlib import Path
import argparse
import collections
import csv
import difflib
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BD, ED = r'\begin{document}', r'\end{document}'
PAGEBREAK = re.compile(r'\\(?:clearpage|newpage|cleardoublepage|pagebreak(?:\[\d\])?)(?![A-Za-z])')
EMAIL = re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}')
LOCAL = re.compile(r'(?:[A-Za-z]:[\\/](?:Users|home)[\\/][^\s\n"<>]+|/(?:Users|home|root|workspace|tmp|opt|usr|var)/[^\s\n"<>]+)')

def clean(text):
    return LOCAL.sub('[local path removed]', EMAIL.sub('[e-mail address removed]', text))

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def body(text):
    return text.split(BD, 1)[1].rsplit(ED, 1)[0]

def active(text):
    return re.sub(r'(?<!\\)%[^\n]*', lambda m: ' ' * len(m.group()), text)

def brace_end(text, start):
    assert text[start] == '{'
    masked = active(text)
    depth = 0
    for m in re.finditer(r'\\[A-Za-z@]+|\\.|[{}]', masked[start:]):
        if m.group() == '{':
            depth += 1
        elif m.group() == '}':
            depth -= 1
            if depth == 0:
                return start + m.end()
    raise ValueError('Unclosed source group')

def shared_repairs(text, unit):
    text = text.replace(r'\mathbf{\Delta}', r'\boldsymbol{\Delta}')
    if unit.endswith('Der-ChXIIc-30-03-03_p061-064.tex'):
        old = r'baseline=(\tikzcdmatrixname-2-1.base)'
        if text.count(old) == 2:
            text = text.replace(old, r'baseline=(\tikzcdmatrixname-2-2.base)', 1)
    return text

def apply_variants(text, edits):
    previous_end = 0
    for edit in sorted(edits, key=lambda e: (e['start'], e['end'])):
        assert edit['start'] >= previous_end, ('overlap', edit['id'])
        assert text[edit['start']:edit['end']] == edit['before'], ('stale', edit['id'])
        previous_end = edit['end']
    for edit in sorted(edits, key=lambda e: e['start'], reverse=True):
        text = text[:edit['start']] + edit['after'] + text[edit['end']:]
    return text

def projected_body(unit, index):
    text = unit['forms'][index]
    marker = '\\let\\mspin\\DERmspin%\n'
    assert text.count(marker) == 1
    text = text.split(marker, 1)[1]
    own = '\\edef\\derfnsaved{\\the\\value{footnote}}\\setcounter{footnote}{0}%\n'
    if text.startswith(own):
        text = text[len(own):]
        tail = '\n\\setcounter{footnote}{\\derfnsaved}%\n\\endgroup\n% END UNIT ' + unit['unit'] + '\n'
    else:
        tail = '\n\\endgroup\n% END UNIT ' + unit['unit'] + '\n'
    assert text.endswith(tail), unit['unit']
    return text[:-len(tail)]

def strip_attribution(text, lang):
    label = 'Note des éditeurs de l’édition transcrite' if lang == 'FR' else 'Note by the editors of the transcribed edition'
    text = text.replace('\\par\\noindent\\textbf{' + label + '.}\\par\n', '')
    return text

def replay(text, rows, lang):
    """Replay only explicit before/after strings, independent of note parsing."""
    pl = 'plutôt' if lang == 'FR' else 'rather'
    text = re.sub(r'\\pl(?![A-Za-z])', lambda _: r'\texttt{[' + pl + '}', text)
    cursor = 0
    matched = []
    failures = []
    for row in rows:
        before = row['before']
        if not before:
            failures.append(dict(id=row['id'], issue='Empty omission source'))
            continue
        start = text.find(before, cursor)
        if start < 0:
            start = text.find(before)
        if start < 0:
            failures.append(dict(id=row['id'], kind=row['kind'], issue='Logged source not found', before=before))
            continue
        after = row['after']
        # The front-note log records its retained anchor; the builder also
        # separates it from the next page boundary with one newline.
        if row['kind'] == 'editorial_front_note':
            after += '\n'
        text = text[:start] + after + text[start + len(before):]
        cursor = start + len(after)
        matched.append(row['id'])
    return text, matched, failures

def first_difference(expected, actual):
    for tag, i, j, k, l in difflib.SequenceMatcher(None, expected, actual, autojunk=False).get_opcodes():
        if tag != 'equal':
            return dict(operation=tag, expected=expected[max(0,i-70):min(len(expected),j+70)], actual=actual[max(0,k-70):min(len(actual),l+70)])
    return None

def anchors(text):
    result = []
    for m in re.finditer(r'\\(printedpage|msp|mspin)\s*\{', text):
        end = brace_end(text, m.end()-1)
        result.append((m[1], text[m.end():end-1]))
    return result

def visible_editor_markers(text):
    masked = active(text)
    remaining = []
    for m in re.finditer(r'\\(?:texttt|edbr)\s*\{', masked):
        end = brace_end(text, m.end()-1)
        inside = text[m.end():end-1]
        if '[' in inside or ']' in inside:
            remaining.append(dict(kind='typewriter_bracket', text=text[m.start():end]))
    for m in re.finditer(r'\[(?:\s|\\[,;:! ]|~)*\?(?:\s|\\[,;:! ]|~)*\]', masked):
        remaining.append(dict(kind='plain_editorial_doubt', text=m.group()))
    return remaining

def signed_footnotes(text):
    result = []
    for m in re.finditer(r'\\footnote(?:\[[^\]]*\])?\s*\{', text):
        end = brace_end(text, m.end()-1)
        inner = text[m.end():end-1]
        if re.search(r'N\.(?:~|\s)*Éd\.|Ed\.(?:~|\s)*note\.', inner[:70]):
            result.append((m.group(), inner, text[m.start():end]))
    return result

def footnote_events(text):
    """Track the standard LaTeX counter operations in the affected source units."""
    masked = active(text)
    token = re.compile(r'\\(?:(setcounter|addtocounter|stepcounter)\s*\{footnote\}(?:\s*\{(-?\d+)\})?|(footnotemark|footnotetext|footnote)(?![A-Za-z@])(?:\s*\[(\d+)\])?)')
    counter = 0
    cursor = 0
    events = []
    while True:
        m = token.search(masked, cursor)
        if not m:
            break
        cursor = m.end()
        if m[1]:
            if m[1] == 'setcounter':
                counter = int(m[2])
            elif m[1] == 'addtocounter':
                counter += int(m[2])
            else:
                counter += 1
            continue
        kind = m[3]
        optional = m[4]
        if optional is None and kind in ('footnote','footnotemark'):
            counter += 1
        number = int(optional) if optional is not None else counter
        contents = ''
        if kind != 'footnotemark':
            opening = re.match(r'\s*\{', masked[cursor:])
            assert opening is not None
            start = cursor + opening.end()-1
            end = brace_end(text, start)
            contents = text[start+1:end-1]
            cursor = end
        events.append(dict(kind=kind, number=number, contents=contents))
    return events

def footnote_numbering_checks(originals, readings, lang):
    early = 'der-ch18/der-ch18_p016-020.tex'
    late = 'der-ch18/der-ch18_p091-095.tex'
    probes = [(early, 'Autres conditions' if lang == 'FR' else 'Other conditions', 19),
              (early, 'Un peu bref' if lang == 'FR' else 'A bit brief', 20),
              (late, 'Un peu court' if lang == 'FR' else 'A bit short', 105)]
    results = []
    for unit, prefix, expected in probes:
        source = [e for e in footnote_events(originals[unit]) if e['contents'].startswith(prefix)]
        read = [e for e in footnote_events(readings[unit]) if e['contents'].startswith(prefix)]
        assert len(source) == len(read) == 1
        results.append(dict(unit=unit, author_note_prefix=prefix, source_number=source[0]['number'],
                            reading_number=read[0]['number'], expected=expected,
                            exact=source[0]['number'] == read[0]['number'] == expected))
    marked = []
    for unit, text in originals.items():
        numbers = {7,10} if unit.startswith('Der-ChV-234/') else ({75,80,93} if unit.startswith('der-ch18/') else set())
        if not numbers:
            continue
        for m in re.finditer(r'\\footnotemark\s*\[(\d+)\]', active(text)):
            if int(m[1]) in numbers:
                marked.append(dict(unit=unit, number=int(m[1])))
    return dict(author_number_checks=results,
                author_numbers_preserved=all(x['exact'] for x in results),
                explicit_removed_note_numbers_have_no_separate_marks=not marked,
                unexpected_marks=marked,
                invisible_counter_advances={unit:readings[unit].count(r'\stepcounter{footnote}') for unit in [early,late]})

ALIGNMENT_NOTES = {
    'Der-ChI-234/Der-ChI-234_p041-045.tex': 'The two final rows of a label tabular belong entirely to the editor note; the preceding author rows remain.',
    'Der-ChV-234/Der-ChV-234_p001-005.tex': 'The bracket opens before a separate display and owns its complete array.',
    'Der-ChVI-345/Der-ChVI-345_p121-125.tex': 'One shared matrix interleaves the author left triangle and editor right triangle. The reading projection retains author columns 1–3 of both rows.',
    'Der-ChVII-456/Der-ChVII-456_p041-045.tex': 'The bracket owns the separately displayed editorial cancellation diagram.',
    'Der-ChXIIc-30-03-03/Der-ChXIIc-30-03-03_p056-060.tex': 'The bracket owns a separate editorial replacement diagram and its surrounding display.',
    'Der-ChXIII-25-01-04/Der-ChXIII-25-01-04_p006-010.tex': 'The bracket owns the entire editorial definition and its displayed square diagram.',
    'Der-ChXV-05-11-10/Der-ChXV-05-11-10_p006-010.tex': 'The note continues across one array line break; author expressions occur only before its opening and after its closing bracket.',
    'der-ch18/der-ch18_p146-150.tex': 'The note continues across one array line break; no author expression is interleaved between the bracket boundaries.',
}

def alignment_ownership_checks(rows, readings):
    candidates = [r for r in rows if r['kind'] in ('editorial_note','interleaved_editorial_diagram')
                  and (r'\\' in r['before'] or r'\cr' in r['before'] or r'\tabularnewline' in r['before'])]
    extra_single = [r['id'] for r in rows if r['kind'] == 'editorial_note' and '&' in r['before'] and r'\\' not in r['before']]
    expected_triangle = "\\begin{tikzcd}[column sep=small]\n& \\mathrm{HOT}^{\\mathrm{lc}}_W(S') \\arrow[dl] \\arrow[dr] & \\\\\n\\mathrm{HOT}_W(S') & & \\mathrm{HOT}^{o}_W(S') \n\\end{tikzcd}"
    vi = 'Der-ChVI-345/Der-ChVI-345_p121-125.tex'
    return dict(spans_reviewed=len(candidates),
                reviewed_units_exact=len(candidates)==8 and {r['unit'] for r in candidates}==set(ALIGNMENT_NOTES),
                no_other_single_row_alignment_spans=not extra_single,
                unexpected_single_row_spans=extra_single,
                vi_author_triangle_exact=expected_triangle in readings[vi],
                decisions=[dict(unit=r['unit'],kind=r['kind'],decision=ALIGNMENT_NOTES.get(r['unit'],'UNREVIEWED')) for r in candidates])

def ownership_checks(originals, readings, lang):
    toc = 'dertbmt/dertbmt_p001-005.tex'
    xiv_a = 'Der-ChXIV-07-10-10/Der-ChXIV-07-10-10_p006-010.tex'
    xiv_b = 'Der-ChXIV-07-10-10/Der-ChXIV-07-10-10_p011-011.tex'
    fn1 = 'der-ch18/der-ch18_p016-020.tex'
    fn58 = 'der-ch18/der-ch18_p046-050.tex'
    toc_text = 'Dans cette table de matières' if lang == 'FR' else 'In this table of contents'
    heading = r'\section*{Postface des éditeurs}' if lang == 'FR' else r"\section*{Editors' afterword}"
    note1 = signed_footnotes(originals[fn1])
    note58 = signed_footnotes(originals[fn58])
    assert len(note1) == len(note58) == 1
    command, inner, _ = note58[0]
    if lang == 'FR':
        a = inner.index('“'); b = inner.index('”', a+1)+1
        h = inner.index(r'\textbf{Corollaire.}')
        article = r'\texttt{[une]}'
    else:
        a = inner.index('``'); b = inner.index("''", a+2)+2
        h = inner.index(r'\textbf{Corollary.}')
        article = r'\texttt{[a]}'
    quote = inner[a:b]
    corollary = inner[h:].replace(article, '')
    quoted_footnote = command + quote + r'\par' + '\n' + corollary + '}'
    b_active = active(readings[xiv_b])
    b_without_anchors = re.sub(r'\\(?:printedpage|msp|mspin)\s*\{[^}]*\}', '', b_active)
    tests = {
        'contents_editor_note_removed': toc_text not in readings[toc],
        'xiv_afterword_heading_removed': heading not in readings[xiv_a],
        'xiv_afterword_continuation_only_retained_anchors': not b_without_anchors.strip(),
        'first_signed_editor_footnote_removed': not signed_footnotes(readings[fn1]),
        'fn58_editorial_signature_removed': not signed_footnotes(readings[fn58]),
        'fn58_exact_author_quote_retained': quote in readings[fn58],
        'fn58_exact_author_corollary_retained': corollary in readings[fn58],
        'fn58_complete_author_only_footnote_exact': quoted_footnote in readings[fn58],
    }
    return tests

def snapshot(lang):
    master_path = ROOT / f'output/{lang}/DER_{lang}_annotated_master.tex'
    master_text = master_path.read_text()
    payload = master_text.split('\n%%DER_JSON_PAYLOAD_BEGIN%%\n', 1)[1].split('\n%%DER_JSON_PAYLOAD_END%%', 1)[0]
    data = json.loads(payload)
    notes_text = (ROOT / f'output/records/EDITORIAL_NOTES_{lang}.tsv').read_text()
    note_rows = list(csv.DictReader(io.StringIO(notes_text), delimiter='\t'))
    notes = collections.defaultdict(list)
    for row in note_rows:
        notes[row['unit']].append(row)
    source_dir = ROOT / ('work/fr/transcription' if lang == 'FR' else 'work/en/translation')
    issues = []
    checks = []
    marker_hits = []
    originals = {}
    readings = {}
    for unit in data['units']:
        name = unit['unit']
        source = (source_dir / name).read_text()
        source_hash_ok = sha(source) == unit['source_sha256']
        embedded_original_ok = clean(source) == unit['original_source']
        corrected = apply_variants(source, unit['variants'])
        original_body = clean(body(shared_repairs(source, name)))
        corrected_body = clean(body(shared_repairs(corrected, name)))
        expected_dip = PAGEBREAK.sub(r'\\par', original_body)
        actual_dip = strip_attribution(projected_body(unit, 0), lang)
        expected_app = PAGEBREAK.sub(r'\\par', corrected_body)
        actual_app = projected_body(unit, 1)
        actual_app = re.sub(r'\n(?:\\DERmark\{[^{}]+\})+\n', '', actual_app)
        actual_app = strip_attribution(actual_app, lang)
        replayed, matched, missing = replay(corrected_body, notes[name], lang)
        expected_read = PAGEBREAK.sub(r'\\par', replayed)
        actual_read = projected_body(unit, 2)
        originals[name] = original_body
        readings[name] = actual_read
        _, matched_original, changed_editor = replay(original_body, notes[name], lang)
        record = dict(unit=name, source_hash_match=source_hash_ok,
                      embedded_source_match=embedded_original_ok,
                      diplomatic_body_exact=expected_dip == actual_dip,
                      apparatus_body_exact=expected_app == actual_app,
                      reading_body_replayed_exact=expected_read == actual_read,
                      omission_records=len(notes[name]), replayed_records=len(matched),
                      omissions_present_in_original=len(matched_original),
                      anchor_sequence_exact=all(anchors(projected_body(unit, i)) == anchors(original_body) for i in range(3)))
        for kind, expected, actual in [('diplomatic',expected_dip,actual_dip), ('apparatus',expected_app,actual_app), ('reading',expected_read,actual_read)]:
            if expected != actual:
                issues.append(dict(unit=name, kind=kind, difference=first_difference(expected, actual)))
        issues.extend(dict(unit=name, kind='record_replay', detail=x) for x in missing)
        issues.extend(dict(unit=name, kind='editor_source_changed', detail=x) for x in changed_editor)
        remaining = visible_editor_markers(actual_read)
        marker_hits.extend(dict(unit=name, **x) for x in remaining)
        checks.append(record)
    ownership = ownership_checks(originals, readings, lang)
    numbering = footnote_numbering_checks(originals, readings, lang)
    alignment = alignment_ownership_checks(note_rows, readings)
    unit_pieces = [p for p in data['pieces'] if p[0].startswith('% BEGIN UNIT ')]
    pieces_exact = unit_pieces == [u['forms'] for u in data['units']]
    names = {'FR':['DER_FR_diplomatique','DER_FR_corrige_apparat','DER_FR_texte_de_lecture'],
             'EN':['DER_EN_diplomatic','DER_EN_corrected_apparatus','DER_EN_reading']}[lang]
    flat_files = []
    for index, name in enumerate(names):
        flat = (ROOT / f'output/{lang}/{name}.tex').read_text()
        expected = ''.join(p[index] for p in data['pieces'])
        prefix_at = flat.find(expected[:160])
        exact = prefix_at >= 0 and flat[prefix_at:] == expected
        flat_files.append(dict(file=name+'.tex', sha256=sha(flat), master_projection_exact=exact))
    return dict(language=lang, master_sha256=sha(master_text), notes_sha256=sha(notes_text),
                units=len(checks), variants=data['variants'],
                omission_records=len(note_rows), omission_kinds=dict(collections.Counter(r['kind'] for r in note_rows)),
                neutral_signs=sum(r'\DERlacuna{}' in r['after'] for r in note_rows),
                source_hashes_exact=all(r['source_hash_match'] for r in checks),
                embedded_sources_exact=all(r['embedded_source_match'] for r in checks),
                diplomatic_bodies_exact=all(r['diplomatic_body_exact'] for r in checks),
                apparatus_bodies_exact=all(r['apparatus_body_exact'] for r in checks),
                reading_bodies_replayed_exact=all(r['reading_body_replayed_exact'] for r in checks),
                editorial_records_match_original=all(r['omissions_present_in_original'] == r['omission_records'] for r in checks),
                anchors_exact=all(r['anchor_sequence_exact'] for r in checks),
                unit_projections_match_master_pieces=pieces_exact,
                standalone_files=flat_files, ownership_checks=ownership,
                footnote_numbering=numbering, alignment_note_ownership=alignment,
                remaining_reading_editor_markers=marker_hits, issues=issues, checks=checks)

def write_summary(result, path):
    fr, en = result['languages']
    status = 'PASS' if result['all_checks_passed'] else 'CHECK REQUIRED'
    lines = [
        '# Independent reader note and author-text audit', '',
        f'**Status: {status}.** This audit covers both annotated masters and all six emitted reader sources. It reads the verified original units and replays the recorded changes without importing the reader builder or its editorial-note parser.', '',
        '## Results', '',
        '| Check or count | French | English |',
        '|---|---:|---:|',
        f"| Original units checked | {fr['units']} | {en['units']} |",
        f"| Exact variant intervals | {fr['variants']} | {en['variants']} |",
        f"| Recorded reading omissions or replacements | {fr['omission_records']} | {en['omission_records']} |",
        f"| Neutral signs for missing or illegible text | {fr['neutral_signs']} | {en['neutral_signs']} |",
    ]
    labels = [
        ('source_hashes_exact', 'Original source hashes match'),
        ('embedded_sources_exact', 'Embedded original sources match'),
        ('diplomatic_bodies_exact', 'Diplomatic bodies preserve the source'),
        ('apparatus_bodies_exact', 'Apparatus bodies contain the exact recorded variants'),
        ('editorial_records_match_original', 'Editorial source strings remain unchanged'),
        ('reading_bodies_replayed_exact', 'Every reading-body byte is explained by recorded changes'),
        ('anchors_exact', 'All source page anchors occur in the same order'),
        ('unit_projections_match_master_pieces', 'Unit forms equal the master projection pieces'),
    ]
    for key, label in labels:
        lines.append(f"| {label} | {'Pass' if fr[key] else 'Fail'} | {'Pass' if en[key] else 'Fail'} |")
    lines += [
        f"| Standalone files exactly equal their master projections | {sum(x['master_projection_exact'] for x in fr['standalone_files'])}/3 | {sum(x['master_projection_exact'] for x in en['standalone_files'])}/3 |",
        f"| Unexplained source or projection differences | {len(fr['issues'])} | {len(en['issues'])} |",
        f"| Remaining bracketed editorial markers in reading bodies | {len(fr['remaining_reading_editor_markers'])} | {len(en['remaining_reading_editor_markers'])} |", '',
        'Variant intervals are exact edits, and are not counts of correction-table rows. Duplicate table rows can share an interval, and a row can require several intervals. Omission records also count structural cleanup and retained-author replacements; they are not a census of distinct editorial assertions.', '',
        '## What exact replay proves', '',
        'For every unit, the diplomatic body equals the original body after the declared common typesetting repairs, page-break reflow, privacy redaction, and the separately added editorial attribution label. Removing apparatus markers from the corrected apparatus body gives exactly the original body with its recorded variants. Applying the omission ledger to that corrected body gives exactly the reading body. This checks all body characters. The separate ownership review below establishes which parts of a recorded span belong to the editors and which author parts its replacement must retain; exact replay alone does not establish ownership.', '',
        'The audit also replays every omission source string against the original body. All ledger strings are present unchanged, including the complete unbracketed editorial passages. The shared bold-Delta repair does not occur in any logged editorial passage. Every source anchor argument and its order are checked in all three projections of both languages.', '',
        '## Editorial ownership decisions checked against the supplied sources', '',
        '1. **Plain question marks.** The edition front note states: “Un point d\'interrogation entre crochets signifie que l\'on n\'est pas sûr du mot qui précède.” All twenty-six plain doubt markers in each language, including six with TeX spacing inside the brackets, were inspected in context. They mark uncertainty about the preceding word or expression. The reading form removes the marker and retains that word or expression. Diplomatic and apparatus forms retain the markers. Evidence: the introductory editorial note in `transcription/Der-ChI-234/Der-ChI-234_p001-005.tex` and the twenty-six `plain_editorial_doubt` ledger records.', '',
        '2. **Table-of-contents note.** The final note in `transcription/dertbmt/dertbmt_p001-005.tex` describes the electronic edition’s chapter division and manuscript pagination. Its source wording is retained and attributed in diplomatic/apparatus forms; the reading form omits the exact note and its separator. The table entries remain.', '',
        '3. **Chapter XIV afterword.** The section expressly headed `Postface des éditeurs` / `Editors’ afterword`, printed pages 7–9, is editorial. The reading form omits its two unit spans, while retaining all page anchors. Both other forms preserve its full text. Sources: `transcription/Der-ChXIV-07-10-10/Der-ChXIV-07-10-10_p006-010.tex` and `_p011-011.tex`, with the corresponding translation units.', '',
        '4. **Signed Chapter XVIII footnotes.** The chapter’s front note expressly identifies `N. Éd.` as the mark of editor-added footnotes. In `der-ch18_p016-020.tex`, only the third, signed editorial footnote and its separating comma are removed. The two preceding author footnotes remain. The exact replay checks their complete contents.', '',
        '5. **Author quotations inside footnote 58.** In `der-ch18_p046-050.tex`, the editors explicitly attribute two marginal annotations to Grothendieck: the quotation beginning “cf. résultat plus simple ci-dessus” and the following corollary. The reading form retains those exact author strings, including the original footnote command, and removes the editorial attribution prose and the nested editorial insertion `[une]` / `[a]`. Separate exact-string assertions verify the quotation, the corollary, and their complete retained footnote in both languages. The reading prefaces explain this treatment.', '',
        '6. **Chapter XIII reference material.** Its front note identifies the final indexes, axiom list, glossary, and bibliography as compiled by the editors. These reference sections remain, with their editorial authorship stated in the reading preface.', '',
        '7. **Struck-out and missing-text reports.** The short notes reporting crossed-out words or passages disappear with the other editorial notes. Their surrounding author prose and proofs remain through the exact-body invariant. All eleven neutral replacements were inspected: each records missing or illegible text, including a missing page, theorem number, index, or continuation. The fourteen longest bracketed omissions were also inspected, including array and diagram closings and the definition crossing a printed-page boundary.', '',
        '## Interleaved diagrams and line-break ownership', '',
        'All eight original bracket-note spans containing alignment row breaks were inspected in each language, including their surrounding source cells. No further single-row bracket-note span contains an alignment separator. One span, Chapter VI manuscript pages 197–198, interleaves the author’s left triangle with the editors’ right triangle in a single matrix. Its ledger record now replaces the whole matrix by the exact first three columns of both rows. This retains the author’s apex, both lower objects, and both arrows. The other seven spans contain no interleaved author cell. The audit asserts the complete retained VI triangle and the exact inventory of reviewed spans.', '',
        '| Source unit | Ownership finding |', '|---|---|',
    ]
    for unit, decision in ALIGNMENT_NOTES.items():
        lines.append(f'| `{unit}` | {decision} |')
    lines += ['', '## Footnote markers and numbering', '',
        'The six empty-note removals and the newly removed signed editorial footnote were inspected. All seven remove a complete `\\footnote` call; none removes only a `\\footnotetext` while leaving its paired marker. The five explicit optional numbers 7, 10, 75, 80, and 93 have no separate `\\footnotemark` reference in their respective chapters. Explicit-number `\\footnote[n]` does not advance the standard LaTeX counter; the installed LaTeX kernel’s `\\@xfootnote` definition was checked for this point.', '',
        'The other two omissions remove implicit-number notes and therefore retain an invisible `\\stepcounter{footnote}`. In Chapter XVIII `p016-020`, editor note 18 is omitted and the following author notes remain 19 and 20. In `p091-095`, editor note 104 is omitted and the following author note remains 105. The audit independently simulates the relevant LaTeX counter operations and asserts the original and reading numbers of all three affected author notes in both languages. Their author words are covered by the full-body replay.', '',
        '| Affected author note | Source number | French reading | English reading |', '|---|---:|---:|---:|',
    ]
    for a, b in zip(fr['footnote_numbering']['author_number_checks'], en['footnote_numbering']['author_number_checks']):
        lines.append(f"| {a['author_note_prefix']} | {a['source_number']} | {a['reading_number']} | {b['reading_number']} |")
    lines += ['',
        '## Omission ledger breakdown', '',
        '| Recorded event kind | French | English |',
        '|---|---:|---:|',
    ]
    for kind in sorted(set(fr['omission_kinds']) | set(en['omission_kinds'])):
        lines.append(f"| `{kind}` | {fr['omission_kinds'].get(kind,0)} | {en['omission_kinds'].get(kind,0)} |")
    lines += ['', '## Reproduction and snapshot identity', '',
              'Run `python output/records/scripts/build_appendix_reader_audit.py` from the extracted workspace. The script writes `APPENDIX_READER_NOTES_AUDIT.json` and this report, and exits unsuccessfully if any source, projection, ownership, or replay check fails. The JSON includes all per-unit checks and the six standalone-source hashes.', '',
              '| Audited input | SHA-256 |', '|---|---|',
              f"| Reader builder | `{result['builder_sha256']}` |",
              f"| French annotated master | `{fr['master_sha256']}` |",
              f"| English annotated master | `{en['master_sha256']}` |",
              f"| French omission ledger | `{fr['notes_sha256']}` |",
              f"| English omission ledger | `{en['notes_sha256']}` |", '',
              'These are textual and ownership checks for the identified snapshot. The reader compilation and visual layout checks are recorded separately in the main build records. No original source unit is modified by this audit.', '']
    path.write_text(clean('\n'.join(lines)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='output/records/APPENDIX_READER_NOTES_AUDIT.json')
    args = parser.parse_args()
    result = dict(audit='Independent source and omission-record replay; note ownership additionally inspected against source headings and credits.',
                  builder_sha256=sha((ROOT/'output/records/scripts/build_readers.py').read_text()),
                  languages=[snapshot('FR'), snapshot('EN')])
    required = ['source_hashes_exact','embedded_sources_exact','diplomatic_bodies_exact',
                'apparatus_bodies_exact','reading_bodies_replayed_exact','editorial_records_match_original',
                'anchors_exact','unit_projections_match_master_pieces']
    result['all_checks_passed'] = all(all(lang[key] for key in required)
                                    and all(lang['ownership_checks'].values())
                                    and lang['footnote_numbering']['author_numbers_preserved']
                                    and lang['footnote_numbering']['explicit_removed_note_numbers_have_no_separate_marks']
                                    and all(n==1 for n in lang['footnote_numbering']['invisible_counter_advances'].values())
                                    and lang['alignment_note_ownership']['reviewed_units_exact']
                                    and lang['alignment_note_ownership']['no_other_single_row_alignment_spans']
                                    and lang['alignment_note_ownership']['vi_author_triangle_exact']
                                    and all(x['master_projection_exact'] for x in lang['standalone_files'])
                                    and not lang['issues'] and not lang['remaining_reading_editor_markers']
                                    for lang in result['languages'])
    (ROOT / args.output).write_text(clean(json.dumps(result, ensure_ascii=False, indent=2)) + '\n')
    write_summary(result, (ROOT / args.output).with_suffix('.md'))
    for lang in result['languages']:
        print(json.dumps({k:v for k,v in lang.items() if k not in ('checks','issues','remaining_reading_editor_markers')}, ensure_ascii=False))
        print('Issues:', len(lang['issues']), 'remaining markers:', len(lang['remaining_reading_editor_markers']))
    raise SystemExit(0 if result['all_checks_passed'] else 1)

if __name__ == '__main__':
    main()
