# Inventories for the glossary: n-grams outside mathematics (spelling, accent, hyphen, number and gender
# variants grouped), LaTeX alphabets and decorations per letter, operator names by command, arrows and
# symbols, per-file macro definitions (Les Derivateurs: every file has its own preamble).
# Usage: python -I inventory.py DER|LM
import sys, os, re, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
sys.stdout.reconfigure(encoding="utf-8")

work = sys.argv[1]
if work == 'DER':
    files = [(os.path.basename(p)[:-4], p) for p in der_files()]
else:
    files = [(k, p) for k, p in lm_files() if p]
inv = os.path.join(OUT, 'inventory')
os.makedirs(inv, exist_ok=True)

STOP = set("""a à au aux avec ce ces cet cette ceci cela c ça comme d dans de des du donc dont elle elles en est et etc eu
il ils j je l la le les leur leurs lui m mais me même n ne ni nous on ou où par pas pour qu que qui s sa se ses si son sont
sur t te tout tous toute toutes un une y ai ainsi alors aussi bien cas ceux deux être fait faire ie
mon ma mes moins plus peut pu quand sans soit sous très ont été avoir ayant étant entre encore déjà ici là non oui
peu car or cf voir resp ib id dire dit doit puis vers chez tel telle tels telles autre autres quelque quelques
lorsque puisque pourvu celui celle celles lequel laquelle lesquels auquel dès après avant jusqu enfin
donne donné prend pris vu soient serait sera était avait aurait suis sommes afin quel quelle quels quelles
dessus dessous notamment également toujours jamais parfois souvent seulement surtout assez trop beaucoup chaque aucun aucune
premier première second seconde trois quatre the of and to in is for that""".split())
word_re = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ" + MARK + r"]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ]+)*")
ELIDE = re.compile(r"^(l|d|s|n|qu|c|j|m|t|jusqu|lorsqu|puisqu)'", re.I)


def key_of(tokens):
    ks = []
    for w in tokens:
        f = fold(w).replace('-', '').replace("'", '')
        if len(f) > 3 and f.endswith(('s', 'x')):
            f = f[:-1]
        if len(f) > 4 and f.endswith('e'):
            f = f[:-1]   # crude gender folding
        ks.append(f)
    return ' '.join(ks)


groups = collections.defaultdict(collections.Counter)
firstloc = {}
alph = collections.defaultdict(collections.Counter)
alph_loc = {}
opn = collections.defaultdict(collections.Counter)
opn_loc = {}
syms = collections.Counter()
macros = collections.defaultdict(collections.Counter)
cmds = collections.Counter()
nchars = 0
npages = 0
ALPH = re.compile(r'\\(mathcal|mathscr|mathfrak|mathbb|mathbf|boldsymbol|bm|mathsf|mathit|mathrm|mathtt|underline|'
                  r'overline|widehat|widetilde|hat|tilde|bar|check|vec|operatorname\*?|text|textbf|textit|textrm|'
                  r'textsf|pmb|uline)\s*\{([^{}]{1,40})\}')
SYM = re.compile(r'\\([A-Za-z]*[aA]rrow[A-Za-z]*|to|mapsto|longmapsto|leadsto|simeq|cong|approx|sim|equiv|overset|'
                 r'underset|stackrel|varinjlim|varprojlim|injlim|projlim|lim|colim|coprod|amalg|sqcup|bigsqcup|times|'
                 r'otimes|circ|bullet|wr|wedge|emptyset|varnothing|setminus|backslash|smallsetminus|subset|subseteq|'
                 r'varepsilon|epsilon|varphi|phi|Delta|triangle|nabla|star|ast|natural|flat|sharp|dagger|ldots|cdots|'
                 r'dots|iso|isom|xto|buildrel)(?![A-Za-z])')

for name, p in files:
    raw = read(p)
    nchars += len(raw)
    d = preamble_macros(raw) if work == 'DER' else {}
    for k, v in d.items():
        macros[k][v] += 1
    s = strip_comments(body(raw))
    npages += len(re.findall(r'\\printedpage\{|\\scanpage\{', s))
    s = expand(s, d)
    t, maths = split_math(s)
    # compounds whose first part is a formula, e.g. $\DD$-fibration, are kept as "§-fibration"
    t = re.sub(MARK + r' -(?=[A-Za-zÀ-ÿ])', MARK + '-', t)
    t = re.sub(MARK + r' \\[a-z]+\{-(?=[A-Za-zÀ-ÿ])', MARK + '-', t)
    t = detex_text(t)
    for sent in re.split(r'[.;:!?()\[\],«»“”"]| ' + MARK + r' ', t):
        toks = [ELIDE.sub('', w) for w in word_re.findall(sent)]
        low = [w.lower() for w in toks if len(w) > 1]
        for n in (1, 2, 3):
            for i in range(len(low) - n + 1):
                g = low[i:i + n]
                if g[0] in STOP or g[-1] in STOP:
                    continue
                if n == 1 and len(g[0]) < 3:
                    continue
                k = key_of(g)
                groups[(n, k)][' '.join(g)] += 1
                firstloc.setdefault((n, k), name)
    for m in maths:
        for a in ALPH.finditer(m):
            c, arg = a.group(1), a.group(2).strip()
            if re.fullmatch(r'[A-Za-z]|\\[A-Za-z]+', arg):
                alph[arg][c] += 1
                alph_loc.setdefault((arg, c), name)
            elif re.fullmatch(r"[A-Za-z][A-Za-zéèàôû.\-' ]{1,24}", arg):
                opn[arg][c] += 1
                opn_loc.setdefault((arg, c), name)
        for a in SYM.finditer(m):
            syms[a.group(1)] += 1
        for a in re.finditer(r'\\arrow\[([^\]]*)\]|\\ar\[([^\]]*)\]', m):
            opts = a.group(1) or a.group(2)
            opts = re.sub(r'"[^"]*"\'?', '', opts)
            for o in opts.split(','):
                o = o.strip()
                if o and not re.fullmatch(r'[udlr]+', o) and 'sep' not in o:
                    syms['tikzcd:' + re.sub(r'=.*', '=', o)] += 1
        for a in re.finditer(r'\\([A-Za-z]+)', m):
            cmds[a.group(1)] += 1


def wr(fn, header, rows):
    with open(os.path.join(inv, fn), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


rows = []
for (n, k), c in groups.items():
    tot = sum(c.values())
    if tot < 3:
        continue
    rows.append((n, k, tot, len(c), '; '.join('%s (%d)' % (v, x) for v, x in c.most_common(8)), firstloc[(n, k)]))
rows.sort(key=lambda r: (r[0], -r[2]))
wr(work + '_ngrams.csv', ['n', 'key', 'total', 'n_variants', 'variants_with_counts', 'first_file'], rows)
rows = []
for L, c in sorted(alph.items(), key=lambda kv: -sum(kv[1].values())):
    rows.append((L, sum(c.values()), len(c),
                 '; '.join('\\%s (%d; first %s)' % (k, v, alph_loc[(L, k)]) for k, v in c.most_common())))
wr(work + '_alphabets_by_letter.csv', ['letter', 'total', 'n_commands', 'commands_with_counts'], rows)
rows = []
for L, c in sorted(opn.items(), key=lambda kv: -sum(kv[1].values())):
    rows.append((L, sum(c.values()), len(c),
                 '; '.join('\\%s (%d; first %s)' % (k, v, opn_loc[(L, k)]) for k, v in c.most_common())))
wr(work + '_names_by_command.csv', ['name', 'total', 'n_commands', 'commands_with_counts'], rows)
wr(work + '_symbols.csv', ['command', 'count'], syms.most_common())
wr(work + '_math_commands.csv', ['command', 'count'], cmds.most_common())
if macros:
    rows = []
    for k, c in sorted(macros.items(), key=lambda kv: -sum(kv[1].values())):
        rows.append((k, sum(c.values()), len(c), ' || '.join('%s (%d)' % (dd, v) for dd, v in c.most_common())))
    wr(work + '_macros.csv', ['macro', 'n_files', 'n_definitions', 'definitions_with_file_counts'], rows)
print(work, 'files', len(files), 'chars', nchars, 'page markers', npages, 'ngram groups', len(groups))
