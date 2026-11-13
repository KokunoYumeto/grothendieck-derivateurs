"""Exact certificate for the rational resolving-class counterexample.

The category is infinite but finitely specified.  Associativity is checked
symbolically for every composable triple of arrow *families*, with three
independent integer exponent variables.  This is not a bounded exponent
enumeration.  Polynomial calculations use exact SymPy arithmetic over Q.
"""

from dataclasses import dataclass
import itertools
import json
import sympy as sp


@dataclass(frozen=True)
class Arrow:
    kind: str
    source: str
    target: str
    index: int = 0
    # Affine form c + n1*x1 + n2*x2 + n3*x3.
    exponent: tuple = (0, 0, 0, 0)


def plus(left, right):
    return tuple(x + y for x, y in zip(left, right))


def constant(value):
    return (value, 0, 0, 0)


offsets = ((0, 1, 2), (0, 2, 1))


def identity(obj):
    return Arrow('sigma', 'v', 'v') if obj == 'v' else Arrow('id', obj, obj)


def compose(g, f):
    """Return g after f, for all integer values of exponent variables."""
    assert f.target == g.source
    if g.kind == 'id':
        return f
    if f.kind == 'id':
        return g
    if g.kind == 'terminal':
        return Arrow('terminal', f.source, 't')
    if g.kind == 'sigma':
        assert f.kind in ('sigma', 'h', 'b')
        return Arrow(f.kind, f.source, 'v', f.index,
                     plus(g.exponent, f.exponent))
    if g.kind == 'h' and f.kind == 'a':
        return Arrow('b', 'p', 'v', exponent=plus(
            g.exponent, constant(offsets[g.index][f.index])))
    raise AssertionError(('unlisted composable families', g, f))


def families(variable):
    exponent = [0, 0, 0, 0]
    exponent[variable] = 1
    exponent = tuple(exponent)
    arrows = [identity(x) for x in ('p', 'q', 't')]
    arrows += [Arrow('terminal', x, 't') for x in ('p', 'q', 'v')]
    arrows += [Arrow('a', 'p', 'q', i) for i in range(3)]
    arrows += [Arrow('sigma', 'v', 'v', exponent=exponent)]
    arrows += [Arrow('h', 'q', 'v', j, exponent) for j in range(2)]
    arrows += [Arrow('b', 'p', 'v', exponent=exponent)]
    return arrows


def main():
    triples = 0
    for f, g, h in itertools.product(families(1), families(2), families(3)):
        if f.target != g.source or g.target != h.source:
            continue
        triples += 1
        assert compose(h, compose(g, f)) == compose(compose(h, g), f)
    identity_checks = 0
    terminal_checks = 0
    for f in families(1):
        assert compose(identity(f.target), f) == f
        assert compose(f, identity(f.source)) == f
        identity_checks += 2
        if f.target != 't':
            terminal_target = Arrow('terminal', f.target, 't')
            assert compose(terminal_target, f) == Arrow('terminal', f.source, 't')
            terminal_checks += 1
    # Inverses are identities for arbitrary formal n.
    sigma = Arrow('sigma', 'v', 'v', exponent=(0, 1, 0, 0))
    sigma_inverse = Arrow('sigma', 'v', 'v', exponent=(0, -1, 0, 0))
    assert compose(sigma, sigma_inverse) == identity('v')
    assert compose(sigma_inverse, sigma) == identity('v')

    t = sp.Symbol('t')
    # Each column j is (h_j a_1 - h_j a_0, h_j a_2 - h_j a_0).
    matrix = sp.Matrix([[t**row[1] - t**row[0] for row in offsets],
                        [t**row[2] - t**row[0] for row in offsets]])
    change = sp.Matrix([[1, 1], [1, -1]])
    diagonal = (change.inv() * matrix * change).applyfunc(sp.factor)
    expected = sp.diag((t - 1) * (t + 2), -t * (t - 1))
    assert diagonal == expected
    determinant = sp.factor(matrix.det())
    assert determinant == -t * (t - 1)**2 * (t + 2)
    integral_determinant = sp.Poly(sp.expand(determinant), t, domain=sp.ZZ)
    assert integral_determinant.as_expr() == -t**4 + 3*t**2 - 2*t
    assert integral_determinant.LC() == -1

    witness = sp.Matrix([t - 1, t - 1])
    relation = matrix * sp.Matrix([1, 1]) - (t + 2) * witness
    assert relation.applyfunc(sp.expand) == sp.zeros(2, 1)
    # Evaluation at t=-2, followed by row (1,1), annihilates image D.
    evaluation_functional = sp.Matrix([[1, 1]])
    assert evaluation_functional * matrix.subs(t, -2) == sp.zeros(1, 2)
    nonzero_value = (evaluation_functional * witness.subs(t, -2))[0]
    assert nonzero_value == -6
    # Failure of the full tensor-stable invariant at n=1 is explicit:
    # (t^2-4) witness = D((t-2),(t-2)).
    invariant_relation = matrix * sp.Matrix([t - 2, t - 2]) - (t**2 - 4) * witness
    assert invariant_relation.applyfunc(sp.expand) == sp.zeros(2, 1)

    print(json.dumps({
        'category': {
            'objects': ['p', 'q', 'v', 't'],
            'terminal_object': 't',
            'endomorphisms_of_v': 'Z, with sigma^n for every n in Z',
            'arrow_families': len(families(1)),
            'symbolic_associativity_triples': triples,
            'symbolic_identity_checks': identity_checks,
            'symbolic_terminal_composition_checks': terminal_checks,
            'independent_exponent_variables': 3,
            'bounded_exponent_enumeration_used': False,
            'offset_table': offsets
        },
        'column_module_at_v': {
            'coefficient_ring': 'Q[t,t^-1]',
            'matrix': [[str(x) for x in row] for row in matrix.tolist()],
            'change_of_basis': [[int(x) for x in row] for row in change.tolist()],
            'change_of_basis_determinant': int(change.det()),
            'diagonal_matrix': [[str(x) for x in row] for row in diagonal.tolist()],
            'determinant': str(determinant),
            'integral_determinant_expanded': str(integral_determinant.as_expr()),
            'integral_determinant_leading_coefficient': int(integral_determinant.LC()),
            'nonzero_mod_every_prime_certificate': 'leading coefficient -1 is a unit modulo every prime',
            'cokernel': 'R/((t-1)(t+2)) direct_sum R/(t-1)',
            'eigenvalue_minus_two_witness': [str(x) for x in witness],
            'witness_relation': '(t+2) z = D(1,1)',
            'detecting_functional': 'evaluate at t=-2, then sum the coordinates',
            'functional_on_witness': int(nonzero_value),
            'invariant_failure_certificate': '(t^2-4) z = D(t-2,t-2)',
            'vector_space_dimension': 3
        },
        'scope': {
            'filtered': True,
            'higher_colimits_of_column_module': 'zero, because t is terminal',
            'refuted': 'universal direct membership of Q_a in the rational resolving closure',
            'not_refuted': 'total implies exact, or use of a different module with the same T_1',
            'closure_invariant': 'sigma^(2n)-2^(2n) is injective for every n>=1',
            'tensor_permutation_closure': 'proved by orbit decomposition in the written proof',
            'integral_strengthening': 'same column module has torsion-free values and lies outside integral P1 closure'
        }
    }, indent=2))


if __name__ == '__main__':
    main()
