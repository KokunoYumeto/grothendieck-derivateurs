"""Match every numbered paper statement to its ledger row and final PDF page.

Run after LuaLaTeX has produced PRETOT_paper.aux.  Works with the self-contained
delivery source or the sectioned development source.  No external data needed.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
from collections import Counter
import csv
import json
import re

ROOT = Path(__file__).resolve().parent.parent


def expanded(path):
    data = path.read_text(encoding='utf-8')
    return re.sub(r'\\input\{([^}]+)\}',
                  lambda m: expanded(ROOT / (m[1] if m[1].endswith('.tex') else m[1]+'.tex')),
                  data)


def main():
    source = expanded(ROOT / 'PRETOT_paper.tex')
    aux = (ROOT / 'PRETOT_paper.aux').read_text()
    labels = {m[1]: (m[2], m[3]) for m in re.finditer(
        r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}', aux)}
    metadata = json.loads((ROOT / 'code/result_metadata.json').read_text())
    pattern = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|definition|'
                         r'example|construction|remark)\}\[([\s\S]*?)\]\s*\\label\{([^}]+)\}')
    matches = list(pattern.finditer(source))
    assert len(matches) == len(metadata), (len(matches), len(metadata))
    assert set(m[3] for m in matches) == set(metadata), 'Missing or surplus result metadata.'
    rows = []
    for m in matches:
        kind, title, lab = m.groups()
        assert lab in labels, ('Uncompiled label', lab)
        number, page = labels[lab]
        row = dict(metadata[lab])
        status_match = re.match(r'(Proved|Refuted|Known|Open)\b', title)
        assert status_match, (lab, title)
        actual_status = status_match[1]
        assert row['status'] == actual_status, (lab,row['status'],actual_status)
        row['id'] = number
        row['where_proved'] = f'{kind.title()} {number}; PRETOT_paper.pdf p. {page}; LaTeX label {lab}'
        dep = row.get('depends_on','')
        for target in sorted(metadata, key=len, reverse=True):
            dep = re.sub(r'(?<![\w:-])'+re.escape(target)+r'(?![\w:-])',
                         lambda _: labels[target][0] + ' [' + target + ']', dep)
        row['depends_on'] = dep
        if row['status'] == 'Open':
            row['manuscript_pages_settled'] = '(Partial; general assertion open) ' + row.get('manuscript_pages_settled','')
        rows.append(row)
    fields = ['id','statement','status','where_proved','depends_on',
              'manuscript_pages_settled','notes']
    with (ROOT / 'PRETOT_results.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=fields)
        writer.writeheader()
        writer.writerows({k:row.get(k,'') for k in fields} for row in rows)
    summary={'numbered_statements':len(rows),'statuses':dict(Counter(r['status'] for r in rows)),
             'all_labels_have_rows':True,'all_rows_have_labels':True,
             'labels':{m[3]:dict(number=labels[m[3]][0],page=int(labels[m[3]][1])) for m in matches}}
    out=ROOT/'code/outputs'
    (out/'results_validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    report=f"Matched {len(rows)} numbered statements to exactly {len(rows)} CSV rows.\nStatus counts: {summary['statuses']}.\nAll printed numbers, labels, and PDF start pages verified: PASS.\n"
    (out/'assemble_results.out').write_text(report)
    print(report,end='')


if __name__=='__main__':
    main()
