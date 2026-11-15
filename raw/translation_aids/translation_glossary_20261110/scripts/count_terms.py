# Batch counts of regexes in one corpus, with the first location (and optionally one context line).
# Usage: python -I count_terms.py DER|LM|PS|<dir-or-file-glob> patterns.txt [ctx]
#   patterns.txt: one regex per line (case-insensitive); lines starting with # are skipped.
#   For PS the location is the file and the nearest preceding section title.
import sys, os, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

work, pf = sys.argv[1], sys.argv[2]
ctx = len(sys.argv) > 3
if work == 'DER':
    files = [(os.path.basename(p)[:-4], p) for p in der_files()]
elif work == 'LM':
    files = [(k, p) for k, p in lm_files() if p]
elif work == 'PS':
    files = [(os.path.basename(p), p) for p in ps_files()]
else:
    files = [(os.path.basename(p), p) for p in sorted(glob.glob(work, recursive=True))]
texts = []
for name, p in files:
    s = read(p)
    if work == 'DER':
        s = expand(strip_comments(body(s)), preamble_macros(s))
    elif work == 'LM':
        s = strip_comments(s)
    texts.append((name, re.sub(r'\s+', ' ', s)))
sec_re = re.compile(r'\\(?:section|chapter|subsection)\*?(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}|\\@dblarg\\@hangsection\{([^{}]*)\}|\\hangsection(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}')
for line in open(pf, encoding='utf-8'):
    pat = line.rstrip('\n')
    if not pat or pat.startswith('#'):
        continue
    rx = re.compile(pat, re.I)
    tot = 0
    first = None
    for name, s in texts:
        for m in rx.finditer(s):
            tot += 1
            if first is None:
                loc = name
                if work == 'PS':
                    secs = re.findall(r'\\label\{sec:([0-9A-Za-z]+)\}', s[:m.start()])
                    loc = 'PS sec. ' + (secs[-1] if secs else '?') + ' (' + name + ')'
                first = (loc, s[max(0, m.start() - 70):m.end() + 70])
    if first and ctx:
        print('%5d  %-40s first: %s | ...%s...' % (tot, pat, first[0], first[1]))
    elif first:
        print('%5d  %-40s first: %s' % (tot, pat, first[0]))
    else:
        print('%5d  %s' % (0, pat))
