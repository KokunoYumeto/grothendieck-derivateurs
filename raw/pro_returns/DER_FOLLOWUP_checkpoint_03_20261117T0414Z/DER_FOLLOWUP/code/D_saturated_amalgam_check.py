"""Exact finite certificate for the saturated-chart amalgamation obstruction.

The mathematical proof is in notes/D_saturated_amalgam_obstruction.md.
This script checks the free-group basis identities, the folded labelled
graph, its first-return language structure, and the length contradiction.
It does not assert that the configuration is a C_delta diagram.
"""
from pathlib import Path
import json


def reduce_word(word):
    ans = []
    for a in word:
        if ans and ans[-1] == -a:
            ans.pop()
        else:
            ans.append(a)
    return tuple(ans)


def inverse(word):
    return tuple(-a for a in reversed(word))


def subst(word, images):
    out = []
    for a in word:
        v = images[abs(a)]
        out.extend(v if a > 0 else inverse(v))
    return reduce_word(out)


# Domain generators x,y,z; codomain a,b,c, all numbered 1,2,3.
phi = {1: (1, 2), 2: (2, 1, 3), 3: (2,)}
psi = {1: (1, -3), 2: (3,), 3: (3, -1, -3, 2)}
left = {str(i): subst(phi[i], psi) for i in range(1, 4)}
right = {str(i): subst(psi[i], phi) for i in range(1, 4)}
assert all(left[str(i)] == (i,) for i in range(1, 4))
assert all(right[str(i)] == (i,) for i in range(1, 4))

# The two cycles ab and bac, with all edges also available inversely.
positive_edges = [(0, 1, 1), (1, 2, 0),
                  (0, 2, 2), (2, 1, 3), (3, 3, 0)]
transition = {}
for source, letter, target in positive_edges:
    for s, a, t in ((source, letter, target), (target, -letter, source)):
        assert (s, a) not in transition
        transition[s, a] = t

# Away from root, every vertex has exactly one positive successor.
positive = {}
for source, letter, target in positive_edges:
    positive.setdefault(source, []).append((letter, target))
assert len(positive[0]) == 2
assert all(len(positive[v]) == 1 for v in (1, 2, 3))
first_returns = []
for letter, target in positive[0]:
    word, seen = [letter], set()
    while target:
        assert target not in seen
        seen.add(target)
        nxt, target = positive[target][0]
        word.append(nxt)
    first_returns.append(tuple(word))
assert sorted(first_returns) == sorted([(1, 2), (2, 1, 3)])
assert len(positive_edges) - 4 + 1 == 2

# The second span leg is the same graph after renaming and swapping x,y.
# In the amalgam: x=ab=edf and y=bac=de.
# Subtracting equations |y|-|x|=|c| and |x|-|y|=|f| gives c+f=0.
# Coordinates: |x|,|y|,|c|,|f|.
row1 = (-1, 1, -1, 0)
row2 = (1, -1, 0, -1)
sum_rows = tuple(a + b for a, b in zip(row1, row2))
assert sum_rows == (0, 0, -1, -1)

result = {
    "scope": "A saturated positive free-factor span has no nonerasing free-monoid cocone; not a C_delta counterexample.",
    "phi": phi,
    "psi": psi,
    "psi_phi": left,
    "phi_psi": right,
    "inverse_basis_checks_pass": True,
    "inverse_automaton_folded": True,
    "positive_first_return_words": first_returns,
    "graph_free_rank": 2,
    "length_rows": [row1, row2],
    "length_sum": sum_rows,
    "contradiction": "|c|+|f|=0, impossible when both monoid maps are nonerasing",
}
out = Path(__file__).resolve().parent / "outputs" / "D_saturated_amalgam_check.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
