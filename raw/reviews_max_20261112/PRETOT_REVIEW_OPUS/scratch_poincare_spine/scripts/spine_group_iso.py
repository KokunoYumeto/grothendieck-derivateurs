"""pi_1(K) for the dodecahedral 2-skeleton K, after Tietze moves on the output of
dodecahedral_spine.py: x6 = x7 = x5 x8, x9 = x5^-1, x4 = x8 x5, leaving
    <s, t | s t s^-1 t s t^-1,  s^-1 t^-1 s^-1 t s^2 t>   (s = x5, t = x8).
The script checks the order of this group by coset enumeration, then searches the
icosian group for images of s, t that satisfy both relators and generate all 120
elements. A surjection between groups of order 120 is an isomorphism, so
pi_1(K) = icosian group = pi_1(P) (the latter by char_table_2I.py).
"""
import importlib.util
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ct", os.path.join(here, "char_table_2I.py"))
ct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ct)

from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup

F, s, t = free_group("s t")
R5 = s * t * s**-1 * t * s * t**-1
R6 = s**-1 * t**-1 * s**-1 * t * s**2 * t
print("order of <s,t | R5, R6>:", FpGroup(F, [R5, R6]).order())

G = sorted(ct.icosians(True), key=lambda q: tuple((x.a, x.b) for x in q))
inv = ct.qconj
mul = ct.qmul


def word(x, y, letters):
    w = ct.ONE
    for c in letters:
        w = mul(w, {"s": x, "S": inv(x), "t": y, "T": inv(y)}[c])
    return w


sol = None
for x in G:
    for y in G:
        if word(x, y, "stStsT") == ct.ONE and word(x, y, "STStsst") == ct.ONE \
                and len(ct.closure([x, y])) == 120:
            sol = (x, y)
            break
    if sol:
        break
print("images in the icosian group: s ->", sol[0], ", t ->", sol[1])
print("relators hold and the images generate all 120 elements:", sol is not None)
