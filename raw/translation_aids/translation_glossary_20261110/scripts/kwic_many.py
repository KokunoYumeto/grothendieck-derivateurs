# Several key-word-in-context queries in one run.
# Usage: python -I kwic_many.py DER|LM|PS patterns.txt [lines_per_pattern] [width]
# Prints, per regex: the total, the number of files, and the first contexts (spread over the files).
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

work, pf = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 2
wd = int(sys.argv[4]) if len(sys.argv) > 4 else 80
if work == 'DER':
    files = [(os.path.basename(p)[:-4], p) for p in der_files()]
elif work == 'LM':
    files = [(k, p) for k, p in lm_files() if p]
else:
    files = [(os.path.basename(p), p) for p in ps_files()]
texts = []
for name, p in files:
    s = read(p)
    if work == 'DER':
        s = expand(strip_comments(body(s)), preamble_macros(s))
    elif work == 'LM':
        s = strip_comments(s)
    texts.append((name, re.sub(r'\s+', ' ', s)))
for line in open(pf, encoding='utf-8'):
    pat = line.rstrip('\n')
    if not pat or pat.startswith('#'):
        continue
    rx = re.compile(pat, re.I)
    hits = []
    nf = 0
    for name, s in texts:
        hs = [(name, s[max(0, m.start() - wd):m.end() + wd]) for m in rx.finditer(s)]
        if hs:
            nf += 1
            hits.append(hs)
    tot = sum(len(h) for h in hits)
    print('=== %s : %d in %d files' % (pat, tot, nf))
    # one context per file, files spread evenly
    if hits:
        step = max(1, len(hits) // mx)
        for h in hits[::step][:mx]:
            print('   %s: ...%s...' % h[0])
