# Root audit of D.2.40

15 November 2026, 22:22 UTC. Status: complete proof audit passed.

The proof determines the actual space five-type of U, rather than assuming
that an abstract homology module is realizable. The previously computed
groups pi3=Z4, pi4=Z4, pi5=Z2 and the nonzero eta action force the unique
nonzero first k-invariant. Integral H4(K(Z4,3))=0 and H5=Z2 make the
coefficient UCT exact with no Ext ambiguity. The next k-invariant is zero
because its nonzero transgression would kill the actual nonzero Hurewicz
image of the pi5 generator. This is only a space-level product splitting.

I opened and read the original Serre PDF at
https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf.
The exact printed passages checked are section 2 no.7, Theorem 1 and
paragraph 7.3, pp.201--203; no.11, pp.204--205, including the higher
coefficient connecting homomorphism, its transgression, the inductive
generator proof and Theorem 4 on p.205; no.14 on p.207 and no.15 on
pp.208--209, including the UCT/Bockstein proof and Theorems 8--9 on p.209.
The webpage text extraction, not an unavailable screenshot image, was the
root reading interface. The older p.206 locator for Theorem 4 was corrected
in the manuscript and results dependency string.

The complete base and fiber generator lists through degree eleven agree
with the admissibility and excess inequalities. The simple transgressive
system must retain r4 squared and s5 squared. Pulling back the coefficient
extension gives delta4 i = Sq1, so d6(s5)=x3 squared. The only additional
nonzero generator transgression in range is d10(Sq4 s5)=z5 squared.
These are a regular sequence: after quotienting by x3 squared, z5 remains
an independent polynomial generator. Thus there are no annihilator cycles.
Naturality kills earlier outgoing differentials on every universally
transgressive generator; the fiber line receives no incoming differential,
and zero transgression leaves no possible later outgoing differential.
This proves permanence for all other needed generators, including s5 squared.

The alternative coefficient fiber supplies an actual r4 with Sq1 r4=z5.
It is therefore legitimate to lift Sq5 Sq2 r4. Any lift v7 of the permanent
Sq2 s5 supplies Sq4 v7, with the required fiber leading term. These two
classes account for the degree-eleven fiber indecomposables; the sole
base indecomposable and the two K(F2,5) indecomposables are positive
Steenrod operations. Every remaining filtration term is a product of
permanent lifts. Filtration induction therefore proves the stated spanning
identity without guessing hidden extensions.

The canonical q4 has zero positive homology squares, including its first
Bockstein, by the actual bottom map and connectivity. Q7 q4 is primitive;
the possible top-operation cross terms contain units in Browder brackets
and vanish. The Nishida coefficients for indices one through three are
even, indices four and five give unstable operations, and indices at
least six vanish by dual Steenrod instability. Hence this class projects
to zero in H11(P5U), while the independently established paired functional
has value one on it. Pure descent from P5U is impossible.

No assertion is made about mu restricted to the five-connected cover,
the stronger relative extension problem, or survival through all ordinary
nullification cones. D.2.4 and D.3.2 remain Open.
