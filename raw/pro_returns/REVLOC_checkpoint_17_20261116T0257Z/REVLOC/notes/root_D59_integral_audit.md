# Root audit of the integral-source refinement for D.2.59

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
16 November 2026, 02:45 UTC. Mathematical PASS.

Root previously read the degree-fourteen independence note, the complete
degree-fifteen double-bar quotient and the primary matrix certificate.
The present audit covers the new integral interface in
`I_integral_browder_lifts.md`, read in full, and the entire 98-line
`I_integral_browder_sources.py`, which root independently ran.

The map is an actual reduced based map Sigma(T smash T)->T. Translating
the circle of binary E2 operations by the inverse of its basepoint
product gives the displayed coproduct/antipode formula. The unary
operation contractions and the wedge cofibration allow it to descend.
Equivalently its double adjoint is the generalized Whitehead product
of the two evaluation maps Sigma²T->Y. This avoids incorrectly treating
the raw Browder bracket on nonprimitive labels as the induced reduced
map. The code uses the recursively computed antipode in the actual
Pontryagin algebra, not the antipode of the label space B.

The two source connectivities are seven and four, so both maps lift
uniquely to the four-connected cover E. Their final maps into L are
actual integral double suspensions. The earlier integral lift of the
double cohomology suspension of theta, and rational acyclicity, make
theta zero on every such integral image.

The degree-eight integral lift criterion uses H7(E;Z)=Z2. In degree
ten it uses the full group H9(E;Z)=Z8 plus (Z2)^3: first Bockstein
zero leaves only the possible connecting class4N, and the established
third Bockstein detects exactly that case. Thus the cited four
degree-ten combinations lift integrally; no inference from the first
Bockstein alone is made. Root checked the existing D22 statements of
both groups and both third Bocksteins.

The three displayed Tor chains have literal zero boundaries. Their
reductions are exactly a tensor B5, b tensor Ksum plus a tensor B4,
and d tensor h. The first reduction does not require a specified
mod-two representative of the integral N-cycle, because its coefficient
is four. The Ksum reduction follows directly from the first integral
connecting class. Thus there is no hidden Kunneth splitting choice.

The independent code run verifies all images in the actual cover edge
and then in the fourteen-relation quotient. The six source combinations
give respectively K5, K1+K2, K4, K3, K6 and K7. Their coordinates are
independent. The sixth uses both the tensor (d+e) tensor h and the Tor
cycle; it is not inferred from an individual integral lift of e.

The six directions are precisely the kernel of the nonzero functional
on the seven-dimensional primary source space. The integral primary
cycle of D52 lies outside that kernel because theta evaluates to one.
They therefore span all seven primary directions by reductions of
integral classes on L. This proves theta(K1)=theta(K2)=1 and zero on
the other five. It does not give integral lifts in E of K1 or K2, nor
stable sphericity merely from integral lifting. The separate D61
secondary differential proof is required for the stable conclusion.

Root subsequently read the complete released TeX at02:49UTC, including
the triangular degree14 test, bounded edge extension, all fourteen
double-bar relations, exact seven-dimensional primary kernel and every
integral-image formula. The sole literal correction requested was the
saved quotient basis range: the identifiers run01--33, not00--32.
The mathematical proof passes in full. Layout verification follows.
