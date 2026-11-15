# Builds pro_prompts_20261110/8_RESIDUE/{PROMPT.md, 8_RESIDUE_background.zip} and the work-folder MANIFEST.tsv.
# Claude (Fable 5.2), 11 Nov 2026. Run with: python -I build_8_RESIDUE.py
import os, io, re, zipfile, hashlib, glob, sys

ROOT = r'C:/Users/user/Documents/derivateurs_companion_20261109'
WORK = ROOT + '/pro_prompts_20261110_work/8_RESIDUE'
OUT = ROOT + '/pro_prompts_20261110/8_RESIDUE'
os.makedirs(OUT, exist_ok=True)
assert sorted(os.listdir(OUT)) in ([], ['8_RESIDUE_background.zip', 'PROMPT.md'], ['PROMPT.md'], ['8_RESIDUE_background.zip'])

ATTACHED = '''## What is attached for this package

One zip, `8_RESIDUE_background.zip`, with `MANIFEST.tsv` at its top (every file with its origin and hash) and these folders:
- `returns/<n>_<NAME>/`: for each of the seven packages its paper (PDF and TeX with `sections/`), register (`*_results.csv`), report and bibliography. No code is attached: write your own.
- `reviews/<n>_<NAME>/`: the reviews. `reviews/7_BISITE/` also has `COMBINED_REVIEW.md` (the seven read together; Leads 1 to 3 above are its section 3).
- `grothendieck/DER_<id>/` and `companion/DER_<id>/`: the transcription and the companion's audit of the chapters involved (I, II, VI, VII, IX, XI to XIII, XV, XVI), as described under WHAT IS ATTACHED below.
- `papers/`: sources and PDFs of the background literature (Cisinski 2004, 2006, 2019; Maltsiniotis 2005 and his book of 2020; Lurie, *Higher Topos Theory*; Quillen 1967; Dwyer–Kan; Thomason; Evrard; Mann 2022; Jansen 2023; Kent–Leininger–Schleimer; Keel; Kaledin; and others listed in the manifest).
Not attached, to be found by you where a Part names them: Lurie, *Higher Algebra*; Brown (1973); Quillen, *Higher algebraic K-theory I*; Aoki (2022), Volpe (2025), Heyer–Mann (2024), Kahn–Maltsiniotis, Rivera–Wierstra–Zeinalian (2021), Ara–Maltsiniotis (the Theorem A, nerve-comparison and Thomason papers), Rijke–Shulman–Spitters (2020). Open them at the source and mark each `verified` or `unverified`.

'''

head = io.open(WORK + '/PROMPT_head.md', encoding='utf-8').read()
assert '## Parts' in head
head = head.replace('## Parts', ATTACHED + '## Parts', 1)
common = io.open(ROOT + '/pro_prompts_20261110/_COMMON_BLOCK.md', encoding='utf-8').read()
prompt = head.rstrip() + '\n\n\n---\n\n' + common
io.open(OUT + '/PROMPT.md', 'w', encoding='utf-8', newline='\n').write(prompt)

# ---- statistics of the Parts
parts_txt = head.split('## Parts', 1)[1]
verbs = ['prove', 'refute', 'decide', 'construct', 'compute', 'classify', 'determine', 'characterize', 'find', 'verify',
         'derive', 'give', 'state', 'check', 'extend', 'define', 'search', 'enumerate', 'recompute', 'settle', 'rewrite', 'run', 'attack', 'test']
strong = ['prove', 'refute', 'decide', 'construct', 'compute', 'classify', 'determine', 'characterize']
stats = []
for m in re.finditer(r'\*\*([A-J])\. (.*?)\*\*(.*?)(?=\n\*\*[A-J]\. |\Z)', parts_txt, re.S):
    body = m.group(3)
    w = len(body.split())
    low = body.lower()
    nall = sum(len(re.findall(r'\b' + v + r'\w*', low)) for v in verbs)
    nstrong = sum(len(re.findall(r'\b' + v + r'\w*', low)) for v in strong)
    stats.append((m.group(1), m.group(2)[:70], w, nstrong, nall))

# ---- the zip
entries = []  # (arcname, source description, bytes)
def add_bytes(arc, data, src):
    entries.append((arc, src, data))
def add_file(arc, path):
    with open(path, 'rb') as f:
        add_bytes(arc, f.read(), path.replace('/', '\\'))

# 1. from the BISITE zip: grothendieck, companion, papers (minus two large ones not used here)
bz = ROOT + '/pro_prompts_20261110/7_BISITE/7_BISITE_background.zip'
man7 = {}
for line in io.open(ROOT + '/pro_prompts_20261110_work/7_BISITE/MANIFEST.tsv', encoding='utf-8'):
    if line.startswith('#') or line.startswith('path_in_zip'): continue
    c = line.rstrip('\n').split('\t')
    if len(c) >= 2: man7[c[0]] = c[1]
skip_papers = ('papers/Heller1988_memoir/', 'papers/Ayoub_these/', 'papers/Lurie_HA/')
with zipfile.ZipFile(bz) as z:
    for i in z.infolist():
        n = i.filename
        if n.endswith('/'): continue
        if n.split('/')[0] not in ('grothendieck', 'companion', 'papers'): continue
        if n.startswith(skip_papers): continue
        add_bytes(n, z.read(n), man7.get(n, 'from 7_BISITE_background.zip'))
have = {e[0] for e in entries}

# 2. further chapters
for ch in ['II-a', 'XIIb-a', 'VII-b', 'VIII-X', 'XV-a', 'XV-b', 'III-V']:
    d = 'DER_' + ch
    p = ROOT + '/packages/%s/%s_text.tex' % (d, d)
    if os.path.exists(p) and 'grothendieck/%s/%s_text.tex' % (d, d) not in have:
        add_file('grothendieck/%s/%s_text.tex' % (d, d), p)
    for suf in ['_overview.tex', '_blocks.tex', '_claims.csv', '_references.bib']:
        p = ROOT + '/checks/%s/%s%s' % (d, d, suf)
        arc = 'companion/%s/%s%s' % (d, d, suf)
        if os.path.exists(p) and arc not in have:
            add_file(arc, p)

# 3. returns
RET = ROOT + '/pro_returns_20261110'
rets = {'1_CATHOT': ('1_CATHOT/CATHOT', 'CATHOT'), '2_TOTAL_ASPHERICITY': ('2_TOTAL_ASPHERICITY/TOTASPH', 'TOTASPH'),
        '3_POLES': ('3_POLES/POLES', 'POLES'), '4_GALOIS': ('4_GALOIS/GALOIS', 'GALOIS'),
        '5_STRATA': ('5_STRATA/STRATA', 'STRATA'), '6_PATHS': ('6_PATHS', 'PATHS'), '7_BISITE': ('7_BISITE', 'BISITE')}
for name, (sub, pre) in rets.items():
    base = RET + '/' + sub
    for suf in ['_paper.pdf', '_paper.tex', '_report.md', '_results.csv', '_references.bib']:
        p = base + '/' + pre + suf
        if os.path.exists(p): add_file('returns/%s/%s%s' % (name, pre, suf), p)
        else: print('MISSING', p)
    for p in sorted(glob.glob(base + '/sections/*.tex')):
        add_file('returns/%s/sections/%s' % (name, os.path.basename(p)), p)

# 4. reviews
REV = ROOT + '/pro_reviews_20261110'
for name in rets:
    for fn in ['REVIEW_author.md', 'REVIEW.md', 'COMBINED_REVIEW.md']:
        p = REV + '/' + name + '/' + fn
        if os.path.exists(p): add_file('reviews/%s/%s' % (name, fn), p)

# 5. further papers from the series downloads
DL = ROOT + '/pro_prompts_20261110_work/_downloads'
extra = ['0706.2874', '1412.0317', '2305.01474', '1503.02036', '2409.17489', '2608.19870', '2205.02353',
         'Cisinski2004_minimal', 'Cisinski1999_Dwyer', 'Maltsiniotis_Ast301', 'Keel1992',
         'DwyerKan1980Calculating', 'DwyerKan1980Function', 'DwyerKan1980Simplicial', 'Thomason1980_CatModel', 'Quillen1967']
def add_tree(arcbase, d):
    if os.path.isfile(d):
        add_file(arcbase, d); return
    for r, _, fs in os.walk(d):
        for f in fs:
            p = os.path.join(r, f).replace('\\', '/')
            arc = arcbase + '/' + os.path.relpath(p, d).replace('\\', '/')
            if arc not in {e[0] for e in entries}:
                add_file(arc, p)
notfound = []
for x in extra:
    if any(e[0].startswith('papers/' + x + '/') for e in entries): continue
    d = DL + '/' + x
    if os.path.exists(d): add_tree('papers/' + x, d)
    else: notfound.append(x)
SO = REV + '/5_STRATA/sources_opened'
for x in sorted(os.listdir(SO)):
    if x.startswith('2308.09551'): continue
    if not any(e[0].startswith('papers/' + x) for e in entries):
        add_tree('papers/' + x, SO + '/' + x)

# size control: drop optional items, largest first, while the raw total is far above the target
def total(): return sum(len(e[2]) for e in entries)
optional = ['papers/Quillen1967', 'papers/Maltsiniotis_Ast301', 'papers/Brown1973', 'papers/Joyal_quasicat', 'papers/Cisinski_CatLR']
dropped = []

def write_zip(path):
    rows = []
    for arc, src, data in sorted(entries):
        rows.append('%s\t%s\t%s\t%d\t' % (arc, src, hashlib.sha256(data).hexdigest(), len(data)))
    body = 'path_in_zip\tsource_path_or_url\tsha256\tbytes\tnote\n' + '\n'.join(rows) + '\n'
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr('MANIFEST.tsv', '# MANIFEST of 8_RESIDUE_background.zip (%d files besides this one)\n' % len(entries) + body)
        for arc, src, data in sorted(entries):
            z.writestr(arc, data)
    return body

zp = OUT + '/8_RESIDUE_background.zip'
body = write_zip(zp)
while os.path.getsize(zp) > 50_000_000 and optional:
    o = optional.pop(0)
    if any(e[0].startswith(o + '/') or e[0] == o for e in entries):
        entries[:] = [e for e in entries if not (e[0].startswith(o + '/') or e[0] == o)]
        dropped.append(o)
        body = write_zip(zp)
size = os.path.getsize(zp)
sha = hashlib.sha256(open(zp, 'rb').read()).hexdigest()
io.open(WORK + '/MANIFEST.tsv', 'w', encoding='utf-8', newline='\n').write(
    '# MANIFEST of 8_RESIDUE_background.zip (%d files plus MANIFEST.tsv, %d bytes zipped)\n# zip SHA-256: %s\n' % (len(entries), size, sha) + body)

rep = []
rep.append('PROMPT.md: %d bytes, %d words; head %d words' % (len(prompt.encode('utf-8')), len(prompt.split()), len(head.split())))
for s in stats: rep.append('Part %s (%s): %d words, %d strong verbs, %d demanding verbs' % (s[0], s[1], s[2], s[3], s[4]))
rep.append('Parts total: %d words, %d strong, %d all' % (sum(s[2] for s in stats), sum(s[3] for s in stats), sum(s[4] for s in stats)))
rep.append('zip: %d files + MANIFEST.tsv, %d bytes, sha256 %s' % (len(entries), size, sha))
top = {}
for arc, _, data in entries:
    k = arc.split('/')[0]; top.setdefault(k, [0, 0]); top[k][0] += 1; top[k][1] += len(data)
rep.append('by folder (files, raw bytes): ' + str(top))
rep.append('downloads not found: ' + str(notfound) + '; dropped for size: ' + str(dropped))
rep.append('output folder: ' + str(sorted(os.listdir(OUT))))
io.open(WORK + '/ASSEMBLY.md', 'w', encoding='utf-8', newline='\n').write('# Assembly of 8_RESIDUE (build_8_RESIDUE.py)\n\n' + '\n'.join('- ' + r for r in rep) + '\n')
sys.stdout.buffer.write(('\n'.join(rep) + '\n').encode('utf-8'))
