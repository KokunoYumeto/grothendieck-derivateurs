# Finite chain unions: a pure-order extension argument

Proof draft, 18 November 2026, 12:29 UTC. This is an order-theoretic auxiliary
argument, not a monoid or derived-colimit result. The mechanism was discussed
and checked independently by dynamics_totality; this complete note is not
entered as a new numbered theorem. It uses G.43. No compatibility with binary
products is supplied.

## Proposed statement

Fix a finite strong base E. Let L be a finite disjoint union of transitive
smooth G_E-orbits, each identified with strong embeddings of some finite
F_i over E. Suppose L is linearly ordered and the action preserves the order.
The restrictions to individual orbits have their G.19 signed closure flags.

There is an order defined by finitely many raw-coordinate comparisons,
equalities, and fixed finite color priorities on the disjoint union of ALL
increasing raw embeddings of the underlying F_i over E into a dense linear
order, extending the given order on actual strong embeddings. The extension
can introduce additional comparisons at tuple coincidences that cannot occur
between actual strong supports. It need not be unique there.

## 1. Interleaving classes

Say two orbit types interleave if neither whole orbit lies strictly before the
other. Equivalently, the predecessor-cut map from one to the other is neither
constantly empty nor constantly full. By G.43, their first pivot must have
the same raw gap over E and the same sign. For unequal first-pivot values,
comparison is exactly comparison of those values in that sign. This applies
both to realized common first closures and to incompatible closure types,
whose equal-pivot case is impossible in the actual structure.

Interleaving is transitive. If A interleaves B and B interleaves C, all three
have the same first-pivot gap and sign. If A and C were separated blocks,
choose three pivot values in the opposite order to that separation, with the
B value between. These three copies are simultaneously realizable by ordered
free amalgamation over E. The A/B and B/C comparisons contradict the proposed
separation of A and C. Thus the orbit types partition into interleaving
classes. Distinct classes are ordered blocks. Their block order is well
defined: an interleaving orbit cannot lie on opposite sides of a third whole
orbit, since it has points on both sides of every intervening first-pivot
value.

Zero-depth orbits are single points fixed by G_E. They cannot interleave a
nontrivial orbit: an invariant cut in a transitive orbit is empty or full.
They are therefore singleton block types, with their actual mutual order.

## 2. The first coordinate of an interleaving class

Inside a nontrivial interleaving class, put the common signed first pivot
first in the comparison key. Thus all unequal-pivot comparisons already
agree with the actual order. At equal pivots, consider the pointed strong
closure type of E together with that pivot.

Two actual supports with the same pivot necessarily have the same pointed
closure type. For different pointed closure types, actual equality of that
pivot cannot occur. Assign these finitely many types any fixed linear color
order to resolve such artificial ties in the raw-tuple extension. This
assignment changes no actual comparison.

For one common pointed closure type A, the order-preserving pointed
isomorphisms identify the same finite raw coordinate block A in every orbit
that continues through it. Those identifications are unique, since finite
strong structures have the raw linear order. After the pivot and its closure
color, insert all remaining coordinates of A\E in their raw order, omitting
the pivot already used. They are extra lexicographic levels only at artificial
ties: on actual strong embeddings, equality of E and the pivot forces equality
of the entire strong closure A. Inserting these coordinates therefore also
changes no actual comparison.

## 3. Recursion over the common closure

When that full raw closure block agrees, fix its embedding and look at the
fiber of each orbit above it. Each nonempty fiber is a transitive G_A-orbit
with the remaining signed closure flag. Their union is still a chain. Apply
the same construction with base A. Some orbits have now finished and become
singleton tags; the others have shorter flags.

This recursion terminates. Every passage into a pivot block shortens the
remaining flag of each continuing orbit, and only finitely many orbit types
are present. Taking an ordered sum of interleaving blocks at each step,
then a lexicographic pivot coordinate, a finite closure-color priority,
the extra raw closure coordinates, and the recursively constructed fiber
order, gives a linear order on all raw tuples of the indicated types.

The construction is compatible with order embeddings of the ambient raw
linear order: every decision uses only strict order, equality, fixed tuple
coordinate positions, and finite type priorities. Restricting to actual
strong tuples recovers the original order, by induction through the common
closure flags. No arbitrary overlap pattern is being asserted realizable in
the predimension structure; such patterns receive the additional tie rules
only in the auxiliary pure-order structure.

## Remaining scope issues

This argument concerns one linearly ordered union of finitely many orbits.
The finite-orbit rooted tree in G.42 can have branching; a common tree template
needs an additional compatibility argument between its chain components.
Even a completed finite tree template would not by itself preserve monoid
products. A product can have strong support in the closure of two input
supports, with new coordinates outside both. The one-input property for
rooted meets supplies no corresponding one-input property for multiplication.

Likewise, the strict finite direct K-translation enclosure in G.42 does not
automatically cover representative transports after taking an H-quotient.
Their two face composites may differ by a stabilizer element. The cyclic
stabilizer row is already accounted for in G.33, but no argument here removes
the remaining kernel of its transgression.
