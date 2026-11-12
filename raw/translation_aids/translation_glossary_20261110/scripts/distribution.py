# Distribution of competing forms over the chapters (DER) or archive files (LM).
# Usage: python -I distribution.py DER|LM patterns.txt
#   patterns.txt: one regex per line (case-sensitive, applied to the macro-expanded, comment-stripped source).
# Output: per regex the total and the counts per chapter folder (DER) or per cote group (LM), and the first file.
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

work, pf = sys.argv[1], sys.argv[2]
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
for line in open(pf, encoding='utf-8'):
    pat = line.rstrip('\n')
    if not pat or pat.startswith('#'):
        continue
    rx = re.compile(pat)
    c = collections.Counter()
    first = None
    for g, name, s in texts:
        n = len(rx.findall(s))
        if n:
            c[g] += n
            first = first or name
    print('%6d  %-46s %s  first %s' % (sum(c.values()), pat, ' '.join('%s:%d' % kv for kv in c.items()), first))
    # optional third argument: a group (chapter or cote) for which the counts are also given per file
    if len(sys.argv) > 3:
        row = ['%s:%d' % (name[-8:], len(rx.findall(s))) for g, name, s in texts if g == sys.argv[3]]
        print('          per file in %s: %s' % (sys.argv[3], ' '.join(row)))
