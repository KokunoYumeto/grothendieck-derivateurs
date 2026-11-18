#!/usr/bin/env python3
"""Exact cellular-chain certificate for D_2^(4) M(Z/2,3).

The mathematical model is S^3_+ smash_{C2} M smash M, with the
antipodal action on S^3 and the signed interchange on Moore chains.
The accompanying note proves applicability; this script checks the
integral differential and Smith invariants, not stable attaching maps.
"""
from collections import defaultdict
import json
import sympy as sp
from EH5_braid_moore import integer_homology, homology_mod2


def model():
    cells = defaultdict(list)
    degrees = {"a": 3, "b": 4}
    for i in range(4):
        for x in "ab":
            for y in "ab":
                cells[i + degrees[x] + degrees[y]].append((i, x, y))
    indices = {d: {c: j for j, c in enumerate(cs)} for d, cs in cells.items()}
    ds = {}
    for d, cs in cells.items():
        mat = sp.zeros(len(cells.get(d - 1, [])), len(cs))
        for j, (i, x, y) in enumerate(cs):
            if i:
                mat[indices[d - 1][(i - 1, x, y)], j] += 1
                swap = (-1) ** (degrees[x] * degrees[y])
                mat[indices[d - 1][(i - 1, y, x)], j] += (-1) ** i * swap
            if x == "b":
                mat[indices[d - 1][(i, "a", y)], j] += 2 * (-1) ** i
            if y == "b":
                mat[indices[d - 1][(i, x, "a")], j] += 2 * (-1) ** (i + degrees[x])
        ds[d] = mat
    return cells, ds


def main():
    cells, ds = model()
    for d in sorted(ds):
        if d - 1 in ds:
            assert ds[d - 1] * ds[d] == sp.zeros(ds[d - 1].rows, ds[d].cols)
    ranks, _, _ = homology_mod2(cells, ds)
    result = {
        "space": "S^3_+ smash_{C2} M(Z/2,3)^{smash 2}",
        "scope": "Integral chains and homology only; no stable cell splitting is inferred.",
        "cells": {d: [list(c) for c in cs] for d, cs in sorted(cells.items())},
        "differentials": {d: [[int(x) for x in row] for row in mat.tolist()]
                          for d, mat in sorted(ds.items())},
        "d_squared": "zero in every degree",
        "integral_homology": integer_homology(cells, ds),
        "mod2_homology_ranks": ranks,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
