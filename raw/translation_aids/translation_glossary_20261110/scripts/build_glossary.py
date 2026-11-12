# Builds GLOSSARY_DER.csv / GLOSSARY_LM.csv from the decision files scripts/entries_DER.txt and entries_LM.txt.
# Each entry line:  french ;; regex ;; english ;; source_of_english ;; note
# The regex is run (case-insensitive) over the running text of the work: comments removed, per-file macros of
# Les Derivateurs expanded, every formula replaced by the mark "§" (so "$W$-asphérique" reads "§-asphérique"),
# markup commands dropped. The variants and their counts in the CSV are what the regex found, so the counts
# can be reproduced:  python -I build_glossary.py DER|LM
import sys, os, re, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

work = sys.argv[1]
if work == 'DER':
    files = [(os.path.basename(p)[:-4], p) for p in der_files()]
else:
    files = [(k, p) for k, p in lm_files() if p]
chunks = []
for name, p in files:
    raw = read(p)
    d = preamble_macros(raw) if work == 'DER' else {}
    s = expand(strip_comments(body(raw)), d)
    t, maths = split_math(s)
    t = re.sub(MARK + r' -(?=[A-Za-zÀ-ÿ])', MARK + '-', t)
    t = re.sub(MARK + r' \\[a-z]+\{-(?=[A-Za-zÀ-ÿ])', MARK + '-', t)
    t = detex_text(t)
    # words inside formulas (\text{...}, \mathrm{...} labels) are searched too, after the running text
    inner = ' '.join(re.findall(r'\\(?:text|textit|textup|mbox|textrm)\{([^{}]*)\}', ' '.join(maths)))
    t = re.sub(r'\s+', ' ', t + ' ' + inner)
    chunks.append(t)
text = ' \n '.join(chunks)
here = os.path.dirname(os.path.abspath(__file__))
rows = []
zero = []
for ln, line in enumerate(open(os.path.join(here, 'entries_%s.txt' % work), encoding='utf-8'), 1):
    line = line.rstrip('\n')
    if not line.strip() or line.startswith('#'):
        continue
    parts = [x.strip() for x in re.split(r'\s;;(?:\s|$)', line)]
    if len(parts) != 5:
        print('BAD LINE', ln, len(parts), line[:80])
        continue
    fr, rx, en, src, note = parts
    c = collections.Counter()
    if rx != '-':
        for m in re.finditer(rx, text, re.I):
            c[re.sub(r'\s+', ' ', m.group(0).lower())] += 1
    tot = sum(c.values())
    if tot == 0 and rx != '-':
        zero.append(fr)
    var = '; '.join('%s (%d)' % kv for kv in c.most_common(7))
    if len(c) > 7:
        var += '; ... %d more forms' % (len(c) - 7)
    var = ('total %d: ' % tot + var) if rx != '-' else 'not counted (see note)'
    rows.append((fr, var, en, src, note))
out = os.path.join(OUT, 'GLOSSARY_%s.csv' % work)
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['french', 'variants_with_counts', 'english', 'source_of_english', 'note'])
    w.writerows(rows)
print(work, 'entries', len(rows), '->', out)
print('zero-count entries:', zero)
