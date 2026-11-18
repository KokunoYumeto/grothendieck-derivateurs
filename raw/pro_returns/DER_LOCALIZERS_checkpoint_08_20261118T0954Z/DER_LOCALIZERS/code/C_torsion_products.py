"""Finite arithmetic checks for C.18; the infinite assertion is proved in C.tex.

For q_n: Z/2^n -> Z/2, enumerate every lift of 1 and compute its additive
order.  No bounded enumeration is claimed to prove an infinite-product fact.
"""
from math import gcd


def check_prime_power_lifts(p: int, max_n: int) -> None:
    for n in range(1, max_n + 1):
        modulus = p**n
        lifts = [a for a in range(modulus) if a % p == 1]
        orders = {modulus // gcd(a, modulus) for a in lifts}
        assert orders == {modulus}, (p, n, orders)
        print(
            f"p={p}, n={n}: checked {len(lifts)} lifts of 1; "
            f"every additive order equals {modulus}."
        )


if __name__ == "__main__":
    check_prime_power_lifts(2, 8)
    print("PASS: all finite cyclic calculations.")
    print(
        "Scope: these checks illustrate the formula ord(a mod p^n)=p^n "
        "when a=1 mod p. The proof of the infinite-product obstruction "
        "uses that these orders are unbounded for all n."
    )
