#!/usr/bin/env python3
"""Exact finite checks for the gap-polynomial proof in PRETOT.

Requires Python 3 and SymPy. Run from any working directory; the report
is printed and saved beside this script as outputs/semisimplicial_affine_checks.out.
Only n <= 3 is tested here. The paper proves the assertion for every n.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib
import json

import sympy as sp


@lru_cache(maxsize=None)
def cone(n, k):
    """C_(n,k), using the paper's integral coordinate interpolation."""
    z = sp.symbols(f'z0:{n + 2}')
    if n == 0:
        return sp.Poly(1, *z, domain=sp.ZZ)
    y = sp.symbols(f'y0:{n + 1}')
    x = sp.symbols(f'x0:{n + 1}')
    u = sp.Symbol('u')
    previous = cone(n - 1, 2 * k)
    q = previous.as_expr().xreplace(dict(zip(previous.gens, y)))
    z_of_x = tuple(u + sum(x[j:]) for j in range(n + 1)) + (u,)
    lifts = []
    for i in range(n + 1):
        prescribed = q * sp.prod(y[j] ** k for j in range(n + 1) if j != i)
        lift = dict(zip(y, z_of_x[:i + 1] + z_of_x[i + 2:]))
        lifts.append(sp.Poly(prescribed.xreplace(lift), *x, u, domain=sp.ZZ))

    # Inclusion-exclusion over the coordinate hyperplanes x_i = 0.
    result = 0
    for size in range(1, n + 2):
        for subset in combinations(range(n + 1), size):
            rho = {x[i]: sp.Integer(0) for i in subset}
            restricted = lifts[subset[0]].as_expr().xreplace(rho)
            # The boundary value is independent of the chosen member.
            for i in subset[1:]:
                assert sp.expand(lifts[i].as_expr().xreplace(rho) - restricted) == 0
            result += (-1) ** (size + 1) * restricted
    result = sp.expand(result)
    for i in range(n + 1):
        assert sp.expand((result - lifts[i].as_expr()).subs(x[i], 0)) == 0
    back = {x[i]: z[i] - z[i + 1] for i in range(n + 1)}
    back[u] = z[-1]
    return sp.Poly(result.xreplace(back), *z, domain=sp.ZZ)


def nonzero_terms(counter):
    return {key: int(value) for key, value in counter.items() if value}


def merged_face(poly, i, k):
    """Compute y_i^k D_i(poly) directly on exponent tuples."""
    out = defaultdict(int)
    for gaps, coefficient in poly.terms():
        merged = gaps[:i] + (gaps[i] + gaps[i + 1] + k,) + gaps[i + 2:]
        out[merged] += int(coefficient)
    return nonzero_terms(out)


def to_injection_combination(poly, n, target):
    """An independent combinatorial reading of the polynomial's monomials."""
    out = {}
    for gaps, coefficient in poly.terms():
        assert sum(gaps) == target - n
        injection = tuple(i + sum(gaps[:i + 1]) for i in range(n + 1))
        assert all(a < b for a, b in zip(injection, injection[1:]))
        assert 0 <= injection[0] <= injection[-1] <= target
        recovered = (injection[0],) + tuple(
            injection[i] - injection[i - 1] - 1 for i in range(1, n + 1)
        ) + (target - injection[-1],)
        assert recovered == gaps
        out[injection] = int(coefficient)
    return out


def postcompose(t, injection):
    out = defaultdict(int)
    for arrow, coefficient in t.items():
        out[tuple(arrow[i] for i in injection)] += coefficient
    return nonzero_terms(out)


def main():
    reports = []
    for n in range(4):
        poly = cone(n, 1)
        degree = 2 ** (n + 1) - n - 2
        target = n + degree
        assert poly.total_degree() == degree
        assert sum(int(c) for _, c in poly.terms()) == 1
        faces = [merged_face(poly, i, 1) for i in range(n + 1)]
        assert all(face == faces[0] for face in faces)
        t = to_injection_combination(poly, n, target)
        checked = 0
        for m in range(n + 1):
            all_maps = list(combinations(range(n + 1), m + 1))
            reference = postcompose(t, all_maps[0])
            for injection in all_maps:
                assert postcompose(t, injection) == reference
                checked += 1
        assert checked == 2 ** (n + 1) - 1
        canonical = json.dumps(
            [[list(exponents), int(coefficient)] for exponents, coefficient in poly.terms()],
            separators=(',', ':'),
        ).encode('ascii')
        reports.append({
            'n': n,
            'target_M': target,
            'polynomial_degree': degree,
            'nonzero_integer_coefficients': len(t),
            'augmentation': sum(t.values()),
            'cofaces_equal': True,
            'all_parallel_injections_equalized': True,
            'injections_checked': checked,
            'coefficient_sha256': hashlib.sha256(canonical).hexdigest(),
        })

    # Also verify the auxiliary values k > 1 used in the recursion.
    auxiliary = []
    for n, k in ((0, 2), (0, 4), (0, 8), (1, 2), (1, 4), (2, 2)):
        poly = cone(n, k)
        assert poly.total_degree() == k * (2 ** (n + 1) - n - 2)
        assert sum(int(c) for _, c in poly.terms()) == 1
        faces = [merged_face(poly, i, k) for i in range(n + 1)]
        assert all(face == faces[0] for face in faces)
        auxiliary.append({'n': n, 'k': k, 'normalized_face_identity': True})

    report = {
        'finite_scope': 'n = 0,1,2,3; unbounded induction is in the paper',
        'cases': reports,
        'recursive_auxiliary_cases': auxiliary,
        'first_nontrivial_polynomial': str(cone(1, 1).as_expr()),
        'all_exact_checks_passed': True,
    }
    rendered = json.dumps(report, indent=2) + '\n'
    output = Path(__file__).resolve().parent / 'outputs'
    output.mkdir(exist_ok=True)
    (output / 'semisimplicial_affine_checks.out').write_text(rendered, encoding='utf-8')
    print(rendered, end='')


if __name__ == '__main__':
    main()
