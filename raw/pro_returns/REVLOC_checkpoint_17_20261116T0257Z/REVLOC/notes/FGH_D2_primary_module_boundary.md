# Full suspended-source primary tests: an exact boundary

Status: verified 2026-11-15. This records and expands the already stated
boundary in `EH5_first_cone_suspensions.md`, Section 9. It is not a new
numbered result or a new obstruction.

## The proposed test

Put

\[
B=K(\mathbb F_2,2),\quad X=\Sigma B,\quad A=QX,
\quad Y=\Sigma^2B,\quad T=\Omega^2Y.
\]

An arbitrary fourth-suspension map has double adjunct
\(G:\Sigma^2A\to T\). After D.2.36, the dangerous bottom pattern is
\(G_*(\sigma^2B_0)=k=\{a,b\}\), with no linear degree-six component.
One might try to exclude this pattern by computing the complete primitive
Steenrod module of \(T\), including all Dyer--Lashof-generated source
classes of \(A\). Such a test has a compatible solution in every degree.

## An all-degree solution, directly from the stable adjunction

Let \(j:X\to QX=A\) be the stable unit. The counit of
\(\Sigma^\infty\dashv\Omega^\infty\), evaluated at
\(\Sigma^\infty X\), gives an actual spectrum map

\[
p:\Sigma^\infty A\longrightarrow\Sigma^\infty X,
\qquad p\circ\Sigma^\infty j=\mathrm{id}.
\]

The equality is the triangle identity; no realization of a stable
projection as a space map is being asserted. Equivalently, one can use
the weight-one projection in the stable Snaith splitting. For that
choice the higher stable summands are sent to zero.

D.2.29 supplies the actual entire-unit map

\[
g_0:\Sigma^2X=\Sigma^3B\longrightarrow T,
\]

the double adjunct of \([u_4,\mathrm{id}_Y]:\Sigma^5B\to Y\).
Form the stable composite

\[
\Sigma^\infty\Sigma^2A
\xrightarrow{\Sigma^2p}
\Sigma^\infty\Sigma^2X
\xrightarrow{\Sigma^\infty g_0}
\Sigma^\infty T.
\]

Its mod-two homology map \(\Phi\) has all the following properties.

1. It commutes with every homological Steenrod operation, in all
   degrees, because both maps in the composite are spectrum maps.
   It therefore respects every Steenrod-module relation among the
   source Dyer--Lashof classes, including relations beyond the range
   where iterated operations first appear. This is not a claim of
   compatibility with a Dyer--Lashof operation on the suspended source.
2. It restricts on the unit to \((g_0)_*\), by the triangle identity.
   In particular
   \(\Phi(\sigma^2B_0)=k\), while the suspended bottom label maps
   to zero.
3. Its entire reduced image is primitive. Indeed \(\Sigma^2X\) is
   a suspension, and \(g_0\) is an actual space map. Every reduced
   homology class of \(\Sigma^2X\) is primitive, so naturality of
   the diagonal gives the assertion.
4. Extending by the identity in degree zero makes \(\Phi\) a map
   of connected homology coalgebras: the reduced coalgebra of the
   source \(\Sigma^2A\) is also trivial. Thus adding the full
   coalgebra condition, rather than merely listing primitive target
   generators, does not remove this solution.
5. The actual unit map has zero linear degree-eight attaching
   homology, as proved in D.2.29 and required generally by D.2.36.
   Its double-adjoint value \(k\) has zero double homology
   suspension. Hence that additional prescribed low constraint is
   met as well.

The same stable construction commutes with changes of coefficients and
stable Bockstein operations. It is unnecessary to assume that an
ordinary candidate \(G\) preserves a Pontryagin product or a
Dyer--Lashof operation; neither property is used or imposed here.

## Scope

There is therefore no contradiction available from the full suspended
source and the primitive Steenrod module of \(T\), at degree 16, 24,
or any higher bound. This conclusion does not depend on completing a
free-\(E_2\) primitive-basis enumeration in the target. The obstruction
to an actual map lies beyond the listed primary module and coalgebra
conditions.

The stable composite is not an actual map \(\Sigma^2A\to T\).
It does not furnish an extension of the unit or control its relative
homotopy choices, secondary operations, or iterated delooping data.
In particular it leaves the actual k4 extension question, the values
of \(\mu|_V\) on realizable relative maps, and the James--Hopf
image question for \(2c\) open.

The ingredients are the formal stable adjunction and the actual
generalized-Whitehead map of D.2.29, whose primary Arkowitz and CLM
sources were opened and checked there. No additional source theorem
or finite numerical certificate is needed for this boundary.
