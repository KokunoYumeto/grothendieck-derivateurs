"""Compile fix after GALOIS: \\id is not defined in chunk I-b; and key names in new_misc_STRATA.tex. Run once."""
import pathlib
H = pathlib.Path(__file__).parent
p = H.parent.parent / 'checks' / 'DER_I-b' / 'DER_I-b_blocks.tex'
raw = p.read_bytes()
crlf = b'\r\n' in raw
s = raw.decode('utf-8').replace('\r\n', '\n')
a = s.index(r'{The localizer of locally constant coefficients}')
b = s.index(r'\end{dcomment}', a)
seg = s[a:b]
n = seg.count('\\id)') + seg.count('\\id$')
seg2 = seg.replace('\\id)', '\\mathrm{id})').replace('\\id$', '\\mathrm{id}$')
assert n >= 1 and '\\id' not in seg2.replace('\\mathrm{id}', ''), n
s = s[:a] + seg2 + s[b:]
p.write_bytes((s.replace('\n', '\r\n') if crlf else s).encode('utf-8'))
print('I-b: \\id replaced', n, 'times')
q = H / 'new_misc_STRATA.tex'
t = q.read_text(encoding='utf-8')
for old, new in (('{BarwickGlasmanHaine2020}', '{BGH2020}'), ('{DouteauWaas2022}', '{CDDouteauWaas2022}'),
                 ('with finitely many arrows, still has a realization stratified over the poset of its objects, in which parallel arrows give distinct cells;',
                  'with finitely many arrows, still has a realization stratified over the poset of its objects, in which parallel arrows give distinct cells (with the same unopened comparison as in (2));')):
    assert t.count(old) == 1, old
    t = t.replace(old, new)
q.write_text(t, encoding='utf-8', newline='\n')
print('misc STRATA keys fixed')
