#!/usr/bin/env python3
"""Exact finite certificate for D.2.45, not a model of the full target.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
The input is the proved low cellular chain model from D.2.43.
The output certifies its ordinary tensor H15 and the norm transfer.
"""
from itertools import product
from pathlib import Path
import json

names15 = ['ab', 'ba', 'ar', 'ra']
d15 = [-4, 4, 0, 0]
names16 = ['bb', 'as', 'sa', 'br', 'rb', 'rr']
d16 = [
    [4, 4, 0, 0], [0, 0, -2, 0], [0, 0, 0, 2],
    [0, 0, 4, 0], [0, 0, 0, 4], [0, 0, 0, 0],
]
assert all(sum(a*b for a, b in zip(d15, col)) == 0 for col in d16)
# The equation -4x+4y=0 has the integral basis t=(1,1,0,0),
# v=(0,0,1,0), w=(0,0,0,1).  It is saturated, since x=y.
relations = [[col[0], col[2], col[3]] for col in d16]
assert relations == [[4, 0, 0], [0, -2, 0], [0, 0, 2],
                     [0, 4, 0], [0, 0, 4], [0, 0, 0]]
assert all(c[0] % 4 == c[1] % 2 == c[2] % 2 == 0 for c in relations)
assert [4, 0, 0] in relations and [0, -2, 0] in relations and [0, 0, 2] in relations

source = list(product(range(8), range(2)))
def transfer(z):
    c, u = z
    return (c % 4, u, u)
kernel = [list(z) for z in source if transfer(z) == (0, 0, 0)]
assert kernel == [[0, 0], [4, 0]]
assert transfer((2, 0)) == (2, 0, 0)
assert len(set(map(transfer, source))) == 8
for x, y in product(source, repeat=2):
    s = ((x[0]+y[0]) % 8, (x[1]+y[1]) % 2)
    a, b = transfer(x), transfer(y)
    assert transfer(s) == ((a[0]+b[0]) % 4,
                           (a[1]+b[1]) % 2, (a[2]+b[2]) % 2)

out = {
    'statement': 'D.2.45',
    'status': 'PASS',
    'chain15_basis': names15,
    'chain16_basis': names16,
    'd15': d15,
    'd16_columns': d16,
    'integral_kernel_basis': [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    'relations_in_kernel': relations,
    'H15': ['Z/4{t}', 'Z/2{v}', 'Z/2{w}'],
    'source': ['Z/8{c}', 'Z/2{u}'],
    'transfer': {'c': [1, 0, 0], 'u': [0, 1, 1]},
    'transfer_kernel': kernel,
    'transfer_of_2c': list(transfer((2, 0))),
    'elements_checked': len(source),
    'addition_pairs_checked': len(source)**2,
    'scope': 'No full-target cup product or stable Hurewicz image is computed.',
}
dest = Path(__file__).resolve().parents[1] / 'outputs' / 'D45_integral_transfer.json'
dest.parent.mkdir(exist_ok=True)
dest.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
