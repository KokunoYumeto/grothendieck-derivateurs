# La Longue Marche: the \unsure{A|B} alternatives whose two readings differ only in the alphabet, the case or a
# decoration of one symbol (script S against script G, pi against Pi, Sl against SL ...). These are the places
# where the same handwritten form is typeset in two ways; the counts show which pairs are systematically confused.
# Usage: python -I unsure_pairs.py   -> inventory/LM_unsure_symbol_pairs.csv
import sys, os, re, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

pairs = collections.Counter()
loc = {}
tot = 0
for k, p in lm_files():
    if not p:
        continue
    s = strip_comments(read(p))
    i = 0
    while True:
        i = s.find(r'\unsure{', i)
        if i < 0:
            break
        j = i + len(r'\unsure{')
        depth = 1
        st = j
        while j < len(s) and depth:
            c = s[j]
            if c == '\\':
                j += 2
                continue
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            j += 1
        arg = s[st:j - 1]
        i = j
        tot += 1
        if '|' not in arg or len(arg) > 90:
            continue
        parts = arg.split('|')
        if len(parts) != 2:
            continue
        a, b = [re.sub(r'\s+', ' ', x.strip()) for x in parts]
        if a == b:
            continue
        # strip what both share at the two ends, to isolate the symbol that differs
        m = 0
        while m < min(len(a), len(b)) and a[m] == b[m]:
            m += 1
        n = 0
        while n < min(len(a), len(b)) - m and a[-1 - n] == b[-1 - n]:
            n += 1
        # widen to the enclosing command
        da, db = a[:len(a) - n], b[:len(b) - n]
        ka = re.findall(r'(\\[A-Za-z]+\s*\{?[^{}\\ ]*\}?|[A-Za-z])$', da[:max(m + 1, 1)] + da[m + 1:])
        core_a, core_b = da[m:], db[m:]
        if len(core_a) > 25 or len(core_b) > 25:
            continue
        if not re.search(r'[\\$_^]', a + b):
            continue      # word readings, not symbols
        # context: the command just before the differing core
        pre = re.findall(r'(\\[A-Za-z]+\s*\{?)$', a[:m])
        key = tuple(sorted([(pre[0] if pre else '') + core_a, (pre[0] if pre else '') + core_b]))
        pairs[key] += 1
        loc.setdefault(key, k)
rows = [(a, b, n, loc[(a, b)]) for (a, b), n in pairs.most_common() if n >= 3]
with open(os.path.join(OUT, 'inventory', 'LM_unsure_symbol_pairs.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reading_1', 'reading_2', 'count', 'first_package'])
    w.writerows(rows)
print('unsure marks', tot, 'symbol pairs with count >= 3:', len(rows))
for r in rows[:60]:
    print('%4d  %s  |  %s   (%s)' % (r[2], r[0], r[1], r[3]))
