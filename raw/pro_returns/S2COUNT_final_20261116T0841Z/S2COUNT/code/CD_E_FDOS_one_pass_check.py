"""Finite check for the existence-only warning in FDOS, Section 3.1.

This verifies a word-map obstruction in the binary icosahedral group.
The general argument and the exact limit of the source audit are in
notes/CD_E_FDOS_one_pass.md.  SymPy's finite permutation representation
is obtained from the stated finite presentation by coset enumeration.
"""

from collections import deque

from sympy.combinatorics.fp_groups import FpGroup
from sympy.combinatorics.free_groups import free_group


F, a, b = free_group("a,b")
Q = FpGroup(F, [a**5 * b**-3, b**3 * (b * a)**-2])
P, presentation_map = Q._to_perm_group()
aa, bb = presentation_map(a), presentation_map(b)

words = {P.identity: F.identity}
queue = deque([P.identity])
steps = [(aa, a), (bb, b), (aa**-1, a**-1), (bb**-1, b**-1)]
while queue:
    u = queue.popleft()
    for generator, word in steps:
        v = u * generator
        if v not in words:
            words[v] = words[u] * word
            queue.append(v)

assert len(words) == 120
xx = bb**2
hh = aa**2 * bb * aa**-1 * bb * aa**-2
assert xx.order() == 3
assert hh.order() == 4
assert hh**-1 * xx * hh == xx**2


def phi(u):
    return u**-2 * hh**-1 * u * hh


image = {phi(u) for u in words}
assert phi(P.identity) == phi(xx) == P.identity
assert len(image) == 80
assert bb not in image

print("Presentation: <a,b | a^5=b^3, b^3=(ba)^2>")
print("Finite permutation group order:", len(words))
print("x=b^2 has order", xx.order())
print("h=a^2*b*a^-1*b*a^-2 has order", hh.order())
print("Verified h^-1*x*h=x^2 and phi(1)=phi(x)=1.")
print("phi(u)=u^-2*h^-1*u*h has image size:", len(image))
print("b is not in the image.")
print("Thus u=[u^-1,h^-1]*b^-1 is an unsolvable Gamma equation.")
