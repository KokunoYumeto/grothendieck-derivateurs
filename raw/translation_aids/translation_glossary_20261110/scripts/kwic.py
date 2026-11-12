# Key word in context, with a total count.
# Usage: python -I kwic.py DER|LM|PS "regex" [max_lines] [width] [cs]
#   DER and LM: comments stripped, per-file macros of Les Derivateurs expanded. PS: Pursuing Stacks (ps1..ps7.tex).
#   "cs" as fifth argument makes the search case-sensitive.
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

work, pat = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 15
wd = int(sys.argv[4]) if len(sys.argv) > 4 else 90
cs = len(sys.argv) > 5 and sys.argv[5] == 'cs'
if work == 'DER':
    files = [(os.path.basename(p)[:-4], p) for p in der_files()]
elif work == 'LM':
    files = [(k, p) for k, p in lm_files() if p]
else:
    files = [(os.path.basename(p), p) for p in ps_files()]
rx = re.compile(pat, 0 if cs else re.I)
n = 0
tot = 0
nf = 0
for name, p in files:
    s = read(p)
    if work == 'DER':
        s = expand(strip_comments(body(s)), preamble_macros(s))
    elif work == 'LM':
        s = strip_comments(s)
    s = re.sub(r'\s+', ' ', s)
    hit = False
    for m in rx.finditer(s):
        tot += 1
        hit = True
        if n < mx:
            n += 1
            print('%s: ...%s...' % (name, s[max(0, m.start() - wd):m.end() + wd]))
    nf += hit
print('TOTAL', tot, 'in', nf, 'files')
