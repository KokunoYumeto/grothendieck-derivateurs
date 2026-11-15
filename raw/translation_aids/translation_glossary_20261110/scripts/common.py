# Shared helpers: file selection and text/math separation. Read-only on the sources.
import os, re, glob, unicodedata
DOC = r'user\Documents'
DER_DIR = os.path.join(DOC, 'derivateurs_opus_pilot_20261109', 'out_all')
LM_DIR = os.path.join(DOC, 'longue_marche_pro_pilot_20261104')
PS_DIR = os.path.join(DOC, 'pursuing_stacks_expert_20261110', 'src')
OUT = os.path.join(DOC, 'translation_glossary_20261110')


def der_files():
    return sorted(glob.glob(os.path.join(DER_DIR, '*', '*.tex')))


def lm_files():
    """Per package: second_pass checked_fixed, then checked, then answers/fixed,
    then answers/unzipped, then answers/ (the pilot packages P01, P02, P04)."""
    sp = os.path.join(LM_DIR, 'second_pass')
    an = os.path.join(LM_DIR, 'answers')
    keys = set()
    for f in os.listdir(sp):
        m = re.match(r'LM_(.+?)_checked(_fixed)?\.tex$', f)
        if m:
            keys.add(m.group(1))
    for f in os.listdir(os.path.join(an, 'fixed')):
        m = re.match(r'LM_(.+?)_transcription\.tex$', f)
        if m:
            keys.add(m.group(1))
    for f in os.listdir(os.path.join(an, 'unzipped')):
        if f.startswith('LM_'):
            keys.add(f[3:])
    for f in os.listdir(an):
        m = re.match(r'LM_(P\d+)_transcription\.tex$', f)
        if m:
            keys.add(m.group(1))
    # P057 was second-passed as P057api; P068..P071 are superseded by the combined packages
    if 'P057api' in keys:
        keys.discard('P057')
    for k in ('P068', 'P069', 'P070', 'P071'):
        keys.discard(k)
    out = []
    for k in sorted(keys):
        cands = [os.path.join(sp, 'LM_%s_checked_fixed.tex' % k),
                 os.path.join(sp, 'LM_%s_checked.tex' % k),
                 os.path.join(an, 'fixed', 'LM_%s_transcription.tex' % k),
                 os.path.join(an, 'unzipped', 'LM_%s' % k, 'LM_%s_transcription.tex' % k),
                 os.path.join(an, 'LM_%s_transcription.tex' % k)]
        for c in cands:
            if os.path.exists(c):
                out.append((k, c))
                break
        else:
            out.append((k, None))
    return out


def ps_files():
    return sorted(glob.glob(os.path.join(PS_DIR, 'ps[1-7].tex')))


def read(p):
    with open(p, encoding='utf-8', errors='replace') as f:
        return f.read()


def strip_comments(s):
    return re.sub(r'(?<!\\)%.*', '', s)


def body(s):
    i = s.find(r'\begin{document}')
    if i >= 0:
        s = s[i + len(r'\begin{document}'):]
    j = s.find(r'\end{document}')
    if j >= 0:
        s = s[:j]
    return s


def preamble_macros(s):
    """No-argument \\newcommand and \\DeclareMathOperator definitions in the preamble."""
    i = s.find(r'\begin{document}')
    pre = s[:i] if i >= 0 else ''
    d = {}
    for m in re.finditer(r'\\(?:re|provide)?newcommand\*?\{?(\\[A-Za-z]+)\}?(\[\d\])?\{', pre):
        if m.group(2):
            continue
        st = m.end()
        depth = 1
        k = st
        while k < len(pre) and depth:
            if pre[k] == '{' and pre[k - 1] != '\\':
                depth += 1
            elif pre[k] == '}' and pre[k - 1] != '\\':
                depth -= 1
            k += 1
        d[m.group(1)] = pre[st:k - 1]
    for m in re.finditer(r'\\DeclareMathOperator(\*?)\{(\\[A-Za-z]+)\}\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', pre):
        d[m.group(2)] = r'\operatorname' + m.group(1) + '{' + m.group(3) + '}'
    return d


def expand(s, d):
    if not d:
        return s
    names = sorted(d, key=len, reverse=True)
    pat = re.compile('(' + '|'.join(re.escape(n) for n in names) + r')(?![A-Za-z])')
    for _ in range(3):
        s2 = pat.sub(lambda m: d[m.group(1)], s)
        if s2 == s:
            break
        s = s2
    return s


MATH_ENVS = (r'equation\*?|align\*?|aligned|gather\*?|gathered|multline\*?|tikzcd|array|cases|eqnarray\*?|'
             r'displaymath|math|split|alignat\*?|matrix|pmatrix|bmatrix|smallmatrix|tikzpicture|xy')
_math_re = re.compile(
    r'\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\begin\{(' + MATH_ENVS + r')\}.*?\\end\{\1\}',
    re.S)
MARK = '\u00a7'


def split_math(s):
    """Returns (text with each formula replaced by the mark, list of formulas)."""
    maths = []

    def rep(m):
        maths.append(m.group(0))
        return ' ' + MARK + ' '
    t = _math_re.sub(rep, s)
    return t, maths


def detex_text(t):
    """Keep the content of text-level macros (\\deleted, \\inserted, \\unsure, \\textit ...), drop the commands."""
    t = re.sub(r'\\(scanpage|mspage|printedpage|msp|label|ref|tag\*?|vspace\*?|hspace\*?|includegraphics(\[[^\]]*\])?)\{[^{}]*\}', ' ', t)
    t = re.sub(r'\\(begin|end)\{[^{}]*\}(\[[^\]]*\])?', ' ', t)
    t = re.sub(r"\\[a-zA-Z@]+\*?", ' ', t)
    t = re.sub(r'\\.', ' ', t)
    t = t.replace('{', '').replace('}', '').replace('~', ' ')
    t = t.replace('\u2019', "'").replace('\u0153', 'oe').replace('\u0152', 'Oe')
    return t


def fold(w):
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(c for c in w if unicodedata.category(c) != 'Mn')
