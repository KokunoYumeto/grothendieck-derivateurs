# D.2.51 — exact stable pairing criterion

## Status and scope

Proved from D.2.43, D.2.45 and the exact low mod-two product calculation already in D.2.45j. The root and fibrations agent independently passed the mathematical refinement before this final manuscript was written. No new external source statement is used; Klein's transfer identity and comparison with the actual James–Hopf map were opened and audited for D.2.45.

This is an existential equivalence. It does not evaluate the stable Hurewicz image, make the D.2.50 integral cycle stably spherical, choose an order for the actual obstruction, or settle fourth-suspension nullification.

## Complete calculation

Write L = Y<7>, and use the specified quadratic group

    pi15 D2 L = Z/8{c} + Z/2{u},   h = boundary(2c).

The integral transfer followed by Hurewicz is

    c -> t = ab+ba,    u -> ar+ra,

in Z/4{t} + Z/2{ar,ra}. The integral label chains satisfy db=4a and ds=2r. In mod-two homology b is the Moore-four Tor class and r the distinct reduction of the integral order-two class. The four ordered tensors ab, ba, ar, ra are independent.

The full product vanishing H7(L;F2) H8(L;F2)=0, rather than only vanishing of one chosen product, makes the reduced diagonal of every integral fifteen-class zero after mod-two reduction. These are all possible bidegrees because L is six-connected. Apply the actual stable Hopf-transfer identity to a stable sphere. For JH(f)=k c+epsilon u, independence of the four tensors forces k even and epsilon=0. Thus the entire image is contained in <2c>.

The mod-four pairing with a7 red4(b8) is -k mod4. The half-product pairing with theta is one exactly when k=2 or6 modulo8. If k=6, replace f by3f; JH is a homomorphism on pi15 and 3*6=2 modulo8. Hence

    h=0  iff  some stable integral Hurewicz class pairs as2
          iff  some stable integral Hurewicz class pairs with theta as1.

For a particular sphere class, the pairing still does not distinguish JH=2c from JH=6c. The old transfer kernel <4c> is retained, not incorrectly discarded.

The subgroup possibilities are:

| JH image | Order of h | Stable theta functional |
|---|---:|---|
| 0 | 4 | zero |
| <4c> | 2 | zero |
| <2c> | 1 | nonzero |

The D.2.50 ordinary integral class has the required pairing but is not yet known to lie in the stable Hurewicz image. Its existence therefore does not choose a row.

## Audit crosswalk

- D.2.43: actual Goodwillie comparison, quadratic coordinates, and exactness ker(boundary)=im(JH).
- D.2.45e–h: the actual transfer identity and its integral norm calculation, including kernel <4c>.
- D.2.45j: all degree-seven by degree-eight mod-two products vanish. This is the essential stronger input that removes the independent u coordinate.
- D.2.45k: exact coefficient pairing and independence from the Sq1 ambiguity.
- D.2.50: a detected ordinary integral class exists, but stable sphericity is not asserted.
- Parent is preparing the independent finite certificate `code/D51_stable_transfer_range.py`; the proof does not depend on an enumeration in place of the displayed argument.

## Final manuscript

`sections/D2_stable_pairing_equivalence.tex`, tags D.2.51a–k. One owned FGH record; no new bibliography key or duplicated primary source entry.
