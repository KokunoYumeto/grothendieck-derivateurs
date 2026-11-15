# Counts of regexes in a plain-text extraction of a PDF (pages marked "<<<PDFPAGE n>>>"), or in any text
# or TeX files given by a glob. Prints count, first location and one context.
# Usage: python -I count_txt.py "<file-or-glob>" patterns.txt [width]
import sys, os, re, glob
sys.stdout.reconfigure(encoding="utf-8")
src, pf = sys.argv[1], sys.argv[2]
wd = int(sys.argv[3]) if len(sys.argv) > 3 else 60
texts = []
for p in sorted(glob.glob(src, recursive=True)):
    with open(p, encoding='utf-8', errors='replace') as f:
        s = f.read()
    # undo the ligature loss of some PDF text layers and join hyphenated line ends
    s = s.replace('ﬁ', 'fi').replace('ﬂ', 'fl').replace('ﬀ', 'ff').replace('ﬃ', 'ffi')
    s = re.sub(r'-\n(?=[a-z])', '', s)
    s = re.sub(r'[ \t\r\n]+', ' ', s)
    texts.append((os.path.basename(p), s))
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
                pg = re.findall(r'<<<PDFPAGE (\d+)>>>', s[:m.start()])
                loc = ('pdf p. ' + pg[-1]) if pg else name
                first = (loc, s[max(0, m.start() - wd):m.end() + wd])
    if first:
        print('%4d  %-34s %s | ...%s...' % (tot, pat, first[0], first[1]))
    else:
        print('%4d  %s' % (0, pat))
