# Builds NOTATION_DER.csv, NOTATION_LM.csv and TYPESETTING.csv from the decision files
#   scripts/notation_DER.txt, scripts/notation_LM.txt, scripts/typesetting.txt.
# Line format (notation):     object ;; form := regex || form := regex ... ;; english_form ;; note
# Line format (typesetting):  work ;; written_form ;; form := regex || form := regex ... ;; unified_form ;; note
# The regexes are case-sensitive and run over the source (comments removed; the per-file macros of
# Les Derivateurs expanded). For each form the CSV gives the count, the spread over the chapters (DER) or
# archive files (LM: C1 = cote 140-1, C2a = P01-P030, C2b = P031-P058, C3 = cote 140-3, C4 = cote 140-4)
# and the first file in which it occurs.   Usage: python -I build_tables.py
import sys, os, re, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))


def load(work):
    texts = []
    if work == 'DER':
        for p in der_files():
            s = read(p)
            g = os.path.basename(os.path.dirname(p))
            g = re.sub(r'^[Dd]er-[Cc]h', '', g)
            g = re.sub(r'-.*', '', g)
            texts.append((g, os.path.basename(p)[:-4], expand(strip_comments(body(s)), preamble_macros(s))))
    else:
        for k, p in lm_files():
            if not p:
                continue
            if k.startswith('C'):
                g = k[:2]
            else:
                n = int(re.sub(r'\D.*', '', k[1:]))
                g = 'C2a' if n <= 30 else ('C2b' if n <= 58 else 'C3')
            texts.append((g, k, strip_comments(read(p))))
    return texts


TEXTS = {'DER': load('DER'), 'LM': load('LM')}


def forms(work, spec):
    out = []
    for item in spec.split(' || '):
        label, rx = item.split(' := ', 1)
        rx = re.compile(rx.strip())
        c = collections.Counter()
        first = None
        for g, name, s in TEXTS[work]:
            n = len(rx.findall(s))
            if n:
                c[g] += n
                first = first or name
        tot = sum(c.values())
        if tot:
            spread = ' '.join('%s:%d' % kv for kv in c.most_common(6))
            if len(c) > 6:
                spread += ' +%d more' % (len(c) - 6)
            out.append('%s (%d; %s; first %s)' % (label.strip(), tot, spread, first))
        else:
            out.append('%s (0)' % label.strip())
    return '; '.join(out)


def split(line):
    return [x.strip() for x in re.split(r'\s;;(?:\s|$)', line)]


for work in ('DER', 'LM'):
    rows = []
    for ln, line in enumerate(open(os.path.join(here, 'notation_%s.txt' % work), encoding='utf-8'), 1):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        p = split(line)
        if len(p) != 4:
            print('BAD', work, ln, len(p), line[:70])
            continue
        rows.append((p[0], forms(work, p[1]) if p[1] != '-' else '', p[2], p[3]))
    with open(os.path.join(OUT, 'NOTATION_%s.csv' % work), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['object', 'forms_found_with_counts_and_example_locations', 'english_form', 'note'])
        w.writerows(rows)
    print('NOTATION_%s rows %d' % (work, len(rows)))
rows = []
for ln, line in enumerate(open(os.path.join(here, 'typesetting.txt'), encoding='utf-8'), 1):
    line = line.rstrip('\n')
    if not line.strip() or line.startswith('#'):
        continue
    p = split(line)
    if len(p) != 5:
        print('BAD typesetting', ln, len(p), line[:70])
        continue
    rows.append((p[0], p[1], forms(p[0], p[2]) if p[2] != '-' else 'see note', p[3], p[4]))
with open(os.path.join(OUT, 'TYPESETTING.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['work', 'written_form', 'typeset_variants_with_counts', 'unified_form', 'note'])
    w.writerows(rows)
print('TYPESETTING rows', len(rows))
