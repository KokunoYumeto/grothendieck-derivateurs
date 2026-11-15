"""The icosian group of char_table_2I.py is the preimage in S^3 of the rotation group of
a regular dodecahedron (Hatcher's I_120): each g acts on pure quaternions v by v -> g v g^-1,
and this action preserves the 20 vertices of the dodecahedron used in dodecahedral_spine.py.
The image consists of 60 distinct rotations (g and -g act alike). Exact arithmetic in Q(sqrt5).
"""
import importlib.util, os
from itertools import product
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ct", os.path.join(here, "char_table_2I.py"))
ct = importlib.util.module_from_spec(spec); spec.loader.exec_module(ct)
Q5, half = ct.Q5, ct.half
phi, phinv = Q5(half, half), Q5(-half, half)
Z = Q5(0)
verts = {(Z, Q5(a), Q5(b), Q5(c)) for a, b, c in product((1, -1), repeat=3)}
for s1, s2 in product((1, -1), repeat=2):
    verts |= {(Z, Z, s1 * phinv, s2 * phi), (Z, s1 * phinv, s2 * phi, Z), (Z, s2 * phi, Z, s1 * phinv)}
assert len(verts) == 20
verts_b = {(Z, Q5(a), Q5(b), Q5(c)) for a, b, c in product((1, -1), repeat=3)}
for s1, s2 in product((1, -1), repeat=2):
    verts_b |= {(Z, Z, s1 * phi, s2 * phinv), (Z, s2 * phinv, Z, s1 * phi), (Z, s1 * phi, s2 * phinv, Z)}
assert len(verts_b) == 20
G = ct.icosians(True)
act = lambda g, v: ct.qmul(ct.qmul(g, v), ct.qconj(g))
ok = all({act(g, v) for v in verts} == verts for g in G)
rotations = {tuple(sorted((tuple((x.a, x.b) for x in v), tuple((x.a, x.b) for x in act(g, v))) for v in verts_b)) for g in G}
print("every icosian preserves the dodecahedron of dodecahedral_spine.py:", ok)
ok_b = all({act(g, v) for v in verts_b} == verts_b for g in G)
print("every icosian preserves the mirror dodecahedron (0,+-phi,+-1/phi) cyclic:", ok_b)
print("number of distinct rotations induced:", len(rotations))
