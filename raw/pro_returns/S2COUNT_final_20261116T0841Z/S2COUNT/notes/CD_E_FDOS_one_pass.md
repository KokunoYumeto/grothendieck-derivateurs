# Existence-only audit of Farjoun--Orr--Shelah

This is an auxiliary source audit for the unfinished Part E; it is not a
proof of E2--E4, and the distinction below does not affect the iterated
finite-system construction used in audited INDLOCAL A.19.

Primary source: E. Dror Farjoun, K. E. Orr, S. Shelah, *Bousfield
localization as an algebraic closure of groups*, Israel J. Math.
66 (1989), 143--153, DOI 10.1007/BF02765889. Author-hosted original:
https://shelah.logic.at/files/95836/350.pdf.

## What the source actually supplies

Definition 1.1 on p.145 distinguishes existence of solutions to Gamma
systems from uniqueness. Theorem 0.1 on p.143 identifies HZ-locality
with **unique** solvability. The countable-to-arbitrary dependency-closure
argument on p.146 does work for existence alone: solve one countable
closed set of equations, substitute those values into the other equations,
and continue transfinitely. There is no missing compatibility in that
argument, since the old values are fixed by actual substitution.

The central-extension lifting argument in Example 1.7(v), pp.147--148,
also gives an existence-only assertion when the base is Gamma-soluble.
It does not yield the needed countable simple target, or make ordinary
equational compactness equivalent to Gamma-solubility.

## The literal one-pass group in Section 3.1

On p.151 the source describes CG by adjoining separate variable sets
for every countable Gamma system over G and imposing each system's
relations. It then asserts that this one group solves every Gamma
system over CG. Read literally, without an additional identification
of earlier solutions or further passes, this assertion is false.

Indeed, for G=1 the construction is the free product of the presentation
groups of all coefficient-free countable Gamma systems. If Q is any
finite perfect group, choose, for each q in Q, an expression for q as a
finite product of commutators of elements of Q. Introduce variables X_q
and the corresponding equations

    X_q = product of commutators of the X_r.

This is a finite coefficient-free Gamma system; the evaluations
X_q -> q give its presentation group an epimorphism onto Q. Killing
all other free factors therefore gives an epimorphism C1 -> Q.

Gamma-solubility passes to quotients: lift the coefficients of a system,
solve the lifted system, and project. Consequently it suffices to exhibit
a finite perfect Q that is not Gamma-soluble.

Take the binary icosahedral group

    Q = <a,b | a^5=b^3, b^3=(ba)^2>.

The primary identification and order 120 are Mikhailov--Orr,
arXiv:1306.6065v1, Example 3.2; this is the same example used in
Statement E.13. Its exponent matrix has determinant -1, so its
abelianization is trivial. In Q put

    x=b^2,  h=a^2 b a^-1 b a^-2.

The accompanying finite calculation verifies |x|=3 and h^-1 x h=x^2.
Thus the finite self-map

    phi(u)=u^-2 h^-1 u h

has phi(1)=phi(x)=1 and cannot be onto. The calculation gives the
more explicit facts that its image has 80 elements and does not contain
b. Hence

    u = [u^-1,h^-1] b^-1

is an unsolvable Gamma equation over Q, for the convention
[r,s]=r s r^-1 s^-1. Its equivalent form is phi(u)=b. This proves
that the literal C1 is not Gamma-soluble.

The exact compatibility issue in the printed substitution argument is
that a solution of the enlarged system can assign previously adjoined
variables different values from the already selected coefficient values.
Their old defining equations permit this unless uniqueness has been
imposed. The existence of some joint solution does not imply an extension
of the prescribed old solution.

## Limit of this observation

This is **not** a rejection of the paper's HZ-localization theorem.
For the quotient CG/Gamma(CG), at-most-one-solution is the relevant
additional fact. After projecting a joint solution to that quotient,
its old-system coordinates must agree with the projected old coefficient
coordinates. This repairs precisely the compatibility issue in the
localization argument. Alternatively, an existence-only construction
can use repeated stages, but its size and embedding/asphericity
properties must then be proved separately.

Accordingly Section 3.1 is not a valid shortcut from arbitrary countable
equational-compactness obstructions to the aspherical, relative integral
homology equivalences required by Part E.

Verification: `code/CD_E_FDOS_one_pass_check.py` and its saved output.
