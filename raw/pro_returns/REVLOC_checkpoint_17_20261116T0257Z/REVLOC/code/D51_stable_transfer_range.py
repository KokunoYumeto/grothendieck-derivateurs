#!/usr/bin/env python3
"""Exact finite quotient check for D.2.51; does not select the actual image."""
from pathlib import Path
import json


def multiple(n, element):
    return ((n * element[0]) % 8, (n * element[1]) % 2)


def transfer(element):
    a, b = element
    return (a % 4, b, b)


def reduced_transfer(element):
    a, b = element
    return (a % 2, a % 2, b, b)


def subgroup(generator):
    return sorted({multiple(n, generator) for n in range(8)})


elements = [(a, b) for a in range(8) for b in range(2)]
allowed = [x for x in elements if not any(reduced_transfer(x))]
assert allowed == [(0, 0), (2, 0), (4, 0), (6, 0)]
assert allowed == subgroup((2, 0))
witnesses = [x for x in allowed if transfer(x)[0] == 2]
assert witnesses == [(2, 0), (6, 0)]
adjusted = []
for x in witnesses:
    n = 1 if x == (2, 0) else 3
    assert multiple(n, x) == (2, 0)
    adjusted.append({"value": x, "sphere_multiple": n, "new_value": (2, 0)})

image_cases = []
for generator in [(0, 0), (4, 0), (2, 0)]:
    image = subgroup(generator)
    boundary_order = next(n for n in range(1, 5) if multiple(n, (2, 0)) in image)
    functional_nonzero = any((x[0] // 2) % 2 for x in image)
    image_cases.append({
        "image_generator": generator,
        "image_elements": image,
        "order_of_boundary_2c": boundary_order,
        "theta_on_image_nonzero": functional_nonzero,
    })
assert [x["order_of_boundary_2c"] for x in image_cases] == [4, 2, 1]
assert [x["theta_on_image_nonzero"] for x in image_cases] == [False, False, True]

result = {
    "status": "PASS",
    "source_group": "Z/8{c} plus Z/2{u}",
    "ordered_reduced_tensor_coordinates": ["a tensor b", "b tensor a", "a tensor r", "r tensor a"],
    "checked_source_elements": len(elements),
    "allowed_by_zero_mod2_products": allowed,
    "pairing_two_values_and_adjustments": adjusted,
    "complete_possible_image_cases": image_cases,
    "scope": "Verifies only the finite algebra after the proved transfer and product-vanishing interfaces. Does not decide the actual stable James-Hopf image, stable sphericity, or the localizer question.",
}
output = Path(__file__).resolve().parent / "outputs" / "D51_stable_transfer_range.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
